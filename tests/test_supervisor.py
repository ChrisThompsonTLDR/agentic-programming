"""Tests for guardrail supervisor."""

import pytest
from pathlib import Path
from agentic_sdlc.parsers.guardrail_parser import GuardrailParser
from agentic_sdlc.guardrails.supervisor import GuardrailSupervisor


@pytest.fixture
def supervisor(tmp_path):
    """Create a supervisor with test constraints."""
    support_dir = tmp_path / "support"
    support_dir.mkdir()
    
    forbidden_file = support_dir / "01-forbidden.md"
    forbidden_file.write_text("""
## Forbidden Actions

### 1. Scope and Time
- ❌ Do not make or imply **time estimates**.
- ❌ Do not invent **scope**.

### 2. Code Generation
- ❌ No code emission in planning phases.

### 3. Output Formatting
- ❌ Never include "Next steps" in output.

### 4. Security
- ❌ Never expose credentials or tokens.
""")
    
    parser = GuardrailParser(support_dir)
    return GuardrailSupervisor(parser)


def test_validate_agent_input_time_estimation(supervisor):
    """Test validation catches time estimation in input."""
    result = supervisor.validate_agent_input(
        "11-discuss",
        "How long will this take? I estimate 2 weeks."
    )
    
    assert not result.passed
    assert len(result.violations) > 0
    assert any("time estimation" in v.lower() for v in result.violations)


def test_validate_agent_input_valid(supervisor):
    """Test validation passes for valid input."""
    result = supervisor.validate_agent_input(
        "11-discuss",
        "Let's discuss the requirements for the new feature."
    )
    
    assert result.passed
    assert len(result.violations) == 0


def test_validate_agent_output_unsolicited_recommendations(supervisor):
    """Test validation catches unsolicited recommendations."""
    result = supervisor.validate_agent_output(
        "11-discuss",
        "Here are the results.\n\nNext steps:\n1. Do this\n2. Do that",
        "planning"
    )
    
    assert not result.passed
    assert len(result.violations) > 0
    assert any("next steps" in v.lower() for v in result.violations)


def test_validate_agent_output_premature_code(supervisor):
    """Test validation catches premature code generation."""
    result = supervisor.validate_agent_output(
        "11-discuss",
        "Here's the plan:\n\n```python\nclass User:\n    pass\n```",
        "planning"
    )
    
    assert not result.passed
    assert len(result.violations) > 0
    assert any("code generation" in v.lower() for v in result.violations)


def test_validate_agent_output_credential_exposure(supervisor):
    """Test validation catches credential exposure."""
    result = supervisor.validate_agent_output(
        "42-code",
        "Set your API_KEY='sk-abc123456789'",
        "development"
    )
    
    assert not result.passed
    assert len(result.violations) > 0
    assert any("credential" in v.lower() for v in result.violations)


def test_validate_agent_output_valid(supervisor):
    """Test validation passes for valid output."""
    result = supervisor.validate_agent_output(
        "11-discuss",
        "The discussion path is .taskmaster/epics/001/01-discuss.md",
        "planning"
    )
    
    assert result.passed
    assert len(result.violations) == 0
