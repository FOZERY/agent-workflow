---
name: ask-workflow
description: "Explain this workflow and recommend the next skill."
argument-hint: "[workflow question or current task state]"
disable-model-invocation: true
---

# Ask about the workflow

Answer questions about this kit and recommend the next skill. Give advice only. You can read files, Git history and tracker items. Leave every skill run, install, file edit, Git change and tracker change to the user.

## 1. Read the sources

1. In a project with a root `AGENTS.md` or `CLAUDE.md`, read it and the pointers that apply, also for a general question. Outside a project, use the map in step 2.
2. For the current task state, read the conversation and the project's `CONTEXT.md` and `LESSONS.md` (in `.docs/` by default). Treat them as a lead, not as proof that a check passed or a decision was made.
3. List the skill folders to see which skills are installed. The `/` menu and the model's skill list hide some skills.
   - Claude Code: `.claude/skills/`, `~/.claude/skills/`.
   - Codex: `.agents/skills/`, `~/.agents/skills/`, `~/.codex/skills/`.
   - OMP: `.omp/skills/`, `~/.omp/agent/skills/`.
4. Before you give details about a skill, read its `SKILL.md`. A same-named skill from another source can differ from this kit.

Ask the user a question only if the answer changes the recommendation.

**Done when:** you can answer from the sources, or you can name the missing fact that changes the answer.

## 2. Choose the route

Recommend the smallest route that reaches the goal. The map lists candidates, not a required order.

| Need | Skill |
| --- | --- |
| Set up a home for several repositories | `setup-home-repo` (manual) |
| Configure project rules, permissions and selected skills | `setup-workflow` (manual) |
| Study a new task before discussion: history, code and a plain explanation | `investigate` (manual) |
| Fix a bug in code that the user does not know | `investigate` (manual), then `implement` |
| Find where recent work on a topic stands and what comes next | `recall` (manual) |
| Test an idea and find open questions | `grilling` |
| Test an idea and record terms and decisions | `grill-with-docs` (manual) |
| Agree domain terms or record a decision (ADR) | `domain-modeling` |
| Research a question in primary sources | `research` |
| Plan an effort too large and too unclear for one session | `wayfinder` (manual) |
| Answer a design question with a throwaway experiment | `prototype` |
| Save an implementation plan for a task | `to-plan` (manual) |
| Turn agreed requirements into a spec, then tickets | `to-spec`, `to-tickets` (manual) |
| Implement an agreed task or fix a bug | `implement`: it runs `tdd`, `simplify-codebase`, `code-review` and `verify` by the project's settings |
| Write tests that prove real behavior, or check whether existing tests prove anything | `tdd` |
| Simplify changed code outside `implement` | `simplify-codebase` |
| Check that a change works in the running product outside `implement` | `verify` |
| Review uncommitted changes, a branch, a PR or a commit | `code-review` |
| Implementation finished, next steps before the merge | The user's review of the `implement` report, then the project's delivery rules |
| Prepare or publish a PR | The project's delivery rules |
| Turn mistakes from recent sessions into skills or rules | `retro` (manual) |
| Find structural problems after a stage of work and rewrite one | `refactor-codebase` (manual) |
| Write replies; write documents; write skills and `AGENTS.md` | `writing-for-people`; `writing-technical`; `writing-for-agents` |
| Restate the last reply in plain words | `rephrase` (manual) |
| Rewrite documents; remove stale documents | `refactor-docs`; `cleanup-artifacts` (manual) |

- A task with requirements from an analyst can go straight to `implement`.
- A task that is ready for the user's review needs that review, not another skill.
- If a recommended skill or a skill that it calls is not installed, say so and name the install decision.
- If the project has the `agent-workflow:core` block but no section for the recommended skill under `## Skills`, say that setup did not select it, and give `/setup-workflow` as the way to add it.
- If a source that the route needs is blocked, such as a tracker without access, say so and name what the user can give instead.

**Done when:** the route fits the goal, the project rules and the installed skills, with no extra stage.

## 3. Answer and stop

1. Start with the recommendation or the comparison.
2. Give the input that the skill needs, the expected result and any decision that the user must make first.
3. If the user wants a next action, give the command: `$name` in Codex, `/name` in clients with slash commands.
4. For a question about the whole process, show the phases as a Mermaid flowchart: from the project's `agent-workflow:core` block, or from the kit README outside a set-up project. For a narrow question, explain only that branch.

**Done when:** the user knows which skill to use, why, and what to have ready. Stop without starting it.
