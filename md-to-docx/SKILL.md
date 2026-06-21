---
name: md-to-docx
description: Use when exporting or rebuilding a Markdown-first manuscript as Word, especially when Pandoc formatting, citations, images, tables, or TeX equations must remain stable.
---

# Md To Docx

Use this skill when the workspace is Markdown-first and the user wants a Word export.

## Workflow

1. Treat the Markdown manuscript as the editable source of truth.
2. Read `.codex/project.yaml` when present and reuse `reference_docx`, `bibliography`, `docx_blank_line_filter`, and the current manuscript path.
3. If the project does not define `reference_docx` or `docx_blank_line_filter`, fall back to bundled assets in `assets/`.
   - The bundled `assets/default_reference.docx` is the standard minimal academic-paper template.
   - The older thesis-style template is retained as `assets/legacy_thesis_reference.docx` for explicit opt-in use only.
4. Run `scripts/build_md_to_docx.ps1`.
5. Review preflight fixes and warnings, especially malformed math, HTML tables, and missing images.
6. For the minimal academic-paper template, verify that Word headings were converted to Normal/body paragraphs with direct bold/italic formatting.
7. Verify the exported `.docx` is saved in modern Word compatibility mode (`compatibilityMode=15`) when OMML equations are present.
8. Review hyphen/en dash usage before submission: use hyphens for compound adjectives and reserve en dashes for value, date, page, or similar ranges.
9. Keep generated `.docx` files as outputs, not as the canonical manuscript.

## Guardrails

- Do not overwrite the Markdown source with `.docx` edits.
- Prefer rebuilding from Markdown over hand-editing generated Word files.
- When formatting regressions affect tables, preserve the OOXML post-processing step instead of simplifying the Pandoc command.
- Treat the bundled minimal academic-paper reference docx as the global default style, but let explicit parameters and project YAML override it when a project needs a different house style.
- Minimal academic exports should not rely on Word Heading styles: title and first-level headings use Normal/body paragraphs with bold; second-level headings use bold italic; third-level and lower headings use italic. Main-text section numbers are inserted as plain text prefixes, such as `1.`, `2.1.`, and `2.1.1.`.
- Figure and table captions remain body paragraphs with default paragraph alignment; do not force them to be centered.
- Reference-list paragraphs use the legacy thesis-style hanging indent and double line spacing for readability.
- Prefer Pandoc-native Markdown images (`![](...)`) and tables over raw HTML blocks to avoid layout drift in Word exports.
- Use `$...$` for inline equations and `$$...$$` for display equations. Do not use ````math` fences or place code backticks inside `$...$`.
- Verify important equations are Word OMML objects when Pandoc reports a TeX conversion warning.
- If Word shows the Compatibility Checker warning that equations may be converted to images, inspect `word/settings.xml`; `compatibilityMode=11` is the usual cause and should be upgraded to `15` for modern `.docx` exports.
- Treat `letter–letter` en dash patterns as review warnings, not automatic replacements. Likely compound adjectives should use hyphens, valid ranges should keep en dashes, and reference titles or fixed terms should be inspected manually.

For parameter details and project-path fallback rules, read [workflow.md](references/workflow.md).
