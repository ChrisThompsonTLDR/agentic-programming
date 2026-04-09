---
title: saloon
org: saloonphp
package: saloon
github_url: https://github.com/saloonphp/saloon
docs_url: https://docs.saloon.dev
composer_require: composer require saloonphp/saloon
author: Sam Carré
announce_date: 2022-01-18
latest_release: v4.0.0 (2026-03-25)
release_date: 2026-03-25
laravel_news_url: https://laravel-news.com/saloon
downloads_30d: 700734
stars: 2398
tags: [laravel, packages, api, api-integrations, api-wrapper, framework-agnostic, guzzle-wrapper, php, saloon, sdk]
---

# Saloon

**A PHP package for building elegant API integrations and SDKs. Saloon provides a clean, object-oriented way to define, send, and test HTTP requests, making it easy to integrate third-party APIs into Laravel applications.**

## Key Features
- Define API integrations as expressive PHP classes (Connectors, Requests, Responses)
- Built-in support for authentication (Bearer tokens, Basic auth, OAuth2)
- Request middleware and plugin system for reusable request/response logic
- First-class mocking and testing utilities — fake HTTP responses without hitting real APIs
- Pagination support for paginated API endpoints
- Works as a standalone PHP package or with the dedicated `saloonphp/laravel-plugin` for Laravel-specific features
- Supports asynchronous (concurrent) requests out of the box

## Installation

```bash
composer require saloonphp/saloon
```

For the full Laravel integration (service provider, config, artisan commands):

```bash
composer require saloonphp/laravel-plugin
```

## Usage

Define a **Connector** for your API base URL and shared config:

```php
use Saloon\Http\Connector;

class ForgeConnector extends Connector
{
    public function resolveBaseUrl(): string
    {
        return 'https://forge.laravel.com/api/v1';
    }
}
```

Define individual **Requests** as classes:

```php
use Saloon\Http\Request;
use Saloon\Enums\Method;

class GetServersRequest extends Request
{
    protected Method $method = Method::GET;

    public function resolveEndpoint(): string
    {
        return '/servers';
    }
}
```

Send the request and work with the response:

```php
$connector = new ForgeConnector();
$response = $connector->send(new GetServersRequest());

$servers = $response->json();
```

Mock requests in tests:

```php
use Saloon\Http\Faking\MockClient;
use Saloon\Http\Faking\MockResponse;

$mockClient = new MockClient([
    GetServersRequest::class => MockResponse::make(['data' => []], 200),
]);

$connector->withMockClient($mockClient);
```

## Resources
- [GitHub](https://github.com/saloonphp/saloon)
- [Docs](https://docs.saloon.dev)
- [[Laravel Packages]]
