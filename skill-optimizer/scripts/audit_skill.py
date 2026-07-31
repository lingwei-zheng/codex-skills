#!/usr/bin/env python3
"""Audit skill folders for common bloat and structure problems."""

from __future__ import annotations

import argparse
import ast
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

try:
    import yaml
except ImportError:  # pragma: no cover - keeps the script usable in bare Python envs.
    yaml = None


FORBIDDEN_DOCS = {
    "README.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
    "TODO.md",
    "NOTES.md",
}


def extract_frontmatter(text: str) -> str:
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return ""
    parts = normalized.split("\n---\n", 1)
    if len(parts) < 2:
        return ""
    return parts[0].removeprefix("---\n")


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


def validate_skill_frontmatter(frontmatter: str) -> tuple[dict, list[str]]:
    """Strictly validate SKILL.md YAML frontmatter.

    Codex slash discovery depends on valid YAML. Plain string scans can miss
    invalid descriptions such as `read-only: it must...`, where the colon starts
    an accidental mapping and causes the whole skill to be skipped.
    """
    issues: list[str] = []
    if not frontmatter.strip():
        return {}, ["SKILL.md must start with YAML frontmatter delimited by ---"]

    if yaml is None:
        if re.search(r"^[A-Za-z0-9_-]+: .+?:\s+", frontmatter, flags=re.MULTILINE):
            issues.append(
                "SKILL.md frontmatter may contain an unquoted colon; use a quoted string or >- block scalar"
            )
        parsed = {key: True for key in frontmatter_keys(frontmatter)}
        return parsed, issues

    try:
        parsed = yaml.safe_load(frontmatter)
    except Exception as exc:
        return {}, [
            f"SKILL.md frontmatter is not valid YAML: {type(exc).__name__}: {exc}",
            "Use quoted strings or `description: >-` when the description contains `: `.",
        ]

    if not isinstance(parsed, dict):
        return {}, ["SKILL.md frontmatter must parse to a YAML mapping"]

    for key in ("name", "description"):
        value = parsed.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"SKILL.md frontmatter.{key} must be a non-empty string")
    return parsed, issues


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


def script_validation_files(root: Path) -> list[Path]:
    patterns = (
        "test_*.py",
        "*_test.py",
        "validate_*.py",
        "check_*.py",
        "verify_*.py",
        "test_*.ps1",
        "validate_*.ps1",
        "validate-*.ps1",
        "check_*.ps1",
        "check-*.ps1",
        "verify_*.ps1",
        "verify-*.ps1",
    )
    found: set[Path] = set()
    for pattern in patterns:
        found.update(root.rglob(pattern))
    return sorted(path for path in found if ".git" not in path.parts)


def python_script_issues(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")

    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        return [f"{path.name} does not parse: line {exc.lineno}: {exc.msg}"]

    stdlib_names = getattr(sys, "stdlib_module_names", set())
    if path.stem in stdlib_names:
        issues.append(f"{path.name} shadows a Python standard-library module")

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Name) and node.func.id in {"eval", "exec"}:
            issues.append(f"{path.name}:{node.lineno} uses unsafe {node.func.id}()")
        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "os"
            and node.func.attr == "system"
        ):
            issues.append(f"{path.name}:{node.lineno} uses unsafe os.system()")
        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "subprocess"
            and any(
                keyword.arg == "shell"
                and isinstance(keyword.value, ast.Constant)
                and keyword.value.value is True
                for keyword in node.keywords
            )
        ):
            issues.append(
                f"{path.name}:{node.lineno} uses subprocess with shell=True"
            )

    if re.search(
        r"(?i)(?:[a-z]:[\\/](?:users|documents and settings)[\\/][^\\/\s]+|"
        r"/(?:users|home)/[^/\s]+)",
        text,
    ):
        issues.append(f"{path.name} contains a hardcoded user-specific home path")
    return issues


def markdown_link_issues(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).strip().strip("<>")
        if not target or target.startswith("#"):
            continue
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, flags=re.IGNORECASE):
            continue
        local = unquote(target.split("#", 1)[0])
        candidate = (path.parent / local).resolve()
        if not candidate.exists():
            issues.append(f"{path.name} has a broken local link: {target}")
    return issues


def audit_skill_dir(root: Path, profile: str = "strict") -> list[str]:
    issues: list[str] = []
    skill_md = root / "SKILL.md"

    if not skill_md.exists():
        issues.append("Missing SKILL.md")
    else:
        text = skill_md.read_text(encoding="utf-8")
        frontmatter = extract_frontmatter(text)
        parsed_frontmatter, frontmatter_issues = validate_skill_frontmatter(frontmatter)
        issues.extend(frontmatter_issues)
        keys = set(parsed_frontmatter) if parsed_frontmatter else frontmatter_keys(frontmatter)
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
        issues.extend(markdown_link_issues(skill_md))

    nested_skills = [
        path for path in root.rglob("SKILL.md") if path.resolve() != skill_md.resolve()
    ]
    if nested_skills:
        issues.append(
            "Nested SKILL.md files may register duplicate skills: "
            + ", ".join(str(path.relative_to(root)) for path in nested_skills[:3])
        )

    if profile == "strict":
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
            issues.extend(markdown_link_issues(path))

    scripts = root / "scripts"
    if scripts.exists():
        executable_scripts = [
            path
            for path in scripts.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".py", ".ps1", ".sh", ".js", ".ts"}
            and not path.name.startswith(
                (
                    "test_",
                    "test-",
                    "validate_",
                    "validate-",
                    "check_",
                    "check-",
                    "verify_",
                    "verify-",
                )
            )
            and not path.stem.endswith("_test")
        ]
        if (
            profile == "strict"
            and executable_scripts
            and not script_validation_files(root)
        ):
            issues.append(
                "scripts/ contains executable helpers but no deterministic test "
                "or validation script"
            )
        for path in scripts.glob("*.py"):
            max_script_lines = 500 if profile == "strict" else 2000
            if count_lines(path) > max_script_lines:
                issues.append(f"{path.name} is large; consider splitting or simplifying")
            issues.extend(python_script_issues(path))

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
