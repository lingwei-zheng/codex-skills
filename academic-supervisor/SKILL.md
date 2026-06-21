---
name: academic-supervisor
description: >-
  Use when evaluating a research proposal, rough idea, paper concept,
  manuscript, pre-submission package, or journal targeting strategy through a
  supervisor-style assessment. Triggers include proposal review, idea
  evaluation, research supervision, manuscript pre-submission audit, journal
  targeting, 投稿建议, 研究想法评估, 论文投稿路线, and 投稿期刊选择. Combines
  good-question, academic-research, Zotero evidence, and web literature checks
  into one integrated report.
---

# Academic Supervisor

Provide supervisor-style evaluation for proposals, rough ideas, research plans, manuscripts, and journal targeting decisions. The output is one integrated report, not separate sub-skill reports.

## Defaults

- Always perform deep evidence grounding: search Zotero first, then use web literature or journal searches when current evidence, target-journal fit, or novelty claims matter.
- Default language: Chinese, with English academic terms preserved when useful.
- Default domain baseline: geography, human geography, GIScience, health geography, spatial analysis, and environmental or health geography when relevant.
- Journal strategy defaults to ambitious targeting: recommend a high-impact route first, then realistic and fallback options with explicit risk.
- Do not edit the proposal or manuscript by default. Produce a separate assessment report unless the user explicitly asks for rewriting.

## Routing Boundaries

- Use `academic-supervisor` for author-side project diagnosis, pre-submission audit, and journal strategy.
- Use `good-question` logic for question quality, falsifiability, pilot design, and strongest reviewer rejection risk.
- Use `academic-research` logic for literature positioning, research design, manuscript structure, contribution, and ARS-style paper/reviewer workflows.
- Use `zotero:Zotero` for local-library evidence search, citation metadata, and full text only when needed.
- Use `peer-review` instead for formal referee reports, external manuscript review, or journal-style reviewer comments not tied to the user's author strategy.

## Required Workflow

1. Intake the provided proposal, idea file, manuscript, and optional journal list.
2. Classify the task as `idea-proposal`, `manuscript-pre-submission`, `journal-targeting-only`, or `revision-strategy`.
3. Build evidence before giving a mature recommendation:
   - Search Zotero for core theory, methods, adjacent papers, target-journal examples, and missing references.
   - Browse the web for latest papers, journal scope, author guidelines, recent special issues, and representative target-journal articles when needed.
   - Maintain an evidence ledger with `Source-backed`, `Inference`, and `Unknown`.
4. Evaluate with both lenses:
   - Good-question lens: importance, tractability, falsifier, pilot, hidden assumptions, reviewer risk.
   - Academic-research lens: literature gap, design fit, methods, claim-evidence boundary, contribution, structure, and manuscript readiness.
5. If a journal list is supplied, treat it as an active constraint and ranking pool, not an appendix. Read `references/journal-fit-rubric.md`.
6. Produce one integrated report using `templates/integrated-supervisor-report.md`.

## Reference Loading

- Read `references/supervisor-rubric.md` for proposal, idea, manuscript, and revision evaluation.
- Read `references/evidence-triangulation.md` before making novelty, literature-gap, or target-journal claims.
- Read `references/journal-fit-rubric.md` when the user provides a journal list or asks where to submit.

## Output Rules

- Lead with a bottom-line verdict and the recommended paper route.
- Separate source-backed claims from inferences and unknowns.
- Do not claim "nobody has studied this" unless the evidence search supports that claim.
- For manuscripts, inspect actual text structure and, when figures or tables carry claims, use `pdf` or `docx` visual/document tools as appropriate.
- For journal ladders, include `high target`, `realistic target`, and `fallback target`, with the minimum changes required for each.
- Keep the final report directly reusable as a project document.
