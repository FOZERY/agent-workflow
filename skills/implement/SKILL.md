---
name: implement
description: "Implement an agreed task, obtain independent review and hand it to the human for acceptance."
disable-model-invocation: true
---

# Implement a task

Requires the adapted `code-review` skill, including its `references/implementation-cycle.md`, and `plain-writing` for the parent's explanation of the implementation. Locate both installed packages and read the shared cycle before starting. If a dependency or required reviewer capability is unavailable, resolve it with the user rather than silently installing packages or substituting self-review.

## Defaults

Use these when the project instructions settle nothing for implementation, and mention once that `setup-agents-workflow` can configure the project.

- **Workspace:** the current checkout and branch. On the default branch, propose a task branch name and ask before editing.
- **Checks:** the commands in the project's scripts, task runner or CI configuration. While working, run the narrowest relevant ones, such as the type check and the affected test files; run the full required set once before review.

## 1. Establish the task and workspace

Read root `AGENTS.md` (or the project's `CLAUDE.md`) and the applicable requirement, testing, review and delivery sources. Fetch a supplied ticket through the project's authorized method and state its identity. A user-approved task description is also valid; neither a local spec nor an agent-owned tracker is required.

Identify scope, acceptance criteria and unresolved decisions. Confirm the repository, workspace/worktree and branch using configured defaults or the [defaults](#defaults); clarify ambiguous targets before editing. Respect working-copy ownership and unrelated changes. Creation of worktrees and implementation delegation follow the project procedure, not a mandatory topology.

Record the immutable base of the full task change before editing, reusing its original base on resumption. Include existing task commits and intended uncommitted work; keep unrelated changes outside the review scope.

**Done when:** the task, working copy, permitted changes, required checks and reviewer profile are known; blocking requirement decisions are resolved.

## 2. Implement and verify

Implement the agreed behavior using existing project patterns. Follow the project test policy: test levels, coverage priorities and infrastructure permissions, not an automatic full-suite or integration-test requirement.

TDD runs only when the user asks for it. Then read the installed `tdd` skill and run its cycles: you launch the test-author subagent and write production code for a behavior only after its test is red. Otherwise perform the required project verification without `tdd`. Report unmet verification requirements rather than creating unapproved test infrastructure.

Run the checks required for the affected work and retain their actual commands, results and revision. Resolve failures within scope; escalate changes in requirements, design or authority.

**Done when:** the approved implementation and required verification are ready for independent review, or a specific blocker needs the human.

## 3. Review, correct and obtain acceptance

Follow the installed `code-review` package's [shared cycle](../code-review/references/implementation-cycle.md) for independent review, permitted corrections, the plain-language implementation walkthrough and human decisions. If packages are installed separately, resolve this reference inside the installed dependency rather than assuming sibling paths.

After corrections or human feedback, repeat checks and fresh review of the current changes. `Ready for review` is not completion. Finish only when the human accepts the reviewed revision or explicitly ends the task, as defined by that cycle.

Commit only on the authorized project route, including an explicit human commit request. Do not automatically push, invoke `pr`, merge, close tracker items or remove worktrees; those actions need their own request or project authorization.
