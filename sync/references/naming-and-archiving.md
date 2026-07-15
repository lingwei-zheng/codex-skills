# Naming And Archiving Protocol

Use this protocol whenever `sync` creates, renames, or archives research outputs.

## Current Versus Archived

- Keep active and still-changing artifacts in `output/current/`.
- Copy or move an important completed output batch into
  `output/archived_runs/` at a meaningful checkpoint.
- Archive a batch when it supports a reported result, manuscript revision,
  coauthor exchange, submission package, reviewer response, or reproducible run.
- Do not archive every incidental preview or temporary file.
- Do not overwrite a prior archive. Create a new dated version.

## File Names

Do not use ambiguous names such as:

- `final.docx`
- `final_v2.docx`
- `real_final.docx`
- `latest`
- `updated`
- `test`

Use:

`YYYY-MM-DD_vNN_filetype_short_description.ext`

Examples:

- `2026-05-12_v02_manuscript_main_after_coauthor_comments.docx`
- `2026-05-20_v03_Table2_model_performance.xlsx`
- `2026-05-20_v03_Figure3_calibration_plot.pdf`

Keep analysis version labels readable, for example
`v02_add_clinical_covariates`. Increment `vNN` when the output meaningfully
changes, not after every save.

## Archive Batch Names

Name each archive folder:

`YYYY-MM-DD_vNN_short_purpose`

Keep related tables, figures, reports, and machine-readable outputs from the same
run together. Do not mix outputs produced with materially different configs.

## Archive Procedure

1. Confirm which files form one reproducible output batch.
2. Record the scripts or notebooks, configs, inputs, and purpose.
3. Create a dated and versioned archive folder.
4. Preserve the outputs without overwriting an earlier batch.
5. Add a short provenance note using
   [archived-run-readme-template.md](archived-run-readme-template.md).
6. Update the relevant analysis or manuscript log with the archive path and why
   this checkpoint matters.
7. Keep only the active working copies needed for the next step in
   `output/current/`.

An archive records what was produced and with which settings. Git records code
and text changes; the logs record why the decision was made. Do not ask one layer
to replace the others.
