---
name: implement-spec
description: "Implement an agreed specification and its task graph, then obtain independent review and human acceptance."
disable-model-invocation: true
---

# Implement a specification

Requires the adapted `code-review` skill and its `references/implementation-cycle.md`, plus `human-text` for the coordinator's explanation of the integrated result. Locate both installed packages and read the shared cycle before starting; resolve missing dependencies with the user rather than silently installing them. This skill orchestrates the agreed scope without calling `implement`; it reads `tdd` only when the user asks for TDD.

## Defaults

Use these when the project instructions settle nothing for this specification's execution, and mention once that `setup-workflow` can configure the project.

- **Workspace and checks:** as in `implement`: the current checkout and branch, proposing a task branch when on the default branch; narrow checks while working and the full required set before review.
- **Slices:** planned in the conversation when no tickets exist.
- **Execution:** the main agent implements slices one at a time in dependency order; parallel subagents only when the project permits delegation.

## 1. Establish scope and execution ownership

Read root `AGENTS.md` (or the project's `CLAUDE.md`), the authoritative spec and any associated tickets through approved sources. External or read-only requirements are valid. If tickets do not exist, plan bounded implementation slices in the agreed location or conversation; creating tracker records is not a prerequisite.

Identify acceptance criteria, dependencies and unresolved decisions. Where tickets exist, treat them as a task graph: the **frontier** contains work whose prerequisites are satisfied under project rules, not merely items without a blocking label. Clarify missing task sources directly; setup is needed only if the owner wants to configure the broader workflow.

Confirm repositories, workspaces/worktrees, branches, file ownership and integration responsibility. Use the project's implementation profiles, delegation permissions and concurrency limits. A shared working copy is valid with non-overlapping ownership; isolated worktrees or an integration branch are options, not requirements. Preserve existing work and ask before changing an incompatible base.

Record the immutable original comparison base for each affected repository before editing; preserve it across resumed work. Coordinate writers and integration so review can identify the complete stable change, including uncommitted files. Serialize shared-index or overlapping writes.

**Done when:** the approved scope, graph or slices, execution targets, ownership and review/test policies are known.

## 2. Implement the available work

Select unblocked slices. Delegate independent work only where permitted, with fresh bounded briefs containing the task, source pointers, project rules, acceptance criteria, file ownership and test policy. Pass the applicable instructions explicitly when the harness does not inherit them. Main-agent implementation is the fallback when delegation is unavailable or disallowed.

Keep exploration read-only where that is its role; it can return sourced findings without creating a research file. Use approved artifact locations only when a durable record is needed.

Each implementer changes only its assigned scope and runs the required checks. If the user asked for TDD, the coordinator runs the `tdd` cycles for each slice: it launches the test-author subagent, and implementers write production code for a behavior only after its test is red. Otherwise follow ordinary project testing requirements.

Integrate completed slices through the authorized project procedure. Reconcile overlapping edits and dependency changes before advancing the frontier. A branch merge, commit, push or tracker transition requires its own authority; it is not implicit in completing a slice. Test the integrated result at the required level, not just each isolated slice.

**Done when:** each in-scope requirement is implemented and verified, or its blocker is explicit. Partial completion remains partial; scope changes require the human.

## 3. Review the integrated result and obtain acceptance

Follow the installed `code-review` package's [shared cycle](../code-review/references/implementation-cycle.md) for review, corrections, the plain-language implementation walkthrough and human decisions. The coordinator dispatches the configured fresh-context reviewer with the complete integrated scope, relevant per-slice evidence and project review rules. Per-ticket reviews can supplement, but do not replace, review of the integrated result.

Resolve deterministic findings within authority and return decision-dependent findings to the human. After corrections or human feedback, run affected checks and obtain a fresh review covering the updated integration. Resolve the reference inside the installed dependency if packages are not siblings.

Finish only at the human-acceptance checkpoint defined by the shared cycle. Report implemented scope, remaining limitations and actual workspace/branch locations. A request to commit follows project commit policy; PR publication, ticket closure, merging and worktree cleanup are separate authorized actions, not automatic completion steps.
