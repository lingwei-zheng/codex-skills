# Research Calibration Protocol

This is the shared source of truth for scientific value, method complexity,
evidence standards, stopping decisions, and research-stage calibration.
Use it from question design through experiments, interpretation, writing, and
project resumption. Existing ethics, safety, approval, and verification gates
remain in force.

## Scientific Value Before Methodological Complexity

Default to:

`Scientific question -> Simplest adequate method -> Evidence -> Necessary complexity -> Scientific contribution`

Seek the minimum sufficient method, not the smallest method regardless of
validity. A basic estimator supports a mechanism claim only when the design
identifies that mechanism; simplicity cannot repair identification failure.

Before adding a model component, experimental condition, estimator, or workflow,
state briefly in the existing plan:

1. Which scientific question can the simplest current method not answer?
2. What substantive obstacle does the addition resolve?
3. Which assumptions, parameters, and validation duties does it add?
4. What scientific explanation or decision capability should improve?
5. What evidence would justify stopping this route if it adds no value?

Do not expand work for methodological completeness, sophistication, or coverage
of every possible condition. Reuse settled decisions; this justification is not
a new approval checkpoint for routine implementation.

## Progressive Method Complexity

| Level | Purpose | Reason to advance |
|---|---|---|
| M0 | Understand distributions, quality, missingness, time structure, basic associations, and the research target | A defined question needs estimation or a discriminating test |
| M1 | Use the simplest adequate estimator and small evidence test | A substantive feature prevents that method from answering the question |
| M2 | Add necessary heterogeneity, nonlinearity, temporal dependence, selection, or resource constraints | The realistic problem exposes a specific inferential deficit |
| M3 | Add targeted weighting, joint estimation, bias correction, or comparable statistical enhancement | The simpler approach cannot meet the claim's evidence needs |
| M4 | Develop advanced joint models, optimization, or a fuller inference system | A clear incremental scientific contribution justifies the extra burden |

These are decision aids, not mandatory stages or a prestige ranking. Reuse an
already justified method without reenacting earlier stages. Stop at any adequate
level. Record scientific ambition separately: a simple reliable method may
support a law across sources or mechanisms, while a complex model may answer
only a narrow question. Variables, models, repetitions, code size, and PASS counts
do not measure contribution.

## Three Layers of Evaluation

### A. Non-negotiable validity and integrity

Preserve correct data transformations and statistical formulas; align the
estimand (the target quantity) with the research goal; enforce information
visibility and prevent leakage; retain reproducible code, configuration, seeds,
and data provenance. Record failures, extreme values, and negative outcomes,
including attempted and excluded runs and their reasons.

Never change seeds, parameters, eligibility, or scenarios to obtain a favorable
result, discard inconvenient failures, present exploration as independent
confirmation, or use invalid inference to support a broader claim. A genuine
bug repair must preserve the original record and identify affected results.

### B. Claim-specific statistical evidence

Select Monte Carlo precision, uncertainty, bias/risk, robustness/sensitivity,
multiplicity controls, and numerical-failure/tail diagnostics according to the
claim and decision they support. Specify the criterion before confirmation;
label revisions and post hoc work. Existing agreed criteria remain binding
until changed through the applicable decision/approval process.

Do not require every scenario or comparison to meet one relative-MSE precision
threshold. A reliable branch may support a scoped conclusion while another is
inconclusive or invalid. Propagate a defect to every dependent claim, including
the whole study when the defect is shared. Never simply relabel a failed
mandatory criterion as optional.

### C. Scientific contribution

There is no universal minimum percentage improvement. A credible small gain can
matter through stability, cost, explanation, or scientific consequence. Compare
magnitude, uncertainty, costs, and meaning; statistical significance is neither
scientific importance nor sufficient evidence of validity. Greater improvement
is attractive with other conditions equal, but cannot replace explanation.
Do not increase simulation indefinitely to obtain significance.

