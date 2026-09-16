# Minimal Paper Project Governance

Use this reference when a project contains `analysis/config.yaml`, `paper/` with
the three core Markdown files, and `results/`.

## Path contract

| Path | Role | Update when |
|---|---|---|
| `analysis/config.yaml` | Active analysis settings, labels, scope boundaries, and writing contract | A model, variable, time window, term, or inference rule changes |
| `analysis/01_*` onward | One ordered reproduction flow | A computation or analysis order changes |
| `analysis/07_validate.py` | Reproducibility and governance checks, when present | A required invariant or result check changes |
| `paper/methods_results.md` | Methods and numerical results in execution order | A method, sample, estimate, or result interpretation changes |
| `paper/research_assessment.md` | Advisor assessment, evidence ledger, contribution risk, journal ladder | Positioning, novelty evidence, or journal strategy changes |
| `paper/writing_outline.md` | Story spine, section plan, figures/tables, terminology, and claim limits | Writing logic or manuscript boundaries change |
| `results/` | Generated tables, registries, manifests, and validation verdict | Analysis is rerun or validated |
| `README.md` | Short project entry point and reproduction commands | The active flow or top-line conclusion changes |

## Language contract

The three governance documents are a single language-controlled set. Infer the
documentation language from the user request and the project configuration. If
the project language is Chinese, keep all prose and headings in Simplified
Chinese in `paper/methods_results.md`, `paper/research_assessment.md`, and
`paper/writing_outline.md`. Keep technical identifiers, code, file paths,
journal names, citation keys, URLs, and necessary abbreviations unchanged, but
translate their surrounding explanations. Check all three files together after
any language or structure change.

## Resume protocol

1. Read `README.md` to identify the one active question and reproduction order.
2. Read `analysis/config.yaml` before interpreting any result labels.
3. Read `paper/methods_results.md` to recover the factual analysis state.
4. Read `paper/research_assessment.md` to recover the contribution and submission
   boundary.
5. Read `paper/writing_outline.md` before drafting or restructuring prose.
6. Inspect `results/` and run validation before reporting the project as current.

## Synchronization rules

- Keep the three core documents mutually consistent; a change to one may require
  a check of the other two.
- Preserve one main analysis line. Supporting robustness and pathway analyses are
  subordinate branches, not separate papers or competing workflows.
- Do not describe discarded development paths as part of the paper's main text.
- Keep the project's stated daytime window, sample definitions, and observational
  claim boundary intact unless the analysis and all three documents are updated.
- Treat journal advice as a recommendation ledger, not a submission decision.

## Change handoff

At the end of a work block, report the changed paths, validation verdict, and the
next writing or analysis action in the final response. Do not create a separate
handoff log when the project uses this minimal profile.

## Research Continuity

Use [the shared continuity record](../../shared/advantage-led-research-narrative.md#research-continuity)
inside the existing three documents. Keep the advantage state, fair comparison,
C#/E# evidence map, result/configuration versions, and retellable sentence in
`paper/writing_outline.md`. Keep actual execution, skipped units and contrary
observations in `paper/methods_results.md`; do not copy execution chronology into
the manuscript structure. Update the assessment only when positioning changes.

Before continuing a draft, compare its evidence dependencies against the active
configuration and result artifacts. Mark stale claims for reconciliation rather
than silently promoting an earlier finding. Distinguish candidate/support status
from verification and approval status. Use the experiment workflow's study-state
reference only for multi-session human-study management; no duplicate handoff log.
