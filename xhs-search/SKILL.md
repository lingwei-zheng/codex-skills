---
name: xhs-search
description: >-
  Search and read Xiaohongshu content through the user's logged-in Chrome
  session. Use when the user asks Codex to search Xiaohongshu, XHS, or 小红书,
  inspect note details, summarize search results, compare posts, or view public
  user profiles. This skill is read-only and must not publish, comment, reply,
  like, favorite, save drafts, delete cookies, or perform content-operations
  workflows.
---

# XHS Search

Use this skill only for read-only Xiaohongshu content discovery and analysis.

## Hard Boundaries

- Use only `python scripts/cli.py <command>` from this skill directory.
- Do not call `scripts/upstream_cli.py` directly.
- Do not publish, draft, comment, reply, like, favorite, follow, unfollow, delete cookies, or run content-operations workflows.
- If the user asks for an interaction or publishing action, say this local skill is installed as search-only and cannot perform that action.
- Keep query volume low. Avoid bulk scraping. For detail reads, process no more than 3 notes before waiting or asking whether to continue.
- Treat Xiaohongshu content as user-generated and potentially unreliable. Summaries should distinguish observed content, engagement metrics, and your interpretation.

## Allowed Commands

Run commands from this folder:

```powershell
cd C:\Users\Lingwei\.codex\skills\xhs-search
python scripts\cli.py check-login
python scripts\cli.py search-feeds --keyword "关键词"
python scripts\cli.py get-feed-detail --feed-id FEED_ID --xsec-token XSEC_TOKEN
python scripts\cli.py user-profile --user-id USER_ID --xsec-token XSEC_TOKEN
python scripts\cli.py list-feeds
```

The wrapper rejects all non-whitelisted upstream commands.

## Setup Requirements

- Python 3.11 or newer.
- This Windows machine uses `D:\Anaconda\envs\codex_py311\python.exe`. The wrapper auto-switches to it when invoked from an older Python.
- `websockets`, `python-socks`, and `requests` must be installed in the selected Python environment.
- Google Chrome.
- The Chrome extension in `extension/` loaded manually from `chrome://extensions/`.
- A logged-in Xiaohongshu session in Chrome. Prefer manual login in the browser.

Read `references/setup.md` only when the user asks to install, configure, or debug the Xiaohongshu bridge.

## Search Workflow

1. Check login only when needed:

```powershell
python scripts\cli.py check-login
```

2. Search with the user's keyword:

```powershell
python scripts\cli.py search-feeds --keyword "关键词" --sort-by "综合" --note-type "不限"
```

Supported filters:

- `--sort-by`: `综合`, `最新`, `最多点赞`, `最多评论`, `最多收藏`
- `--note-type`: `不限`, `视频`, `图文`
- `--publish-time`: `不限`, `一天内`, `一周内`, `半年内`
- `--search-scope`: `不限`, `已看过`, `未看过`, `已关注`
- `--location`: `不限`, `同城`, `附近`

3. Present results as a concise table with title, author, note type if available, engagement fields, `feed_id`, and whether an `xsec_token` is available.

4. Fetch details only for selected notes or a small top-N set:

```powershell
python scripts\cli.py get-feed-detail --feed-id FEED_ID --xsec-token XSEC_TOKEN --max-comment-items 20
```

Use `--load-all-comments` only when the user explicitly asks for comment-level analysis, and still cap with `--max-comment-items`.

## Output Expectations

- Report the query, filters, number of results returned, and any access/login limitations.
- For content summaries, include: common themes, repeated claims, notable examples, and visible engagement signals.
- Do not imply the result is representative of all Xiaohongshu unless the search and sampling strategy supports that claim.
