"""
main.py / pocket-forge / The front door of the Pocket Forge /
Copyright (c) 2026 Kitsune Kits. All rights reserved.

The interactive forge: the Architect speaks, the ensemble answers, and
every GitHub write waits for the Architect's word at the terminal.
`agent` is defined at module level so `agents chat` can load it too —
but run this file directly for the approval gates to be answered by hand:

    uv run --env-file .env python main.py
"""

import asyncio

from mistralai import agents

from forge.personas import build_forge_agent

# The forge. `agents chat` looks for this name.
agent = build_forge_agent()


# ────────────────────────────────────────────────────────────────────────
# MARK: - Approvals (the Architect's word)
# ────────────────────────────────────────────────────────────────────────

def architects_word(
    ctx: agents.ApprovalCallbackContext,
    request: agents.ApprovalRequest,
) -> agents.AllowApproval | agents.DenyApproval | agents.KeepCallbackOpen:
    """Allow the reads the policy already trusts; hold every write open
    for the Architect's hand."""
    annotations = getattr(request.tool, "annotations", None)
    if annotations is not None and getattr(annotations, "read_only_hint", False):
        return agents.AllowApproval()
    return agents.KeepCallbackOpen()


async def the_architects_word(
    callback: agents.OpenCallback,
) -> agents.AllowApproval | agents.DenyApproval:
    """Ask the Architect, at the terminal, for each gated write."""
    print(f"\n  ⏸  {callback.title}")
    print(f"     {callback.request.input}")
    while True:
        reply = (
            await asyncio.to_thread(input, "     the Architect's word? [y/N] ")
        ).strip().lower()
        if reply in {"y", "yes", "aye", "granted"}:
            return agents.AllowApproval()
        if reply in {"", "n", "no", "deny"}:
            return agents.DenyApproval()
        print("     answer y or n.")


# ────────────────────────────────────────────────────────────────────────
# MARK: - The session loop
# ────────────────────────────────────────────────────────────────────────

async def forge_session() -> None:
    """The forge, open: conversation in, passages out, writes gated."""
    session = await agent.start_session(on_approval=architects_word)
    print("🦊 The Pocket Forge is open. The Architect speaks; the forge answers.")
    print("   Reads run free; every GitHub write waits for your word.")
    print("   /exit closes the forge.")
    try:
        while True:
            try:
                message = await asyncio.to_thread(input, "\nArchitect> ")
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if message.strip().lower() in {"/exit", "exit", "quit"}:
                break
            if not message.strip():
                continue

            state = await session.run(message)
            while isinstance(state, agents.Blocked):
                turn = session.turn(state.turn_id)
                for callback in state.callbacks:
                    await turn.answer(callback.id, await the_architects_word(callback))
                state = await turn.result(after=state)

            match state:
                case agents.Completed(text=text):
                    print(f"\n{text}")
                case agents.Blocked():
                    pass
                case _:
                    print(f"\n(the turn stopped early: {state!r})")
    finally:
        await session.cancel()
        print("🦊 The forge sleeps. The Ledger keeps what was decided.")


if __name__ == "__main__":
    asyncio.run(forge_session())
