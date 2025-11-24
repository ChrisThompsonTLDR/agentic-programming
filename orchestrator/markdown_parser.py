"""
MarkdownParser - Extracts agent definitions from markdown files.
"""
import re
from pathlib import Path
from typing import Dict, List, Optional


class MarkdownParser:
    """Parses markdown files to extract agent instructions and metadata."""
    
    def __init__(self, commands_dir: Path):
        """
        Initialize the MarkdownParser.
        
        Args:
            commands_dir: Path to the commands directory containing markdown files
        """
        self.commands_dir = Path(commands_dir)
        
    def parse_file(self, filepath: Path) -> Dict[str, any]:
        """
        Parse a single markdown file to extract agent definition.
        
        Args:
            filepath: Path to the markdown file
            
        Returns:
            Dictionary containing agent metadata and instructions
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title (first H1 heading)
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem
        
        # Extract role and mindset section
        role_section = self._extract_section(content, "Role & Mindset")
        
        # Extract preparation steps
        preparation = self._extract_section(content, "Preparation")
        
        # Extract steps
        steps = self._extract_section(content, "Steps")
        
        # Build system prompt from extracted sections
        system_prompt = self._build_system_prompt(title, role_section, preparation, steps)
        
        # Determine phase from file path
        phase = self._determine_phase(filepath)
        
        # Extract command number
        command_number = self._extract_command_number(filepath)
        
        return {
            "title": title,
            "filepath": str(filepath),
            "phase": phase,
            "command_number": command_number,
            "role_section": role_section,
            "preparation": preparation,
            "steps": steps,
            "system_prompt": system_prompt,
        }
    
    def _extract_section(self, content: str, section_name: str) -> Optional[str]:
        """Extract content under a specific section heading."""
        # Match section heading and capture content until next same-level heading
        pattern = rf'^##\s+{re.escape(section_name)}\s*$\n(.*?)(?=^##\s|\Z)'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else None
    
    def _build_system_prompt(self, title: str, role: str, preparation: str, steps: str) -> str:
        """Build a comprehensive system prompt from extracted sections."""
        prompt_parts = [f"# {title}\n"]
        
        if role:
            prompt_parts.append(f"## Role & Mindset\n{role}\n")
            
        if preparation:
            prompt_parts.append(f"## Preparation\n{preparation}\n")
            
        if steps:
            prompt_parts.append(f"## Steps\n{steps}\n")
            
        return "\n".join(prompt_parts)
    
    def _determine_phase(self, filepath: Path) -> str:
        """Determine the workflow phase from file path."""
        path_str = str(filepath)
        
        if "10-planning" in path_str:
            return "Planning"
        elif "20-roles" in path_str:
            return "Role Definition"
        elif "30-process" in path_str:
            return "Process"
        elif "40-dev" in path_str:
            return "Development"
        elif "50-final" in path_str:
            return "Finalization"
        elif "00-start" in path_str:
            return "Foundation"
        else:
            return "Unknown"
    
    def _extract_command_number(self, filepath: Path) -> Optional[str]:
        """Extract command number from filename (e.g., '22' from '22-architect.md')."""
        match = re.search(r'(\d+)-', filepath.name)
        return match.group(1) if match else None
    
    def parse_all_commands(self) -> Dict[str, Dict]:
        """
        Parse all markdown command files in the commands directory.
        
        Returns:
            Dictionary mapping command numbers to agent definitions
        """
        agents = {}
        
        # Find all markdown files recursively
        md_files = list(self.commands_dir.rglob("*.md"))
        
        for md_file in md_files:
            try:
                agent_def = self.parse_file(md_file)
                command_num = agent_def.get("command_number")
                if command_num:
                    agents[command_num] = agent_def
                else:
                    # Use filename as key if no command number
                    agents[md_file.stem] = agent_def
            except Exception as e:
                print(f"Warning: Failed to parse {md_file}: {e}")
                
        return agents
    
    def get_commands_by_phase(self) -> Dict[str, List[Dict]]:
        """
        Get all commands organized by phase.
        
        Returns:
            Dictionary mapping phase names to lists of agent definitions
        """
        all_agents = self.parse_all_commands()
        phases = {}
        
        for agent_def in all_agents.values():
            phase = agent_def.get("phase", "Unknown")
            if phase not in phases:
                phases[phase] = []
            phases[phase].append(agent_def)
            
        # Sort commands within each phase by command number
        for phase in phases:
            phases[phase].sort(key=lambda x: x.get("command_number", "99"))
            
        return phases
