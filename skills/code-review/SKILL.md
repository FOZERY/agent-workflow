---
name: code-review
description: "Review committed or uncommitted changes against project standards and task requirements. Use for standalone review or as the independent reviewer in an implementation workflow."
---

# Code review

Review without editing the implementation. This skill works in a standalone thread or inside the configured reviewer subagent. It does not recursively launch another mandatory review team. Split review work only if the project explicitly configures and permits it.

When coordinating `implement` or `implement-spec`, read [the implementation review cycle](references/implementation-cycle.md). A reviewer executing an assigned review follows the process below and returns findings to its caller.

## Defaults

Use these when the project instructions settle nothing for review, and mention once that `setup-workflow` can configure the project. In a subagent, put that mention in your result.

- **Base:** the merge-base of `HEAD` with the default branch (`origin/HEAD`, otherwise `main` or `master`).
- **Endpoint:** the working tree, including the task's staged, unstaged and untracked files.
- **Spec:** the task the caller supplies; otherwise the issues referenced in commit messages since the base; otherwise ask.
- **Standards:** the repository's lint, format and type-check configuration and its contributing guide.

## 1. Resolve policy and review scope

Read root `AGENTS.md` (or the project's `CLAUDE.md`), its review procedure, coding/testing standards and required project review skills. Use the supplied task/spec and accepted decisions as requirement sources. Ask the user about missing scope or conflicting requirements; as a subagent without access to the user, return the question to your caller as a blocker. No tracker or local spec file is mandatory. If a required source or skill is inaccessible, mark the affected mandatory review checks as blocked. Continue review within the available scope, without treating missing required coverage as a pass.

Establish an immutable comparison base and the endpoint being reviewed. Resolve a branch/tag to its revision; use the project's merge-base or direct-comparison convention; without one, use the [default base](#defaults) and state it in the result. Preserve the original task base across resumed work so prior task commits remain included.

Include the agreed committed, staged, unstaged and relevant untracked changes. A `HEAD`-only diff does not review uncommitted implementation. For working-tree review, use a read-only scoped snapshot or content identities for the reviewed files and relevant context, leaving the real index and unrelated work untouched. State exclusions. If the files change during review, mark the result stale and obtain a stable view; never commit or stage merely to make review possible.

**Done when:** sources, scope and stable base/endpoint are identified. If there are no changes, report that scope result rather than inventing findings.

## 2. Review two axes

Keep the axes visible so one cannot hide a failure in the other:

- **Standards:** apply the project's documented rules, required review skills and agreed focus areas. Cite the applicable rule for violations. Check the permitted test strategy and verification evidence; do not demand integration infrastructure, new abstractions or extra coverage merely from personal preference.
- **Spec:** trace accepted behavior and constraints through the complete change, including missing/incorrect behavior, regressions and scope creep. Check relevant edge cases and integration boundaries. Use the requirement source, not only the implementer's explanation.

Inspect enough surrounding code to substantiate findings. Reuse valid check results; run additional checks only within reviewer permissions and disclose their side effects. Missing evidence is not a passing check. A missing spec leaves requirement coverage limited; review what can be established without claiming full Spec acceptance.

Distinguish observed violations and defects from design suggestions. Heuristics about naming, duplication, coupling or speculative abstraction are prompts to investigate, not automatic reasons to refactor working code. Avoid duplicating a verified tooling report without adding evidence, but surface failed or missing mandatory checks.

On repeat review, verify previous findings against the new revision, include the human's feedback and decisions, and look for regressions caused by fixes. Keep the full task change in scope, not just the latest correction.

**Done when:** both axes and the requested focus areas have evidence-backed results or explicit coverage limits.

## 3. Return actionable findings

For each finding, give its axis, severity/impact, file and location, evidence, rule or requirement, and recommended next action. Classify the action separately from severity:

- **Deterministic correction:** an explicit rule or accepted decision uniquely determines an in-scope fix without changing behavior, public contracts or architecture. A constant required by a documented convention can qualify; a style label alone does not.
- **Human decision:** requirements, business behavior, architecture, public contracts, competing implementations or authority need a choice. Explain the question and meaningful options without choosing on the owner's behalf.

The reviewer recommends; the parent verifies the finding and whether it may act. Keep suggestions and uncertain findings distinct from defects. The reviewer does not edit files, commit, publish or accept the task.

Return findings grouped by Standards and Spec, plus the reviewed base/endpoint, check evidence, unresolved prior findings and coverage limits. State whether mandatory review coverage is complete or blocked and why. With no actionable findings, say so for the actual scope; that result does not clear blocked coverage or express human acceptance.

**Done when:** the caller can identify what can be corrected under existing rules, what requires a decision, and which exact changes were reviewed.
