FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN pip install "mcp[cli]"

COPY server.py /app/server.py

CMD ["python", "server.py"]
