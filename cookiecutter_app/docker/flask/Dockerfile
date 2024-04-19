FROM python:3.12.2-slim-bookworm

WORKDIR /app

RUN apt-get update &&  \
    apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ../../requirements /app/requirements
RUN pip install --no-cache-dir -r /app/requirements/local.txt

COPY .. /app/
