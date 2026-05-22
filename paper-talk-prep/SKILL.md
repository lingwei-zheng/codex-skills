---
name: paper-talk-prep
description: Prepare slide-by-slide academic talks from a research paper, manuscript draft, extended abstract, or research summary. Use when the user wants to turn a paper into a presentation plan, defense deck outline, conference talk structure, seminar storyline, per-slide on-screen text, speaker notes, or a full speaking script. Also use when the user asks what each slide should contain, how to shorten a paper for a talk, how to present methods/results clearly, or how to generate slide-ready content before building the actual deck.
---

# Paper Talk Prep

Turn a paper into a talk plan before slide design starts. Produce the presentation structure, the text that belongs on each slide, and the words the speaker should say.

## Core Workflow

1. Identify the talk context:
   - paper title or draft source
   - audience
   - talk length
   - venue or format: class presentation, group meeting, conference talk, seminar, defense
   - language

   If `.codex/project.yaml` defines `paths.manuscript.source_of_truth`, use that Markdown manuscript as the default paper draft source before scanning for DOCX/PDF exports.

2. Choose the analysis route:
   - Use `academic-research-suite` for general academic papers and standard research communication tasks.
   - Use `nora` when the paper is in geoscience, GIScience, remote sensing, GeoAI, spatial data science, disaster resilience, environmental health, or related domains.
   - Use `nature-polishing` only if the user specifically asks to refine English wording for slide text or speaker notes.

3. Extract the paper's talkable structure:
   - problem and motivation
   - research question or claim
   - method logic
   - data or study setting
   - key results
   - limitations
   - contribution and takeaway

4. Convert the paper into a slide sequence:
   - decide the minimum viable number of slides for the allotted time
   - assign one rhetorical job to each slide
   - decide what must appear on-screen versus what should stay in speaker notes
   - keep slide text lean; move explanation into notes

5. Produce the requested artifact:
   - outline only
   - slide-by-slide content plan
   - slide-by-slide content plan plus speaker notes
   - full script

6. If the user wants the deck built, hand off the approved slide plan to the renderer that matches the requested output:
   - browser-openable HTML deck -> `beautiful-html-slides`
   - editable PowerPoint deck -> `ppt-master`
   - artifact-tool or Google Slides-oriented deck -> Presentations plugin when available

## Output Modes

Choose the smallest output that satisfies the request.

- `outline-only`: title plus one-line purpose for each slide.
- `slide-plan`: title, slide goal, on-slide text, and visual suggestion for each slide.
- `slide-plan-with-notes`: `slide-plan` plus speaker notes and transition sentence.
- `full-script`: `slide-plan-with-notes` plus a continuous presentation script.

Default to `slide-plan-with-notes` unless the user asks for a lighter or heavier output.

## Slide Design Rules

- Keep one main idea per slide.
- Keep on-slide text short enough to scan in a few seconds.
- Prefer bullets, short claims, equations, figure callouts, and result labels on slides.
- Move nuance, interpretation, caveats, and transitions into speaker notes.
- Do not paste paragraph prose onto slides unless the user explicitly wants text-heavy slides.
- Make the method and results sections carry the talk; compress literature review and long related-work material.
- If the source paper is dense, rewrite for oral delivery instead of mirroring section headings mechanically.

## Timing Heuristics

Use these defaults unless the user gives a slide count or structure.

- `5-7 min`: 5-7 slides
- `10-15 min`: 8-12 slides
- `20-30 min`: 12-18 slides
- `45-60 min`: 18-30 slides

For short talks, compress related work and limitations. For longer talks, add intuition, ablations, case studies, and implications.

## Required Per-Slide Contract

When producing slide-by-slide output, use the contract in `references/output-contract.md`.

Each slide should normally include:

- slide number
- slide title
- slide goal
- on-slide text
- visual suggestion
- speaker notes
- transition sentence

If the user asks for a concise version, omit `transition sentence` first. Do not omit `slide goal`.

## Talk Adaptation Rules

- For conference talks, prioritize novelty, method, results, and contribution.
- For defense talks, add background, study design justification, limitations, and future work.
- For lab meetings or reading groups, add interpretive commentary and discussion prompts.
- For teaching slides, define terms explicitly and slow down method exposition.

If the user gives a target audience, adapt vocabulary and assumed background to that audience.

## Hand-off To Deck Building

If the user asks to build slides after the content plan is approved:

1. Keep the slide numbering and titles stable.
2. Choose the renderer by output format:
   - `.html` or browser deck: pass only the approved slide sequence to `beautiful-html-slides`.
   - `.pptx` or editable PowerPoint: pass only the approved slide sequence to `ppt-master`.
   - artifact-tool presentation: use the Presentations plugin if that is the user's requested target.
3. Preserve the distinction between `on-slide text` and `speaker notes`.
4. Keep speaker notes as separate notes, not visible body copy.

## Deliverable Defaults

- Default language follows the user's request. If unspecified, mirror the language the user used.
- For bilingual requests, keep slide text concise and put fuller bilingual explanation in notes.
- When the source material is incomplete, explicitly mark inferred content as inference.
- When figures or tables are referenced but not available, describe the intended visual rather than inventing numeric detail.
