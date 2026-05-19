---
name: sync
description: Use when the user wants to continue work across devices, recover Codex local context after switching machines, set up or follow a cross-device handoff workflow, or decide whether a task should stay on the coding machine or move to the writing machine.
---

# Sync

This skill standardizes cross-device work for `Codex local`, especially a stronger coding machine plus a lighter writing machine.

## Project path contract

Every project should use one canonical path contract:

- `.codex/project.yaml`

Before reading or writing project workflow files, resolve paths from `.codex/project.yaml` first. If the file or key is missing, use the documented default path and record the fallback in `HANDOFF.md` when it affects future resume work.

If `.codex/project.yaml` does not exist and the user asks to initialize or clean up project workflow state, offer to create it from:

- `references/project-yaml-template.yaml`

Do not create multiple competing path maps for different skills. Add new semantic paths to `.codex/project.yaml` instead.

## Manuscript Source Contract

For academic writing projects, prefer the manuscript paths declared under `.codex/project.yaml`:

- `paths.manuscript.source_of_truth` is the canonical editable manuscript, normally Markdown.
- `paths.manuscript.exchange_format` identifies the advisor-facing format, commonly DOCX.
- `paths.manuscript.reference_docx` is the Pandoc Word style template when DOCX export is needed.
- `paths.manuscript.bibliography` is the preferred BibTeX file.
- `paths.manuscript.latex_status: deferred` means do not require LaTeX tooling or create LaTeX/PDF outputs unless the user explicitly re-enables that path.

When syncing or handing off writing work, record changes against the Markdown source first. Treat Word files as imported originals, exported review copies, or tracked-comment inputs unless the project path contract explicitly says otherwise.

## Default model

- Treat the stronger machine as the default `coding / analysis / experiment` machine.
- Treat the lighter machine as the default `writing / ideation / reading` machine.
- Do not assume local chat history syncs across devices.
- Assume code state can sync through `git` or cloud storage, but conversation state must be reconstructed from project files.

## When this skill should act

Use this workflow when the user asks to:

- continue a task after switching machines
- set up a reusable handoff process
- decide which machine should own a task
- recover context for a `Codex local` project
- convert current project state into writing-ready notes

## Required project files

At the project root, prefer these files:

- `.codex/project.yaml`
- `TODO.md`
- `HANDOFF.md`
- `notes/experiment-log.md`
- `notes/writing-notes.md`

Optional `sync`-owned machine-readable files may live under `sync/`:

- `sync/sync_state.json`
- `sync/sessions.log`

These are owned by this skill only. They should not replace or overwrite state files owned by another workflow skill.

If they do not exist, offer to create them from:

- `references/project-yaml-template.yaml`
- `references/todo-template.md`
- `references/handoff-template.md`
- `references/experiment-log-template.md`
- `references/writing-notes-template.md`

## Ownership boundaries

Before creating, cleaning, or updating sync files, inspect whether the project contains state files from other workflow skills. Do not treat them as duplicate `sync` files.

Known examples:

- `handoff.json`, `memory/MEMORY.md`, and `harness/logs/sessions.log` are NORA checkpoint files when the `nora` skill is in use.
- `paper_framework_figure/` and `output/figures/` are figure-workflow files when `paper-framework-figure` or NORA figure generation is in use.
- `.checkpoints/` can be a workflow checkpoint archive and should not be deleted during sync cleanup.

Default behavior:

- `sync` may read other skill-owned files to reconstruct context.
- `sync` should not write, overwrite, move, rename, or delete other skill-owned files unless the user explicitly asks for compatibility output or cleanup.
- If machine-readable `sync` state is useful, write it under `sync/`, not into another skill's root-level files.
- If compatibility output is requested, clearly label it as a mirror and preserve the other skill's expected schema.

## First-pass decision rule

Classify the current request before doing anything else.

Send the task to the coding machine if it requires:

- running code, tests, notebooks, benchmarks, or long jobs
- editing implementation across multiple files
- environment setup or dependency debugging
- deep repo inspection that depends on local tooling

