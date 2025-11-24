"""Guardrail supervisor to enforce constraints."""

import re
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

from ..parsers.guardrail_parser import GuardrailParser, Constraint


@dataclass
class ValidationResult:
    """Result of constraint validation."""
    
    passed: bool
    violations: List[str]
    warnings: List[str]


class GuardrailSupervisor:
    """Enforces constraints from forbidden.md and rules.md before agent execution."""
    
    def __init__(self, guardrail_parser: GuardrailParser):
        """Initialize supervisor with parsed constraints."""
        self.parser = guardrail_parser
        self.constraints = guardrail_parser.get_all_constraints()
        self.forbidden_patterns = guardrail_parser.get_forbidden_patterns()
        
    def validate_agent_input(self, agent_id: str, user_input: str) -> ValidationResult:
        """Validate user input against constraints before agent execution."""
        violations = []
        warnings = []
        
        # Check for forbidden patterns in input
        input_lower = user_input.lower()
        
        if "time_estimation" in self.forbidden_patterns:
            time_patterns = [
                r'\d+\s*(hour|day|week|month|sprint)',
                r'estimate[sd]?\s+time',
                r'how long',
                r'timeline',
            ]
            for pattern in time_patterns:
                if re.search(pattern, input_lower):
                    violations.append(
                        "Input contains time estimation request, which is forbidden. "
                        "See support/01-forbidden.md: Do not make or imply time estimates."
                    )
                    break
        
        # Check for scope invention requests
        if "scope_invention" in self.forbidden_patterns:
            scope_patterns = [
                r'add\s+feature',
                r'also\s+include',
                r'might\s+want',
                r'could\s+add',
            ]
            for pattern in scope_patterns:
                if re.search(pattern, input_lower):
                    warnings.append(
                        "Input may be requesting scope invention. "
                        "Ensure all features trace to PRD or task metadata."
                    )
                    break
        
        return ValidationResult(
            passed=len(violations) == 0,
            violations=violations,
            warnings=warnings,
        )
    
    def validate_agent_output(
        self, 
        agent_id: str, 
        output: str,
        phase: str
    ) -> ValidationResult:
        """Validate agent output against constraints."""
        violations = []
        warnings = []
        
        output_lower = output.lower()
        
        # Check for unsolicited recommendations
        # Always check this constraint even if not explicitly in patterns
        if any(phrase in output_lower for phrase in [
            "next steps:",
            "next steps\n",
            "recommendations:",
            "recommendation:",
            "to do next",
            "consider adding",
            "you might want",
        ]):
            violations.append(
                "Output contains unsolicited recommendations or 'Next steps'. "
                "See support/01-forbidden.md: Never include 'Next steps' or 'Recommendations' in output."
            )
        
        # Check for premature code generation in planning phases
        # Always check this in planning/roles phases
        if phase in ["planning", "roles"]:
            code_indicators = [
                r'```(?:php|python|javascript|typescript)',
                r'class\s+\w+\s*{',
                r'function\s+\w+\s*\(',
                r'public\s+function',
                r'def\s+\w+\s*\(',
            ]
            for pattern in code_indicators:
                if re.search(pattern, output, re.IGNORECASE):
                    violations.append(
                        f"Output contains code generation in {phase} phase. "
                        "See support/01-forbidden.md: No code emission in planning/expand phases."
                    )
                    break
        
        # Check for credential exposure
        # Always check this constraint
        credential_patterns = [
            r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
            r'password\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
            r'secret\s*=\s*["\'][^"\']+["\']',
            r'sk-[a-zA-Z0-9]{32,}',  # OpenAI-style keys
        ]
        for pattern in credential_patterns:
            if re.search(pattern, output, re.IGNORECASE):
                violations.append(
                    "Output may contain exposed credentials. "
                    "See support/01-forbidden.md: Never expose real credentials, tokens, or API keys."
                )
                break
        
        return ValidationResult(
            passed=len(violations) == 0,
            violations=violations,
            warnings=warnings,
        )
    
    def get_constraints_for_agent(self, agent_id: str, phase: str) -> List[Constraint]:
        """Get constraints applicable to a specific agent/phase."""
        applicable = []
        
        for constraint in self.constraints:
            # All constraints apply unless specifically scoped
            applicable.append(constraint)
        
        return applicable
    
    def format_constraints_for_prompt(self, agent_id: str, phase: str) -> str:
        """Format constraints as a prompt section for agent instructions."""
        constraints = self.get_constraints_for_agent(agent_id, phase)
        
        prompt_parts = [
            "## CRITICAL CONSTRAINTS",
            "",
            "You MUST adhere to these constraints from support/01-forbidden.md:",
            "",
        ]
        
        # Group by type
        forbidden = [c for c in constraints if c.type == "forbidden"]
        required = [c for c in constraints if c.type == "required"]
        
        if forbidden:
            prompt_parts.append("### FORBIDDEN ACTIONS (You MUST NOT do these):")
            for constraint in forbidden:
                if constraint.severity == "critical":
                    prompt_parts.append(f"- 🚫 CRITICAL: {constraint.description}")
                else:
                    prompt_parts.append(f"- ❌ {constraint.description}")
            prompt_parts.append("")
        
        if required:
            prompt_parts.append("### REQUIRED ACTIONS (You MUST do these):")
            for constraint in required:
                prompt_parts.append(f"- ✅ {constraint.description}")
            prompt_parts.append("")
        
        prompt_parts.extend([
            "### ENFORCEMENT",
            "If you detect a constraint violation:",
            "1. Halt execution immediately",
            "2. Output only: ❌ Forbidden action detected — see 01-forbidden.md",
            "3. Exit without performing side effects",
        ])
        
        return "\n".join(prompt_parts)
