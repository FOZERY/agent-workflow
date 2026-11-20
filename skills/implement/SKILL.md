---
name: implement
description: "Implement one agreed task in the current session. Use when the user asks you to implement or fix something and the change is more than a trivial edit, or when an approved plan, spec or ticket is ready."
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

Implement the assigned work from the user's task description and any supplied plan, spec, or tickets.

The current session owns the code changes and may use reviewers or other helpers under project rules. If the user wants the main session to coordinate separate implementers as architect, recommend `implement-with-swarm`. If this session is already the architect of an `implement-with-swarm` run, do not use this skill. The workers use it.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Before editing, record the starting commit as the default review base. Track the exact file paths that this task owns.

Write or update tests when the task requires them. Follow the project's testing procedure. Where TDD applies, use `tdd` at the agreed seams.

If the project runs TDD, simplify or review in subagents, launch them from this session. Give the subagent the path from the `skill` setting of that skill's section, tell it to read the file in full and follow it, and pass the inputs. Do not summarize the skill in the brief. If this session is itself a subagent, follow the nesting option in the project's `implement` section.

Run typechecking regularly and single test files regularly.

When the implementation is complete and its tests pass, run `simplify` if the project's `simplify` section sets `trigger: auto`. If the project has no `simplify` section or sets `trigger: manual`, skip this step.

Run `simplify` in a subagent with a fresh context, unless the section sets another `execution`. Pass the starting commit and the task-owned file paths as its inputs. Wait for its report and do not edit those files meanwhile. Run it before review, so that review sees the final code.

Run the full test suite once at the end, after `simplify` when it ran.

Follow the project's review procedure and checkpoint if specified. Otherwise, run `code-review` before committing or handing off uncommitted changes. Delegate review of the scoped snapshot to its reviewer subagents. Pass the source task, review base, and task-owned file paths. If required review cannot run, report the blocker instead of substituting a self-check.

For snapshot review, compare the intended commit tree with the reviewed tree before committing. If they differ, review a fresh snapshot of the final intended changes. Leave unrelated work outside the commit.

If authorized, commit only the assigned changes to the target branch. Otherwise, hand off the changed paths without committing.

If you commit after snapshot review, compare the delivered commit tree with the final reviewed tree. Report any mismatch without claiming review coverage for the differing content.
