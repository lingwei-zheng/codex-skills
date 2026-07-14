---
name: grill-me
description: >-
  Use only when the user explicitly asks to be grilled, interrogated,
  pressure-tested, challenged question-by-question, or requests a
  one-question-at-a-time interview about a plan or design. Best for software,
  product, workflow, operational, or general project decisions with unresolved
  branches. Do not auto-trigger for routine planning, ordinary clarification,
  academic research-question development, proposal or manuscript evaluation,
  or literature review; use good-question or academic-advisor for those
  academic tasks unless the user explicitly invokes grill-me.
---

# Grill Me

Use this as a deliberate interview mode, not as the default response to an
underspecified request.

1. Inspect the available files, codebase, and prior decisions before asking.
   Do not ask the user for information that can be discovered locally.
2. Identify the unresolved decision with the greatest effect on feasibility,
   scope, risk, evidence, cost, or reversibility.
3. Ask exactly one concise question at a time.
4. For every question, provide a recommended answer and briefly state the main
   tradeoff. Do not hand the decision back without guidance.
5. Follow dependencies through the decision tree. Revisit an earlier branch
   only when a later answer materially changes it.
6. Stop when the high-impact branches are resolved. Do not prolong the interview
   to cover cosmetic or easily reversible details.
7. Finish with a concise decision summary: settled choices, assumptions,
   remaining unknowns, and the next action.

If the user explicitly invokes this skill for an academic idea, it may conduct
the interview, but it should not replace the evidence, falsifiability, pilot,
and reviewer-risk checks in `good-question` or the integrated assessment in
`academic-advisor`.
