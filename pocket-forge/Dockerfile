# syntax=docker/dockerfile:1.4
FROM python:3.12-slim

# Install uv
RUN pip install uv

# Set up a non-root user
RUN useradd -m -u 1000 agent && \
    mkdir -p /app && \
    chown agent:agent /app

WORKDIR /app

# Copy lockfile and project files
COPY pyproject.toml uv.lock ./

# Sync dependencies (frozen, no dev)
RUN uv sync --frozen --no-dev

# Copy the rest of the application
COPY . .

# Ensure correct ownership
RUN chown -R agent:agent /app

USER agent

CMD ["agents", "run-worker"]
