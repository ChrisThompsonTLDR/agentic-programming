---
title: larastan
org: larastan
package: larastan
github_url: https://github.com/larastan/larastan
docs_url: https://github.com/larastan/larastan/tree/3.x/docs
composer_require: composer require --dev "larastan/larastan:^3.0"
author: Can Vural
announce_date: null
latest_release: v3.9.3 (2026-02-20)
release_date: 2026-02-20
laravel_news_url: https://laravel-news.com/package/nunomaduro-larastan
downloads_30d: 3230200
stars: 6360
tags: [laravel, packages, phpstan, static-analysis, larastan, type-safety, eloquent]
---

# larastan

**A PHPStan extension for Laravel that understands framework “magic” and surfaces bugs before tests run.**

[Larastan](https://github.com/larastan/larastan) boots the application container so types that only exist at runtime can be resolved—closer to **code analysis** than pure static analysis. It was created by Can Vural and Nuno Maduro and is maintained with Viktor Szépe. **Install the `larastan/larastan` package** on modern apps; the [Laravel News package page](https://laravel-news.com/package/nunomaduro-larastan) still lives under the historical `nunomaduro/larastan` slug and shows older `^2.0` install lines—prefer this repo and Composer vendor name for new work.

## Key Features
- **Laravel-aware typing:** Models, facades, containers, and much of the framework’s dynamic API
- **Version alignment:** Larastan 3.x targets **Laravel 11.16+** and **PHP 8.2+** (see the [README](https://github.com/larastan/larastan) matrix for older Laravel ↔ Larastan major pairs)
- **Deep docs in-repo:** [Features](https://github.com/larastan/larastan/blob/3.x/docs/features.md), [rules](https://github.com/larastan/larastan/blob/3.x/docs/rules.md), [custom types](https://github.com/larastan/larastan/blob/3.x/docs/custom-types.md), [custom parameters](https://github.com/larastan/larastan/blob/3.x/docs/custom-config-parameters.md), [errors to ignore](https://github.com/larastan/larastan/blob/3.x/docs/errors-to-ignore.md)
- **Package development:** Analysing a Laravel package may require [`orchestra/testbench`](https://github.com/orchestra/testbench) (noted in the README)

## Installation

```bash
composer require --dev "larastan/larastan:^3.0"
```

## Usage

Add a `phpstan.neon` or `phpstan.neon.dist` at the project root (paths and level to taste):

```neon
includes:
    - vendor/larastan/larastan/extension.neon
    - vendor/nesbot/carbon/extension.neon

parameters:
    paths:
        - app/
    level: 5
```

Run analysis:

```bash
./vendor/bin/phpstan analyse
./vendor/bin/phpstan analyse --memory-limit=2G
```

Use `--generate-baseline` for legacy codebases, `@phpstan-ignore-next-line` / config `ignoreErrors` for targeted suppressions, and the [PHPStan config reference](https://phpstan.org/config-reference) for global options.

## Resources
- [GitHub](https://github.com/larastan/larastan)
- [Documentation (3.x tree)](https://github.com/larastan/larastan/tree/3.x/docs)
- [Laravel News — Larastan (package hub)](https://laravel-news.com/package/nunomaduro-larastan)
- [PHPStan](https://phpstan.org/)
- [[Laravel Packages]]
