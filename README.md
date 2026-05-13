# Codex Skills Sync

This repository stores user-installed Codex skills for syncing across machines.

## Use On A New Machine

Clone this repository into the Codex skills directory:

```bash
mkdir -p ~/.codex
git clone <repo-url> ~/.codex/skills
```

If `~/.codex/skills` already exists, clone elsewhere and copy/merge the skill folders manually.

## Routine Sync

After changing skills on one machine:

```bash
cd ~/.codex/skills
git status
git add <changed-skill>
git commit -m "Update Codex skills"
git push
```

On another machine:

```bash
cd ~/.codex/skills
git pull
```

## Policy

- Do not commit `.system/`; Codex manages system skills.
- Do not commit runtime outputs such as `output/`, `handoff.json`, `.checkpoints/`, or logs.
- Do not commit real API keys or machine-local config.
- Keep project-specific NORA outputs in project workspaces, not in the installed skill folder.
