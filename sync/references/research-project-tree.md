# Research Project Tree

## Minimal single-analysis paper project (preferred)

```text
project/
  README.md
  AGENTS.md                         # optional local instructions
  .gitignore
  analysis/
    config.yaml
    01_*.py or 01_*.R
    02_*.R
    ...
    07_validate.py                  # when validation is available
  paper/
    methods_results.md
    research_assessment.md
    writing_outline.md
  results/
    machine-readable outputs
    run registries
    validation verdict
```

Conventions:

- `analysis/` is the only active analysis flow; numeric prefixes define order.
- `analysis/config.yaml` is the active computational and writing contract.
- `paper/methods_results.md` is the factual methods/results ledger.
- `paper/research_assessment.md` is the positioning and journal-fit ledger.
- `paper/writing_outline.md` is the story, structure, terminology, and claim-boundary ledger.
- `results/` contains generated outputs and validation artifacts; do not edit them by hand.
- `README.md` is the short entry point and reproduction command list.

## Expanded multi-branch project (compatibility)

```text
project/
  README.md
  data/raw/
  code/analysis/
  code/scripts/
  configs/
  output/current/
  output/archived_runs/
  paper/manuscript/current/
  paper/manuscript/versions/
  notes/analysis_log.md
  notes/manuscript_log.md
```

Use the expanded profile only when multiple active branches, dated archives, or
review packages make the minimal tree insufficient. Never recreate it during a
minimal-project resume without an explicit user request.
