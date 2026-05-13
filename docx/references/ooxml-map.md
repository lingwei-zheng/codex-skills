# OOXML Map For `.docx`

Use this reference when a Word document needs more than plain-text extraction.

## Important package parts

- `word/document.xml`: main body text
- `word/styles.xml`: style definitions
- `word/numbering.xml`: list numbering and bullets
- `word/comments.xml`: comments
- `word/footnotes.xml`: footnotes
- `word/endnotes.xml`: endnotes
- `word/header*.xml`: headers
- `word/footer*.xml`: footers
- `word/_rels/document.xml.rels`: relationships to images and linked parts
- `word/media/`: embedded images and other media
- `docProps/core.xml`: document metadata

## Tracked change markers

- `<w:ins>`: inserted content
- `<w:del>`: deleted content
- `<w:commentRangeStart>` / `<w:commentRangeEnd>`: comment anchors

## Practical guidance

- If the user wants only content rewriting, extract text first and avoid low-level OOXML edits.
- If formatting fidelity matters, inspect the package before making claims about structure.
- If comments or revisions matter, preserve the original and write a new output file rather than mutating in place.
