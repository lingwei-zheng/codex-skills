---
name: peer-review
description: Use when reviewing an academic journal manuscript, referee report, peer-review PDF, manuscript plus supplementary materials, or when the user wants a structured journal review with critical, important, and minor revisions. This skill uses the academic-research reviewer workflow, local geography/GIScience/health geography field context when relevant, and pdf/docx tools for manuscript and visual-material inspection. Chinese outputs default to Simplified Chinese.
---

# Journal Peer Review

Produce a rigorous external-reviewer assessment from the manuscript and all
available supplementary materials.

This is a submission-stage external review and therefore uses comprehensive
rigor. Do not export its full robustness burden backward into exploratory or
first-draft workflows; those are calibrated by
`../shared/research-calibration.md`.

## Review Stack

1. Read `../academic-research/SKILL.md` and use its
   `academic-paper-reviewer` workflow as the main review framework.
2. Use `../shared/field-context/` only for geography, human geography,
   GIScience, GeoAI, remote sensing, spatial analysis, environmental exposure,
   or health geography. Do not assume NORA is installed.
3. Use the active PDF and DOCX skills for extraction, media inspection,
   rendering, and visual review.
4. Read [references/report-structure.md](references/report-structure.md) before
   drafting the final reports.

## Non-Negotiable Visual Rule

Do not finalize a review from extracted text alone when figures, maps, diagrams,
tables, equations, statistical charts, or supplementary visuals support the
claims. Attempt visual inspection first. If it cannot be performed, disclose
exactly what was not inspected and how that limits the review.

Chinese working reports default to Simplified Chinese. Use Traditional Chinese
only when explicitly requested.

## Workflow

### 1. Discover Materials

- Identify the main manuscript and every supplementary file.
- Read `.codex/project.yaml` when present.
- Record what was reviewed, rendered, visually inspected, or unavailable.

### 2. Inspect Text And Evidence

- For PDFs, combine text extraction with rendered-page inspection.
- For DOCX, inspect OOXML and embedded media when relevant.
- Inspect central figures, maps, tables, plots, diagrams, equations, and
  supplementary evidence supporting key claims.
- Track whether each concern arises from text, captions, visual evidence,
  supplements, methods, statistics, or domain reasoning.

### 3. Run Independent Review Lenses

Assess field and journal fit, research question, contribution, method validity,
reproducibility, sampling, representativeness, statistical assumptions,
figure/table evidence, claim-evidence alignment, causal language, limitations,
ethics, and data access. Preserve independent lenses before synthesis.

For relevant geography manuscripts, read only the needed field references:

- `geography-publication-readiness.md` for the five publication gates and
  desk-reject risk.
- `spatial-methods.md` for scale, spatial units, MAUP, dependence, and validity.
- `environmental-health.md` for exposure and outcome pathways.
- `geoai-domain.md` for GeoAI or geospatial machine learning.
- `journal-templates/` for venue fit.

Use a devil's-advocate pass to identify the strongest rejection risk. Explicitly
test whether a location change has cumulative, transferability, policy,
measurement, or boundary-condition value; do not reject it for similarity
alone. Also test method stacking without inferential gain,
theory-as-label, Discussion restatement, and title overpromise when relevant.

### 4. Triage And Draft

Separate the single highest-risk critical issue from important and minor issues.
Follow user-specified counts when provided; otherwise use the defaults in
[references/report-structure.md](references/report-structure.md). Base the
editorial recommendation on fixability, not tone or preference.

Bind every critical and important issue to an inspectable evidence pointer:
page, section, paragraph, figure, table, equation, supplement, or exact claim.
State whether the concern is directly observed, inferred from the manuscript, or
cannot be verified from the available files. Do not use a vague topic label as
the evidence for a major criticism.

### 5. Verify

Before delivery, confirm that visual inspection or its limitation is disclosed,
the critical issue is singular, issue counts are respected, geography gates were
applied when relevant, every critical and important issue has an evidence
pointer, and user-edited files were not overwritten.

## Output

Create only the report set the user needs. Use
[references/report-structure.md](references/report-structure.md) as the source of
truth for filenames, section structure, issue hierarchy, decision standards,
tone, and final report checks.
