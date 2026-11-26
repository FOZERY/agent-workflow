---
name: tdd
description: Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", wants integration tests, or wants to audit or prune existing tests.
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, use this skill's defaults. In your report, say once that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex).

# Test-Driven Development

TDD is the red → green loop. This skill is the reference that makes that loop produce tests worth keeping: what a good test is, where tests go, the anti-patterns, and the rules of the loop. Every section applies on every cycle: consult them before and during the loop, not after.

When exploring the codebase, read `GLOSSARY.md` (if it exists) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching.

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification: "user can checkout with valid cart" tells you exactly what capability exists, and it survives refactors because it doesn't care about internal structure.

Check each test against two edits. Break the behavior, for example return a wrong value or skip an effect: the test must fail. Change only the internals and keep every observable result: the test must pass. The red run before the code is the first edit. Judge the second by reading the test. Derive the expected value from the requirement. Assert the error type that callers branch on, not the message.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidelines.

## When the loop fits

Use the loop for a behavior with an input and an observable output that an independent source pins down: business logic, a request and response contract, a transformation, validation.

Write no new test when it would need broad harness setup, brittle mocks, slow end-to-end infrastructure, production-only state or large unrelated fixture churn. Write none when nothing independent says what the result must be, as with configuration, wiring and glue code. Use the closest executable check instead, such as a targeted script, a reproduction command or `verify`, and name it in your report.

## Fixing a bug

1. Write the test that would have caught the bug. It encodes the intended behavior, not the current code.
2. Run it before you fix anything. It must fail for the reported reason. If it passes or fails for another reason, correct the test or the reproduction first.
3. Make the smallest fix that passes it, and keep the nearby contracts.
4. Run it again, and the other tests of that area if the project has them.

If the bug is flaky, make the test deterministic. Land the focused regression test first. Add tests for related failures only after it.

## Seams: where tests go

A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals.

**Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user. No test is written at an unconfirmed seam. Seams listed in an approved plan, in the orchestrator's assignment or by the user for this task count as confirmed; confirm only seams you add. You can't test everything, so agreeing the seams up front is how testing effort lands on the critical paths and complex logic instead of every edge case.

Ask: "What's the public interface, and which seams should we test?" Give each proposed seam a one-line note on what it catches and what it misses.

## Anti-patterns

- **Implementation-coupled**: mocks internal collaborators, tests private methods, or verifies through a side channel (querying the database instead of using the interface). The tell: the test breaks when you refactor but behavior hasn't changed.
- **Tautological**: the assertion recomputes the expected value the way the code does (`expect(add(a, b)).toBe(a + b)`, a snapshot derived by hand the same way, a constant asserted equal to itself), so it passes by construction and can never disagree with the code. Expected values must come from an independent source of truth: a known-good literal, a worked example, the spec.
- **Exercise without a claim**: the test runs lines, copies identities or lists exports, so coverage rises but no credible defect can be detected. The tell: the assertions still pass on broken behavior.
- **The harness does the job**: a mock implements the behavior the test claims to prove, a fixture supplies the acknowledgement or ordering that production must create, or a persistence check reads a store that the real path never writes. One identical fake for different dependency APIs hides their differences.
- **The wrong cause goes red**: a negative case fails on a different guard, or never reaches the intended branch. Check the failing condition, not only that something rejected the input.
- **Declaration posing as behavior**: source greps, import lists, capability flags and call-shape checks certify the declaration while the user path is broken. Test the behavior that the declaration promises.
- **One proof repeated**: private helper tests, per-provider replays of shared logic and several layers that run the same regression scenario all protect one contract. Keep distinct transport and lifecycle risks, not copies of one scenario.
- **Tests keeping code alive**: a helper or production escape hatch exists only because tests call it. Test the real entry point and remove the hook, not replace it with another test-only abstraction.
- **Horizontal slicing**: writing all tests first, then all implementation. Bulk tests verify _imagined_ behavior: you test the _shape_ of things rather than user-facing behavior, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in **vertical slices** instead: one test → one implementation → repeat, each test a **tracer bullet** that responds to what the last cycle taught you.

## Rules of the loop

- **Red before green.** Write the failing test first, then only enough code to pass it. Don't anticipate future tests or add speculative features.
- **One slice at a time.** One seam, one test, one minimal implementation per cycle.
- **Refactoring is not part of the loop.** It belongs to `simplify-codebase` after the implementation, not the red → green implementation cycle.
- **Tests follow the requirement.** Do not change a test to match a wrong implementation. Weaken an assertion only when the required behavior changed, and say why.
- **Slow tests last.** Write browser and end-to-end tests after the behavior works at a faster seam. `verify` checks the running product.

## Report

For each new test, give the red output before the code and the green output after it. For each behavior that you checked without a new test, name the check and the reason.

## Auditing existing tests

To audit or prune existing tests, read [audit.md](audit.md). Use the anti-patterns above as investigation prompts, not as automatic removal rules.

## In a subagent

When the project runs TDD in a subagent, the launching session passes the requirements, the interface and the confirmed seams. The subagent writes the failing test for one seam, runs it, and returns the test path and the red result. It gets no implementation plan. The launching session writes the code that makes the test pass.
