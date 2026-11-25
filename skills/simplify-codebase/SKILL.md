---
name: simplify-codebase
description: "Simplify code changed in the current task and roll back overengineering. Use when the user asks to simplify, tidy or trim recent changes, or when another skill calls it."
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

# Simplify codebase

Make the code that this task changed easier to read and cheaper to own. Choose clarity over brevity. Make two kinds of change:

- **Restructure.** Keep the behavior: the same outputs, errors and public interfaces. Make the shape simpler: flatter flow, clearer names, less duplication.
- **Roll back.** Remove code that solves a problem nobody has: a guard for an edge case of an edge case, or a migration or compatibility path for a product without users. A rollback changes only the behavior of the code that it removes.

## Roles

- **Finder.** Does steps 1 to 5 and reports findings. The finder does not edit files.
- **Author.** The session that wrote the code. It applies the findings in step 6.

In a subagent or a separate session, you are the finder only. Return the findings to the caller. In the session that wrote the code, you take both roles.

## Principles

1. **Keep the behavior.** Before each change, check: the same output for every input, the same errors, the same side effects in the same order. If an answer is unclear, skip the change.
2. **Follow the project.** Make the code more like the rest of the codebase, not like an outside preference.
3. **Prefer clarity.** Write explicit code when the compact form makes the reader stop.
4. **Keep useful structure.** Keep a helper that names a concept, unrelated logic apart, and an abstraction that exists for tests or for a second use.
5. **Stay in scope.** Change only the diff of this task, or the whole files that the caller names.

## 1. Find the scope

1. Use the paths and the starting commit from the caller.
2. Otherwise use the files that you changed in this session. If there are none, use the uncommitted changes against `HEAD`.
3. Read each file in full and the diff of its changed lines.

If the caller names whole files, for example `refactor-codebase`, all code in those files is in scope. Otherwise touch code outside the diff only when the user asks.

If the scope is empty, or the diff changes only formatting, report that and stop.

## 2. Read the standards

1. Read the project's coding standards: `AGENTS.md`, the standards file that it points to, `CONTRIBUTING.md`, and the linter and formatter configs. A project standard wins over this skill. If there is none, match the surrounding code.
2. Read what the project says about its consumers: published interfaces, released versions, stored data and untrusted input.

## 3. Check why the code exists

Before you propose a change, answer for the code that you would change:

- What is its job?
- What calls it, and what does it call?
- Which test or requirement defines its behavior?
- What do `git log` and `git blame` say about why it exists, for example performance, a platform limit or history?

If you cannot answer, leave the code alone.

Stop and report in these cases:

- The code is already clear. Report "No changes required".
- You do not understand what the code does.
- The code is performance-critical, and the simpler form is measurably slower.
- The module will be rewritten soon.

## 4. Find restructures

Look for these signals and for others that make the code harder to read. Record each match as a finding: the file and lines, the signal and the proposed change.

| Signal | Fix |
| --- | --- |
| Nesting of 3 or more levels | Use guard clauses and early returns, or extract a named function. |
| A long function with several jobs | Split it into functions with clear names. |
| A nested ternary or a dense one-liner | Use `if`/`else`, a `switch` or a lookup table. |
| Boolean flag parameters, such as `run(true, false)` | Use an options object or separate functions. |
| The same condition in several places | Extract a named predicate. |
| Generic names: `data`, `temp`, `item` | Name the value by its content. |
| Abbreviations: `usr`, `cfg` | Use full words. Keep `id` and `url`. |
| A misleading name, such as a `get` function that changes state | Rename it to match the behavior. |
| A comment that says what the code does | Delete it. Keep comments that say why. |
| The same logic of 5 or more lines in several places | Extract one shared function. |
| Dead branches, unused variables, commented-out code | Delete them after you confirm that they are dead. |
| A redundant type assertion | Delete it. |

Leave prop drilling and similar design questions as a note in the report.

## 5. Find rollbacks

For each guard, fallback, validation, wrapper, option, extension point, compatibility path and migration that the diff adds or touches, name the requirement, contract or consumer that needs it. If you cannot name one from the task, the callers and the history, it is a candidate. Compare it with the table. If it looks more like "Keep", keep it.

| Pattern | Roll back | Keep |
| --- | --- | --- |
| Validation inside trusted code | `if (id <= 0) throw` in an internal function whose callers already check `id` | The email check in a public `/register` endpoint |
| A handler for a failure that cannot happen | `try { JSON.stringify(internalConfig) } catch { return "{}" }` | `try` around `JSON.parse(userInput)`, a file read or a network call |
| A fallback that hides a bug | `order.price ?? 0` when an order always has a price | A documented default for an optional setting |
| The same guard at each symptom | One null check at four call sites, when one place makes the bad value. Fix that place. | A shared guard that restores a real contract |
| An interface with one implementation | `UserRepository` with only `PostgresUserRepository`; a factory for two `if` branches | `Storage` with real `S3Storage` and `LocalStorage` |
| A helper used once or twice | `formatTimestamp(date)` for three lines in two places | `validateOrderTotal(order)` with real logic, used in six modules |
| A wrapper that only forwards | `isEmpty(list) { return list.length === 0 }` | A thin adapter around an unstable external SDK that five modules use |
| An extension point without a second use | A plugin registry with one plugin; an `options` parameter that no caller passes | Two payment providers that the task requires |
| Configuration for a constant | A `MAX_RETRY_COUNT` variable that no environment changes | `DATABASE_URL` |
| A compatibility alias without consumers | A deprecated alias that nothing outside the diff calls and nothing published | The alias of a public method that external callers use |
| A migration or rollout that the change does not need | A data migration when no stored shape changes | A migration for data that exists in production |
| Structure larger than the code | `types.ts`, `utils.ts`, `constants.ts` and `index.ts` for 80 lines | A split of a 1500-line file by responsibility |

Always keep:

- validation and encoding of input that the system does not control;
- authentication, authorization and other security checks;
- protection against data loss;
- accessibility basics;
- logging and error reporting that the project requires;
- comments that explain why;
- code that a requirement, a contract test or a named consumer needs.

Sort each candidate by size:

- **Small:** inside the diff, nothing else depends on it, no test names it. Record it as a finding.
- **Larger:** it spans several files, a test covers it, or it is a public interface, a config value, a migration or a compatibility path. Record it as a proposal with the evidence and the smallest safe deletion. The user decides.

A test that covers only rolled-back code goes with that code, after the user confirms the rollback.

## 6. Apply and check

The author does this step.

1. Apply the findings one at a time. Check each one against the principles first. Skip a wrong finding and record why.
2. After each change, run the typecheck and the tests that cover the file. If a check fails, revert that change.
3. If the checks cannot run, report which ones and why. Do not claim that the behavior is unchanged.
4. Compare the result with the original. If it is harder to read, or adds a pattern that the codebase does not use, revert it.

## 7. Report

- **Finder:** one line per finding: the file and lines, the signal or pattern, the proposed change, restructure or rollback. Then the proposals.
- **Author:** one line per file: what changed, and which findings you skipped and why. Pass the proposals to the user.

Leave the changes uncommitted unless the caller or the project rules say otherwise.

## Stop and revert

- A test needs an edit to pass. The change altered the behavior.
- A rename follows your preference, not the project's convention.
- Error handling was removed without a rollback reason.
- You changed code that you do not fully understand, or code outside the scope without a request.
- You made several changes at once and cannot tell which one broke a check.

**Done when:** the finder edited no file and each finding names its place and change. The author applied or skipped each finding with a reason, the typecheck and the covering tests pass, and no test was edited.
