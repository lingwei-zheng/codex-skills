---
name: handoff
description: >-
  Use only when the user explicitly asks to hand off, compact, transfer, or
  summarize the current conversation for a fresh agent or later session. Create
  a concise temporary handoff document that points to existing artifacts,
  records unresolved work, and recommends relevant skills. Use sync instead for
  durable cross-device research-project state, directory initialization, or
  ongoing analysis and manuscript logs.
---

# Handoff

Compact the current conversation into a handoff document that lets a fresh
agent continue without reconstructing the task from chat history.

## Workflow

1. Infer the current objective, completed work, active decisions, verification
   state, unresolved issues, and next action from the conversation and available
   artifacts.
2. If the user provides arguments or a stated destination, treat them as the
   next session's focus and prioritize the handoff accordingly.
3. Write the document to the operating system's temporary directory, not the
   current workspace. Use a readable timestamped name such as
   `codex-handoff-YYYY-MM-DD-HHmm.md`.
4. Reference existing specs, plans, ADRs, issues, commits, diffs, reports, and
   files by path or URL. Do not duplicate their full content.
5. Redact API keys, passwords, tokens, personal data, private identifiers, and
   other sensitive information. Prefer a description of where a secret is
   configured over reproducing its value.
6. Include a `Suggested skills` section with only the skills the next agent is
   likely to need.
7. Report the handoff path and a one-sentence summary. Do not modify project
   files unless the user separately requests it.

## Document Shape

```markdown
# Handoff

## Objective
## Current state
## Decisions and constraints
## Artifacts and changed files
## Verification performed
## Unresolved work and risks
## Next action
## Suggested skills
```

Keep the document concise and operational. Distinguish verified facts from
assumptions, and disclose any command, test, file, or source that was not
checked.
