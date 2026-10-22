from pathlib import Path


SKILLS_ROOT = Path(__file__).resolve().parents[3]


def read(path: str) -> str:
    return (SKILLS_ROOT / path).read_text(encoding="utf-8")


def test_retired_shared_policy_has_no_remaining_markdown_callers():
    """Prevent a dangling load or a bundled replacement of project policy."""
    retired = "research-calibration.md"
    assert not (SKILLS_ROOT / "shared" / retired).exists()
    assert not list(SKILLS_ROOT.rglob("SCIENTIFIC_EXPLORATION_PROTOCOL.md"))
    for path in SKILLS_ROOT.rglob("*.md"):
        assert retired not in path.read_text(encoding="utf-8-sig"), path


def test_scientific_decision_routes_reference_project_protocol():
    for path in (
        "academic-research/SKILL.md",
        "academic-advisor/SKILL.md",
        "good-question/SKILL.md",
        "good-story/SKILL.md",
        "sync/SKILL.md",
        "academic-research/ars/deep-research/WORKFLOW.md",
        "academic-research/ars/experiment-agent/WORKFLOW.md",
        "academic-research/ars/academic-pipeline/WORKFLOW.md",
    ):
        assert "SCIENTIFIC_EXPLORATION_PROTOCOL.md" in read(path), path


def test_validation_checks_remain_claim_triggered():
    workflow = read("academic-research/ars/experiment-agent/WORKFLOW.md")
    assert "All 11 must be checked" not in workflow
    assert "Check every pattern triggered by the design and claim" in workflow


def test_simulation_reference_is_reachable_from_active_routes():
    """Check routing integrity, not the quality of scientific judgments."""
    relative = "references/simulation-method-validation.md"
    workflow_dir = SKILLS_ROOT / "academic-research/ars/experiment-agent"
    assert (workflow_dir / relative).is_file()
    assert relative in (workflow_dir / "WORKFLOW.md").read_text(encoding="utf-8")
    architect_dir = SKILLS_ROOT / "academic-research/ars/deep-research/agents"
    architect_ref = "../../experiment-agent/" + relative
    assert architect_ref in (architect_dir / "research_architect_agent.md").read_text(
        encoding="utf-8"
    )
    assert (architect_dir / architect_ref).resolve() == (workflow_dir / relative).resolve()


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
    polishing = read("nature-polishing/SKILL.md")
    protected = read(
        "academic-research/ars/shared/references/"
        "protected_hedging_phrases.md"
    )
    assert "accurate associational verb as a sufficient causal boundary" in polishing
    assert "Minimal sufficient inclusion" in protected
    assert "Conservative inclusion." not in protected


def test_spatial_diagnostics_are_claim_triggered():
    spatial = read("shared/field-context/spatial-methods.md")
    stats = read(
        "academic-research/ars/experiment-agent/references/"
        "statistical_interpretation_guide.md"
    )
    assert "Diagnostics And Robustness Menu" in spatial
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


def test_author_side_skills_use_advantage_led_narrative():
    protocol = read("shared/advantage-led-research-narrative.md")
    assert "Lead With the Advantage" in protocol
    assert "Choose the Winning Arena" in protocol
    assert "Give Every Analysis One Argument Job" in protocol
    assert "Integrity Floor" in protocol

    for path in (
        "academic-research/SKILL.md",
        "academic-advisor/SKILL.md",
        "good-question/SKILL.md",
        "good-story/SKILL.md",
    ):
        assert "advantage-led-research-narrative.md" in read(path), path


def test_reviewer_risk_is_conditional_for_author_work():
    question = read("good-question/SKILL.md")
    advisor = read("academic-advisor/references/advisor-rubric.md")
    story = read("good-story/SKILL.md")
    assert "mandatory author-side output" in question
    assert "Run a full reviewer-risk analysis for" in advisor
    assert "Do not append a generic weakness inventory" in story
    assert "`Weak points`: what would make reviewers resist" not in story


def test_paper_workflow_uses_argument_jobs_and_conditional_limits():
    workflow = read("academic-research/ars/academic-paper/WORKFLOW.md")
    architect = read(
        "academic-research/ars/academic-paper/agents/structure_architect_agent.md"
    )
    writer = read(
        "academic-research/ars/academic-paper/agents/draft_writer_agent.md"
    )
    formatter = read(
        "academic-research/ars/academic-paper/agents/formatter_agent.md"
    )
    assert "Reviewer-first narrative" in workflow
    assert "Advantage Narrative Brief" in architect
    assert "final evidence logic rather than the project's chronology" in writer
    assert "standalone section conditional" in formatter
    assert "unresolved items become Acknowledged Limitations" not in workflow


def test_polishing_removes_self_undermining_comparisons():
    skill = read("nature-polishing/SKILL.md")
    defensive = read("nature-polishing/references/defensive-phrasing.md")
    assert "self-undermining comparison language" in skill
    assert "responsibility-expansion test" in defensive
    assert "Never use positive reframing to hide a failed primary outcome" in defensive
