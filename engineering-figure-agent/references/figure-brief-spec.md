# Figure Brief Spec

Engineering Figure Agent uses a figure brief as the platform-neutral input contract between paper thinking and figure production. Codex is the primary authoring environment, but the same brief can be used in Claude Code, ChatGPT, Claude, VS Code, Obsidian, or a future CLI.

## Meaning of approved semantics

`Approved` nodes and edges mean either semantics explicitly confirmed by the user,
or semantics directly verifiable from the supplied materials without changing their
scientific meaning. This word alone does not add a per-node or per-edge user gate.
Preserve source evidence, relationship direction, certainty, and causal status.
New inferences, conflicting directions, or content the user explicitly reserved
for review require a user decision; the agent cannot approve its own invented
mechanism. Record those pending choices and continue only independent authorized
preparation. Rendering must not silently include unsettled scientific assertions.

## Required Fields

| Field | Type | Purpose |
|---|---|---|
| `figure_goal` | string | What this figure should help the paper prove or explain. |
| `paper_claim` | string | The claim, method contribution, or result the figure supports. |
| `figure_type` | string | `system-architecture`, `algorithm-workflow`, `graphical-abstract`, `electronic-schematic`, `benchmark-plot`, `mixed-panel`, or a domain-specific label. |
| `mode` | string | `openai-image`, `drawio`, or `mixed`. |
| `panels` | array | Panel/module plan, in reading order. |
| `semantic_nodes` | array | Approved concepts, constructs, stages, actors, or datasets. |
| `semantic_edges` | array | Approved source-target relationships with direction, relation type, evidence status, and causal status. |
| `render_graph` | object | Panels, containers, hierarchy, reading order, edge ports, and visual encodings. |
| `visible_text_allowlist` | array | Exact text permitted inside the figure. |
| `must_keep_labels` | array | Terms that must remain faithful to the paper. |
| `negative_constraints` | array | Relationships, labels, mergers, or implications the figure must not introduce. |
| `issue_ledger` | array | Unresolved scientific or visual decisions that must remain visible during iteration. |
| `candidate_mode` | string | `single` by default or `explore` when structural alternatives are genuinely useful. |
| `data` | object | Numeric arrays, tables, links to data files, or `not_applicable`. |
| `style_constraints` | array | Venue, palette, language, density, aspect ratio, or export constraints. |
| `output_formats` | array | For example `drawio`, `png`, `pdf`, `svg`, or `prompt-only`. |
| `verification_checklist` | array | What must be checked before the figure is used in a paper. |

## Research Evidence Continuity

For research figures, reuse existing brief fields rather than adding a second
schema: `paper_claim` carries the C# and supported advantage; each panel's
`purpose` names its argument job; `data`/`evidence_or_data` points to E#, source
version and transformation (or explicit theory/hypothesis status); include
caption-to-manuscript alignment in `verification_checklist`.

Keep an internal trace from source/derivation to each caption assertion and the
manuscript claim. Keep claim IDs, file locations, version labels and approval
history in working notes, not publication-facing labels or captions unless the
user explicitly requests that audit information. Numeric arrays, visible labels and scientific meaning remain
unchanged by visual emphasis. A conceptual mechanism is not empirical evidence;
do not render an unsettled assertion. For quantitative panels use the
`nature-figure` evidence trace and its selected backend/confirmation rules.

## Mode Rules

- Use `openai-image` for illustrative conceptual synthesis, graphical abstracts,
  reference-inspired redraws, or image editing.
- Use `drawio` when nodes, labels, arrows, topology, or later manual revision
  must remain exact and editable.
- Use `mixed` when a figure combines `nature-figure` quantitative panels with
  conceptual panels or an editable schematic composition.
- Do not invent numeric data. If numeric values are missing, ask for data or keep the figure conceptual.
- Set `candidate_mode` to `explore` only when composition is materially
  ambiguous. Keep semantics fixed across candidates.

## Minimal JSON Example

```json
{
  "figure_goal": "Explain the full RAG pipeline in one publication-style architecture figure.",
  "paper_claim": "The method improves answer reliability by separating retrieval, reranking, and synthesis.",
  "figure_type": "system-architecture",
  "mode": "drawio",
  "panels": [
    {
      "name": "Pipeline",
      "content": "Documents -> OCR -> Vector Search -> Answer Synthesis"
    }
  ],
  "semantic_nodes": [
    "Documents",
    "OCR",
    "Vector Search",
    "Answer Synthesis"
  ],
  "semantic_edges": [
    {
      "source": "Documents",
      "target": "OCR",
      "relation": "processing flow",
      "evidence_status": "method-defined",
      "causal": false
    },
    {
      "source": "OCR",
      "target": "Vector Search",
      "relation": "processing flow",
      "evidence_status": "method-defined",
      "causal": false
    },
    {
      "source": "Vector Search",
      "target": "Answer Synthesis",
      "relation": "processing flow",
      "evidence_status": "method-defined",
      "causal": false
    }
  ],
  "render_graph": {
    "reading_order": "left-to-right",
    "containers": ["Input Processing", "Retrieval and Synthesis"],
    "edge_routing": "orthogonal"
  },
  "visible_text_allowlist": [
    "Documents",
    "OCR",
    "Vector Search",
    "Answer Synthesis"
  ],
  "must_keep_labels": ["OCR", "Vector Search", "Answer Synthesis"],
  "negative_constraints": [
    "Do not show benchmark values.",
    "Do not add feedback loops."
  ],
  "issue_ledger": [],
  "candidate_mode": "single",
  "data": {"not_applicable": true},
  "style_constraints": ["white background", "short labels", "left-to-right flow", "English labels"],
  "output_formats": ["drawio", "svg"],
  "verification_checklist": [
    "All labels are readable at paper width.",
    "No unsupported numerical claims are shown.",
    "Data flow direction is unambiguous."
  ]
}
```

## Plot Request Relationship

For exact plots, the figure brief should point to or contain a `plot-request` object. The concise plot request is expanded by `scripts/build_plot_spec.py`, then rendered by `scripts/plot_publication_figure.py`.

The recommended multi-series scatter form is:

```json
{
  "kind": "scatter",
  "title": "Latency vs Accuracy",
  "xlabel": "Latency (ms)",
  "ylabel": "Accuracy",
  "data": {
    "series": [
      {"label": "Ours", "x": [24], "y": [0.93], "color": "blue_main"},
      {"label": "Baseline", "x": [39], "y": [0.83], "color": "red_strong"}
    ]
  }
}
```

Single-series scatter remains supported through `data.x` and `data.y`.
