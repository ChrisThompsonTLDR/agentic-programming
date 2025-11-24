"""Command file parser to extract agent specifications."""

import re
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class AgentSpec:
    """Specification for an agent extracted from a command file."""
    
    id: str  # e.g., "11-discuss"
    name: str  # e.g., "Product Manager"
    phase: str  # e.g., "planning"
    phase_number: int  # e.g., 10
    role: str  # Extracted from "Role & Mindset" section
    preparation: List[str]  # Steps from "Preparation" section
    steps: List[str]  # Steps from "Steps" section
    file_path: Path
    raw_content: str


class CommandParser:
    """Parse markdown command files to extract agent specifications."""
    
    PHASE_MAP = {
        "00": "foundation",
        "10": "planning",
        "20": "roles",
        "30": "process",
        "40": "development",
        "50": "finalization",
        "99": "operations",
    }
    
    def __init__(self, commands_dir: Path):
        """Initialize parser with commands directory."""
        self.commands_dir = Path(commands_dir)
        
    def parse_all_commands(self) -> Dict[str, AgentSpec]:
        """Parse all command files and return agent specifications."""
        agents = {}
        
        for md_file in self.commands_dir.rglob("*.md"):
            if md_file.is_file():
                agent_spec = self.parse_command_file(md_file)
                if agent_spec:
                    agents[agent_spec.id] = agent_spec
                    
        return agents
    
    def parse_command_file(self, file_path: Path) -> Optional[AgentSpec]:
        """Parse a single command file."""
        try:
            content = file_path.read_text()
            
            # Extract agent ID from filename
            agent_id = file_path.stem
            
            # Determine phase from first 1-2 digits
            phase_prefix = agent_id.split("-")[0] if "-" in agent_id else "00"
            
            # Map to phase using first digit(s)
            # 00 -> foundation, 10-19 -> planning, 20-29 -> roles, etc.
            if phase_prefix.startswith("0") and phase_prefix != "00":
                phase_key = "00"  # 01-09 -> foundation
            elif len(phase_prefix) >= 2:
                phase_key = phase_prefix[0] + "0"  # 11 -> 10, 23 -> 20, etc.
            else:
                phase_key = phase_prefix
            
            phase = self.PHASE_MAP.get(phase_key, "unknown")
            
            try:
                phase_number = int(phase_prefix)
            except ValueError:
                phase_number = 0
            
            # Extract agent name/role from "Role & Mindset" section
            name = self._extract_agent_name(content)
            role = self._extract_role(content)
            
            # Extract preparation steps
            preparation = self._extract_section_items(content, "Preparation")
            
            # Extract execution steps
            steps = self._extract_section_items(content, "Steps")
            
            return AgentSpec(
                id=agent_id,
                name=name,
                phase=phase,
                phase_number=phase_number,
                role=role,
                preparation=preparation,
                steps=steps,
                file_path=file_path,
                raw_content=content,
            )
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None
    
    def _extract_agent_name(self, content: str) -> str:
        """Extract agent name from content."""
        # Look for patterns like "You are a **Product Manager**"
        match = re.search(r'You (?:are|will act as) a \*\*([^*]+)\*\*', content)
        if match:
            return match.group(1)
        
        # Fall back to first heading
        match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if match:
            return match.group(1)
        
        return "Unknown Agent"
    
    def _extract_role(self, content: str) -> str:
        """Extract full role description from Role & Mindset section."""
        role_section = self._extract_section(content, "Role & Mindset")
        if role_section:
            # Clean up markdown formatting
            role = role_section.strip()
            role = re.sub(r'\*\*', '', role)  # Remove bold markers
            return role
        
        return "No role description available"
    
    def _extract_section(self, content: str, section_name: str) -> Optional[str]:
        """Extract content of a specific section."""
        # Match section header
        pattern = rf'##\s+{re.escape(section_name)}\s*\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        
        return None
    
    def _extract_section_items(self, content: str, section_name: str) -> List[str]:
        """Extract numbered or bulleted items from a section."""
        section = self._extract_section(content, section_name)
        if not section:
            return []
        
        items = []
        
        # Extract numbered items (1. , 2. , etc.)
        numbered_pattern = r'^\s*\d+\.\s+\*\*(.+?)\*\*'
        for match in re.finditer(numbered_pattern, section, re.MULTILINE):
            items.append(match.group(1))
        
        # If no numbered items, try bullet points
        if not items:
            bullet_pattern = r'^\s*[-*]\s+(.+)$'
            for match in re.finditer(bullet_pattern, section, re.MULTILINE):
                items.append(match.group(1).strip())
        
        return items
    
    def get_pipeline_order(self, agents: Dict[str, AgentSpec]) -> List[str]:
        """Get agents in pipeline execution order."""
        # Sort by phase number and then by ID
        sorted_agents = sorted(
            agents.values(),
            key=lambda a: (a.phase_number, a.id)
        )
        return [agent.id for agent in sorted_agents]
