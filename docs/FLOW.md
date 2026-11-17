# Choose a workflow

[Overview](../README.md) · [Русская версия](FLOW.ru.md)

Start with the task you already have. Make only the decisions and artifacts the executor needs.

## Route map

| What you have | What to do next |
| --- | --- |
| A ready task with enough detail to start | Give the task to an authorized agent that can read it. Skip planning. |
| An idea with open decisions | Use [`grilling`](../skills/grilling/SKILL.md) to settle the outcome and scope. For a large effort, use [`wayfinder`](../skills/wayfinder/SKILL.md) to track open decisions, not implementation assignments. |
| A clear task that needs a saved approach | Use [`to-plan`](../skills/to-plan/SKILL.md). It saves a Markdown plan with the task. It does not start implementation or require new specs or tickets. |
| Agreed requirements that need a new spec | Use [`to-spec`](../skills/to-spec/SKILL.md) to publish it to the tracker. If the team already owns the requirements in Jira or another source, link to them instead. |
| Work that needs separate assignments in a tracker | Use [`to-tickets`](../skills/to-tickets/SKILL.md) from a plan, spec, or discussion. Approve the tickets and their dependencies before publication. |

Before you start a route, check that its [skills and helpers](../skills/setup-workflow/references/catalog.md#dependencies) are installed in your client.
Check project permissions for tracker, branch, and delegation actions. If a required step is unavailable or forbidden, report what blocks it.

## Give the task to an executor

| Input | Executor |
| --- | --- |
| A task described by a spec or tickets | [`implement`](../skills/implement/SKILL.md) |
| An approved plan and its source task | An agent configured to read both. Approval of the plan does not start execution. |
| A spec and its ticket graph | [`implement-spec`](../skills/implement-spec/SKILL.md). A plan alone is not enough. |

For example, if Jira task `APP-123` needs a plan, ask `/to-plan` to save it alongside the task artifacts and link the Jira requirements.
Review the plan. Then give the executor the plan path, the Jira task, and a separate request to implement it.
In Codex, use `$to-plan`.

For work across services, use one plan. Give each worker readable project rules, its assignment, and the relevant shared contracts.
Assign disjoint files for parallel work. Check the complete interaction after integration.

## Verify and accept

Follow the project's settings for TDD and review. Manual means you start that activity separately.
By default, `implement` reviews a snapshot of the task's changes before commit. `implement-spec` reviews the integration branch after merging the tickets.
See [review coverage and follow-up](../skills/setup-workflow/references/AGENTS.md#review-coverage) for scope, timing, and whether the agent can fix findings.

Failed required checks or unresolved required findings block completion. Once all required checks and review pass, you decide whether to accept the result.
You can stop after acceptance. Commit, push, opening a PR/MR, merge, and deployment follow the project's permissions.
If the session exposed a recurring problem, [`retro`](../skills/retro/SKILL.md) proposes a change. You decide whether it becomes a rule or a lesson.

## Keep project rules and task artifacts separate

[`setup-workflow`](../skills/setup-workflow/SKILL.md) records rules, permissions, and selected skill settings in root `AGENTS.md`.
Keep recent work in `CONTEXT.md` and confirmed experience in `LESSONS.md`. Both default to `.docs/`.
Keep plans with their tasks. Keep requirements in their original source.
See [project artifacts](../skills/setup-workflow/references/project-artifacts.md) for file ownership and when to read or update each file.
