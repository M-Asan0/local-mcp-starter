import os
from pathlib import Path
from typing import List

from mcp.server.fastmcp import FastMCP

PROJECT_ROOT = Path(os.environ["PROJECT_ROOT"]).resolve()
SERVER_NAME = os.environ["MCP_SERVER_NAME"]

mcp = FastMCP(SERVER_NAME, json_response=True)


def _safe_join(relative_path: str) -> Path:
    """
    Resolve a relative path safely within the project root.
    Raises an exception if the path escapes the root (e.g., "../").
    """
    target = (PROJECT_ROOT / relative_path).resolve()
    if not str(target).startswith(str(PROJECT_ROOT)):
        raise ValueError("Path escapes project root")
    return target


@mcp.tool()
def list_project_files(subdir: str = ".") -> List[str]:
    """
    Retrieve all files located within the target project directory.

    subdir: A relative path under the project root to start scanning from.
    Returns: A list of file paths, each relative to the project root.
    """
    base = _safe_join(subdir)
    if not base.exists():
        return []

    files: List[str] = []
    for p in base.rglob("*"):
        if p.is_file():
            rel = p.relative_to(PROJECT_ROOT)
            files.append(str(rel))
    return files


@mcp.tool()
def read_project_file(path: str) -> str:
    """
    Return the contents of the specified file.

    path: A file path relative to the project root.
    """
    target = _safe_join(path)
    if not target.exists():
        return f"[ERROR] File not found: {path}"
    if target.is_dir():
        return f"[ERROR] {path} is a directory, not a file."

    # 文字コードはとりあえず utf-8 を想定
    return target.read_text(encoding="utf-8", errors="replace")


if __name__ == "__main__":
    # MCPクライアントとは stdio で通信
    mcp.run(transport="stdio")
