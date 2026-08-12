# Interaction and Moderation Track

Use this R-only track when a manuscript result concerns an interaction,
moderation, conditional association, heterogeneous slope, or a predictor whose
relationship with the outcome changes across another variable. Use the
`interactions` package as the sole interaction-analysis plotting interface.
Its output is a `ggplot2` object and may be styled with the shared R theme and
exported through the standard R workflow.

## Scientific Role

An interaction plot is often the primary evidence for a moderation claim, not
an optional diagnostic. The default main-text figure shows the model-implied
outcome across the focal predictor at meaningful moderator values, with
uncertainty when the fitted model and package route support it.

Do not replace this with only an interaction coefficient or coefficient forest
plot. A coefficient can establish that an interaction term differs from zero,
but it usually does not communicate the direction, magnitude, or substantive
conditions of the moderation.

## Function Router

| Variable structure or claim | Primary function | Default display |
|---|---|---|
| Continuous predictor x continuous moderator | `interact_plot()` | Predicted outcome lines at meaningful moderator values |
| Continuous predictor x categorical moderator | `interact_plot()` | One predicted line per moderator level |
| Categorical predictor x categorical moderator | `cat_plot()` | Point-range or ordered point-line plot; avoid bars by default |
| Three-way interaction | `interact_plot(..., mod2 = ...)` | Facet by the second moderator; keep line count low |
| Conditional slopes are the result | `sim_slopes()` plus `plot()` when useful | Slope estimates and intervals at selected moderator values |
| Threshold or region of significance is the result | `johnson_neyman()` | Conditional slope across the observed moderator range |

Do not call `probe_interaction()` by default. It calls plotting and simple-slope
work separately and may refit models repeatedly. Use only the component needed
for the paper's current claim, especially for expensive mixed or Bayesian
models.

## Required Decisions

Before plotting, resolve these fields from the model, analysis plan, or user:

1. Focal predictor (`pred`) and moderator (`modx`). Do not swap them merely
   because a default plot looks cleaner.
2. Moderator values. Prefer theory-, policy-, or measurement-relevant values.
3. Prediction scale. For GLMs, default to the response scale unless the link
   scale is itself the scientific object.
4. Other-covariate handling. Record whether non-focal covariates are centered
   or fixed through `at`; do not leave this implicit in the legend.
5. Mixed-model level. For `lme4` models, use the fixed-effect interaction as the
   default population-level display. Do not imply that subject-, site-, or
   region-specific random effects are shown.
6. Uncertainty. Request intervals where supported. If the selected model route
   cannot provide them, disclose that limitation and pair the main plot with
   `sim_slopes()` uncertainty when appropriate; do not fabricate ribbons.
7. Observed support. Keep plotted moderator values inside the observed range
   and flag sparse combinations or extrapolated predictor regions.

## Moderator Values

For a continuous moderator:

- use substantively meaningful cut points when available;
- otherwise use mean - 1 SD, mean, and mean + 1 SD, which is the
  `interactions` convention;
- use quantile-based values when the distribution is strongly skewed or the
  mean +/- SD values have poor empirical support;
- do not default to minimum and maximum values merely because they maximize
  visual separation;
- preserve original units in the visible labels even when variables were
  centered or standardized for modelling.

For a categorical moderator, show all substantively relevant levels. If there
are many levels, select a justified subset or facet rather than producing an
unreadable legend.

## Plot Patterns

### Continuous by continuous

```r
library(interactions)

p <- interact_plot(
  model,
  pred = focal_predictor,
  modx = moderator,
  modx.values = c(low_value, central_value, high_value),
  data = analysis_data,
  interval = TRUE,
  outcome.scale = "response",
  plot.points = FALSE,
  vary.lty = TRUE
)
```

Use direct, substantive labels for moderator values. Add observed points only
when they clarify support and remain readable; use transparency and jitter when
needed.

### Continuous by categorical

```r
p <- interact_plot(
  model,
  pred = focal_predictor,
  modx = group_variable,
  data = analysis_data,
  interval = TRUE,
  outcome.scale = "response",
  plot.points = TRUE,
  vary.lty = TRUE
)
```

Use stable colors and line types so the figure survives grayscale printing.

### Categorical by categorical

```r
p <- cat_plot(
  model,
  pred = focal_factor,
  modx = moderator_factor,
  data = analysis_data,
  geom = "point",
  interval = TRUE,
  point.shape = TRUE
)
```

Use `geom = "line"` when the focal categories are ordered and connecting them
has a defensible interpretation. Do not use a bar chart merely because the
variables are categorical.

### Three-way interaction

```r
p <- interact_plot(
  model,
  pred = focal_predictor,
  modx = first_moderator,
  mod2 = second_moderator,
  modx.values = c(low_value, high_value),
  data = analysis_data,
  interval = TRUE,
  outcome.scale = "response",
  vary.lty = TRUE
)
```

Facet by `mod2`. Prefer two well-justified first-moderator values over three or
more lines per facet unless the middle value carries a claim.

### Simple slopes

```r
slopes <- sim_slopes(
  model,
  pred = focal_predictor,
  modx = moderator,
  modx.values = c(low_value, central_value, high_value),
  data = analysis_data,
  confint = TRUE,
  johnson_neyman = FALSE
)

p_slopes <- plot(slopes)
```

Use this when the conditional slopes themselves are easier to interpret than
predicted outcomes, or as a supporting panel for the main prediction plot.

### Johnson-Neyman

```r
jn <- johnson_neyman(
  model,
  pred = focal_predictor,
  modx = moderator,
  plot = TRUE,
  mod.range = range(analysis_data[["moderator"]], na.rm = TRUE)
)

p_jn <- jn$plot
```

Use Johnson-Neyman only when the transition across moderator values is a
substantive result. Do not add it automatically to every interaction figure or
describe statistical significance as the magnitude of the moderation.

## Styling and Legend Rules

- Label the y-axis as the predicted outcome, probability, or expected count,
  not generically as `Effect`.
- Label each line with the actual moderator value and unit; low/medium/high may
  be added as interpretation, not used as the only information.
- Use ribbons or intervals with restrained opacity and keep line identities
  visible in grayscale.
- Do not encode significance through line color or hide non-significant lines.
- Keep the same focal predictor, moderator ordering, colors, and values across
  manuscript panels.
- State the model class, covariate handling, response/link scale, and interval
  level in the legend.

## Interpretation Boundaries

- Write `association differs by`, `relationship varies across`, or `is
  moderated by` according to the analysis; do not upgrade an interaction to a
  causal mechanism.
- A significant product term does not by itself show which conditional slopes
  differ meaningfully; use predictions or simple slopes to interpret it.
- A non-significant simple slope is not evidence of no difference between two
  slopes. Interpret the interaction test and conditional estimates together.
- Do not call line crossing a crossover interaction unless the estimated model,
  uncertainty, and observed support justify that description.

## Delivery Contract

Deliver:

- the fitted-model assumptions used for prediction;
- chosen moderator values and why they were chosen;
- an `interactions`-based R script;
- the plot data or slope table returned by the analysis when accessible;
- SVG, PDF, TIFF, and preview exports requested by the user;
- a QA note covering prediction scale, covariate handling, uncertainty, mixed-
  model level, observed support, and extrapolation.
