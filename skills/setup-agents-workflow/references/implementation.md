# Testing, implementation and review interview

Read this when the selected workflow includes `tdd`, `implement`, `implement-spec` or `code-review`, or when revising their policy. Inspect existing tests, standards, review guides, agent profiles and working-copy conventions first. Ask only for decisions the sources do not settle; configure the selected branches, not an entire implementation pipeline for standalone review.

## Testing policy

Ask which behavior deserves tests and which test levels apply to each kind of change: business-logic unit tests, integration, contract or end-to-end tests. Establish naming, fixture and mocking conventions, required edge cases, intentional exclusions, coverage expectations and representative existing tests. Reuse configuration for commands and thresholds instead of transcribing it into instructions.

Ask which existing environments may be used and whether new containers, databases, services, dependencies or network access require approval. Adding SQL does not itself select integration testing. If permitted tests cannot prove a required property, the agent must report the gap and ask; it cannot claim coverage or expand infrastructure silently.

`tdd` is optional and user-invoked, even if installed. Ordinary implementation still follows the project's required checks without it. If independent test authorship is selected, establish the test-author subagent's role and model; the author owns the test files in the shared working copy. Distinguish test-first red/green evidence from parallel independent authorship. Neither mode makes the implementation agent the test author.

## Execution scope

For `implement` or `implement-spec`, establish workspace/worktree and branch selection, implementation roles, permitted delegation/concurrency and integration ownership. Determine which defaults may be reused and which targets need task-time confirmation. Single-checkout, ticket-branch and integration-branch workflows are options; agree how shared writers avoid conflicts and how changes are reviewed before commits when needed.

## Reviewer profile and brief

Ask: "Which available reviewer role/profile and model should perform independent review? May the implementation agent launch it automatically after checks and after corrections? Which project rules, example implementations and additional review skills must it receive? What should it focus on?"

Show available choices rather than selecting a supposedly smart model for the user. Record the owner's chosen native profile pointer or exact supported model identifier and its approved fallback, if any, in root `AGENTS.md` or the referenced review procedure. Keep reasoning effort with the harness unless the owner specifies it. Verify the harness can dispatch that selection. Without a working subagent route, the fallback is a review session the user runs with the parent's brief; self-review never substitutes.

The default trigger is an explicit dispatch step in the implementation skills, not a newly installed hook. If the project already uses a review hook, identify its trigger, supplied context and result channel; verify it before relying on it and avoid duplicate dispatch. Creating hooks or changing client profiles requires separate approval.

Pass the review skill, project sources and required supplementary skills explicitly into the fresh context; do not assume inheritance. Resolve those packages as dependencies of that configured route and check reviewer access to them. The reviewer reports findings without editing code. Standalone `code-review` remains available without an implementation parent or mandatory nested subagents.

## Corrections and human acceptance

Agree which documented rules allow deterministic automatic corrections and which actions require human decisions. Keep severity separate from fix authority: constants or formatting may be automatic only if the rule determines one behavior-preserving fix. Business behavior, architecture, competing implementations or unclear requirements go to the human.

These implementation routes require independent review, checks after fixes, fresh review after corrections/human feedback, a stop for the human after three review rounds, and explicit acceptance of the current revision. Agree the audience, language and project-specific attention points for the shared cycle's implementation walkthrough, and who accepts it. The parent explains the result before presenting remaining findings; ready-for-human-review is not completion. A commit request for the reviewed result can express acceptance, but an intermediate/WIP commit cannot. PR/MR publication remains separately requested and authorized.

If the owner declines these gates, explain that the selected implementation route is incompatible; do not claim that a generic instruction pointer removed a required step. Standalone TDD or review can still be configured independently.

## Capture and verify

Keep concise test/review policy in root `AGENTS.md`, or add mandatory pointers to existing project procedures. Use the selected agent-documentation directory for new supporting documents only if needed and approved. Record mandatory testing/review rules here, not solely in `LESSONS.md`. A retrospective can propose a policy change; promote it to the authoritative rule only after approval. Lessons retain the useful experience and link to the rule without becoming a competing policy source.

Walk through the affected cases: a SQL change with business-unit tests only; a required database property that those tests cannot prove; TDD declined; a missing reviewer model or review skill; no findings but a required review source was inaccessible; a deterministic style finding beside a business decision; human feedback after a clean review; and a WIP commit that is not acceptance. These are contract checks, not permission to run implementation or publish changes during setup.

**Done when:** the selected route has agreed testing scope and infrastructure limits, execution ownership where needed, an available or explicitly blocked reviewer profile, required instruction/skill sources, correction authority and acceptance checkpoints. Actual configuration and discovery are distinguished from a live review execution test.
