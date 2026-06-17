# Xiaohongshu Search Setup

This local skill is a read-only wrapper around `autoclaw-cc/xiaohongshu-skills`.

## Dependencies

- Python 3.11+
- `D:\Anaconda\envs\codex_py311\python.exe` on this Windows machine, or another Python 3.11+ interpreter
- Google Chrome

Install Python dependencies:

```powershell
cd C:\Users\Lingwei\.codex\skills\xhs-search
D:\Anaconda\envs\codex_py311\python.exe -m pip install requests websockets python-socks
```

If using another Python 3.11+ environment, either run that interpreter explicitly or set:

```powershell
$env:XHS_SEARCH_PYTHON = "C:\path\to\python.exe"
```

## Chrome Extension

Load the extension manually:

1. Open `chrome://extensions/`.
2. Enable Developer mode.
3. Click "Load unpacked".
4. Select `C:\Users\Lingwei\.codex\skills\xhs-search\extension`.
5. Confirm that "XHS Bridge" is enabled.

The CLI talks to a local WebSocket bridge at `ws://localhost:9333`. The wrapper starts the bridge server through upstream CLI behavior when needed.

## Read-Only Contract

Use only:

- `check-login`
- `list-feeds`
- `search-feeds`
- `get-feed-detail`
- `user-profile`

The wrapper blocks publishing, drafts, comments, replies, likes, favorites, cookie deletion, and phone-code login commands.
