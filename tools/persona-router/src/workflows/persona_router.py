"""Persona router workflow: coco-sensei routes conversations to zaku, piko, or nui."""

import json
import os
from collections.abc import Awaitable, Callable
from typing import Any, cast

from mistralai import workflows
from mistralai.workflows.plugins.mistralai import get_mistral_client
from pydantic import BaseModel

COCO = "coco-sensei"
CUBS = ("zaku", "piko", "nui")
MAX_HANDOFFS = 6
ROUTE_FUNCTION = "route_to_persona"

History = list[dict[str, str]]
AgentResult = dict[str, Any]
AgentCaller = Callable[[str, list[dict[str, Any]]], Awaitable[AgentResult]]


class PersonaRouterInput(BaseModel):
    message: str
    history: list[dict[str, str]] = []


@workflows.activity()
async def call_agent(agent: str, messages: list[dict[str, Any]]) -> AgentResult:
    client = get_mistral_client()
    agent_id = os.environ.get(f"AGENT_ID_{agent.upper().replace('-', '_')}", agent)
    response = await client.agents.complete_async(
        agent_id=agent_id, messages=cast("Any", messages)
    )
    choice = response.choices[0]
    tool_calls: list[dict[str, Any]] = []
    message = choice.message
    if message is not None:
        for tc in message.tool_calls or []:
            try:
                arguments = json.loads(str(tc.function.arguments or "{}"))
            except (json.JSONDecodeError, TypeError):
                arguments = {}
            tool_calls.append({"name": tc.function.name, "arguments": arguments})
    content = message.content if message is not None else None
    return {"content": content or "", "tool_calls": tool_calls}


def extract_route(tool_calls: list[dict[str, Any]]) -> tuple[str, str] | None:
    for tc in tool_calls:
        if tc.get("name") != ROUTE_FUNCTION:
            continue
        arguments = tc.get("arguments") or {}
        persona = arguments.get("persona")
        if persona:
            return normalize_persona(persona), arguments.get("context_note") or ""
    return None


def normalize_persona(persona: str) -> str:
    return COCO if persona == "coco" else persona


def _handoff_message(
    persona: str, context_note: str, from_agent: str
) -> dict[str, str]:
    note = context_note.strip()
    prefix = f"[Handoff from {from_agent} to {persona}]"
    return {"role": "user", "content": f"{prefix} {note}".strip()}


async def run_routing(
    message: str,
    history: History,
    agent_caller: AgentCaller = call_agent,
    max_handoffs: int = MAX_HANDOFFS,
) -> str:
    messages: list[dict[str, Any]] = [dict(m) for m in history]
    messages.append({"role": "user", "content": message})

    agent = COCO
    best_answer = ""
    handoffs = 0
    from_cub_to_coco = False

    while True:
        result = await agent_caller(agent, messages)
        content = (result.get("content") or "").strip()
        if content:
            best_answer = content
            messages.append({"role": "assistant", "content": content})

        if from_cub_to_coco:
            return best_answer

        route = extract_route(result.get("tool_calls") or [])
        if route is None:
            return best_answer

        persona, context_note = route
        if handoffs >= max_handoffs:
            return best_answer
        handoffs += 1

        if agent == COCO:
            if persona not in CUBS:
                return best_answer
        else:
            if persona != COCO:
                return best_answer
            from_cub_to_coco = True

        messages.append(_handoff_message(persona, context_note, agent))
        agent = persona


@workflows.workflow.define(
    name="persona-router",
    workflow_display_name="Persona Router",
    workflow_description=(
        "Routes each user message through coco-sensei, who may hand off to "
        "zaku, piko, or nui via route_to_persona; a cub hands back to coco "
        "for a final binding reply."
    ),
)
class PersonaRouterWorkflow:
    @workflows.workflow.entrypoint
    async def run(self, input: PersonaRouterInput) -> str:
        return await run_routing(input.message, input.history)
