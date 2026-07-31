from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_skill.py"
SPEC = importlib.util.spec_from_file_location("audit_skill", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


def make_skill(root: Path) -> None:
    (root / "SKILL.md").write_text(
        "---\nname: sample\ndescription: Sample skill.\n---\n\n# Sample\n",
        encoding="utf-8",
    )


def test_flags_unsafe_python_and_missing_validation():
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_skill(root)
        scripts = root / "scripts"
        scripts.mkdir()
        (scripts / "runner.py").write_text(
            "def run(value):\n    return eval(value)\n",
            encoding="utf-8",
        )
        issues = AUDIT.audit_skill_dir(root)
        assert any("unsafe eval" in issue for issue in issues)
        assert any("no deterministic test" in issue for issue in issues)


def test_accepts_script_with_test():
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_skill(root)
        scripts = root / "scripts"
        scripts.mkdir()
        (scripts / "runner.py").write_text(
            "def run(value):\n    return value.strip()\n",
            encoding="utf-8",
        )
        tests = root / "tests"
        tests.mkdir()
        (tests / "test_runner.py").write_text(
            "def test_runner():\n    assert True\n",
            encoding="utf-8",
        )
        issues = AUDIT.audit_skill_dir(root)
        assert not any("no deterministic test" in issue for issue in issues)


def test_flags_broken_local_markdown_link():
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_skill(root)
        with (root / "SKILL.md").open("a", encoding="utf-8") as handle:
            handle.write("[missing](references/missing.md)\n")
        issues = AUDIT.audit_skill_dir(root)
        assert any("broken local link" in issue for issue in issues)


def test_ignores_example_links_inside_code_fences():
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_skill(root)
        with (root / "SKILL.md").open("a", encoding="utf-8") as handle:
            handle.write("```markdown\n[example](references/example.md)\n```\n")
        issues = AUDIT.audit_skill_dir(root)
        assert not any("broken local link" in issue for issue in issues)
