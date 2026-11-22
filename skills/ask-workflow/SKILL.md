---
name: ask-workflow
description: "Explain this workflow and suggest the next appropriate skill."
argument-hint: "[workflow question or current task state]"
disable-model-invocation: true
---

# Ask about the workflow

Answer questions about this kit, compare skills and help the user choose the next step. This is an advice-only guide, not an orchestrator: recommend an invocation without invoking other skills, installing packages, editing artifacts or starting Git/tracker operations. No other skill is required to use this guide.

## 1. Establish what the answer depends on

For a general question, use the routing map below. For project-specific advice, read root `AGENTS.md` (or the project's `CLAUDE.md`) and only the relevant procedure pointers. Use recent conversation and, when needed, the configured `CONTEXT.md` to identify the current task state; memory is not proof that checks passed or a decision was accepted.

Inspect available skill discovery information, including user-invoked skills hidden from automatic model selection, to distinguish selected, installed and permitted procedures. Claude Code hides manual skills from the model and helper skills from the `/` menu, so check the skill folders directly: `.claude/skills/` and `~/.claude/skills/` for Claude Code; `.agents/skills/`, `~/.agents/skills/` and `~/.codex/skills/` for Codex; `.omp/skills/` and `~/.omp/agent/skills/` for OMP. Before giving detailed instructions about a particular skill, read its available prompt and relevant references without executing it. An upstream or same-named global package may differ from this kit. If the package or project policy is unavailable, explain the general route and label the missing information; an incomplete discovery list does not prove a skill is absent.

Ask a focused question only if a missing goal, state or decision changes the recommendation. No project setup is needed merely to explain the workflow.

**Done when:** the question can be answered from identified sources, or the uncertainty that changes the answer is explicit.

## 2. Choose the smallest useful route

Use this map to locate candidate skills, not as a required sequence or a substitute for their actual prompts:

| Need | Candidate |
| --- | --- |
| Establish or revise a navigation and shared-material home for several repositories | Optional manual `home-repo-init` |
| Configure or revise project procedures, permissions, artifact locations or selected packages | `setup-workflow` |
| Challenge an idea, clarify the desired outcome and uncover overlooked questions | `grilling` |
| Explore questions while developing domain terms and decision records | `grill-with-docs` |
| Agree domain language, business concepts and consequential decisions | `domain-modeling`, also used by `grill-with-docs` |
| Investigate a question deeply, including a wayfinder research ticket | `research` |
| Find the route through a large, uncertain effort too big for one session | `wayfinder` |
| Reason about module boundaries, investigate architecture or evaluate an incoming issue | Follow the project procedure and inspect relevant evidence |
| Run a bounded experiment to answer a design question | `prototype`, also used by prototype tickets in `wayfinder` |
| Design a module interface or choose a test seam | `codebase-design` |
| Explain a design question with an optional editable diagram | Bundled `excalidraw-diagram`, after consent and through a separate drawing subagent |
| Plan an existing task for implementation without creating a spec or tickets | `to-plan` |
| Synthesize agreed requirements, then decompose work if needed | `to-spec`, `to-tickets` |
| Run original test-first red–green cycles; audit or prune existing tests | `tdd` |
| Implement one agreed task in the current session | `implement` |
| Coordinate workers on a large task while the main session acts as architect | `implement-with-swarm` |
| Simplify changed code and roll back needless guards, fallbacks and abstractions | `simplify-codebase` |
| Review scoped uncommitted changes or an explicit committed branch, PR or commit | `code-review` |
| Prepare or publish a PR/MR | Follow project delivery rules and permissions |
| Inspect session evidence for agent-environment improvements | `retro` |
| Write conversational replies; write artifacts; write reusable agent rules | `human-text`; `asd-ste100`; `writing-for-agents`, respectively |
| Refactor existing artifacts; retire stale artifacts | `refactor-docs`; `cleanup`, respectively |

Recommend only the relevant next step and explain its input, expected result and outstanding human decision. Existing analyst-owned requirements may go directly to implementation; they need not pass through spec/ticket authoring. Routine fact lookup does not require a deep research report. A ready-for-human-review task needs the person's review, not another skill merely to keep the agent busy.

A ready task can go through `to-plan` when it needs a saved implementation plan. Hand the plan and source task to an executor that can read both.

For `implement-with-swarm`, use existing task sources. No spec, ticket graph, or tracker is required. Recommend separate sessions for multiple repositories or worktree isolation. Consider subagents for disjoint changes in one repository if they can run `implement` and delegate required review.

For a multi-repository home, recommend `home-repo-init` for structure, navigation and approved shared materials.
Recommend `setup-workflow` afterward only if workflow procedures need configuration. `to-plan` remains task planning, not home initialization.
Explain that the home preserves child rules and needs verified instruction and skill access from child-start sessions and workers.
An existing home needs only proposed deltas. A missing local repository needs clone permission, not an automatic clone from a pointer.
Read the available package for detailed scope and approval rules; do not inventory repositories or execute this manual skill as part of advice.

For design diagrams, recommend `excalidraw-diagram` only when a visual explanation would help. It is optional support, not a required phase. Selection or installation is not generation consent; an explicit diagram request is consent. Explain that approval permits a separate drawing subagent with a narrow brief, while refusal continues without diagram work. This advice-only skill does not dispatch that subagent, even when consent exists.

Point to the package prompt and project setup rules for the drawing route. Keep generation references and library JSON out of advice context. The worker returns editable `.excalidraw` and PNG paths, visual-check results and caveats. Missing delegation, required assets or render permission blocks only the diagram branch, with no same-context fallback. Keep ADR decisions and contracts in authoritative text; diagrams do not replace prototypes, plan approval or user acceptance.

For pre-commit review, explain the bundled `implement` default: it sends the task's file paths and review base to `code-review`. Both reviewers use the same pinned working-tree snapshot. It includes intended staged, unstaged and nonignored untracked changes within those paths. For explicit branch, PR or commit review, recommend the committed endpoint.

Apply explicit project settings first. Recommend a custom reviewer only if the bundled procedure cannot cover the chosen policy or approved scope. If the required procedure cannot cover the intended changes, report the gap. A separate manual invocation remains manual. Neither review nor setup grants permission to delegate, commit or publish.

The kit includes the fixed helper dependencies, but the target client must have them installed. Read the actual prompt before advising. The former local separate test-author and three-round acceptance cycle are absent.

If the candidate or its required dependencies are missing, explain that gap and the setup/install decision instead of treating it as runnable. Naming several related skills does not require installing them all. Reuse configured artifact locations and distinguish recent `CONTEXT.md`, durable `LESSONS.md`, mandatory project rules and authoritative requirements/ADRs.

**Done when:** the recommended route fits the known goal, project policy and available capabilities, without adding unnecessary stages.

## 3. Answer and stop

Lead with the recommendation or direct comparison. Cite the relevant project rule or skill source when available. Give a ready-to-use invocation in the current client's supported syntax when the user wants a next action; distinguish a skill invocation from a tool with a similar name. For example, Codex uses `$ask-workflow`, while slash-command clients use `/ask-workflow`.

For a workflow overview, show a compact phase map; for a narrow question, explain only the relevant branch. State blockers or unverified availability beside the recommendation. The user chooses whether to proceed; finish without launching the suggested procedure.

**Done when:** the user understands what to use, why it fits and what is needed before starting it.
