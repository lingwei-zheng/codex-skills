---
name: academic-research
description: >-
  Academic research, literature review, research design, paper drafting,
  manuscript revision, research-to-paper workflow routing, and experiment
  planning for geography, human geography, GIScience, and health geography.
  Use when the user asks for literature review, systematic review, paper
  outlining, geography-specific title design, abstract writing, revision,
  citation or integrity checks, full pipeline support, or experiment/study
  planning. Use good-question when research-question quality is the primary
  task, peer-review for a formal referee report, good-story for an evidence-led
  manuscript story, and academic-advisor for submission strategy.
---

# Academic Research

This is the Codex entry router for the vendored research suite under `ars/`.

## Defaults

- Domain default: geography, human geography, GIScience, and health geography.
- Chinese default: Simplified Chinese. Use Traditional Chinese only when the user explicitly asks for it.
- NORA is not an installed skill here. Use `../shared/field-context/` only as a local reference pack when domain grounding is needed.
- Read `../shared/research-calibration.md` for analysis planning, experiment
  execution, question evaluation, or manuscript-readiness decisions. When the
  user is developing an analysis or manuscript and gives no stage, default to
  `first-draft + proportionate rigor + incremental-allowed contribution +
  balanced compute`.
- Do not import submission, formal peer-review, systematic-review, or
  reviewer-response standards into first-draft analysis unless a named validity
  risk makes them immediately necessary.
- For reading, outlining, drafting, or revision, read
  `references/selective-quality-control.md`. Check load-bearing claims first,
  accept bounded PDF/manuscript reading scopes, use claim skeletons before
  uncertain prose, and prefer local patches over whole-section rewrites.

## First rule

Do not load the whole suite by default. Start from one workflow entry file and then load only the needed agent, reference, or template files.

## Routing boundaries

- Use `good-question` when the main decision is whether a question is important,
  tractable, falsifiable, or worth pursuing.
- Use `good-story` when results or manuscript materials already exist and the
  main task is to organize them into an evidence-supported narrative.
- Use `academic-advisor` for proposal diagnosis, pre-submission assessment, and
  journal targeting.
- Use `peer-review` for a formal external-reviewer report.
- Keep the internal question-refinement and reviewer workflows available only
  when the user explicitly invokes this skill or needs an end-to-end pipeline.

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

## Mode routing

Prefer `/academic-research mode=<mode>` or the equivalent natural-language
request. Supported modes include:

- `plan`
- `outline`
- `abstract`
- `lit-review`
- `citation-check`
- `disclosure`
- `format-convert`
- `revision-coach`
- `revision`
- `full`

Legacy `ars-*` tokens may be interpreted as these internal modes when supplied
after `/academic-research`; they are not separate slash-callable skills.

If the user only has a broad topic or tentative title but no clear research
question, use `good-question` first unless the user explicitly requests the
end-to-end academic-research pipeline.

## Codex mapping

- Treat upstream Claude/agent dispatch wording as phase prompts to execute inline.
- Do not install or run Claude hooks.
- Treat `WORKFLOW.md` files as the actual internal entrypoints.
- Use `../shared/field-context/geography-publication-readiness.md` for geography-specific contribution, method-fit, theory, argument, and title checks.
- Apply `../shared/research-calibration.md` before interpreting contribution
  magnitude, deciding robustness scope, or scheduling expensive analysis.
- Use `references/selective-quality-control.md` for impact-first review,
  bounded novelty language, evidence-led Introduction recalibration, and
  advisory claim-drift checks.
- Use `../shared/field-context/academic-writing.md`, `spatial-methods.md`, `geoai-domain.md`, `environmental-health.md`, and `journal-templates/` only when relevant.
- For projects that use dynamic greenspace exposure and Space-Time Constraints,
  read `references/space-time-greenspace-terminology.md` before drafting,
  revising, or auditing terminology. Treat it as a project/domain calibration
  reference, not a universal replacement for field-standard wording.
