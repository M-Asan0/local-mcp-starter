
# local-mcp-starter（ローカル MCP スターター）

**local-mcp-starter** は、任意のローカルプロジェクトを  
**Cursor / ChatGPT Desktop / Claude Desktop** などの MCP 対応クライアントから  
安全に参照できるようにする **汎用ローカル MCP サーバー** です。

- 🔧 **どんな言語・フレームワークにも対応**
- 🔒 **read-only で安全**
- ⚙️ **設定は `.env` に集約**
- 🐳 **Docker コンテナで隔離実行**
- 🔌 **Cursor / Claude Desktop で使用可能**
  （ChatGPT Desktop はまだローカル MCP 非対応）

---

## ✨ 機能

### ✔ `list_project_files(subdir=".")`
指定ディレクトリ以下の全ファイルを再帰的に取得。

例：

```
Run tool local-project-filesystem.list_project_files with {"subdir":"<your/path/here>"}
```

---

### ✔ `read_project_file(path)`
指定ファイルの内容を返す。

例：

```
Run tool local-project-filesystem.read_project_file with {"path":"<your/file/here>"}
```

---

# 📁 ディレクトリ構成

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

# 📦 インストール手順

## 1. リポジトリ取得

```bash
cd ~
git clone https://github.com/M-Asan0/local-mcp-starter.git
cd local-mcp-starter
```

---

## 2. `.env` を作成

```env
HOST_PROJECT_PATH=/home/yourname/your-project
CONTAINER_PROJECT_PATH=/workspace/target-project
PROJECT_ROOT=/workspace/target-project
MCP_SERVER_NAME=local-mcp-starter
MCP_IMAGE_NAME=local-mcp-starter
```

---

## 3. Docker イメージをビルド

```bash
docker build -t ${MCP_IMAGE_NAME} .
```

---

# 🖥 Cursor（WSL）での MCP 設定

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

# 🧪 Cursor での使用例

### ファイル一覧取得

```
Run tool local-project-filesystem.list_project_files with {"subdir":"src"}
```

### ファイル内容の読み取り

```
Run tool local-project-filesystem.read_project_file with {"path":"src/main.ts"}
```

### AI に MCP を使わせるテンプレート

```
必要に応じて以下の MCP ツールを使用して調査してください：

- local-project-filesystem.list_project_files
- local-project-filesystem.read_project_file

問題の原因を特定し、修正版を提示してください。
```

---

# 📜 ライセンス

MIT License  
Copyright (c) 2025
