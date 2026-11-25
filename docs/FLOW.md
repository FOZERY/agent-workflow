# Choose a workflow

[Overview](../README.md) · [Русская версия](FLOW.ru.md)

Start with the task you already have. Make only the decisions and artifacts the executor needs.

## Route map

| What you have | What to do next |
| --- | --- |
| A ready task with enough detail to start | Give the task to an authorized agent that can read it. Skip planning. |
| A new task that you need to understand first | Use [`investigate`](../skills/investigate/SKILL.md). Subagents study the task history and the code. You get a facts file and a plain explanation, then discuss or plan. |
| An idea with open decisions | Use [`grilling`](../skills/grilling/SKILL.md) to settle the outcome and scope. For a large effort, use [`wayfinder`](../skills/wayfinder/SKILL.md) to track open decisions, not implementation assignments. |
| A clear task that needs a saved approach | Use [`to-plan`](../skills/to-plan/SKILL.md). It saves a Markdown plan with the task. It does not start implementation or require new specs or tickets. |
| Agreed requirements that need a new spec | Use [`to-spec`](../skills/to-spec/SKILL.md) to publish it to the tracker. If the team already owns the requirements in Jira or another source, link to them instead. |
| Work that needs separate assignments in a tracker | Use [`to-tickets`](../skills/to-tickets/SKILL.md) from a plan, spec, or discussion. Approve the tickets and their dependencies before publication. |

Before you start a route, check that its [skills and helpers](../skills/setup-workflow/references/catalog.md#dependencies) are installed in your client.
Check project permissions for tracker, branch, and delegation actions. If a required step is unavailable or forbidden, report what blocks it.

## Give the task to an executor

| Situation | Executor |
| --- | --- |
| An agreed task of any size | [`implement`](../skills/implement/SKILL.md). The session is the orchestrator. It writes small changes itself and gives larger ones to one or several workers. Use the task sources you already have. |
| An approved plan and its source task | [`implement`](../skills/implement/SKILL.md) with the plan path and the source task. Approval of the plan does not start execution. |

For example, if Jira task `APP-123` needs a plan, ask `/to-plan` to save it alongside the task artifacts and link the Jira requirements.
Review the plan. Then give the executor the plan path, the Jira task, and a separate request to implement it.
In Codex, use `$to-plan`.

Each worker runs in a separate session with its own thread. The orchestrator recommends the size and the mode, and you confirm them before any work starts.

## Verify and accept

Follow the project's settings for TDD, simplify and review. Manual means you start that activity separately. With `auto`, the worker runs `simplify-codebase` before review, so review sees the final code. A subagent finds the simplifications, and the worker applies them.
Before any work starts, `implement` lists the mode and the steps for the task and asks you to confirm them. You can turn off a step for a simple task.
Each worker checks the Standards axis of `code-review` on its own changes. The orchestrator then checks the Spec axis once, against the task, and sends findings back to the same worker.
See [review coverage and follow-up](../skills/setup-workflow/references/AGENTS.md#review-coverage) for scope, timing, and whether the agent can fix findings.

Failed required checks or unresolved required findings block completion. Once all required checks and review pass, you decide whether to accept the result.
You can stop after acceptance. Commit, push, opening a PR/MR, merge, and deployment follow the project's permissions.
If the session exposed a recurring problem, [`retro`](../skills/retro/SKILL.md) proposes a change. You decide whether it becomes a rule or a lesson.

After a stage of work, such as several tasks or an epic, you can start [`refactor-codebase`](../skills/refactor-codebase/SKILL.md) by hand. It finds structural problems in the code of that stage, and you pick one. It then rewrites that one through `implement` with the behavior kept. `implement` never starts it.

## Keep project rules and task artifacts separate

[`setup-workflow`](../skills/setup-workflow/SKILL.md) records rules, permissions, and selected skill settings in root `AGENTS.md`.
Keep recent work in `CONTEXT.md` and confirmed experience in `LESSONS.md`. Both default to `.docs/`.
Keep plans with their tasks. Keep requirements in their original source.
See [project artifacts](../skills/setup-workflow/references/project-artifacts.md) for file ownership and when to read or update each file.
