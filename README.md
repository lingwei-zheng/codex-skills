# Codex Skills Sync

This repository stores user-installed Codex skills for syncing across machines.

## Use On A New Machine

Clone this repository anywhere convenient, then run the platform installer to copy the managed skills into `~/.codex/skills`.

```bash
git clone <repo-url>
cd codex-skills
./install-mac.sh
```

On Windows PowerShell:

```powershell
git clone <repo-url>
cd codex-skills
.\install-windows.ps1
```

Notes:

- The Mac installer skips `docx` because Codex already provides the built-in `Documents` capability there.
- The Windows installer keeps `docx` available from this repository.
- Both installers copy top-level skills and supported `nora/skills/*` sub-skills into `~/.codex/skills`.
- Restart Codex after installation so it reloads the updated skills.

## Routine Sync

After changing skills on one machine:

```bash
cd /path/to/codex-skills
git status
git add <changed-skill>
git commit -m "Update Codex skills"
git push
```

On another machine:

```bash
cd /path/to/codex-skills
git pull
./install-mac.sh
```

## Policy

- Do not commit `.system/`; Codex manages system skills.
- Do not commit runtime outputs such as `output/`, `handoff.json`, `.checkpoints/`, or logs.
- Do not commit real API keys or machine-local config.
- Keep project-specific NORA outputs in project workspaces, not in the installed skill folder.
