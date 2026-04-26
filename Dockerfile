# Dockerfile for ecollege
FROM python:3.13.3-slim-bookworm AS build

# Environment variables to optimize Python performance
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create the app directory
#RUN mkdir /app

# Install dependencies
RUN apt-get update && apt-get install -y gcc 

# Set working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Stage 2: Production stage
FROM python:3.13.3-slim-bookworm

RUN useradd -m -r appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

COPY --from=build /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Set working directory
WORKDIR /app

# Copy the application code
COPY  --chown=appuser:appuser . .

# Environment variables to optimize Python performance
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.prod.sh

ENV DJANGO_SETTINGS_MODULE=capstone.settings.local

# Set the entrypoint script
ENTRYPOINT ["/app/entrypoint.prod.sh"]
