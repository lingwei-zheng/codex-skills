# Claude Code Adapter

This adapter packages Engineering Figure Agent as a Claude Code skill. It is intended for local repository work where Claude Code can inspect paper text, method notes, code, data tables, and existing figure drafts.

## Install As A User Skill

PowerShell:

```powershell
$target = "$env:USERPROFILE\.claude\skills\engineering-figure-agent"
New-Item -ItemType Directory -Force $target | Out-Null
Copy-Item -Recurse -Force adapters\claude-code\skills\engineering-figure-agent\* $target
Move-Item -Force "$target\CLAUDE_SKILL.md" "$target\SKILL.md"
```

macOS/Linux:

```bash
mkdir -p ~/.claude/skills/engineering-figure-agent
cp -R adapters/claude-code/skills/engineering-figure-agent/* ~/.claude/skills/engineering-figure-agent/
mv ~/.claude/skills/engineering-figure-agent/CLAUDE_SKILL.md ~/.claude/skills/engineering-figure-agent/SKILL.md
```

The adapter keeps its Claude Code skill file as `CLAUDE_SKILL.md` inside the Codex skill repository so Codex does not register it as a second local skill with the same name.

## Use

```text
Use the engineering-figure-agent skill. Create a figure brief, choose image or plot mode, and produce the prompt or exact plot request for this paper figure.
```

Chinese:

```text
使用 engineering-figure-agent skill。先整理 figure brief，再判断 image mode / plot mode，最后生成工程论文配图 prompt 或精确定量图请求。
```
