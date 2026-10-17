# Selective Quality Control

Use this reference for reading plans, paper outlines, drafting, revision, and
submission preparation. It adapts quality control to the current research stage
instead of treating every task as a full audit.

## Reading Scope

For PDFs or long manuscripts, accept an explicit `read_scope`:

```yaml
pages: 1-8, 21-25
sections: Introduction, Results, Discussion
figures: 1-3
supplements: none
```

Review the requested scope first. Disclose what was not read or visually
inspected. Expand only when a central claim depends on material outside scope.

## Impact-First Checks

Prioritize:

1. central research question and contribution;
2. primary results, figures, and tables;
3. load-bearing method and measurement choices;
4. claims that determine the abstract, title, or conclusion;
5. changed, stale, disputed, or weakly sourced citations.

Sample lower-impact prose and references. Do not create an issue quota or audit
every sentence at equal depth.

Calibrate severity to field norms and consequence:

- `block` only when a defect invalidates a central result or inference;
- `repair` when it could materially alter interpretation or credibility;
- `note` for optional extensions and reporting preferences.

## Skeleton-First Drafting

Before full prose, read `../../shared/advantage-led-research-narrative.md` and
make a compact narrative brief:

| Leading advantage | Winning arena | Decisive evidence | Conditions where it matters | Non-story material |
|---|---|---|---|---|

Then make a compact claim skeleton:

| ID | Paragraph or section function | Claim | Evidence | Argument job | Material condition, if any |
|---|---|---|---|---|---|

Use topic sentences or claim slots to test sequence and coherence before
expanding prose. TEEL, CARS, or another rhetorical pattern may help a particular
paragraph, but no single pattern, paragraph length, or paragraph count is
mandatory across a manuscript.

A disposable `Draft 0` can be useful when the argument is unsettled. It is not
required for short edits, mature sections, or formats where the structure is
already fixed.

For empirical papers, treat the early Introduction as provisional. After the
Results and main evidence stabilize, recalibrate the final Introduction so that
its gap, contribution, and roadmap promise only what the paper actually
delivers. Paragraph count and roadmap follow the argument and the user/venue
requirements; a six-paragraph layout is optional.

Order Results by final argument logic, not by the order in which analyses were
attempted. Each prominent experiment, model, figure, or table must establish,
explain, demonstrate, distinguish, or materially bound the central advantage.
Defer or demote checks with no current argument job.

## Revision Economy

Default to the smallest coherent patch:

1. map feedback to the affected claim, paragraph, figure, table, or section;
2. preserve verified text and citations outside that scope;
3. revise locally;
4. recheck the surrounding transition and contribution map;
5. compare central claims before and after.

Rewrite a whole section only when its argument order, evidence allocation, or
section purpose is unsound. Treat claim drift as an advisory author decision
unless it creates unsupported content or contradicts the evidence.

## Evidence Reuse

Reuse a verified citation ledger when source identity, version, and claim scope
are unchanged. Re-verify decisive, changed, disputed, or time-sensitive claims.
Never convert a bounded search into a universal novelty statement:

- preferred: `Within the databases, dates, and terms searched, we found...`
- avoid: `No previous study has ever...`

## Bounded Source-Method Assessment

When a source's design affects selection, interpretation, or citation, identify
the specific design choice and the condition under which it changes the claim.
Distinguish an author-acknowledged limitation (with page/section locator) from
a reader-inferred concern (label the inference and uncertainty). For a claim
that a safeguard is absent, state which methods/supplement sections were
checked; absence from an abstract is not absence from the study. An abstract-only
read cannot support a full-methods review. Use no weakness quota or mandatory
per-paper matrix. Keep this diagnosis internal unless it materially changes
the manuscript's interpretation or required reporting.

## Optional Acronym Check

For long manuscripts or a requested terminology/terminal consistency check,
use the read-only helper when useful:

```text
python ars/scripts/check_acronyms.py --input manuscript.md --scopes body,abstract_en,abstract_zh --lang en --json-out acronym-report.json
```

Run from the academic-research skill directory; choose only scopes present in
the manuscript. See `--help` for headings, allowlists, and parser limits. Body
and each abstract are independent definition scopes. Review undefined, late,
and repeated definitions in context; findings are advisory and never a new
submission gate. `not_checked`/partial coverage is not a clean pass. The tool
does not modify the manuscript or call a model. Explain findings in the user's
language; its optional `zh-TW` report labels are not a manuscript language rule.

## Delivery

Report only:

- active stage and review scope;
- high-impact items checked;
- material gaps or blocking defects, not speculative reviewer attacks;
- local changes made;
- deferred checks and their triggers;
- any central claim drift requiring author confirmation.

## Claim Preservation In Revision

Use the shared narrative protocol's Revision Invariants on touched central
claims: preserve numbers/units, direction/negation, comparison conditions,
uncertainty, causal meaning, scope and citation ownership. Foregrounding a
supported advantage is ordinary editing; a material scientific change follows
existing author-decision rules. Removing redundant qualifiers is not itself
claim drift. Do not add a per-sentence approval gate or a universal verb ranking.

Missing factual support requires evidence, attribution, omission or an explicit
material gap. A hedge cannot substitute for evidence. Presentation quality,
source support, execution completion and reproducibility remain separate checks.
