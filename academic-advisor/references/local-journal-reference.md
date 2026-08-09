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
- any notes attached to shortlisted journals.

Extract the journal name, local tier, fit keywords, acceptance conditions, and
recommended reframing. Treat `check`, `new`, old impact metrics, CAS/JCR class,
and acceptance tendencies as facts requiring current verification.

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
