from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from tempfile import TemporaryDirectory


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "resolve_journal_reference.py"
)
SPEC = spec_from_file_location("resolve_journal_reference", SCRIPT)
assert SPEC and SPEC.loader
RESOLVER = module_from_spec(SPEC)
SPEC.loader.exec_module(RESOLVER)


def test_finds_reference_relative_to_project():
    with TemporaryDirectory() as tmp:
        root = Path(tmp) / "Literatures"
        project = root / "project"
        others = root / "others"
        project.mkdir(parents=True)
        others.mkdir()
        reference = others / "journal_ai_reference.md"
        reference.write_text("# journals\n", encoding="utf-8")

        result = RESOLVER.resolve_reference(
            project,
            include_windows_fallback=False,
        )

        assert result["status"] == "loaded"
        assert result["source"] == "relative"
        assert result["path"] == str(reference.resolve())
        assert result["display_path"].endswith(
            str(Path("..") / "others" / "journal_ai_reference.md")
        )


def test_configured_relative_path_has_priority():
    with TemporaryDirectory() as tmp:
        project = Path(tmp) / "project"
        project.mkdir()
        reference = project / "config" / "journals.md"
        reference.parent.mkdir()
        reference.write_text("# journals\n", encoding="utf-8")

        result = RESOLVER.resolve_reference(
            project,
            configured="config/journals.md",
            include_windows_fallback=False,
        )

        assert result["status"] == "loaded"
        assert result["source"] == "project-config"


def test_returns_not_found_without_fallback():
    with TemporaryDirectory() as tmp:
        result = RESOLVER.resolve_reference(
            Path(tmp),
            include_windows_fallback=False,
        )
        assert result["status"] == "not_found"
        assert result["path"] is None
