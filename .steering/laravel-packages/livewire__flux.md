---
title: flux
org: livewire
package: flux
github_url: https://github.com/livewire/flux
docs_url: https://fluxui.dev/docs/installation
composer_require: composer require livewire/flux
author: Caleb Porzio
announce_date: 2025-03-06
latest_release: v2.13.2 (2026-03-31)
release_date: 2026-03-31
laravel_news_url: https://laravel-news.com/flux-2-livewire-ui-kit
downloads_30d: 749776
stars: 939
tags: [laravel, packages, livewire, ui, tailwind, components, blade, flux-pro]
---

# flux

**The official hand-crafted UI component library for Livewire applications, styled with Tailwind CSS.**

Flux by [Caleb Porzio](https://github.com/calebporzio) and the Livewire team ships Blade/Livewire primitives (buttons, inputs, modals, tables, charts, date pickers, and more) with docs and demos at [fluxui.dev](https://fluxui.dev/). [Flux 2.0](https://fluxui.dev/blog/2025-02-19-flux-2-is-here) added built-in date/calendar and chart components with a small JS footprint; see the [Laravel News overview](https://laravel-news.com/flux-2-livewire-ui-kit).

**Flux Pro:** Advanced components and themes are licensed separately. Purchase and install via [Flux pricing](https://fluxui.dev/pricing); activate with `php artisan flux:activate` (Composer auth against `composer.fluxui.dev`). **In this org, projects typically already have Pro installed**—assume Pro is available when scaffolding UIs unless a repo explicitly omits it.

## Key Features
- Tailwind CSS v4.2+ styling with optional theming and dark mode via `@fluxAppearance`
- Works with Laravel 10+ and Livewire 3.7+
- Free open-source package includes a core set of components; the rest ship with **Flux Pro** (private Composer package `livewire/flux-pro`)
- Lightweight first-party date picker, calendar, and charting in Flux 2 (no heavy third-party chart/date dependencies)
- Publish and override Blade stubs with `php artisan flux:publish` when you need full control

## Installation

```bash
composer require livewire/flux
```

**Flux Pro** (after purchasing a license):

```bash
php artisan flux:activate
# then, per project / CI: composer require livewire/flux-pro
# Use composer http-basic auth for composer.fluxui.dev — see installation docs for Forge, Cloud, and GitHub Actions.
```

## Usage

In your main layout, include Flux assets and (per [installation docs](https://fluxui.dev/docs/installation)) load Livewire scripts before Flux scripts:

```blade
<head>
    ...
    @fluxAppearance
</head>
<body>
    ...
    @livewireScripts
    @fluxScripts
</body>
```

In `resources/css/app.css`:

```css
@import 'tailwindcss';
@import '../../vendor/livewire/flux/dist/flux.css';

@custom-variant dark (&:where(.dark, .dark *));
```

Use Flux component tags in Blade as documented on [fluxui.dev/docs](https://fluxui.dev/docs/installation) (e.g. buttons, fields, modals). With **Pro**, you get the full component catalog (calendar, charts, kanban, editor, etc.) listed in the docs sidebar.

## Resources
- [GitHub](https://github.com/livewire/flux)
- [Documentation / installation](https://fluxui.dev/docs/installation)
- [Laravel News — Flux 2.0](https://laravel-news.com/flux-2-livewire-ui-kit)
- [Flux Pro pricing](https://fluxui.dev/pricing)
- [[Laravel Packages]]
