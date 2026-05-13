#!/usr/bin/env python3
"""Cross-platform checkpoint writer for the NORA Codex adapter.

Run from a NORA project workspace, or pass --workspace. The script writes:
- handoff.json
- memory/MEMORY.md
- harness/logs/sessions.log
- optional .checkpoints/<session>_output copy of output/
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SECTION_NAMES = [
    "abstract",
    "introduction",
    "literature_review",
    "methodology",
    "results",
    "discussion",
    "conclusion",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def write_json(path: Path, data: Any, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def first_existing(workspace: Path, candidates: list[str]) -> Path | None:
    for rel in candidates:
        path = workspace / rel
        if path.exists():
            return path
    return None


def infer_topic(workspace: Path, config: dict[str, Any] | None) -> str | None:
    if config:
        topic = config.get("topic") or config.get("research_topic")
        if isinstance(topic, str) and topic.strip():
            return topic.strip()
    for rel in ["RESEARCH_PLAN.md", "BRIEF.md", "research_contract.md"]:
        path = workspace / rel
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="replace")
            for pattern in [
                r"(?im)^#\s+(.+)$",
                r"(?im)^##\s+1\.\s*Topic\s*\n+(.+)$",
                r"(?im)^Topic:\s*(.+)$",
            ]:
                match = re.search(pattern, text)
                if match:
                    value = match.group(1).strip()
                    if value and not value.startswith("["):
                        return value[:200]
    return None


def infer_journal(workspace: Path, config: dict[str, Any] | None) -> str | None:
    if config:
        journal = config.get("journal") or config.get("target_journal") or config.get("venue")
        if isinstance(journal, str) and journal.strip():
            return journal.strip()
    for rel in ["output/PAPER_PLAN.md", "BRIEF.md", "RESEARCH_PLAN.md"]:
        path = workspace / rel
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="replace")
            match = re.search(r"(?im)^(Target Journal|Target Venue|Venue):\s*(.+)$", text)
            if match:
                return match.group(2).strip()[:120]
    return None


def collect_sections(workspace: Path) -> tuple[list[str], list[str], str | None]:
    search_dirs = [
        workspace / "output" / "manuscript",
        workspace / "output" / "papers",
        workspace / "outputs" / "papers",
        workspace / "outputs" / "manuscript",
    ]
    files: list[Path] = []
    for directory in search_dirs:
        if directory.exists():
            files.extend(directory.glob("*.md"))

    written_names = {f.stem.lower().replace("-", "_") for f in files}
    accepted = [section for section in SECTION_NAMES if any(section in name for name in written_names)]
    pending = [section for section in SECTION_NAMES if section not in accepted]
    latest = max(files, key=lambda p: p.stat().st_mtime, default=None)
    return accepted, pending, str(latest.relative_to(workspace)) if latest else None


def load_review_state(workspace: Path) -> tuple[dict[str, Any] | None, Path | None]:
    path = first_existing(workspace, ["output/REVIEW_STATE.json", "outputs/REVIEW_STATE.json"])
    data = read_json(path) if path else None
    return data if isinstance(data, dict) else None, path


def detect_stage(workspace: Path, accepted: list[str], pending: list[str], review_state: dict[str, Any] | None) -> tuple[str, str, str]:
    if review_state and str(review_state.get("status", "")).lower() not in {"complete", "accepted", "done"}:
        round_value = review_state.get("round")
        next_round = int(round_value) + 1 if isinstance(round_value, int) else "next"
        return (
            "review-loop",
            f"resume adversarial review at round {next_round}",
            "auto-review-loop",
        )

    markers = [
        ("output/papers", "finalization", "run submit-check or paper-covert", "submit-check"),
        ("output/manuscript", "manuscript", "run paper-review-loop or paper-covert", "paper-review-loop"),
        ("output/PAPER_PLAN.md", "paper-plan", "run paper-figure-generate or paper-draft", "paper-writing-pipeline"),
        ("output/NARRATIVE_REPORT.md", "report", "run paper-writing-pipeline", "paper-writing-pipeline"),
        ("output/experiment/EXPERIMENT_RESULT.md", "experiment", "run auto-review-loop or generate-report", "auto-review-loop"),
        ("output/refine-logs/EXPERIMENT_PLAN.md", "experiment-design", "run deploy-experiment", "deploy-experiment"),
        ("output/IDEA_REPORT.md", "idea-discovery", "run novelty-check, idea-review, or experiment-design", "experiment-design"),
        ("output/LIT_REVIEW_REPORT.md", "literature-review", "run idea-discovery-pipeline", "idea-discovery-pipeline"),
        ("BRIEF.md", "intake", "run full-pipeline or the selected phase workflow", "full-pipeline"),
        ("RESEARCH_PLAN.md", "planning", "run full-pipeline or lit-review", "full-pipeline"),
    ]
    for rel, stage, next_step, skill in markers:
        if (workspace / rel).exists():
            if stage == "manuscript" and pending:
                next_step = f"continue manuscript work; pending sections: {', '.join(pending)}"
            return stage, next_step, skill

    return "not-started", "run launcher intake or create BRIEF.md", "launcher"


def build_handoff(workspace: Path, session_id: str, timestamp: str) -> dict[str, Any]:
    config = read_json(workspace / "configs" / "default.json")
    if not isinstance(config, dict):
        config = None

    review_state, review_state_path = load_review_state(workspace)
    accepted, pending, latest_section = collect_sections(workspace)
    stage, next_step, resume_skill = detect_stage(workspace, accepted, pending, review_state)

    read_first = []
    for rel in [
        "handoff.json",
        "memory/MEMORY.md",
        "RESEARCH_PLAN.md",
        "BRIEF.md",
        "output/REVIEW_STATE.json",
        "outputs/REVIEW_STATE.json",
        "output/PROJ_NOTES.md",
        "output/EXPERIMENT_LOG.md",
        "output/NARRATIVE_REPORT.md",
        "output/PAPER_PLAN.md",
    ]:
        if (workspace / rel).exists() and rel != "handoff.json":
            read_first.append(rel)

    experiment = read_json(first_existing(workspace, ["output/experiment/EXPERIMENT_RESULT.json", "output/EXPERIMENT_RESULT.json"]) or Path())
    if not isinstance(experiment, dict):
        experiment = {}

    token_usage = read_json(first_existing(workspace, ["output/token_usage.json", "outputs/token_usage.json"]) or Path())
    if not isinstance(token_usage, dict):
        token_usage = {}

    return {
        "timestamp": timestamp,
        "schema_version": 1,
        "runtime": "codex",
        "session_id": session_id,
        "workspace": str(workspace),
        "pipeline": {
            "stage": stage,
            "last_completed_step": None,
            "next_step": next_step,
            "resume_skill": resume_skill,
        },
        "review_state": review_state,
        "review_state_path": str(review_state_path.relative_to(workspace)) if review_state_path else None,
        "last_experiment": {
            "summary": experiment.get("summary"),
            "status": experiment.get("status"),
            "best_model": experiment.get("best_model"),
            "best_metric": experiment.get("best_metric"),
        },
        "paper": {
            "sections_accepted": accepted,
            "sections_pending": pending,
            "last_written": latest_section,
        },
        "token_budget": {
            "total_used": token_usage.get("total_tokens"),
            "estimated_cost_usd": token_usage.get("estimated_cost_usd"),
        },
        "recovery": {
            "read_first": read_first,
            "resume_skill": resume_skill,
            "human_checkpoint_needed": bool(review_state and review_state.get("human_checkpoint_needed")),
            "notes": [],
        },
    }


def replace_code_block(content: str, section: str, block: str) -> str:
    pattern = re.compile(rf"(## {re.escape(section)}.*?)(```.*?```)", re.DOTALL)
    replacement = lambda match: match.group(1) + block
    new_content, count = pattern.subn(replacement, content, count=1)
    return new_content if count else content


def update_memory(workspace: Path, skill_root: Path, handoff: dict[str, Any], timestamp: str, dry_run: bool) -> None:
    memory_dir = workspace / "memory"
    memory_path = memory_dir / "MEMORY.md"
    if not memory_path.exists():
        template = skill_root / "memory" / "MEMORY.md"
        if template.exists() and not dry_run:
            memory_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(template, memory_path)
        elif not template.exists() and not dry_run:
            memory_dir.mkdir(parents=True, exist_ok=True)
            memory_path.write_text("# NORA Session Memory\n", encoding="utf-8")

    if dry_run or not memory_path.exists():
        return

    content = memory_path.read_text(encoding="utf-8", errors="replace")
    pipeline = handoff["pipeline"]
    paper = handoff["paper"]

    state_block = (
        "```\n"
        f"Topic:           {infer_topic(workspace, None) or '[not set]'}\n"
        f"Mode:            codex\n"
        f"Stage:           {pipeline['stage']}\n"
        f"Target journal:  {infer_journal(workspace, None) or '[not set]'}\n"
        f"Run ID:          {handoff['session_id']}\n"
        f"Last updated:    {timestamp}\n"
        f"Overall status:  {pipeline['stage']}\n"
        "```"
    )
    draft_block = (
        "```\n"
        f"File:                    {paper.get('last_written') or '-'}\n"
        f"Sections completed:      {len(paper.get('sections_accepted', []))} / {len(SECTION_NAMES)}\n"
        f"Sections accepted:       {', '.join(paper.get('sections_accepted', [])) or '-'}\n"
        f"Review round:            {((handoff.get('review_state') or {}).get('round', '-'))}\n"
        f"Review decision:         {((handoff.get('review_state') or {}).get('status', '-'))}\n"
        f"Final paper path:        {paper.get('last_written') or '-'}\n"
        "```"
    )

    content = replace_code_block(content, "Current Research State", state_block)
    content = replace_code_block(content, "Active Paper Draft", draft_block)

    last_action = f"- {timestamp}: checkpoint written; next step: {pipeline['next_step']}\n"
    content = re.sub(
        r"(## Last Action\s*\n\n)(.*?)(\n---)",
        lambda m: m.group(1) + last_action + m.group(3),
        content,
        count=1,
        flags=re.DOTALL,
    )

    memory_path.write_text(content, encoding="utf-8")


def copy_output_checkpoint(workspace: Path, session_id: str, dry_run: bool) -> str | None:
    output_dir = workspace / "output"
    if not output_dir.exists():
        return None
    checkpoint_dir = workspace / ".checkpoints"
    target = checkpoint_dir / f"{session_id}_output"
    if dry_run:
        return str(target)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(output_dir, target)
    return str(target)


def append_log(workspace: Path, timestamp: str, session_id: str, dry_run: bool) -> None:
    if dry_run:
        return
    log_dir = workspace / "harness" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    with (log_dir / "sessions.log").open("a", encoding="utf-8") as handle:
        handle.write(f"{timestamp} | CHECKPOINT | Session {session_id} checkpointed\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a NORA Codex checkpoint.")
    parser.add_argument("--workspace", default=".", help="Project workspace to checkpoint. Defaults to current directory.")
    parser.add_argument("--skill-root", default=None, help="NORA skill root. Defaults to parent of this script directory.")
    parser.add_argument("--session-id", default=None, help="Checkpoint/session id. Defaults to env or timestamp.")
    parser.add_argument("--dry-run", action="store_true", help="Inspect state without writing files.")
    parser.add_argument("--no-copy-output", action="store_true", help="Do not copy output/ into .checkpoints/.")
    args = parser.parse_args()

    workspace = Path(args.workspace).expanduser().resolve()
    script_path = Path(__file__).resolve()
    skill_root = Path(args.skill_root).expanduser().resolve() if args.skill_root else script_path.parents[1]
    timestamp = utc_now()
    session_id = args.session_id or os.environ.get("GEO_AGENT_SESSION_ID") or f"session_{timestamp.replace(':', '').replace('-', '')}"

    handoff = build_handoff(workspace, session_id, timestamp)
    checkpoint_path = None if args.no_copy_output else copy_output_checkpoint(workspace, session_id, args.dry_run)
    if checkpoint_path:
        handoff["checkpoint_output"] = checkpoint_path

    update_memory(workspace, skill_root, handoff, timestamp, args.dry_run)
    write_json(workspace / "handoff.json", handoff, args.dry_run)
    append_log(workspace, timestamp, session_id, args.dry_run)

    print(json.dumps({
        "workspace": str(workspace),
        "dry_run": args.dry_run,
        "stage": handoff["pipeline"]["stage"],
        "next_step": handoff["pipeline"]["next_step"],
        "resume_skill": handoff["pipeline"]["resume_skill"],
        "handoff": str(workspace / "handoff.json"),
        "memory": str(workspace / "memory" / "MEMORY.md"),
        "checkpoint_output": checkpoint_path,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
