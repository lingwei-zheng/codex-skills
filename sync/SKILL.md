---
name: sync
description: Resume a research or paper project from files, initialize a minimal workspace, or leave a cross-device handoff without relying on shared chat history.
---

# Sync

Maintain continuity from Git, active configuration, current results/validation
and existing project documents. Do not assume conversation history transfers.

## Initialize Only What Is Needed

Before creating directories, read `references/research-project-tree.md`.
Use `minimal-paper` for a single analysis flow: `analysis/`, `results/` and
three governance documents under `paper/`, specified in
`references/minimal-paper-project.md`. Use an expanded structure only when
existing branches, archives, manuscript versions or reviewer packages need it,
or the user requests it.

Respect existing conventions and raw data. Read legacy TODO/HANDOFF/logs for
continuity without extending them as a new default. Do not recreate deleted
`configs/`, `output/`, `notes/` or nested manuscript folders from old templates.
Add `.codex/project.yaml` only for non-standard paths that cannot be inferred;
it is a path index, not a log.

## Resume

Read Git status/recent commits, README, active configuration/scripts, declared
governance documents, then current results/validation/run registries. Use the
path map if present. Identify the source-of-truth files.

Recover the current task, last validated result, claim/evidence versions,
writing boundaries, current decisions, blockers and next authorized step.
Resolve superseded decisions into the active specification; retain necessary
history in existing records. Carry only history needed for the next decision
or required reporting into the handoff, without replaying editorial corrections.
Reconcile stale configurations/results before reusing claims. When deciding
readiness or the next scientific action, read the project-root
`SCIENTIFIC_EXPLORATION_PROTOCOL.md` under project `AGENTS.md` and restore
recorded decisions, branch limits and resource bounds. There is no bundled
methodology fallback: report a missing protocol and defer only dependent
scientific decisions. File-state recovery can continue. Preserve integrity and
approval gates.

## End a Work Block

Keep artifacts in the active results directory. Run the project validation
command when available and record the verdict. Update only documents affected
by material changes, preserving the project's language and terminology; README
remains the short entry point with active commands. Update the path map only
when paths change. Archive only on request or for a reproducible submission
checkpoint; use `references/naming-and-archiving.md` when naming or archiving.

## Preservation and References

Raw source data is immutable. Do not hand-edit generated registries/private
schemas. Preserve checkpoints, figure-workflow folders and skill-owned archives.
A second active analysis route must update the entry point/governance documents.

- `references/project-yaml-template.yaml`: optional non-standard path index.
- `references/archived-run-readme-template.md`: archive provenance.
- `references/analysis-log-template.md` and
  `references/manuscript-log-template.md`: existing legacy expanded profiles only.

Deliver the initialized structure, reconstructed state or concise handoff the
user requested, identifying source files and validation status. Recommend a
machine split only when device capabilities affect the next action.
