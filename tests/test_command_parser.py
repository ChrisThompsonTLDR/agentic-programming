"""Tests for command parser."""

import pytest
from pathlib import Path
from agentic_sdlc.parsers.command_parser import CommandParser, AgentSpec


def test_command_parser_initialization(tmp_path):
    """Test CommandParser initialization."""
    commands_dir = tmp_path / "commands"
    commands_dir.mkdir()
    
    parser = CommandParser(commands_dir)
    assert parser.commands_dir == commands_dir


def test_parse_command_file(tmp_path):
    """Test parsing a single command file."""
    commands_dir = tmp_path / "commands"
    commands_dir.mkdir()
    
    # Create a sample command file
    command_file = commands_dir / "11-discuss.md"
    command_file.write_text("""# Begin Epic Discussion

## Role & Mindset

You will act as a **Product Manager** initiating structured discovery.

## Preparation

1. **Read all files in `.cursor/support`**.
2. **Determine working epic.**

## Steps

1. **Initiate Conversation**
2. **Q and A**
3. **Generate Discussion Artifact**
""")
    
    parser = CommandParser(commands_dir)
    spec = parser.parse_command_file(command_file)
    
    assert spec is not None
    assert spec.id == "11-discuss"
    assert spec.name == "Product Manager"
    assert spec.phase == "planning"
    assert spec.phase_number == 11
    assert len(spec.preparation) > 0
    assert len(spec.steps) > 0


def test_parse_all_commands(tmp_path):
    """Test parsing all command files."""
    commands_dir = tmp_path / "commands"
    planning_dir = commands_dir / "10-planning"
    planning_dir.mkdir(parents=True)
    
    # Create multiple command files
    (planning_dir / "11-discuss.md").write_text("""
# Test
## Role & Mindset
You are a **Product Manager**.
""")
    
    (planning_dir / "12-idea.md").write_text("""
# Test
## Role & Mindset
You are an **Innovation Lead**.
""")
    
    parser = CommandParser(commands_dir)
    agents = parser.parse_all_commands()
    
    assert len(agents) == 2
    assert "11-discuss" in agents
    assert "12-idea" in agents


def test_get_pipeline_order(tmp_path):
    """Test getting agents in pipeline order."""
    commands_dir = tmp_path / "commands"
    commands_dir.mkdir()
    
    # Create command files with different phases
    (commands_dir / "00-start.md").write_text("# Start\n## Role & Mindset\nYou are a **Starter**.")
    
    planning_dir = commands_dir / "10-planning"
    planning_dir.mkdir()
    (planning_dir / "11-discuss.md").write_text("# Discuss\n## Role & Mindset\nYou are a **PM**.")
    
    parser = CommandParser(commands_dir)
    agents = parser.parse_all_commands()
    order = parser.get_pipeline_order(agents)
    
    assert order[0] == "00-start"
    assert order[1] == "11-discuss"
