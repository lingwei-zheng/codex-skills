"""Fixture ownership regressions, including Windows nested paths."""
from scripts.check_v3_6_6_ab_manifest import _check_reverse_scan


def test_declared_nested_fixture_is_not_an_orphan(tmp_path):
    nested = tmp_path / "baseline" / "paper A" / "draft.md"
    nested.parent.mkdir(parents=True)
    nested.write_text("Draft evidence\n", encoding="utf-8")
    (tmp_path / "manifest.yaml").write_text("# manifest\n", encoding="utf-8")
    manifest = {"papers": [{"baseline_output": {
        "writer_draft": "baseline/paper A/draft.md"
    }}]}
    assert _check_reverse_scan(manifest, tmp_path) == []


def test_unlisted_nested_fixture_remains_an_error(tmp_path):
    nested = tmp_path / "treatment" / "paper B" / "unexpected.md"
    nested.parent.mkdir(parents=True)
    nested.write_text("Unowned evidence\n", encoding="utf-8")
    errors = _check_reverse_scan({"papers": []}, tmp_path)
    assert len(errors) == 1
    assert "treatment/paper B/unexpected.md" in errors[0]
