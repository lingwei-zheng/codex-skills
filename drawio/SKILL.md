---
name: drawio
description: >-
  Create or edit native Draw.io diagrams and optionally export editable
  PNG/SVG/PDF files. Use when the user explicitly requests Draw.io or an
  editable diagram, or when engineering-figure-agent selects Draw.io for a
  reviewed, label-heavy conceptual framework, mechanism diagram, architecture,
  workflow, ER diagram, sequence diagram, network diagram, or other
  topology-sensitive figure. For unreviewed academic conceptual figures, use
  conceptual-figure-workflow first; use nature-figure for statistical plots and
  maps.
---

# Draw.io

This is a compact local adaptation of the official
[`jgraph/drawio-mcp`](https://github.com/jgraph/drawio-mcp) Codex skill. Generate
native `.drawio` files from Mermaid or Draw.io XML, then optionally apply layout
or export editable PNG, SVG, or PDF files.

## Research Routing

- Treat Draw.io as an editable execution backend, not as the authority on
  theory, mechanisms, or claims.
- For academic conceptual figures, preserve the semantic graph, render graph,
  visible-text allowlist, negative constraints, and issue ledger supplied by
  `conceptual-figure-workflow` and `engineering-figure-agent`.
- Every arrow must map to an approved semantic edge. Do not invent labels,
  feedback loops, causal directions, variables, stages, or evidence.
- Use `nature-figure` for empirical maps, statistical charts, and exact
  quantitative panels.

For the meaning of approved nodes and edges, read [semantic approval scope](../engineering-figure-agent/references/figure-brief-spec.md#meaning-of-approved-semantics). Directly supported semantics do not require an extra approval round; new or conflicting scientific assertions still require a user decision.

## Workflow

1. Read the reviewed figure contract or establish the requested non-academic
   diagram structure.
2. Detect whether the Draw.io Desktop CLI is available.
3. Choose an authoring route:
   - Mermaid for standard flowcharts, sequence/class/state/ER diagrams,
     timelines, mind maps, C4 diagrams, and other supported types when the
     Desktop CLI is available.
   - Draw.io XML for precise placement, custom styling, special shape libraries,
     or any machine without the Desktop CLI.
4. Create a native `.drawio` file first.
5. For XML, optionally apply one layout pass:
   - `verticalFlow` or `horizontalFlow` for pipelines
   - `verticalTree`, `horizontalTree`, or `radialTree` for hierarchies
   - `organic` for networks
   - `libavoid` only to reroute edges without moving nodes
6. Validate XML structure and audit labels, nodes, and arrows against the figure
   contract.
7. Deliver the native `.drawio` source. When requested and the Desktop CLI is
   available, also export PNG, SVG, or PDF with embedded diagram XML.
8. Report absolute source and export paths. Do not silently flatten an editable
   research figure because optional export tooling is unavailable.

## Authoring Rules

- Mermaid must be converted to `.drawio` before export. Do not export `.mmd`
  directly to an embedded PNG/SVG/PDF.
- Prefer XML when scientific labels, ports, edge direction, or topology must be
  exact.
- Keep the `.drawio` source as the primary editable artifact even after export.
- Match diagram labels to the user's requested language.
- Use concise labels and ensure the figure remains readable at its intended
  publication size.
- Do not apply both ELK and `libavoid` to the same result; ELK already routes its
  edges.

## Critical XML Rules

- Start with an `mxGraphModel` containing root cells `id="0"` and `id="1"`.
- Escape `&`, `<`, `>`, and quotes in attribute values.
- Use a unique ID for every `mxCell`.
- Give every edge a child `<mxGeometry relative="1" as="geometry" />`.
- Do not include XML comments in generated diagram files.
- Validate XML well-formedness before opening or exporting.

## References

Read only what is needed:

- `references/cli-export-and-troubleshooting.md`: Desktop CLI discovery,
  conversion, layout, export, URL delivery, and common failures.
- Official Mermaid reference:
  `https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/mermaid-reference.md`
- Official Draw.io XML reference:
  `https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-reference.md`

## Minimal Commands

Convert Mermaid to native Draw.io:

```bash
drawio -x -f xml -o diagram.drawio diagram.mmd
```

Apply an XML layout:

```bash
drawio -x -f xml --layout horizontalFlow -o diagram.drawio diagram.drawio
```

Export with editable XML embedded:

```bash
drawio -x -f svg -e -b 10 -o diagram.drawio.svg diagram.drawio
```

When the Desktop CLI is unavailable, author Draw.io XML directly and deliver
the `.drawio` file. Node.js may still be used for the optional browser-URL route.
