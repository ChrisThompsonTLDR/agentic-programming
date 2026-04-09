---
name: tdd
description: Test-Driven Design (TDD) for Laravel work—red/green/refactor, Pest-first workflow, grouping, mocks, browser and architecture tests, coverage and type gates. Use when implementing features, fixing bugs with tests first, or structuring a test suite.
license: MIT
metadata:
  author: agentic-programming
  version: "1.0"
---

# Test-Driven Design (TDD)

**Test-Driven Design** is the same loop as classic TDD—**red → green → refactor**—used deliberately to shape APIs, boundaries, and seams before production code hardens. Tests express the behavior you want; the implementation follows. Prefer small steps: one failing assertion at a time, minimal code to pass, then refactor with a green suite.

## When to use

- New behavior: write or extend a **failing** test that names the outcome, then implement until green.
- Bugfixes: reproduce with a test that fails today, then fix until green (regression locked in).
- Refactors: keep tests green while changing structure; add tests only where behavior was implicit.
- Reviews / CI: you need fast default runs plus optional slow groups (browser, integration).

## Laravel + Pest

This repo’s **Pest** stack is summarized in [[laravel-packages/pestphp__pest]] (file: `.steering/laravel-packages/pestphp__pest.md`). Use **Pest** on top of PHPUnit for expressive tests; follow its [installation](https://pestphp.com/docs/installation) and [continuous integration](https://pestphp.com/docs/continuous-integration) docs for project setup and CI.

### Pest docs to keep handy

| Topic | Why it matters for TDD |
|--------|-------------------------|
| [Grouping tests](https://pestphp.com/docs/grouping-tests) | Put slow or flaky paths (e.g. browser) in named groups; default CI runs fast groups, scheduled jobs run `--group=browser` (or similar). Configure in `Pest.php` with `pest()->…->in('…')` or per-test `->group()`. |
| [Mocking](https://pestphp.com/docs/mocking) | Isolate the unit under design: mock HTTP clients, queues, and external services with Mockery so tests fail for **your** logic, not network reality. |
| [Browser testing](https://pestphp.com/docs/browser-testing) | After core behavior is covered with fast tests, add a thin **end-to-end** slice for critical user journeys (Pest 4 + plugin). |
| [Architecture testing](https://pestphp.com/docs/arch-testing) | Encode **design rules** (e.g. “controllers don’t talk to DB directly”) as automated checks so refactors can’t erode structure silently. |
| [Test coverage](https://pestphp.com/docs/test-coverage) | Use Xdebug 3+ or PCOV; `--coverage --min=…` to gate merges when the team agrees on a threshold. |
| [Type coverage](https://pestphp.com/docs/type-coverage) | Optional `pestphp/pest-plugin-type-coverage`: enforce typed surface area alongside tests via `--type-coverage --min=…`. |

## Workflow (agent checklist)

1. **Red** — Add the smallest test that describes missing behavior (name reads like a spec).
2. **Green** — Write only enough application code to pass; no speculative features.
3. **Refactor** — Improve names and structure with tests still green.
4. **Boundaries** — At I/O edges, use mocks/fakes ([mocking](https://pestphp.com/docs/mocking)); keep domain tests fast and deterministic.
5. **Layers** — When the module graph matters, add or extend [architecture tests](https://pestphp.com/docs/arch-testing).
6. **Confidence ladder** — Unit/feature tests first; add [browser tests](https://pestphp.com/docs/browser-testing) for journeys that justify the cost; use [groups](https://pestphp.com/docs/grouping-tests) so `./vendor/bin/pest` stays quick locally and in PR CI.
7. **Quality gates** — Turn on [coverage](https://pestphp.com/docs/test-coverage) and, if desired, [type coverage](https://pestphp.com/docs/type-coverage) where the team has agreed thresholds.

## Anti-patterns

- Writing a large chunk of production code before any test (harder to validate seams).
- Testing implementation details (private methods, exact call order) instead of observable behavior.
- Running every browser test on every push with no grouping—burns time and hides real failures in noise.

## Related

- Internal note: `.steering/laravel-packages/pestphp__pest.md` (`[[laravel-packages/pestphp__pest]]` in Obsidian when that folder is in the vault).
- [Pest upgrade guide](https://pestphp.com/docs/upgrade-guide) when bumping major versions.
