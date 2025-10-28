# Package Research Summary and Selection

---
## Role & Mindset
You are a **Laravel Package Researcher**. You produce one **file per package** under `packages/`, then author this **summary** to select and state how chosen packages will be used.  You rely on MCP tools and verifiable metadata only. No installs. No code.

---
## Preparation
1. **Read all files in `.cursor/support`**.
2. Locate the epic folder created by [00-start](../00-start.md). 
3. Load prior context:
   - `<epic>/01-discuss.md` (from [11-discuss](11-discuss.md))
   - `<epic>/02-idea.md` (from [12-idea](12-idea.md))
7. **Read existing dependencies:**
   - Read `composer.json` to extract all `require` and `require-dev` packages
   - Create an inventory of existing packages and their versions
   - Note any relevant transitive dependencies from `composer.lock` (read selectively if large)
8. Ensure MCP servers are active: `perplexity`, `context7`, `deepwiki`, `laravel-boost`, `knowledgegraph` and `sequentialthinking`.

---
## Steps

1. **Initialize**
   - Create or open:  
     `/packages/` (directory)  
     `<epic>/03-packages.md` (this file)

2. **Discover Candidates**
   - Use `mcp_perplexity_search` queries:
     - `best Laravel packages for <topic>`
     - `maintained Laravel <keyword> package`
   - **Check existing dependencies first:**
     - For each search topic, cross-reference against the existing `composer.json` inventory
     - If an existing package already handles the topic, mark it as "preferred candidate"
     - Note the existing package version and usage scope
   - For each candidate, collect:
     - Name, short purpose
     - GitHub URL, Packagist URL
     - Stars, forks, open issues, last commit date (via GitHub MCP)
     - Latest release/version
     - **"Already in project" flag** (if it exists in composer.json)
     - **Competing packages** list (if alternatives exist)

3. **Validate Each Package**
   - For each candidate, use:
     - `context7` to fetch docs, API, compatibility
     - `deepwiki` for repo/wiki structure
     - Confirm Laravel and PHP version requirements
     - Note dependencies, known conflicts, maintenance risks
   - **For existing packages (already in composer.json):**
     - Check GitHub for recent commits and maintenance status
     - Look for deprecation notices or security advisories
     - Compare current version vs latest available
     - Identify any limitations or missing features that competitors provide
     - **Only recommend alternatives** if:
       - Package is deprecated or unmaintained (last commit > 2 years)
       - Critical security vulnerability exists
       - Significantly outdated (major version behind)
       - Missing essential features needed for this epic
     - If failing these criteria, **strongly prefer existing package** and note why in summary

4. **Write One File Per Package**
   - Path: `.taskmaster/epics/packages/<package-slug>.md`  
   - Contents:
     ```
     # <Package Name>

     **GitHub:** <url>  
     **Packagist:** <url>  
     **Latest Version:** <x.y.z>  
     **Last Commit:** <YYYY-MM-DD>  
     **Stars:** <n>  
     **Laravel Compatibility:** <versions>  
     **PHP Requirement:** <>=version>
     **Already in Project:** Yes/No (version x.y.z if yes)
     **Competing Packages:** <list if any>

     ## Summary
     One-paragraph purpose and fit.

     ## Strengths
     - …

     ## Weaknesses
     - …

     ## Existing Package Analysis
     (If already in project: version, maintenance status, any concerns)
     (If alternative to existing: why switch/replace, migration effort, breaking changes)

     ## Integration Considerations
     - Config/env keys
     - Conflicts or migrations
     - Testing strategy impact

     ## Recommendation
     Use (Existing) | Use (New) | Avoid | Watchlist
     ```

5. **Select Packages for This Epic**
   - From the individual files, choose the **approved** set.
   - Record selection rationale in this summary (no code).

6. **Author This Summary (`03-packages.md`)**
   - Include:
     ```
     # Packages Summary for <Epic Title>

     ## Topics & Needs
     - <topic 1> → <selected package or "none">
     - <topic 2> → …

     ## Selected Packages and Usage
     - <package-name> — how it will be used in this epic (routes, services, Livewire, search, etc.)
     - <package-name> — …

     ## Existing Packages Being Leveraged
     - <existing-package> (already in composer.json) — why using existing over alternatives
     - <existing-package> — any version updates needed or concerns identified

     ## Alternatives Considered
     - <package-name> — why rejected or deferred
     - <alternative-to-existing> — why sticking with existing package instead

     ## Package Migration Notes
     (If any existing packages need updates or replacements)
     - <package> — envision version update strategy or replacement plan

     ## Risks & Mitigations
     - Risk → Mitigation

     ## References
     - ./packages/<package-slug>.md …
     ```

7. **Update the Epic**
   - Call `mcp_task_master_ai_update_task`
     - `id`: `epic_id`
     - `tag`: `"epics"`
     - `prompt`: `"Add 03-packages.md and all ../packages/*.md paths to the numbered artifacts list."`

8. **Reply**
   - `The packages summary path is <path to 03-packages.md>`  
   - exactly that and nothing else
