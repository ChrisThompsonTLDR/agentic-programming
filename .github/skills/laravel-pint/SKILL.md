---
name: laravel-pint
description: "Use when formatting PHP in Laravel projects that use Laravel Pint. Trigger after editing PHP files, before finalizing a change, or when the user mentions Pint or project PHP style. Covers: running pint on dirty files, --format agent when supported, and not using pint --test for autofix workflows."
license: MIT
metadata:
  author: laravel
---

> **Synced from** [`laravel/boost`](https://github.com/laravel/boost) @ `14a5c6ab6729a8bb108bc5a29280fe53e5da6abd` — `.ai/pint/core.blade.php` (Blade branches merged). Regenerate: `python3 scripts/sync-boost-ai-skills.py`.

# Laravel Pint Code Formatter

- If you have modified any PHP files, run `./vendor/bin/pint --dirty` before finalizing changes so code matches the project's expected style.
- When your tooling supports Pint's agent formatter, prefer `./vendor/bin/pint --dirty --format agent`.
- Do not rely on `./vendor/bin/pint --test` to fix style; run `./vendor/bin/pint` (with or without `--format agent`) to apply fixes.
- With **Laravel Sail**, prefix: `./vendor/bin/sail bin pint --dirty` (and add `--format agent` when appropriate).
