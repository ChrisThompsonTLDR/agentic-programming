Frontmatter
```
---
name:  # Required: 1-64 chars, lowercase a-z 0-9 -, no leading/trailing/consecutive hyphens. Matches folder name.
description:  # Required: 1-1024 chars. Describe what the skill does and when to use it. Include keywords.
license:  # Optional: License name or reference.
compatibility:  # Optional: Max 500 chars. Environment requirements (e.g., tools, packages, network).
metadata:  # Optional: Arbitrary key-value pairs.
  author: 
  version: "1.0"
allowed-tools:  # Optional (experimental): Space-delimited pre-approved tools.
---
```

# Skill Instructions

Write clear, step-by-step instructions for agents to perform the task effectively.

## Recommended Structure
- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases
- References to other files: [REFERENCE.md](references/REFERENCE.md), scripts/extract.py

Keep under 500 lines (~5000 tokens). Use `references/`, `scripts/`, `assets/` for more.

# Directory Structure
```
skill-name/
├── SKILL.md          # This file
├── scripts/          # Optional: Executable code (e.g., extract.py)
├── references/       # Optional: Docs (e.g., REFERENCE.md)
├── assets/           # Optional: Templates, images, data
└── ...               # Additional files
```

# Frontmatter Details

## name
- 1-64 chars
- Lowercase a-z, 0-9, -
- No start/end/consecutive hyphens
- Matches parent dir

**Valid:** `pdf-processing`, `data-analysis`

**Invalid:** `PDF-Processing`, `-pdf`, `pdf--processing`

## description
**Good:** "Extracts text/tables from PDFs, fills forms, merges files. Use for PDF tasks."
**Poor:** "PDF helper."

## Other Fields
- **license:** e.g., "Apache-2.0" or "See LICENSE.txt"
- **compatibility:** e.g., "Requires Python 3.10+, internet access"
- **metadata:** Custom key-values
- **allowed-tools:** e.g., "Bash(git:*) Read"

# Optional Directories
- **scripts/**: Self-contained executables (Python, Bash, JS)
- **references/**: Load on demand (REFERENCE.md, FORMS.md)
- **assets/**: Static files (templates, images)

# Validation
Use [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref):
```
skills-ref validate ./my-skill
```

# Full Spec Reference
See https://agentskills.io/specification.md for complete details.

# Progressive Disclosure
1. Metadata (~100 tokens): Loaded for all skills
2. Instructions (<5000 tokens): Loaded on activation
3. Resources: Loaded as needed