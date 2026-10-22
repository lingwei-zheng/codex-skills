# Reproducibility Protocol

Defines how validate mode verifies reproducibility by re-running and comparing.
Compare against the recorded specification and declared tolerances.
Successful execution, reproducibility and scientific contribution are separate.

## Applicability

- **Applicable**: Any experiment with an executable command and recorded original results
- **Environment-sensitive but still comparable**: Hardware-dependent benchmarks, GPU training runs, OS-sensitive pipelines where the environment can be documented and approximately matched
- **Not applicable**: Human studies, external API calls with non-deterministic responses, experiments whose original environment can no longer be reconstructed at all
- If not applicable, skip reproducibility verification and report: "Reproducibility: N/A — [reason]"

## Procedure

### Step 1: Classify Experiment Determinism

| Type | Criteria | Expected Outcome |
|------|----------|-----------------|
| **Deterministic replay** | All random states, inputs, code, and relevant environment fixed; deterministic implementation | Exact scientific-output match |
| **Stochastic replication** | New draws under the same declared design, or documented nondeterminism | Compare prespecified targets with uncertainty appropriate to the claim |
| **Environment-sensitive** | Hardware, OS, driver, or libraries affect outputs | Document differences and justify comparability; do not automatically widen tolerances |

Infer the class from configuration, code, logs, and prior decisions. Ask only
about a material unresolved ambiguity. Randomness in an algorithm does not
preclude deterministic replay when all relevant states are controlled.

### Step 2: Re-Run

1. Record the comparison scope, primary outputs, seed policy, criteria and
   environment before execution. Preserve approved project tolerances; a material
   change requires the existing decision/approval process
2. Delegate to code_runner_agent with the recorded command and working directory,
   applying existing run/restart and resource approvals
3. code_runner_agent runs full EXECUTE → MONITOR → COLLECT cycle
4. Collect new experiment_result, including failures and deviations

### Step 3: Compare

**Deterministic comparison:**
- For each numeric metric: `abs(original - rerun)` must be exactly 0
- Compare deterministic scientific payloads exactly. Byte equality is appropriate
  for canonical deterministic artifacts; timestamps or serialization metadata
  may differ. Declare any normalization and never normalize scientific differences away
- Any scientific-output difference = `MISMATCH`; diagnose before attributing it
  to acceptable numerical tolerance

**Stochastic comparison:**
- Compare the relevant estimate, contrast, or distribution with uncertainty,
  including Monte Carlo uncertainty where applicable. Read
  `simulation-method-validation.md` for estimator comparisons
- Use justified absolute, relative, or decision-scale criteria for the target;
  no universal percentage tolerance or all-scenario relative-MSE requirement
- Near-zero quantities need meaningful absolute precision, not an arbitrary
  epsilon that makes a relative ratio look well-defined
- Retain failures, extreme values, and tails that affect the claim. A
  nonsignificant difference alone does not establish equivalence

**Environment-sensitive comparison:**
- Record environment details first: hardware, OS, major library/toolchain versions
- Identify which outputs should remain invariant and which require a justified
  numerical comparison. An environment change does not authorize a looser criterion
- When efficiency is a scientific claim, compare time/cost using documented
  workloads, hardware and measurement uncertainty; otherwise timing is operational metadata

**File comparison:**
- Check required artifacts, schema, units, identifiers, and substantive content.
  Same-run replay should preserve expected record counts; independent datasets
  or stochastic outputs need their declared generation and inclusion rules
- Unequal source sample sizes are not a reproducibility failure by themselves.
  Compare each source to its own recorded inputs and analytic denominator
- File size and spot checks are diagnostics, not sufficient evidence of
  numerical reproduction or scientific validity

### Step 4: Verdict

| Verdict | Criteria |
|---------|---------|
| `REPRODUCIBLE` | Successful rerun meets the justified comparison criteria for the declared outputs/scope |
| `PARTIALLY_REPRODUCIBLE` | Identified outputs/branches reproduce while others do not; name dependent claims |
| `NOT_REPRODUCIBLE` | Meaningful comparison demonstrates a failure of the primary reproduction criteria |
| `CANNOT_VERIFY` | Re-run or comparison could not be completed meaningfully |

The verdict covers the declared comparison, not every possible research
scenario. Do not shrink that scope post hoc to conceal a mismatch. Use
`VERIFIED` only for an artifact/scope with a successful reproducibility rerun;
stats-only interpretation stays `ANALYZED`. Partial reproduction cannot promote
the whole artifact to verified or negate independent valid findings.

## Edge Cases

- **Missing original results**: Cannot compare → report "Reproducibility: CANNOT_VERIFY — original results not provided"
- **Environment changed**: Warn "environment may differ from original run — results may not match even if code is correct"
- **Uncertainty too large**: report inability to resolve the comparison, not a
  fabricated match; add runs only within a justified authorized budget
- **Partial output**: identify the missing file and affected claims; if it is
  essential to the primary comparison, do not call that comparison reproduced
