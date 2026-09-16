# Experiment To Paper Integration

The main agent coordinates the existing experiment roles and author-side paper
roles inline. Read the shared [research continuity protocol](../../../../shared/advantage-led-research-narrative.md).
This does not install another runtime, change pipeline gates, or enable external
transmission.

## Intake

Reuse the current Research Question Brief, Methodology Blueprint, configuration,
story handoff, or equivalent project files. Match meaning rather than requiring
exact heading strings. Ask only for missing information that changes execution.
Carry existing C# and E# identifiers forward. A plan is not an observed result.

## Producing ARS-Compatible Output

All experiment-agent outputs include a **Material Passport** header (ARS Schema 9):

```markdown
## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: [run | manage | validate | plan]
- Origin Date: [ISO 8601 timestamp]
- Verification Status: [UNVERIFIED | ANALYZED | VERIFIED]
- Version Label: [exp_result_v1 | study_status_v1 | validation_v1 | code_plan_v1 | study_protocol_v1]
```

**Verification Status rules:**
- `run` mode output → `UNVERIFIED` (results not yet validated)
- `manage` mode output → `UNVERIFIED` (data collected but not analyzed)
- `plan` mode output → `UNVERIFIED` (design artifact only; nothing has been executed yet)
- `validate` mode output without a successful reproducibility re-run → `ANALYZED` (statistical interpretation completed, but execution-level verification is absent, not applicable, or failed)
- `validate` mode output with a successful reproducibility re-run → `VERIFIED`
- Only upgrade a prior `run` artifact to `VERIFIED` after a successful reproducibility re-run. If re-run is skipped, not applicable, partial, or fails, keep the original artifact at `UNVERIFIED` and attach the separate validation report.

**Optional fields** (include when available):
- `Integrity Pass Date`: timestamp when validate mode completed
- `Upstream Dependencies`: version labels of artifacts this one depends on (e.g., if experiment used ARS Stage 1 RQ Brief)

## Evidence Handoff

Use the table in `../templates/output_formats.md` beside the existing passport.
It records planned and actual work, execution/skip status, comparison conditions,
result location/version, actual observations and verification status. Empty or
unknown evidence must not be auto-filled. No result-value or paper-quality
guarantee follows from a structurally complete table.

For an experiment-backed claim, the main agent checks the exact result location
and scope. Classify the implication in ordinary language: supported, needs a
narrower claim, contradicted, or insufficient evidence. Preserve material contrary
results and primary outcomes. Keep claim support separate from the passport's
reproducibility status; an evidence-backed claim can still lack a rerun.

## Authorized Continuation

1. Design roles establish the advantage hypothesis and experiment jobs.
2. Run/manage roles record actual execution and study metadata.
3. Validate only to the depth warranted by the stage and the claim.
4. The main agent updates the existing contribution/evidence map and marks any
   changed story assumptions before proceeding to the writer.
5. The writer orders evidence by argument, with traceable facts kept in the
   project records. Update dependent abstract, figures and conclusion together.

For a full research-to-paper task, continue without asking the user to copy
artifacts between internal roles. Preserve applicable experiment-retry,
scientific-parameter, ethics, independent-review and finalization approvals.
For run-only, plan-only or validation-only requests, deliver that result and stop
at the requested scope. A missing claim link blocks only dependent prose; work on
other authorized, supported sections may continue.
