# Skill Research Note — neo4j-contrib/neo4j-skills

> **⚠️ Verification status:** GitHub MCP and DeepWiki tools were unavailable during this research session.
> All sections marked **[NEEDS LIVE VERIFICATION]** must be confirmed by reading the repository directly.
> Source URL: <https://github.com/neo4j-contrib/neo4j-skills>

---

## 1. URL Parse

| Field       | Value                                         |
|-------------|-----------------------------------------------|
| owner       | `neo4j-contrib`                               |
| repo        | `neo4j-skills`                                |
| skill-name  | `neo4j-skills` (entire repo; no sub-path given) |
| path        | repo root                                     |

Because the URL points to the repository root (not a specific skill subdirectory), this note covers the whole repo as a skills collection. Individual skills discovered inside should each get their own note following the `<owner>__<skill-name>.md` convention.

---

## 2. Frontmatter vs Spec [NEEDS LIVE VERIFICATION]

The SKILL.md file(s) inside the repo were not readable in this session. The table below shows the required/optional fields from `skill-template.md` and what needs to be confirmed.

| Spec field      | Required? | Status                         |
|-----------------|-----------|--------------------------------|
| `name`          | ✅ Yes    | **Unverified** — must be 1-64 chars, lowercase `a-z 0-9 -`, no leading/trailing/consecutive hyphens, must match folder name |
| `description`   | ✅ Yes    | **Unverified** — must be 1-1024 chars with keywords |
| `license`       | Optional  | **Unverified**                 |
| `compatibility` | Optional  | **Unverified**                 |
| `metadata`      | Optional  | **Unverified**                 |
| `allowed-tools` | Optional  | **Unverified**                 |

---

## 3. Skill Instructions [NEEDS LIVE VERIFICATION]

The body of any `SKILL.md` file(s) could not be read. Based on the repository name and organization context:

- **neo4j-contrib** is the official Neo4j community GitHub organization, home to community-maintained Neo4j tooling.
- **neo4j-skills** strongly implies Copilot skills for working with the [Neo4j graph database](https://neo4j.com/) and its [Cypher query language](https://neo4j.com/docs/cypher-manual/current/).

Likely skill topics include (all **unverified**):
- Writing and optimizing Cypher queries
- Graph data modeling patterns
- Neo4j schema/constraint design
- Integration with Neo4j drivers (Python, JavaScript, Java)

To populate this section accurately, read each `SKILL.md` in the repository and extract its step-by-step instructions, examples, and edge cases.

---

## 4. Directory Structure [NEEDS LIVE VERIFICATION]

Expected layout per `skill-template.md`:

```
neo4j-skills/
├── README.md             # Likely present (repo-level overview)
├── <skill-name>/
│   ├── SKILL.md          # Core skill file (frontmatter + instructions)
│   ├── scripts/          # Optional executables
│   ├── references/       # Optional reference docs
│   └── assets/           # Optional static files
└── ...
```

Actual layout: **unknown** — list the repo root and each skill subdirectory to confirm.

---

## 5. Validation & Spec

Once the `SKILL.md` files are accessible, validate against the agentskills.io spec:

```bash
skills-ref validate ./<skill-name>
```

Open questions for the maintainer:
- Do all skill `name` values match their folder names?
- Are `description` fields keyword-rich (>10 words)?
- Are instructions under 500 lines / ~5000 tokens?
- Are any heavyweight assets split into `references/` or `assets/` subdirectories?

Full spec: <https://agentskills.io/specification.md>

---

## 6. Follow-up Tasks

1. Re-run this research with GitHub MCP available to read live file contents.
2. If multiple skills exist in the repo, create one research note per skill:  
   `.steering/skills/neo4j-contrib__<skill-name>.md`
3. Check for any `.agent.md` or workflow files in the repo that activate or reference these skills.
4. Note the license from the repo's `LICENSE` file or `SKILL.md` frontmatter.

---

## 7. Sources

| Source | URL / Path |
|--------|-----------|
| Repository root | <https://github.com/neo4j-contrib/neo4j-skills> |
| Skill spec template | `.github/skills/skill-research/skill-template.md` (this workspace) |
| agentskills.io spec | <https://agentskills.io/specification.md> |
| skills-ref validator | <https://github.com/agentskills/agentskills/tree/main/skills-ref> |
