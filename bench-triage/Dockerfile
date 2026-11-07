# Managed deployment image for the kitsune bench triage worker.
# Mirrors the scaffolded project's Dockerfile intent: install the project,
# run the worker entrypoint. The platform injects the service-account
# token at runtime — never bake an API key into this image.
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY pyproject.toml ./
COPY src ./src

RUN pip install --no-cache-dir .

CMD ["python", "-m", "src.entrypoints.worker"]
