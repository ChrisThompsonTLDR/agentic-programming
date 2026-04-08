---
title: laravel-markdown-response
org: spatie
package: laravel-markdown-response
github_url: https://github.com/spatie/laravel-markdown-response
docs_url: https://spatie.be/docs/laravel-markdown-response/v1/introduction
composer_require: composer require spatie/laravel-markdown-response
author: Freek Van der Herten
announce_date: 2025-04-07
latest_release: 
release_date: 
laravel_news_url: https://laravel-news.com/serve-markdown-versions-of-your-laravel-pages-to-ai-agents
downloads_30d: 
stars: 
tags: [laravel, packages, markdown, ai-agents, llm, response, content-negotiation, llms-txt]
---

# laravel-markdown-response

**A Laravel package that lets you serve Markdown versions of your web pages alongside standard HTML responses, enabling AI agents and LLM-powered tools to consume your content directly.**

## Key Features
- Register routes that automatically have a `.md` Markdown counterpart
- Return `MarkdownResponse` instead of a standard view response to serve structured Markdown
- Supports content negotiation via `Accept` header and `.md` URL suffix
- Enables AI crawlers and agents to read your pages as clean Markdown
- Integrates seamlessly with existing Laravel route definitions
- Pair with `llms.txt` conventions for full AI-agent discoverability

## Installation

```bash
composer require spatie/laravel-markdown-response
```

## Usage

Return a `MarkdownResponse` from any controller action:

```php
use Spatie\LaravelMarkdownResponse\MarkdownResponse;

class DocsController extends Controller
{
    public function show(string $slug): MarkdownResponse
    {
        $content = // fetch your Markdown content...

        return new MarkdownResponse($content);
    }
}
```

Or register a route with an automatic Markdown counterpart:

```php
use Spatie\LaravelMarkdownResponse\MarkdownResponse;

Route::get('/docs/{slug}', function (string $slug) {
    return new MarkdownResponse(
        view: 'docs.show',
        data: ['slug' => $slug],
    );
})->withMarkdownRoute();
```

Visiting `/docs/introduction.md` (or sending `Accept: text/markdown`) will return the Markdown version; `/docs/introduction` returns the normal HTML view.

## Resources
- [GitHub](https://github.com/spatie/laravel-markdown-response)
- [Docs](https://spatie.be/docs/laravel-markdown-response/v1/introduction)
- [Laravel News](https://laravel-news.com/serve-markdown-versions-of-your-laravel-pages-to-ai-agents)
- [[Laravel Packages]]
