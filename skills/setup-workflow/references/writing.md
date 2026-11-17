# Project writing contract

Read when configuring writing routes, languages, clients or instruction loading.
The writing packages are independent. Setup neither needs them to run nor changes their prompts for a consumer project.
Configure their approved use in that project's root `AGENTS.md`.

## Routes and language

Propose this composition unless the project already has an authoritative writing policy:

| Output | Proposed package | Project loading trigger |
| --- | --- | --- |
| Conversation with a person | `human-text` and its applicable language reference | At the first prompt, before the first reply |
| Artifacts for people or agents, including ADRs, docs, specs, tickets, reports, context and lessons | `asd-ste100` | Before drafting or editing the artifact, including a draft returned in chat |
| Reusable rules, including skills, `AGENTS.md` and procedural references | `writing-for-agents` | Before drafting or editing rules |

These are project requirements only after configuration approval.
The packages remain usable alone; a package's general scope can be broader than its assigned role here.
Classify mixed output by section purpose. An agent reading a document does not make that document an execution rule.
Agree conversation, artifact and instruction languages. Preserve required formats, technical content and permissions.
ASD-STE100 is English. Required non-English artifacts use an adaptation, not a claim of English conformance.

## Check selected packages

For each approved route, run the [same-name check](skills.md#check-same-name-copies).
Report complete references, scope, path and target-client discovery. Unknown access is not confirmed absence.
Reuse compatible copies and effective triggers. A missing pointer does not require reinstalling the package.
If a project-selected package is missing, obtain a bounded deployment decision or leave that route explicitly unavailable.
Do not silently install it or block standalone setup and unrelated skills.
An explicit decision to use no writing package is valid; preserve any higher-priority writing rules already in effect.

## Instruction loading and approval

For project activation, root `AGENTS.md` owns the pointers.
Use an existing client import only when needed to reach that file.
Global installation does not imply global activation; global instruction changes require separate approval.
Verify the effective source when global changes were explicitly selected:

| Client | User-wide instruction source |
| --- | --- |
| Claude Code | Loaded user instructions, normally `~/.claude/CLAUDE.md`; honor configured directories and imports. See [memory documentation](https://code.claude.com/docs/en/memory). |
| Codex | First applicable non-empty `AGENTS.override.md` or `AGENTS.md` under effective `CODEX_HOME`. See [instruction discovery](https://developers.openai.com/codex/guides/agents-md/). |
| OMP | Active native agent-directory instructions, normally under `~/.omp/agent`; honor profiles and `PI_CODING_AGENT_DIR`. Verify client behavior before relying on precedence. |

OMP task subagents do not inherit context files named `AGENTS.md`.
Supply applicable project rules and readable package paths in a delegated brief when inheritance is absent.
Describe the actual output: a helper returning an artifact follows the configured artifact route.
A native shared-rule file is an option only after its target and effects are separately approved.

## Pointer text

Adapt approved triggers to the instruction language. Keep style details in the installed packages.

> At the first prompt of a session, before replying to the user, read the installed `human-text` skill and its applicable language reference unless already in context. Apply it to conversation. Reuse the guidance while available; reload after context loss or a source change.

> Before writing or editing artifact prose, read the installed `asd-ste100` skill unless already in context. Apply it to documentation, ADRs, specs, tickets, reports, context and lessons, including drafts returned in chat. Preserve project format and language; non-English prose uses an adaptation, not a claim of English conformance.

> Before writing or editing reusable rules, read the installed `writing-for-agents` skill unless already in context. Use it for skills, `AGENTS.md` and procedural references. For mixed documents, select the route by section purpose.

Show exact pointers, clients, profiles and project/global targets in the configuration preview.
Show deployment sources and destinations separately. Configuration does not authorize installation.
Write a new activation pointer only after its target is readable by the selected client.
If deployment fails or is declined, report the unavailable project route and unwritten pointer; preserve unrelated instructions.
Do not edit installed package prompts to encode project paths, roles, languages or this routing.

A newly saved pointer cannot retroactively style the current session's first reply.
State any required client reload or new session. This prompt installs no startup hook.

## Verify

Check the selected packages, local pointers and instruction entrypoint separately from observed model adherence.
Consider first-prompt conversation, artifact drafts in chat, memory versus rules, mixed documents and non-English artifacts.
Also consider one writing package alone, setup alone, no writing selection, missing or declined deployment, existing global triggers and helpers without inherited instructions.
Preserve accepted choices on unrelated reruns.
Do not launch a live client or substantive helper without approval for that probe.

**Done when:** approved writing routes are configured or have precise deployment/loading blockers, and every unselected package remains optional.

