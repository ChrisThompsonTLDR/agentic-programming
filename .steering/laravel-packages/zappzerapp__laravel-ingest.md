---
title: laravel-ingest
org: zappzerapp
package: laravel-ingest
github_url: https://github.com/zappzerapp/laravel-ingest
docs_url: https://zappzerapp.github.io/laravel-ingest/
composer_require: composer require zappzerapp/laravel-ingest
author: Robin Kopp
announce_date: 
latest_release: v0.5.3 (2026-04-07)
release_date: 2026-04-07
laravel_news_url: https://laravel-news.com/laravel-ingest
downloads_30d: 207
stars: 88
tags: [laravel, packages, etl, csv, excel, import, streaming, queue, data-ingestion]
---

# laravel-ingest

![Laravel Ingest Banner](https://raw.githubusercontent.com/zappzerapp/laravel-ingest/refs/heads/main/.github/header.png)

**A robust, configuration-driven ETL (Extract, Transform, Load) framework for Laravel. Replaces fragile, procedural import scripts with declarative importer classes that scale from 100 to 10 million rows using PHP Generators and Laravel Queues.**

## Key Features
- Infinite scalability via PHP Generators and Laravel Queues — flat memory usage regardless of file size
- Declarative `IngestConfig` fluent builder — define *what* to import, not *how* to loop
- Dry-run mode to validate imports without touching the database
- Auto-resolution of `BelongsTo` and `BelongsToMany` relationships by column value
- Duplicate handling strategies: `SKIP`, `CREATE`, `UPDATE`, `UPDATE_IF_NEWER`
- Failed row tracking with downloadable CSV export for fix-and-retry workflows
- Column aliasing to map varying header names to a single field
- Import sources: file upload, filesystem disks (S3, FTP, SFTP), URL
- Auto-generated Artisan commands and REST API endpoints per importer
- Lifecycle events: `IngestRunStarted`, `ChunkProcessed`, `RowProcessed`, `IngestRunCompleted`, `IngestRunFailed`

## Installation

```bash
composer require zappzerapp/laravel-ingest

# Publish config & migrations
php artisan vendor:publish --provider="LaravelIngest\IngestServiceProvider"

# Run migrations
php artisan migrate
```

## Usage

Define an importer class implementing `IngestDefinition`:

```php
namespace App\Ingest;

use App\Models\Role;
use App\Models\User;
use LaravelIngest\Contracts\IngestDefinition;
use LaravelIngest\IngestConfig;
use LaravelIngest\Enums\SourceType;
use LaravelIngest\Enums\DuplicateStrategy;

class UserImporter implements IngestDefinition
{
    public function getConfig(): IngestConfig
    {
        return IngestConfig::for(User::class)
            ->fromSource(SourceType::UPLOAD)
            ->keyedBy('email')
            ->onDuplicate(DuplicateStrategy::UPDATE)
            ->map('Full Name', 'name')
            ->map(['E-Mail', 'Email Address'], 'email') // supports aliases
            ->relate('Role', 'role', Role::class, 'slug', createIfMissing: true)
            ->validate([
                'email'     => 'required|email',
                'Full Name' => 'required|string|min:3',
            ]);
    }
}
```

Register in `AppServiceProvider`:

```php
use LaravelIngest\IngestServiceProvider;

$this->app->tag([UserImporter::class], IngestServiceProvider::INGEST_DEFINITION_TAG);
```

Run via Artisan or HTTP API:

```bash
php artisan ingest:run user-importer --file=users.csv
# POST /api/v1/ingest/upload/user-importer
```

## Resources
- [GitHub](https://github.com/zappzerapp/laravel-ingest)
- [Docs](https://zappzerapp.github.io/laravel-ingest/)
- [Laravel News](https://laravel-news.com/laravel-ingest)
- [[Laravel Packages]]
