# Artifact Templates

Use these compact schemas when creating project-local outputs. Keep them concise and source-grounded.

## `output/PAPER_PLAN.md`

```markdown
# Figure Plan: <paper/thesis title>

## 0. Document Status
- Source file:
- Target slot:
- Figure type:
- Production pathway:
- Target style:

## 1. One-Sentence Claim
<single sentence>

## 2. Figure Purpose
<what the figure lets a skim reader understand>

## 3. Claim-Evidence Map
| Claim ID | Claim | Source support | Figure role |
|---|---|---|---|

## 4. Figure Plan
| ID | Title | Type | Priority | Pathway | Status | Source |
|---|---|---|---|---|---|---|

## 5. Required Structure
<main modules, relationship types, and forbidden readings>
```

## `output/figures/FIGURE_MANIFEST.md`

```markdown
# Figure Manifest

| ID | Title | Type | Pathway | Priority | Status | Data Source | Script / Prompt | Claims | Missing Inputs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|

## Provenance
- Current render source:
- Project copy:
- Production rationale:
```

## `output/figures/FIGURE_CAPTIONS.md`

```markdown
# Figure Captions

**Figure 1. <Title>.** <What is shown>. <How the modules relate>. <Key takeaway aligned with the figure claim.>
```

## `output/figures/prompts/Fig01_<slug>_prompt.md`

```markdown
# Fig01 Prompt: <title>

## 1. Objective
## 2. Figure Type
## 3. Target Journal Style
## 4. Audience
## 5. Layout Instructions
## 6. Element Inventory
## 7. Relationships
## 8. Text Labels To Include
## 9. Style Constraints
## 10. Rendering Constraints
## 11. Negative Prompt / Avoidance
## 12. Short Prompt Version
## 13. Long Prompt Version
```

## `output/figures/prompts/Fig01_<slug>_design_notes.md`

```markdown
# Fig01 Design Notes

## Assumptions
- <assumption> Source: <file/section/line when available>.

## Review Of Current Render
- Strength:
- Issue:

## Revision Checklist
- [ ] <check>

## Second-Pass Prompt Hook
After viewing the next render: if <failure>, revise the prompt to state: "<repair instruction>".

## Confirmation List
- <items the author should confirm before shipping>
```

## `output/figures/Fig01_NORA_REVIEW.md`

```markdown
# NORA-Style Review: Fig01

## Verdict
<ship / revise / block>

## Major Checks
| Check | Status | Diagnosis | Revision Action |
|---|---|---|---|

## Recommended Next Render
<single highest-value revision>
```
