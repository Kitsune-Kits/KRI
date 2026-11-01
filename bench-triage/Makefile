.PHONY: start-worker execute

# Start the worker locally (requires MISTRAL_API_KEY in the environment).
start-worker:
	uv run python -m src.entrypoints.worker

# Trigger one execution, e.g.:
#   make execute input='{"capture": "<verbatim capture text>", "mode": "triage"}'
execute:
	@uv run python -c "import os, json; from mistralai.client import Mistral; \
	e = Mistral(api_key=os.environ['MISTRAL_API_KEY']).workflows.execute_workflow( \
	workflow_identifier='kitsune-bench-triage', input=json.loads('$(input)')); \
	print(e.model_dump_json(indent=2))"
