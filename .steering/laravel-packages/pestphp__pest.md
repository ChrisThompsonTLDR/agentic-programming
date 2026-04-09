---
title: pest
org: pestphp
package: pest
github_url: https://github.com/pestphp/pest
docs_url: https://pestphp.com/docs/installation
composer_require: composer require pestphp/pest --dev --with-all-dependencies
author: Nuno Maduro
announce_date: 2025-08-21
latest_release: v4.4.5 (2026-04-03)
release_date: 2026-04-03
laravel_news_url: https://laravel-news.com/pest-4
downloads_30d: 3500383
stars: 11409
tags: [laravel, packages, pest, testing, phpunit, browser-testing, playwright, ci, expectations]
---

# pest

**An elegant PHP testing framework focused on expressive syntax and a single toolchain from unit tests to browser automation.**

[Pest](https://github.com/pestphp/pest) sits on top of PHPUnit and is widely used with Laravel (`laravel new my-app --pest`). [Pest 4](https://laravel-news.com/pest-4) adds first-class **browser testing** (e.g. Playwright-backed flows), **visual** and **device** testing, unified **coverage** across browser and PHP tests, **Tinker-style sessions** inside tests, and **test sharding** for parallel CI. The [installation guide](https://pestphp.com/docs/installation) requires **PHP 8.3+** and documents init, plugins, and PHPUnit migration paths.

## Key Features
- **Readable API:** `expect()`, datasets, hooks, and plugins—see [Writing tests](https://pestphp.com/docs/installation) and deeper guides on the same site
- **Pest 4 browser stack:** End-to-end tests alongside PHP tests; see [Browser testing](https://pestphp.com/docs/browser-testing) and the [v4 announcement](https://pestphp.com/docs/pest-v4-is-here-now-with-browser-testing)
- **Ecosystem plugins:** e.g. `pest-plugin-browser` for browser testing; `pest-plugin-drift` to convert PHPUnit tests ([migrating from PHPUnit](https://pestphp.com/docs/migrating-from-phpunit-guide))
- **Ops-friendly:** Sharding and CI patterns are covered in [Continuous integration](https://pestphp.com/docs/continuous-integration); upgrades use the [upgrade guide](https://pestphp.com/docs/upgrade-guide)

## Installation

On a greenfield Laravel app, prefer the installer with Pest selected (`laravel new my-project --pest` per [Laravel News](https://laravel-news.com/pest-4)).

On an existing project, follow [Installation](https://pestphp.com/docs/installation):

```bash
composer remove phpunit/phpunit
composer require pestphp/pest --dev --with-all-dependencies
./vendor/bin/pest --init
```

Then run the suite:

```bash
./vendor/bin/pest
```

Add browser testing when needed via `pest-plugin-browser` (see the Browser testing docs).

## Usage

After `--init`, configure the generated `Pest.php` and write tests under your tests directory using Pest’s function-style API; PHPUnit-style classes remain supported where configured.

## Resources
- [GitHub](https://github.com/pestphp/pest)
- [Documentation — Installation](https://pestphp.com/docs/installation)
- [Laravel News — Pest 4 is released](https://laravel-news.com/pest-4)
- [Pest v4 announcement](https://pestphp.com/docs/pest-v4-is-here-now-with-browser-testing)
- [[Laravel Packages]]
