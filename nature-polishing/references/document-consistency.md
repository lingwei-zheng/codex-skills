# Document Consistency Protocol

Use this protocol for a whole manuscript, multiple sections, or repeated
polishing rounds. Do not create ledgers for a narrow sentence-level request.

## Terminology Ledger

Track terms whose wording affects scientific meaning, discoverability, or
cross-section consistency.

| Concept | Preferred term | Allowed variant | Avoid | First definition | Notes |
|---|---|---|---|---|---|

Rules:

- Select the preferred term from the user's manuscript, target field, or stated
  terminology policy; do not normalize a specialist term from memory alone.
- Preserve established abbreviations after their first definition.
- Treat variable names, exposure definitions, spatial units, outcome labels,
  population labels, and model names as protected terminology.
- Use an allowed variant only when repetition would harm readability and the
  variant cannot change interpretation.
- Flag unresolved term conflicts rather than silently choosing between
  substantively different meanings.

## Claim-Strength Ledger

Track central and repeated claims so polishing does not strengthen or weaken them
across sections.

| Claim ID | Evidence type | Supported verb | Required qualifier | Sections | Prohibited upgrade |
|---|---|---|---|---|---|

Use stable IDs such as `C1`, `C2`, and `C3`. Record:

- whether the evidence is descriptive, associational, predictive, quasi-causal,
  experimental, mechanistic, or interpretive;
- the strongest verb the evidence supports;
- population, place, time, scale, or design qualifiers that must remain;
- every section where the claim appears;
- upgrades that are not supported, such as association to causation or sample
  findings to universal generalisation.

Record only qualifiers that change interpretation. Do not turn a study-level
design label into a phrase that must be repeated with every claim. When
`associated with` already sets the correct evidence level, leave
`Required qualifier` empty unless scope, timing, population, post hoc status, or
another independent boundary matters.

## Cross-Section Check

Before delivery:

1. Compare title, abstract, Introduction contribution, Results, Discussion, and
   Conclusion against the claim-strength ledger.
2. Confirm that repeated quantities, sample descriptions, spatial units, model
   names, and abbreviations are consistent.
3. Confirm that the Discussion and Conclusion do not exceed the strongest claim
   supported in the Results.
4. Confirm that a wording improvement has not removed a necessary boundary.
5. Report unresolved conflicts with their section locations.

Keep the ledgers as working state. Show the full tables only when the user asks
for an audit trail; otherwise report concise consistency flags.
