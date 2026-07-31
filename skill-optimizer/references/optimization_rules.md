# Optimization Rules

Use these rules when slimming a skill folder.

## Keep

- Trigger wording in `SKILL.md` frontmatter.
- Strictly valid YAML frontmatter. Prefer `description: >-` for long descriptions or any text containing `: `.
- The shortest workflow that still lets Codex do the job.
- One example only when it removes ambiguity.
- Deterministic logic in `scripts/`.
- Stable reference material in `references/`.

## Validate Discoverability

Before treating a skill as slash-callable, parse the frontmatter with a real YAML parser.
Do not rely only on string checks for `name:` and `description:`.

Common failure:

```yaml
description: This skill is read-only: it must not publish.
```

The `: ` after `read-only` can break YAML parsing and cause Codex to skip the skill.
Use:

```yaml
description: >-
  This skill is read-only and must not publish.
```

## Validate Scripts

For any skill containing executable scripts:

1. Parse Python scripts before running them.
2. Reject `eval`, `exec`, `os.system`, and `subprocess(..., shell=True)` unless
   the user explicitly accepts a documented need.
3. Flag hardcoded user-specific Windows, macOS, or Linux home paths.
4. Avoid script names that shadow Python standard-library modules.
5. Require at least one deterministic test, self-test, or validation script and
   run it.
6. Check local Markdown links and nested `SKILL.md` files.

See [script-contract.md](script-contract.md) for the executable contract.

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
