---
name: research-framework-figure-workflow
description: Default workflow for creating, reviewing, and iterating thesis or research-paper conceptual framework figures by combining NORA research-logic skills with paper-framework-figure visual candidate generation. Use when the user asks to make a conceptual framework figure, thesis overview figure, paper framework diagram, graphical model, dissertation figure, or wants NORA plus paper-framework-figure to produce prompts, candidate boards, captions, manifests, review notes, or final figure revisions from a manuscript, thesis, proposal, or paper draft.
---

# Research Framework Figure Workflow

Use this skill as the default orchestrator for research framework figures. It separates **research logic** from **visual production**:

- NORA defines and audits the thesis/paper argument, claim-evidence structure, figure inventory, captions, and revision checklist.
- `paper-framework-figure` handles visual subtype diagnosis, candidate boards, target-image isolation, second-round optimization, final image prompts, and image generation.

Do not let image generation invent the conceptual model. Lock the model first with NORA-style artifacts, then generate and revise visuals.

Do not route conceptual framework figures through `nature-figure`. `nature-figure` is for empirical publication plots and multi-panel scientific figures, not for defining or rendering conceptual models.

## Required Skill Routing

When this skill triggers, also use these local skills when available:

1. `nora` at `C:/Users/Lingwei/.codex/skills/nora/SKILL.md`
2. `paper-framework-figure` at `C:/Users/Lingwei/.codex/skills/paper-framework-figure/SKILL.md`

Read only the needed sections of their `SKILL.md` files:

- From NORA: read root routing plus `skills/paper-plan/SKILL.md`, `skills/paper-figure-generate/SKILL.md`, and, when critique is requested, `skills/paper-review-loop/SKILL.md`.
- From `paper-framework-figure`: read the response-mode contract, candidate-image bridge, P6b/P6b-IMAGE/P6c requirement, and text-reply section requirements.

If either skill is missing, continue with the available half and explicitly record the gap.

## Workflow

### 1. Intake And Source Lock

Identify the source manuscript and figure target:

- thesis/paper/proposal file path;
- target slot such as introduction overview, methods overview, graphical abstract, or chapter roadmap;
- target language for labels;
- whether paper/chapter tags should appear in the figure;
- whether the final deliverable must be editable as SVG/PPT after raster ideation.

Prefer existing project files over asking the user. If multiple plausible source files exist, use the newest or most explicit manuscript file and record the assumption.

If `.codex/project.yaml` defines `paths.manuscript.source_of_truth`, use that Markdown manuscript as the preferred source before scanning for Word, PDF, or legacy draft files. Treat generated DOCX files as exchange copies unless the user explicitly says the figure should follow a reviewed Word version.

### 2. NORA Logic Pass

Use NORA-style planning before visual design. Extract:

- one-sentence thesis or paper claim;
- 3-6 core concepts that must appear;
- research questions or sub-paper/chapter roles;
- claim-evidence map;
- figure purpose and skim-reader takeaway;
- relationships that must be arrows, bridges, mediators, moderators, contexts, or feedback loops;
- forbidden or risky interpretations.

Write or update a lightweight project artifact at `output/PAPER_PLAN.md` when no stronger plan exists. For a single figure, keep it concise and figure-focused.

### 3. NORA Figure Specification

Use NORA `paper-figure-generate` conventions for conceptual diagrams. Produce these files:

- `output/figures/FIGURE_MANIFEST.md`
- `output/figures/FIGURE_CAPTIONS.md`
- `output/figures/prompts/Fig01_<slug>_prompt.md`
- `output/figures/prompts/Fig01_<slug>_prompt.txt`
- `output/figures/prompts/Fig01_<slug>_design_notes.md`

Load `references/artifact-templates.md` for the expected structure when creating these artifacts.

### 4. Visual Candidate Bridge

Use `paper-framework-figure` for visual routing:

1. P2/P3 diagnose figure subtype and produce text candidates.
2. P4 set up first-round candidate board.
3. P5 generate first-round target-paper candidates as `IMAGE_ONLY`.
4. P6 review first-round candidates.
5. P6b set up paper-local best-practice second-round variants.
6. P6b-IMAGE generate second-round variants as `IMAGE_ONLY`.
7. P6c select or combine final direction.
8. P7 write final image prompt.
9. P8 generate formal target-paper image as `IMAGE_ONLY`.
10. P9 review, caption, and handoff.

Do not skip P6b/P6b-IMAGE/P6c after a first-round selection unless the user explicitly asks to stay text-only or skip image candidates.

### 5. NORA Review Loop For Rendered Figures

After each formal render, inspect the image and run a NORA-style critique:

- Does the figure state the main thesis/paper claim?
- Do paper/chapter tags support the structure without becoming a table?
- Are arrows semantically correct?
- Are mediators, contexts, bridges, and feedback loops visually distinguishable?
- Are planning/application implications integrated without dominating the mechanism?
- Are labels clipped, crowded, mistranscribed, or overflowing?
- What single revision would most reduce conceptual misreading?

Write or update `output/figures/Fig01_NORA_REVIEW.md`.

### 6. Final Handoff

End with:

- paths to current render and prompt artifacts;
- selected visual direction;
- remaining conceptual or rendering risks;
- exact next prompt for revision or editable conversion.

Run NORA checkpointing before pausing a multi-step workflow:

```powershell
python "C:/Users/Lingwei/.codex/skills/nora/scripts/nora_checkpoint.py" --workspace .
```

## Production Rules

- Use `image_gen` only for target-paper raster candidate/final images when `paper-framework-figure` allows an `IMAGE_ONLY` step.
- Do not call `nature-figure` for this workflow.
- Never embed target-paper candidate, second-round, formal, final, or revision images in prose replies.
- For text replies governed by `paper-framework-figure`, obey its required section order and state footer.
- Prefer English labels for manuscript figures unless the user requests another language.
- Keep figure text minimal; put details in caption or design notes.
- Do not fabricate numeric results, datasets, citations, or claims.
- Keep NORA artifacts project-local under `output/`.
- Copy generated images into `output/figures/` only when registering them; leave originals in the generated image folder.

## Common User Requests

- "Use this as the default drawing workflow" -> run this skill, then ask only for missing source/target if no manuscript is discoverable.
- "Make a thesis conceptual framework figure" -> run NORA logic pass, then paper-framework candidate workflow.
- "Review this framework figure" -> inspect image, run NORA review loop, then if needed map to `paper-framework-figure` revision step.
- "Generate the final figure" -> verify P6c/P7 are complete; if not, complete the required setup first.
- "Make it editable" -> after raster direction is locked, recommend or build an SVG/PPT recreation from the approved structure.

## Reference Files

- `references/artifact-templates.md`: compact templates for NORA-style figure plan, prompt, caption, manifest, and review notes.
