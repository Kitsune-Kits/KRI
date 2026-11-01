"""Worker entrypoint — registers the bench triage workflow and serves.

Passes the workflow class directly to run_worker() from the Workflows
SDK (mistralai.workflows), which registers it in the workspace and
starts serving executions.
"""

import asyncio

import mistralai.workflows as workflows

from src.workflows.bench_triage import BenchTriageWorkflow


async def main() -> None:
    """Run the worker, serving kitsune-bench-triage until stopped."""
    await workflows.run_worker([BenchTriageWorkflow])


if __name__ == "__main__":
    asyncio.run(main())
