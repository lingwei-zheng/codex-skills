---
name: sync
description: Use when the user wants to resume a research or paper project across devices, initialize a clean research-project workspace, reconstruct recent analysis or writing state from project files, or leave a concise cross-device handoff without relying on chat history.
---

# Sync

Standardize file-based continuity for research and paper projects across Codex
devices. Do not assume that chat history is shared.

## Core Contract

Use the smallest set of sources of truth that matches the project profile:

- `git` records what changed.
- The active analysis configuration records which settings were used.
- The active result directory records current outputs and validation.
- The paper governance documents record methods/results, research assessment, and
  writing rules.

For a single active paper analysis, prefer the minimal tree described in
`references/research-project-tree.md`. Do not recreate deleted `configs/`,
`output/`, `notes/`, or nested manuscript directories merely because an older
template used them. Retain the expanded tree only when the project already has
multiple analysis branches, archives, or review packages.

## Minimal Paper Profile

Recognize `minimal-paper` when these paths exist:

```text
README.md
analysis/config.yaml
analysis/01_*.py or analysis/01_*.R
paper/methods_results.md
paper/research_assessment.md
paper/writing_outline.md
results/
```

Treat the three files under `paper/` as one governance set:

- `methods_results.md`: ordered methods and results; use it for factual analysis
  state and claim-evidence boundaries.
- `research_assessment.md`: advisor assessment, evidence ledger, contribution
  risks, and journal ladder; use it for positioning and submission decisions.
- `writing_outline.md`: story spine, section order, figure/table plan, terminology,
  and inference rules; use it for manuscript drafting.

The minimal profile has one analysis flow. Read scripts in numeric order and do
not introduce a second active route without updating all three governance files
and `README.md`.

## Workflow

### Initialize

1. Read [references/research-project-tree.md](references/research-project-tree.md).
2. Detect the project profile. For `minimal-paper`, create only `analysis/`,
   `paper/`, and `results/`; do not create legacy logs or archive folders unless
   the user explicitly asks for them.
3. Read [references/minimal-paper-project.md](references/minimal-paper-project.md)
   when the project has the three core documents.
4. Read [references/naming-and-archiving.md](references/naming-and-archiving.md)
   before creating a dated archive or changing result names. A minimal project
   may keep one active `results/` directory without archiving.
5. Add `.codex/project.yaml` only when paths are non-standard or cannot be
   inferred from the minimal tree.

### Resume

Inspect state in this order:

1. Git status and recent commits.
2. `README.md` for the active question and reproduction order.
3. `analysis/config.yaml` and numeric analysis scripts.
4. `paper/methods_results.md`, then `paper/research_assessment.md`, then
   `paper/writing_outline.md`.
5. `results/`, prioritizing the validation verdict and run registries.
6. `.codex/project.yaml`, only when the project uses it.

For the minimal profile, reconstruct the current task, last validated result,
writing boundaries, next step, and any blocker from those files. Existing legacy
logs may be read for compatibility, but do not extend them as the new default.

### End A Work Block

1. Keep active analysis artifacts in `results/` and keep the three governance
   documents synchronized with any material change.
2. Run the project's validation script when available and record its verdict in
   `results/`; do not claim completion from a prose note alone.
3. Update `methods_results.md` when methods or numerical results change,
   `research_assessment.md` when contribution or journal fit changes, and
   `writing_outline.md` when story, section order, figures, terminology, or
   inference boundaries change.
4. Keep `README.md` as the short entry point with the active flow and commands.
5. Archive only when requested or when a reproducible submission checkpoint needs
   preservation; follow [references/naming-and-archiving.md](references/naming-and-archiving.md).
6. Change `.codex/project.yaml` only when path structure changes.

## Optional Path Map

`.codex/project.yaml` is a small optional path index, not a workflow log. When
present, resolve non-standard manuscript, config, export, or data paths from it.
Use [references/project-yaml-template.yaml](references/project-yaml-template.yaml)
for initialization. Do not require it for simple projects.

## Machine Split

- Prefer the coding machine for code, models, figures, batch exports, environment
  debugging, and validation.
- Prefer the writing machine for prose, reviewer responses, outlines, synthesis,
  and reading completed results.
- For mixed work, let the coding machine produce artifacts, configs, and validated
  outputs before the writing machine turns them into manuscript text.

## Ownership And Safety

- Treat `data/raw/` as immutable source data.
- Keep minimal project workflows in `analysis/`; use `code/analysis/` only for the
  expanded legacy profile.
- Treat `results/` as generated analysis state and do not rewrite registries by hand.
- Read other skill-owned files when needed for recovery, but do not rewrite their
  private state schemas.
- Preserve `.checkpoints/`, figure-workflow folders, and other skill-owned archives.
- Do not claim conversation continuity when only project files were synchronized.

## Reference Router

| Reference | Use |
|---|---|
| [references/research-project-tree.md](references/research-project-tree.md) | Minimal and expanded directory structures |
| [references/minimal-paper-project.md](references/minimal-paper-project.md) | Three-document governance and resume protocol |
| [references/naming-and-archiving.md](references/naming-and-archiving.md) | Output names and optional archive batches |
| [references/analysis-log-template.md](references/analysis-log-template.md) | Legacy expanded-profile analysis log |
| [references/manuscript-log-template.md](references/manuscript-log-template.md) | Legacy expanded-profile writing log |
| [references/archived-run-readme-template.md](references/archived-run-readme-template.md) | Archive-batch provenance note |
| [references/project-yaml-template.yaml](references/project-yaml-template.yaml) | Optional non-standard path map |

## Output

Produce the smallest useful result: an initialized structure, reconstructed
project-state summary, validation status, machine recommendation, or two-machine
handoff. Always identify the files used as the source of truth.
