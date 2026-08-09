---
name: grill-me
description: >-
  Use only when the user explicitly asks to be grilled, interrogated,
  pressure-tested, or challenged about a plan, design, decision, or idea. Best
  for software, product, workflow, operational, or general project decisions
  with unresolved branches. Do not auto-trigger for routine planning,
  clarification, academic research-question development, proposal or manuscript
  evaluation, or literature review; use good-question or academic-advisor for
  those academic tasks unless the user explicitly invokes grill-me.
---

# Grill Me

Run a deliberate, stateless interview. Sharpen the user's idea through
decisions; do not turn the session into implementation or write project files
unless the user later requests that work.

## Protocol

1. Inspect available files, prior decisions, and environment facts before
   asking. Do not ask the user for information that can be discovered locally.
2. Map the subject as a **decision tree**: each decision may unlock dependent
   decisions.
3. Compute the current **frontier**: every unresolved decision whose
   prerequisites are already settled.
4. Ask the whole frontier as one numbered round. Do not place two questions in
   the same round when one answer could change the other question.
5. Give a recommended answer and the main tradeoff for every question. The
   user owns each decision; never answer it on their behalf.
6. After the user responds, update the tree, reopen branches affected by changed
   answers, recompute the frontier, and ask the next round.
7. Continue until the frontier is empty. Then summarize the settled choices,
   assumptions, remaining unknowns, and next action.
8. Ask the user to confirm that shared understanding has been reached. Do not
   act on the resulting plan before that confirmation.

Use this format:

```text
Q1 - <question title>: <question, with concise options when useful>

Recommendation: <recommended answer and main tradeoff>
```

## Boundaries

- Separate **facts** from **decisions**. Investigate facts with available tools;
  put decisions to the user and wait.
- Do not block the whole round on an independent fact lookup. Ask unaffected
  frontier questions while downstream branches wait for the fact.
- If a question cannot be settled through discussion, identify the needed
  prototype, pilot, observation, or evidence instead of manufacturing certainty.
- If the scope is too large for one coherent session, split it into smaller
  grillable units before continuing.
- If the user asks for one-question-at-a-time pacing, use that pacing while
  preserving the same decision-tree and dependency logic.
- For an explicitly requested academic grilling session, do not replace the
  evidence, falsifiability, pilot, and reviewer-risk checks in `good-question`
  or the integrated assessment in `academic-advisor`.
