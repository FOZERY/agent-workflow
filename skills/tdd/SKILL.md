---
name: tdd
description: "Write tests that prove real behavior, test first: integration and module tests through the real flow of the application, with mocks only at external boundaries. Use when implement calls it, when the user wants to build or fix something test-first, or when the user wants to know whether existing tests prove anything."
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, use this skill's defaults. In your report, say once that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex).

# Test-Driven Development

A test proves that a real behavior of the application works. Write a test only when you can name the realistic bug that would make it fail.

When exploring the codebase, read `GLOSSARY.md` (if it exists) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching. Read the project's testing rules and use its test commands.

## 1. Decide whether a test fits

Write a test for a behavior with an input and an observable result that an independent source pins down: business logic, a request and response contract, a state change, a transformation, validation.

Write no new test for configuration, wiring, glue code, trivial getters, constants or the framework's own behavior. Write none when it would need brittle mocks, production-only state or large unrelated fixture churn. Use the closest executable check instead, such as a reproduction command or `verify`, and name it in your report.

## 2. Choose the level

Take the highest level that stays fast and deterministic:

1. **Integration test of a flow.** Enter through a real entry point of the application: an HTTP route, a CLI command, a job handler, a page with only the network faked. Run the real modules, the test database of the project and the real side effects.
2. **Module test.** Call the public interface of one module with its real internal collaborators. Use it when the flow cannot reach a case cheaply, such as many inputs of a calculation.
3. **Browser and end-to-end tests.** Write them only after the behavior works at a faster level. `verify` checks the running product.

Test at the layer that the claim names: an HTTP response does not prove what the page shows. Do not extract a helper only to give it a test.

## 3. Agree the seams

A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside.

**Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user. No test is written at an unconfirmed seam. Seams listed in an approved plan, in the orchestrator's assignment or by the user for this task count as confirmed; confirm only seams you add.

Ask: "What's the public interface, and which seams should we test?" For each proposed seam, give its level and one line on what it catches and what it misses.

## 4. Run the loop

1. List the behaviors to prove at the agreed seams, one line each.
2. Take the next behavior. Name the realistic bug that its test must catch.
3. Write one test for it. Write the expected value as a literal from the requirement.
4. Run it. It must fail because the behavior is missing or wrong, such as an unknown command or a wrong value. If it fails in the test setup, passes, or fails for another reason, fix the test first.
5. Write only enough code to pass it. Run it again.
6. Go to step 2. Write the next test only after this one passes.
7. Run the project's full test suite.

For a bug, the first behavior is the reported one. Its test reproduces the bug and fails for the reported reason before you change the code. If the bug is flaky, make the test deterministic. Add tests for related failures only after the fix.

Refactoring is not part of the loop. `simplify-codebase` does it after the implementation.

## 5. Check each test

- **Two edits.** Break the behavior, for example return a wrong value or skip an effect: the test must fail. Change only the internals and keep every observable result: the test must pass. The red run in step 4 is the first edit. Judge the second by reading the test.
- **Real collaborators.** Mock only external boundaries: network services, payment, email, the clock and randomness. Use the project's test database, not a database mock. Keep real the side effects that the test depends on. Never assert on a mock. Read [mocking.md](mocking.md) when you add a mock.
- **Independent expected values.** Take them from the requirement, a worked example or a known literal, never from the code under test.
- **State, not calls.** Assert what a caller can observe: the result, the stored state that the interface reads back, the error type that callers branch on.
- **Tests follow the requirement.** Do not change a test to match a wrong implementation. Weaken an assertion only when the required behavior changed, and say why.

Signs of a bad test:

- **Implementation-coupled**: mocks internal collaborators, tests private methods, or verifies through a side channel. It breaks on a refactor that keeps the behavior.
- **Tautological**: the assertion recomputes the expected value the way the code does, so it passes by construction.
- **The harness does the job**: a mock or a fixture supplies the behavior, the ordering or the stored state that production must create.
- **The wrong cause goes red**: a negative case fails on a different guard, or never reaches the intended branch.

See [tests.md](tests.md) for examples.

## 6. Report

- For each new test: its level, the bug that it catches, the red output before the code and the green output after it.
- For each behavior that you checked without a new test: the check and the reason.
- The result of the full test suite.

## Review existing tests

Judge existing tests by the same rules. For each test, name the realistic bug that would escape if it disappeared. These signs mark a test that proves nothing:

- **Exercise without a claim**: it runs lines, copies identities or lists exports, and still passes on broken behavior.
- **Change detector**: only a deliberate decision can fail it, such as a constant's value, a message's wording or a private structure. If users depend on the value, such as a default data path or a wire format, test it through behavior instead.
- **Declaration posing as behavior**: source greps, import lists and call-shape checks pass while the user path is broken.
- **One proof repeated**: several tests or layers protect the same contract with the same scenario.
- **Tests keeping code alive**: a helper or a production hook exists only because tests call it.

Give each test one verdict: keep, repair, combine or remove. Repair a test that catches only part of its bug, such as a message without the stored state. For an audit or a pruning batch, read [audit.md](audit.md). Keep a test until you can name the stronger test that covers its bug.

## In a subagent

When the project runs TDD in a subagent, the launching session passes the requirements, the interface and the confirmed seams. The subagent writes the failing test for one seam, runs it, and returns the test path and the red result. It gets no implementation plan. The launching session writes the code that makes the test pass.
