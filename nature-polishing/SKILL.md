---
name: nature-polishing
description: Polish, translate or restructure academic prose into clear, concise Nature-leaning English; also supports a requested final human-style pass on already polished text.
---

# Nature-Style Academic Polishing

Improve scientific prose while preserving verified content. Nature-leaning means
clear, concise, evidence-led English; the user's journal/style takes precedence.

## Scope and Workflow

1. Use `formal-polish` by default. Identify the section's job and revise the
   smallest coherent unit. Repair local argument order before sentence style.
2. For tone or section-organization decisions, use the shared
   [manuscript style and structure](../shared/manuscript-style-and-structure.md).
   Load other references only for the identified problem (table below).
   For Chinese-to-English work, reconstruct propositions and logical relations
   rather than translating clause by clause.
3. Preserve numbers/units, formulas, citations, terminology, negation, comparison
   conditions, uncertainty, causal meaning and population/time/scale.
4. Compare touched claims against the source. For multi-section work, use
   `references/document-consistency.md`; check dependent abstracts, title and
   conclusion if a result or claim changes. Return self-contained text. Add notes
   when requested or needed to understand scientific meaning, use, validation
   status or a pending decision; apply routine editorial corrections directly.

## Scientific and Language Boundaries

- Do not invent evidence, mechanisms, references or novelty, upgrade association
  to causation, or broaden generalisability. A missing material factual basis
  needs evidence or an explicit gap; a hedge does not supply support.
- Treat an accurate associational verb as a sufficient causal boundary.
  Use `exploratory` for post hoc/confirmatory status and `observational` for
  meaningful design distinctions, not automatic caution labels.
- Preserve supported claim strength. For whole-paper framing, Results/Discussion
  interpretation or central-claim edits, read
  `../shared/advantage-led-research-narrative.md` and reuse existing decisions,
  evidence and exclusions. Substantive question/evidence redesign belongs to
  `academic-research` or `good-story`, within the authorized scope.
- Remove self-undermining comparison language when rhetorical; report material
  trade-offs precisely and retain required boundaries. Do not add a weakness,
  limitations or future-work quota, or hide a failed primary outcome.
- Avoid em dashes by default; preserve necessary hyphens, ranges and notation.

## Human Final Pass

Use `human-final-pass` only when requested for already polished text. Mention
its purpose once and continue; read all three `human-final-pass-*` references
before substantial changes. Natural variation is limited to Introduction,
related-work Literature Review, Results/result-facing Discussion, Conclusion
and Limitations. Protect Methods, formulas, tables, references, code, exact
technical claims and numeric statements. Never add grammar errors unless the
user explicitly enables grammar-error mode in the same request.

## References on Demand

| Need | Reference |
|---|---|
| Author-side style and section organization | `../shared/manuscript-style-and-structure.md` |
| Argument repair | `references/writing-strategy.md` |
| Optional Nature article patterns | `references/published-article-patterns.md` |
| Phrase-level and rhetorical moves | `references/section-moves.md` |
| Transitions, hedging or comparisons | `references/phrasebank-playbook.md` |
| Mechanics, register or integrity checks | `references/style-guardrails.md` |
| Defensive wording | `references/defensive-phrasing.md` |
| Cross-section consistency | `references/document-consistency.md` |
| Updating manuscript deliverables after polishing or Word feedback | [Paper review and submission workflow](../md-to-docx/references/paper-review-and-submission.md) |
| Human pass policy, eligibility and intensity | `references/human-final-pass-policy.md`, `references/human-final-pass-targeting.md`, `references/human-final-pass-calibration.md` |

Return polished prose without a fixed revision-note quota. Use Original /
Polished / Why changed when a side-by-side comparison is requested. For
document-level work, report unresolved conflicts, not full internal ledgers.
