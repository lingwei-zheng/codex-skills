# Advantage-Led Research Narrative

Use this protocol for author-side question development, analysis planning,
experiment execution and interpretation, manuscript architecture, story diagnosis,
polishing, and submission strategy.
It governs emphasis, not scientific truth: build the paper around the strongest
honest advantage while preserving material evidence and required reporting.

## Research Continuity

Use the same compact record across author-side stages; reuse existing question
cards, contribution IDs (`C1`, `C2`), experiment IDs (`E1`, `E2`), and story
handoffs. In a minimal-paper project, keep the narrative in
`paper/writing_outline.md`, facts in `paper/methods_results.md`, and active
settings in the existing configuration. Do not create a parallel ledger.

| Field | Meaning |
|---|---|
| Research question | The problem the work actually addresses |
| Leading advantage and state | `candidate`, `supported`, or `needs-reframing` |
| Fair arena | Task, comparator, metrics, population, scale, resource budget |
| Claim / experiment / evidence | Existing C# and E# IDs, result locator and version |
| Retellable sentence | One evidence-supported contribution; conditional if planned |
| Material change | What new evidence changed and which claims/figures need updating |

These states describe evidence, not authorization or task completion. A
`supported` advantage is not a reproducibility verdict. Reuse the separate
story status and material verification status without promoting either.

- Design: good-question proposes a falsifiable advantage hypothesis; name the
  result that would support, narrow, or defeat it before treating it as a finding.
- Execute: record actual conditions and outcomes, including skipped work and
  consequential contrary evidence. An exit code or output file is not proof.
- Interpret: the main agent links validated observations to the claims they
  support. Mark a changed advantage `needs-reframing` until the evidence supports
  a revised scope; retain primary outcomes and label post hoc analyses.
- Write: good-story and the writer use the strongest supported advantage.
  Update dependent title, abstract, figures, and conclusion when it changes.
- Resume: compare current configuration and result versions with the record.
  Reconcile stale dependencies before drafting; do not silently reuse old claims.

Continue these transitions only within the user's requested scope and existing
approval rules. A run-only request ends with its requested results; a full
research-to-paper request continues through the authorized downstream work.

## 1. Lead With the Advantage

Identify one leading advantage that can carry the paper:

- a capability that was previously unavailable;
- a mechanism or explanation that becomes clearer;
- lower cost, effort, or data requirements;
- better scalability, transferability, or practical usefulness;
- a modest but credible improvement in measurement, implementation, evidence,
  or local decision value.

Supporting contributions may strengthen that advantage, but content that does
not help establish, explain, or use it should not compete for equal prominence.
Incremental value is valid; the task is to state precisely what improves and
for whom, not to manufacture categorical uniqueness.

## 2. Choose the Winning Arena

Define the task, comparator, metric, population, scale, and application setting
that best reveal the paper's real value. Do not require comprehensive dominance.
A credible paper may win on one decision-relevant dimension while trading off
another.

Changing the arena is legitimate when it follows the research purpose and is
declared consistently. It is not legitimate to:

- choose metrics after seeing results solely to hide a failed primary outcome;
- omit preregistered, protocol-required, or venue-required endpoints;
- use an unfair comparator or remove a relevant simple baseline;
- redefine the task in a way that makes the comparison scientifically empty.

A new useful metric discovered after inspecting results may motivate an
exploratory follow-up, but cannot silently replace the original primary metric.
Resource, deployment, or interpretability trade-offs require evidence for both
the cost and the benefit; do not invent an advantage to explain a lower score.

## 3. Carry the Advantage Through the Paper

Use one contribution thread from beginning to end:

`problem -> specific limitation in current practice -> proposed advance -> decisive evidence -> conditions where it matters -> consequence`

- Abstract and Introduction: problem -> specific gap -> core approach ->
  strongest supported result -> significance. The Introduction may briefly
  preview decisive findings; detailed analysis belongs in Results. Paragraph
  counts and roadmaps are optional unless the user or venue requires them.
