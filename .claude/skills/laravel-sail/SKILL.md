---
name: laravel-sail
description: "Use when the Laravel project runs under Laravel Sail. Trigger for Docker/Sail workflows, running artisan, composer, npm, or PHP only inside containers. Covers: ./vendor/bin/sail up/down, sail artisan, sail composer, sail npm, and never running host PHP/Composer against a Sail-only app by mistake."
license: MIT
metadata:
  author: laravel
---

> **Synced from** [`laravel/boost`](https://github.com/laravel/boost) @ `14a5c6ab6729a8bb108bc5a29280fe53e5da6abd` — `.ai/sail/core.blade.php`. Regenerate: `python3 scripts/sync-boost-ai-skills.py`.

# Laravel Sail

- This project runs inside Laravel Sail's Docker containers. You MUST execute all commands through Sail.
- Start services using `./vendor/bin/sail up -d` and stop them with `./vendor/bin/sail stop`.
- Open the application in the browser by running `./vendor/bin/sail open`.
- Always prefix PHP, Artisan, Composer, and Node commands with `./vendor/bin/sail`. Examples:
    - Run Artisan Commands: `./vendor/bin/sail artisan migrate`
    - Install Composer packages: `./vendor/bin/sail composer install`
    - Execute Node commands: `./vendor/bin/sail npm run dev`
    - Execute PHP scripts: `./vendor/bin/sail php [script]`
- View all available Sail commands by running `./vendor/bin/sail` without arguments.
