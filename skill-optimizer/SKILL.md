---
name: skill-optimizer
description: Audit and slim down skill folders by removing redundant instructions, shortening SKILL.md, and moving detail into references or scripts. Use when Codex needs to refactor a skill repo, simplify its layout, dedupe content, or validate that a skill follows the compact OpenAI skill structure.
---

# Skill Optimizer

Optimize a skill folder for clarity, concision, and maintainability.

## Workflow

1. Inspect `SKILL.md`, `agents/openai.yaml`, `references/`, `scripts/`, and `assets/`.
2. Strictly parse `SKILL.md` frontmatter as YAML before judging discoverability.
3. Remove duplicate or overlapping instructions first.
4. Keep only core trigger info and the shortest usable workflow in `SKILL.md`.
5. Move detail into `references/` and repeatable logic into `scripts/`.
6. Delete docs that exist only for human convenience.
7. Recheck the folder with the audit script after every non-trivial edit.

## Keep In `SKILL.md`

- Trigger conditions in frontmatter `description`.
- YAML-safe frontmatter. If `description` contains `: `, use quotes or a `>-` block scalar.
- One short workflow.
- Any essential guardrails that change how Codex should act.

## Move Out

- Long explanations.
- Repeated examples.
- Schema, command, or policy details.
- Variant-specific guidance.
- Anything that can be enforced by a script.

## Repository Defaults

- Keep skill folders flat and shallow.
- Prefer one `SKILL.md`, one `agents/openai.yaml`, a small `scripts/` set, and only the references you actually need.
- Avoid adding `README.md`, `CHANGELOG.md`, or similar support docs unless a user explicitly asks for them.
- Keep references one level deep from `SKILL.md`.
- See [repo_profile.md](references/repo_profile.md) for the default shape this repo expects.

## Output Standard

When optimizing a skill, produce:

1. A short diagnosis of what changed.
2. A file map showing the final source of truth for each topic.
3. The patch or updated file content.
4. Any remaining ambiguity or validation gaps.
