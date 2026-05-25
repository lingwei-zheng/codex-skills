---
name: md-to-docx
description: Export a Markdown-first manuscript to `.docx` with Pandoc, project YAML auto-discovery, bundled default style/filter assets, preflight image normalization, bibliography support, and post-processing for thesis-style table borders. Use when Codex needs to build or rebuild a Word manuscript from Markdown without treating the `.docx` as the source of truth.
---

# Md To Docx

Use this skill when the workspace is Markdown-first and the user wants a Word export.

## Workflow

1. Treat the Markdown manuscript as the editable source of truth.
2. Read `.codex/project.yaml` when present and reuse `reference_docx`, `bibliography`, `docx_blank_line_filter`, and the current manuscript path.
3. If the project does not define `reference_docx` or `docx_blank_line_filter`, fall back to bundled assets in `assets/`.
4. Run `scripts/build_md_to_docx.ps1`.
5. Review preflight warnings (especially HTML table and missing-image warnings) and fix source Markdown when needed.
6. Keep generated `.docx` files as outputs, not as the canonical manuscript.

## Guardrails

- Do not overwrite the Markdown source with `.docx` edits.
- Prefer rebuilding from Markdown over hand-editing generated Word files.
- When formatting regressions affect tables, preserve the OOXML post-processing step instead of simplifying the Pandoc command.
- Treat the bundled reference docx as the global default style, but let explicit parameters and project YAML override it when a project needs a different house style.
- Prefer Pandoc-native Markdown images (`![](...)`) and tables over raw HTML blocks to avoid layout drift in Word exports.

For parameter details and project-path fallback rules, read [workflow.md](references/workflow.md).
