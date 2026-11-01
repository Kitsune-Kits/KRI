"""Worker entrypoint — mirrors the scaffolded project's generated file.

Discovers workflow classes under ``src/workflows`` and hands them to
``run_worker()``, which registers the workflows and starts serving
executions. If the deploy build rejects this file's shape, regenerate it
with ``uvx mistralai-workflows-cli@latest setup`` and keep only
``src/workflows/bench_triage.py`` — it is scaffold-independent.
"""

import asyncio

import mistralai_workflows

# Importing the workflow modules registers their classes for discovery.
import src.workflows.bench_triage  # noqa: F401


async def main() -> None:
    """Discover workflows in src/workflows and run the worker until stopped."""
    discovered = mistralai_workflows.discover_workflows()
    await mistralai_workflows.run_worker(discovered)


if __name__ == "__main__":
    asyncio.run(main())
