---
name: nature-polishing
description: Polish, restructure, translate, or humanize academic prose into Nature-leaning English using writing-strategy principles, curated Nature/Nature Communications article patterns, and phrase-level support from Academic Phrasebank. Use whenever the user asks to polish a manuscript paragraph, abstract, introduction, results, discussion, conclusion, title, methods section, or Chinese academic draft for publication-quality English, or when the user wants an already polished paper to sound less mechanical through a controlled final human-style pass.
---

# Nature-Style Academic Polishing

Improve scientific prose without changing its verified scientific content. Treat
`Nature-leaning` as concise, evidence-led, readable academic English, not as an
instruction to imitate a journal mechanically. Follow the user's target journal,
house style, and explicit preferences when they differ from the defaults here.

## Modes

Choose the smallest mode that matches the request.

- `formal-polish`: default mode for translation, restructuring, section rewriting,
  clarity, concision, academic register, and publication-quality English.
- `human-final-pass`: use only after formal polishing when the user wants credible
  academic prose that sounds less mechanical.

For `human-final-pass`:

- Mention once that it is intended for already polished text, then continue.
- Preserve facts, citations, formulas, LaTeX, numbers, technical terms, and claims.
- Apply natural variation only to eligible prose in Introduction, related-work
  Literature Review, Results or result-facing Discussion, Conclusion, and
  Limitations.
- Do not humanize Methods, formulas, tables, references, code, exact technical
  claims, or numeric statements.
- Never add grammar errors unless the user explicitly enables grammar-error mode
  in the same request.
- Read the three `human-final-pass-*` references before making substantial changes.

## Non-Negotiable Boundaries

- Repair argument and section logic before sentence style.
- Do not invent data, references, mechanisms, evidence, or novelty claims.
- Do not upgrade association to causation or broaden generalisability.
- Do not alter verified quantitative values, citations, formulas, or terminology.
- Do not hide a weak core argument under fluent prose. State material gaps plainly.
- If the central research question, evidence interpretation, or paper story needs
  substantive redesign, diagnose the problem and hand it to `academic-research`
  or `good-story`; do not solve it by silently changing the science during
  polishing.
- Prefer direct, information-dense claims over `we do not claim`, `this does not
  mean`, or `our purpose is not ... but ...`.
- Keep a limitation when removing it would overstate the evidence. Place it where
  it clarifies interpretation rather than leading a contribution-heavy sentence.
- Avoid em dashes as prose punctuation unless the user requests them.
- Use hyphens for compound modifiers and en dashes only for ranges or established
  forms. Do not create forms such as `mobility–based` or `indoor–outdoor`.

## Workflow

1. **Establish the target.** Identify the paper type, section, target journal or
   style, source language, requested depth, and whether the text is ready for
   `formal-polish` or `human-final-pass`.
2. **Diagnose before rewriting.** Check, in order:
   `paper type -> section job -> paragraph logic -> claim/evidence/boundary -> sentence style`.
3. **Load only the needed references.** Use the table below. Do not load every
   reference for a narrow sentence-level request.
4. **Rewrite at the highest necessary level.** Rebuild section or paragraph logic
   when needed; otherwise make the smallest wording change that solves the problem.
5. **Keep document-level state when needed.** For a whole manuscript, multiple
   sections, or repeated revision rounds, read `references/document-consistency.md`
   and maintain terminology and claim-strength ledgers.
6. **Preserve the evidence contract.** Keep claim strength aligned with the source,
   retain necessary uncertainty, and distinguish observation from interpretation.
7. **Run a final check.** Verify meaning, citations, numbers, terminology, section
   function, overclaim, defensive phrasing, punctuation, and target-journal fit.

## Reference Router

| Reference | Read when |
|---|---|
| [references/writing-strategy.md](references/writing-strategy.md) | Section or paragraph reasoning needs repair |
| [references/published-article-patterns.md](references/published-article-patterns.md) | An abstract, Introduction, Results, Discussion, Conclusion, or title needs article-level patterns |
| [references/section-moves.md](references/section-moves.md) | A specific section needs rhetorical moves or ordering |
| [references/phrasebank-playbook.md](references/phrasebank-playbook.md) | Hedging, transitions, evidence, comparison, limitation, or implication wording is needed |
| [references/style-guardrails.md](references/style-guardrails.md) | Mechanics, register, articles, numbers, sentence checks, integrity, or AI boundaries need review |
| [references/defensive-phrasing.md](references/defensive-phrasing.md) | Defensive disclaimers must be retained, compressed, or rewritten |
| [references/document-consistency.md](references/document-consistency.md) | A whole manuscript, multiple sections, or repeated rounds need stable terminology and claim strength |
| [references/human-final-pass-policy.md](references/human-final-pass-policy.md) | `human-final-pass` is active |
| [references/human-final-pass-targeting.md](references/human-final-pass-targeting.md) | Section eligibility or protected content is uncertain |
| [references/human-final-pass-calibration.md](references/human-final-pass-calibration.md) | Naturalness intensity or explicit grammar-error mode needs calibration |

## Compact Section Check

- `Introduction`: importance -> known context -> unresolved gap -> question or aim
  -> approach and contribution. Do not report Results prematurely.
- `Results`: report what was observed, where or when, and with what quantitative
  support. Keep interpretation limited and intentional.
- `Discussion`: explain what the findings add, how they relate to prior work, which
  mechanism is plausible, and where the interpretation may fail.
- `Conclusion`: contribution -> key evidence -> bounded implication. Add no new data.
- `Methods`: preserve reproducibility, assumptions, parameters, controls, software,
  and analysis details. Do not polish away necessary specificity.
- `Abstract`: context or problem -> gap or objective -> approach -> key results ->
  implication, unless the journal requires another structure.
- `Title`: accurate, searchable, evidence-supported, and no broader than the paper.

## Chinese-to-English Work

Extract propositions before translating. Reconstruct causal, contrastive,
qualifying, and inferential links instead of translating clause by clause. Keep
technical terminology stable and verify causality and hedging after reconstruction.

## Output

Unless the user requests another format, provide:

1. The polished text as plain prose.
2. `Revision notes:` with `3-5` short bullets covering substantive structural or
   stylistic changes.
3. A clear note when the rewrite changed section logic or exposed an unresolved
   evidence or argument gap.

For side-by-side requests, use `Original`, `Polished`, and `Why changed`.
For document-level work, report only unresolved terminology or claim-strength
conflicts unless the user asks to see the full ledgers.
