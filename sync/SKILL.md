---
name: sync
description: Use when the user wants to resume a research or paper project across devices, initialize a clean research-project workspace, reconstruct recent analysis or writing state from project files, or leave a concise cross-device handoff without relying on chat history.
---

# Sync

This skill standardizes cross-device work for research and paper projects in `Codex local`.

## Core model

Treat these four layers as the default research handoff contract:

- `git` records what changed
- `configs/` records which settings were used
- `output/archived_runs/` keeps each important output batch
- `notes/*_log.md` records why the work changed and what happens next

Do not default to `TODO.md`, `HANDOFF.md`, `sync_state.json`, or chat-history assumptions.

## Default project layout

Prefer this lightweight research layout:

```text
project/
  README.md
  AGENTS.md
  CLAUDE.md
  .gitignore

  data/
    raw/
    clean/

  code/
    analysis/
    scripts/

  configs/
  htc/

  output/
    current/
    archived_runs/

  paper/
    manuscript/
      current/
      versions/
    supplement/
      current/
      versions/
    response_to_reviewers/

  notes/
    analysis_log.md
    manuscript_log.md
```

Default rules:

- `data/raw/` is read-only source data and should not be overwritten.
- `code/analysis/` holds project-specific workflows; use ordered names such as `00_...` to `99_...`.
- `code/scripts/` holds reusable helpers and should not depend on project-global paths.
- `output/current/` holds in-progress artifacts.
- `output/archived_runs/` holds dated, versioned output snapshots.
- `notes/analysis_log.md` records analysis reasons, decisions, and next runs.
- `notes/manuscript_log.md` records writing, submission, and reviewer-response reasons.

## Optional path map

`.codex/project.yaml` is optional. Use it only when the project has non-standard or multiple active paths for manuscripts, configs, exports, or data locations.

When present:

- resolve workflow paths from it first
- keep it as a small path index, not a second workflow log
- prefer `references/project-yaml-template.yaml` as the initializer
- do not require it for simple projects

## When this skill should act

Use this workflow when the user asks to:

- continue a research or paper task after switching machines
- initialize a reusable research-project skeleton
- reconstruct current analysis or manuscript state
- decide whether coding or writing work belongs on a different machine
- leave a concise project handoff based on files, outputs, and git state

## Machine split

Prefer the coding machine for code edits, notebooks, model runs, figures, batch exports, environment debugging, or tooling-heavy inspection.

Prefer the writing machine for drafting or revising prose, reviewer responses, outlines, synthesis, or light reading of notes and outputs without execution.

If mixed, split into two phases:

1. coding machine produces artifacts, configs, and logged decisions
2. writing machine turns them into manuscript prose or response text

## Default state sources

Prefer these sources, in this order:

1. `git` status and recent commits
2. `configs/`
3. `output/current/`
4. recent `output/archived_runs/`
5. `notes/analysis_log.md`
6. `notes/manuscript_log.md`
7. `.codex/project.yaml` only when the project actually uses it

Do not create or require these as new defaults:

- `TODO.md`
- `HANDOFF.md`
- `notes/experiment-log.md`
- `notes/writing-notes.md`
- `sync/sync_state.json`
- `sync/sessions.log`

Old files may still be read for compatibility when they already exist, but new projects should not be initialized around them.

## Initialization workflow

When asked to initialize a research project, create only the default working set: `configs/`, `output/current/`, `output/archived_runs/`, `notes/analysis_log.md`, and `notes/manuscript_log.md`.

Add `.codex/project.yaml` only when the project needs non-default paths.

## Ownership boundaries

- `sync` may read other skill-owned files to reconstruct context.
- `sync` should not write into another skill's private state schema unless the user explicitly asks for compatibility output.
- `sync` should not delete `.checkpoints/`, figure-workflow folders, or other skill-owned archives during cleanup.
- `sync` should place its own initialized docs under the project structure above, not under a separate `sync/` state tree.

## Resume workflow

When resuming on another machine:

1. Inspect recent commits and current uncommitted changes.
2. Read active config files under `configs/`.
3. Inspect `output/current/` and the newest folders or files under `output/archived_runs/`.
4. Read `notes/analysis_log.md` and `notes/manuscript_log.md`.
5. If `.codex/project.yaml` exists, use it to resolve non-standard paths.
6. Reconstruct:
   - current task
   - what changed recently
   - why it changed
   - most recent outputs
   - next step
   - machine recommendation if relevant

## End-of-session workflow

Before switching devices or ending a substantial work block:

1. Archive important completed outputs into `output/archived_runs/`.
2. Leave still-active artifacts in `output/current/`.
3. Update `notes/analysis_log.md` for analysis runs, parameters, decisions, failures, or next experiments.
4. Update `notes/manuscript_log.md` for manuscript revisions, submission packaging, reviewer responses, or writing next steps.
5. Mention the relevant configs and output paths explicitly.
6. If `.codex/project.yaml` is in use, update path keys only when the project structure actually changed.

Keep logs short, operational, and decision-oriented.

## Output contract

When using this skill, the assistant should produce one or more of:

- a machine recommendation for the task
- a reconstructed research-project state summary
- initialized research-project folders and templates
- an updated analysis or manuscript log
- a split coding-machine versus writing-machine handoff

## Naming rules

Do not recommend vague names such as `final.docx`, `final_v2.docx`, `real_final.docx`, `latest`, `updated`, or `test`.

Prefer:

- `YYYY-MM-DD_vNN_filetype_short_description.ext`
- readable analysis labels such as `v02_add_clinical_covariates`

Examples: `2026-05-12_v02_manuscript_main_after_coauthor_comments.docx`, `2026-05-20_v03_Table2_model_performance.xlsx`, `2026-05-20_v03_Figure3_calibration_plot.pdf`.

## Templates

For initialization or cleanup, use `references/project-yaml-template.yaml`, `references/analysis-log-template.md`, `references/manuscript-log-template.md`, `references/archived-run-readme-template.md`, and `references/research-project-tree.md`.

Do not initialize the old `todo`, `handoff`, `experiment-log`, or `writing-notes` templates for new projects.

## Limits

- This skill does not assume shared local chat state across devices.
- This skill should not claim continuity of conversation history when only files were synced.
- This skill should not require `.codex/project.yaml` for simple projects.
- This skill should preserve other skills' checkpoint files as separate layers.
- This skill should not collapse another workflow's private state into a new `sync/` state tree.
