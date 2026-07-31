# Research Calibration Protocol

Use this shared protocol to calibrate research rigor, computing effort, and
contribution expectations. It prevents submission-stage standards from
overloading exploratory analysis or a first manuscript draft.

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
| `exploratory` | Learn data shape and test feasibility | Fast primary analysis; exclude only fatal errors |
| `first-draft` | Establish the paper's main result | Main specification, one baseline, key diagnostic, and 0-2 targeted checks |
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
5. at most two additional checks triggered by a named risk

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

## Contribution Ladder

Evaluate contribution separately from novelty.

| Level | Contribution form | Valid use |
|---|---|---|
| 1 | Direct replication | Reproducibility, cumulative evidence, benchmark confirmation |
| 2 | Contextual or regional extension | New population, place, policy setting, or transferability evidence |
| 3 | Incremental improvement | Better measurement, data coverage, implementation, estimation, or modest method gain |
| 4 | Mechanism or boundary contribution | Distinguishes explanations or identifies where prior findings hold |
| 5 | Theory or method advance | Revises a framework or materially changes inferential capability |

All five levels can support publishable research. Judge:

- what becomes more credible, measurable, transferable, or useful
- who benefits from the added evidence
- whether the contribution is stated honestly
- whether the target venue rewards that contribution magnitude

Do not block a study for being incremental. Recommend a narrower claim, a more
appropriate venue, or a specific value-adding repair when needed.

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

For analysis planning or execution, report only:

- active calibration profile
- primary analysis
- immediate validity checks
- deferred checks
- performance contract or measured bottleneck when runtime matters
- contribution level and suitable claim strength when evaluating the study

Keep the report proportional to the current stage.
