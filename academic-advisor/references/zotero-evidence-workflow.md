# Zotero Evidence Workflow

Use this file whenever `academic-advisor` performs evidence grounding. This workflow is read-only by default.

## Resolve the Helper

Prefer the currently available `zotero:Zotero` skill when it is loaded in the session. If it is not loaded automatically, locate the helper dynamically instead of hard-coding a plugin cache hash:

```powershell
Get-ChildItem -Path "$HOME\.codex\plugins\cache" -Recurse -Filter zotero.py |
  Where-Object { $_.FullName -match '\\skills\\zotero\\scripts\\zotero.py$' } |
  Select-Object -First 1 -ExpandProperty FullName
```

Run the helper with the available Python executable. On Windows, `python` is acceptable when it can run the helper; otherwise use the bundled or Anaconda Python already used for Zotero workflows.

## Minimum Protocol

1. Run readiness check:

```powershell
python <zotero.py> status --json
```

2. If the local API is disabled and the user asked for Zotero-backed evidence, enable it:

```powershell
python <zotero.py> enable --restart
```

3. Search Zotero before web search:

```powershell
python <zotero.py> search "keyword" --json
```

4. Use full text only when metadata is insufficient and the claim affects the recommendation:

```powershell
python <zotero.py> fulltext ITEM_KEY --out <temporary-or-output-path>
```

Do not import, edit, tag, delete, or otherwise write to Zotero unless the user explicitly requests it.

## Query Sources

Generate 5-12 targeted Zotero queries from:

- research question terms and synonyms;
- theory constructs;
- method terms and data source names;
- target journal names from the user's journal list;
- geography, human geography, GIScience, health geography, spatial analysis, environmental exposure, mobility, place, neighborhood, or health outcome terms when relevant.

Prefer fewer high-signal queries over broad bulk searches.

## Evidence Ledger Fields

For each useful Zotero item, capture:

- title;
- creators and year;
- Zotero item key;
- BibTeX key when available;
- evidence role: theory anchor, method precedent, direct neighbor, contradictory evidence, target-journal example, missing-reference candidate;
- the specific claim or decision it supports.

## Blockers

If Zotero cannot be used, report the exact gate in the final report:

- Zotero app missing or closed;
- local API disabled;
- port `23119` closed;
- helper not found;
- no matching item;
- full text unavailable;
- permission or connector failure.

Do not hide a Zotero failure by immediately switching to web search. Use web search as fallback, but keep the Zotero blocker visible in the evidence ledger.
