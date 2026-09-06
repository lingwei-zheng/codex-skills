# High-Resolution Policy

Apply this policy to an explicit raster-generation resolution or model-quality
requirement, such as 2K, high resolution, or `--highres`. A user-selected distinct
high-resolution model also establishes the requirement.

## Scope

- `final export`, `final-export`, or `final quality` alone means completion, not
  selection of a distinct high-resolution model. Use the normal configured route
  unless the user separately specifies a raster resolution or model-quality tier.
- Editable Draw.io/SVG/PDF export alone does not invoke a raster-generation model.
  For mixed figures, this policy governs only the raster-generation component.
- Use `NANOBANANA_HIGHRES_MODEL` or `OPENAI_IMAGE_HIGHRES_MODEL` when the explicit
  high-resolution request selects that configured route. Honor an explicit model
  choice and retain provider-selection and third-party transmission approvals.

## Fail-closed behavior

When an explicitly requested high-resolution path is unavailable or fails:

- Stop the affected generation operation, not independent authorized work.
- Do not silently downgrade the model, resolution, or quality tier.
- Ask the user whether to retry that high-resolution generation or explicitly
  allow a fallback. No automatic paid retry or inferred approval from silence.
- While waiting, finish independent label checks, caption work, and source-file
  preparation where these do not require the missing image or pending decision.

These rules include missing model configuration, HTTP 429, upstream failures,
and network errors. Do not report the requested high-resolution asset as complete
when only its preparation is finished.
