# Spatial Methods Decision Guide

Use this reference for GIScience, spatial statistics, remote sensing, GeoAI,
environmental-health, and health-geography work. Read
`../research-calibration.md` first. The research question and claim determine
the method; coordinates alone do not require a spatial model.

## Claim-First Intake

Before choosing a method, record:

- question type: description, pattern, process, association, prediction,
  mechanism, intervention, or transfer;
- unit and scale of observation and inference;
- whether aggregation, neighborhood, distance, boundary, or geographic
  transfer is part of the claim;
- the simplest credible baseline;
- the uncertainty that a more complex spatial method would resolve.

If a choropleth, summary statistic, global model, or simple comparison answers
the question, do not add GWR/MGWR, spatial regression, or a large sensitivity
grid for prestige.

## Spatial Dependence

Global Moran's I summarizes overall spatial autocorrelation; local indicators
such as LISA identify clusters and local outliers. Their interpretation depends
on the spatial weights definition, multiple-testing treatment, and substantive
meaning of the neighborhood.

Run residual spatial-dependence diagnostics when:

- a fitted regression or inferential model relies on residual independence;
- spatial dependence is substantively plausible; and
- a failure would change uncertainty estimates, model choice, or a central
  interpretation.

Do not require residual Moran's I for purely descriptive mapping, fixed-unit
summaries, or methods whose reported claim does not rely on residual
independence.

### Spatial weights

Choose contiguity, k-nearest-neighbor, distance, network, or domain-defined
weights according to the process being represented. Row standardization is
common, but not automatic: retain binary or other scaling when magnitude,
exposure, or the data-generating process requires it. Explain the choice.

## Regression And Local Models

Use a simple global model as a baseline when it is meaningfully comparable.
Escalate only for a named reason:

| Method | Appropriate trigger |
|---|---|
| Spatial lag | The outcome plausibly depends on neighboring outcomes and that spillover is part of the interpretation |
| Spatial error | Spatially structured omitted processes threaten inference, without a substantive outcome-spillover claim |
| GWR | Spatial variation in relationships is the research target, with adequate local information and a defensible bandwidth |
| MGWR | Different covariates are hypothesized to operate at different spatial scales and the added flexibility is interpretable |

MGWR is not inherently preferable to GWR, and neither is inherently preferable
to a global model. Local coefficient surfaces require uncertainty, multiple
testing, collinearity, edge, and bandwidth-aware interpretation.

## Diagnostics And Robustness Menu

Apply only triggered checks:

| Check | Trigger | Common N/A reason |
|---|---|---|
| Residual Moran's I | Inference relies on residual independence | Descriptive or non-inferential task |
| MAUP/alternative scale | Researcher-chosen aggregation may change the headline result | Unit fixed by process or claim explicitly single-scale |
| Alternative weights | Headline clustering or coefficient depends on neighborhood definition | Neighborhood fixed by physical/network process |
| Spatial CV | Nearby train/test observations may inflate out-of-area prediction | No spatial prediction or leakage prevented by design |
| Boundary sensitivity | Edge neighborhoods influence the claim | Interior-only analysis or excluded edge units |
| Temporal mismatch | Joined sources differ in time and the process may change over the gap | One time slice or substantively stable period |
| Subgroup/region analysis | A prespecified heterogeneity claim exists | No such claim, weak power, or first-draft scope |

For a first draft, run the one diagnostic most likely to invalidate the primary
result and at most two additional named-risk checks. Defer the rest with
triggers. Submission or reviewer-response stages may justify more.

## Prediction And Validation

Use spatial or buffered cross-validation when the target is geographic
generalization and spatial proximity can leak information. Standard random
cross-validation can be acceptable for non-spatial targets, independent
sampling by design, or explicitly within-sample prediction. State what the
validation design estimates: interpolation, transfer to new areas, transfer to
new times, or ordinary held-out performance.

## Interpolation

Use interpolation only for variables and processes where spatial continuity is
defensible. Inspect and report the variogram when kriging depends on it.
Compare plausible methods when method choice could change the conclusion; a
routine first draft does not need every interpolation variant. Do not
interpolate nominal categories as though they were continuous measurements.

## Remote Sensing And GeoAI

Trigger checks from the claim:

- use geographic or scene-level separation when transferability is claimed;
- inspect sensor, preprocessing, cloud, resolution, and temporal compatibility
  when they affect the measured construct;
- report per-class or subgroup performance when class-specific claims matter;
- do not require cross-region transfer experiments when no transfer claim is
  made.

## CRS And Measurement

- Verify CRS compatibility before overlays and spatial joins.
- Use projected, geodesic, or network distance appropriate to the measurement;
  do not treat longitude/latitude degrees as planar distance.
- Use an equal-area method when area preservation is required.
- Document projection choices when they can affect distance, area, direction,
  neighborhood, or visual interpretation.

## Reporting

Report:

1. unit and scale of analysis and inference;
2. why the chosen method answers the question;
3. the simple baseline and what the spatial extension adds;
4. diagnostics actually triggered and their consequences;
5. checks considered but deferred or marked `N/A`, with one-line reasons;
6. boundaries on transfer, mechanism, or causal interpretation only where they
   change how the result should be read.

Skipping an inapplicable spatial check is a valid methodological decision, not
an omission to apologize for.
