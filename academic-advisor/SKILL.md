---
name: academic-advisor
description: >-
  Use when evaluating a research proposal, rough idea, paper concept,
  manuscript, pre-submission package, or journal targeting strategy through an
  advisor-style assessment. Triggers include proposal review, idea
  evaluation, research supervision, manuscript pre-submission audit, journal
  targeting, 投稿建议, 研究想法评估, 论文投稿路线, and 投稿期刊选择. Produces one
  integrated Simplified Chinese report by combining good-question,
  academic-research, Zotero evidence, and web literature checks.
---

# Academic Advisor

Provide advisor-style evaluation for proposals, rough ideas, research plans, manuscripts, and journal targeting decisions. The output is one integrated Simplified Chinese report, not separate sub-skill reports.

## Defaults

- Always perform deep evidence grounding: read `references/zotero-evidence-workflow.md`, check Zotero readiness, search Zotero first, then use web literature or journal searches when Zotero is unavailable, sparse, or insufficient for current evidence, target-journal fit, or novelty claims.
- Default report language: Simplified Chinese. English manuscripts, English journal names, and English source metadata do not change the report language. Use English only when the user explicitly asks for an English report or when a specific submission-ready English passage is requested.
- Default domain baseline: geography, human geography, GIScience, health geography, spatial analysis, and environmental or health geography when relevant.
- Journal strategy defaults to ambitious targeting: recommend a high-impact route first, then realistic and fallback options with explicit risk.
- Do not edit the proposal or manuscript by default. Produce a separate assessment report unless the user explicitly asks for rewriting.

## Routing Boundaries

- Use `academic-advisor` for author-side project diagnosis, pre-submission audit, and journal strategy.
- Use `good-question` logic for question quality, falsifiability, pilot design, and strongest reviewer rejection risk.
- Use `academic-research` logic for literature positioning, research design, manuscript structure, contribution, and ARS-style paper/reviewer workflows.
- Use `zotero:Zotero` for local-library evidence search, citation metadata, and full text only when needed. If the plugin skill is not automatically loaded, follow `references/zotero-evidence-workflow.md` to locate and run the current Zotero helper without hard-coding a cache hash.
- Use `peer-review` instead for formal referee reports, external manuscript review, or journal-style reviewer comments not tied to the user's author strategy.

## Required Workflow

1. Intake the provided proposal, idea file, manuscript, and optional journal list.
2. Classify the task as `idea-proposal`, `manuscript-pre-submission`, `journal-targeting-only`, or `revision-strategy`.
3. Build evidence before giving a mature recommendation:
   - Read `references/zotero-evidence-workflow.md`.
   - Run a Zotero readiness check and search Zotero for core theory, methods, adjacent papers, target-journal examples, and missing references.
   - Browse the web for latest papers, journal scope, author guidelines, recent special issues, and representative target-journal articles only when Zotero is unavailable, sparse, outdated, or insufficient for the decision.
   - Maintain an evidence ledger with `来源支持 Source-backed`, `推断 Inference`, and `未知/待核查 Unknown`.
   - If Zotero is unavailable, do not silently skip it; report the exact blocker in the evidence ledger.
4. Evaluate with both lenses:
   - Good-question lens: importance, tractability, falsifier, pilot, hidden assumptions, reviewer risk.
   - Academic-research lens: literature gap, design fit, methods, claim-evidence boundary, contribution, structure, and manuscript readiness.
5. If a journal list is supplied, treat it as an active constraint and ranking pool, not an appendix. Read `references/journal-fit-rubric.md`.
6. Produce one integrated report using `templates/integrated-advisor-report.md`.

## Reference Loading

- Read `references/advisor-rubric.md` for proposal, idea, manuscript, and revision evaluation.
- Read `references/evidence-triangulation.md` before making novelty, literature-gap, or target-journal claims.
- Read `references/zotero-evidence-workflow.md` whenever evidence grounding is required.
- Read `references/journal-fit-rubric.md` when the user provides a journal list or asks where to submit.

## Output Rules

- Lead with a Chinese bottom-line verdict and the recommended paper route.
- Separate source-backed claims from inferences and unknowns using the Chinese evidence ledger labels.
- Do not output the final integrated report in full English unless the user explicitly requests English.
- Do not claim "nobody has studied this" unless the evidence search supports that claim.
- For manuscripts, inspect actual text structure and, when figures or tables carry claims, use `pdf` or `docx` visual/document tools as appropriate.
- For journal ladders, include `high target`, `realistic target`, and `fallback target`, with the minimum changes required for each.
- Keep the final report directly reusable as a project document.
