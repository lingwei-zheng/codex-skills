# Intent Clarification Protocol — Codex Adaptation

Route by the requested deliverable and current conversation, not by the number
of material types. Apply [execution and approval scope](../../../references/execution-and-approval.md).

## Routing order

1. Read the current request, relevant earlier decisions, and available materials.
   Identify the deliverable, requested mode, and scope already authorized.
2. If the intended task is clear, use the matching workflow directly. A draft
   plus reviewer comments can be sufficient input for revision; an abstract plus
   literature can be sufficient input for checking the abstract's citations.
3. When a missing choice would materially change the deliverable, cost, or scope
   and cannot be resolved from context, ask one concise clarification. Use the
   question mechanism permitted by the current environment. Do not require the
   user to select internal agent names or pipeline terminology.
4. Continue independent authorized work while a necessary answer is pending.
   Do not infer an answer from silence or start dependent work before it arrives.

## Follow-ups and compatibility

- Interpret natural-language corrections and mode changes in any turn. Preserve
  the active task unless the user clearly changes it; do not require a new session.
- Prefer `/academic-research mode=<mode>` or natural language. Legacy `ars-*`
  tokens and `[direct-mode]` remain optional intent hints when explicitly supplied
  by the user; their position or capitalization must not force a redundant question.
  They are not approval tokens and do not bypass gates or resolve an unclear goal.
- Do not reclassify every internal phase handoff as a new intake request.
- A request for one deliverable does not authorize an entire research pipeline.
  Formal external review still routes to `peer-review` under the parent skill's
  routing boundaries; it does not authorize rewriting the submitted manuscript.

## Examples

| Request and context | Action |
|---|---|
| Draft + comments: "Revise this paper using these reviews" | Route to revision; do not ask merely because materials span phases |
| Abstract + papers: "Check that the abstract matches these sources" | Check the specified claims; do not start a full paper |
| "Write only an abstract" after earlier work | Reuse the supplied content and language decisions; no full-paper intake |
| "Here is some material, see what you can do" with no settled goal | Ask which deliverable is wanted |
| "Actually, only give me the outline" in a later turn | Narrow to the outline using the existing context |
| "Continue" with a new unapproved finalization decision | Present the concrete pending decision; do not treat earlier approvals as its approval |
