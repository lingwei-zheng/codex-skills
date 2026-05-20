# Conda Environment

Use `environment.yml` to reproduce the `codex_ppt` environment on Windows or macOS.

## Create

From the `ppt-master` skill directory:

```bash
conda env create -f environment.yml
```

If the environment already exists:

```bash
conda env update -n codex_ppt -f environment.yml --prune
```

## Verify

```bash
conda run -n codex_ppt python scripts/svg_to_pptx.py --help
conda run -n codex_ppt python scripts/project_manager.py --help
conda run -n codex_ppt ffprobe -version
conda run -n codex_ppt pandoc --version
```

For a quick import check:

```bash
conda run -n codex_ppt python -c "import pptx, cairosvg, svglib, reportlab, fitz, mammoth, markdownify, ebooklib, openpyxl, edge_tts, openai, google.genai, flask"
```

## macOS Notes

- Use the same environment name, `codex_ppt`, on macOS and Windows so workflow commands stay portable.
- On macOS arm64, keep `cairo`, `pkg-config`, and `pycairo` in the Conda dependency layer. This avoids pip building `pycairo` from source when installing `svglib` / `rlpycairo`.
- `ffmpeg` is included so `ffprobe` is available for recorded narration duration checks.
- If visual review is needed, install Playwright browser support after creating the environment:

```bash
conda run -n codex_ppt python -m pip install playwright
conda run -n codex_ppt python -m playwright install chromium
```

## Notes

- `pandoc` is included through Conda for cross-platform document conversion fallback.
- `cairosvg` is included in addition to upstream `requirements.txt` because it improves SVG-to-PNG fallback rendering for Office compatibility.
- `ffmpeg` is included for narration timing and video/audio workflows.
- API-backed image generation packages are installed, but API keys are not stored in the skill repository.
