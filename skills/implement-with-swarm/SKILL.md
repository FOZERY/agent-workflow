---
name: implement-with-swarm
description: "Coordinate a large implementation across agents while the main session acts as architect."
disable-model-invocation: true
---

# Implement with a swarm

The main session is the **architect**. Own the design, work split, shared contracts, integration, and final verification. Assign production code changes and fixes to workers. Use `implement` instead when the main session should own the code changes.

## 1. Map the work

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

Read the applicable project instructions and the user's task. Use the requirements already available: a brief, a plan, a spec, tickets, or a combination. This skill does not require a new spec, ticket graph, or issue tracker.

Identify the repositories, shared interfaces, and acceptance checks. Split the work into assignments with one owner per change area. Record which assignments depend on other results and which can start independently. Resolve shared contracts before dependent workers edit against them.

## 2. Recommend how to run the workers

- **Separate sessions (default):** recommend these for multiple repositories or when workers need their own branches, worktrees, or workspaces. Use the session tool configured for the project.
- **Subagents:** recommend these for disjoint changes in one repository when workers can run the required checks and delegate their own reviews. Sequence shared edits.

Check that each worker can run the configured review procedure. If subagents cannot launch the required reviewers, recommend separate sessions. If no approved mode supports required review, report the blocker.

Before dispatch, present the recommended mode, why it fits, the assignments, and their isolation and integration plan. Use the mode the user already authorized or ask the user to choose. If the required tool or isolation is unavailable, report the blocker. Get approval before switching modes.

## 3. Dispatch and coordinate

For each assignment, provide the repository, target branch or file boundaries, and links to readable project rules and task sources. Include shared contracts, dependencies, acceptance checks, the seams to test, and the expected handoff.

Every worker runs [`implement`](../implement/SKILL.md) for its assignment:

- **Session worker:** send `/implement` (`$implement` in Codex) with the assignment as its first prompt.
- **Subagent worker:** a subagent cannot run a slash command, and `implement` is user-invoked. Give it the path to `implement/SKILL.md` and tell it to read the file and follow it.

Verify access to the procedure, task sources, and workspace before edits.

The worker owns its code, applicable tests, and review. It runs TDD, simplify and review as the project's `implement` section says, including the nesting option recorded there. A self-check does not replace required independent review.

Start independent assignments in parallel. Start dependent assignments once their prerequisites are available. Route contract changes through the architect and notify workers whose assignments depend on them.

Collect each worker's delivered branch, commits, or changed paths. Require test results, the review scope and outcome, and any unresolved findings or blockers in the handoff.

## 4. Integrate and verify

Track the result in each repository. Coordinate integration in dependency order through the authorized delivery procedure. Commit, push, PR/MR, merge, deployment, and cleanup remain subject to their own permissions.

Run agreed checks against the combined changes, including affected cross-repository interactions. Follow the project policy for any integration review. This checkpoint does not replace worker-level review. Send required fixes to the assigned workers and recheck the affected result.

Report what each repository delivered, which combined checks passed, and what remains blocked or awaits approval. Mark the swarm complete only when the agreed checks and required review pass.
