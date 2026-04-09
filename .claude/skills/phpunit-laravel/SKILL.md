---
name: phpunit-laravel
description: "Use when writing or running PHPUnit tests in a Laravel app that uses PHPUnit (not Pest). Trigger for test classes, assertions, make:test --phpunit, or running the test suite. Covers: creating tests, running filtered tests, and treating tests as core code that must not be removed without approval."
license: MIT
metadata:
  author: laravel
---

> **Synced from** [`laravel/boost`](https://github.com/laravel/boost) @ `14a5c6ab6729a8bb108bc5a29280fe53e5da6abd` — `.ai/phpunit/core.blade.php`. Regenerate: `python3 scripts/sync-boost-ai-skills.py`.

# PHPUnit

- This application uses PHPUnit for testing. All tests must be written as PHPUnit classes. Use `php artisan make:test --phpunit <name>` to create a new test.
- If you see a test using "Pest", convert it to PHPUnit.
- Every time a test has been updated, run that singular test.
- When the tests relating to your feature are passing, ask the user if they would like to also run the entire test suite to make sure everything is still passing.
- Tests should cover all happy paths, failure paths, and edge cases.
- You must not remove any tests or test files from the tests directory without approval. These are not temporary or helper files; these are core to the application.

## Running Tests
- Run the minimal number of tests, using an appropriate filter, before finalizing.
- To run all tests: `php artisan test --compact`.
- To run all tests in a file: `php artisan test --compact tests/Feature/ExampleTest.php`.
- To filter on a particular test name: `php artisan test --compact --filter=testName` (recommended after making a change to a related file).
**Command prefix:** Use `php artisan` on the host or `./vendor/bin/sail artisan` when using Sail.

