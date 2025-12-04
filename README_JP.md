[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://hub.docker.com/_/python)
[![FastMCP](https://img.shields.io/badge/FastMCP-1.22.0-green.svg)](https://pypi.org/project/mcp/)
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

### ✔ `read_project_file(path)`
指定ファイルの内容を返す。

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
set -a
. .env
set +a
docker build -t ${MCP_IMAGE_NAME} .
```

---

# 🖥 MCP 設定
~/local-mcp-starterにgit cloneすることを想定しています。
もし別のパスにgit cloneしたのであれば、 「$HOME/local-mcp-starter」をそのパスに書き換えてください。

### 4-1. Cursor

### 操作説明
#### 1. Cursor を開く
Cursor を起動します。
#### 2. 設定画面を開く
`Shift + Ctrl + P` を押してコマンドパレットを開き、  
`settings` と入力して **Cursor Settings** を選択します。
#### 3. Tools & MCP を開く
設定画面左のメニューから **Tools & MCP** を選びます。
#### 4. Custom MCP の追加
**Add custom MCP** ボタンを押すと`mcp.json`が開きます。
#### 5. MCP 設定を追加する
開いたファイルに、下記の内容を貼り付けて保存します。
#### 6. MCP サーバーを有効化する
設定画面の Tools & MCP タブに戻り、
一覧に表示された local-mcp-starter のスイッチをオンにしてスイッチが緑になれば成功です。

### Windwos/WSL
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

### macOS 
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

### Linux
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

### 操作説明

#### 1. Claude for Desktop を起動する
アプリを起動します。

#### 2. 設定を開く
左上のメニューから **設定（Settings）** を開きます。

#### 3. 「開発者」メニューを開く
設定画面左のリストから **開発者（Developer）** を選択します。

#### 4. 設定ファイルを開く
**「設定を編集（Edit Config）」** ボタンを押すと、  
`claude_desktop_config.json` が置かれているフォルダが開きます。

#### 5. MCP 設定を追加する
開いた JSON ファイルに、下記を参考に設定を追加して保存します。

6. Claude for Desktop を再起動する
※ 右上の「×」で閉じるだけではバックグラウンドでプロセスが残るため、
Windowsではタスクマネージャーから完全終了させてください。
アプリを再起動すると設定が読み込まれます

7. MCP サーバーが認識されているか確認する
チャット画面に戻り、画面下部の 「検索とツール（Search & Tools）」 に
local-mcp-starter が表示され、スイッチが オン（緑） になっていれば成功です。

### Windwos/WSL 
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

### macOS 
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

### Linux
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

# 🧪 Cursor での使用例

### ファイル一覧取得

```
Run tool local-project-filesystem.list_project_files with {"subdir":"<path-to-the-directory-you-want-to-scan>"}
```

### ファイル内容の読み取り

```
Run tool local-project-filesystem.read_project_file with {"path":"<path-to-the-file-you-want-to-read>"}
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
