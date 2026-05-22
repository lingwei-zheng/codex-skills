---
name: academic-workflow-router
description: "Route the user's recurring academic work into the right local skill without starting an oversized pipeline. Use when the user asks about the overall skill library, wants help choosing a skill, or has one of these common tasks: literature review, research design, Python/R data analysis, spatial analysis, results interpretation, discussion writing, academic writing or polishing, conceptual framework figures, paper-to-talk conversion, slide planning, or peer review. This skill is a lightweight dispatcher; it should select the smallest appropriate workflow and then hand off to the relevant specialist skill."
---

# Academic Workflow Router

Use this skill as the top-level decision layer for the user's recurring academic tasks. It should choose a route, state the route briefly, then load only the specialist skill needed for the current request.

Do not run a full NORA or Academic Research Suite pipeline unless the user explicitly asks for an end-to-end workflow.

## Default Task Routes

| User task | Default route | Secondary support |
|---|---|---|
| Literature review | `nora` -> `skills/lit-review/SKILL.md` with Zotero when available | `academic-research-suite` for stricter synthesis, claim-reference checks, or review design |
| Research design | `nora` -> `skills/refine-research/SKILL.md`, `skills/experiment-design/SKILL.md`, or `skills/experiment-design-pipeline/SKILL.md` | `academic-research-suite` as external critique |
| Data analysis and charts in Python/R | `data-analysis-and-figures` | NORA `spatial-analysis`, `nature-figure`, `pdf`, `docx` as needed |
| Reading results and writing discussion | `academic-research-suite` for claim/evidence logic, then `nature-polishing` or `journal-adapt` only for prose/style | NORA paper skills when the results belong to an active NORA project |
| Academic writing and polishing | `academic-research-suite` for structure and argument; `journal-adapt` for target-journal adaptation; `nature-polishing` for language polishing | NORA `paper-writing-pipeline` only for full manuscript generation from NORA artifacts |
| Conceptual framework figure | `research-framework-figure-workflow` | `paper-framework-figure`; do not route through `nature-figure` |
| Engineering, algorithm, system, or exact benchmark figure | `engineering-figure-agent` | `nature-figure` only for journal-format plot polish |
| Paper to talk, slides, or speaker notes | `paper-talk-prep` first | `beautiful-html-slides` for HTML decks; `ppt-master` for editable PPTX |
| Formal journal peer review | `peer-review` | NORA and ARS inside that skill |

## Routing Rules

1. Prefer one specialist entry point per request.
2. If the user names a target output format, let that format decide the renderer:
   - HTML/browser slides -> `beautiful-html-slides`
   - editable PowerPoint -> `ppt-master`
   - Word document -> `docx` or Documents plugin
   - PDF processing -> `pdf`
3. Treat `nora` as the default for geography, human geography, GIScience, GeoAI, spatial data science, health geography, remote sensing, environmental health, disaster resilience, and spatial experiments.
4. Treat `academic-research-suite` as the default for general academic reasoning, literature synthesis, manuscript logic, reviewer-style checks, and writing architecture outside a NORA project.
5. Keep renderer skills behind planning skills. For example, use `paper-talk-prep` before building a deck, and use `research-framework-figure-workflow` before generating a conceptual figure image.
6. When a request is small, answer or act directly with the smallest relevant skill instead of invoking a pipeline.

## Conflict Avoidance

- Do not stack multiple large orchestrators by default. Avoid routes such as NORA -> ARS -> peer-review unless the user asks for a combined review.
- Do not use `nature-figure` for conceptual framework figures. Use it for publication-quality plots, multi-panel empirical figures, or journal export checks.
- Do not use K-Dense-style broad workflow skills as defaults if they are installed later. Narrow package/database skills may support execution, but routing should stay here.
- If two skills both fit, choose the one closest to the user's requested deliverable rather than the broadest one.

## Response Pattern

When this skill routes a task, start with one short line:

`Route: <task> -> <skill(s)> because <reason>.`

Then proceed with the selected skill. If the route is uncertain, ask one concise question only when the answer materially changes the workflow.
