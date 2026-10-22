# Good Question Workflow Protocol

Read this reference when running the full question-development workflow. It is
the source of truth for information sufficiency, intake, scoring, kill rules,
card structure, onboarding, and response order.

Use the project's `SCIENTIFIC_EXPLORATION_PROTOCOL.md` under `AGENTS.md`
for exploration decisions. This reference supplies question-development tools,
not a second methodology policy. Load
`../../shared/advantage-led-research-narrative.md` only for paper framing.

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
- acceptable contribution ambition: replication, contextual extension,
  incremental improvement, mechanism/boundary, or theory/method advance;
- venue, ethics, sample size, field site, compute, seasonality, and other hard
  constraints.

Ask at most one short clarifying question when one missing input would materially
change the direction. Otherwise proceed with explicit assumptions.

## Candidate Generation

Generate only enough candidates to expose a meaningful choice. Refine a supplied
question directly when the direction is settled; for open ideation, start with
a few distinct candidates and expand only if none is adequate. Choose useful
lenses rather than applying every lens:

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

Compare promising candidates on the decision-relevant criteria below. Use a
one-to-five scoring table only when it helps resolve a real trade-off or the
user requests it; qualitative reasoning is normally sufficient.

| Criterion | Meaning |
|---|---|
| Importance | Consequence for theory, practice, policy, or method |
| Feasibility | Credible evidence is possible with available resources |
| Falsifiability | Observable results could weaken or kill the idea |
| Evidence leverage | A small pilot can change belief meaningfully |
| Contribution value | The work adds credible replication, transferability, measurement, method, mechanism, theory, or decision value |
| Venue fit | The contribution magnitude and evidence match a plausible outlet |
| Downside learning | A negative result remains useful or publishable |
| Advantage clarity | The study can name what becomes more credible, useful, measurable, transferable, or efficient |
| Arena fit | The comparator, metric, population, and setting fairly reveal that value |

Drop or park candidates when:

- no clear beneficiary, theoretical stake, or practical consequence exists;
- novelty is only "nobody has done X" and no credible replication,
  transferability, measurement, policy, or cumulative-evidence value is named;
- no plausible falsifier can be named;
- required resources exceed the user's constraints;
- the method appears before the problem;
- complexity does not buy inferential value.

## Decision Test

For the strongest one to three candidates:

1. Name competing explanations when the claim is explanatory or causal and the
   alternative could materially change the conclusion. For
   replication or descriptive work, name the benchmark, prior estimate, or
   transferability expectation being tested.
2. Identify an observation or experiment that distinguishes them.
3. State what result would weaken or kill the preferred explanation.
4. Design the smallest feasible evidence test within available resources;
   two weeks is an example planning horizon, not a required duration.
5. State the advantage hypothesis and the fair comparison, metric, population,
   or setting in which it would matter.
6. In `reviewer` or `grant` mode, for high-cost irreversible projects, or when a
   material defect changes the decision, name the strongest reviewer or funder
   objection. Otherwise keep speculative attacks out of the user-facing card.
7. Repair, park, or reject a route with no credible evidence path or scientific
   value. A falsified hypothesis is not a failed research project: assess what
   its contradiction or boundary would teach. Distinguish that from a test
   too imprecise to decide.

## Good Question Card

Use this stable schema for a full planning/handoff card. For a focused question
refinement, return the question, rationale, discriminating test and next action
without empty fields or a full card. Preserve field names when a downstream
workflow expects the schema.

```markdown
## Good Question Card

**Working title:**
**Research question:**
**Why it matters:**
**Core assumption challenged:**
**Competing hypotheses (when relevant):**
**Discriminating observation or experiment:**
**What would falsify it:**
**Contribution level:**
**What this adds beyond prior work:**
**Leading advantage (candidate until supported):**
**Claim ID and decisive experiment ID, when assigned:**
**Winning arena or comparison:**
**Two-week pilot:**
**Data/resources needed:**
**Material decision risk (only when triggered):**
**Best next action:**
```

For Chinese responses, use:

```markdown
## 好问题卡

**暂定题目：**
**核心研究问题：**
**为什么值得做：**
**它挑战了什么默认假设：**
**竞争性解释（适用时）：**
**关键判别证据或实验：**
**什么结果会推翻它：**
**贡献层级：**
**相较既有研究增加了什么：**
**领先优势（证据支持前为候选）：**
**主张编号和关键实验编号（已有时）：**
**取胜场景或比较口径：**
**两周内可做的 pilot：**
**需要的数据/资源：**
**实质决策风险（仅在触发时）：**
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

For full development, combine the applicable elements below; these are not
mandatory separate sections for every request.

1. Brief diagnosis.
2. Mode and assumptions.
3. Domain brief and evidence ledger when required.
4. Source audit when decisive claims require it.
5. Candidate questions and chosen lenses.
6. Ranked shortlist.
7. Material repair or rejection notes, when triggered.
8. Good Question Cards.
9. Next action or pilot.
