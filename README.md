# local-mcp-starter

A fully generic, environment‑variable–driven **local MCP server** that allows  
Cursor / ChatGPT Desktop / Claude Desktop (MCP‑enabled clients)  
to safely inspect any local project on your machine.

This starter is designed to be:

- 🔧 **Project‑agnostic** — works with any language or framework  
- 🔒 **Read‑only and safe** — no write access to your files  
- ⚙️ **Fully configurable via `.env`**  
- 🐳 **Runs inside Docker** for isolation  
- 🔌 **Usable with Cursor / Claude Desktop**  
  (ChatGPT Desktop does not support local MCP yet)

---

## ✨ Features

### ✔ `list_project_files(subdir=".")`
Recursively returns all file paths under the specified subdirectory.

Example:

```
Run tool local-project-filesystem.list_project_files with {"subdir":"<your/path/here>"}
```

### ✔ `read_project_file(path)`
Reads the content of a file relative to the project root.

Example:

```
Run tool local-project-filesystem.read_project_file with {"path":"<your/file/here>"}
```

---

# 📁 Directory Structure

```
local-mcp-starter/
│
├── Dockerfile
├── server.py
├── requirements.txt
├── .env.example
├── README.md
├── README_JP.md
└── LICENSE
```

---

# 📦 Installation

## 1. Clone the repository

```bash
cd ~
git clone https://github.com/yourname/local-mcp-starter.git
cd local-mcp-starter
```

---

## 2. Create your `.env`

All user‑specific configuration is handled here:

```env
HOST_PROJECT_PATH=/home/yourname/your-project
CONTAINER_PROJECT_PATH=/workspace/target-project
PROJECT_ROOT=/workspace/target-project
MCP_SERVER_NAME=local-project-filesystem
MCP_IMAGE_NAME=local-mcp-starter
```

---

## 3. Build the Docker image

```bash
docker build -t ${MCP_IMAGE_NAME} .
```

Rebuild if you modify `server.py` or Dockerfile.

---

# 🖥 MCP Configuration (Cursor / WSL example)

`~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "local-mcp-starter": {
      "command": "wsl",
      "args": [
        "bash",
        "-lc",
        "cd /home/you/local-mcp-starter && set -a && . .env && set +a && docker run --rm -i -v ${HOST_PROJECT_PATH}:${CONTAINER_PROJECT_PATH}:ro -e PROJECT_ROOT=${PROJECT_ROOT} -e MCP_SERVER_NAME=${MCP_SERVER_NAME} ${MCP_IMAGE_NAME}"
      ]
    }
  }
}

```

---

# 🧪 Usage Examples (Cursor)

### List files

```
Run tool local-project-filesystem.list_project_files with {"subdir":"src"}
```

### Read a file

```
Run tool local-project-filesystem.read_project_file with {"path":"src/utils/helpers.ts"}
```

### Ask the AI to use MCP

```
If needed, use these MCP tools:

- local-project-filesystem.list_project_files
- local-project-filesystem.read_project_file

Investigate the issue and provide a fix.
```

---

# 📝 License

MIT License  
Copyright (c) 2025