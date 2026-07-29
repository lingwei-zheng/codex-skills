# Domain Adapters

Use this card after a domain brief when the user works in one of these familiar research areas. Do not use it as a substitute for current sources; it only adds field-specific evidence norms and common failure modes.

## How To Use

1. Pick only the relevant adapter.
2. Translate the user's rough idea into that domain's evidence norms.
3. Add at least one domain-specific reviewer objection to the Good Question Card.
4. If the claim depends on current literature, mark it as source-backed, inference, or unknown.
5. Calibrate expectations with `../../shared/research-calibration.md`. Treat
   incremental and regional contributions as valid when their added value and
   venue fit are explicit.

## Ecology

**Common weak forms:** descriptive pattern hunting with no cumulative,
management, measurement, or local-decision value; relying on single-site
newness alone; "biodiversity is important" without a useful question.

**Stronger question forms:**
- Which mechanism best explains the pattern across environmental gradients, disturbance, or management regimes?
- Under what boundary conditions does a general ecological relationship fail?
- What management or forecasting decision would change if the answer were known?

**Evidence norms:** replication across space/time, scale matching, natural-history plausibility, confound control, uncertainty in detection or sampling.

**Reviewer objections:** site-specific story, unmeasured environmental gradient, weak causal identification, result is interesting but not generalizable.

## Remote Sensing

**Common weak forms:** treating a new region as self-justifying without naming
replication, transferability, underrepresentation, measurement, or decision
value; benchmark improvement without ground-truth value; visual products
without an evidentiary use.

**Stronger question forms:**
- What uncertainty does the sensor/model resolve that simpler baselines cannot?
- Where does transfer fail across regions, seasons, sensors, or management contexts?
- How much uncertainty is acceptable for the intended decision?

**Evidence norms:** ground truth quality, spatial/temporal scale mismatch,
baseline comparison, domain shift, uncertainty calibration, and leakage checks.
For a first draft, prioritize leakage, one simple baseline, and the single
scale/validation issue most likely to change the result; defer exhaustive
robustness work.

**Reviewer objections:** weak validation data, no simple baseline, model learns site artifacts, accuracy gain does not change any decision.

## Machine Learning And AI4Science

**Common weak forms:** "use foundation model/LLM/transformer for X", leaderboard chasing, method-first novelty.

**Stronger question forms:**
- What scientific uncertainty or failure mode does the model diagnose?
- Which simpler model or mechanistic baseline must the method beat to matter?
- What would make improved prediction scientifically informative rather than only operationally useful?

**Evidence norms:** leakage control, baseline strength, uncertainty,
interpretability, and out-of-distribution or ablation tests when they address
the paper's main claim. Do not require the entire suite for an exploratory or
first-draft analysis.

**Reviewer objections:** benchmark is disconnected from the scientific question, data leakage, insufficient baseline, no insight beyond prediction.

## Social Science

**Common weak forms:** broad "impact of X on Y", survey-only description, vague policy relevance.

**Stronger question forms:**
- Which mechanism links X to Y, and what rival explanation could produce the same pattern?
- What comparison or design makes the claim credible?
- Which decision-maker or population would update their belief?

**Evidence norms:** construct validity, causal identification, sampling frame, measurement invariance, ethics, external validity.

**Reviewer objections:** unclear construct, selection bias, weak identification, overgeneralization beyond the sample.

## Biomedicine

**Common weak forms:** biomarker fishing, therapeutic promise without mechanism, small cohort association as a conclusion.

**Stronger question forms:**
- Which biological mechanism or clinical decision could this evidence change?
- What comparator, endpoint, or perturbation would distinguish mechanism from correlation?
- What negative result would stop translation?

**Evidence norms:** endpoint validity, cohort size and bias, preclinical-to-clinical translation, controls, reproducibility, safety or ethical constraints.

**Reviewer objections:** underpowered cohort, confounding, endpoint is indirect, effect is not actionable, mechanism is post hoc.
