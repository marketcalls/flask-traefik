FROM python:3.9-slim

WORKDIR /app

# Install system dependencies and debugging tools
RUN apt-get update && apt-get install -y \
    curl \
    procps \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Set Python path
ENV PYTHONPATH=/app

# Change the CMD to use app.py instead of hello_world.py
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "120", "--workers", "3", "--log-level", "debug", "app:app"]