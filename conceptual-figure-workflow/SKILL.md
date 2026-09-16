---
name: conceptual-figure-workflow
description: Use when the user wants a conceptual framework figure, experiment design diagram, thesis framework, research mechanism diagram, theoretical model figure, variable relationship diagram, or paper overview schematic. This skill first uses academic-research to review the theory structure, research question, variables, mechanisms, hypotheses, and claim-evidence boundaries, then produces a figure brief for engineering-figure-agent to execute.
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
   relevant internal workflow, normally `academic-paper`, `deep-research`, or
   `experiment-agent`.
2. If the figure is geography, human geography, GIScience, GeoAI, spatial
   analysis, environmental exposure, or health geography work, optionally read
   only the relevant files in `../shared/field-context/`. Read
   `../shared/field-context/geography-conceptual-figure-patterns.md` when
   selecting the figure structure.
3. Review the proposed figure logic before design:
   - research question, central claim ID, leading advantage and evidence state
   - theoretical constructs or variables
   - mechanisms, pathways, hypotheses, or stages
   - spatial and temporal units when relevant
   - claim-evidence boundaries; check reviewer objections internally and surface
     only material scientific or delivery issues
   - what must not be implied by the figure
4. Build a semantic contract before choosing layout:
   - approved nodes with construct type and evidence status
   - approved directed or undirected relationships
   - relation type, certainty, and causal status for every edge
   - spatial and temporal scale attached to the relevant nodes or edges
   - competing explanations and unresolved decisions in an issue ledger
5. Produce a figure brief using
   `../engineering-figure-agent/references/figure-brief-spec.md`, including:
   - one-sentence figure purpose and the supported advantage readers should notice
   - audience and paper section
   - central claim or argument
   - semantic graph and render graph
   - panel, region, container, or layer plan
   - visual hierarchy, reading order, and edge ports
   - exact visible-text allowlist
   - label language, normally English unless the user asks otherwise
   - negative constraints and prohibited visual implications
   - `candidate_mode: single` or, only when structure is genuinely ambiguous,
     `candidate_mode: explore`
   - caption draft or caption logic, with evidence/derivation pointers for each
     assertion and the manuscript claim it supports
6. Hand the brief to `engineering-figure-agent`. Use its OpenAI image route for
   illustrative synthesis and its `drawio` route for exact, editable,
   label-heavy frameworks. Use `nature-figure` separately for quantitative or
   statistical panels. Do not ask an execution skill to reinterpret the theory
   from scratch.

For the meaning of approved nodes and edges, read [semantic approval scope](../engineering-figure-agent/references/figure-brief-spec.md#meaning-of-approved-semantics). Directly supported semantics do not require an extra approval round; new or conflicting scientific assertions still require a user decision.

## Output Contract

When the user asks only for planning, return the figure brief and stop.

When the user asks to create the figure, first return or save the brief, then use
`engineering-figure-agent` to execute it. Preserve the brief as the reviewable
source of truth for later iterations.

For `candidate_mode: explore`, keep the semantic graph fixed while comparing
2-4 structural candidates. Refine only 1-2 selected directions. Use one issue
ledger across candidates so rejected problems do not silently return.

## Quality Rules

- Do not invent theory, mechanisms, variables, hypotheses, data, or citations.
- Separate confirmed evidence from design interpretation.
- Treat every arrow as a claim and record its relation type, direction,
  certainty, and causal status before rendering.
- Do not merge constructs merely to simplify layout. Simplify the render graph,
  not the semantic graph.
- Avoid causal arrows unless causality is part of the study design or theory.
- For spatial work, state the spatial unit and avoid implying scale-free effects.
- For health geography, separate exposure, vulnerability, access, outcome, and
  contextual pathways unless the user's theory combines them explicitly.
