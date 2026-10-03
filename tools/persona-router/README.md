# persona-router

A Mistral Workflows project that routes each user message through a persona
agent chain: **coco-sensei** → (**zaku** | **piko** | **nui**) → **coco-sensei**.

## Logic

1. Every user message (plus full conversation history) goes to `coco-sensei`.
2. If she calls `route_to_persona(persona, context_note)`, the conversation —
   including a `[Handoff from X to Y] <context_note>` message — goes to that
   cub (`zaku`, `piko`, or `nui`).
3. If the cub calls `route_to_persona(persona: "coco", ...)`, the conversation
   returns to `coco-sensei` exactly once for a short closing binding reply,
   which is returned as the final markdown answer.
4. If coco makes no route call, her reply is the final answer directly.
5. Handoffs are capped at 6 per user message; the best answer so far is
   returned if the cap is hit. Invalid personas (e.g. coco routing to "coco",
   or a cub routing to another cub) end the loop with the best answer so far.

## Setup

```bash
uv sync
# put your real MISTRAL_API_KEY in .env (already gitignored)
```

`.env` is loaded automatically by the worker entrypoint (`dotenv`).

Optional env overrides if your Studio agent IDs differ from the agent names:

```
AGENT_ID_COCO_SENSEI=<agent-id-or-name>
AGENT_ID_ZAKU=<agent-id-or-name>
AGENT_ID_PIKO=<agent-id-or-name>
AGENT_ID_NUI=<agent-id-or-name>
```

## Test

```bash
uv run pytest tests/ -q          # routing loop unit tests (mocked agent calls)
make check                        # ruff + mypy + semgrep workflow lint
```

## Run locally

```bash
make start-worker                 # registers persona-router + hello-world
make execute workflow=persona-router input='{"message": "Hi!", "history": []}'
```

## Deployment

Managed Mistral deployments clone the repo via the Mistral GitHub App
(GitHub only). Since this project lives on GitLab, the native path is a
self-managed worker:

1. Build and run the Docker image locally or on your own infra
   (`docker build -t persona-router . && docker run --env-file .env persona-router`).
2. The worker connects outbound to Mistral and registers `persona-router`.
3. Trigger executions from Studio, or via `make execute`.

Alternatively, mirror the repo to GitHub and use a managed deployment.