Execution checks (exit status, readable files, schema) establish operational
completion, not hypothesis support. Reproducibility status establishes what was
rerun and verified, not that a hypothesis is true or a contribution is large.

## Scientific Decisions and Stopping

For each question, distinguish **supported**, **not supported**, and
**insufficient evidence**. All are legitimate research outcomes. Explain the
direction and precision: a nonsignificant test alone does not demonstrate no
effect; an informative null, contradiction, or equivalence claim needs evidence
appropriate to that claim.

Stop an added technical route when it provides no new explanatory value, reaches
its authorized resource bound, or exposes an identification/information limit
that further tuning cannot resolve. Diagnose implementation bugs with bounded
checks; distinguish them from scientific limits. Record the boundary and route
status instead of searching indefinitely for a passing configuration.

Once sufficient evidence supports a bounded conclusion, proceed to authorized
interpretation, writing, or the next RQ without requiring all auxiliary analyses
to pass. Preserve unresolved findings, required reporting, and all applicable
approvals; a narrower conclusion is not permission to bypass an integrity gate.

Use a scientific question or substantive obstacle as the work unit. Carry the
decision and stopping reason in existing project records, not a new parallel
ledger. For material changes to goals, estimands, DGPs, acceptance principles,
or resource commitments, apply the existing
[execution and approval scope](../academic-research/references/execution-and-approval.md#scientific-decision-units).

### Typical decisions

| Situation | Proportionate decision |
|---|---|
| A 0.5% improvement is reliable, stable in relevant conditions, and cheap | Assess its scientific/use value and uncertainty; it may support a contribution. Neither 0.5% nor any other percentage is a universal acceptance threshold |
| A complex estimator is unstable while a simpler estimator answers the scoped question | Check correctness and retain all failed/extreme runs; bound or stop the complex route when justified, report its domain limit, and use the valid simpler result |
| Sources have unequal sample sizes | Clarify populations, units, coverage, matching, and source-specific estimands; retain appropriate denominators. Do not truncate to equal counts or add weighting merely for symmetry; a pooling/transport claim needs its own justification |
| Evidence contradicts the scientific hypothesis | Report that finding and its implications; do not change seeds or the primary outcome to obtain support. If uncertainty is wide instead, classify the result as insufficient rather than proving absence |

## Default Profile

When the user is developing an analysis or manuscript and does not specify a
stage, use:

```yaml
research_stage: first-draft
rigor_profile: proportionate
contribution_profile: incremental-allowed
compute_profile: balanced
```

State a different profile only when the request or evidence requires it.

## Research Stage

| Stage | Purpose | Default behavior |
|---|---|---|
| `exploratory` | Learn data shape and test feasibility | Small informative analysis with the same integrity floor; mark exploration |
| `first-draft` | Establish the paper's main result | Main specification, simple baseline, and claim-triggered validity checks |
| `submission` | Support claims at the target venue | Add risk-triggered robustness, reporting, and reproducibility checks |
| `review-response` | Answer known reviewer concerns | Run only checks that resolve the cited concern or a newly exposed validity risk |

Do not apply formal peer-review or systematic-review requirements to ordinary
first-draft analysis.

## Proportionate Rigor

### First-draft default

Prioritize:

1. data and variable integrity
2. a reproducible primary analysis
3. one defensible simple baseline or reference specification
4. the single diagnostic most likely to invalidate the main result
5. a small number of additional checks triggered by named risks; start with one
   or two when sufficient, never cap checks essential to validity

Put other plausible checks in a short `Deferred checks` ledger with:

- check
- trigger for running it
- likely cost
- decision it could change

Do not run a robustness checklist merely because the checks are conventional.

### Claim-triggered diagnostics

Diagnostics are a menu, not a completeness score. Run a diagnostic only when
its result could change a central claim, model choice, interpretation, or
decision at the current research stage. Record an inapplicable check as `N/A`
with a short reason; omission is not a defect by itself.

For spatial research, use these common triggers:

| Check | Run when | Usually defer or mark N/A when |
|---|---|---|
| Residual spatial dependence | A fitted model relies on residual independence and plausible spatial dependence could alter inference | The task is descriptive, the method does not rely on independence, or no meaningful neighborhood structure exists |
| MAUP or alternative scale | Aggregation is researcher-chosen and the headline magnitude, ranking, or inference could change across units | Units are fixed by the data-generating process or the claim is explicitly single-scale |
| Alternative spatial weights | The central clustering or spatial-model result materially depends on the definition of neighborhood | The weights do not enter the claim or are fixed by a defensible physical/network process |
| Spatial cross-validation | Prediction uses spatially structured data and nearby train/test observations could inflate performance | Prediction is not spatial, leakage is impossible by design, or the target is within-sample description |
| GWR/MGWR | Spatially varying relationships are themselves part of the research question and a global baseline is inadequate | Coordinates are incidental or a simpler global/descriptive model answers the question |
| Boundary or transfer checks | Edge effects or geographic transfer are part of the claim | The analysis is interior-only or makes no transfer claim |

When unsure about a costly spatial check, report its trigger, likely cost,
simpler alternative, and recommendation before running it. Prefer the lightest
analysis that answers the question.

### Immediate checks

Run a check now when failure could reverse or invalidate the main result,
including:

- corrupted joins, coding errors, duplicate leakage, or outcome leakage
- invalid spatial or temporal validation
- severe model non-convergence or assumption failure
- central causal-identification failure
- a scale, MAUP, or ecological-inference problem that directly determines the
  claim
- a high-stakes clinical, safety, legal, or policy decision

### Deferred checks

Normally defer exhaustive specification grids, every plausible control set,
multiple arbitrary bandwidths or spatial units, repeated alternative outcomes,
and broad subgroup sweeps until:

- the primary result is stable enough to justify the cost
- the target journal requires them
- a reviewer raises the issue
- one check diagnoses a concrete risk rather than adding ceremonial volume

## Contribution Forms

Evaluate contribution separately from novelty.

The forms below describe kinds of contribution, not a scoring scale
or a journal-tier ceiling. Assess question importance, distinctive evidence,
result strength and audience fit separately, using the intended journal's
actual criteria and relevant published work.

| Contribution form | Valid use |
|---|---|
| Direct replication | Reproducibility, cumulative evidence, benchmark confirmation |
| Contextual or regional extension | New population, place, policy setting, or transferability evidence |
| Incremental improvement | Better measurement, data coverage, implementation, estimation, or modest method gain |
| Mechanism or boundary contribution | Distinguishes explanations or identifies where prior findings hold |
| Theory or method advance | Revises a framework or materially changes inferential capability |

All five forms can support publishable research. Judge:

- what becomes more credible, measurable, transferable, or useful
- who benefits from the added evidence
- whether the contribution is stated honestly
- whether the target venue rewards that contribution magnitude

Do not block or downgrade a study merely for being incremental or regional.
Identify the strongest credible route; narrow a claim, repair evidence, or
retarget only for a specific mismatch. Keep current submission readiness and
evidence-dependent development potential separate.

Changing only the study location is weak framing, but not automatically weak
research. It can be valuable when it adds underrepresented evidence, local
policy relevance, independent replication, data improvement, transferability
testing, or cumulative comparison.

Novelty and gap statements are bounded by the search actually performed.
Prefer `within the databases, dates, and terms searched, we found...` over
universal claims that no prior work exists.

## Severity Calibration

Calibrate criticism to consequence and field norms:

- `block`: the problem invalidates or reverses a central result or makes the
  claimed inference untenable at the current decision stage;
- `repair`: the problem can materially change interpretation, credibility, or
  venue fit but is plausibly fixable;
- `note`: a reporting preference, optional extension, or non-triggered
  convention that does not threaten the main result.

The absence of a conventional analysis is not automatically a defect. First
state the assumption or claim that would require it. Do not manufacture a
critical issue to satisfy an issue count.

## Compute Profiles

| Profile | Use | Resource behavior |
|---|---|---|
| `quick` | Debugging and pilot runs | Small sample, short iterations, minimal parallel overhead |
| `balanced` | Default analysis | Use available parallelism while preserving system responsiveness |
| `max-throughput` | Explicit speed priority | Use most suitable CPU/GPU capacity with thermal and memory safeguards |

High utilization is useful only when it improves throughput. Diagnose CPU,
GPU, memory, and I/O bottlenecks before increasing workers.

## Performance Contract

Before a long analysis:

1. detect available CPU cores, memory, GPU, and relevant runtime limits
2. run a 1-5% pilot or one representative unit when feasible
3. measure elapsed time, throughput, peak memory, and CPU/GPU utilization
4. estimate full-run time and likely bottleneck
5. choose vectorization, batching, worker count, caching, checkpointing, and
   output strategy
6. verify optimized and reference implementations agree on a small sample

Monitor:

- elapsed time and ETA
- units processed per minute
- CPU/GPU utilization
- memory pressure
- disk or network I/O wait
- output growth and checkpoint health

Low utilization plus poor throughput is a performance anomaly. Investigate
serial loops, repeated reads, unnecessary copies, tiny tasks, worker
oversubscription, and missing vectorization.

## Scientific Invariants

Performance optimization may change implementation, chunking, scheduling, file
formats, and worker counts. It must not silently change:

- sample inclusion
- variable definitions
- model specification
- random seed policy
- numerical precision that affects conclusions
- convergence criteria
- statistical or scientific meaning

When equivalence cannot be guaranteed, treat the optimized run as a new
specification and label it.

## Causal Language Economy

Preserve the distinction between association and causation without repeating
the distinction in every sentence.

- `X was associated with Y` is already a non-causal claim. Do not routinely
  weaken it to `an exploratory association`, `an observational association`,
  or append a separate no-causality disclaimer.
- Use `observational` when naming the study design, contrasting designs, or
  when the design class materially changes interpretation.
- Use `exploratory` when distinguishing post hoc or non-preregistered analyses
  from confirmatory analyses, not as a generic synonym for cautious.
- State a central causal limitation once in Methods, Discussion, or
  Limitations when it matters. Repeat it only where omission would make a
  specific claim misleading.
- Prefer accurate verb selection over qualifier stacking: `associated with`,
  `correlated with`, `predicted`, `estimated`, or `co-occurred with` as the
  evidence warrants.

One sufficient boundary signal is usually better than a design label, hedge,
and disclaimer stacked on the same claim.

## Evidence And Revision Economy

- Review high-impact claims, primary figures/tables, and load-bearing method
  choices first. Sample lower-impact material rather than auditing every
  sentence at equal depth.
- Reuse a verified citation or evidence ledger when its source identity and
  scope remain unchanged. Re-verify only changed, decisive, stale, or disputed
  claims.
- Accept a user-specified PDF `read_scope` such as pages, sections, figures, or
  appendices. Disclose unread material; do not imply full-document review.
- Revise the smallest coherent unit by default. Rewrite a whole section only
  when its argument, evidence order, or structure is genuinely unsound.
- After revision, compare central claims before and after. Flag material claim
  drift for author review; do not turn every wording change into a gate.

## Reporting

For analysis planning or execution, prioritize:

- the scientific question actually answered and its supported scope
- reliable findings, exploratory findings, and unresolved evidence
- what added complexity bought, or why the simpler method suffices
- limits needing more evidence versus boundaries that can be reported
- the single most valuable next authorized research action, or why to stop

Include the active profile, immediate/deferred checks, and measured resource
budget when they affect that decision. For simulation design or estimator
validation, read the on-demand
[simulation and method validation guide](../academic-research/ars/experiment-agent/references/simulation-method-validation.md).

Keep the report proportional to the current stage.
