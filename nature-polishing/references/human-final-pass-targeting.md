# Human Final Pass Targeting

## Eligible sections

Apply human-style variation only to these sections unless the user explicitly asks otherwise:

- Introduction
- Related Work
- Related Works
- Literature Review when it functions as related work
- Results
- Experimental Results
- Results-facing prose inside Results and Discussion

## Excluded sections

Do not add conversational phrasing or intentional grammar imperfections to:

- Title
- Abstract
- Keywords
- Method, Methodology, Approach, Model, Framework, or Algorithm
- Theory, Preliminaries, Problem Formulation, or Proofs
- Experimental Setup, Datasets, Metrics, or Implementation Details
- Ablation Study setup prose
- Limitations
- Conclusion
- Acknowledgments
- References or Bibliography
- Tables, figure captions, equations, algorithms, theorem environments, and code blocks

## Boundary handling

For LaTeX, detect boundaries from `\section`, `\subsection`, and `\paragraph` commands and preserve those commands exactly.

For Markdown or plain prose, rely on visible headings. If headings are missing or ambiguous, edit only paragraphs whose section role is clear and state the assumption in `Revision notes:`.

When a section mixes setup and results, edit only the result-facing interpretive prose and leave setup details formal.
