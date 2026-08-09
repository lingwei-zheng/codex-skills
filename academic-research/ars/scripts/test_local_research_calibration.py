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


def test_association_language_uses_one_sufficient_boundary():
    calibration = read("shared/research-calibration.md")
    polishing = read("nature-polishing/SKILL.md")
    protected = read(
        "academic-research/ars/shared/references/"
        "protected_hedging_phrases.md"
    )
    assert "Causal Language Economy" in calibration
    assert "accurate associational verb as a sufficient causal boundary" in polishing
    assert "Minimal sufficient inclusion" in protected
    assert "Conservative inclusion." not in protected


def test_spatial_diagnostics_are_claim_triggered():
    calibration = read("shared/research-calibration.md")
    spatial = read("shared/field-context/spatial-methods.md")
    stats = read(
        "academic-research/ars/experiment-agent/references/"
        "statistical_interpretation_guide.md"
    )
    assert "Diagnostics are a menu" in calibration
    assert "coordinates alone do not require a spatial model" in spatial
    assert "MGWR is not inherently preferable to GWR" in spatial
    assert "Check ALL 11 types" not in stats
    assert "Triggered Fallacy Scan" in stats


def test_selective_quality_control_is_loaded():
    router = read("academic-research/SKILL.md")
    quality = read("academic-research/references/selective-quality-control.md")
    writer = read(
        "academic-research/ars/academic-paper/agents/draft_writer_agent.md"
    )
    reviewer = read("peer-review/SKILL.md")
    report = read("peer-review/references/report-structure.md")
    assert "selective-quality-control.md" in router
    assert "Impact-First Checks" in quality
    assert "recalibrate the final Introduction" in quality
    assert "TEEL is one useful diagnostic" in writer
    assert "do not manufacture one" in reviewer
    assert "zero or one issue" in report


def test_upstream_selective_backports_are_present():
    good_question = read("good-question/SKILL.md")
    first_principles = read(
        "good-question/references/first-principles-lens.md"
    )
    nature_figure = read("nature-figure/SKILL.md")
    legend = read("nature-figure/references/figure-legend-contract.md")
    assert "first-principles-lens.md" in good_question
    assert "calibration layer" in first_principles
    assert "figure-legend-contract.md" in nature_figure
    assert "Source Data Wording" in legend


def test_journal_targeting_loads_local_reference_by_default():
    advisor = read("academic-advisor/SKILL.md")
    protocol = read(
        "academic-advisor/references/local-journal-reference.md"
    )
    rubric = read("academic-advisor/references/journal-fit-rubric.md")
    template = read("academic-advisor/templates/integrated-advisor-report.md")
    project_yaml = read("sync/references/project-yaml-template.yaml")
    assert "local-journal-reference.md" in advisor
    assert "../others/journal_ai_reference.md" in protocol
    assert "CODEX_JOURNAL_REFERENCE" in protocol
    assert "Windows-only fallback" in protocol
    assert "resolve_journal_reference.py" in advisor
    assert "resolve_journal_reference.py" in protocol
    assert "local-journal-reference.md" in rubric
    assert "本地期刊参考" in template
    assert "journal_reference" in project_yaml
