from pathlib import Path


SKILLS_ROOT = Path(__file__).resolve().parents[3]


def read(path: str) -> str:
    return (SKILLS_ROOT / path).read_text(encoding="utf-8")


def test_shared_calibration_defaults_are_stable():
    calibration = read("shared/research-calibration.md")
    assert "research_stage: first-draft" in calibration
    assert "rigor_profile: proportionate" in calibration
    assert "contribution_profile: incremental-allowed" in calibration
    assert "compute_profile: balanced" in calibration


def test_research_entry_points_load_calibration():
    for path in (
        "academic-research/SKILL.md",
        "academic-advisor/SKILL.md",
        "good-question/SKILL.md",
        "peer-review/SKILL.md",
    ):
        assert "research-calibration.md" in read(path), path


def test_first_draft_does_not_require_exhaustive_robustness():
    workflow = read("academic-research/ars/experiment-agent/WORKFLOW.md")
    assert "All 11 must be checked" not in workflow
    assert "at most two additional checks" in workflow
    assert "Record other checks as deferred" in workflow


def test_runtime_contract_detects_low_utilization():
    runner = read(
        "academic-research/ars/experiment-agent/agents/code_runner_agent.md"
    )
    protocol = read(
        "academic-research/ars/experiment-agent/references/"
        "stall_detection_protocol.md"
    )
    assert "LOW_UTILIZATION" in runner
    assert "LOW_UTILIZATION" in protocol
    assert "THROUGHPUT_REGRESSION" in protocol


def test_geography_uses_location_value_not_location_veto():
    readiness = read(
        "shared/field-context/geography-publication-readiness.md"
    )
    question_agent = read(
        "academic-research/ars/deep-research/agents/"
        "research_question_agent.md"
    )
    assert "location-value check" in readiness.lower()
    assert "location-value check" in question_agent.lower()
    assert "location-swap gate" not in question_agent.lower()
