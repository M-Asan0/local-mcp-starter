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

### ✔ `read_project_file(path)`
Reads the content of a file relative to the project root.

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
git clone https://github.com/M-Asan0/local-mcp-starter.git
cd local-mcp-starter
```

---

## 2. Create your `.env`

All user‑specific configuration is handled here:

```env
HOST_PROJECT_PATH=/home/yourname/your-project
CONTAINER_PROJECT_PATH=/workspace/target-project
PROJECT_ROOT=/workspace/target-project
MCP_SERVER_NAME=local-mcp-starter
MCP_IMAGE_NAME=local-mcp-starter
```

---

## 3. Build the Docker image

```bash
set -a
. .env
set +a
docker build -t ${MCP_IMAGE_NAME} .
```

Rebuild if you modify `server.py` or Dockerfile.

---

# 🖥 MCP Configuration (Cursor / WSL example)
 Assume you cloned the repo under $HOME/local-mcp-starter.If you use a different location, update the cd path accordingly.

 `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "local-mcp-starter": {
      "command": "wsl",
      "args": [
        "bash",
        "-lc",
        "$HOME/local-mcp-starter/run-for-MCP-client.sh"
      ]
    }
  }
}

```

---

# 🧪 Usage Examples (Cursor)

### List files

```
Run tool local-project-filesystem.list_project_files with {"subdir":"<path-to-the-directory-you-want-to-scan>"}
```

### Read a file

```
Run tool local-project-filesystem.read_project_file with {"path":"<path-to-the-file-you-want-to-read>"}
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