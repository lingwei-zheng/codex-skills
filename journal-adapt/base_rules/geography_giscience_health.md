# Geography, GIScience, and Health Geography Writing Rules

Use these rules as the default Priority 4 static base layer when the manuscript is in geography, human geography, GIScience, GeoAI, remote sensing, spatial data science, health geography, environmental health, urban studies, or spatial epidemiology.

These rules are lower priority than the target-journal corpus and any reviewed secondary corpus or user/lab exemplars. They apply only when corpus-derived rules are absent, weak, or underspecified.

## Core Argument Logic

1. Anchor the paper in a spatial, geographic, or place-based problem before introducing the method.
2. State the substantive geographic question before the technical contribution.
3. Make clear what is spatial about the problem: scale, place, neighborhood, mobility, distance, accessibility, exposure, network position, boundary, spatial interaction, or spatial dependence.
4. Avoid presenting spatial methods as generic machine-learning or statistical tools. Explain why spatial structure matters for the claim.
5. Tie each method choice to a geographic inferential need, not only to predictive performance.

## Introduction

1. Open with a concrete geographic, social, environmental, or public-health problem rather than a generic technology gap.
2. Move from substantive problem to spatial mechanism, then to the gap in current evidence or method.
3. Position the contribution in relation to both domain literature and spatial-method literature when both are relevant.
4. Avoid vague contribution claims such as "provides new insights" unless the insight is named.
5. If the paper is method-oriented, state the empirical or geographic setting early enough that the method does not read as context-free.

## Literature Review and Positioning

1. Organize literature by conceptual problem, spatial mechanism, data limitation, or inferential limitation, not by a flat list of authors.
2. Distinguish domain debates from technical limitations.
3. Make the target gap explicit: measurement gap, scale mismatch, spatial dependence, temporal dynamics, exposure misclassification, uncertainty, representativeness, transferability, interpretability, or causal identification.
4. Avoid claiming novelty only from combining a place, dataset, and model. Explain the knowledge gap that this combination resolves.
5. For interdisciplinary papers, define which audience each body of literature serves.

## Methods and Data

1. Describe the study area, units of analysis, temporal scope, data sources, inclusion criteria, and spatial resolution before model details when they affect interpretation.
2. Report coordinate reference systems, spatial joins, buffers, areal units, aggregation choices, and boundary definitions when relevant.
3. Explain scale choices and modifiable areal unit risks when they can affect results.
4. State how missing data, geocoding uncertainty, sampling bias, sensor bias, and administrative boundary changes are handled.
5. Separate data construction from model estimation. Do not bury key spatial preprocessing steps inside implementation prose.
6. For GeoAI or remote sensing, connect architecture, features, labels, spatial splits, and evaluation design to spatial generalization.
7. For health geography, distinguish exposure, outcome, confounder, mediator, and contextual variable roles when applicable.

## Results

1. Lead each result paragraph with the geographic or substantive finding, then provide supporting metrics or map evidence.
2. Explain spatial patterns using precise spatial language: clustering, gradients, hotspots, accessibility, centrality, segregation, spillover, spatial heterogeneity, or place-specific effects.
3. Do not overinterpret maps. Separate visual pattern description from causal or mechanism claims.
4. When reporting model performance, include spatial transferability, robustness across places, or out-of-region performance when relevant.
5. Discuss uncertainty in mapped or spatially predicted results.
6. Avoid treating statistically significant spatial coefficients as self-explanatory; interpret their geographic meaning.

## Discussion

1. Return to the geographic problem and explain what the paper changes about understanding, measurement, policy, or method.
2. Separate substantive implications from methodological implications.
3. Keep policy claims proportional to the design. Do not make causal recommendations from descriptive or predictive evidence unless the identification strategy supports them.
4. Discuss generalizability across places, scales, populations, periods, and data regimes.
5. Name limitations that are spatially meaningful: boundary effects, scale dependence, unobserved mobility, ecological inference, sampling coverage, spatial autocorrelation, or transferability.

## Language Register

1. Prefer concrete spatial verbs and nouns over generic academic phrasing.
2. Use "place", "scale", "spatial heterogeneity", "exposure", "accessibility", "neighborhood", "mobility", and related terms only when analytically justified.
3. Avoid empty transitions and AI-like framing, including "in today's rapidly changing world", "delves into", "sheds light on", and "plays a crucial role".
4. Avoid inflated novelty language. Use specific contribution language: measures, identifies, estimates, compares, maps, evaluates, diagnoses, explains, or validates.
5. Preserve author-defined terminology, citation keys, equations, labels, variable names, and numerical claims exactly.

## Reviewer-Risk Checks

Before revision is accepted, check whether the revised section answers:

1. What is the geographic or spatial object of inquiry?
2. Why is the selected scale or spatial unit defensible?
3. What spatial bias, uncertainty, or dependence could affect the claim?
4. Does the evidence support the strength of the wording?
5. Are method claims separated from substantive claims?
6. Would a domain reviewer and a methods reviewer both understand the contribution?

