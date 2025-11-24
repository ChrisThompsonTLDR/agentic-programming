"""Guardrail parser to extract constraints from support files."""

import re
from pathlib import Path
from typing import List, Set
from dataclasses import dataclass


@dataclass
class Constraint:
    """A single constraint rule."""
    
    type: str  # "forbidden" or "required"
    category: str  # e.g., "Scope and Time", "Code Generation"
    description: str
    severity: str  # "critical", "high", "medium"


class GuardrailParser:
    """Parse forbidden.md and rules.md to extract constraints."""
    
    def __init__(self, support_dir: Path):
        """Initialize parser with support directory."""
        self.support_dir = Path(support_dir)
        
    def parse_forbidden_actions(self) -> List[Constraint]:
        """Parse forbidden.md to extract prohibited actions."""
        forbidden_file = self.support_dir / "01-forbidden.md"
        if not forbidden_file.exists():
            return []
        
        content = forbidden_file.read_text()
        constraints = []
        
        # Extract sections from "Forbidden Actions"
        forbidden_section = self._extract_section(content, "Forbidden Actions")
        if forbidden_section:
            constraints.extend(self._parse_forbidden_section(forbidden_section))
        
        return constraints
    
    def parse_required_actions(self) -> List[Constraint]:
        """Parse forbidden.md to extract required actions (marked with ✅)."""
        forbidden_file = self.support_dir / "01-forbidden.md"
        if not forbidden_file.exists():
            return []
        
        content = forbidden_file.read_text()
        constraints = []
        
        # Extract all ✅ items
        required_pattern = r'- ✅ (.+?)(?:\n|$)'
        for match in re.finditer(required_pattern, content):
            constraints.append(
                Constraint(
                    type="required",
                    category="Global Principles",
                    description=match.group(1).strip(),
                    severity="high",
                )
            )
        
        return constraints
    
    def parse_quality_gates(self) -> List[Constraint]:
        """Parse quality gate requirements."""
        forbidden_file = self.support_dir / "01-forbidden.md"
        if not forbidden_file.exists():
            return []
        
        content = forbidden_file.read_text()
        constraints = []
        
        # Extract Metrics and Validation section
        metrics_section = self._extract_section(content, "Metrics and Validation")
        if metrics_section:
            # Extract quality gate requirements
            gate_pattern = r'([A-Za-z]+):\s*(.+?)(?:\n|$)'
            for match in re.finditer(gate_pattern, metrics_section):
                tool_name = match.group(1).strip()
                requirement = match.group(2).strip()
                constraints.append(
                    Constraint(
                        type="required",
                        category="Quality Gates",
                        description=f"{tool_name}: {requirement}",
                        severity="critical",
                    )
                )
        
        return constraints
    
    def get_all_constraints(self) -> List[Constraint]:
        """Get all constraints from support files."""
        constraints = []
        constraints.extend(self.parse_forbidden_actions())
        constraints.extend(self.parse_required_actions())
        constraints.extend(self.parse_quality_gates())
        return constraints
    
    def get_forbidden_patterns(self) -> Set[str]:
        """Extract forbidden action patterns for validation."""
        patterns = set()
        
        for constraint in self.parse_forbidden_actions():
            # Extract key forbidden terms
            desc_lower = constraint.description.lower()
            
            # Common forbidden patterns
            if "time estimate" in desc_lower:
                patterns.add("time_estimation")
            if "scope" in desc_lower and "invent" in desc_lower:
                patterns.add("scope_invention")
            if "code" in desc_lower and ("emission" in desc_lower or "planning" in desc_lower or "expand" in desc_lower or "generation" in desc_lower):
                patterns.add("premature_code_generation")
            if "next steps" in desc_lower or "recommendations" in desc_lower or "recommendation" in desc_lower:
                patterns.add("unsolicited_recommendations")
            if "credential" in desc_lower or "secret" in desc_lower or "token" in desc_lower or "expose" in desc_lower:
                patterns.add("credential_exposure")
        
        return patterns
    
    def _extract_section(self, content: str, section_name: str) -> str:
        """Extract content of a specific section."""
        # Match section header - look for ## followed by section name
        # Then capture everything until the next ## (not ###) or end of string
        pattern = rf'##\s+{re.escape(section_name)}\s*\n(.*?)(?=\n##\s+[^#]|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        
        return ""
    
    def _parse_forbidden_section(self, section: str) -> List[Constraint]:
        """Parse the Forbidden Actions section."""
        constraints = []
        current_category = "General"
        
        # Split by subsections (### headers)
        subsection_pattern = r'###\s+\d+\.\s+(.+?)\n(.*?)(?=\n###|\Z)'
        
        for match in re.finditer(subsection_pattern, section, re.DOTALL):
            category = match.group(1).strip()
            subsection_content = match.group(2).strip()
            
            # Extract all ❌ items
            forbidden_pattern = r'- ❌ (.+?)(?:\n|$)'
            for item_match in re.finditer(forbidden_pattern, subsection_content):
                description = item_match.group(1).strip()
                
                # Determine severity based on content
                severity = "high"
                if any(word in description.lower() for word in ["never", "must not", "security"]):
                    severity = "critical"
                
                constraints.append(
                    Constraint(
                        type="forbidden",
                        category=category,
                        description=description,
                        severity=severity,
                    )
                )
        
        return constraints
