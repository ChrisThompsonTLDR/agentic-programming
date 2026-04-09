---
title: pint
org: laravel
package: pint
github_url: https://github.com/laravel/pint
docs_url: https://laravel.com/docs/13.x/pint
composer_require: composer require laravel/pint --dev
author: Nuno Maduro
announce_date: 2022-06-22
latest_release: v1.29.0 (2026-03-12)
release_date: 2026-03-12
laravel_news_url: https://laravel-news.com/laravel-pint
downloads_30d: 6045960
stars: 3114
tags: [laravel, packages, pint, php-cs-fixer, lint, formatter, code-style, ci, github-actions]
---

# pint

**An opinionated PHP code style fixer for minimalists, built on PHP CS Fixer.**

[Laravel Pint](https://github.com/laravel/pint) ships with new Laravel apps and enforces consistent formatting with almost no setup. The [Laravel 13.x docs](https://laravel.com/docs/13.x/pint) cover installation, CLI flags, `pint.json` (presets, rules, excludes), and a sample GitHub Actions workflow. [Laravel News](https://laravel-news.com/laravel-pint) introduced it at launch with a walkthrough of presets, `--test`, and verbose output.

## Key Features
- **Defaults first:** Runs with Laravel’s opinionated style out of the box; optional `pint.json` for presets and rule tweaks
- **Presets:** `laravel`, `per`, `psr12`, `symfony`, or `empty` (then compose rules yourself)
- **PHP CS Fixer rules:** Any Fixer rule applies; Pint also exposes custom rules under the `Pint/` prefix (e.g. `Pint/phpdoc_type_annotations_only`)
- **CLI workflow:** Fix the tree with `./vendor/bin/pint`, or `--test` for CI (non-zero on violations), `--dirty` / `--diff=branch` for scoped runs, `--repair` to fix and still fail the exit code, `-v` for detail, `--parallel` for faster runs
- **Scope control:** `exclude`, `notName`, and `notPath` in config to skip paths or patterns

## Installation

Pint is already present on current Laravel skeletons. For older apps:

```bash
composer require laravel/pint --dev
```

## Usage

```bash
./vendor/bin/pint
./vendor/bin/pint --test
./vendor/bin/pint app/Models/User.php
./vendor/bin/pint --diff=main
```

Optional `pint.json` at the project root:

```json
{
    "preset": "laravel"
}
```

Override config path: `./vendor/bin/pint --config path/to/pint.json`.

## Resources
- [GitHub](https://github.com/laravel/pint)
- [Documentation (Laravel 13.x)](https://laravel.com/docs/13.x/pint)
- [Laravel News — Laravel Pint](https://laravel-news.com/laravel-pint)
- [[Laravel Packages]]
