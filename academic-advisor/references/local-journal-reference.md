# Local Journal Reference

Use this protocol before naming, ranking, or excluding concrete journals. The
local file is a user-maintained candidate pool and preference ledger. It does
not replace current publisher scope, author guidelines, journal status, or
metric verification.

## Automatic Loading

Attempt to load `journal_ai_reference.md` without asking the user to attach it
when the filesystem is available. Resolve paths in this order:

Run:

```powershell
python scripts/resolve_journal_reference.py --project-root <project-root>
```

When `.codex/project.yaml` declares `paths.journal_reference`, add
`--configured <value>`. The resolver returns JSON containing the readable path,
relative display path, resolver source, and modification time.

1. A path explicitly supplied by the user.
2. `paths.journal_reference` in `.codex/project.yaml`. Resolve a relative value
   from `project.root`.
3. Relative candidates from the active research-project root:
   - `journal_ai_reference.md`
   - `others/journal_ai_reference.md`
   - `../others/journal_ai_reference.md`
   - `../../others/journal_ai_reference.md`
4. Walk upward from the project root. If an ancestor is named `Literatures`,
   try `others/journal_ai_reference.md` under that ancestor.
5. The `CODEX_JOURNAL_REFERENCE` environment variable.
6. Windows-only fallback:
   `D:\OneDrive\Literatures\others\journal_ai_reference.md`.

Stop at the first readable file. On macOS or another Windows machine, prefer a
relative path or `CODEX_JOURNAL_REFERENCE`; do not assume the fallback drive
exists.

## Reading Contract

Read at least:

- purpose, update date, metric source, and interpretation rules;
- required evaluation output;
- journal target table;
- matching map relevant to the manuscript;
- relevant entries in `Special Issue and Collection Matching`, if present;
- any notes attached to shortlisted journals.

Extract the journal name, local tier, fit keywords, acceptance conditions, and
recommended reframing. Treat `check`, `new`, old impact metrics, CAS/JCR class,
and acceptance tendencies as facts requiring current verification.

Local tier labels and `accepts_when`/`revise_toward` notes are search aids, not
universal editorial prerequisites or instructions to add every listed analysis.
Use the journal-fit rubric to separate current readiness, development potential,
and submission order. Correct an overrestrictive local inference against the
particular journal's current criteria; a broad-readership requirement for one
journal must not be applied to every selective venue. Do not infer acceptance
probability from a local tier or an available special issue.

## Optional Special Issue And Collection Matching

The register belongs to the user's journal reference document; do not duplicate
it in the skill. Use its `journal_ids` to associate relevant calls with candidate
journals, within the user's active journal constraints. Start with journal fit,
then assess call-specific topic, audience, eligibility, timing, and preparation.
A verified topical match may strengthen a recommendation or break a tie; it
does not lower evidence standards or imply better acceptance odds.

For relevant shortlisted calls, follow the document's Decision Rules and verify
the current official call before recommending that channel: opening and closing
dates, any abstract deadline or invitation requirement, article types, and author
eligibility. Recorded status and `checked_on` describe a past check, not current
availability. Keep unverified leads separate; exclude expired calls unless an
extension is officially confirmed. For cross-journal collections, evaluate each
participating journal separately and select one journal per submission.

Include useful matches alongside regular submission, with the document's
`special_issue_matches` fields. Explain the extra fit and necessary preparation;
do not reshape a strong paper solely to fit a call. Limit checks to relevant
candidates, unless the user asks for a broader call search or register refresh.
If the section is absent or irrelevant, skip it. If no suitable call is verified,
continue regular recommendations without waiting for a register update; omit an
empty table and use a brief scoped note when reporting the call search. A failed
verification is not evidence that no call exists.

## Priority

Use this precedence when sources disagree:

1. User's current explicit journal list or instruction.
2. Current official journal and publisher information.
3. The local journal reference as the user's maintained preference and
   candidate pool.
4. Zotero examples and broader web evidence.
5. Inference, clearly labeled.

Do not recommend journals outside a user-supplied hard list unless asked. When
no hard list is supplied, begin with suitable candidates from the local file,
then add an outside journal only when current evidence shows a materially
better fit and explain why.

## Reporting

Record:

```markdown
**本地期刊参考**
- 状态：已加载 / 未找到 / 读取失败
- 解析来源：project config / relative / Literatures ancestor / environment / Windows fallback
- 文件更新时间：
- 当前外部核查：已完成 / 部分完成 / 未完成
```

Use a relative path in reports when the file is inside or adjacent to the
project tree. Otherwise call it `local journal reference` unless the user asks
for the absolute path.
