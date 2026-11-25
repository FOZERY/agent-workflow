---
name: implement
description: "Implement an agreed task as the orchestrator: write small changes yourself, give larger ones to workers, then check the result against the task. Use when the user asks to implement or fix something larger than a trivial edit, or when an approved plan, spec or ticket is ready."
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

# Implement

You are the **orchestrator**. You decide the size, split the work, own the shared contracts, check the result against the task and write the final report.
A **worker** owns the code of one assignment and follows [WORKER.md](WORKER.md). In direct mode, you are your own worker.

Each role gets its agent from a project setting:

| Role | Who | Setting |
| --- | --- | --- |
| Orchestrator | This session | Chosen by the user who started it |
| Worker | A separate session with its own thread | `worker` in the project's `implement` section |
| Standards reviewer | Subagent of the worker | `standards-reviewer` in the `code-review` section |
| Spec reviewer | Subagent of the orchestrator | `spec-reviewer` in the `code-review` section |
| Simplify finder | Subagent of the worker | `finder` in the `simplify-codebase` section |

## 1. Read the task

1. Read the task and any plan, spec or tickets that come with it. If the task has a facts file from `investigate`, read it and put its path in each worker brief.
2. If the user gives a ticket reference, fetch the ticket from the tracker and state its title. If the reference is ambiguous, ask.
3. If a plan is not approved, ask the user before you continue.
4. If the task is a set of tickets with blocking edges, take the unblocked tickets in their order. Use the acceptance criteria of each ticket as its checks. After the work, update each ticket if the project's tracker rules allow it.

**Done when:** you can state the goal, the acceptance checks and the files or repositories that the task touches.

## 2. Choose the size

| Size | Signs | Mode |
| --- | --- | --- |
| Trivial | A typo, a rename, or an edit that the user dictated word for word | Make the edit, report it and stop. Skip the rest of this skill. |
| Small | One place in the code and no design decision | **Direct:** you write the code by [WORKER.md](WORKER.md). |
| Normal | Several files or a design decision inside one change area | **One worker** in a separate session. |
| Large | Parts that can go to separate owners, or several repositories | **Several workers**, each in its own session and with one change area. |

**Done when:** you have a recommended size and mode with a one-line reason.

## 3. Confirm the mode and the steps

If the user already gave the mode and the steps for this task, skip this step.

Ask the user through the question tool, in one call:

1. **Mode.** Your recommended size and mode. For worker modes, add the number of workers, their isolation (branch, worktree or workspace) and the agent for each role.
2. **Steps.** The steps that the project settings give this task, in this order:
   - TDD, with its trigger and where it runs;
   - `simplify-codebase`, with its trigger;
   - the full test suite;
   - the Standards review and the Spec review;
   - the review follow-up and the round limit;
   - the commit or the handoff.

In the question:
- Show a step whose skill has `trigger: manual` as off. The user can turn it on.
- Let the `trigger` of `code-review` cover both review axes.
- If TDD is on, list the seams to test, so that the user confirms them.
- If a project rule makes a step mandatory, say so.

The user can change the mode or turn off steps for this task. Start nothing before the answer. Run only the confirmed steps.

**Done when:** the user confirmed the mode and the list of steps.

## 4. Do the work

If the caller gives a review base, use it. Otherwise, record the current commit as the starting commit and use it as the base.

**Direct mode.** Follow [WORKER.md](WORKER.md) yourself, then go to step 5.

**Worker modes.**

1. Split the work into assignments with one owner for each change area. Record which assignments depend on other results. Resolve shared contracts before dependent workers edit against them.
2. Write a brief for each worker with:
   - links to the task sources and the plan or spec, not a retelling;
   - the repository, the file boundaries and the branch or worktree;
   - the shared contracts and the seams to test;
   - the confirmed steps and the starting commit;
   - the report that you expect.
3. Start each worker in a separate session with the session tool from the project's `implement` section and the agent from the `worker` setting. Give it the brief. Tell it to read [WORKER.md](WORKER.md) in full and follow it, and give the absolute path of that file.
4. Start independent assignments in parallel. Start dependent assignments when their prerequisites are ready. Route contract changes through you and tell the affected workers.
5. Wait for the reports. Do not edit the workers' files meanwhile.

**Done when:** every worker reported, or you finished the direct work, and the confirmed checks of each part passed.

## 5. Check against the task

Skip this step if the user turned off the Spec review.

1. Run `code-review` from this session with the Spec axis only. Its reviewer is a fresh subagent with the `spec-reviewer` setting.
2. Pass the task sources, the base, and the changed paths with the worktree or branch of each part. The reviewer reads each part in its own worktree or branch.
3. Read the findings, not the whole diff.
4. If the `followup` setting of `code-review` is `report`, give the findings to the user and wait.
5. If it is `fix-and-rereview`, send the findings to the worker that owns the code, in the same worker session. In direct mode, fix them yourself by [WORKER.md](WORKER.md) step 8. Then run the Spec review again.

The round limit is the `rounds` setting of `code-review`, `3` by default. If the Spec review or a worker's Standards review reaches it, stop and ask the user.

**Done when:** the Spec review has no open findings, or the user decided about the remaining ones.

## 6. Integrate and finish

With several workers, integrate the parts in dependency order through the project's delivery procedure. Run the agreed checks on the combined result, including cross-repository interactions.

Run the full test suite once on the final tree, unless the only worker already ran it on that tree.

If you may commit, commit only the assigned changes to the target branch. Otherwise, hand off the changed paths without a commit.

If review used a snapshot of the working tree:
1. Before the commit, compare the intended commit tree with the reviewed tree. If they differ, review a fresh snapshot of the final changes.
2. After the commit, compare the commit tree with the last reviewed tree. Report any difference, and do not claim review for the content that differs.

Report to the user:

- the mode and the steps that the user turned off;
- what changed, per worker or repository;
- the checks that ran and their results;
- the Standards and Spec outcomes;
- the `simplify-codebase` proposals that wait for the user;
- what remains blocked or waits for approval.

**Done when:** the agreed checks and the confirmed reviews passed, and the user has the report.
