---
name: sync
description: Use when the user wants to resume a research or paper project across devices, initialize a clean research-project workspace, reconstruct recent analysis or writing state from project files, or leave a concise cross-device handoff without relying on chat history.
---

# Sync

Maintain file-based continuity for research and paper projects across Codex
devices. Do not assume chat history is shared.

## Sources Of Truth

Use the smallest set that matches the project:

- Git records what changed.
- The active configuration records which settings were used.
- The active results directory records outputs and validation.
- Project governance documents record methods, results, assessment, story, and
  writing boundaries.

## Project Profiles

Read [references/research-project-tree.md](references/research-project-tree.md)
before creating directories.

- `minimal-paper`: one active analysis flow using `analysis/`, `results/`, and
  three governance files under `paper/`. Read
  [references/minimal-paper-project.md](references/minimal-paper-project.md).
- `expanded-research`: multiple analysis branches, archived runs, manuscript
  versions, supplements, or reviewer packages. Retain the expanded tree only
  when the project already needs it or the user explicitly requests it.
- `legacy`: read existing `TODO.md`, `HANDOFF.md`, logs, and `sync/` state for
  compatibility, but do not extend them as the new default.

Do not recreate deleted `configs/`, `output/`, `notes/`, or nested manuscript
directories merely because an older template used them.

## Workflow

### Initialize

1. Detect the project profile and existing conventions.
2. Create only the directories and governance files required by that profile.
3. Protect raw data and existing user files.
4. Add `.codex/project.yaml` only when non-standard paths cannot be inferred.
5. Apply [references/naming-and-archiving.md](references/naming-and-archiving.md)
   only when naming outputs or creating an archive.

### Resume

Inspect state in this order:

1. Git status and recent commits.
2. `README.md` for the active question and reproduction order.
3. Active configuration and numerically ordered analysis scripts.
4. Project governance documents in their declared order.
5. Current results, validation verdicts, and run registries.
6. `.codex/project.yaml` only when present.

Recover the current advantage state and claim/evidence dependencies from existing
project records; reconcile stale configuration/results before reusing a story.
Reconstruct the current task, last validated result, writing boundaries, next
step, and blockers. Identify every file used as a source of truth.

### End A Work Block

1. Keep active artifacts in the profile's current results directory.
2. Run the project validation command when available and record its verdict.
3. Update only the governance documents affected by material changes.
4. Keep `README.md` as the short entry point with the active flow and commands.
5. Preserve the project's documentation language and terminology policy.
6. Archive only when requested or when a reproducible submission checkpoint
   needs preservation.
7. Change `.codex/project.yaml` only when path structure changes.

## Optional Path Map

`.codex/project.yaml` is a small path index, not a workflow log. Use
[references/project-yaml-template.yaml](references/project-yaml-template.yaml)
only when manuscript, configuration, export, data, or results paths are
non-standard.

## Machine Split

- Prefer the coding machine for code, models, figures, batch exports,
  environments, and validation.
- Prefer the writing machine for prose, outlines, synthesis, reviewer responses,
  and reading validated results.
- For mixed work, let the coding machine produce traceable artifacts before the
  writing machine converts them into manuscript text.

## Safety

- Treat raw source data as immutable.
- Do not introduce a second active analysis route without updating the project
  entry point and governance documents.
- Do not rewrite generated registries or private state schemas by hand.
- Preserve `.checkpoints/`, figure-workflow folders, and skill-owned archives.
- Do not claim conversation continuity when only files were synchronized.

## Reference Router

| Reference | Use |
|---|---|
| [references/research-project-tree.md](references/research-project-tree.md) | Minimal and expanded directory profiles |
| [references/minimal-paper-project.md](references/minimal-paper-project.md) | Three-document governance, language, and resume protocol |
| [references/naming-and-archiving.md](references/naming-and-archiving.md) | Output names and archive batches |
| [references/analysis-log-template.md](references/analysis-log-template.md) | Legacy expanded-profile analysis log |
| [references/manuscript-log-template.md](references/manuscript-log-template.md) | Legacy expanded-profile writing log |
| [references/archived-run-readme-template.md](references/archived-run-readme-template.md) | Archive provenance note |
| [references/project-yaml-template.yaml](references/project-yaml-template.yaml) | Optional non-standard path map |

## Output

Produce the smallest useful result: an initialized structure, reconstructed
state summary, validation status, machine recommendation, or cross-device
handoff. Always identify the source-of-truth files.
