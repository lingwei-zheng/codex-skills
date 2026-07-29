---
name: engineering-figure-agent
description: >-
  Use when the user needs to execute an already scoped engineering or
  research-paper figure brief, including system architecture diagrams,
  algorithm workflows, hardware schematics, mechanism diagrams, graphical
  abstracts, editable Draw.io diagrams, redraws, or image edits.
  Uses the official OpenAI image path by default, with Gemini, Nano Banana, and
  other providers retained as explicit opt-in compatibility paths.
  For conceptual framework or experiment-design figures whose theory,
  variables, mechanisms, or claim-evidence boundaries are not yet reviewed, use
  conceptual-figure-workflow first.
---

# Engineering Figure Agent

Use this skill after the figure goal is already reasonably clear. For conceptual
framework or experiment-design figures, prefer `conceptual-figure-workflow` first
so `academic-research` can review the theory structure and produce a figure brief
before this skill handles schematic or image execution.

## Boundary

Good fit:

- Turn a figure brief into a conceptual diagram, workflow figure, schematic,
  graphical abstract, redraw, or edited image.
- Produce an editable `.drawio` figure when labels, arrows, topology, or later
  manual revision must remain exact.
- Build prompts, generate conceptual panels, and refine existing briefs.
- Assemble already rendered quantitative panels with a schematic when the panel
  contract is fixed.

Not the main tool for:

- Deciding from scratch what claim the paper should visualize.
- Full paper-argument or reviewer-style critique.
- Reviewing theoretical structure, variable relationships, mechanisms, hypotheses, or claim-evidence boundaries for a conceptual framework.
- Creating empirical, statistical, benchmark, ablation, map, or multi-panel
  results figures from numeric data. Use `nature-figure` for those tasks.

If the user is still deciding the figure claim, panel logic, or caption argument,
use `conceptual-figure-workflow` or `academic-research` first.

Legacy plot scripts and references remain for upstream compatibility. Do not load
or invoke them in normal routing; send numeric-data figure work to
`nature-figure`.

## Core Decision

- `openai-image` mode: illustrative conceptual figures, graphical abstracts,
  reference-inspired redraws, and image edits where visual synthesis matters
  more than object-level editability.
- `drawio` mode: label-heavy conceptual frameworks, mechanism diagrams,
  architecture/workflow figures, or any figure requiring exact nodes, arrows,
  topology, and editable vector-like objects. Route execution to the installed
  `drawio` skill while preserving this skill's reviewed figure contract.
- `mixed` mode: use `nature-figure` to produce quantitative panels, then use this
  skill only for conceptual panels or final schematic-led composition. Use
  Draw.io when the final composition must remain editable.

Never use image generation for exact values, axes, or benchmark geometry.

## Default Workflow

1. Inspect the user input and decide whether a figure brief is already present.
2. If needed, create a brief using `references/figure-brief-spec.md`.
3. Lock the semantic contract before rendering: nodes, directed relationships,
   evidence status, visible-text allowlist, prohibited implications, and any
   unresolved issue ledger.
4. Choose `openai-image`, `drawio`, or `mixed` mode. Prefer Draw.io when a
   mislabeled arrow or generated-text error would change the scientific claim.
5. For image execution, prefer the prompt-builder scripts; read template
   references only when template wording needs customization.
6. For Draw.io execution, hand the semantic and render contracts to `drawio`.
   Keep the `.drawio` source as the primary editable artifact.
7. For a mixed figure, obtain quantitative panels from `nature-figure` without
   asking image generation to redraw their values, axes, or geometry.
8. When the brief selects `explore`, create 2-4 structurally distinct low-cost
   candidates, compare them against one issue ledger, then refine only 1-2
   directions. Do not use candidate exploration by default.
9. Audit the final figure against the semantic contract. Reject unsupported
   arrows, unapproved visible text, reversed flows, duplicated concepts, and
   decorative elements that imply evidence not present in the brief.
10. Save prompt/spec/source/output paths when files are produced, then run only
   the checks needed for the touched path.

## Reference Loading

Read only what is needed:

- `references/figure-brief-spec.md`: brief structure and mode rules.
- `references/semantic-render-audit.md`: semantic graph, render graph, text
  allowlist, candidate comparison, and final audit.
- `references/publication-figure-design.md`: publication styling defaults.
- `references/provider-selection.md`: OpenAI-first setup and optional
  Gemini/Banana compatibility.
- `references/highres-policy.md`: high-resolution and fail-closed rules.
- `references/chinese-labels.md`: Chinese label readability rules.
- `references/engineering-figure-templates.md` and `references/materials-science-figure-template.md`: template wording when script output needs customization.
- `references/editable-figure-handoff.md`: Draw.io-first editable handoff and
  optional SVG reconstruction.

## Scripts

- Build a prompt without network calls:

```bash
python scripts/build_engineering_figure_prompt.py --figure-template system-architecture --lang en "technical background"
python scripts/build_materials_figure_prompt.py --materials-figure mechanism-figure --lang en "scientific background"
```

- Generate or edit a conceptual image:

```bash
python scripts/generate_image.py --provider openai --figure-template system-architecture --lang en "technical background"
python scripts/generate_image.py --provider openai --materials-figure mechanism-figure --lang en "scientific background"
```

- Use the unified CLI:

```bash
python scripts/efa.py prompt --figure-template system-architecture "technical background"
python scripts/efa.py prompt --materials-figure mechanism-figure "scientific background"
python scripts/efa.py check
```

## Quality Rules

- Do not fabricate measurements, benchmark values, hardware specs, or unsupported causal claims.
- Keep arrows, reading order, and module hierarchy explicit.
- Treat every arrow as a scientific assertion. Match it to an approved semantic
  edge and preserve direction, relation type, and certainty.
- Render only allowlisted visible text. Do not let image generation invent
  acronyms, metrics, stages, captions, or explanatory labels.
- Favor white backgrounds, publication-style spacing, and readable labels.
- Use prompt-first workflows when layout fidelity matters.
- Use the official OpenAI image path by default. Use Gemini, Banana, relays, or
  other providers only when the user explicitly selects them.
- For high-resolution requests, follow `references/highres-policy.md`.
- For third-party providers, require explicit opt-in before sending keys or user files.
- For Chinese figures, preserve standard technical notation when it improves clarity.
