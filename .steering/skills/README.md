# `.steering/skills`

## Packaged skills (synced)

Subdirectories with **`SKILL.md`** are canonical. Replicate each to:

- `.cursor/skills/<name>/SKILL.md`
- `.claude/skills/<name>/SKILL.md`
- `.github/skills/<name>/SKILL.md`

Edit only under `.steering/skills/<name>/`, then run **`python3 scripts/regenerate-ide-mirrors.py`** (or follow the **sync-skills** skill) so `.cursor`, `.claude`, and `.github` match `.steering`.

## Upstream-derived skills (repeatable sync)

Some skills are regenerated from external catalogs rather than edited by hand. See **[SOURCES.md](./SOURCES.md)** for the list (for example [Laravel Boost `.ai`](https://github.com/laravel/boost/tree/main/.ai)). Refresh them with **`python3 scripts/sync-boost-ai-skills.py`**, then run **`python3 scripts/regenerate-ide-mirrors.py`**. The latest Boost commit used is stored in **`.boost-ai-sync.json`**.

## Research notes (not synced)

Flat files named **`<owner>__<skill-name>.md`** are outputs from the **`research-skill`** agent. They are not mirrored.
