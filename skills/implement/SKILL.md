---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Before editing, record the starting commit as the default review base. Track the exact file paths that this task owns.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Follow the project's review procedure and checkpoint if specified. Otherwise, once done, call the Skill tool with `code-review` for a scoped snapshot before committing. Pass the source task, review base and task-owned file paths.

For snapshot review, compare the intended commit tree with the reviewed tree before committing. If they differ, review a fresh snapshot of the final intended changes. Leave unrelated work outside the commit.

Commit your work to the current branch.

If review used a snapshot, compare the delivered commit tree with the final reviewed tree. Report any mismatch without claiming review coverage for the differing content.
