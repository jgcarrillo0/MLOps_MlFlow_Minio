FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --group api --no-install-project

COPY api ./api
COPY src ./src

ENV PYTHONPATH=/workspace

EXPOSE 8025

CMD ["uv", "run", "--no-sync", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8025"]
