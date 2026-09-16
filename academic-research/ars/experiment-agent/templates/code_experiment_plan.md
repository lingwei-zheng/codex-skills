# Code Experiment Plan

## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: plan
- Origin Date: [ISO 8601]
- Verification Status: UNVERIFIED
- Version Label: code_plan_v1

## Experiment Overview

- **Title**: [descriptive name]
- **Objective**: [what this experiment tests]
- **Hypothesis**: [expected outcome, if any]
- **Type**: [training | analysis | etl | simulation | generic]
- **Research stage**: [exploratory | first-draft | submission | review-response]
- **Rigor profile**: [proportionate | comprehensive]
- **Compute profile**: [quick | balanced | max-throughput]

## Argument And Comparison

- **Claim / experiment IDs**: [reuse C# / E#]
- **Advantage hypothesis**: [candidate, not an observed result]
- **Argument job**: [establish | explain | demonstrate | distinguish | bound]
- **Fair arena**: [task, population/scale, comparator, resource budget]
- **Supports / narrows / defeats**: [observable outcomes for this claim]
- **Intended presentation**: [main text | supplement | internal; provisional]

## Setup

- **Language/Framework**: [e.g., Python 3.11, PyTorch 2.x]
- **Entry Command**: `[exact command to run]`
- **Working Directory**: `[path]`
- **Dependencies**: [list or "see requirements.txt"]
- **Environment**: [OS, GPU, memory requirements if relevant]

## Inputs

| Input | Path | Description |
|-------|------|-------------|
| [name] | [path] | [what it is] |

## Expected Outputs

| Output | Path | Format | Success Criterion |
|--------|------|--------|------------------|
| [name] | [path] | [CSV/JSON/model/figure] | [e.g., "file exists and > 0 bytes"] |

## Monitoring Configuration

- **Timeout**: [duration, default 30 min]
- **Monitor files**: [paths to watch for progress]
- **Experiment type override**: [if auto-detection should be overridden]
- **Metric file**: [path to loss/metric log, if applicable]
- **Metric key**: [column/field name, if applicable]

## Performance Contract

- **Pilot scope**: [1-5% sample, one tile/fold/file, or not needed]
- **Available resources**: [CPU cores, RAM, GPU]
- **Expected bottleneck**: [CPU | GPU | memory | disk I/O | network | serial dependency]
- **Worker/batch strategy**: [n_jobs/workers, chunk size, batch size]
- **Caching/checkpointing**: [what is reused or recoverable]
- **Pilot throughput**: [units/time]
- **Estimated full runtime**: [duration]
- **Utilization target**: [appropriate range and device]
- **Equivalence check**: [how optimized and reference outputs will be compared]

## Analysis Plan

- **Primary metric and purpose**: [prespecified metric and decision relevance]
- **Secondary / exploratory metrics**: [distinguish planned from post hoc]
- **Scientific criterion**: [meaningful effect, precision, performance or cost,
  with uncertainty and an applicable statistical test; not p-value alone]
- **Comparison**: [fair baseline and matched conditions]
- **Configuration / input version**: [existing config and data version, or unknown]

## Planned Execution And Evidence

| Experiment ID / unit | Planned measurement | Execution status | Skip reason, if not run | Result locator and version |
|---|---|---|---|---|
| [E#] | [measurement] | planned | [if deferred] | pending |

Update from actual runs, never expected values. Preserve raw results and required
controls even when a unit will not appear in the paper. Execution success in
Expected Outputs is distinct from the scientific criterion above.

## Rigor Budget

### Immediate Checks

1. [fatal validity risk or key diagnostic]
2. [optional targeted check]

### Deferred Checks

| Check | Trigger | Estimated Cost | Decision It Could Change |
|---|---|---|---|
| [check] | [journal/reviewer/risk signal] | [time/compute] | [interpretation or claim] |
