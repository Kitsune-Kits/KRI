"""Unit tests for the persona routing loop with a mocked agent caller."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from workflows.persona_router import (
    extract_route,
    run_routing,
)


def agent_reply(content, route=None):
    tool_calls = []
    if route:
        persona, note = route
        tool_calls.append(
            {
                "name": "route_to_persona",
                "arguments": {"persona": persona, "context_note": note},
            }
        )
    return {"content": content, "tool_calls": tool_calls}


def test_extract_route_ignores_other_functions():
    calls = [
        {"name": "other_function", "arguments": {"persona": "zaku"}},
        {
            "name": "route_to_persona",
            "arguments": {"persona": "piko", "context_note": "ask piko"},
        },
    ]
    assert extract_route(calls) == ("piko", "ask piko")


def test_extract_route_missing_persona():
    assert extract_route([{"name": "route_to_persona", "arguments": {}}]) is None


def make_scripted(responses):
    calls = []

    async def caller(agent, messages):
        calls.append((agent, [dict(m) for m in messages]))
        return responses.pop(0)

    return caller, calls


def test_no_route_returns_coco_reply():
    caller, calls = make_scripted([agent_reply("Direct answer from coco.")])
    result = __import__("asyncio").run(run_routing("hi", [], caller))
    assert result == "Direct answer from coco."
    assert [c[0] for c in calls] == ["coco-sensei"]


def test_coco_routes_to_cub_then_cub_routes_back():
    responses = [
        agent_reply("", route=("zaku", "talk like a robot")),
        agent_reply("Zaku speaks.", route=("coco", "please close")),
        agent_reply("Coco closes the loop."),
    ]
    caller, calls = make_scripted(responses)
    result = __import__("asyncio").run(run_routing("hi", [], caller))
    assert result == "Coco closes the loop."
    assert [c[0] for c in calls] == ["coco-sensei", "zaku", "coco-sensei"]
    zaku_messages = calls[1][1]
    assert zaku_messages[1]["content"].startswith("[Handoff from coco-sensei to zaku]")
    assert "talk like a robot" in zaku_messages[1]["content"]


def test_cub_cannot_route_to_another_cub():
    responses = [
        agent_reply("", route=("piko", "piko time")),
        agent_reply("", route=("coco", "please close")),
        agent_reply("Final."),
    ]
    caller, calls = make_scripted(responses)
    result = __import__("asyncio").run(run_routing("hi", [], caller))
    assert result == "Final."
    assert [c[0] for c in calls] == ["coco-sensei", "piko", "coco-sensei"]


def test_coco_invalid_persona_enum_stops():
    responses = [agent_reply("", route=("coco", "illegal self-route"))]
    caller, calls = make_scripted(responses)
    result = __import__("asyncio").run(run_routing("hi", [], caller))
    assert result == ""
    assert [c[0] for c in calls] == ["coco-sensei"]


def test_handoff_cap_returns_best_answer():
    responses = [
        agent_reply("", route=("zaku", "n1")),
        agent_reply("Zaku 1", route=("coco", "back for closing")),
        agent_reply("Coco closing (should not run)"),
    ]
    caller, calls = make_scripted(responses)
    result = __import__("asyncio").run(run_routing("hi", [], caller, max_handoffs=1))
    assert result == "Zaku 1"
    assert [c[0] for c in calls] == ["coco-sensei", "zaku"]


def test_history_is_passed_to_coco():
    caller, calls = make_scripted([agent_reply("ok")])
    history = [
        {"role": "user", "content": "earlier"},
        {"role": "assistant", "content": "reply"},
    ]
    __import__("asyncio").run(run_routing("new", history, caller))
    assert calls[0][1][:2] == history
    assert calls[0][1][2]["content"] == "new"
