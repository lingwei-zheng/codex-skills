#!/usr/bin/env python3
"""Install synced Codex skills from this repository into ~/.codex/skills."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


PLATFORM_EXCLUDES = {
    "macos": {"docx"},
    "windows": set(),
}

EXCLUDED_PATH_PARTS = {"adapters"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install synced skills from this repository into CODEX_HOME/skills."
    )
    parser.add_argument(
        "--platform",
        choices=sorted(PLATFORM_EXCLUDES),
        required=True,
        help="Target platform profile.",
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to the skills sync repository root.",
    )
    parser.add_argument(
        "--codex-home",
        type=Path,
        default=Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser(),
        help="Codex home directory. Defaults to $CODEX_HOME or ~/.codex.",
    )
    return parser.parse_args()


def should_skip_path(skill_dir: Path, source_root: Path) -> bool:
    relative_parts = skill_dir.relative_to(source_root).parts
    return any(part in EXCLUDED_PATH_PARTS for part in relative_parts)


def discover_skills(source_root: Path) -> dict[str, Path]:
    discovered: dict[str, Path] = {}
    duplicates: dict[str, list[Path]] = {}

    for skill_md in sorted(source_root.rglob("SKILL.md")):
        skill_dir = skill_md.parent

        if ".git" in skill_dir.parts or should_skip_path(skill_dir, source_root):
            continue

        skill_name = skill_dir.name
        if skill_name in discovered:
            duplicates.setdefault(skill_name, [discovered[skill_name]]).append(skill_dir)
            continue

        discovered[skill_name] = skill_dir

    if duplicates:
        lines = ["Duplicate skill names found:"]
        for name, paths in sorted(duplicates.items()):
            lines.append(f"- {name}:")
            for path in paths:
                lines.append(f"  - {path}")
        raise SystemExit("\n".join(lines))

    return discovered


def sync_skill(src: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    codex_home = args.codex_home.resolve()
    skills_root = codex_home / "skills"
    skills_root.mkdir(parents=True, exist_ok=True)

    discovered = discover_skills(source_root)
    excludes = PLATFORM_EXCLUDES[args.platform]
    installed: list[str] = []
    removed: list[str] = []

    for skill_name, src_dir in sorted(discovered.items()):
        dest_dir = skills_root / skill_name
        if skill_name in excludes:
            if dest_dir.exists():
                shutil.rmtree(dest_dir)
                removed.append(skill_name)
            print(f"Skipped {skill_name} for {args.platform}")
            continue

        sync_skill(src_dir, dest_dir)
        installed.append(skill_name)
        print(f"Installed {skill_name} -> {dest_dir}")

    if removed:
        print("")
        print("Removed excluded skills:")
        for name in removed:
            print(f"- {name}")

    print("")
    print(f"Done. Synced {len(installed)} skills into {skills_root}")
    print("Restart Codex to pick up new skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
