# Dockerfile for ecollege
FROM python:3.15-slim-trixie AS builder
# It is best practice to pin to a specific uv version like below:
COPY --from=ghcr.io/astral-sh/uv:0.13.8 /uv /uvx /bin/


# Environment variables to optimize Python performance
# Pin the Python version uv should use
#		UV_PYTHON=<PYTHON_VERSION>
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1 \
    UV_TOOL_BIN_DIR=/usr/local/bin

# UV_PYTHON=3.15

# Set working director
WORKDIR /app


# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
		uv sync --frozen --no-install-project

# Copy the project into the image
COPY . /app

#Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked


# Stage 2: Production stage
FROM python:3.15-slim-trixie AS runtime

WORKDIR /app

#RUN groupadd --system --gid 999 app && useradd --system --gid 999 --uid 999 --home-dir /app app

# Setup a non-root user
RUN groupadd --system --gid 999 app \
	&& useradd --system --gid 999 --uid 999 --home-dir /app --no-create-home app \
  && chown -R app:app . /app



# Copy the environment, but not the source code
#COPY --from=builder  /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app /app

ENV	PATH="/app/.venv/bin:$PATH" \
		PYTHONUNBUFFERED=1
		#DJANGO_SETTINGS_MODULE=campus.settings.local

# Expose the application port
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x entrypoint.prod.sh

USER app

## Set the entrypoint script
ENTRYPOINT ["/app/entrypoint.prod.sh"]