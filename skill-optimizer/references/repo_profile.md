# Repo Profile

This repository is a compact skill repo, so optimize for a small number of files and a low cognitive load.

## Default Shape

- `SKILL.md`: the only required entry point.
- `agents/openai.yaml`: UI metadata for the skill.
- `scripts/`: deterministic checks or transformations.
- `references/`: stable guidance and audit rules.
- `assets/`: only when the skill needs output artifacts.

## Preferred Style

- Keep the folder shallow.
- Keep instructions imperative and short.
- Use references for details that do not need to load every time.
- Use scripts for logic that should not be retyped.
- Remove anything that only helps a human browse the repo but does not help Codex execute the task.