- Results: order analyses by what the reader must believe, not by the order in
  which the project was performed.
- Discussion: explain where the advantage appears, why it is useful, and how it
  changes the relevant understanding or decision.
- Conclusion: core contribution -> decisive evidence -> memorable implication.
  Add no new defect, experiment, or unsupported claim. Repeat a material boundary
  only if omission would mislead or the venue requires it; no limitation quota.

Establish the contribution before discussing material boundaries. A boundary
belongs near the claim it changes, but a speculative vulnerability does not
deserve prominence merely because a reviewer could imagine it.

## 4. Give Every Analysis One Argument Job

Each experiment, model, table, or figure should do at least one of these jobs:

1. establish that the central approach or finding works;
2. explain where the advantage comes from;
3. demonstrate value in the target setting;
4. distinguish the most plausible alternative explanation;
5. define a condition that materially changes the central claim.

Use an experiment-job map:

| Analysis or figure | Argument job | Claim advanced | Decision if absent |
|---|---|---|---|
| ... | establish / explain / demonstrate / distinguish / bound | ... | keep / supplement / defer / remove |

Do not add robustness, sensitivity, subgroup, or ablation work without naming
which uncertainty it resolves. Defer checks that do not affect the current
draft's main interpretation.

Removing an analysis from the narrative means omit, demote, or defer its
presentation, not delete raw data, run records, required endpoints, or controls
needed to judge the central claim. Keep factual execution history separate
from the paper's argument order.

## 5. Do Not Expand the Paper's Burden of Proof

Before adding a weakness, caveat, or defensive sentence, ask:

- Does it change the truth, scope, or interpretation of the central claim?
- Is it required by the design, protocol, reporting standard, or venue?
- Does the current section need it to prevent a material overclaim?
- Does the sentence enlarge the paper's responsibility beyond what it claims?

If the first three answers are no, omit the sentence from the main narrative.
Avoid self-undermining language such as `unfortunately`, `merely`, `only`,
`still lags behind`, `failed to outperform`, or `performance degradation` when
it turns a non-central comparison into a general defect. If the comparison is
material, report it neutrally and specifically as a condition or trade-off.

Apply this semantically in Chinese as well: remove emotional judgments such as
`遗憾的是`; replace `明显落后` or `效果有限` with the specific material observation.
`仅需一种传感器` and `only 10 samples` may convey an advantage or necessary
sample information. Do not mechanically delete `仅`, `仍`, or `only`.

## 6. Write the Result Logic, Not the Project Diary

Reconstruct the paper around the conclusion the evidence now supports. It is
acceptable to redefine the question, reorder contributions, change figure
sequence, or narrow the central claim when the final evidence differs from the
initial plan. Preserve a chronological account only when the discovery process
itself is evidence.

## Revision Invariants

Compare touched central claims before and after revision: numbers and units,
direction and negation, comparison conditions, uncertainty, causal meaning,
population/time/scale, and citation ownership. Preserve supported strength in
both directions. A background citation must not become a finding of this study.
Use the existing claim ledger, not a universal ranking of verbs.

Reordering, emphasizing a supported advantage, and removing redundant qualifiers
may proceed as ordinary editing. Surface a material scientific change and use
existing authorization rules; no new sentence-by-sentence approval is required.
For an unsupported factual assertion, obtain support or attribution, omit a
nonessential assertion, or mark a material evidence gap. Adding `may` supplies
no evidence. Distinguish a hypothesis from an observed finding.

## Integrity Floor

Advantage-led writing never permits hiding evidence that materially overturns,
reverses, or sharply narrows the central claim. Preserve preregistered and
required outcomes, fair comparators, accurate uncertainty, and material design
limitations. Distinguish a genuine interpretation boundary from a list of every
conceivable reviewer attack. The former belongs in the paper; the latter belongs
in an internal decision ledger and is surfaced only when it changes the route.
