---
name: ppt-master
description: Build native editable PowerPoint decks from papers, Markdown, PDFs, DOCX, web pages, spreadsheets, or approved slide plans using the hugohe3/ppt-master SVG-to-PPTX workflow. Use when the user wants a real .pptx with editable slide elements, PPTX conversion, PPTX live preview, SVG-authored slides, animations, speaker audio, or a PowerPoint version of an academic talk. Prefer paper-talk-prep for paper-to-slide planning before using this renderer; prefer beautiful-html-slides for browser HTML decks; prefer Presentations for artifact-tool editorial/business decks.
---

# PPT Master

Codex adapter for `hugohe3/ppt-master` at upstream commit `668131f`.

Use this skill as the native editable `.pptx` renderer. It is not the default paper-analysis, HTML-deck, or artifact-tool deck skill.

## Routing

- Paper-to-talk structure, slide text, and speaker notes: use `paper-talk-prep` first, then hand the approved slide plan to `ppt-master`.
- Browser-openable HTML slides: use `beautiful-html-slides`, not this skill.
- High-polish business, analytics, investor, board, Google Slides, or artifact-tool decks: use the `Presentations` plugin unless the user specifically wants this SVG-to-PPTX pipeline.
- Academic paper understanding, literature logic, methods/results synthesis: use `academic-research-suite` or `nora` upstream, then pass the distilled plan here.
- Figure assets and conceptual diagrams: generate or refine with `paper-framework-figure`, `research-framework-figure-workflow`, `nature-figure`, or `engineering-figure-agent`; then embed the final assets in the deck here.
- DOCX/PDF reading or review only: use `docx` or `pdf`. Use this skill's source importers only when entering the PPT generation pipeline.

If multiple slide skills could apply, ask or infer the final artifact:

- `.html` deck -> `beautiful-html-slides`
- `.pptx` with editable native elements -> `ppt-master`
- `.pptx` built through artifact-tool / Google Slides -> `Presentations`

## Installed Resources

The upstream skill resources live in this skill directory:

- `references/upstream-SKILL.md`: original Claude Code skill instructions.
- `references/upstream-AGENTS.md`: upstream multi-agent entry notes.
- `workflows/`: optional workflow add-ons for preview, review, chart verification, animation, audio, brands, and templates.
- `scripts/`: deterministic helpers, including `svg_to_pptx.py`, project management, validators, converters, image analysis, and TTS helpers.
- `templates/`: upstream layout and spec templates.
- `requirements.txt`: Python dependencies declared by upstream.

Read `references/upstream-SKILL.md` before running a full PPT creation workflow. Load workflow files only when the requested feature needs them.

## Codex Safety Overrides

These override upstream Claude Code assumptions.

1. Work in the user's active workspace, not inside the installed skill folder.
2. Do not let `project_manager.py import-sources --move` move the user's original files. If the upstream workflow requires `--move`, first copy the sources into a project staging folder, then run `--move` on those copies.
3. Use absolute paths in commands and outputs.
4. On Windows, run PPT Master scripts through the dedicated Conda environment `codex_ppt`.
5. Do not install or update dependencies silently. Check missing packages and report them, unless the user explicitly asks you to install.
6. Do not use the upstream `update_repo.py` to self-update the installed skill. Sync skill changes through the user's `codex-skills` Git repository.
7. Do not delegate per-slide SVG generation to subagents unless the user explicitly asks for subagents. The main Codex agent owns slide logic and final QA.

## Core Workflow

1. Confirm output target is editable `.pptx`.
2. If the input is a research paper or manuscript, use `paper-talk-prep` first unless the user already provided a slide-by-slide plan.
3. Create or select a project folder in the active workspace.
4. Import source material into the project using upstream scripts, with the staging-copy safety rule above.
5. Build `SPEC.md` / slide plan before drawing pages.
6. Author slides as SVG pages following upstream canvas, naming, and validation rules.
7. Run upstream validation and visual review scripts when available.
8. Convert SVG slides to PPTX with `scripts/svg_to_pptx.py`.
9. Open or render the resulting PPTX for verification when practical.
10. Report output paths, validation status, and any missing dependency or conversion limitations.

## Useful Commands

Use the dedicated Conda environment:

```powershell
$SKILL_DIR = 'C:\Users\Lingwei\.codex\skills\ppt-master'
conda run -n codex_ppt python "$SKILL_DIR\scripts\svg_to_pptx.py" --help
conda run -n codex_ppt python "$SKILL_DIR\scripts\batch_validate.py" --help
conda run -n codex_ppt python "$SKILL_DIR\scripts\project_manager.py" --help
```

The `codex_ppt` environment is expected at `D:\Anaconda\envs\codex_ppt` on this Windows machine. It contains the upstream requirements plus `cairosvg` for stronger SVG-to-PNG fallback rendering.

For SVG to PPTX export:

```powershell
$SKILL_DIR = 'C:\Users\Lingwei\.codex\skills\ppt-master'
conda run -n codex_ppt python "$SKILL_DIR\scripts\svg_to_pptx.py" "<project_path>" -o "<output.pptx>"
```

For optional live preview or visual review behavior, read:

- `workflows/live-preview.md`
- `workflows/visual-review.md`
- `references/visual-review.md`

For templates or brand systems, read:

- `workflows/create-template.md`
- `workflows/create-brand.md`
- `references/template-designer.md`
- `references/shared-standards.md`

For animations or speaker audio, read:

- `workflows/customize-animations.md`
- `workflows/generate-audio.md`
- `references/animations.md`

## Handoff Contract

When receiving an approved plan from `paper-talk-prep`, preserve:

- slide number
- slide title
- slide goal
- on-slide text
- visual suggestion
- speaker notes
- transition sentence

Keep speaker notes out of visible slide body text unless the user asks for text-heavy slides.
