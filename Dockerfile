FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ./uv.lock ./uv.lock
COPY ./pyproject.toml ./pyproject.toml

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

RUN uv sync --locked --no-dev

COPY ./src ./src

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]