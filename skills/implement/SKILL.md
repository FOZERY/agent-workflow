---
name: implement
description: "Implement one agreed task as the orchestrator: confirm the mode and steps, write small changes yourself or give the code to workers, then check the result against the task. Use when the user asks you to implement or fix something and the change is more than a trivial edit, or when an approved plan, spec or ticket is ready."
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

# Implement

You are the **orchestrator**. You own the size decision, the work split, shared contracts, the check against the task and the final report. A **worker** owns the code of its assignment and follows [WORKER.md](WORKER.md). In direct mode you are your own worker.

Roles and their project settings:

| Role | Who | Setting |
| --- | --- | --- |
| Orchestrator | This session | Chosen by the user who started it |
| Worker | A separate session with its own thread | `worker` in the project's `implement` section |
| Standards reviewer | Subagent of the worker | `standards-reviewer` in the `code-review` section |
| Spec reviewer | Subagent of the orchestrator | `spec-reviewer` in the `code-review` section |
| Simplify finder | Subagent of the worker | `finder` in the `simplify-codebase` section |

## 1. Read the task

Read the user's task and any supplied plan, spec or tickets. If the user passes a ticket reference, fetch it from the issue tracker and state its title. If the reference is ambiguous, ask.

If a plan has a status other than approved, ask the user before you continue.

If the task is a set of tickets with blocking edges, take the unblocked tickets in their order. Use the acceptance criteria of each ticket as its acceptance checks. After the work, update each ticket where the project's tracker rules allow it.

**Done when:** you can state the goal, the acceptance checks and the files or repositories that the task touches.

## 2. Choose the size

| Size | Signs | Mode |
| --- | --- | --- |
| Trivial | A typo, a rename, or an edit that the user dictated word for word | Make the edit, report it and stop. The rest of this skill does not apply. |
| Small | One place in the code and no design decision | **Direct:** you write the code by [WORKER.md](WORKER.md). |
| Normal | Several files or a design decision inside one change area | **One worker** in a separate session. |
| Large | Parts that can go to separate owners, or several repositories | **Several workers**, each in its own session and with one change area. |

**Done when:** you have a recommended size and mode with a one-line reason.

## 3. Confirm the mode and the steps

Ask the user through the question tool, in one call:

1. **Mode.** Your recommended size and mode. For worker modes, also the number of workers, their isolation (branch, worktree or workspace) and the agent for each role from the settings above.
2. **Steps.** The steps that the project settings give this task, in order: TDD (trigger and where it runs), `simplify-codebase` (trigger), the full test suite, the Standards review, the Spec review, the review follow-up and round limit, and the commit or handoff.

List a step whose skill has `trigger: manual` as off. The user can turn it on. The `trigger` of `code-review` covers both axes. If TDD is on, list the seams to test, so the user confirms them. The user can change the mode or turn off steps for this task. If a project rule makes a step mandatory, say so in the question. Run only the confirmed steps. Start nothing before the answer. If the user already gave the mode and the steps for this task, do not ask again.

**Done when:** the user confirmed the mode and the list of steps.

## 4. Do the work

Use the review base that the caller gives. Otherwise, record the current commit as the starting commit and use it as the base.

**Direct mode.** Follow [WORKER.md](WORKER.md) yourself, then go to step 5.

**Worker modes.**

1. Split the work into assignments with one owner for each change area. Record which assignments depend on other results. Resolve shared contracts before dependent workers edit against them.
2. Write a brief for each worker: links to the task sources and the plan or spec, the repository and file boundaries, the branch or worktree, the shared contracts, the seams to test, the confirmed steps, the starting commit and the expected report. Link the task sources. Do not retell them.
3. Start each worker in a separate session with the session tool from the project's `implement` section. Use the agent from the `worker` setting. Give it the brief and tell it to read [WORKER.md](WORKER.md) in full and follow it. Give the absolute path of that file.
4. Start independent assignments in parallel. Start dependent assignments when their prerequisites are ready. Route contract changes through you and tell the affected workers.
5. Wait for the reports. Do not edit the workers' files meanwhile.

**Done when:** every worker reported, or you finished the direct work, and the confirmed checks of each part passed.

## 5. Check against the task

If the user kept the Spec review, run `code-review` from this session with the Spec axis only. Its reviewer is a fresh subagent with the `spec-reviewer` setting. Pass the task sources, the base, and the changed paths with the worktree or branch of each part. The reviewer reads each part in its own worktree or branch. Read its findings, not the whole diff.

If the `followup` setting of `code-review` is `report`, give the findings to the user and wait. If it is `fix-and-rereview`, send the findings to the worker that owns the code, in the same worker session, because it already knows the code. In direct mode, fix them yourself by [WORKER.md](WORKER.md) step 8. Then run the Spec review again.

The round limit is the `rounds` setting of `code-review` (`3` by default). When the Spec review or a worker's Standards review reaches it, stop and ask the user.

**Done when:** the Spec review has no open findings, or the user decided about the remaining ones.

## 6. Integrate and finish

With several workers, integrate the parts in dependency order through the project's delivery procedure. Run the agreed checks on the combined result, including cross-repository interactions.

Run the full test suite once on the final tree, unless the only worker already ran it on that tree.

If authorized, commit only the assigned changes to the target branch. Otherwise, hand off the changed paths without committing. For snapshot review, compare the intended commit tree with the reviewed tree before committing. If they differ, review a fresh snapshot of the final intended changes. If you commit after snapshot review, compare the delivered commit tree with the final reviewed tree. Report any mismatch without claiming review coverage for the differing content.

Report to the user:

- the mode and the steps that the user turned off;
- what changed, per worker or repository;
- the checks that ran and their results;
- the Standards and Spec outcomes;
- the `simplify-codebase` proposals that wait for the user;
- what remains blocked or waits for approval.

**Done when:** the agreed checks and the confirmed reviews passed, and the user has the report.
