# Good Story Handoff Contract

Use this contract when a story diagnosis will be consumed by
`academic-research`, `academic-advisor`, a presentation workflow, or a later
revision pass. It prevents each downstream step from inventing a new paper
story.

## Required Status

Classify the story before recommending structural changes:

- `supported`: the central claim and evidence chain are already supported.
- `candidate`: the story is plausible but one or more decisive links are
  unverified.
- `blocked`: the available evidence cannot support a coherent central claim.

## Stable Handoff

```markdown
## Story handoff

**Status:** supported | candidate | blocked
**Leading advantage:**
**Winning arena:**
**Central claim:**
**Resolved tension:**
**Decisive turn:**
**Intended audience:**
**Retellable sentence:**

### Story spine
1.
2.
3.
4.
5.

### Evidence and experiment-job map
| Claim or beat | Evidence location | Argument job | Evidence strength | Material condition, if any |
|---|---|---|---|---|

### Rewrite targets
| Priority | Target | Required change | Evidence dependency |
|---|---|---|---|

### Material constraints
-

### Downstream boundary
- Preserve:
- May revise:
- Must not claim:
```

## Rules

- Keep the central claim singular. Secondary contributions can support it but
  must not compete for equal narrative weight.
- Point evidence locations to a figure, table, result, section, dataset, or
  source rather than describing evidence vaguely.
- Mark a story `candidate` when a decisive evidence link is missing or only
  inferred.
- Do not populate `Material constraints` with speculative attacks. Include only
  an issue that changes the central claim, route, or required reporting.
- Put manuscript, abstract, section-order, figure-order, and title changes under
  `Rewrite targets`; do not bury them in prose.
- Carry `Must not claim` into later drafting, polishing, presentation, and
  journal-targeting steps.
- Localize the visible headings for the user, but preserve the fields and their
  order so another workflow can consume the handoff reliably.
