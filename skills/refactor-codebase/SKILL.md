---
name: refactor-codebase
description: "Find structural problems in the code after a stage of work, agree one fix with the user, and rewrite it with the behavior kept."
disable-model-invocation: true
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

# Refactor codebase

Find where the structure of the code makes it hard to change, agree one fix with the user, and rewrite it with the behavior kept. The user runs this skill after a stage of work, such as several tasks or an epic. `simplify-codebase` cleans the code of one task. This skill works on the structure across tasks.

Read [VOCABULARY.md](VOCABULARY.md) for the terms: module, interface, depth, seam, adapter, leverage, locality and the deletion test. Use these terms in every candidate.

## 1. Find the scope and the rules

Choose the scope in this order:

1. The module or problem that the user names.
2. The commit range that the user gives: the commit, tag or branch where the stage began.
3. The files that change most often in `git log`. If no file stands out, ask the user for a module or a commit range.

Read the project rules: `AGENTS.md`, the coding standards, the architecture notes, the linter and formatter configs, `GLOSSARY.md` and the ADRs of the area. Reopen an ADR only for a real problem, and say so in the candidate.

If the scope is empty, report that and stop.

**Done when:** you have the paths in scope, the range or files behind them, and the rule sources.

## 2. Check the baseline

1. Run the typecheck and the tests that cover the scope. If a check fails, report it and stop.
2. Record the current `HEAD` as the starting commit.

## 3. Collect simplifications

If the project has no `simplify-codebase` section, skip this step and say so.

1. Start `simplify-codebase` as its finder, with the agent from the `finder` setting, unless its `execution` setting says otherwise. Give it the path from the `skill` setting, and the files in scope as whole files. If subagents are not available, run it in this session.
2. Keep its findings and proposals. Leave the files unchanged: the user decides about them in step 5.

**Done when:** you have the findings and the proposals, or a note that the step was skipped.

## 4. Scan

Give the scan to a subagent with a fresh context. If subagents are not available, scan in this session. Read the code in scope and note each problem through these views:

- **Depth.** One concept needs many small modules. An interface is nearly as complex as its implementation. Pure functions exist only for tests, while bugs sit in how callers use them. Modules leak across their seams. Behavior is hard to test through its interface.
- **Project rules.** The code breaks the coding standards, the module boundaries in the architecture notes, the intent of the linter configs, or an ADR.
- **Practices of the stack.** The code goes against the practices of its language and framework, for the versions that the project uses.
- **Performance.** The code does work that it could avoid.

Apply the deletion test to each module that looks shallow. Keep the candidate only if the test shows a pass-through: deleting the module makes its complexity vanish instead of spreading to its callers.

Each candidate names the place in the code and the rule or practice that it breaks. Drop a finding that has neither. Mark a practice or performance finding `hypothesis` until the code or a measurement confirms it.

**Done when:** each candidate has its files, its problem, the rule or practice behind it, and whether tests reach the code through its interface.

## 5. Show the candidates

List the candidates in the chat, most valuable first. For each one give:

- **Files.**
- **Problem**, in the terms of [VOCABULARY.md](VOCABULARY.md) and the project's domain terms.
- **Solution**, in plain words. Leave the interface for step 6.
- **Win**, in locality and leverage, and how the tests improve.
- **Dependency category**, from [DEEPENING.md](DEEPENING.md).
- **Strength:** `Strong`, `Worth exploring` or `Speculative`.
- **Tests:** do tests reach the code through its interface, yes or no.
- **Basis:** the rule or practice, or `hypothesis`.

End with the candidate that you would take first, and why. Draw a diagram only if the project's diagram rules allow it and the user agrees.

If step 3 found simplifications, list them as one more option, "simplifications only", and say whether they can go with a candidate.

Ask the user through the question tool which candidate to take. Offer "none". If the user takes none, report and stop. The files stay unchanged.

**Done when:** the user chose one candidate or none.

## 6. Grill the candidate

1. Run the `grilling` skill on the chosen candidate: constraints, dependencies, the shape of the deepened module, what sits behind the seam, which tests stay and which are replaced.
2. If the user wants alternative interfaces, use [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md).
3. If the project has `domain-modeling`, use it as decisions form. Add a new term to `GLOSSARY.md` when a deepened module takes its name. If the user rejects a candidate for a reason that a future scan needs, offer to record an ADR.
4. If no tests reach the candidate through its interface, tell the user that the rewrite has no safety net. Get the user's confirmation through the question tool.

**Done when:** the decision is one task for `implement`: the files, the target interface, the tests to keep, delete or add, and the user's confirmation.

## 7. Rewrite

Run `implement` in this session with that task. Add the simplifications from step 3 that the user chose. Give it the starting commit from step 2 as the review base.

The behavior stays the same. Tests that passed before still pass, except the tests of replaced shallow modules, which go with them. Write new tests at the interface of the deepened module.

**Done when:** `implement` finished with its required checks and review.

## 8. Report and continue

1. Report what changed and what you left alone.
2. Check that the rewrite did not change or remove the other candidates.
3. Ask the user through the question tool whether to take the next candidate.

## Stop and tell the user

- A test needs an assertion change to pass. The change altered the behavior. Edits of imports and paths do not count.
- The rewrite reaches outside the files that the user agreed.
- The candidate is no longer a pass-through by the deletion test.
