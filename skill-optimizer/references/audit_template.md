# Skill Audit Template

Use this checklist when reviewing a skill folder.

## Structure

- `SKILL.md` has only `name` and `description` in frontmatter.
- File names are lowercase and hyphenated.
- References are one level deep from `SKILL.md`.
- The folder contains no unnecessary helper docs.

## Redundancy

- No repeated explanation across files.
- No duplicated examples.
- No overlapping workflows in separate sections.
- No prose that repeats what a script can enforce.

## Maintainability

- Deterministic behavior lives in `scripts/`.
- Stable background knowledge lives in `references/`.
- The main file stays short enough to scan quickly.
