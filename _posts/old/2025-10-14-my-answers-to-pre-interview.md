---
layout: single
title: "My answers to pre-interview"
date: 2025-10-14T18:29:14.136Z
permalink: /blog/my-answers-to-pre-interview/
tags: ["job-prep", "knowledge"]
categories: ["blog"]
---

These were interesting questions to answer. I have limited knowledge in this field, and I tried my best.

Hello xxxxx, 

Thank you for the opportunity. Below are my answers.

### **Screening and Evaluation Questions**

**How do you differentiate unit testing from integration testing? Give examples of when each is most appropriate in a micro-services or modular codebase.**

- *Unit testing is precise and focuses on individual components in complete isolation. Integration testing. Integration testing tests multiple components together under real conditions.*
- *Example: At Globalnet, I built scalable automation tools using Python, Flask, and REST APIs.*
   - *Unit tests verified input/ output for isolated functions like device configuration parsing, customer data retrieval logic from upstream systems, and API request payload validation.* 
   - *Integration tests used to verify the main API endpoint flow. Ensuring the Flask API route correctly handled an HTTP requests, persisted the new customer record from/ to the database, and successfully called Powercode APIs to create customer account, ticket, equipment, etc.*


**When setting a target test-coverage percentage, do you ever aim for 100%? Why or why not? What trade-offs do you consider?**
 - *I don't. It will require way more time to cover 100% and it's not worth effort to write complex tests for simple code. Then main trade-offs I consider: Time vs value; maintainability*

**Describe your experience with tools like semantic-release or Google’s release-please. How would you extend or replace their heuristics with ML to highlight changelog entries based on actual code diffs?**
 - *I have experience with CI/CD tooling like Github Actions and Jenkins for configuration management. I haven't used semantic-release directly, but my experience with automation pipelines provides the basis for understanding automated versioning and release logic.*
 - *Instead of just using commits messages, I would include the actual code change with git diff, and what files were changed.*

**How would you design a release pipeline that enforces minimum coverage thresholds (pulled from services like Codecov or Coveralls) before publishing a new version?**
 - *I would use Github Actions as required step before the deployment:*
   - *Run tests and get coverage report, upload report and calculate the coverage delta for the current branch*
   - *Then pipeline would use service integration to fetch the current coverage percentage*
   - *Add conditional step*
   - *If the condition fails, the job fails, and pipeline is blocked from proceeding to the publish stage.*

**Suppose you need to map a `git diff origin/main…origin/develop` patch to affected API docs. What techniques or ML models would you use to identify which sections of the docs must be updated?**
 - *I would try to use hybrid approach, static analysis and text embedding models.*
 - *I’d extract the code symbols from the diff using an AST parser. Then, I’d embed both code snippets and doc sections using a some model and compute cosine similarity*

**How would you integrate auto-generated doc changes into a Git-based review process (e.g. opening PRs/MRs) to ensure human oversight?**
 - *When dev creates pull request with code changes, Github Action runs the documentation generation tool like Sphinx for Python*
 - *The tool compares the new generated documentation against the documentation in target branch, and if a diff is found, the job fails with a warning about the change*
 - *In mature setup, the CI job would automatically commit generated doc to developer branch and push the commit back to pull request*
 - *Then the manual review.*

**Have you used AI or property-based testing to auto-generate unit or integration tests? Describe the setup, how you prioritized test cases, and what success metrics you tracked.**
 - *I’ve used AI-assisted code generation to bootstrap initial unit tests — primarily with Python-based APIs. Using pytest and hypothesis.*

**How would you train a model (e.g., using historical CI logs) to flag tests that are likely to be flaky? What data would you collect, and how would you act on the predictions?**
 - *That's tougher I haven't done this yet. But I would collect test names/ module, run timestamp, duration of test, pass/ fail result, environment metadata.*
 - *I would use other model with all the collected info to train current model*
 - *And then implement logic to tag if test stable or flaky.*

