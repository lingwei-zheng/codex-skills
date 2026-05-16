---
name: nora
description: Codex adapter for NORA, the Night Owl Research Agent. Use when the user asks for autonomous or guided academic research workflows in geoscience, remote sensing, GIScience, GeoAI, spatial data science, disaster resilience, environmental health, literature review, idea discovery, novelty checking, experiment design/execution, spatial analysis, adversarial review, report generation, manuscript drafting, figure generation, or journal submission preparation. This skill routes Claude Code-style NORA skills under skills/ into Codex-compatible workflows.
---

# NORA for Codex

## Purpose

Use this root skill as the Codex router for the bundled NORA Claude Code skill pack. The original NORA files remain source material:

- `CLAUDE.md`: upstream dashboard, control flags, recovery protocol, and workflow inventory.
- `.claude/commands/launcher.md`: upstream launcher intake flow.
- `skills/<workflow>/SKILL.md`: Claude Code workflow skills to read as phase instructions.
- `skills/knowledge/*.md`: domain references for geoscience, GIScience, GeoAI, spatial methods, environmental health, disaster resilience, literature mining, and academic writing.
- `templates/`, `configs/`, `tools/`, `mcp/`: bundled templates, configuration, CLI utilities, and upstream MCP server notes.

Do not load the whole pack by default. Select one workflow, read only the needed `SKILL.md`, then load only directly referenced knowledge, template, config, or tool files.

## Project Path Contract

When operating inside a project workspace, read `.codex/project.yaml` if it exists before routing into a NORA workflow. Treat it as the project-level path contract for shared workflow paths such as handoff, notes, inputs, outputs, papers, and sync state.

Path resolution priority:

1. explicit user argument or selected workflow input
2. `.codex/project.yaml`
3. NORA's documented default paths from `CLAUDE.md` or `skills/<workflow>/SKILL.md`

Preserve NORA-owned checkpoint files (`handoff.json`, `memory/MEMORY.md`, `harness/logs/sessions.log`, `.checkpoints/`) as a separate state layer. Use `.codex/project.yaml` for shared path resolution, not as a replacement for NORA's checkpoint schema.

## Codex Runtime Mapping

Interpret upstream Claude Code terms as follows:

| Upstream wording | Codex behavior |
|---|---|
| `/launcher` | Read `.claude/commands/launcher.md` and perform the intake inline. |
| `Skill: <name>` or `/full-pipeline` | Read `skills/<name>/SKILL.md` and execute that workflow inline. |
| `Skill tool` | No native Codex Skill tool call is available; route manually by reading the referenced file. |
| `Agent`, `subagent`, `.claude/agents/*.md` | Treat agent files as role prompts. Do not spawn Codex subagents unless the user explicitly asks for delegation or parallel agents. |
| `AskUserQuestion` | Ask concise clarification questions in chat. |
| `WebSearch`, `WebFetch` | Use Codex web browsing when current literature, datasets, journal requirements, citations, or external evidence must be verified. |
| Claude hooks in `harness/hooks/` or `settings.json` | Preserve as upstream metadata. Do not install or execute hooks unless the user explicitly asks. |
| `.mcp.json` servers | Treat as setup notes. Use currently available Codex tools instead of assuming those MCP servers are installed. |

## Zotero Integration

When a NORA workflow needs Zotero, citations, BibTeX, references, or local paper-library search, use the Zotero plugin if it is available even when upstream NORA text refers to a Zotero MCP server.

Resolution order:

1. Use any currently available Zotero MCP or app tool if present.
2. Otherwise use the installed Zotero plugin helper:
   `C:/Users/Lingwei/.codex/plugins/cache/openai-curated/zotero/dc902811/skills/zotero/scripts/zotero.py`
3. If the helper path is missing, search under `C:/Users/Lingwei/.codex/plugins/cache/openai-curated/zotero/*/skills/zotero/scripts/zotero.py`.
4. If no Zotero route is available, continue with local PDFs and web sources and record the gap.

Helper command pattern:

```bash
python <zotero.py> status --json
python <zotero.py> search "<query>" --json
python <zotero.py> export-bibtex --out references.bib
python <zotero.py> fulltext <attachment-key> --out <file>
```

