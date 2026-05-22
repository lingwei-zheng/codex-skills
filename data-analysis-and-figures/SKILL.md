---
name: data-analysis-and-figures
description: Default entry point for academic data analysis and empirical figure production in Python or R, especially for geography, human geography, GIScience, health geography, spatial analysis, quantitative social science, and environmental or public-health datasets. Use when the user asks to analyze data, inspect results, run statistical or spatial methods, make charts, build reproducible Python/R workflows, create publication-ready plots, or interpret analysis outputs before writing results/discussion. Routes spatial-method decisions to NORA spatial-analysis and publication figure polishing to nature-figure when appropriate.
---

# Data Analysis And Figures

Use this skill as the default workbench for empirical analysis and chart production. It covers code, diagnostics, interpretation, and reproducible figures. It is not a manuscript-writing skill; hand off to writing skills after the analysis claims are stable.

## Core Workflow

1. Clarify the analysis unit:
   - dataset paths and formats;
   - spatial unit, temporal unit, outcome, predictors, grouping variables;
   - target claim or question;
   - required language: Python, R, or either;
   - final output: exploratory notes, clean tables, figures, scripts, or manuscript-ready interpretation.
2. Inspect data before modeling or plotting:
   - schema, CRS, missingness, ranges, units, duplicates, and joins;
   - spatial coverage and projection when geometries are involved;
   - whether data support the requested claim.
3. Choose the analysis path:
   - ordinary tabular/statistical analysis -> Python/R directly;
   - spatial autocorrelation, accessibility, GWR/MGWR, spatial regression, spatial joins, buffers, raster/vector workflows -> read NORA `skills/spatial-analysis/SKILL.md`;
   - publication multi-panel empirical figures -> use `nature-figure` for export, layout, and journal-quality checks;
   - algorithm/system/benchmark figures -> route to `engineering-figure-agent`.
4. Run analysis reproducibly:
   - prefer scripts or notebooks already present in the project;
   - keep generated outputs under project-local `output/`, `figures/`, or the existing project convention;
   - record assumptions, filters, and derived variables.
5. Interpret only what the analysis supports:
   - distinguish descriptive patterns, associations, model estimates, and causal claims;
   - report uncertainty, sensitivity, and limitations;
   - flag weak evidence before prose polishing.

## Python And R Defaults

- Use Python for GeoPandas, rasterio, xarray, PySAL, scikit-learn, statsmodels, seaborn, matplotlib, plotly, and data pipelines already in Python.
- Use R for tidyverse, sf, terra, tmap/ggplot2, lme4, fixest, mgcv, INLA, or projects already written in R.
- Do not translate a working project from Python to R or R to Python unless the user asks or the existing toolchain cannot complete the task.
- For exact published values, generate charts from data or tables, not from image prompts.

## Figure Rules

- Use code-generated plots for numeric results.
- Use vector formats (`svg`, `pdf`) plus high-resolution `png` or `tiff` when publication export is required.
- Keep figure text short and units explicit.
- Use colorblind-safe palettes and test that panels remain interpretable in grayscale when the figure is for publication.
- Do not use `image_gen` for axes, p-values, map geometry, scale bars, or numeric chart shapes.

## Results And Discussion Handoff

After analysis, produce a compact evidence handoff before writing:

- main empirical finding;
- data subset and model/plot supporting it;
- uncertainty or robustness status;
- what cannot be claimed;
- figure/table paths;
- suggested Results paragraph points;
- suggested Discussion implication points.

For prose:

- use `academic-research-suite` when the task is claim-evidence organization;
- use `journal-adapt` when the writing must match a target journal or corpus;
- use `nature-polishing` only for style, clarity, or English polishing.

## Boundaries

- Do not run NORA full pipelines for ordinary data analysis unless the user asks for full research automation.
- Do not use `nature-figure` for conceptual framework figures.
- Do not fabricate data, results, citations, or statistical significance.
- If important data or metadata are missing, state the blocker and continue with exploratory analysis only when clearly marked.
