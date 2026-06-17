# Md To Docx Workflow

## What the script does

`scripts/build_md_to_docx.ps1`:

- auto-discovers the workspace root from the current directory;
- reads `.codex/project.yaml` if present;
- resolves the source Markdown, reference docx, bibliography, and Lua filter from project paths unless explicit parameters override them;
- performs markdown preflight cleanup:
  - converts HTML `<img ...>` tags to Pandoc image syntax;
  - normalizes image paths to `/`;
  - attempts `.emf/.wmf -> .png` conversion for Word compatibility;
  - converts fenced ````math` blocks to Pandoc `$$...$$` display math;
  - removes code backticks incorrectly nested inside `$...$`;
  - removes empty `^{}` and `_{}` scripts from normalized equations;
  - warns when HTML tables or `rowspan/colspan` are detected;
- builds a temporary `.docx` with Pandoc and `--citeproc`;
- post-processes `word/document.xml` so tables keep thesis-style top and bottom borders.

## Hyphen and en dash QA

Before or after DOCX export, scan the Markdown source and, when available, the exported DOCX text for suspicious `letter–letter` en dash patterns.

- Use a hyphen to connect words that form a compound adjective, such as `mobility-based`, `trajectory-based`, or `view-based`.
- Use an en dash only for ranges of values, dates, pages, or similar intervals, such as `2021–2023`, `10–20 m`, or `pp. 45–52`.
- Treat `letter–letter` en dash matches as warnings, not automatic replacements. Some may appear in reference titles, quoted text, or fixed terms.
- Review matches in three categories: likely compound adjectives to convert to hyphens, valid ranges to keep as en dashes, and reference titles or fixed terms to inspect manually.
- A future report mode may list counts and surrounding snippets without editing the source or bibliography automatically.

## Default path rules

When `.codex/project.yaml` exists, the script prefers these keys:

- `paths.manuscript.current_pandoc_manuscript`
- `paths.manuscript.source_of_truth`
- `paths.manuscript.reference_docx`
- `paths.manuscript.bibliography`
- `paths.manuscript.docx_blank_line_filter`

If `reference_docx` is missing, the script falls back to:

- `assets/default_reference.docx` inside the skill folder

If `docx_blank_line_filter` is missing, the script falls back to:

- `assets/docx_blank_lines.lua` inside the skill folder

If `OutputPath` is omitted, the script writes:

- `output/submission/docx/<source-basename>.docx`

## Typical use

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\Lingwei\.codex\skills\md-to-docx\scripts\build_md_to_docx.ps1"
```

Or with explicit overrides:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\Lingwei\.codex\skills\md-to-docx\scripts\build_md_to_docx.ps1" `
  -WorkspaceRoot "D:\path\to\project" `
  -SourcePath "output\manuscript\manuscript_v4.md" `
  -OutputPath "output\submission\docx\manuscript_v4.docx"
```

## Resolution priority

For style-related paths, the priority order is:

1. explicit script parameter
2. project YAML path
3. bundled skill asset

## Failure modes

- If the target `.docx` is open in Word, the script should fail rather than silently corrupting the file.
- If project YAML is missing, the script falls back to explicit parameters.
- If the project has no `reference_docx`, the bundled default template is used automatically.
- If the project has no `docx_blank_line_filter`, the bundled default filter is used automatically.
- If the bibliography path is missing, Pandoc still runs without it.
- If Pandoc reports `Could not convert TeX math`, inspect the Markdown for
  ````math` fences, `$`code``$`, unmatched delimiters, or invalid TeX. The
  preflight fixes the first two forms without modifying the source file.
