#!/usr/bin/env python3
"""Resolve the user's journal targeting reference with relative paths first."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Iterable


FILENAME = "journal_ai_reference.md"
WINDOWS_FALLBACK = Path(
    r"D:\OneDrive\Literatures\others\journal_ai_reference.md"
)


def normalized(path: Path) -> Path:
    return path.expanduser().resolve(strict=False)


def candidate_paths(
    project_root: Path,
    explicit: str | None = None,
    configured: str | None = None,
    env_value: str | None = None,
    include_windows_fallback: bool = True,
) -> Iterable[tuple[str, Path]]:
    root = normalized(project_root)

    for source, value in (("explicit", explicit), ("project-config", configured)):
        if value:
            path = Path(value).expanduser()
            yield source, normalized(path if path.is_absolute() else root / path)

    for relative in (
        FILENAME,
        f"others/{FILENAME}",
        f"../others/{FILENAME}",
        f"../../others/{FILENAME}",
    ):
        yield "relative", normalized(root / relative)

    for ancestor in (root, *root.parents):
        if ancestor.name.casefold() == "literatures":
            yield "Literatures-ancestor", normalized(
                ancestor / "others" / FILENAME
            )
            break

    if env_value:
        yield "environment", normalized(Path(env_value))

    if include_windows_fallback and os.name == "nt":
        yield "Windows-fallback", normalized(WINDOWS_FALLBACK)


def display_path(path: Path, project_root: Path) -> str:
    try:
        return os.path.relpath(path, normalized(project_root))
    except ValueError:
        return FILENAME


def resolve_reference(
    project_root: Path,
    explicit: str | None = None,
    configured: str | None = None,
    env_value: str | None = None,
    include_windows_fallback: bool = True,
) -> dict:
    seen: set[str] = set()
    attempted = 0
    for source, path in candidate_paths(
        project_root,
        explicit=explicit,
        configured=configured,
        env_value=env_value,
        include_windows_fallback=include_windows_fallback,
    ):
        key = os.path.normcase(str(path))
        if key in seen:
            continue
        seen.add(key)
        attempted += 1
        if path.is_file() and os.access(path, os.R_OK):
            modified = datetime.fromtimestamp(path.stat().st_mtime).astimezone()
            return {
                "status": "loaded",
                "source": source,
                "path": str(path),
                "display_path": display_path(path, project_root),
                "modified_at": modified.isoformat(timespec="seconds"),
            }

    return {
        "status": "not_found",
        "source": None,
        "path": None,
        "display_path": None,
        "modified_at": None,
        "attempted_candidates": attempted,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--explicit")
    parser.add_argument(
        "--configured",
        help="paths.journal_reference from .codex/project.yaml",
    )
    args = parser.parse_args()

    result = resolve_reference(
        Path(args.project_root),
        explicit=args.explicit,
        configured=args.configured,
        env_value=os.environ.get("CODEX_JOURNAL_REFERENCE"),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "loaded" else 1


if __name__ == "__main__":
    raise SystemExit(main())
