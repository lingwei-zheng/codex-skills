---
name: peer-review
description: Use when reviewing an academic journal manuscript, referee report, peer-review PDF, manuscript plus supplementary materials, or when the user wants a structured journal review with required/important/minor revisions. This skill orchestrates NORA and Academic Research Suite review perspectives, requires visual inspection of key figures/tables when possible, and produces bilingual working reports plus a concise journal-submission-ready review.
---

# Journal Peer Review Workflow

## Purpose

Use this skill to produce rigorous, human-like journal peer reviews from a manuscript PDF and optional supplementary materials. It is designed for tasks such as:

- "review this paper"
- "prepare a referee report"
- "generate a journal submission review"
- "combine NORA and academic-research-suite for manuscript review"
- reviewing a paper folder containing PDF, DOCX, supplementary figures/tables, or extracted text

This skill coordinates two upstream review lenses:

- **NORA** (`C:/Users/Lingwei/.codex/skills/nora/SKILL.md`) for GIScience, spatial analysis, remote sensing, GeoAI, geospatial methods, evidence logic, and venue-fit concerns.
- **Academic Research Suite** (`C:/Users/Lingwei/.codex/skills/academic-research-suite/SKILL.md`) for multi-perspective peer-review logic, methodology review, domain review, devil's-advocate stress testing, and editorial synthesis.

Read those skill files when the user explicitly requests this combined workflow or when the manuscript review needs those perspectives. Do not duplicate their full instructions here.

## Core Rule

Do not produce a final review from extracted text alone if the manuscript contains figures, maps, diagrams, tables, clustering plots, statistical charts, or supplementary visual materials. First attempt visual inspection. If visual inspection is not possible, state that limitation clearly in the report.

## Workflow

### 1. Intake And File Discovery

1. Identify the manuscript PDF and all supplementary files in the user-specified folder.
2. Read `.codex/project.yaml` if present to respect project paths.
3. Record reviewed materials explicitly:
   - main manuscript PDF
   - extracted manuscript text
   - rendered figures/pages
   - supplementary DOCX/PDF/images/tables
   - any materials that could not be inspected

### 2. Text Extraction

Use available local tools in this order:

1. For PDFs, use `pypdf` for text extraction if available.
2. If layout matters, render relevant pages with `pypdfium2`, `pdftoppm`, or another available renderer.
3. For `.docx`, use the docx skill extraction script:
   `C:/Users/Lingwei/.codex/skills/docx/scripts/extract_docx_text.ps1`
4. For supplementary DOCX media, inspect the OOXML package and extract embedded images from `word/media/`.

Do not assume supplementary material is only text. Embedded figures and tables often contain review-critical evidence.

### 3. Visual Inspection

Render and inspect at least:

- figures central to the paper's claims
- statistical plots used for inference
- maps or spatial diagrams
- clustering or typology figures
- supplementary figures supporting key claims

Internal notes should distinguish whether an issue is based on:

- manuscript text
- figure caption only
- actual visual inspection
- supplementary material
- methodological logic
- domain knowledge

The final report need not expose all source tags, but it must not imply visual inspection if only captions were read.

### 4. Review Analysis

Use NORA and Academic Research Suite perspectives to evaluate:

- research question and contribution
- field and journal fit
- data representativeness and sampling bias
- spatial/temporal unit of analysis
- method validity and reproducibility
- statistical assumptions and reporting
- figure/table evidence quality
- claim-to-evidence alignment
- overinterpretation and causal language
- limitations and ethics/data access
- planning, policy, or practical implications

Use a devil's-advocate pass to identify the strongest rejection-risk issue.

### 5. Issue Triage

Default issue hierarchy:

1. **Required revision**: exactly 1 issue. Choose the single highest-risk issue that could plausibly lead to rejection if unresolved. Do not bundle several independent issues under one heading.
2. **Important revisions**: 1-5 issues that affect the editorial decision, such as theory, logic, methods, evidence, statistical rigor, interpretation, or journal fit.
3. **Minor revisions**: 1-5 issues for language, terminology, formatting, figure captions, repetition, or presentation.

If the user gives a different issue-count template, follow the user's counts exactly.

### 6. Outputs

When creating files, place outputs in the manuscript folder unless the user specifies otherwise.

Recommended file set:

- `中文审稿报告.md`: Chinese working report.
- `English_Peer_Review_Report.md`: English working report synchronized to the Chinese report.
- `期刊提交审稿意见.md`: concise English journal-submission-ready review.

For journal-submission-ready reviews:

- Start with one paragraph summarizing what the paper studies, its strengths, its main weakness, and the decision.
- Use only three section headings:
  - `## 1. Required Revision`
  - `## 2. Important Revisions`
  - `## 3. Minor Revisions`
- Do not use subheadings for individual points.
- Each point should be a complete sentence or paragraph, not a label followed by notes.
- Write in natural referee-report style, not as a checklist.
- Keep the tone firm, specific, and constructive.

## Decision Guidance

Use **Major Revision** when the manuscript is promising and fixable, but a core method, evidence chain, interpretation, or robustness issue must be addressed before acceptance can be considered.

Use **Reject** only when the core contribution is unsupported, unfixable with available data, outside the journal scope, or methodologically invalid in a way that revision cannot reasonably solve.

Use **Minor Revision** only when methods and evidence are sound and remaining issues are mainly clarification, framing, or presentation.

## Final Check Before Delivery

Before finalizing, verify:

- Visual inspection was performed or its absence was disclosed.
- The required revision is truly one issue, not several bundled issues.
- Important and minor revisions obey the requested count limits.
- The journal-submission-ready report has no per-point subheadings.
- Any user comments in parentheses or placeholders have been resolved.
- Existing user-edited files are not overwritten unintentionally.
