# Editable Figure Handoff

Use this reference when the user asks for an editable conceptual figure, native
Draw.io source, or editable SVG.

## Positioning

Use the installed official `drawio` skill as the default editable backend.
Prefer native object structure from the beginning instead of reconstructing a
raster after generation.

## Draw.io-First Route

1. Pass the locked semantic graph, render graph, visible-text allowlist, and
   negative constraints to `drawio`.
2. Author a native `.drawio` file, using XML when precise placement or styling
   is required.
3. Preserve the `.drawio` source as the primary artifact.
4. Export SVG, PNG, or PDF with embedded diagram XML when the local Draw.io
   Desktop CLI is available.
5. Without the Desktop CLI, deliver the native `.drawio` file or URL route
   supported by the official skill. Do not flatten the figure merely because
   export tooling is unavailable.

## Optional Raster Reconstruction

AutoFigure-Edit remains an optional local post-processing route when the only
available source is a raster image. Treat it as a compatibility hook, not the
default editable workflow.

## Limitation

The upstream AutoFigure-Edit workflow is primarily `method text -> draft figure -> editable SVG`. It may support reference images and SVG reconstruction internally, but direct `existing Banana raster -> editable SVG` depends on local wrappers or custom setup.

## Suggested Local Variables

- `AUTOFIGURE_EDIT_ROOT`
- `AUTOFIGURE_EDIT_PYTHON`
- `AUTOFIGURE_EDIT_OUTPUT_DIR`
- `AUTOFIGURE_EDIT_ENABLED=1`

## Handoff Artifacts

- `figure.drawio`
- optional `figure.drawio.svg`, `figure.drawio.png`, or `figure.drawio.pdf`
- `figure-brief.json`
- `semantic-audit.md`
- `issue-ledger.md`
- for raster reconstruction only:
  - `figure.png`
  - `prompt.txt`
  - `method.txt`
  - optional `handoff.json`

## Source-of-Truth Rule

The reviewed figure brief defines meaning. The `.drawio` file defines editable
layout. Exported raster or PDF files are delivery artifacts and must not become
the only editable source.

## Conservative AutoFigure Wording

Use wording like:

`This raster figure can optionally be handed off to a local AutoFigure-Edit deployment for editable SVG reconstruction or refinement if that pipeline is available on this machine.`

Do not describe raster-to-SVG reconstruction as guaranteed.
