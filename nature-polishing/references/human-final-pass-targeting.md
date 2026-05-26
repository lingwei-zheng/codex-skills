# Section Targeting

## Eligible Sections

Apply human-style variation only to these sections unless the user explicitly asks otherwise:

- Introduction
- Related Work
- Related Works
- Literature Review, when it functions as Related Work
- Results
- Experimental Results
- Results and Discussion, only for the results-facing prose
- Conclusion, with moderate variation only
- Limitations, with moderate variation only

## Excluded Sections

Do not add conversational phrasing or intentional grammar imperfections to:

- Title
- Abstract
- Keywords
- Method, Methodology, Approach, Model, Framework, or Algorithm
- Theory, Preliminaries, Problem Formulation, or Proofs
- Experimental Setup, Datasets, Metrics, or Implementation Details
- Ablation Study, unless the paragraph is clearly results interpretation rather than setup
- Acknowledgments
- References or Bibliography
- Tables, figure captions, equations, algorithms, theorem environments, and code blocks

## Boundary Handling

For LaTeX, use section commands such as `\section`, `\subsection`, and `\paragraph` to detect boundaries. Preserve the commands exactly.

For plain prose, use visible headings. If headings are missing or ambiguous, state the assumption and only edit paragraphs that clearly belong to Introduction, Related Work, Results, Conclusion, or Limitations.

When a section combines setup and results, edit only the interpretive result sentences and leave setup details formal.

For Conclusion and Limitations, preserve the claim boundary, evidence certainty, stated limitations, numeric values, and technical meaning. Do not add new implications, new limitations, or a stronger closing claim.
