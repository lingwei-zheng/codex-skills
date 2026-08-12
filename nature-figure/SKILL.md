---
name: nature-figure
description: >-
  Submission-grade scientific figure workflow for Python or R. Use when the
  user asks to create, revise, audit, or polish empirical manuscript figures,
  statistical plots, static publication maps, multi-panel evidence figures, or
  journal-ready SVG/PDF/TIFF outputs, including R interaction, moderation,
  conditional-prediction, simple-slopes, and Johnson-Neyman plots. Define the
  figure claim, evidence logic, export contract, and review risks before
  plotting. If the user has not chosen Python or R, ask "Python or R?" and stop.
  Use only the selected backend for generation, previewing, exporting, and
  visual QA. Not for dashboards, engineering schematics, or illustration-first
  infographics.
---

# Nature Figure

Build publication figures as visual arguments. Every figure starts from a claim,
an evidence hierarchy, and a review-risk check before code or aesthetics.

## Boundary

Use this skill for:

- empirical and statistical plots;
- multi-panel results figures;
- static publication maps and spatial evidence figures;
- image plates with quantitative evidence;
- journal-ready SVG, PDF, TIFF, and preview exports.

Use `engineering-figure-agent` for system architecture, workflows, mechanisms,
hardware schematics, and illustration-led diagrams. Use
`conceptual-figure-workflow` first when theory, variables, mechanisms, or
claim-evidence boundaries still need review.

Do not use this skill for interactive dashboards, full GIS data-processing
workflows, 3D production, or Illustrator/Figma-first infographics. A static map
that carries a manuscript claim belongs here even when its source data were
prepared in GIS software.

## Blocking Backend Gate

If the current request does not specify Python or R and does not provide an
unambiguous language-specific workflow, ask **Python or R?** and stop. Do not
write plotting code, create mock data, or choose a backend by default.

After selection:

- use the chosen backend for every plot, preview, export, and visual QA render;
- do not substitute the other backend when a runtime or package is missing;
- report the exact blocker and provide selected-backend installation or run
  guidance;
- use the other language only for non-visual data inspection or conversion.

Mentioning R code, an R model object, `lme4`, or the `interactions` package is an
unambiguous R selection. Do not ask the backend question again.

Read [references/backend-selection.md](references/backend-selection.md) when the
user asks for a recommendation or backend details.

## Workflow

1. **Define the contract.** Read
   [references/figure-contract.md](references/figure-contract.md). State the core
   conclusion, evidence chain, figure archetype, target size, panel map,
   statistics, source data, export formats, and strongest reviewer risk.
2. **Select the minimum evidence.** Give every panel a unique claim-bearing role.
   Remove or merge panels that do not change what the reader can conclude.
3. **Load the relevant track.** Use Python references for Python; use
   [references/r-workflow.md](references/r-workflow.md) for R. For a static map
   or spatial figure, also read
   [references/geospatial-figure-contract.md](references/geospatial-figure-contract.md).
   For an interaction or moderation result, read
   [references/interaction-moderation-track.md](references/interaction-moderation-track.md)
   and use `interactions` as the only interaction-analysis plotting interface.
4. **Build reproducibly.** Keep source data, plotting code, statistics, labels,
   dimensions, colors, and export settings traceable.
5. **Integrate the layout.** Use one restrained visual vocabulary, stable method
   colors, readable hierarchy, and direct labels when they reduce eye travel.
6. **Write the legend when in scope.** Read
   [references/figure-legend-contract.md](references/figure-legend-contract.md)
   and keep the title, panel descriptions, statistics, and source-data wording
   aligned with the actual evidence and target journal.
7. **Export with the selected backend.** Produce the requested editable and
   raster formats at final dimensions.
8. **Verify.** Read [references/qa-contract.md](references/qa-contract.md) and
   inspect the rendered outputs at final size.

## Quality Rules

- Never fabricate values, sample sizes, statistics, maps, or source data.
- Preserve the distinction between association, prediction, mechanism, and
  causation.
- Prefer one dominant evidence panel with subordinate validation or robustness
  panels when the evidence hierarchy supports it.
- Keep backgrounds white except where image data require a dark field.
- Avoid rainbow palettes and color-only distinctions that fail in grayscale or
  for color-vision deficiencies.
- Define `n`, center, spread, tests, corrections, and source-data provenance.
- Preserve editable text in vector outputs when the selected backend supports it.
- Do not disclose private paths, filenames, or internal template provenance
  unless the user explicitly requests an audit trail.

## Reference Router

| Reference | Read when |
|---|---|
| [references/figure-contract.md](references/figure-contract.md) | Define claim, evidence hierarchy, panel map, and reviewer risks |
| [references/backend-selection.md](references/backend-selection.md) | Select or troubleshoot Python/R |
| [references/r-workflow.md](references/r-workflow.md) | Use R, ggplot2, patchwork, or ComplexHeatmap |
| [references/interaction-moderation-track.md](references/interaction-moderation-track.md) | Plot R interaction, moderation, conditional prediction, simple slopes, or Johnson-Neyman results with `interactions` |
| [references/geospatial-figure-contract.md](references/geospatial-figure-contract.md) | Build a static map or spatial evidence figure |
| [references/figure-legend-contract.md](references/figure-legend-contract.md) | Write or audit figure/table legends and statistical caption details |
| [references/qa-contract.md](references/qa-contract.md) | Export and final visual/statistical checks |
| [references/design-theory.md](references/design-theory.md) | Typography, color, layout, and export rationale |
| [references/api.md](references/api.md) | Python helpers, palettes, and validation APIs |
| [references/common-patterns.md](references/common-patterns.md) | Python layout patterns and mixed-modality panels |
| [references/nature-2026-observations.md](references/nature-2026-observations.md) | Nature-family page and panel archetypes |
| [references/tutorials.md](references/tutorials.md) | End-to-end examples |
| [references/chart-types.md](references/chart-types.md) | Less common chart patterns |
| [references/demos.md](references/demos.md) | Bundled figures4papers demos and previews |

Load only the references needed for the selected backend and current figure
task. Do not open the entire reference collection by default.

For geography, GIScience, health geography, or GeoAI work, load only the relevant
files from `../shared/field-context/`.

## Output

Deliver the figure contract, source-data or input assumptions, selected-backend
script, requested exports, and a concise QA verdict. State any missing dependency
or unverified visual/statistical condition.
