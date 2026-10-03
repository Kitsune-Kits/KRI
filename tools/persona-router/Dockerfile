FROM python:3.12-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml ./
RUN uv sync --no-dev --no-install-project

COPY src ./src
COPY worker.py ./
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "-m", "entrypoints.worker"]
