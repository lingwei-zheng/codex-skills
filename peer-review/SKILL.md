---
name: peer-review
description: Use when reviewing an academic journal manuscript, referee report, peer-review PDF, manuscript plus supplementary materials, or when the user wants a structured journal review with critical, important, and minor revisions. This skill uses ARS as the main reviewer framework, local geography/GIScience/health geography field context when relevant, and pdf/docx tools for manuscript and visual-material inspection. Chinese outputs default to Simplified Chinese.
---

# Journal Peer Review Workflow

Use this skill to produce rigorous journal peer reviews from a manuscript PDF,
DOCX, Markdown draft, extracted text, and optional supplementary materials.

## Review Lenses

Use `../academic-research/SKILL.md` as the main review framework. Route to ARS
`academic-paper-reviewer` for reviewer calibration, methodology review, domain
review, devil's-advocate stress testing, and editorial synthesis.

Use `../shared/field-context/` only when the manuscript falls within geography,
human geography, GIScience, GeoAI, spatial analysis, remote sensing,
environmental exposure, or health geography. Do not call or assume a NORA skill
is installed.

Use the existing `pdf` and `docx` skills for file inspection, extraction, and
rendered visual checks when the input format requires them.

## Core Rule

Do not produce a final review from extracted text alone if the manuscript
contains figures, maps, diagrams, tables, clustering plots, statistical charts,
or supplementary visual materials. First attempt visual inspection. If visual
inspection is not possible, state that limitation clearly in the report.

Chinese working outputs default to Simplified Chinese. Use Traditional Chinese
only when the user explicitly requests it.

## Workflow

### 1. Intake And File Discovery

1. Identify the main manuscript and all supplementary files in the user-specified
   folder or attachment set.
2. Read `.codex/project.yaml` if present to respect project paths.
3. Record reviewed materials explicitly:
   - main manuscript PDF, DOCX, Markdown, or extracted text
   - rendered pages or figures
   - supplementary DOCX/PDF/images/tables
   - any materials that could not be inspected

### 2. Text And Visual Inspection

Use available local tools in this order:

1. For PDFs, use text extraction plus rendered-page inspection when layout,
   tables, figures, maps, or equations matter.
2. For DOCX, use the `docx` skill for extraction and OOXML/media inspection.
3. For supplementary DOCX media, inspect embedded images under `word/media/`.
4. Render and inspect central figures, maps, statistical plots, diagrams, and
   supplementary figures supporting key claims.

Internal notes should distinguish whether each issue is based on manuscript
text, figure captions, actual visual inspection, supplementary material,
methodological logic, or domain context.

### 3. ARS Review Pass

Read `../academic-research/SKILL.md`, then route to ARS `academic-paper-reviewer`.
Preserve independent reviewer perspectives before synthesis:

- field and journal fit
- research question and contribution
- method validity and reproducibility
- data representativeness and sampling bias
- statistical assumptions and reporting
- figure/table evidence quality
- claim-to-evidence alignment
- overinterpretation and causal language
- limitations, ethics, and data access

For geography/GIScience/health geography manuscripts, consult the minimum
needed field-context files:

- `spatial-methods.md` for spatial unit, scale, MAUP, autocorrelation, and
  spatial validity.
- `environmental-health.md` for exposure, vulnerability, access, and outcome
  pathways.
- `geoai-domain.md` for GeoAI and geospatial ML review.
- `journal-templates/` for venue fit.

Use a devil's-advocate pass to identify the strongest rejection-risk issue.

### 4. Issue Triage

Default issue hierarchy:

1. **Critical revision**: exactly one issue. Choose the single highest-risk issue
   that could plausibly lead to rejection if unresolved. Do not bundle unrelated
   issues under one heading.
2. **Important revisions**: one to five issues that affect editorial decision,
   including theory, logic, methods, evidence, statistical rigor, interpretation,
   or journal fit.
3. **Minor revisions**: one to five issues for language, terminology,
   formatting, figure captions, repetition, or presentation.

If the user gives a different issue-count template, follow the user's counts.

### 5. Outputs

When creating files, place outputs in the manuscript folder unless the user
specifies otherwise.

Recommended file set:

- `涓枃瀹＄鎶ュ憡.md`: Simplified Chinese working report.
- `English_Peer_Review_Report.md`: English working report synchronized to the
  Chinese report.
- `鏈熷垔鎻愪氦瀹＄鎰忚.md`: concise English journal-submission-ready review.

For journal-submission-ready reviews:

- Start with one paragraph summarizing what the paper studies, its strengths,
  its main weakness, and the decision.
- Use only three section headings:
  - `## 1. Critical Revision`
  - `## 2. Important Revisions`
  - `## 3. Minor Revisions`
- Do not use subheadings for individual points.
- Write in natural referee-report style, not as a checklist.
- Keep the tone firm, specific, and constructive.

## Decision Guidance

Use **Major Revision** when the manuscript is promising and fixable, but a core
method, evidence chain, interpretation, or robustness issue must be addressed.

Use **Reject** only when the core contribution is unsupported, unfixable with
available data, outside the journal scope, or methodologically invalid in a way
that revision cannot reasonably solve.

Use **Minor Revision** only when methods and evidence are sound and remaining
issues are mainly clarification, framing, or presentation.

## Final Check Before Delivery

Before finalizing, verify:

- Visual inspection was performed or its absence was disclosed.
- The critical revision is truly one issue.
- Important and minor revisions obey the requested count limits.
- The journal-submission-ready report has no per-point subheadings.
- Existing user-edited files are not overwritten unintentionally.

