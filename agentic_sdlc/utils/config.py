"""Configuration management for the orchestrator."""

from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass
import json
import os


@dataclass
class OrchestratorConfig:
    """Configuration for the SDLC orchestrator."""
    
    # Paths
    repo_path: Path
    commands_dir: Path
    support_dir: Path
    output_dir: Path
    
    # OpenAI
    openai_api_key: str
    openai_model: str = "gpt-4o"
    
    # MCP
    mcp_config: Dict[str, Any] = None
    
    # Execution
    interactive_mode: bool = False
    validate_inputs: bool = True
    validate_outputs: bool = True
    
    # Logging
    log_level: str = "INFO"
    log_file: Optional[Path] = None
    
    @classmethod
    def from_file(cls, config_file: Path) -> "OrchestratorConfig":
        """Load configuration from a JSON file."""
        with open(config_file) as f:
            data = json.load(f)
        
        return cls(
            repo_path=Path(data.get("repo_path", ".")),
            commands_dir=Path(data.get("commands_dir", "commands")),
            support_dir=Path(data.get("support_dir", "support")),
            output_dir=Path(data.get("output_dir", ".taskmaster/epics")),
            openai_api_key=data.get("openai_api_key", os.getenv("OPENAI_API_KEY", "")),
            openai_model=data.get("openai_model", "gpt-4o"),
            mcp_config=data.get("mcp_config"),
            interactive_mode=data.get("interactive_mode", False),
            validate_inputs=data.get("validate_inputs", True),
            validate_outputs=data.get("validate_outputs", True),
            log_level=data.get("log_level", "INFO"),
            log_file=Path(data["log_file"]) if "log_file" in data else None,
        )
    
    @classmethod
    def from_defaults(cls, repo_path: Path = None) -> "OrchestratorConfig":
        """Create configuration with default values."""
        repo_path = Path(repo_path or ".")
        
        return cls(
            repo_path=repo_path,
            commands_dir=repo_path / "commands",
            support_dir=repo_path / "support",
            output_dir=repo_path / ".taskmaster" / "epics",
            openai_api_key=os.getenv("OPENAI_API_KEY", ""),
            openai_model="gpt-4o",
            mcp_config=None,
        )
    
    def validate(self) -> list[str]:
        """Validate configuration and return list of errors."""
        errors = []
        
        if not self.repo_path.exists():
            errors.append(f"Repository path does not exist: {self.repo_path}")
        
        if not self.commands_dir.exists():
            errors.append(f"Commands directory does not exist: {self.commands_dir}")
        
        if not self.support_dir.exists():
            errors.append(f"Support directory does not exist: {self.support_dir}")
        
        if not self.openai_api_key:
            errors.append("OpenAI API key is required")
        
        return errors
