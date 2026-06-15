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
4. Run `scripts/build_md_to_docx.ps1`.
5. Review preflight fixes and warnings, especially malformed math, HTML tables, and missing images.
6. Keep generated `.docx` files as outputs, not as the canonical manuscript.

## Guardrails

- Do not overwrite the Markdown source with `.docx` edits.
- Prefer rebuilding from Markdown over hand-editing generated Word files.
- When formatting regressions affect tables, preserve the OOXML post-processing step instead of simplifying the Pandoc command.
- Treat the bundled reference docx as the global default style, but let explicit parameters and project YAML override it when a project needs a different house style.
- Prefer Pandoc-native Markdown images (`![](...)`) and tables over raw HTML blocks to avoid layout drift in Word exports.
- Use `$...$` for inline equations and `$$...$$` for display equations. Do not use ````math` fences or place code backticks inside `$...$`.
- Verify important equations are Word OMML objects when Pandoc reports a TeX conversion warning.

For parameter details and project-path fallback rules, read [workflow.md](references/workflow.md).
