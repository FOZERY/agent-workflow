# Project writing contract

Read this file when you configure writing routes, languages, clients or instruction loading.
The writing skills are independent. Setup keeps their files unchanged. Setup needs `asd-ste100` and `writing-for-agents` only to write `AGENTS.md` and the project files: it applies both to them whatever route the owner selects here.
Record their approved use in the project's root `AGENTS.md`.

## Routes and languages

1. Agree the language separately for conversation, artifact prose and reusable instructions.
2. If the project has no rule for an output, offer two options: follow a named project convention, or use a named language. For conversation, also offer "follow the user's language".
3. If languages differ by audience or artifact, record the project's own routing rule.
4. Keep a writing policy that is already in effect.
5. For each route without a policy, offer three options: the proposed skill below, an existing policy without a new skill, or no extra style. The owner can choose different styles for different outputs.

| Output | Proposed skill | When the agent reads it |
| --- | --- | --- |
| Conversation with a person | `human-text` and its language reference | At the first prompt of a session, before the first reply |
| Artifacts for people or agents: ADRs, docs, specs, tickets, reports, `CONTEXT.md`, `LESSONS.md` | `asd-ste100` | Before the agent writes or edits the artifact, also for a draft in chat |
| Reusable rules: skills, `AGENTS.md`, procedural references | `writing-for-agents` | Before the agent writes or edits the rules |

- A route becomes a project requirement only after the user approves the configuration.
- Each skill still works alone. Its own scope can be wider than its role here.
- For a mixed document, choose the route by the purpose of each section. A document that agents read is not automatically a rule.
- Keep the required formats, technical content and permissions.
- ASD-STE100 is English. For a required non-English artifact, use an adaptation and claim no English conformance.

## Check the selected skills

1. For each selected writing skill, run the [same-name check](skills.md#check-same-name-copies).
2. Report its reference files, scope, path and discovery in each client. If you cannot check access, report it as unknown, not as missing.
3. Reuse a compatible copy and a trigger that already works. A missing pointer does not need a reinstall.
4. If a selected skill is missing, offer two options: approve its [bounded installation](skills.md#install-plan-and-approval), or leave the route unavailable. A missing writing skill blocks neither setup nor unrelated skills.

## Instruction loading

For each selected route, choose one of three: keep an existing rule, add a project pointer, or leave the route off. Approval to install a skill does not turn it on.

1. The root `AGENTS.md` holds the project pointers. Use a client import only when the client needs it to reach that file.
2. If the user asks for user-wide activation, show that target separately for approval. A global install does not turn the skill on globally.
3. If the user selected global changes, check the effective source:

| Client | User-wide instruction source |
| --- | --- |
| Claude Code | The loaded user instructions, normally `~/.claude/CLAUDE.md`. Follow configured directories and imports. See [memory documentation](https://code.claude.com/docs/en/memory). |
| Codex | The first non-empty `AGENTS.override.md` or `AGENTS.md` under the effective `CODEX_HOME`. See [instruction discovery](https://developers.openai.com/codex/guides/agents-md/). |
| OMP | The native agent-directory instructions, normally under `~/.omp/agent`. Follow profiles and `PI_CODING_AGENT_DIR`. Check client behavior before you rely on precedence. |

4. OMP task subagents do not get `AGENTS.md`. When a subagent does not inherit instructions, put the project rules and readable skill paths in its brief.
5. Route a helper's output by what it is: a helper that returns an artifact follows the artifact route.
6. A native shared-rule file is an option only after the user approves its target and effects.

## Pointer text

Translate the approved triggers into the instruction language. Keep the style details in the installed skills.

> At the first prompt of a session, before replying to the user, read the installed `human-text` skill and its applicable language reference unless already in context. Apply it to conversation. Reuse the guidance while available; reload after context loss or a source change.

> Before writing or editing artifact prose, read the installed `asd-ste100` skill unless already in context. Apply it to documentation, ADRs, specs, tickets, reports, context and lessons, including drafts returned in chat. Preserve project format and language; non-English prose uses an adaptation, not a claim of English conformance.

> Before writing or editing reusable rules, read the installed `writing-for-agents` skill unless already in context. Use it for skills, `AGENTS.md` and procedural references. For mixed documents, select the route by section purpose.

1. In the preview, show the exact pointers, clients, profiles and project or global targets.
2. Show the install sources and destinations as a separate part. Configuration does not approve installation.
3. Write a new pointer only after the selected client can read its target.
4. If installation fails or the user declines it, report the unavailable route and the pointer that you did not write. Keep unrelated instructions.
5. Keep project paths, roles, languages and routing in `AGENTS.md`. Leave installed skill files unchanged.
6. A new pointer cannot change the style of a reply that the session already gave. Tell the user if the client needs a reload or a new session. This setup installs no startup hook.

## Verify

1. Check the selected skills, the local pointers and the instruction entry point. Report these checks separately from observed model behavior.
2. Check the cases that apply: the first reply of a session, an artifact draft in chat, memory versus rules, a mixed document, a non-English artifact.
3. Also check: one writing skill alone, setup alone, no writing skill selected, a missing or declined installation, an existing global trigger, a helper without inherited instructions.
4. On an unrelated rerun, keep the accepted choices.
5. Launch a live client or a helper as a probe only with the user's approval.

**Done when:** each approved writing route is configured or has a precise installation or loading blocker, and every unselected skill stays optional.
