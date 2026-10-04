FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

EXPOSE 5000

CMD ["uv", "run", "--no-sync", "mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]
