# Stall Detection Protocol

Defines monitoring thresholds for code_runner_agent. All thresholds are user-overridable.

## Detection Types

### OUTPUT_STALL

- **What**: Monitored output files have not changed in size
- **Default threshold**: 3 consecutive checks (90 seconds at 30s interval)
- **Override**: User sets `stall_tolerance` (number of checks)
- **Exception**: Long-running single computations (e.g., large matrix operations) produce no intermediate output. If user warns "this takes a while", increase tolerance to 10 checks (5 min).
- **Action**: ADVISORY — notify user, suggest continue/kill/adjust

### METRIC_PLATEAU (training type only)

- **What**: Primary metric has stopped improving
- **Prerequisite**: User specifies `metric_file` (path to log) and `metric_key` (column/field name)
- **Default threshold**: Last 10 data points change < 0.1% relative
- **Override**: User sets `plateau_window` (data points) and `plateau_threshold` (relative change)
- **Action**: ADVISORY — show metric trend, suggest early stopping

### RESOURCE_ANOMALY

- **What**: Memory usage growing unexpectedly
- **Detection**: RSS memory via `ps aux` exceeds 3x the value recorded at process start
- **Override**: User sets `memory_multiplier_limit`
- **Action**: ADVISORY — possible memory leak, suggest investigation

### LOW_UTILIZATION

- **What**: A long, parallelizable task uses little available CPU/GPU while
  throughput remains poor
- **Detection**: utilization remains below 35% of the relevant device for 3
  checks and measured throughput is below the pilot or early-run expectation
- **Exceptions**: I/O-bound work, network waits, serial algorithms, deliberate
  laptop-safe settings, or small tasks where parallel overhead dominates
- **Action**: ADVISORY — identify likely serial loop, worker configuration,
  small batch, repeated I/O, data copy, or accelerator mismatch
- **Do not**: add workers before checking memory pressure, I/O wait, and task
  granularity

### SLOW_PROGRESS (etl and simulation types)

- **What**: Experiment progressing slower than expected
- **Prerequisite**: User specifies expected total units (rows, iterations) and log format
- **Default threshold**: Actual rate < 50% of expected rate (calculated from first 10% of progress)
- **Override**: User sets `progress_rate_threshold`
- **Action**: ADVISORY — show current rate, revised ETA

Apply the same logic to analysis and training when units processed, batches,
folds, tiles, files, or iterations can be observed.

### THROUGHPUT_REGRESSION

- **What**: Units processed per minute fall substantially after the pilot or
  early stable period
- **Default threshold**: current rate < 50% of pilot or early-run rate for 3
  checks
- **Action**: ADVISORY — show ETA and inspect memory pressure, cache misses,
  data growth, checkpoint overhead, thermal throttling, and worker imbalance

### HARD_TIMEOUT

- **What**: Experiment has exceeded maximum allowed duration
- **Default**: 30 minutes
- **Override**: User sets `timeout` at PARSE step
- **Action**: MANDATORY — kill process (SIGTERM, then SIGKILL after 10s), collect stderr, report

## Check Interval

- Default: every 30 seconds
- Override: User sets `check_interval_seconds`
- Minimum: 10 seconds (to avoid excessive polling overhead)
- Maximum: 300 seconds (5 minutes — longer gaps risk missing transient failures)

For tasks shorter than five minutes, prefer one pilot measurement and final
runtime reporting over continuous monitoring.

## Alert Behavior

- First detection: full alert with options (continue / kill / adjust)
- Same anomaly persists after user chooses "continue": silent for 2 checks, then one reminder
- After reminder: silent until anomaly resolves or escalates
- Different anomaly: always full alert regardless of prior alerts
