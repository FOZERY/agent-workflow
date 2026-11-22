---
name: refactor-codebase
description: "Find structural problems in the code after a stage of work, agree one fix with the user, and rewrite it with the behavior kept."
disable-model-invocation: true
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

# Refactor codebase

Find where the structure of the code makes it harder for people and agents to change, agree one fix with the user, then rewrite it with the behavior kept. The user runs this skill after a stage of work: several tasks, an epic. `implement` never starts it. `simplify-codebase` cleans the code of one task. This skill works on the structure across tasks.

Call the Skill tool with "codebase-design" for the vocabulary: **module**, **interface**, **depth**, **seam**, **adapter**, **leverage**, **locality**, and the deletion test. Use these terms exactly in every candidate. Do not write "component", "service", "API" or "boundary".

## Process

### 1. Pin the scope and the rules

Choose the scope in this order:

1. The module or pain point that the user names.
2. The commit range that the user gives: a commit, tag or branch where the stage began.
3. The hot spots of `git log`: the files that keep changing. If the changes are scattered, widen the scope.

Read the project's rules before you look at the code: `AGENTS.md`, the coding standards, the architecture notes, the linter and formatter configs, `GLOSSARY.md` and the ADRs of the area. An ADR is a decision. Reopen it only when the friction that you find is real, and say so in the candidate.

If the scope is empty, report that and stop.

**Done when:** the paths in scope, the range or hot spots behind them, and the rule sources are listed.

### 2. Check the baseline

Run the project's typecheck and the tests that cover the scope. If a check fails, stop and report. Do not refactor on red.

Record the current `HEAD` as the starting commit.

**Done when:** the checks pass, and the starting commit is recorded.

### 3. Simplify

Run `simplify-codebase` in a subagent with a fresh context. Give it the path from the `skill` setting of the project's `simplify-codebase` section and the files in scope as whole-file scope. The subagent only finds simplifications and returns them. Wait for its findings and do not edit the files meanwhile. Apply the findings yourself by step 6 of `simplify-codebase`. Run the typecheck and the covering tests again.

If subagents are unavailable, run `simplify-codebase` in this session. If the project has no `simplify-codebase` section, skip this step and say so.

Carry its proposals into step 4 as candidates.

**Done when:** every finding is applied or skipped with a reason, the checks pass, and the proposals are listed.

### 4. Scan

Delegate the scan to a subagent with a fresh context. If subagents are unavailable, scan in this session. Do not follow a fixed checklist. Read the code in scope and note where you meet friction through these lenses:

- **Depth.** Understanding one concept needs many small modules. An interface is nearly as complex as its implementation. Pure functions were extracted only for testability, while the bugs sit in how callers use them. Modules leak across their seams. Behavior is hard to test through its interface.
- **Project rules.** The code breaks the coding standards, the module boundaries in the architecture notes, the intent of the linter configs, or an ADR.
- **Practices of the stack.** The code goes against the best practices of its language and framework, for the versions that the project declares.
- **Performance.** The code does avoidable work, as judged by the practices of the stack.

Apply the deletion test to every module that you suspect is shallow. A candidate needs a yes: deleting the module concentrates complexity.

Every candidate names the place in the code and the rule or practice that it breaks. Drop a finding that has neither. Mark a practice or performance finding `hypothesis` unless the code or a measurement confirms it.

**Done when:** each candidate has its files, its problem, the rule or practice behind it, and whether tests reach the code through its interface.

### 5. Present the candidates

List the candidates in the chat, most valuable first. Give each candidate:

- **Files.**
- **Problem.** In the glossary terms of `codebase-design` and the domain terms of the project.
- **Solution.** In plain words. Do not propose an interface yet.
- **Win.** In locality and leverage, and how the tests improve.
- **Dependency category.** From [DEEPENING.md](../codebase-design/DEEPENING.md).
- **Strength.** `Strong`, `Worth exploring` or `Speculative`.
- **Tests.** Whether tests reach the code through its interface: yes or no.
- **Basis.** The rule or practice, or `hypothesis`.

End with the candidate that you would take first and why. Draw a diagram only where the project's diagram rules allow it and the user agrees.

Ask the user through the harness's question tool which candidate to take, one at a time. Offer "none" as an option. If the user takes none, report and stop.

**Done when:** the user has chosen one candidate or none.

### 6. Grill the candidate

Call the Skill tool with "grilling" and walk the decision tree of the chosen candidate: the constraints, the dependencies, the shape of the deepened module, what sits behind the seam, which tests survive and which are replaced.

If the user wants alternative interfaces, use the design-it-twice pattern in [DESIGN-IT-TWICE.md](../codebase-design/DESIGN-IT-TWICE.md).

If the project has `domain-modeling`, call the Skill tool with "domain-modeling" while the decisions form:

- Add a new domain term to `GLOSSARY.md` as soon as a deepened module takes its name.
- If the user rejects a candidate for a reason that a future scan would need, offer to record an ADR. Skip reasons like "not now".

If tests do not reach the candidate through its interface, say so. The rewrite then runs without a safety net. Ask the user to confirm that risk through the question tool before step 7.

**Done when:** the decision is written as one task for `implement`: files, the target interface, the tests to keep, delete or add, and the user's confirmation.

### 7. Rewrite

Run `implement` in this session with that task. Give it the starting commit from step 2 as the review base, so the simplifications from step 3 count as part of the task. The behavior stays the same. Tests that passed before still pass, except the tests of replaced shallow modules, which go away with them. Write new tests at the interface of the deepened module.

**Done when:** `implement` has finished with its required checks and review.

### 8. Report and continue

Report what changed and what you left alone. Ask the user through the question tool whether to take the next candidate. First check that the rewrite did not change or remove the other candidates.

**Done when:** the user has answered.

## Red flags

Stop and tell the user if one of these happens:

- The baseline is red.
- A test needs an edit to pass. The change altered the behavior.
- The rewrite reaches outside the files that the user agreed.
- The candidate no longer passes the deletion test.
- You cannot name the rule or practice behind a candidate.
