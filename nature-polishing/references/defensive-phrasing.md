# Defensive Phrasing

Use this file when a draft relies on defensive disclaimers instead of direct claims, especially in abstract, introduction, results openings, contribution sentences, and conclusions.

## Core rule

Prefer direct statements of what the paper does, shows, or evaluates. Do not spend the first clause telling the reader what the paper is not claiming unless that negative framing is necessary for correct interpretation.

## Common low-value defensive forms

- `We do not claim that ...`
- `This does not mean that ...`
- `Our purpose is not ... but rather ...`
- `We are not trying to prove ...`
- `This should not be interpreted as ...`

These forms are often low-density because they lead with negation, slow the argument, and can spotlight weaknesses that the paragraph does not need to foreground.

## Keep versus rewrite

Keep a boundary statement when:

- it prevents a genuine overclaim
- it identifies a real limit of design, sample, identification, or scope
- it belongs in Discussion, Limitations, methods assumptions, or robustness framing
- the omitted boundary would materially change the correct interpretation

Rewrite or compress when:

- the sentence could simply state the scope positively
- the paragraph is carrying the contribution, key result, or main implication
- the sentence pre-emptively raises an objection the reader would not otherwise need to focus on here
- the disclaimer does not change the paper's truth conditions

## Placement rules

Default avoid positions:

- abstract result or implication sentence
- introduction contribution or research-question sentence
- results opening claim
- conclusion's central contribution sentence

Allowed but should be restrained:

- discussion boundary sentence
- limitations section
- methods assumptions or identification constraints
- response-to-reviewers language when the limitation is directly responsive

## Rewrite patterns

Bad:

- `We do not claim that our cases are representative of all contexts.`

Better:

- `The analysis focuses on the observed cases and evaluates the mechanism within those contexts.`

Bad:

- `Our purpose is not to prove causality, but rather to explore the association between X and Y.`

Better:

- `This study examines the association between X and Y.`

Bad:

- `This does not mean that policy A will always improve outcome B.`

Better:

- `The findings indicate that policy A can improve outcome B under the conditions studied.`

Bad:

- `We are not trying to argue that this mechanism is universal.`

Better:

- `We evaluate this mechanism in the cases examined here.`

## Section reminder

State the claim first. Attach the boundary only if it changes how the claim should be read.

## Causal-boundary economy

`Associated with`, `correlated with`, and `related to` already avoid a causal
claim. Do not routinely add `exploratory`, `observational`, `non-causal`, or
`under the observed conditions` to the same sentence. That stacking repeats one
boundary several times and makes ordinary findings sound apologetic.

Keep the extra label only when it carries additional information:

- `exploratory` distinguishes post hoc or non-preregistered analysis from a
  confirmatory analysis;
- `observational` identifies or contrasts the study design;
- a no-causality statement responds to a real ambiguity in a central
  interpretation, preferably once in Discussion or Limitations.
