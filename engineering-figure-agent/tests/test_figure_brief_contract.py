import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_figure_brief_schema_exposes_semantic_contract_and_backends():
    schema = json.loads(
        (ROOT / "schemas" / "figure-brief.schema.json").read_text(encoding="utf-8")
    )

    required = set(schema["required"])
    assert {
        "semantic_nodes",
        "semantic_edges",
        "render_graph",
        "visible_text_allowlist",
        "negative_constraints",
        "issue_ledger",
        "candidate_mode",
    } <= required

    modes = set(schema["properties"]["mode"]["enum"])
    assert {"openai-image", "drawio", "mixed"} <= modes


def test_figure_brief_template_matches_current_contract():
    template = json.loads(
        (ROOT / "templates" / "figure-brief" / "figure-brief.json").read_text(
            encoding="utf-8"
        )
    )

    assert template["mode"] in {"openai-image", "drawio", "mixed"}
    assert template["candidate_mode"] in {"single", "explore"}
    assert isinstance(template["semantic_nodes"], list)
    assert isinstance(template["semantic_edges"], list)
    assert isinstance(template["visible_text_allowlist"], list)
    assert isinstance(template["negative_constraints"], list)
    assert isinstance(template["issue_ledger"], list)
