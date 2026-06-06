---
name: conceptual-figure-workflow
description: Use when the user wants a conceptual framework figure, experiment design diagram, thesis framework, research mechanism diagram, theoretical model figure, variable relationship diagram, or paper overview schematic. This skill first uses ARS to review the theory structure, research question, variables, mechanisms, hypotheses, and claim-evidence boundaries, then produces a figure brief for engineering-figure-agent to execute.
---

# Conceptual Figure Workflow

This is a front-end workflow for research conceptual figures. It does not draw
the final image directly. It prepares a defensible figure brief, then hands the
brief to `engineering-figure-agent`.

## Boundary

Use this skill when the figure depends on research logic:

- conceptual framework figures
- thesis or dissertation framework diagrams
- experiment design diagrams
- mechanism or pathway diagrams
- variable relationship or hypothesis diagrams
- paper overview schematics that must reflect theory, evidence, or study design

Do not use this skill for ordinary statistical plots. Use `nature-figure` for
publication plots and multi-panel empirical figures.

## Workflow

1. Read `../academic-research/SKILL.md` and route the research-logic review to the smallest
   relevant ARS workflow, normally `academic-paper`, `deep-research`, or
   `experiment-agent`.
2. If the figure is geography, human geography, GIScience, GeoAI, spatial
   analysis, environmental exposure, or health geography work, optionally read
   only the relevant files in `../shared/field-context/`.
3. Review the proposed figure logic before design:
   - research question and central claim
   - theoretical constructs or variables
   - mechanisms, pathways, hypotheses, or stages
   - spatial and temporal units when relevant
   - claim-evidence boundaries and likely reviewer objections
   - what must not be implied by the figure
4. Produce a figure brief with:
   - one-sentence figure purpose
   - audience and paper section
   - central claim or argument
   - node list and relationship list
   - panel or layer plan
   - visual hierarchy and reading order
   - label language, normally English unless the user asks otherwise
   - prohibited visual implications
   - caption draft or caption logic
5. Hand the brief to `engineering-figure-agent` for image, prompt, SVG, or plot
   execution. Do not ask `engineering-figure-agent` to reinterpret the theory
   from scratch.

## Output Contract

When the user asks only for planning, return the figure brief and stop.

When the user asks to create the figure, first return or save the brief, then use
`engineering-figure-agent` to execute it. Preserve the brief as the reviewable
source of truth for later iterations.

## Quality Rules

- Do not invent theory, mechanisms, variables, hypotheses, data, or citations.
- Separate confirmed evidence from design interpretation.
- Avoid causal arrows unless causality is part of the study design or theory.
- For spatial work, state the spatial unit and avoid implying scale-free effects.
- For health geography, separate exposure, vulnerability, access, outcome, and
  contextual pathways unless the user's theory combines them explicitly.
