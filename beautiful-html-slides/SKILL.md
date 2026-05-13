---
name: beautiful-html-slides
description: Build polished standalone HTML slide decks using the bundled beautiful-html-templates library from zarazhangrui. Use when the user asks to create, design, adapt, preview, or generate an HTML presentation, HTML slides, a web slide deck, or a beautiful browser-openable deck from a topic, outline, research notes, pitch, lecture, or report.
---

# Beautiful HTML Slides

## Core Workflow

Use the bundled template library at `assets/beautiful-html-templates`.

1. Read `assets/beautiful-html-templates/AGENTS.md` first and follow its workflow unless the user explicitly overrides it.
2. Ask the required occasion and mood questions before choosing templates.
3. Read `assets/beautiful-html-templates/index.json` and pick three tone-matched candidate templates.
4. Build title-slide previews for the three candidates using the user's real title/topic/subtitle/author/date when available.
5. Open each preview in the browser and send the user the absolute paths.
6. After the user chooses a template, clone that template folder into the user's workspace and replace the demo content with the user's actual content.
7. Open the final deck in the browser and send the absolute path.

On Windows, use `Start-Process <absolute-html-path>` to open local HTML files. On macOS, use `open <absolute-html-path>`.

## Template Rules

Preserve each chosen template as a complete visual system:

- Keep its fonts, palette, grid, slide classes, decorative elements, and navigation runtime.
- Replace all placeholder headlines, body copy, numbers, labels, names, dates, attributions, and image placeholders.
- Duplicate existing slide layouts when more slides are needed.
- Remove slides from the bottom when fewer slides are needed.
- Update page numbers after adding or removing slides.
- If the deck needs a missing layout, design it from scratch using the chosen template's existing fonts, colors, spacing, chrome, and component grammar.

Do not mix layouts from different templates.

## Output Expectations

Create artifacts in the user's active workspace, not inside the skill folder. Keep template assets beside the generated HTML when the template requires sibling CSS or JavaScript.

For previews and final decks, always provide:

- The absolute file path.
- A short note on the tone/template choice.
- Any caveat about custom layouts or missing user content.
