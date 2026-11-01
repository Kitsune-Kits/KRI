"""Worker entrypoint — registers the bench triage workflow and serves.

Self-hosted workers must identify themselves with a stable DEPLOYMENT_NAME;
this entrypoint defaults it to kri-bench-triage before anything imports
the SDK, so a bare `make start-worker` is enough.
"""

import os

os.environ.setdefault("DEPLOYMENT_NAME", "kri-bench-triage")

import asyncio

import mistralai.workflows as workflows

from src.workflows.bench_triage import BenchTriageWorkflow


async def main() -> None:
    """Run the worker, serving kitsune-bench-triage until stopped."""
    await workflows.run_worker([BenchTriageWorkflow])


if __name__ == "__main__":
    asyncio.run(main())
