# Geography Conceptual Figure Patterns

Use these patterns to choose a defensible structure for geography, human
geography, GIScience, GeoAI, environmental health, and health geography
conceptual figures. They are starting structures, not theories. Use only the
constructs and relationships supported by the study.

## Pattern Selection

### Place-context pathway

Use for multilevel human or health geography questions.

`Place context -> exposure/opportunity -> individual or household process -> outcome`

Keep area-level and individual-level constructs visually distinct. Show
cross-level relationships explicitly and avoid ecological inference unless the
design supports it.

### Exposure-vulnerability-access-outcome

Use for environmental health, climate risk, service accessibility, or spatial
inequality.

Keep four roles separate:

- exposure or hazard
- susceptibility or vulnerability
- access, behavior, or adaptive capacity
- health, social, or policy outcome

Do not collapse vulnerability into exposure or treat modeled exposure as an
observed health effect.

### Mobility and activity space

Use when residential location is insufficient.

Represent origins, destinations, routes, durations, timing, and contextual
exposures separately. Distinguish movement observation from inferred activity
purpose and distinguish static neighborhood effects from mobile exposure.

### Spatial process and causal process

Use parallel lanes when both matter:

- spatial lane: proximity, connectivity, diffusion, clustering,
  non-stationarity, or spillover
- causal lane: treatment, mediator, confounder, moderator, or outcome

Spatial adjacency is not automatically a causal arrow. Spatial dependence may
be a data-generating property, model assumption, or substantive mechanism; label
which one applies.

### Multiscale mechanism

Use nested or aligned layers for individual, neighborhood, city/region, and
policy scales. Attach the measurement unit and temporal window to each layer.

Show aggregation or cross-level influence explicitly. Do not imply that a
relationship is invariant across zoning systems, resolutions, or time windows.

### GIScience inference pipeline

Use for data and methodological framework figures:

`Phenomenon -> observation/sensing -> representation -> preprocessing ->
model/analysis -> validation -> inference/decision`

Keep the real-world phenomenon separate from its spatial representation.
Identify coordinate reference, spatial/temporal resolution, sampling,
uncertainty, validation geography, and transfer geography when they affect the
claim.

### GeoAI learning and transfer

Use separate regions for:

- source data and labels
- representation or feature learning
- spatial validation
- transfer domain or deployment geography
- uncertainty and failure checks

Do not let a conventional random split visually stand in for spatial
generalization. Show spatial blocking, leave-location-out validation, or
cross-region transfer only when actually used.

### Policy intervention pathway

Use for planning, accessibility, environmental justice, or health impact work:

`Intervention -> environmental/service change -> distribution of exposure or
access -> behavioral/physiological response -> outcome -> equity consequence`

Mark the counterfactual or comparison condition. Separate intended mechanism,
measured intermediate outcome, and projected downstream impact.

## Mandatory Geography Checks

Before approving the semantic graph, ask:

1. What are the spatial unit, support, extent, resolution, and temporal window?
2. Does any arrow cross individual and aggregate levels?
3. Could MAUP, ecological fallacy, spatial dependence, or temporal mismatch
   change the interpretation?
4. Is a mapped or predicted quantity being mistaken for an observed mechanism?
5. Are proximity, accessibility, exposure, and interaction being treated as
   distinct constructs?
6. Does transfer to another place or scale require a boundary or uncertainty
   marker?
7. Does the figure distinguish association, mechanism, and causal identification?

Put unresolved answers in the issue ledger rather than hiding them through
visual simplification.

## Visual Encodings

- Use nested containers for scale and administrative hierarchy.
- Use lanes for actors, evidence sources, or temporal stages.
- Use solid arrows for approved directional relations and clearly differentiated
  non-arrow connectors for association or co-membership.
- Use boundaries or halos for context, not as causal entities.
- Use repeated small multiples when mechanisms differ by place or scale.
- Use uncertainty markers only when their meaning is defined in the legend.
- Keep maps as evidence-bearing panels; do not add decorative maps merely to
  signal that the study is geographic.
