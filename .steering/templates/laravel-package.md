---
title: 
org: 
package: 
github_url: 
docs_url: 
composer_require: composer require 
author: 
latest_release: 
release_date: 
packagist_url: 
downloads_30d: 
stars: 
forks: 
tags: [laravel, packages]
announce_date: ''
laravel_news_url: ''

---

## Field-to-Source Mapping

Resolve every frontmatter field before writing the file. Use these sources:

| Field | Source |
|-------|--------|
| `author` | Packagist (`packagist.org/packages/<vendor>/<package>.json` → `authors[0].name`) |
| `stars` | GitHub MCP → `stargazers_count` |
| `latest_release` | GitHub MCP `get_latest_release` → format as `vX.Y.Z (YYYY-MM-DD)` |
| `release_date` | GitHub MCP `get_latest_release` → `published_at` date (YYYY-MM-DD) |
| `downloads_30d` | Packagist stats page (`packagist.org/packages/<vendor>/<package>/stats`) → "Last 30 days" |
| `announce_date` | Laravel News article publication date (fetch the `laravel_news_url`) |
| `laravel_news_url` | Search `laravel-news.com <package-name>` and verify the URL resolves |
| `docs_url` | GitHub repo `homepage` field or README docs link |
| `tags` | GitHub repo `topics` + relevant feature keywords |

**All fields must be attempted.** Only leave a field blank if the data genuinely does not exist after checking its source.

---

# PACKAGE_NAME

![Banner](https://raw.githubusercontent.com/ORG/PACKAGE/refs/heads/main/.github/header.png)

**Tagline or short description.**

PACKAGE_DESCRIPTION by [AUTHOR](https://github.com/ORG) is a [type, e.g. configuration-driven ETL] package/framework for Laravel. It [key benefit, e.g. replaces fragile import scripts with declarative classes].

The system handles [core features like file processing, validation, etc.], so you can focus on business logic.

![Featured Image](https://example.com/image.png)

## Key Features

- **Icon Scalability**: Description.
- **Icon Syntax**: Description.
- **Icon Feature**: Description.
- Add more as needed.

## Installation

```bash
composer require ORG/PACKAGE
php artisan migrate  # if applicable
# publish config/migrations if needed
```

Register in `config/PACKAGE.php` if applicable.

## Defining/Configuring

Create classes in `App\PACKAGE` implementing `Contract`:

```php
namespace App\PACKAGE;

use PACKAGE\Models\Model;
use PACKAGE\Contracts\Definition;
use PACKAGE\DTOs\Config;

class ExampleImporter implements Definition
{
    public function config(): Config
    {
        return Config::create()
            ->model(Model::class)
            ->strategy(Strategy::UPDATE)
            // ... more config
            ;
    }
}
```

## Running/CLI/API

**CLI**:
```bash
php artisan package:run example-importer --file=data.csv --dry-run
```

**API** (if applicable):
```
POST /api/v1/package/upload/example-importer
```

## Monitoring

**CLI**:
- `php artisan package:list`
- `php artisan package:status {id}`
- `php artisan package:cancel {id}`
- `php artisan package:retry {id}`

REST endpoints available.

## Events

- `EventName1`
- `EventName2`
- etc.

## Resources

- [GitHub]({{github_url}})
- [Documentation]({{docs_url}})
- [Packagist]({{packagist_url}})
- [Laravel News Article]()  # if featured