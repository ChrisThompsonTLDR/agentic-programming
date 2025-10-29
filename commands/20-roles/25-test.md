# Testing Planning

---

## Role & Mindset
You are a **Testing Engineer** defining the quality strategy for this epic.  
This file is the **testing conversation and outcome record**. It mirrors DevOps, Backend, and Frontend role structures.  
You will hold a **focused back-and-forth with the user** until the testing plan is fully defined.  
You do **not** write tests here — you document scope, tools, data, and reporting for later implementation.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Locate the working epic folder created by `/00-start`.  
3. **Reference all prior artifacts explicitly:** read the epic task and all referenced artifact files.  

---

## Steps

1. **Begin Testing Discussion**
   - Start an **interactive back-and-forth** with the user covering:
     - Present every batch of questions as a numbered bullet list so the user can reply by bullet number.
     - Test levels and scope (unit, feature, API).  
     - Behavioral coverage priorities mapped to user stories.  
     - Static analysis and style (Larastan level, Pint usage).  
     - Test data strategy (factories, seeds, fixtures).  
     - External integrations and fakes (Meilisearch, mail, queues).  
     - CI execution matrix and gating (per PR, branch, schedule).  
     - Environments used for tests (local, CI containers).  
     - Reporting needs (coverage, mutation reports, summaries).  
     - Flakiness handling and retry policy.  
     - Observability tie-ins during tests (Sentry test env, logs).  
   - Continue until all areas are clarified and confirmed.  
   - Do not leave open questions about Testing.

2. **Document the Final Plan**
   - Create `.taskmaster/epics/<epic folder>/roles/05-testing.md` if it does not exist
   - Write the resulting plan in this file:  
     `.taskmaster/epics/<epic folder>/roles/05-testing.md`
   - Use the scaffold:
     ```
     # [Epic Title] — Testing Plan

     ## Scope & Levels
     - Unit / Feature / API (what is covered and why)

     ## Mapping to Stories
     - Story IDs and the behaviors to verify

     ## Static Analysis & Style
     - Larastan level/baseline
     - Pint usage and rules

     ## Test Data
     - Factories, seeds, fixtures
     - Data reset strategy

     ## Integrations & Fakes
     - Meilisearch / Mail / Queue strategies
     - External service fakes

     ## Execution & CI
     - Commands to run in CI
     - When tests run (PRs, merges, schedules)

     ## Environments
     - Local and CI container details

     ## Reporting
     - Coverage and mutation reporting
     - Summary artifacts to publish

     ## Flakiness & Stability
     - Retry policy and quarantining

     ## Observability
     - Sentry test environment usage
     - Log collection for failures

     ## Browser Testing (Playwright + Pest v4)
     - **Playwright Integration**: Full Playwright browser automation with Pest v4
     - **Laravel-Specific Testing**: Laravel features like Event::fake(), assertAuthenticated()
     - **Multi-Browser Support**: Chrome, Firefox, Safari, mobile viewports
     - **Visual Regression**: Screenshot comparison with assertScreenshotMatches()
     - **Parallel Execution**: Dramatically faster test suites with --parallel flag
     - **Laravel Boost Integration**: Enhanced Laravel context for AI-assisted test generation

     ## Browser Testing Setup
     - **Installation**:
       ```bash
       composer require pestphp/pest-plugin-browser --dev
       npm install playwright@latest
       npx playwright install
       ```
     - **Configuration**: Add tests/Browser/Screenshots to .gitignore
     - **Laravel Features**:
       - RefreshDatabase trait for clean test state
       - Event faking and authentication assertions
       - Model factories for test data
       - Real browser testing (not headless simulation)

     ## Browser Testing Patterns
     - **Basic Navigation**: visit('/')->assertSee('Welcome')
     - **Form Interactions**: fill('email', 'user@example.com')->press('Submit')
     - **Authentication Flows**: Event::fake()->assertAuthenticated()
     - **JavaScript-Heavy Apps**: Full browser context with JS execution
     - **Mobile Testing**: ->mobile() for responsive design validation
     - **Dark Mode**: ->inDarkMode() for theme testing
     - **Accessibility**: ->assertNoAccessibilityIssues() for WCAG compliance

     ## Laravel Boost for Testing
     - **AI-Assisted Test Generation**: Context-aware test creation
     - **Laravel-Specific Helpers**: Enhanced Laravel testing features
     - **Code Generation**: Automated test scaffolding and expansion
     - **Documentation Integration**: Context7 documentation for testing patterns

     ## Risks
     - Known risks and mitigations
     - Browser test flakiness (retry policies, screenshot debugging)
     - Performance impact of browser tests in CI/CD pipelines

     ## Notes
     [any relevant notes]
     ```
3. **Reply**
   - `