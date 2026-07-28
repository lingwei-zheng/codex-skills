# Good Question Workflow Protocol

Read this reference when running the full question-development workflow. It is
the source of truth for information sufficiency, intake, scoring, kill rules,
card structure, onboarding, and response order.

## Information Sufficiency Gate

Proceed without retrieval when:

- the user provides the domain facts, data context, and constraints needed;
- the answer can remain methodological or assumption-labelled;
- no decisive claim depends on current literature, field consensus, reviewer
  expectations, novelty, journal fit, or domain-specific feasibility.

Enter enhanced retrieval before ideation when:

- the user asks for current, recent, field-specific, source-grounded, or deep
  research help;
- the recommendation depends on a literature gap, consensus, technical
  bottleneck, target journal, grant context, or reviewer norm;
- the field is unfamiliar, niche, fast-moving, or not covered by supplied
  evidence.

Enhanced retrieval means:

1. State which knowledge and claims are missing.
2. Gather targeted evidence with suitable research or web tools.
3. Build a compact domain brief.
4. Audit claims that would decide the recommendation.
5. Generate and rank questions only after that evidence is available.

Use this ledger when field claims matter:

```markdown
**Evidence ledger**
- Source-backed:
- Inference:
- Unknown / needs verification:
```

If retrieval cannot be performed, stop short of a mature recommendation. Offer a
retrieval plan, claim-to-verify checklist, and provisional question forms.

## Intake

Extract or ask for:

- field and subfield;
- mode: mentor, reviewer, collaborator, or grant;
- current idea, frustration, or failure;
- available data, methods, collaborators, time, equipment, and access;
- target output: thesis, paper, grant, pilot, rebuttal angle, or long-term
  direction;
- venue, ethics, sample size, field site, compute, seasonality, and other hard
  constraints.

Ask at most one short clarifying question when one missing input would materially
change the direction. Otherwise proceed with explicit assumptions.

## Candidate Generation

Generate five to ten candidates using several of these lenses:

- importance and tractability;
- assumption challenge;
- strong inference and competing hypotheses;
- boundary conditions;
- what has changed since an older negative result;
- structural analogy with an adjacent field;
- simpler baseline versus unnecessary complexity;
- stakeholder rotation and decision relevance.

For each candidate, state the question and the hidden assumption or tension it
tests. Do not confuse a topic, method, dataset, or activity with a research
question.

## Convergence

Score promising candidates from one to five:

| Criterion | Meaning |
|---|---|
| Importance | Consequence for theory, practice, policy, or method |
| Feasibility | Credible evidence is possible with available resources |
| Falsifiability | Observable results could weaken or kill the idea |
| Evidence leverage | A small pilot can change belief meaningfully |
| Originality | The question challenges assumptions or combines fields non-trivially |
| Downside learning | A negative result remains useful or publishable |

Drop or park candidates when:

- no clear beneficiary, theoretical stake, or practical consequence exists;
- novelty is only "nobody has done X";
- no plausible falsifier can be named;
- required resources exceed the user's constraints;
- the method appears before the problem;
- complexity does not buy inferential value.

## Stress Test

For the strongest one to three candidates:

1. Name at least two competing explanations.
2. Identify an observation or experiment that distinguishes them.
3. State what result would weaken or kill the preferred explanation.
4. Design a two-week pilot or the smallest feasible evidence test.
5. Name the strongest reviewer or funder objection.
6. Repair, park, or reject any candidate that fails a fatal gate.

## Good Question Card

Use this stable schema:

```markdown
## Good Question Card

**Working title:**
**Research question:**
**Why it matters:**
**Core assumption challenged:**
**Competing hypotheses:**
**Discriminating observation or experiment:**
**What would falsify it:**
**Two-week pilot:**
**Data/resources needed:**
**Strongest reviewer objection:**
**Best next action:**
```

For Chinese responses, use:

```markdown
## 好问题卡

**暂定题目：**
**核心研究问题：**
**为什么值得做：**
**它挑战了什么默认假设：**
**竞争性解释：**
**关键判别证据或实验：**
**什么结果会推翻它：**
**两周内可做的 pilot：**
**需要的数据/资源：**
**最强评审质疑：**
**下一步动作：**
```

If the user only needs brainstorming, stop after ranked cards. If execution is
requested, convert the best card into a pilot with milestones and decision
gates.

## Human Onboarding

When the user asks how to use this skill in a discipline, ask for the field,
current confusion, data or resources, target output, intended audience, hard
constraints, and biggest worry. Recommend one mode and provide one reusable
prompt. Use `docs/field-playbooks.md` only when a fuller discipline-oriented
onboarding example is needed.

## Response Order

1. Brief diagnosis.
2. Mode and assumptions.
3. Domain brief and evidence ledger when required.
4. Source audit when decisive claims require it.
5. Candidate questions and chosen lenses.
6. Ranked shortlist.
7. Repair or rejection notes.
8. Good Question Cards.
9. Next action or pilot.
