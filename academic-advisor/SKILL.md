---
name: academic-advisor
description: >-
  Use when evaluating a research proposal, rough idea, paper concept,
  manuscript, pre-submission package, or journal targeting strategy through an
  advisor-style assessment. Triggers include proposal review, idea
  evaluation, research supervision, manuscript pre-submission audit, journal
  targeting, 投稿建议, 研究想法评估, 论文投稿路线, and 投稿期刊选择. Produces one
  integrated Simplified Chinese report by combining good-question,
  good-story, academic-research, Zotero evidence, and web literature checks as
  appropriate to the task.
---

# Academic Advisor

Provide advisor-style evaluation for proposals, rough ideas, research plans, manuscripts, and journal targeting decisions. The output is one integrated Simplified Chinese report, not separate sub-skill reports.

## Defaults

- Read `../shared/research-calibration.md` and infer the research stage,
  contribution level, rigor profile, and compute profile before judging the
  project. If the user does not specify them, use the shared defaults.
- Ground decisive recommendations in evidence: read
  `references/zotero-evidence-workflow.md`, check Zotero readiness, and search
  Zotero first. For rough ideas and first drafts, use a targeted search around
  the decision-critical claims; reserve comprehensive novelty and journal
  benchmarking for submission or explicit deep-evaluation requests.
- Default report language: Simplified Chinese. English manuscripts, English journal names, and English source metadata do not change the report language. Use English only when the user explicitly asks for an English report or when a specific submission-ready English passage is requested.
- Default domain baseline: geography, human geography, GIScience, health geography, spatial analysis, and environmental or health geography when relevant.
- Match journal ambition to the contribution and evidence already present.
  Include a stretch route only when its minimum upgrade is plausible; do not
  treat specialist, regional, replication, or incremental venues as inferior
  when they are the best scholarly fit.
- Before naming or ranking journals, read
  `references/local-journal-reference.md` and attempt to load the user's local
  `journal_ai_reference.md`. Use it as the default candidate pool and preference
  ledger, then verify current scope, guidelines, and unstable metrics from
  primary journal or publisher sources.
- Do not edit the proposal or manuscript by default. Produce a separate assessment report unless the user explicitly asks for rewriting.

## Routing Boundaries

- Use `academic-advisor` for author-side project diagnosis, pre-submission audit, and journal strategy.
- Use `good-question` logic for question quality, falsifiability, pilot design, and strongest reviewer rejection risk.
- Use `good-story` logic for completed manuscripts whose evidence, figure order,
  central claim, or narrative spine needs diagnosis.
- Use `academic-research` logic for literature positioning, research design,
  manuscript structure, contribution, and its internal paper or reviewer
  workflows.
- Use `zotero:Zotero` for local-library evidence search, citation metadata, and full text only when needed. If the plugin skill is not automatically loaded, follow `references/zotero-evidence-workflow.md` to locate and run the current Zotero helper without hard-coding a cache hash.
- Use `peer-review` instead for formal referee reports, external manuscript review, or journal-style reviewer comments not tied to the user's author strategy.

## Required Workflow

1. Intake the provided proposal, idea file, manuscript, and optional journal list.
2. Classify the task as `idea-proposal`, `manuscript-pre-submission`, `journal-targeting-only`, or `revision-strategy`.
3. Apply the shared calibration profile:
   - Name the research stage and contribution level.
   - Separate checks needed now from checks that can be deferred.
   - Do not penalize a first draft for omitting submission-stage robustness
     unless the omission makes the current result invalid or misleading.
4. Build evidence before giving a mature recommendation:
   - Read `references/zotero-evidence-workflow.md`.
   - Run a Zotero readiness check and search Zotero for core theory, methods, adjacent papers, target-journal examples, and missing references.
   - Scale search depth to the decision: targeted evidence is enough for an
     early-stage diagnosis; journal scope, current guidelines, recent special
     issues, and representative articles require current web verification when
     recommending a submission route.
   - Maintain an evidence ledger with `来源支持 Source-backed`, `推断 Inference`, and `未知/待核查 Unknown`.
   - If Zotero is unavailable, do not silently skip it; report the exact blocker in the evidence ledger.
5. Select only the lenses needed for the classified task:
   - `idea-proposal`: good-question for importance, tractability, falsifier,
     pilot, hidden assumptions, and reviewer risk; academic-research for
     literature positioning, design, methods, and contribution.
   - `manuscript-pre-submission`: good-story for the central claim, evidence
     ladder, figure order, and narrative risks; academic-research for structure,
     methods, claim-evidence boundaries, and readiness.
   - `journal-targeting-only`: journal-fit and evidence-triangulation rubrics;
     add good-story only when manuscript materials are available and story
     shape affects fit.
   - `revision-strategy`: load only the question, story, research, or journal
     lens implicated by the requested revision.
6. For every journal-targeting task:
   - Read `references/local-journal-reference.md` and run its path-resolution
     sequence before recommending journals. Prefer
     `python scripts/resolve_journal_reference.py --project-root <project>`;
     pass `.codex/project.yaml`'s `paths.journal_reference` value through
     `--configured` when present.
   - Record whether the local reference was loaded, its visible update date,
     and which resolver found it. Do not silently skip an unreadable file.
   - If the user supplies another journal list, treat that list as the active
     constraint; use the local reference to enrich it, not replace it.
   - Read `references/journal-fit-rubric.md` and verify current external facts
     that could change the recommendation.
7. Produce one integrated report using `templates/integrated-advisor-report.md`.

## Reference Loading

- Read `references/advisor-rubric.md` for proposal, idea, manuscript, and revision evaluation.
- Read `references/evidence-triangulation.md` before making novelty, literature-gap, or target-journal claims.
- Read `references/zotero-evidence-workflow.md` whenever evidence grounding is required.
- Read `references/journal-fit-rubric.md` when the user provides a journal list or asks where to submit.
- Read `references/local-journal-reference.md` before every concrete journal
  recommendation or ranking.
- Read `../shared/research-calibration.md` for stage, rigor, contribution, and
  compute defaults.
- For a completed manuscript whose story affects submission readiness, read
  `../good-story/SKILL.md` and preserve its stable story handoff.
- For geography-related proposals or manuscripts, read `../shared/field-context/geography-publication-readiness.md` and include its five-gate diagnosis.

## Output Rules

- Lead with a Chinese bottom-line verdict and the recommended paper route.
- Separate source-backed claims from inferences and unknowns using the Chinese evidence ledger labels.
- Do not output the final integrated report in full English unless the user explicitly requests English.
- Do not claim "nobody has studied this" unless the evidence search supports that claim.
- State the contribution level without demanding category uniqueness.
  Replication, regional extension, measurement improvement, and modest method
  gains are viable when their value and venue fit are explicit.
- For manuscripts, inspect actual text structure and, when figures or tables carry claims, use `pdf` or `docx` visual/document tools as appropriate.
- For journal ladders, lead with the strongest credible route. Include
  `stretch target`, `realistic target`, and `fallback target` when all three
  are useful; omit a performative stretch route when no plausible upgrade path
  exists.
- Keep the final report directly reusable as a project document.
