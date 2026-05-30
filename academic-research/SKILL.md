---
name: academic-research
description: >-
  Academic research, literature review, paper drafting, manuscript revision,
  peer review, research-to-paper workflow routing, and experiment planning for
  geography, human geography, GIScience, and health geography. Use when the
  user asks for literature review, systematic review, research question
  refinement, paper outlining, abstract writing, revision, citation or
  integrity checks, reviewer simulation, editorial letters, full pipeline
  support, or experiment/study planning. Supports ARS-style aliases such as
  ars-plan, ars-outline, ars-abstract, ars-lit-review, ars-revision, and
  ars-full.
---

# Academic Research

This is the Codex entry router for the vendored ARS suite under `ars/`.

## Defaults

- Domain default: geography, human geography, GIScience, and health geography.
- Chinese default: Simplified Chinese. Use Traditional Chinese only when the user explicitly asks for it.
- NORA is not an installed skill here. Use `../shared/field-context/` only as a local reference pack when domain grounding is needed.

## First rule

Do not load the whole suite by default. Start from one workflow entry file and then load only the needed agent, reference, or template files.

## Workflow router

- Deep research, literature review, systematic review, meta-analysis, research question refinement:
  `ars/deep-research/WORKFLOW.md`
- Academic paper writing, outline, abstract, revision, citation formatting, disclosure, formatting guidance:
  `ars/academic-paper/WORKFLOW.md`
- Peer review, reviewer simulation, editorial decision, re-review:
  `ars/academic-paper-reviewer/WORKFLOW.md`
- End-to-end research-to-paper pipeline:
  `ars/academic-pipeline/WORKFLOW.md`
- Experiment planning, statistical interpretation, reproducibility, human study protocol:
  `ars/experiment-agent/WORKFLOW.md`

## Alias routing

Treat these as mode shortcuts inside this skill:

- `ars-plan`
- `ars-outline`
- `ars-abstract`
- `ars-lit-review`
- `ars-citation-check`
- `ars-disclosure`
- `ars-format-convert`
- `ars-revision-coach`
- `ars-revision`
- `ars-full`

If the user only has a broad topic or tentative title but no clear research question, route to `ars/deep-research/WORKFLOW.md` in Socratic narrowing mode before outlining or drafting.

## Codex mapping

- Treat upstream Claude/agent dispatch wording as phase prompts to execute inline.
- Do not install or run Claude hooks.
- Treat `WORKFLOW.md` files as the actual internal entrypoints.
- Use `../shared/field-context/academic-writing.md`, `spatial-methods.md`, `geoai-domain.md`, `environmental-health.md`, and `journal-templates/` only when relevant.