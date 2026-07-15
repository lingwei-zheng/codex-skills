---
name: sync
description: Use when the user wants to resume a research or paper project across devices, initialize a clean research-project workspace, reconstruct recent analysis or writing state from project files, or leave a concise cross-device handoff without relying on chat history.
---

# Sync

Standardize file-based continuity for research and paper projects across Codex
devices. Do not assume that chat history is shared.

## Core Contract

Use four sources of truth:

- `git` records what changed.
- `configs/` records which settings were used.
- `output/archived_runs/` preserves important output batches.
- `notes/*_log.md` records why work changed and what happens next.

Do not initialize new projects around `TODO.md`, `HANDOFF.md`, legacy experiment
or writing logs, `sync_state.json`, `sessions.log`, or a separate `sync/` state
tree.

## Workflow

### Initialize

1. Read [references/research-project-tree.md](references/research-project-tree.md).
2. Create only the working directories needed by the project. The minimum set is
   `configs/`, `output/current/`, `output/archived_runs/`, and `notes/`.
3. Initialize `notes/analysis_log.md` and `notes/manuscript_log.md` from their
   templates.
4. Read [references/naming-and-archiving.md](references/naming-and-archiving.md)
   before naming outputs or creating the first archive.
5. Add `.codex/project.yaml` only when non-standard or multiple active paths make
   a path index useful.

### Resume

Inspect state in this order:

1. Git status and recent commits.
2. Active files under `configs/`.
3. `output/current/`.
4. The newest entries under `output/archived_runs/`.
5. `notes/analysis_log.md` and `notes/manuscript_log.md`.
6. `.codex/project.yaml`, only when the project uses it.

Reconstruct the current task, recent changes, reasons, latest outputs, next step,
and preferred machine when relevant. Existing `TODO.md`, `HANDOFF.md`, or legacy
logs may be read for compatibility, but do not extend them as the new default.

### End A Work Block

1. Keep active artifacts in `output/current/`.
2. Archive important completed outputs according to
   [references/naming-and-archiving.md](references/naming-and-archiving.md).
3. Update `notes/analysis_log.md` for runs, parameters, decisions, failures, and
   next experiments.
4. Update `notes/manuscript_log.md` for revisions, submission packaging, reviewer
   responses, and writing decisions.
5. Name the relevant configs and output paths explicitly.
6. Change `.codex/project.yaml` only when path structure changed.

Keep logs short, operational, and decision-oriented.

## Optional Path Map

`.codex/project.yaml` is a small optional path index, not a workflow log. When
present, resolve non-standard manuscript, config, export, or data paths from it.
Use [references/project-yaml-template.yaml](references/project-yaml-template.yaml)
for initialization. Do not require it for simple projects.

## Machine Split

- Prefer the coding machine for code, notebooks, models, figures, batch exports,
  environment debugging, and tooling-heavy inspection.
- Prefer the writing machine for prose, reviewer responses, outlines, synthesis,
  and reading completed notes or outputs.
- For mixed work, let the coding machine produce artifacts, configs, and logged
  decisions before the writing machine turns them into manuscript text.

## Ownership And Safety

- Treat `data/raw/` as immutable source data.
- Keep project workflows in `code/analysis/` and reusable path-independent helpers
  in `code/scripts/`.
- Read other skill-owned files when needed for recovery, but do not rewrite their
  private state schemas.
- Preserve `.checkpoints/`, figure-workflow folders, and other skill-owned archives.
- Do not claim conversation continuity when only project files were synchronized.

## Reference Router

| Reference | Use |
|---|---|
| [references/research-project-tree.md](references/research-project-tree.md) | Default directory structure and ownership |
| [references/naming-and-archiving.md](references/naming-and-archiving.md) | Output names, version labels, archive batches, and current-versus-archived rules |
| [references/analysis-log-template.md](references/analysis-log-template.md) | Analysis decisions and next-run log |
| [references/manuscript-log-template.md](references/manuscript-log-template.md) | Writing, submission, and reviewer-response log |
| [references/archived-run-readme-template.md](references/archived-run-readme-template.md) | Archive-batch provenance note |
| [references/project-yaml-template.yaml](references/project-yaml-template.yaml) | Optional non-standard path map |

## Output

Produce the smallest useful result: an initialized structure, reconstructed
project-state summary, updated log, machine recommendation, or two-machine
handoff. Always identify the files used as the source of truth.
