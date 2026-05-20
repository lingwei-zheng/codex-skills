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
```

## Notes

- `pandoc` is included through Conda for cross-platform document conversion fallback.
- `cairosvg` is included in addition to upstream `requirements.txt` because it improves SVG-to-PNG fallback rendering for Office compatibility.
- API-backed image generation packages are installed, but API keys are not stored in the skill repository.