Start with `status --json`. If the local API is disabled but Zotero is needed for the requested workflow, run `enable --restart` only when the user has asked to operate Zotero. Treat Zotero writes such as `import-bibtex` and `import-ris` as explicit write actions requiring clear user intent.

## Codex Checkpointing

Use `scripts/nora_checkpoint.py` instead of Claude Code `Stop` hooks. Run it from the active project workspace before pausing a long NORA workflow, switching machines, or handing off to a future session:

```bash
python <path-to-this-skill>/scripts/nora_checkpoint.py --workspace <project-workspace>
```

The script is cross-platform and writes project-local state:

- `handoff.json`
- `memory/MEMORY.md`
- `harness/logs/sessions.log`
- `.checkpoints/<session>_output/` when `output/` exists

Use `--dry-run` to inspect inferred stage and next step without writing files. Use `--no-copy-output` when `output/` is large.

## Workflow Router

Choose the smallest relevant workflow:

| User intent | Read first |
|---|---|
| Interactive project intake or "launch NORA" | `.claude/commands/launcher.md` |
| End-to-end research lifecycle | `skills/full-pipeline/SKILL.md` |
| Literature review, paper search, gap synthesis | `skills/lit-review/SKILL.md` |
| Generate research ideas | `skills/generate-idea/SKILL.md` |
| Full idea discovery pipeline | `skills/idea-discovery-pipeline/SKILL.md` |
| Novelty check against literature | `skills/novelty-check/SKILL.md` |
| External/critical idea review | `skills/idea-review/SKILL.md` |
| Refine vague research direction into method plan | `skills/refine-research/SKILL.md` |
| Detailed experiment roadmap | `skills/experiment-design/SKILL.md` |
| Refine plus experiment design | `skills/experiment-design-pipeline/SKILL.md` |
| Run local, remote, Modal, GPU, or spatial experiments | `skills/deploy-experiment/SKILL.md` |
| Find/download datasets with provenance | `skills/data-download/SKILL.md` |
| Spatial statistics, GIScience diagnostics, maps, spatial regression | `skills/spatial-analysis/SKILL.md` |
| Adversarial review loop for drafts/results | `skills/auto-review-loop/SKILL.md` |
| Consolidated narrative report | `skills/generate-report/SKILL.md` |
| Full manuscript pipeline | `skills/paper-writing-pipeline/SKILL.md` |
| Paper outline and figure plan | `skills/paper-plan/SKILL.md` |
| Paper figures, maps, diagrams, captions | `skills/paper-figure-generate/SKILL.md` |
| Manuscript drafting | `skills/paper-draft/SKILL.md` |
| Manuscript review and revision | `skills/paper-review-loop/SKILL.md` |
| Submission package conversion | `skills/paper-covert/SKILL.md` |
| Journal requirement validation | `skills/submit-check/SKILL.md` |
| Monitor running experiments | `skills/training-check/SKILL.md` |

If a request spans multiple workflows, start with `skills/full-pipeline/SKILL.md` unless the user clearly asks for a single phase.

## Operating Rules

- Keep generated project artifacts in the user's active workspace unless the user asks to modify the installed skill itself.
- Before writing long-running research artifacts, check whether the active workspace already has `RESEARCH_PLAN.md`, `BRIEF.md`, `handoff.json`, `output/REVIEW_STATE.json`, or `memory/MEMORY.md`.
- Preserve NORA's generator-evaluator separation: the same phase should not both draft and score its own work.
- Do not fabricate citations, datasets, benchmark values, experiment results, or journal requirements. Verify against authoritative sources when claims depend on current or external evidence.
- Do not execute destructive commands, push to remotes, install hooks, or configure MCP servers without explicit user instruction.
- For experiment execution, surface compute, dependency, API key, and GPU assumptions before running expensive or long-lived jobs.
- For data download, record source URL, license/terms when available, retrieval date, and file integrity information.
- Before pausing or ending a multi-step NORA workflow, run `scripts/nora_checkpoint.py` for the active workspace unless the user asks not to write state.

## Output Defaults

Default to concise stage-aware output:

1. State the selected NORA workflow.
2. State required inputs or assumptions.
3. Produce the requested artifact or next-step plan.
4. Record file paths when files are created.
5. Identify verification gaps explicitly instead of filling them by inference.
