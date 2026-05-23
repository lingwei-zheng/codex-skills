# Human Final Pass Policy

## Goal

Make an already polished academic paper sound less mechanical while keeping it credible as a formal research manuscript. The target is not casual writing. The target is slightly more varied, author-like academic prose.

## Authorial posture

In `human-final-pass`, act like a human author doing a final pass while the research context is still fresh.

A human author:

- varies confidence across claims instead of hedging everything equally;
- sometimes follows a dense sentence with a shorter one;
- lets some results receive more interpretive space than others;
- does not force every paragraph into the same rhythm;
- occasionally uses a more direct transition instead of a stock connective.

This posture should guide edits. It is not a license to become casual or imprecise.

## Allowed humanization moves

- More direct motivation or framing sentences in the Introduction.
- Slightly less template-like transitions.
- Occasional short observation sentences after denser technical statements.
- Moderate first-person academic voice when the manuscript already uses `we`.
- Mixed active and passive constructions where both are natural.
- Mild emphasis asymmetry when one result is clearly more important than another.

Examples of acceptable natural phrasing patterns:

- `in practice`
- `a closer look`
- `this pattern is not surprising`
- `this result is useful because`
- `one might expect`
- `at first glance`
- `the reason is straightforward`

Do not inject these mechanically. Use them only when they fit the local argument.

## Pattern-breaking first

Before adding natural phrasing, look for machine-like patterns:

- overused transition starters such as `However,`, `Furthermore,`, `Moreover,`, `In addition,`;
- paragraphs with near-identical length and topic-sentence rhythm;
- overly symmetric space allocation across claims;
- stock strength markers such as `robust`, `comprehensive`, `extensive experiments demonstrate`, `state-of-the-art`.

Break these patterns selectively. Do not change a pattern that is serving clarity, venue convention, or citation accuracy.

## Preserve existing natural traces

If a passage already has convincing human-style phrasing, preserve it. Do not rewrite it simply to make it seem even more human. That usually creates artificial texture.

## Grammar-error policy

Grammar imperfections are an explicit opt-in overlay, not the default humanization mechanism.

Allowed:

- a missing or slightly awkward article in a low-stakes noun phrase;
- a mild preposition choice that remains understandable;
- a small agreement issue in a peripheral clause;
- slightly uneven sentence rhythm that remains readable.

Forbidden:

- anything that changes meaning;
- anything touching method names, dataset names, metrics, formulas, citations, theorem statements, or numeric comparisons;
- anything that makes the paper seem careless or ambiguous;
- more than one imperfection in the same sentence.
