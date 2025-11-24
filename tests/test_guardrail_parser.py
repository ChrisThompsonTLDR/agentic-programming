"""Tests for guardrail parser."""

import pytest
from pathlib import Path
from agentic_sdlc.parsers.guardrail_parser import GuardrailParser, Constraint


def test_guardrail_parser_initialization(tmp_path):
    """Test GuardrailParser initialization."""
    support_dir = tmp_path / "support"
    support_dir.mkdir()
    
    parser = GuardrailParser(support_dir)
    assert parser.support_dir == support_dir


def test_parse_forbidden_actions(tmp_path):
    """Test parsing forbidden actions."""
    support_dir = tmp_path / "support"
    support_dir.mkdir()
    
    forbidden_file = support_dir / "01-forbidden.md"
    forbidden_file.write_text("""
## Forbidden Actions

### 1. Scope and Time
- ❌ Do not make or imply **time estimates**.
- ❌ Do not invent **scope**, features, or requirements.

### 2. Code Generation
- ❌ No code emission in any `expand-*` file.
""")
    
    parser = GuardrailParser(support_dir)
    constraints = parser.parse_forbidden_actions()
    
    assert len(constraints) > 0
    assert all(c.type == "forbidden" for c in constraints)
    assert any("time estimates" in c.description for c in constraints)


def test_parse_required_actions(tmp_path):
    """Test parsing required actions."""
    support_dir = tmp_path / "support"
    support_dir.mkdir()
    
    forbidden_file = support_dir / "01-forbidden.md"
    forbidden_file.write_text("""
## Global Principles
- ✅ Truth over assumption: all data must trace to PRD.
- ✅ No invention: AI must never create new requirements.
""")
    
    parser = GuardrailParser(support_dir)
    constraints = parser.parse_required_actions()
    
    assert len(constraints) > 0
    assert all(c.type == "required" for c in constraints)


def test_get_forbidden_patterns(tmp_path):
    """Test extracting forbidden patterns."""
    support_dir = tmp_path / "support"
    support_dir.mkdir()
    
    forbidden_file = support_dir / "01-forbidden.md"
    forbidden_file.write_text("""
## Forbidden Actions

### 1. Scope and Time
- ❌ Do not make or imply **time estimates**.
- ❌ Do not invent **scope**.

### 2. Code Generation
- ❌ No code generation in planning phases.

### 3. Security
- ❌ Never expose credentials or tokens.
""")
    
    parser = GuardrailParser(support_dir)
    patterns = parser.get_forbidden_patterns()
    
    assert "time_estimation" in patterns
    assert "scope_invention" in patterns
    assert "premature_code_generation" in patterns
    assert "credential_exposure" in patterns
