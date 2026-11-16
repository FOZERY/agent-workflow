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
| Configure or revise project procedures, permissions, artifact locations or selected packages | `setup-agents-workflow` |
| Challenge an idea, clarify the desired outcome and uncover overlooked questions | `grilling` |
| Explore questions while developing domain terms and decision records | `grill-with-docs` |
| Agree domain language, business concepts and consequential decisions | `grill-with-docs` (it loads the `domain-modeling` helper) |
| Investigate a question deeply and preserve a sourced research report | `research` |
| Find the route through a large, uncertain effort too big for one session | `wayfinder` |
| Reason about module boundaries and interfaces | `codebase-design` |
| Run a bounded experiment to answer a design question | A prototype ticket in `wayfinder`, which loads the `prototype` helper |
| Diagnose architectural friction in an existing codebase | `improve-codebase-architecture` |
| Evaluate an incoming issue, relevance, ownership and overlapping work | `triage` |
| Synthesize agreed requirements, then decompose work if needed | `to-spec`, `to-tickets` |
| Write independent test-first checks through a test-author subagent | `tdd` |
| Implement one agreed task, or coordinate a specification/task graph | `implement`, `implement-spec` |
| Review current changes independently, including before a commit | `code-review` |
| Prepare or publish a PR/MR under project delivery rules | `pr` |
| Discuss experience and preserve confirmed project lessons | `retro` |
| Improve prose; refactor existing documents; retire stale artifacts | `plain-writing`; `refactor-docs`; `cleanup`, respectively |

Recommend only the relevant next step and explain its input, expected result and outstanding human decision. Existing analyst-owned requirements may go directly to implementation; they need not pass through spec/ticket authoring. Routine fact lookup does not require a deep research report. A ready-for-human-review task needs the person's review, not another skill merely to keep the agent busy.

Implementation may stay in the discussion thread. Optional TDD uses a fresh test-author subagent, while the implementation review uses a fresh reviewer subagent or a user-run review session. Consult the installed implementation cycle for precise review and acceptance gates. A commit request, a passing check and permission to publish are distinct facts.

If the candidate or its required dependencies are missing, explain that gap and the setup/install decision instead of treating it as runnable. Naming several related skills does not require installing them all. Reuse configured artifact locations and distinguish recent `CONTEXT.md`, durable `LESSONS.md`, mandatory project rules and authoritative requirements/ADRs.

**Done when:** the recommended route fits the known goal, project policy and available capabilities, without adding unnecessary stages.

## 3. Answer and stop

Lead with the recommendation or direct comparison. Cite the relevant project rule or skill source when available. Give a ready-to-use invocation in the current client's supported syntax when the user wants a next action; distinguish a skill invocation from a tool with a similar name. For example, Codex uses `$ask-workflow`, while slash-command clients use `/ask-workflow`.

For a workflow overview, show a compact phase map; for a narrow question, explain only the relevant branch. State blockers or unverified availability beside the recommendation. The user chooses whether to proceed; finish without launching the suggested procedure.

**Done when:** the user understands what to use, why it fits and what is needed before starting it.
