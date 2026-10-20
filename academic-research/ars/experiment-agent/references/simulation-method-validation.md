# Simulation and Method Validation

Read for simulation design, estimator comparisons, or method validation.
Apply [research calibration](../../../../shared/research-calibration.md) as the
governing methodology; this reference supplies operational details, not extra
stages or universal acceptance thresholds.

## Minimal Decision Plan

Reuse the existing experiment plan/configuration. Identify the scientific aim,
estimand and unit/population, data-generating process (DGP), methods including a
simple valid reference, and performance measures that answer the aim. Distinguish
truth available to the simulator from information available to each estimator.
Name the current complexity level and the obstacle an extension would resolve.

Start with a small informative design, then add conditions that distinguish
mechanisms or define a relevant boundary. Avoid a full factorial grid solely for
completeness. Specify the seed policy, scientific decision, resource ceiling,
and stopping rule before a long run. Pilot tuning is exploration; if used to
select a method or condition, confirm with genuinely held-out runs/data under
the declared design, or retain the exploratory label.

## Correctness Before Scale

Check formulas and targets with analytically tractable cases or a trusted small
reference when available. Check joins, units, missingness, information timing,
and leakage. Preserve the full attempt log: condition, seed, input/code version,
estimate, uncertainty, convergence, failure reason, time, and relevant resource
cost. A run failure is a result to diagnose, not a license to drop that replicate.

Report failure frequencies and tail behavior where relevant to the claim.
Conditional-on-success performance needs its denominator and failure selection
disclosed; it does not establish unconditional superiority. Keep scientifically
meaningful extreme values. Bounded bug repair may be appropriate; changes to the
estimator or DGP constitute a new specification, not mere implementation repair.
Do not automatically restart crashed experiments; use existing approval rules.

## Monte Carlo Uncertainty and Effort

Separate sampling uncertainty of a study estimate from Monte Carlo uncertainty
of the simulation's performance summary. For independent simulation replicates,
MCSE of a mean summary is its replicate SD divided by sqrt(R); for an estimated
coverage/failure proportion p, the usual MCSE is sqrt(p(1-p)/R). At boundary
counts, use suitable interval reasoning rather than treating zero observed
failures as zero risk. Dependent replicates need a dependence-aware calculation.

For paired methods on common simulated datasets, estimate uncertainty of the
within-replicate contrast, retaining covariance. MSE and relative-MSE ratios need
uncertainty appropriate to their functional form. Near-zero denominators can
make relative precision misleading; use justified absolute or decision-scale
precision. Never assign the same relative precision target to every comparison.

Choose additional runs only when their expected precision could change the
scientific conclusion. Use a bounded, declared allocation/stopping policy; if
sequential monitoring affects inference, account for it or separate pilot and
confirmation. At the budget limit, report remaining uncertainty or narrow the
claim. Do not change seeds, conditions, or stopping rules to chase significance.

## Sources with Unequal Sample Sizes

Identify the population, observation unit, time coverage, eligibility, repeated
measurements/clusters, and usable denominator in each source. Distinguish
unlinked source counts from the matched analytic cohort and effective sample
size. Equality of counts is not a general validity condition.

For a pooling, transport, or comparative claim, assess target compatibility,
selection, dependence, and precision. Weighting or joint modeling is warranted
only when it solves an identified target/selection problem and its assumptions
are defensible. Otherwise retain source-specific estimates and scope the claim.
Never downsample simply to make table counts match.

## Decision Handoff

Return the question, supported scope and evidence status, unresolved branch,
value gained from complexity, and next action or stopping reason. Distinguish
operational success, reproducibility verification, and scientific support.
An auxiliary method's instability need not prevent writing from independently
valid evidence; a shared DGP or leakage defect affects all dependent results.

Technical reference for simulation design and Monte Carlo uncertainty:
[Morris, White and Crowther (2019), Using simulation studies to evaluate statistical methods](https://doi.org/10.1002/sim.8086).
