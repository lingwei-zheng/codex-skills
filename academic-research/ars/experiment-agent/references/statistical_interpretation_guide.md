# Statistical Interpretation Guide

Full protocol for validate mode's statistical interpretation and fallacy scan.
Read `../../../../shared/research-calibration.md` for the integrity floor,
claim-specific evidence, and contribution criteria. For simulation outputs,
also read `simulation-method-validation.md`.

## Part 1: Statistical Interpretation

### Step 1: Detect Statistical Content

Scan user-provided output for these patterns:
- p-values: `p = 0.023`, `p < .001`, `p > .05`
- Confidence intervals: `95% CI [0.12, 0.45]`, `CI: 0.12-0.45`
- Effect sizes: `d = 0.47`, `eta-squared = .036`, `r = .31`, `OR = 2.4`
- Test statistics: `t(98) = 2.34`, `F(2, 97) = 1.82`, `chi2(4) = 12.3`
- Coefficients: `beta = 0.23`, `B = 1.45`, `SE = 0.12`

If structured format (CSV/JSON): auto-extract column names matching these patterns.
If unstructured (console output, PDF/Word tables, or images), extract the
results with the appropriate available reader/OCR tools. Preserve page/table/row
or output-block locators and check labels, units, outcome, model, sample size,
and uncertainty against the source. Separate observed numbers from inferred
interpretations. Ask only about material unresolved recognition ambiguity or an
unknown primary outcome; do not require confirmation of every extracted value.
Continue interpreting clearly identified results while an ambiguous item waits.

### Step 2: Interpret Each Finding

For each statistical result, assess:

**Significance:**
- Report exact p-values when available instead of replacing them with a binary label.
- Do not create a special "marginal" category merely because a p-value lies
  near .05. Interpret the estimate, interval, effect magnitude, design, and
  decision context together.
- Flag multiple testing only when tests form a family for which selective
  reporting or inflated error is relevant.

**Effect Size:**

| Measure | Small | Medium | Large |
|---------|-------|--------|-------|
| Cohen's d | 0.2 | 0.5 | 0.8 |
| eta-squared | .01 | .06 | .14 |
| r (correlation) | .10 | .30 | .50 |
| Odds Ratio | 1.5 | 2.5 | 4.3 |

- Use conventional small/medium/large labels only when they are meaningful in
  the field; otherwise report the estimate in substantive units.
- Distinguish statistical precision from practical importance in context.

**Confidence Interval:**
- Interpret the interval for its actual estimand, confidence level, and method.
  Investigate apparent disagreement with a p-value (different tests, sidedness,
  or targets); neither automatically overrides the other
- Width: narrow CI = precise estimate; wide CI = uncertain estimate
- Asymmetric CI around point estimate → possible skewness

**Assumption Checks:**

| Test | Assumption or risk | Claim-triggered check |
|------|-----------|----------|
| t-test | Design, independence, distribution/tails, variance method | Assess validity of the chosen mean contrast and SE; absence of a named normality/Levene test is not itself failure |
| ANOVA | Design, variance/covariance assumptions | Assess the fitted model and relevant repeated-measure structure; no compulsory battery of tests |
| Chi-squared | Sparse expected counts can impair approximation | Assess approximation for this table; consider exact/Monte Carlo inference if needed, without changing categories to obtain a result |
| Regression | Functional form, dependence, variance and target | Check assumptions needed for the estimator/inference used; no universal residual-normality gate |
| Correlation | Measurement scale and relation targeted | Match the coefficient to the scientific target and data, including nonlinearity/tails when consequential |

**Multiple Comparisons:**
- Identify the inferential family and whether conclusions depend on selecting
  significant results from it.
- Recommend an appropriate correction, hierarchical model, or explicit
  exploratory labeling only when multiplicity threatens the reported claim.
- Do not trigger correction from an arbitrary count such as more than three
  tests.

### Step 3: Assign Confidence Level

| Level | Criteria |
|-------|---------|
| `SOLID` | Evidence is adequate for the stated scoped claim; applicable assumptions, uncertainty, and checks support it, including a small effect or informative null |
| `CAUTION` | A named unresolved uncertainty or sensitivity limits this claim; small magnitude or a p-value near a cutoff alone is not a warning |
| `RED_FLAG` | A material validity/integrity defect makes the stated inference unsafe; identify the affected branch and dependencies |

Assign confidence to claims/branches, not by counting passing metrics. Separately
state hypothesis outcome: supported, not supported, or insufficient evidence.
Do not turn nonsignificance into proof of absence, require medium effects for
reliability, or reject all findings because one independent branch is uncertain.

---

## Part 2: Triggered Fallacy Scan (11-Type Menu)

The 11 types below are a diagnostic menu. Check a type when its detection or
`When to suspect` condition is present. Report triggered checks, findings, and
material `N/A` decisions; do not claim quality from an "11/11 checked" count.
For first-draft work, prioritize risks that could invalidate the current claim;
defer non-decisive checks without capping essential validity checks.

### Structural Fallacies (Data Level)

**1. Simpson's Paradox**
- **What**: Overall trend reverses when data is split by a grouping variable
- **Detection**: If analysis has grouping variables (gender, department, site), compare aggregated result direction vs per-group direction
- **When to suspect**: Aggregate shows negative relationship but subgroups are all positive (or vice versa)
- **Severity if found**: RED_FLAG
- **Reporting note**: describe what numbers say (overall vs per-group), do NOT recommend which to report — that is an editorial decision for the reviewer

