#!/bin/bash
set -e

cd "$(dirname "$0")"

# .env 読み込み
set -a
source .env
set +a

# Docker MCP サーバー起動
docker run --rm -i \
  -v "$HOST_PROJECT_PATH:$CONTAINER_PROJECT_PATH:ro" \
  -e PROJECT_ROOT \
  -e MCP_SERVER_NAME \
  "$MCP_IMAGE_NAME"