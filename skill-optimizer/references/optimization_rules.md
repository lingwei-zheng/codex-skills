# Optimization Rules

Use these rules when slimming a skill folder.

## Keep

- Trigger wording in `SKILL.md` frontmatter.
- The shortest workflow that still lets Codex do the job.
- One example only when it removes ambiguity.
- Deterministic logic in `scripts/`.
- Stable reference material in `references/`.

## Move Out

- Long examples.
- Duplicate guardrails.
- Variant-specific instructions.
- Schemas, command tables, and implementation notes.
- Any detail that is only occasionally needed.

## Delete

- Files that exist only for human convenience.
- Docs that restate the skill without adding execution value.
- Tutorials, setup notes, and changelogs unless they are operationally required.

## Consolidate

If two sections say the same thing:

1. Keep the shortest correct version.
2. Leave it in the most relevant file.
3. Remove the duplicate or replace it with a pointer.