**In a large monorepo, how would you configure CI (e.g. GitLab CI, GitHub Actions) so that only tests impacting changed files are run, without sacrificing overall confidence?**
 - *I’d use a dependency graph that maps source files to test suites.*
 - *When a commit lands, a script inspects the git diff and looks up affected test groups.* 
 - *Only those run in CI.*

**You’re building a Dart-based CLI assistant that suggests code fixes in the terminal. Which Dart or ANSI-terminal packages would you choose for syntax highlighting, interactive menus, and progress bars?**
 - *My dart/ flutter experience is only based on my Expenses tracker app that I recently started developing. From quick searching, I would use ansicolor, dart-cli and cli_progress_bar.*

**How would you detect the user’s current file or project context in a CLI and surface targeted refactoring recommendations?**
 - *Check working directory with pwd to infer the root project directory by searching for configuration file.*
 - *Once CLI identifies project scope, it could extract metadata, use embeddings, parse active files via LSP.*

**For a Dart/Flutter monorepo, how would you ensure coordinated version bumps and dependency updates across multiple packages—similar to Melos?**
 - *I'd do something like this:*
   - *Parse all pubspec.yaml files in the workspace.*
   - *Build a dependency graph*
   - *When one package updates, propagate compatible version updates to dependent packages automatically.*
   - *Enforce version consistency checks during*
   - *Integrate a changelog generator tied to Git commit messages*

**Describe how you’d let users define pre-release hooks or bespoke versioning strategies in a hosted package-management service.**
 - *I’d allow users to define pre-release hooks in a config file*

**Beyond `dart test` and Mockito, what Dart testing or mocking libraries have you used (e.g. `test_cov`, `mocktail`, `dart_fzzt`)? How do they compare in ergonomics and feature set?**
 - *I have not used Dart-specific testing libraries, as my experience is primarily in Python, Go, and network engineering. In Python, I rely on tools like pytest for unit testing and requests-mock or unittest.mock for mocking services.*

**Show a snippet or outline of how you’d test a Stream-emitting service in Dart, including error and completion cases.**
 - *Since I do not have specific Dart experience, this is an outline based on general reactive programming principles and the Dart Stream API:*

 `// Assume a service that returns a Stream of data
abstract class DataService {
  Stream<String> getDataStream();
}

void main() {
  test('emits data, completes, and handles errors', () {
    final mockService = MockDataService();

    // 1. Define the Stream behavior for the mock
    when(() => mockService.getDataStream())
        .thenAnswer((_) => Stream.fromIterable(['data1', 'data2']));

    // 2. Use the stream matchers (provided by a library like 'test_api')
    expect(
      mockService.getDataStream(),
      // 3. Define the expected sequence of events
      emitsInOrder([
        'data1',
        'data2',
        emitsDone, // Ensures the stream closes cleanly
      ]),
    );

    // --- Error Case Test ---
    test('emits error and stops', () {
      when(() => mockService.getDataStream())
          .thenAnswer((_) => Stream.error(Exception('Network Error')));

      expect(
        mockService.getDataStream(),
        // 4. Expect a specific error to be emitted
        emitsError(isA<Exception>()),
      );
    });
  });
}`

**As a codebase grows, how do you structure a test harness so new modules can plug in without duplicating setup or tear-down logic?**
 - *I would adopt the Pytest fixture pattern: *
   - *Centraziled base test class*
   - *Module-specific setup*
   - *Parameterized test data*

**Have you built end-to-end pipelines (GitHub Actions, GitLab CI, Jenkins) that run tests, collect coverage, and trigger releases? Walk us through a specific example and the biggest challenge you encountered.**
 - *Yes. I built a GitHub Actions pipeline for an internal automation system, but it does not collect coverage and trigger releases.*

