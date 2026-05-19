---
name: docx
description: Comprehensive `.docx` document handling for Codex, including text extraction, OOXML inspection, safe revision workflows, and Word document creation. Use when Codex needs to open, analyze, rewrite, create, or carefully edit Microsoft Word `.docx` files, especially for academic, business, legal, or review-oriented document tasks.
---

# Docx

## Overview

Use this skill to work with `.docx` files in a way that is practical for Codex:

- Extract readable text from a Word document
- Inspect OOXML internals when formatting, comments, or tracked changes matter
- Generate a new `.docx` from rewritten content
- Choose a safer workflow for third-party or high-stakes documents

Prefer this skill over ad hoc zip/XML poking when the user explicitly asks to open or modify a Word document.

## Markdown-First Project Rule

If the active workspace has `.codex/project.yaml` with `paths.manuscript.source_of_truth`, treat that file as the canonical editable manuscript. In that setup:

- Use `.docx` files as originals, advisor review copies, or Pandoc exports.
- When generating Word output, prefer Pandoc with `paths.manuscript.reference_docx` and `paths.manuscript.bibliography` if those paths exist.
- If a reviewed Word file contains useful comments or edits, inspect/extract them and merge accepted changes into the Markdown source of truth.
- Do not overwrite or treat generated DOCX as the primary source unless the user explicitly asks to switch source formats.

## Workflow Decision Tree

1. If the goal is to read content from a `.docx`, run `scripts/extract_docx_text.ps1`.
2. If the goal is to inspect comments, revisions, or embedded media, read `references/ooxml-map.md` and run `scripts/inspect_docx_package.ps1`.
3. If the goal is to create a new Word file from finalized text, run `scripts/write_docx_via_word.ps1`.
4. If the goal is to revise a user-owned document, prefer creating a new output file instead of overwriting the original.
5. If the document is third-party, legal, contractual, academic review, or otherwise high-stakes, do not silently rewrite the original. Extract, revise into a new file, and preserve an audit trail.
6. If the goal is to export a Markdown-first manuscript to Word and Pandoc paths are declared in `.codex/project.yaml`, use that Pandoc build path before Word COM automation.

## Reading A DOCX

Run:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\Lingwei\.codex\skills\docx\scripts\extract_docx_text.ps1" -Path "C:\path\to\file.docx"
```

This script:

- Reads `word/document.xml` directly from the OOXML package
- Outputs paragraph text in reading order
- Counts tracked insertions and deletions
- Reports whether comments are present

Use this first for proposal abstracts, manuscripts, reports, or administrative documents where the user wants rewriting or summarization.

## Inspecting Structure And Revisions

Run:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\Lingwei\.codex\skills\docx\scripts\inspect_docx_package.ps1" -Path "C:\path\to\file.docx"
```

Use this when you need package-level visibility:

- `word/document.xml` for main body content
- `word/comments.xml` for comments
- `word/_rels/document.xml.rels` for linked assets
- `word/media/` for embedded images
- `<w:ins>` and `<w:del>` for tracked changes

Read `references/ooxml-map.md` if you need a quick map of the important OOXML parts.

## Writing A New DOCX

When the target is a new Word document from finalized text, write plain text to a temporary `.txt` file and run:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\Lingwei\.codex\skills\docx\scripts\write_docx_via_word.ps1" -InputTextPath "C:\path\to\content.txt" -OutputPath "C:\path\to\output.docx"
```

This workflow uses local Word COM automation to create a `.docx` with paragraph breaks preserved. Prefer it for:

- New abstracts
- Revised proposals
- Deliverables that must be handed back as Word files

If Word COM is unavailable, fall back to producing Markdown or plain text and clearly state that `.docx` generation could not be completed in the current environment.

## Safe Editing Rules

- Treat the original file as read-only unless the user explicitly asks to overwrite it.
- For user-owned drafts, prefer output names like `*-revised.docx` or `*-rewritten.docx`.
- For third-party or high-stakes documents, do not flatten tracked changes unless the user explicitly asks for a clean copy.
- When exact formatting is business-critical, inspect OOXML before editing assumptions into the workflow.

## Current Skill Boundaries

- This skill is optimized for reading, rewriting, and generating `.docx` files.
- It does not guarantee full fidelity for complex Word features such as section-level layout, floating objects, or native tracked-change author metadata.
- When exact redlining is required, inspect the OOXML package first and keep the original untouched.
