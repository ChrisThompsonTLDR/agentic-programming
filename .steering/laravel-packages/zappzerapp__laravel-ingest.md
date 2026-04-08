---
title: laravel-ingest
org: zappzerapp
package: laravel-ingest
github_url: https://github.com/zappzerapp/laravel-ingest
docs_url: https://zappzerapp.github.io/laravel-ingest/
composer_require: composer require zappzerapp/laravel-ingest
author: 
announce_date: 
latest_release: 
release_date: 
laravel_news_url: https://laravel-news.com/laravel-ingest
downloads_30d: 
stars: 
tags: [laravel, packages, data-ingestion, import, pipeline]
---

# laravel-ingest

**A Laravel package for ingesting and processing data through clean, chainable pipelines.**

## Key Features
- Fluent, chainable API for building data ingestion pipelines
- Supports bulk data import with chunked processing
- Integrates with Laravel's queue system for background ingestion
- Configurable data transformation and validation steps

## Installation

```bash
composer require zappzerapp/laravel-ingest
```

## Usage

```php
use Zappzerapp\LaravelIngest\Facades\Ingest;

Ingest::from($source)
    ->transform(MyTransformer::class)
    ->into(MyModel::class)
    ->run();
```

## Resources
- [GitHub](https://github.com/zappzerapp/laravel-ingest)
- [Docs](https://zappzerapp.github.io/laravel-ingest/)
- [Laravel News](https://laravel-news.com/laravel-ingest)
- [[Laravel Packages]]
