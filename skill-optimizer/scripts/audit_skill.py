#!/usr/bin/env python3
"""Audit skill folders for common bloat and structure problems."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from typing import Iterable


FORBIDDEN_DOCS = {
    "README.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
    "TODO.md",
    "NOTES.md",
}


def extract_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    parts = text.split("\n---\n", 1)
    if len(parts) < 2:
        return ""
    return parts[0]


def count_lines(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def normalized_lines(text: str) -> Iterable[str]:
    for line in text.splitlines():
        cleaned = re.sub(r"\s+", " ", line.strip().lower())
        if cleaned:
            yield cleaned


def has_yaml_key(frontmatter: str, key: str) -> bool:
    return any(line.startswith(f"{key}:") for line in frontmatter.splitlines())


def frontmatter_keys(frontmatter: str) -> set[str]:
    keys: set[str] = set()
    for line in frontmatter.splitlines():
        if ":" not in line:
            continue
        key = line.split(":", 1)[0].strip()
        if key and not key.startswith("#"):
            keys.add(key)
    return keys


def parse_simple_yaml(text: str) -> dict:
    """Parse the small YAML subset used by agents/openai.yaml."""
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue

        indent = len(line) - len(line.lstrip(" "))
        key, value = line.strip().split(":", 1)
        key = key.strip()
        value = value.strip()

        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if not value:
            node: dict = {}
            parent[key] = node
            stack.append((indent, node))
            continue

        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        parent[key] = value

    return root


def validate_openai_yaml(path: Path) -> list[str]:
    issues: list[str] = []
    data = parse_simple_yaml(path.read_text(encoding="utf-8"))
    interface = data.get("interface")
    if not isinstance(interface, dict):
        return ["agents/openai.yaml must contain an interface mapping"]

    for field in ("display_name", "short_description", "default_prompt"):
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"agents/openai.yaml interface.{field} must be a non-empty string")
    return issues


def audit_skill_dir(root: Path, profile: str = "strict") -> list[str]:
    issues: list[str] = []
    skill_md = root / "SKILL.md"

    if not skill_md.exists():
        issues.append("Missing SKILL.md")
    else:
        text = skill_md.read_text(encoding="utf-8")
        frontmatter = extract_frontmatter(text)
        keys = frontmatter_keys(frontmatter)
        if not has_yaml_key(frontmatter, "name") or not has_yaml_key(frontmatter, "description"):
            issues.append("SKILL.md frontmatter must include name and description")
        base_allowed = {"name", "description"}
        compat_allowed = {
            "metadata",
            "short-description",
            "allowed-tools",
            "argument-hint",
            "tools",
            "flags",
            "version",
            "author",
            "display_name",
            "license",
            "compatibility",
            "openclaw",
            "skillKey",
            "tags",
            "codex_adapter",
            "upstream_suite",
            "EXTERNAL_REVIEW",
            "HUMAN_CHECKPOINT",
            "COMPACT_MODE",
        }
        allowed = base_allowed if profile == "strict" else (base_allowed | compat_allowed)
        extra_keys = sorted(keys - allowed)
        if extra_keys:
            issues.append(f"SKILL.md frontmatter has extra fields: {', '.join(extra_keys)}")
        max_skill_lines = 220 if profile == "strict" else 1200
        if count_lines(skill_md) > max_skill_lines:
            issues.append("SKILL.md is long for a compact skill; move detail into references or scripts")

        lines = list(normalized_lines(text))
        dupes = [line for line, n in Counter(lines).items() if n > 1 and len(line) > 40]
        if dupes and profile == "strict":
            issues.append(f"Repeated lines detected: {min(len(dupes), 3)}+ likely duplicates")

    for name in FORBIDDEN_DOCS:
        if (root / name).exists():
            issues.append(f"Remove unnecessary document: {name}")

    openai_yaml = root / "agents" / "openai.yaml"
    if openai_yaml.exists():
        issues.extend(validate_openai_yaml(openai_yaml))

    refs = root / "references"
    if refs.exists():
        for path in refs.glob("*.md"):
            ref_text = path.read_text(encoding="utf-8")
            if count_lines(path) > 120 and not any(line.startswith("#") for line in ref_text.splitlines()[:20]):
                issues.append(f"{path.name} is long and lacks a clear top-level structure")
            if path.name.lower() in {"readme.md", "notes.md", "todo.md"}:
                issues.append(f"{path.name} is too human-centric for a skill reference")

    scripts = root / "scripts"
    if scripts.exists():
        for path in scripts.glob("*.py"):
            max_script_lines = 350 if profile == "strict" else 2000
            if count_lines(path) > max_script_lines:
                issues.append(f"{path.name} is large; consider splitting or simplifying")

    asset_dir = root / "assets"
    if asset_dir.exists() and not any(asset_dir.iterdir()):
        issues.append("assets/ exists but is empty; remove it unless you need it")

    return issues


def find_skill_dirs(root: Path) -> list[Path]:
    return sorted(path.parent for path in root.rglob("SKILL.md"))


def print_result(skill_dir: Path, issues: list[str]) -> None:
    if issues:
        print(f"[FAIL] {skill_dir}")
        for issue in issues:
            print(f"- {issue}")
    else:
        print(f"[OK] {skill_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", nargs="?", default=".", help="Path to a skill folder or a root directory")
    parser.add_argument("--all", action="store_true", help="Audit all skill folders under skill_dir")
    parser.add_argument(
        "--profile",
        choices=("strict", "compat"),
        default="strict",
        help="strict = compact OpenAI baseline, compat = allow common ecosystem extensions",
    )
    args = parser.parse_args()

    root = Path(args.skill_dir).resolve()
    if args.all:
        skill_dirs = find_skill_dirs(root)
        if not skill_dirs:
            print("Skill audit: NO SKILLS FOUND")
            return 1

        failed = 0
        for skill_dir in skill_dirs:
            issues = audit_skill_dir(skill_dir, profile=args.profile)
            print_result(skill_dir, issues)
            if issues:
                failed += 1

        passed = len(skill_dirs) - failed
        print(f"Skill audit summary: {passed} passed, {failed} failed, {len(skill_dirs)} total")
        return 1 if failed else 0

    issues = audit_skill_dir(root, profile=args.profile)
    if issues:
        print("Skill audit: NEEDS WORK")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Skill audit: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
