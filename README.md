
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://hub.docker.com/_/python)
[![FastMCP](https://img.shields.io/badge/FastMCP-1.22.0-green.svg)](https://pypi.org/project/mcp/)
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

## 4. 🖥 MCP Configuration
 Assume you cloned the repo under $HOME/local-mcp-starter.If you use a different location, update the cd path accordingly.

### 4-1. Cursor

### Setup Instructions
#### 1. Launch Cursor
Open the Cursor editor.

#### 2. Open the Settings Panel
Press `Shift + Ctrl + P` to open the command palette,  
type `settings`, and select **Cursor Settings**.

#### 3. Open the “Tools & MCP” Section
In the left sidebar of the settings window, select **Tools & MCP**.

#### 4. Add a Custom MCP Server
Click the **Add custom MCP** button.  
This will open your `mcp.json` file.

#### 5. Add Your MCP Configuration
Paste the following configuration into the opened file and save it:

#### Windwos/WSL 
`%USERPROFILE%\.cursor\mcp.json` 
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

#### macOS 
`~/.cursor/mcp.json`

`<project-directory>/.cursor/mcp.json`
```json
{
  "mcpServers": {
    "local-mcp-starter": {
      "command": "bash",
      "args": [
        "-lc",
        "$HOME/local-mcp-starter/run-for-MCP-client.sh"
      ]
    }
  }
}
```

#### Linux
`~/.cursor/mcp.json`

`<project-directory>/.cursor/mcp.json`
```json
{
  "mcpServers": {
    "local-mcp-starter": {
      "command": "bash",
      "args": [
        "-lc",
        "$HOME/local-mcp-starter/run-for-MCP-client.sh"
      ]
    }
  }
}
```
### 4-2. Claude Desktop

### Setup Instructions

#### 1. Launch Claude for Desktop
Open the application.

#### 2. Open the Settings Menu
Click the menu in the top-left corner and select **Settings**.

#### 3. Open the “Developer” Section
In the left sidebar of the settings window, select **Developer**.

#### 4. Open the Configuration File
Click **Edit Config**.  
This will open the folder containing `claude_desktop_config.json`.

#### 5. Add Your MCP Configuration
Paste and adjust the following content inside the JSON file, then save it:

#### 6. Restart Claude for Desktop
Note: Simply clicking “X” does not fully exit the app.
On Windows, use Task Manager to fully terminate the process.
After restarting Claude for Desktop, the configuration will be reloaded.

#### 7. Verify That the MCP Server Is Enabled
Return to the chat window.
At the bottom (“Search & Tools”), you should see local-mcp-starter listed.
If the switch is ON (green), the MCP server is successfully connected.

#### Windwos/WSL 
`%APPDATA%\Claude\claude_desktop_config.json`
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
  },
  "isDxtAutoUpdatesEnabled": true,
  "preferences": {
    "menuBarEnabled": false,
    "legacyQuickEntryEnabled": false
  }
}
```

#### macOS 
`/Users/<USERNAME>/Library/Application Support/Claude/claude_desktop_config.json`
```json
{
  "mcpServers": {
    "local-mcp-starter": {
      "command": "bash",
      "args": [
        "-lc",
        "$HOME/local-mcp-starter/run-for-MCP-client.sh"
      ]
    }
  },
  "isDxtAutoUpdatesEnabled": true,
  "preferences": {
    "menuBarEnabled": false,
    "legacyQuickEntryEnabled": false
  }
}
```

#### Linux 
`/home/<USERNAME>/.config/Claude/claude_desktop_config.json` 
```json
{
  "mcpServers": {
    "local-mcp-starter": {
      "command": "bash",
      "args": [
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