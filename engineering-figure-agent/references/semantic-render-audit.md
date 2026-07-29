# Semantic and Render Audit

Use this reference for conceptual figures where arrows, labels, or topology carry
scientific meaning. It adapts the strongest controls from
[`paper-framework-figure-studio-pro`](https://github.com/c-narcissus/paper-framework-figure-studio-pro)
without importing its fixed stage gates, candidate counts, checkpoint archives,
or terminal-response rules. The wording and compact workflow here are original
to this local adaptation.

## Two Contracts

Keep scientific meaning separate from visual implementation.

### Semantic graph

Record:

- each approved concept, construct, stage, actor, or dataset as a node
- each approved relationship as an edge with source, target, direction, type,
  evidence status, and causal status
- unresolved or disputed relationships in an issue ledger
- concepts that must remain separate even if visually similar

An arrow is not decoration. It asserts a directional relationship. Use a line,
grouping container, proximity, or shared color when direction is not supported.

### Render graph

Translate the semantic graph into:

- panels, regions, layers, or swimlanes
- containers and parent-child hierarchy
- node placement and reading order
- edge ports and routing
- visual encodings for evidence level, uncertainty, scale, or actor type

The render graph may simplify appearance but must not add, remove, merge, or
reverse semantic relationships.

## Text Contract

Create a visible-text allowlist before rendering:

- exact node labels
- exact edge labels
- exact panel titles
- approved abbreviations and symbols
- optional legend terms

Reject any visible text outside the allowlist unless the user approves it.
Generated captions, figure numbers, explanatory prose, invented metrics, and
decorative acronyms are not permitted inside the figure.

## Negative Constraints

List what the figure must not imply. Common constraints include:

- no causal arrow where evidence is associational
- no scale-free mechanism when effects depend on spatial or temporal units
- no feedback loop without temporal or theoretical support
- no merging of exposure, vulnerability, access, and outcome
- no data flow that reverses collection, processing, modeling, and inference
- no decorative map, icon, or color legend that suggests an unmeasured variable

## Optional Candidate Exploration

Use exploration only when the figure has genuine structural ambiguity or high
publication stakes.

1. Lock the semantic graph, text allowlist, and negative constraints.
2. Produce 2-4 low-cost structural candidates that differ in composition, not
   scientific content.
3. Compare candidates using one issue ledger:
   - semantic fidelity
   - reading order
   - visual hierarchy
   - label burden
   - arrow crossings and ambiguity
   - editability at journal column width
4. Select one direction or at most two.
5. Produce 1-2 refined candidates and stop for human selection when the choice
   is aesthetic rather than scientific.

Do not multiply candidates when the requested layout is already clear.

## Final Audit

Before delivery, verify:

1. Every rendered node maps to one semantic node.
2. Every arrow maps to one approved semantic edge.
3. Edge direction, type, and certainty are unchanged.
4. All visible text is allowlisted and spelled exactly.
5. No unresolved issue is hidden by visual polish.
6. Reading order matches the intended argument.
7. The figure remains legible at its intended publication size.
8. Editable output preserves object structure rather than flattening everything
   into a single raster.
