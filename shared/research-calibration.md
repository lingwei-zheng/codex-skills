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

## Reporting

For analysis planning or execution, report only:

- active calibration profile
- primary analysis
- immediate validity checks
- deferred checks
- performance contract or measured bottleneck when runtime matters
- contribution level and suitable claim strength when evaluating the study

Keep the report proportional to the current stage.