Send the task to the writing machine if it requires:

- drafting or revising prose
- synthesizing papers, notes, or experiment results
- planning, outlining, or reviewer-response writing
- light code reading without execution

If mixed, split it into two phases:

1. coding machine produces artifacts, notes, or results
2. writing machine converts them into prose, plans, or summaries

## Resume workflow

When resuming work on a different machine:

1. Read `.codex/project.yaml` first if present and resolve all workflow paths from it.
2. Read the resolved `TODO.md` and `HANDOFF.md` paths.
3. Inspect recent repository state:
   - latest commits
   - current uncommitted changes
   - any experiment or notes files referenced by `HANDOFF.md`
   - relevant skill-owned state files, read-only, when `HANDOFF.md` points to them or the requested workflow needs them
4. Reconstruct:
   - current task
   - completed work
   - next step
   - constraints and known risks
   - file ownership boundaries that must be preserved
5. Continue only after that reconstruction is explicit.

If `HANDOFF.md` is missing, infer state from the repo and create one before substantial new work.

## End-of-session workflow

Before switching devices or ending a substantial work block:

1. Resolve workflow paths from `.codex/project.yaml` if present.
2. Update the resolved `TODO.md`
3. Update the resolved `HANDOFF.md`
4. Record any experiment results in the resolved experiment log path.
5. Record any reusable writing language or interpretation in the resolved writing notes path.
6. If another skill's checkpoint is required, run or invoke that skill's checkpoint process separately instead of editing its state files from `sync`.

Keep handoff updates short and operational. Do not turn them into narrative diaries.

## Output contract

When using this skill, the assistant should produce one or more of:

- a machine recommendation for the task
- a reconstructed project state summary
- initialized handoff files
- an updated cross-device handoff
- a split plan separating coding and writing phases

## File conventions

### `.codex/project.yaml`

- project-level source of truth for workflow paths
- stores semantic path names, not skill-specific instructions
- every skill should prefer it before using built-in defaults
- add new path keys here when a workflow needs persistent artifacts
- do not use it to claim ownership of another skill's private state schema
- for writing projects, may include `paths.manuscript` with Markdown source, DOCX exchange output, bibliography, style template, and LaTeX readiness

### `sync/`

- use for `sync`-owned helper scripts, `sync_state.json`, and `sessions.log`
- do not mirror another skill's state here unless it is clearly labeled as read-only context or compatibility output
- do not make `sync/` the primary human resume location when root-level `HANDOFF.md` exists

### `TODO.md`

- active checklist only
- short, concrete items
- mark ownership or machine only when useful

### `HANDOFF.md`

Must contain:

- current task
- what was done
- current status
- next steps
- constraints

### `notes/experiment-log.md`

Use for:

- parameters
- result summaries
- failures worth remembering
- file paths to outputs

### `notes/writing-notes.md`

Use for:

- paragraph-ready claims
- figure interpretations
- wording for methods/results/discussion
- reviewer-response fragments

## Prompt patterns

For resume on the coding machine:

```text
Use the sync workflow. Read .codex/project.yaml if present, then read the resolved TODO and HANDOFF files, recent commits, and current uncommitted changes. Reconstruct the current implementation state, then continue the next coding step without repeating completed work.
```

For resume on the writing machine:

```text
Use the sync workflow. Read .codex/project.yaml if present, then read the resolved TODO, HANDOFF, experiment log, and writing notes files. Reconstruct the current project state, then turn it into writing-ready summaries, outlines, or prose.
```

For end-of-session handoff:

```text
Use the sync workflow. Based on the current repo state and this session's work, update TODO.md, HANDOFF.md, and any relevant notes files so the project can be resumed cleanly on another machine.
```

## Limits

- This skill does not assume shared local chat state across devices.
- This skill should not claim continuity of conversation history when only files were synced.
- This skill should prefer explicit handoff files over inferred memory.
- This skill should preserve other skills' checkpoint files as separate state layers.
- This skill should not collapse NORA, figure-generation, experiment, or manuscript-pipeline state into its own handoff files.
