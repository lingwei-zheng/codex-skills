"""Search-only wrapper for the upstream Xiaohongshu CLI.

This file intentionally exposes only read-only commands. Keep the upstream
implementation in upstream_cli.py so future updates can be copied in without
re-opening publishing or interaction commands.
"""

from __future__ import annotations

import json
import os
import random
import subprocess
import sys
import time
from pathlib import Path

from run_lock import RunLock


ALLOWED_COMMANDS = {
    "check-login",
    "list-feeds",
    "search-feeds",
    "get-feed-detail",
    "user-profile",
}

THROTTLED_COMMANDS = {
    "list-feeds",
    "search-feeds",
    "get-feed-detail",
    "user-profile",
}

DEFAULT_DELAY_SECONDS = {
    "list-feeds": 5.0,
    "search-feeds": 8.0,
    "get-feed-detail": 12.0,
    "user-profile": 12.0,
}

DEFAULT_JITTER_SECONDS = 4.0

STATE_FILE = Path(os.environ.get("XHS_SEARCH_STATE_FILE", Path.home() / ".xhs" / "search_rate_limit.json"))

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


def _float_env(name: str, default: float) -> float:
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    try:
        return max(0.0, float(raw))
    except ValueError:
        print(f"[xhs-search] Ignoring invalid {name}={raw!r}; using {default}.", file=sys.stderr)
        return default


def _load_state() -> dict[str, float]:
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def _save_state(state: dict[str, float]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STATE_FILE)


def _rate_limit(command: str) -> None:
    if command not in THROTTLED_COMMANDS:
        return
    if os.environ.get("XHS_SEARCH_DISABLE_DELAY") == "1":
        return

    default_delay = DEFAULT_DELAY_SECONDS.get(command, 8.0)
    min_delay = _float_env("XHS_SEARCH_DELAY_SECONDS", default_delay)
    jitter = _float_env("XHS_SEARCH_JITTER_SECONDS", DEFAULT_JITTER_SECONDS)
    target_delay = min_delay + (random.uniform(0.0, jitter) if jitter else 0.0)

    state = _load_state()
    last_started = float(state.get("last_started_at", 0.0) or 0.0)
    elapsed = time.time() - last_started
    wait_seconds = max(0.0, target_delay - elapsed)

    if wait_seconds > 0:
        print(
            f"[xhs-search] Waiting {wait_seconds:.1f}s before {command} to reduce token/risk-control failures.",
            file=sys.stderr,
        )
        time.sleep(wait_seconds)

    state.update(
        {
            "last_started_at": time.time(),
            "last_command": command,
            "configured_delay_seconds": min_delay,
            "configured_jitter_seconds": jitter,
        }
    )
    _save_state(state)


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
    with RunLock():
        _rate_limit(command)
        completed = subprocess.run([sys.executable, str(upstream), *sys.argv[1:]], check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
