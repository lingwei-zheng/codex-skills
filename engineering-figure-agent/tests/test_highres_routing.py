"""Exercise model selection offline; no API keys or paid generation calls."""

import argparse
import importlib.util
import json
import shutil
import subprocess
from pathlib import Path

import pytest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
spec = importlib.util.spec_from_file_location("image_routing", SCRIPTS / "generate_image.py")
image_routing = importlib.util.module_from_spec(spec)
spec.loader.exec_module(image_routing)


@pytest.fixture
def model_environment(monkeypatch):
    monkeypatch.setenv("NANOBANANA_DEFAULT_MODEL", "routine-gemini")
    monkeypatch.setenv("NANOBANANA_MODEL", "routine-gemini")
    monkeypatch.setenv("OPENAI_IMAGE_MODEL", "routine-openai")
    monkeypatch.delenv("NANOBANANA_HIGHRES_MODEL", raising=False)
    monkeypatch.delenv("OPENAI_IMAGE_HIGHRES_MODEL", raising=False)


@pytest.mark.parametrize("prompt,highres,requires_highres", [
    ("Final export of the framework", False, False),
    ("Final-export figure with readable labels", False, False),
    ("Final quality illustration", False, False),
    ("Export an editable SVG and PDF", False, False),
    ("Final export at 2K", False, True),
    ("High resolution illustration", False, True),
    ("High-res illustration", False, True),
    ("Routine prompt with explicit flag", True, True),
])
def test_python_and_javascript_choose_same_route(prompt, highres, requires_highres, model_environment):
    args = argparse.Namespace(prompt=prompt, highres=highres, model=None,
                              style_note=None, prompt_file=None)
    assert image_routing.is_explicit_highres_request(args) is requires_highres
    for resolver, normal in [(image_routing.resolve_model, "routine-gemini"),
                             (image_routing.resolve_openai_model, "routine-openai")]:
        if requires_highres:
            with pytest.raises(SystemExit, match="HIGHRES_MODEL is not configured"):
                resolver(args)
        else:
            assert resolver(args) == normal

    node = shutil.which("node")
    if node is None:
        pytest.skip("Node is not installed; Python route checked")
    code = """
const routing = require(process.argv[1]);
const args = JSON.parse(process.argv[2]);
try { console.log(JSON.stringify({model: routing.resolveModel(args)})); }
catch (error) { console.log(JSON.stringify({error: error.message})); }
"""
    result = subprocess.run([node, "-e", code, str(SCRIPTS / "generate_image.js"),
                             json.dumps({"prompt": prompt, "highres": highres})],
                            capture_output=True, text=True, encoding="utf-8", check=True)
    data = json.loads(result.stdout)
    if requires_highres:
        assert "NANOBANANA_HIGHRES_MODEL is not configured" in data["error"]
    else:
        assert data == {"model": "routine-gemini"}


def test_explicit_resolution_in_prompt_file_still_requires_highres(tmp_path, model_environment):
    prompt_file = tmp_path / "brief.txt"
    prompt_file.write_text("Final export at high resolution", encoding="utf-8")
    args = argparse.Namespace(prompt="", highres=False, model=None,
                              style_note=None, prompt_file=str(prompt_file))
    with pytest.raises(SystemExit, match="HIGHRES_MODEL is not configured"):
        image_routing.resolve_model(args)


def test_configured_highres_route_and_named_model_are_preserved(monkeypatch, model_environment):
    monkeypatch.setenv("NANOBANANA_HIGHRES_MODEL", "explicit-highres")
    monkeypatch.setenv("OPENAI_IMAGE_HIGHRES_MODEL", "explicit-openai-highres")
    args = argparse.Namespace(prompt="2K illustration", highres=True, model=None,
                              style_note=None, prompt_file=None)
    assert image_routing.resolve_model(args) == "explicit-highres"
    assert image_routing.resolve_openai_model(args) == "explicit-openai-highres"
    args.model = "user-selected-model"
    assert image_routing.resolve_model(args) == "user-selected-model"
    assert image_routing.resolve_openai_model(args) == "user-selected-model"