**2. Ecological Fallacy**
- **What**: Inferring individual-level relationships from group-level data
- **Detection**: Unit of analysis (e.g., schools, countries) differs from unit of inference (e.g., students, citizens)
- **When to suspect**: Regression on aggregated data used to make claims about individuals
- **Severity if found**: RED_FLAG

**3. Berkson's Paradox**
- **What**: Selection/sampling bias creates spurious negative correlation
- **Detection**: Sample drawn from a filtered population (only hospitalized patients, only admitted students, only published papers)
- **When to suspect**: Two seemingly unrelated variables show unexpected negative correlation in a selected sample
- **Severity if found**: CAUTION

**4. Collider Bias**
- **What**: Controlling for a variable that is a common effect of both IV and DV creates spurious association
- **Detection**: Check if any control variable could be caused by both IV and DV
- **When to suspect**: Adding a control variable changes the sign or significance of the main effect
- **Severity if found**: CAUTION

### Inferential Fallacies (Interpretation Level)

**5. Base Rate Neglect**
- **What**: Reporting sensitivity/specificity without considering prevalence
- **Detection**: Results present conditional probabilities (PPV, NPV, sensitivity, specificity) without base rate
- **When to suspect**: Screening or diagnostic accuracy studies
- **Severity if found**: CAUTION

**6. Regression to the Mean**
- **What**: Extreme values naturally move toward the mean on re-measurement
- **Detection**: Pre-post design where groups were selected based on extreme scores (lowest performers, highest risk)
- **When to suspect**: "Improvement" in the worst-performing group without a control group
- **Severity if found**: RED_FLAG if no control group; CAUTION if control group exists but not compared

**7. Survivorship Bias**
- **What**: Analyzing only "survivors" (those who completed, stayed, succeeded)
- **Detection**: Attrition, selection, or missingness could change the target
  comparison; assess reasons and the analysis population rather than a fixed
  percentage. Require intention-to-treat reasoning when the design/estimand calls for it
- **When to suspect**: Longitudinal studies, intervention studies, cohort studies
- **Severity if found**: CAUTION if dropout documented; RED_FLAG if dropout not reported

**8. Look-Elsewhere Effect**
- **What**: Testing many variables and reporting only the significant ones
- **Detection**: Ratio of (reported significant results) to (total tests run) is suspiciously high
- **When to suspect**: Exploratory analysis with many DVs; "we also found..." language
- **Severity if found**: CAUTION

**9. Garden of Forking Paths**
- **What**: Many researcher degrees of freedom (outlier removal criteria, variable transformations, model specifications) but only one path reported
- **Detection**: Undisclosed researcher degrees of freedom, selective reporting,
  or a confirmatory claim that depends on one unmotivated specification.
  Absence of exhaustive robustness checks is not itself a first-draft failure.
- **When to suspect**: Complex analyses with many decision points
- **Severity if found**: NOTE if exploratory; CAUTION if presented as confirmatory

### Causal Fallacies (Claim Level)

**10. Correlation != Causation**
- **What**: Observational study uses causal language
- **Detection**: Study design is cross-sectional, correlational, or observational, but language includes "caused", "led to", "resulted in", "improved", "reduced"
- **When to suspect**: Always check in non-experimental designs
- **Severity if found**: CAUTION
- **Reporting note**: flag the specific causal verb and replace or recommend an
  accurate associational alternative such as `was associated with` or
  `correlated with`. Once the verb is corrected, do not require `exploratory`,
  `observational`, or a repeated no-causality disclaimer unless that additional
  information is independently relevant.

**11. Reverse Causality**
- **What**: The assumed direction of causation may be backwards
- **Detection**: Cross-sectional data with directional claims; no temporal precedence established
- **When to suspect**: directional causal interpretation from cross-sectional
  data. The statistical verb `predicts` may describe model performance without
  claiming temporal or causal priority; inspect the surrounding interpretation.
- **Severity if found**: CAUTION

---

## Relationship to ARS Logical Fallacies Catalog

ARS `deep-research/references/logical_fallacies.md` contains a broader 32-type catalog covering formal, informal, and rhetorical fallacies. This guide's 11-type list focuses specifically on **statistical and methodological** fallacies relevant to experiment validation. 7 types overlap (Simpson's Paradox, Ecological Fallacy, Survivorship Bias, Base Rate Neglect, Regression to Mean, Correlation != Causation, Reverse Causality). When both skills are loaded, this guide takes precedence for experiment result validation; ARS's catalog applies to broader argument evaluation in paper review.

**Severity mapping to ARS terminology**: experiment-agent's `RED_FLAG` corresponds to issues ARS would classify as requiring mandatory revision. `CAUTION` corresponds to issues ARS would flag for author attention. `NOTE` corresponds to optional commentary.

---

## Output Template

See `templates/output_formats.md` "Validation Report" section for the Markdown template.

## Comparison And Author-Side Handoff

Report the actual primary comparison, uncertainty and matched conditions.
Retain primary outcomes even when another metric is more favorable. Label
post hoc dimensions exploratory and keep required contrary results traceable.
An efficiency or deployment trade-off requires evidence for that benefit;
do not invent it from a performance shortfall. Avoid a generic win/lose verdict.
Pass these facts to the main workflow for evidence-supported interpretation;
statistical validation and the paper's advantage state are distinct.

Interpretation references:
[ASA statement on p-values](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf);
[Altman and Bland, Absence of evidence is not evidence of absence](https://doi.org/10.1136/bmj.311.7003.485).