**How would you feed AI-driven test-failure predictions or code-quality scores back into a CI pipeline to block or warn on risky merges?**
 - *I would integrate the AI prediction into the pull request status check flow in GitHub.*

**Describe how you’ve integrated an LCOV-based coverage tool into CI, and how you made the resulting reports actionable for developers.**
 - *I haven’t directly integrated LCOV yet, but I’ve built CI pipelines that run automated tests, collect results, and gate releases based on pass/fail logic. I understand how LCOV would fit into that flow — generating coverage data, uploading reports in CI, and using the results to highlight weakly tested modules for developers to improve.*

**What systematic steps do you take to identify, isolate, and fix flaky tests in an automated test suite?**
 - *I rerun failing tests multiple times to confirm non-determinism, then check logs, timing, and dependency states. Once confirmed flaky, I isolate them in a “quarantine” group, review async or network-related code, and add mocks or controlled waits. After fixing, I monitor their stability across several CI runs before re-enabling them.*

**How do you document a complex testing framework so that new engineers can onboard rapidly? Share a structure or toolchain you’ve used.**
 - *I keep docs lightweight and practical — a single README explaining test structure, setup steps, and examples. For larger systems, I add diagrams and short “how-to” guides in Markdown. The goal is that a new dev can clone the repo, run tests, and understand the flow in under 10 minutes.*

**When improving or refactoring existing test suites, how do you avoid causing large disruptions to active development cycles?**
 - *I refactor in small, incremental PRs and run both the old and new test harnesses in parallel until stability is confirmed. Communication is key — I give teams a heads-up before changing test behavior and make sure existing pipelines stay green during the transition.*

**After a merge causes coverage to drop, what’s your investigation workflow? Which logs, diffs, or metrics do you consult, and how do you remediate?**
 - *First, I check the diff for skipped tests or untested branches. Then I review coverage reports and CI logs to pinpoint which files dropped. I prioritize fixing or adding tests for critical logic first, then automate a follow-up check in the next build to confirm recovery.*

**Tell us about a time you had to overhaul or adapt your testing approach because it didn’t fit with your team’s processes. What compromise or innovation did you introduce?**
 - *When I introduced automated backend testing at GlobalNet, the team was used to manual verification. I adapted by integrating tests into existing deployment scripts instead of forcing a separate workflow. It made testing feel like part of deployment, not an extra step — adoption shot up.*

**How do you work with developers who deprioritize testing? Give an example of how you’ve influenced better practices or provided tools to make testing less onerous.**
- *I lead by showing value, not lecturing. I’ve built simple automation that catches config errors before production — once developers saw it save time, they naturally started writing their own tests. Making testing painless is the best persuasion tool.*
---

## SPECIFIC PREVIOUS STARTUP EXPERIENCE

1. What is your specific experience with equity/cash split compensation models. Specifically have you participated in this in a startup before?
 - *I have not previously participated in an equity/cash split compensation model at a startup. My professional experience has been primarily with established companies, including GlobalNet Inc. and Best Western. I am keen to explore and understand this model as I transition into the startup environment.*

2. Which level of startups have you participated in previously (list below)? The more specific the better.

- pre-pre seed (MVP) (Startups generally with 5 - 10K in funding)
- pre seed (first revenue) (Startups with 50K - 250K in funding)
- seed (first outside hire other than founders and core leaders) (250 -1M in funding)
- Bridge Loan (growth expansion without diluting equity) (varies)
- Series A (pre for acquisition) 1-20M in funding
- Series B (pre for acquisition) 20M-100M in funding
- Series C (pre for acquisition) 100+ in funding
- Company more than 10 years old (Legacy companies)

- *Based on the list provided, I have not participated in a company at the pre-seed through Series C stages.
The companies I have worked for would fall under Company more than 10 years old (Legacy companies), as GlobalNet Inc. is an established provider. However, I bring a startup-like mindset to problem-solving, as evidenced by my work on architecting and deploying scalable backend automation systems.*
