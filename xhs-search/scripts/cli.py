"""Search-only wrapper for the upstream Xiaohongshu CLI.

This file intentionally exposes only read-only commands. Keep the upstream
implementation in upstream_cli.py so future updates can be copied in without
re-opening publishing or interaction commands.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


ALLOWED_COMMANDS = {
    "check-login",
    "list-feeds",
    "search-feeds",
    "get-feed-detail",
    "user-profile",
}

BLOCKED_EXAMPLES = [
    "publish",
    "publish-video",
    "fill-publish",
    "fill-publish-video",
    "click-publish",
    "save-draft",
    "long-article",
    "select-template",
    "next-step",
    "post-comment",
    "reply-comment",
    "like-feed",
    "favorite-feed",
    "delete-cookies",
    "phone-login",
    "send-code",
    "verify-code",
]


def _print_blocked(command: str) -> int:
    payload = {
        "success": False,
        "error": "Command is blocked by the search-only Xiaohongshu skill.",
        "command": command,
        "allowed_commands": sorted(ALLOWED_COMMANDS),
        "blocked_examples": BLOCKED_EXAMPLES,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 2


def main() -> int:
    preferred_python = Path(os.environ.get("XHS_SEARCH_PYTHON", r"D:\Anaconda\envs\codex_py311\python.exe"))
    if sys.version_info < (3, 11) and preferred_python.exists():
        completed = subprocess.run([str(preferred_python), __file__, *sys.argv[1:]], check=False)
        return completed.returncode

    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help"}:
        print("Search-only Xiaohongshu CLI")
        print("Allowed commands:")
        for command in sorted(ALLOWED_COMMANDS):
            print(f"  {command}")
        print()
        print("Use: python scripts\\cli.py <allowed-command> [args...]")
        return 0

    command = sys.argv[1]
    if command not in ALLOWED_COMMANDS:
        return _print_blocked(command)

    upstream = Path(__file__).with_name("upstream_cli.py")
    completed = subprocess.run([sys.executable, str(upstream), *sys.argv[1:]], check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
