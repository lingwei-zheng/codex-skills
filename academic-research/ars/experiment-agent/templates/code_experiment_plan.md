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

- **Primary metric**: [what to look at first]
- **Success threshold**: [e.g., "accuracy > 0.90", "p < .05"]
- **Comparison**: [baseline, previous run, theoretical expectation]

## Rigor Budget

### Immediate Checks

1. [fatal validity risk or key diagnostic]
2. [optional targeted check]

### Deferred Checks

| Check | Trigger | Estimated Cost | Decision It Could Change |
|---|---|---|---|
| [check] | [journal/reviewer/risk signal] | [time/compute] | [interpretation or claim] |
