---
name: academic-research
description: Route literature reviews, research design, statistical simulation, method validation, experiment planning, paper drafting and revision, or a full research-to-paper workflow. Supports geography, GIScience and health geography when relevant.
---

# Academic Research

Codex router for the research suite in `ars/`. Select one entry and load only
the references needed for the current decision; do not traverse the whole suite.

## Select the Task

| Main task | Entry |
|---|---|
| Choose or assess a research question | `../good-question/SKILL.md` |
| Organize existing evidence into a paper story | `../good-story/SKILL.md` |
| Author-side assessment or journal strategy | `../academic-advisor/SKILL.md` |
| Formal referee report | `../peer-review/SKILL.md` |
| Polish or translate supplied prose | `../nature-polishing/SKILL.md` |
| Literature review, systematic review, meta-analysis | `ars/deep-research/WORKFLOW.md` |
| Outline, abstract, drafting, revision, citations, disclosure, format conversion | `ars/academic-paper/WORKFLOW.md` |
| Experiment/study planning, simulation, method validation, statistical interpretation, reproducibility | `ars/experiment-agent/WORKFLOW.md` |
| End-to-end research-to-paper task | `ars/academic-pipeline/WORKFLOW.md` |

Keep `ars/academic-paper-reviewer/WORKFLOW.md` and internal question refinement
available for explicit academic-research requests and full pipelines. Do not
route an established, narrowly scoped task through question development again.

For a bounded judgment from supplied evidence, such as whether a reliable
result supports writing, use the project's exploration protocol. Enter execution
workflows for design, running or verification work; a judgment alone need not
start one. This does not waive any applicable approval or verification gate.

## Project Methodology

Read the project-root `SCIENTIFIC_EXPLORATION_PROTOCOL.md` under the project's
`AGENTS.md` for scientific decisions. There is no bundled methodology fallback.
If unavailable, identify the missing path and defer only decisions needing it;
continue independent authorized work. Do not create a replacement protocol.
Routine wording or formatting does not reopen scientific exploration.

## Execution and Loading

Before using an internal workflow, read
[execution and approval scope](references/execution-and-approval.md).
Select its matching mode; do not expand a narrow request to the full pipeline.
Phase completion returns control to the main agent, who continues the authorized
task while preserving explicit approval and validation gates.

| Read when | Source of truth |
|---|---|
| Developing a question, experiment argument, paper architecture or central claim | `../shared/advantage-led-research-narrative.md` |
| Reading, outlining, drafting or revising research content | `references/selective-quality-control.md` |
| Simulation or estimator work in plan, run or validate mode | [Simulation guide](ars/experiment-agent/references/simulation-method-validation.md) |

Reuse existing decisions, claim/evidence records and verified sources; update
only affected parts. A wording-only edit does not require a new research ledger.

## Local Adaptation

- Default Chinese output to Simplified Chinese.
- Apply `../shared/field-context/` only to relevant geography, GIScience, GeoAI,
  remote-sensing or environmental/health-geography tasks. NORA is not installed.
  Use `geography-publication-readiness.md` for readiness and the relevant
  `academic-writing.md`, `spatial-methods.md`, `geoai-domain.md`,
  `environmental-health.md` or `journal-templates/` for domain decisions.
- For dynamic greenspace exposure and Space-Time Constraints projects, use
  `references/space-time-greenspace-terminology.md` only for that terminology.
- Treat upstream Claude dispatch as inline phase prompts; do not install or run
  Claude hooks. `WORKFLOW.md` files are the internal entrypoints.
- Accept natural language or `/academic-research mode=<mode>`: `plan`, `outline`,
  `abstract`, `lit-review`, `citation-check`, `disclosure`, `format-convert`,
  `revision-coach`, `revision`, `full`. Legacy `ars-*` tokens are internal
  modes, not separate slash-callable skills.
