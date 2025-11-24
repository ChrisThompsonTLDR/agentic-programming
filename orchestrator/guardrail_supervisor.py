"""
GuardrailSupervisor - Validates agent actions against constraints.
"""
from pathlib import Path
from typing import Dict, Any, List
import re


class GuardrailSupervisor:
    """Enforces constraints and guardrails on agent actions."""
    
    def __init__(self, forbidden_md_path: Path):
        """
        Initialize the GuardrailSupervisor.
        
        Args:
            forbidden_md_path: Path to support/01-forbidden.md
        """
        self.forbidden_md_path = Path(forbidden_md_path)
        self.constraints = self._load_constraints()
        
    def _load_constraints(self) -> Dict[str, Any]:
        """Load all constraints from the forbidden.md file."""
        with open(self.forbidden_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        return {
            "global_principles": self._extract_global_principles(content),
            "forbidden_actions": self._extract_forbidden_actions(content),
            "output_rules": self._extract_output_rules(content),
            "security_rules": self._extract_security_rules(content),
            "mcp_rules": self._extract_mcp_rules(content),
            "metrics_gates": self._extract_metrics_gates(content),
        }
    
    def _extract_global_principles(self, content: str) -> List[Dict[str, str]]:
        """Extract global principles from the forbidden.md."""
        principles = []
        
        # Look for bullet points under "Global Principles"
        section = self._extract_section(content, "Global Principles")
        if section:
            matches = re.findall(r'[-*]\s+\*\*([^:]+):\*\*\s+(.+)', section)
            for name, description in matches:
                principles.append({
                    "name": name.strip(),
                    "description": description.strip()
                })
                
        return principles
    
    def _extract_forbidden_actions(self, content: str) -> Dict[str, List[str]]:
        """Extract categorized forbidden actions."""
        forbidden = {}
        
        # Extract the Forbidden Actions section
        section = self._extract_section(content, "Forbidden Actions")
        if not section:
            return forbidden
        
        # Split by subsections
        subsections = re.split(r'###\s+\d+\.\s+(.+)', section)
        
        for i in range(1, len(subsections), 2):
            if i + 1 < len(subsections):
                category = subsections[i].strip()
                rules = subsections[i + 1].strip()
                
                # Extract individual forbidden items (lines starting with ❌)
                items = re.findall(r'❌\s+(.+?)(?=\n|$)', rules)
                forbidden[category] = [item.strip() for item in items]
                
        return forbidden
    
    def _extract_output_rules(self, content: str) -> List[str]:
        """Extract output formatting rules."""
        rules = []
        
        # Look for output formatting section within forbidden actions
        if "Output Formatting" in content:
            section = self._extract_subsection(content, "Output Formatting")
            if section:
                items = re.findall(r'[❌✅]\s+(.+?)(?=\n|$)', section)
                rules.extend([item.strip() for item in items])
                
        return rules
    
    def _extract_security_rules(self, content: str) -> List[str]:
        """Extract security and secrets rules."""
        rules = []
        
        if "Security and Secrets" in content:
            section = self._extract_subsection(content, "Security and Secrets")
            if section:
                items = re.findall(r'[❌✅]\s+(.+?)(?=\n|$)', section)
                rules.extend([item.strip() for item in items])
                
        return rules
    
    def _extract_mcp_rules(self, content: str) -> List[str]:
        """Extract MCP interaction rules."""
        rules = []
        
        if "MCP Interaction" in content:
            section = self._extract_subsection(content, "MCP Interaction")
            if section:
                items = re.findall(r'[❌✅]\s+(.+?)(?=\n|$)', section)
                rules.extend([item.strip() for item in items])
                
        return rules
    
    def _extract_metrics_gates(self, content: str) -> Dict[str, str]:
        """Extract quality gate metrics."""
        gates = {}
        
        if "Metrics and Validation" in content:
            section = self._extract_subsection(content, "Metrics and Validation")
            if section:
                # Extract gate definitions
                if "Pint:" in section:
                    gates["pint"] = "clean"
                if "Larastan:" in section:
                    gates["larastan"] = "level ≥6 or baseline with zero new errors"
                if "Mutation:" in section:
                    gates["mutation"] = "≥70%"
                if "Pulse:" in section:
                    gates["pulse"] = "p95 ≤500 ms, ≤10 queries"
                if "Sentry:" in section:
                    gates["sentry"] = "0 unhandled exceptions, release recorded"
                    
        return gates
    
    def _extract_section(self, content: str, section_name: str) -> str:
        """Extract content under a specific ## section."""
        pattern = rf'^##\s+{re.escape(section_name)}\s*$\n(.*?)(?=^##\s|\Z)'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else ""
    
    def _extract_subsection(self, content: str, subsection_name: str) -> str:
        """Extract content under a specific ### subsection."""
        pattern = rf'^###\s+\d+\.\s+{re.escape(subsection_name)}\s*$\n(.*?)(?=^###\s|\Z)'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else ""
    
    def validate_action(self, action_type: str, action_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate an action against loaded constraints.
        
        Args:
            action_type: Type of action (e.g., "scope", "code_generation", "output")
            action_data: Data about the action being validated
            
        Returns:
            Dictionary with validation result
        """
        violations = []
        
        # Check against forbidden actions by category
        for category, forbidden_items in self.constraints["forbidden_actions"].items():
            for forbidden in forbidden_items:
                if self._check_violation(action_type, action_data, forbidden):
                    violations.append({
                        "category": category,
                        "rule": forbidden,
                        "severity": "error"
                    })
        
        # Check security rules
        for rule in self.constraints["security_rules"]:
            if self._check_security_violation(action_data, rule):
                violations.append({
                    "category": "Security",
                    "rule": rule,
                    "severity": "critical"
                })
        
        return {
            "valid": len(violations) == 0,
            "violations": violations,
            "action_type": action_type
        }
    
    def _check_violation(self, action_type: str, action_data: Dict, forbidden_rule: str) -> bool:
        """Check if an action violates a forbidden rule."""
        # Convert to lowercase for comparison
        rule_lower = forbidden_rule.lower()
        
        # Check action type
        if action_type == "scope" and "scope" in rule_lower:
            return True
        if action_type == "time_estimate" and "time estimate" in rule_lower:
            return True
        if action_type == "code_generation" and "code" in rule_lower and "planning" in action_data.get("phase", "").lower():
            return True
            
        # Check action data content
        for key, value in action_data.items():
            if isinstance(value, str):
                if "next steps" in rule_lower and "next steps" in value.lower():
                    return True
                if "recommendation" in rule_lower and "recommendation" in value.lower():
                    return True
                    
        return False
    
    def _check_security_violation(self, action_data: Dict, security_rule: str) -> bool:
        """Check if action violates security rules."""
        rule_lower = security_rule.lower()
        
        # Check for credential exposure
        if "credential" in rule_lower or "token" in rule_lower:
            for key, value in action_data.items():
                if isinstance(value, str):
                    # Look for common secret patterns with high confidence
                    # Avoid false positives by requiring specific formats
                    secret_patterns = [
                        r'(?:password|token|key|secret|api[_-]?key)\s*[:=]\s*["\'][\w\-]{16,}["\']',  # Quoted secrets
                        r'bearer\s+[\w\-\.]{20,}',  # Bearer tokens
                        r'sk-[\w]{20,}',  # OpenAI-style keys
                        r'ghp_[\w]{36,}',  # GitHub personal access tokens
                        r'glpat-[\w\-]{20,}',  # GitLab tokens
                    ]
                    
                    for pattern in secret_patterns:
                        if re.search(pattern, value, re.IGNORECASE):
                            return True
                        
        return False
    
    def validate_phase_transition(self, current_phase: str, next_phase: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate that a phase transition is allowed.
        
        Args:
            current_phase: Current workflow phase
            next_phase: Requested next phase
            context: Context including completed artifacts
            
        Returns:
            Dictionary with validation result
        """
        # Define required phase order
        phase_order = [
            "Foundation",
            "Planning",
            "Role Definition",
            "Process",
            "Development",
            "Finalization"
        ]
        
        if current_phase not in phase_order or next_phase not in phase_order:
            return {
                "valid": False,
                "reason": f"Unknown phase: {current_phase} -> {next_phase}"
            }
        
        current_idx = phase_order.index(current_phase)
        next_idx = phase_order.index(next_phase)
        
        # Allow only sequential progression or staying in same phase
        if next_idx > current_idx + 1:
            return {
                "valid": False,
                "reason": f"Cannot skip phases: {current_phase} -> {next_phase}"
            }
        
        return {
            "valid": True,
            "reason": None
        }
    
    def get_quality_gates(self) -> Dict[str, str]:
        """Get configured quality gate thresholds."""
        return self.constraints["metrics_gates"]
    
    def get_global_principles(self) -> List[Dict[str, str]]:
        """Get global principles that all agents must follow."""
        return self.constraints["global_principles"]
