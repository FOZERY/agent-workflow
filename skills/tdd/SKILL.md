---
name: tdd
description: "Write independent, test-first checks for agreed behavior using the project's test policy."
disable-model-invocation: true
---

# Test-Driven Development

Use this skill only on the user's explicit request. It is optional: implementation still follows the project's required verification when TDD is not selected.

## 1. Establish the test contract

Read root `AGENTS.md` (or the project's `CLAUDE.md`) and its testing references, relevant requirements, domain vocabulary and accepted decisions. Inspect existing tests and test commands. Project policy determines test levels, boundaries, fixtures, mocking, naming, coverage priorities and permitted infrastructure; this skill supplies no universal integration-test or coverage quota.

Identify the behavior to protect, the observable interface and the meaningful failure each proposed test would catch. Reuse already-agreed boundaries; ask only about missing decisions or a conflict with requirements. Prefer the smallest test that proves the required behavior. Adding SQL does not by itself justify a database container or a new integration suite. If the permitted unit tests cannot establish a required database property, explain that gap and ask rather than expanding infrastructure or claiming coverage.

**Done when:** the selected behaviors, test level, scope, commands and infrastructure permissions are known.

## 2. Launch the independent test author

You stay the implementer in the current thread. The test author is a fresh subagent you launch: the Agent tool in Claude Code, `spawn_agent` in Codex, a task subagent in OMP. Use the test-author role and model from the project contract; without one, use the client's general-purpose subagent.

Give the author:

- This skill's path and its references, so it can follow the red step.
- The behavior for the current cycle, its requirement and acceptance criteria.
- The agreed interfaces, project testing rules and the narrow test command.
- File ownership: the author writes and edits test files only.

Leave out your plan, draft code and any explanation of the intended solution. The tests live in the shared working copy, so no commit or transfer step is needed.

If the client cannot launch a subagent, ask the user to choose: open a separate session for the test author with the same brief, or let you write the tests and report them as not independent.

**Done when:** the test author has a requirements-only brief, or the user has chosen a fallback.

## 3. Run red/green cycles

Each cycle covers exactly one behavior: one test, then the minimal code that passes it. Finish a cycle before starting the next one.

1. **Red (test author).** Write one focused behavioral test, with expected results taken from the requirements or an independently worked example; [test-quality guidance](references/tests.md) and, when test doubles are needed, [mocking guidance](references/mocking.md) apply within the project contract. Run the narrow command and show that the failure comes from the missing behavior, not a broken fixture, a missing dependency or the environment. Return the test path, the behavior covered, the exact command and the observed failure. If the test already passes, report that; the behavior needs no new code.
2. **Green (implementer).** Write only enough production code to make that test pass, then run it. Test files belong to the author: when a test looks wrong, send it back with the requirement it conflicts with.
3. **Refactor (implementer).** Improve the code while the tests stay green, within project policy.
4. **Next cycle.** Send the author the next behavior. Continue the same subagent where the client allows it; otherwise launch a fresh one with the brief and the tests written so far.

Resolve disagreements from the accepted requirements, keeping assertions as strong as the requirement demands.

**Done when:** each selected behavior went red and then green in the shared working copy, or the reason a cycle could not go red is reported.

## 4. Report the evidence

For each behavior, report the test, its red evidence and its green result on the integrated revision, plus failures, unrun checks and coverage limits. If the project chose parallel test authorship instead of cycles, report the result as independent testing, not test-first TDD.

**Done when:** the report covers every selected behavior. It is evidence for review, not human acceptance or delivery permission.
