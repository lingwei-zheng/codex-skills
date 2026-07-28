# Geospatial Figure Contract

Use this reference for static publication maps and spatial evidence figures.
This is not a full GIS processing workflow.

## Scientific Role

State which role the map serves:

- study context or sampling frame;
- spatial distribution or pattern;
- exposure, access, or outcome surface;
- model estimate or residual;
- uncertainty or sensitivity;
- comparison across time, scale, group, or scenario.

A locator map does not become evidence merely because it is visually prominent.
Maps that support a claim must expose the relevant comparison, uncertainty, and
spatial unit.

## Required Decisions

```text
Spatial claim:
Spatial unit:
Temporal unit:
Coordinate reference system:
Geographic extent:
Classification or scale:
Normalization or denominator:
Uncertainty representation:
Missing-data representation:
Comparison contract:
Source-data provenance:
```

## Validity Checks

- Confirm that the spatial unit matches the claim and interpretation.
- Check whether aggregation, zoning, or scale choices could create MAUP or
  ecological-fallacy risks.
- Account for spatial dependence when the map presents model results or
  significance.
- Do not imply individual exposure or risk from area-level values without an
  appropriate design.
- Keep legends and scales comparable across panels that invite comparison.
- Distinguish observed values, modelled estimates, predictions, residuals, and
  uncertainty.
- Show missing, suppressed, and out-of-domain values explicitly rather than
  assigning them to the lowest class.
- Avoid causal language from spatial coincidence alone.

## Cartographic Rules

- Choose a projection appropriate to extent and measurement. Do not use an
  unsuitable geographic coordinate system for distance or area comparisons.
- Use a scale bar only when distance interpretation is useful and valid for the
  projection and extent.
- Use a north arrow only when orientation is not already obvious or the map has
  been rotated.
- Keep administrative boundaries visually subordinate unless they define the
  analytic unit.
- Use sequential scales for ordered magnitude, diverging scales for meaningful
  deviations around a center, and categorical palettes for unordered classes.
- Avoid too many choropleth classes and document the classification method.
- Use insets only when they solve a geographic-context or visibility problem.
- Ensure labels, line weights, and symbols remain legible at final journal size.

## Geography Context

When relevant, also read:

- [spatial-methods.md](../../shared/field-context/spatial-methods.md) for scale,
  units, MAUP, spatial dependence, and validity;
- [environmental-health.md](../../shared/field-context/environmental-health.md)
  for exposure, vulnerability, access, and outcome boundaries;
- [geoai-domain.md](../../shared/field-context/geoai-domain.md) for geospatial
  machine-learning estimates, benchmarks, and uncertainty.

## QA

At final size, verify the projection, legend title and units, classification,
missing-data encoding, source note, panel comparability, uncertainty, and
whether the visual claim exceeds the underlying spatial evidence.
