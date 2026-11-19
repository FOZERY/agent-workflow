---
name: implement
description: "Implement one agreed task in the current session."
disable-model-invocation: true
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

Implement the assigned work from the user's task description and any supplied plan, spec, or tickets.

The current session owns the code changes and may use reviewers or other helpers under project rules. If the user wants the main session to coordinate separate implementers as architect, recommend `implement-with-swarm`.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Before editing, record the starting commit as the default review base. Track the exact file paths that this task owns.

Write or update tests when the task requires them. Follow the project's testing procedure. Where TDD applies, use `tdd` at the agreed seams.

If the project runs TDD or review in subagents, launch them from this session. If this session is itself a subagent, follow the nesting option in the project's `implement` section.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Follow the project's review procedure and checkpoint if specified. Otherwise, run `code-review` before committing or handing off uncommitted changes. Delegate review of the scoped snapshot to its reviewer subagents. Pass the source task, review base, and task-owned file paths. If required review cannot run, report the blocker instead of substituting a self-check.

For snapshot review, compare the intended commit tree with the reviewed tree before committing. If they differ, review a fresh snapshot of the final intended changes. Leave unrelated work outside the commit.

If authorized, commit only the assigned changes to the target branch. Otherwise, hand off the changed paths without committing.

If you commit after snapshot review, compare the delivered commit tree with the final reviewed tree. Report any mismatch without claiming review coverage for the differing content.
