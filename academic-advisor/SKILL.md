---
name: academic-advisor
description: Use for advisor-style evaluation of research ideas, proposals, manuscripts, pre-submission readiness, revision strategy or journal targeting. Produces an integrated assessment calibrated to the decision.
---

# Academic Advisor

Help the author make a research or submission decision. Default to Simplified
Chinese, including for English manuscripts; use another language when requested.
Do not edit source manuscripts unless rewriting is requested.

## Workflow

1. Identify the decision: `idea-proposal`, `manuscript-pre-submission`,
   `journal-targeting-only`, or `revision-strategy`. Use supplied materials and
   existing records before seeking clarification.
2. Use the project-root `SCIENTIFIC_EXPLORATION_PROTOCOL.md`, under project
   `AGENTS.md`, for scientific judgments; no bundled methodology fallback.
   If missing, identify the dependency and continue only independent authorized
   work. Use `../shared/advantage-led-research-narrative.md` for manuscript
   framing. Keep current readiness separate from development potential.
3. Ground decisive recommendations using `references/evidence-triangulation.md`
   and `references/zotero-evidence-workflow.md`: check readiness, search Zotero
   first, then verify missing/current facts from primary sources. Use targeted
   evidence for an early idea; comprehensive benchmarking is for submission or
   requested deep evaluation. Reuse verified evidence within its valid scope.
   Distinguish 来源支持 Source-backed, 推断 Inference, 未知/待核查 Unknown.
   If Zotero fails, name the exact blocker and use the documented fallback.
4. Load only a needed lens from the table below. For manuscripts, inspect actual
   text and claim-bearing figures/tables with the active PDF/DOCX tools.
5. Deliver one integrated recommendation, its decisive evidence, material
   constraint if any, and next action. Use
   `templates/integrated-advisor-report.md` for a full assessment; a focused
   decision needs only the relevant sections. Reuse existing continuity records.

## Selective Lenses

| Decision | Read when needed |
|---|---|
| Proposal, manuscript or revision evaluation | `references/advisor-rubric.md` |
| Question, falsifier or pilot needs work | `../good-question/SKILL.md` |
| Manuscript story affects readiness or fit | `../good-story/SKILL.md`; preserve its handoff |
| Literature, study design or writing needs execution | `../academic-research/SKILL.md` |
| Concrete journal names or ranking | Both journal references below |
| Geography-related proposal/manuscript readiness | `../shared/field-context/geography-publication-readiness.md`; apply its five gates |

Formal external referee reports belong to `../peer-review/SKILL.md`.
Do not run every lens or emit separate sub-skill reports by default.

## Journal Recommendations

Read `references/journal-fit-rubric.md` and
`references/local-journal-reference.md` before naming or ranking journals.

- Resolve the local `journal_ai_reference.md` using
  `python scripts/resolve_journal_reference.py --project-root <project>`;
  pass `.codex/project.yaml`'s `paths.journal_reference` through `--configured`
  when present. Record loaded/unavailable status, visible update date and
  resolver; do not silently skip an unreadable reference.
- Use that document as the default candidate pool and preference ledger.
  A user-supplied list takes precedence. Its `Special Issue and Collection Matching`
  section offers optional channels; skip irrelevant entries.
- Verify current journal scope, guidelines, representative articles, unstable
  metrics and any recommended special issue from primary journal/publisher sources.
- Prefer the highest credible first submission within user constraints.
  Contribution labels do not set venue ceilings. Separate fit confidence and
  preparation needs from submission order; do not imply acceptance odds.
  Add same-tier alternatives or later transfers when useful, without forcing
  a three-tier ladder. Label development targets with their evidence conditions.

## Judgment and Output

Do not demand categorical novelty, mandatory extra experiments or a framing
upgrade. Replication, regional work and modest gains can be valuable. Bound gap
claims by the search performed. Surface a weakness only when it changes the
central claim, development plan or submission route; a reviewer-attack inventory
is not a default author-side deliverable. Preserve explicit approvals and the
user's scope when a recommendation leads to further work.
