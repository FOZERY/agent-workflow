---
name: setup-workflow
description: "Configure or revise a project's agent workflow, permissions, tool requirements and approved skill installation."
argument-hint: "[project context or settings to change]"
disable-model-invocation: true
---

# Setup Workflow

Set up the agent workflow of one project through a conversation with the user. Write the agreed rules in the root `AGENTS.md`.
Use the same steps for an initial setup and for a rerun that changes some settings.

Setup writes project rules. With separate approval, it also installs skills. Setup keeps installed skill files unchanged and does not run their workflows.

## Rules for every step

- **Ask.** Ask only what the project files and the user's answers do not already settle. Ask in small rounds.
  Ask through the harness's question tool, such as `AskUserQuestion` in Claude Code, with all questions of one round in one call. Use plain text only when the harness has no question tool.
  For a choice with known options, ask a separate question in that tool. Give the allowed options and the effect of each.
  For project-specific details, ask an open question. If no option fits, let the user describe the workflow or point to its source.
  One answer can settle several questions.
- **Permission.** Only an explicit "yes" from the user grants a permission. A recommendation, silence or an unanswered question grants nothing.
- **Approval sets.** Rules, installation and later operations are three separate approvals. Approval of one set does not approve another.
- **Mandatory rules.** A company or project rule wins over a skill default and over a preference.
  If two rules conflict and their authority is not clear, show both sources. Block the affected action until the owner decides. Continue the other setup work.
- **Blockers.** If a required skill, source, tool or operation is missing or forbidden, record the blocked step and tell the user. Keep the step blocked; use no substitute procedure.
- **Credentials.** Ask for no credentials and record none.

## 1. Read the current state

1. Read the project: instructions and how the client loads them, product documentation, task sources, repository layout, checks and representative tests. Ask the user only for what these sources do not give.
2. For an initial setup, or a change of instruction owner or memory, read [project artifacts](references/project-artifacts.md). Keep existing instructions, client wrappers and records.
3. If shared files in a company repository are restricted, agree an allowed local loading mechanism with the user.
4. If the project spans repositories, find out whether setup targets the home repository or one child. Follow the [home-repo boundaries](references/project-artifacts.md#multi-repository-homes) and keep the existing navigation.
   If the home must be created or reorganized first, recommend that the user run `home-repo-init` separately. Setup does not do that migration.
5. On a rerun, show the current settings, the known skill availability and the open gaps. Ask what the user wants to change.
   Limit later reading, questions, edits and checks to that change and to what depends on it. If the user wants only an overview, stop here and write nothing.

**Done when:** the scope, the instruction owner, the current settings and the requested change are known. Inaccessible sources are listed as gaps.

## 2. Agree the rules

Go through the parts below in order. On a rerun, ask only the parts that the change affects.

### 2.1 Shared rules

1. Ask which company or project rules setup must keep. Accept links, paths or a description in the user's words.
2. Read those sources through approved access. For each rule, record whether it is mandatory or a preference, what it applies to and when the agent checks it.
3. Agree these topics:
   - Product purpose, working boundaries and authoritative requirements.
   - Artifact locations, owners, formats and visibility: tracked, ignored or local. Link external sources instead of local copies.
   - Autonomy and human checkpoints. Ask about read-only exploration and about implementation delegation as two questions. Options for each: allowed within agreed limits, needs separate approval, or not allowed. Writes follow the delivery, tracker or tool rules.
   - Languages for conversation, artifacts and instructions. To configure writing styles, read [writing routes](references/writing.md).
   - Memory: directory, reading and update checkpoints, writer and approval scope. Follow [project artifacts](references/project-artifacts.md).
   - Lessons: ask "When a disputed question is settled or you correct me, should I ask before I write a lesson, or write it myself and tell you?" Record the matching lessons variant from [core rules](references/core-rules.md).
4. If Git settings are missing or change, read [delivery settings](references/delivery.md).

### 2.2 Skills

1. Offer the skills from [the catalog](references/catalog.md) as one multi-select: each skill is a separate option, plus "no other skills" and the skills that the user suggests. Offer no ready-made bundles. Show each skill's purpose and installation status, and leave every option unselected until the user selects it.
2. For installation or a change of client or scope, read [deployment](references/skills.md).
3. Before you propose settings for a selected skill, read its `SKILL.md`. Agree its sources, output location, project practices and allowed operations.
4. Keep shared paths and permissions in one place in `AGENTS.md`. A skill section holds only the settings of that skill.
5. For `to-plan`, `to-spec`, `to-tickets`, `wayfinder` and `excalidraw-diagram`, ask the questions in [skill questions](references/skill-questions.md).

### 2.3 Implementation, TDD, simplify and review

1. For `tdd`, ask: "How do we work with tests here? Which test types and existing examples should guide us? What infrastructure or mocking constraints apply?" Find the test commands yourself.
2. For review, ask which requirements, coding practices and examples guide it. Accept a project procedure or another review skill. Record the procedure as prose.
3. Ask each question below that belongs to a selected skill, as a separate form question with its options. Each such question is required, also when the user has no preference.
   1. TDD trigger: does `implement` start TDD automatically, or only when the user asks?
   2. TDD location: the current session, a subagent that writes only the failing tests, or a separate session?
   3. Simplify trigger: does `implement` start `simplify-codebase` automatically after the implementation, or only when the user asks?
   4. Simplify location: where does `simplify-codebase` look for simplifications: a subagent (recommended), the current session, or a separate session? The implementing session always applies them.
   5. Review trigger: does `implement` start review automatically, or only when the user asks?
   6. Agents for each role: which agent, model and reasoning effort for the `implement` workers, the `simplify-codebase` finder, the Standards reviewer and the Spec reviewer? List what the harness and Orca offer. Do not assume model names: harnesses name models and roles differently. A common split is a standard model for workers, the finder and Standards, and the strongest model for Spec.
   7. Review follow-up: report findings and wait, or fix and review again?
   8. Review rounds: how many fix-and-review rounds before the agent stops and asks? Offer `3` as the default.
4. Agree which implementation routes each trigger covers.
5. Ask the [review coverage questions](references/AGENTS.md#review-coverage). Use the [automation settings](references/AGENTS.md#automation-settings) for the meaning of each answer.
6. Before you record an answer, check that the skill can run it. For example, the session that runs `code-review` launches its reviewers as subagents. If the harness cannot launch subagents, show the gap and ask the user how review runs instead.
7. Record the installed `SKILL.md` path of `tdd`, `simplify-codebase` and `code-review` for each client in their `skill` setting, and the installed path of `implement/WORKER.md` in the `implement` section. A subagent that runs a skill reads that file, so check that the path exists.
8. Read the harness documentation in this setup before you state how deep subagents can launch subagents. Your memory of the harness is not a source. For Claude Code, read <https://code.claude.com/docs/en/sub-agents> and check `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` in the settings and the environment.

TDD keeps the red-green loop. If TDD runs in a subagent, that subagent writes only the failing tests, from the requirements and the interface.

For the workers of `implement`:

Each worker runs in a separate session with its own thread and launches its own subagents.

1. Ask which tool starts worker sessions, for example Orca.
2. Ask whether dispatch needs approval, and which branch, worktree or workspace isolation workers use.
3. Record the answers in the `implement` section.

### 2.4 Search

1. Ask: "Should bulk searches across files, logs and the web run in the current session or in a subagent?"
2. If the user selects a subagent, list the search agents of the harness: user-defined agents, built-in search roles and cheaper models. Ask which agent and model to use.
3. Record the matching search variant from [core rules](references/core-rules.md).

### 2.5 Other skills and tools

1. Ask: "Do we need any other skills, tools or MCP integrations for this repository? Give a name, a link or a short description, or say none."
2. For each addition, agree its purpose, when to use it and its allowed actions. If its targets and data are not defined, ask about them.
3. Find out whether the addition is available or needs setup. Check that the client and the delegated workers can reach it and its instructions.
4. Record a missing tool or MCP configuration as a prerequisite for separately approved work. A tool named in setup is not approved for installation, connection or use.
5. Ask for practices or examples that the earlier questions did not cover.

### 2.6 Compatibility

Check the selected settings against skill dependencies, client capabilities and the handoff from `implement` to review. Look for these gaps:

- A required helper skill is not installed.
- The review comparison does not include the intended changes.
- A mandatory operation is forbidden.
- A separate session is selected, but the client cannot start one and no user-started handoff is agreed. Setup does not create sessions.

Record each gap with its blocked step.

**Done when:** every applicable topic has an agreed answer, an authoritative source, or a recorded gap with its blocked action. Unselected workflows need no answers.

## 3. Draft and get approval

1. Read [the AGENTS.md structure](references/AGENTS.md) and [core rules](references/core-rules.md). Read the installed `asd-ste100` and `writing-for-agents` skills and apply both to every file that you draft. If one is missing, stop this step, tell the user and offer its [bounded installation](references/skills.md#install-plan-and-approval). Continue the unrelated work.
2. Put the core block in `## Workflow rules` and fill its fields. Build its phase list from the selected skills.
3. Write a section under `## Skills` for every selected skill. Start each section with its `Runs:` line.
4. Write the shared sections with the agreed facts. Omit the sections that do not apply. Use a skill default only where it fits the project rules and permissions. Follow the project's writing rules.
5. Keep `AGENTS.md` under 300 lines. Move each procedure, standard and long fact set to a file under `<agent-docs>/project/` and link it with a trigger. Link existing practices instead of copying them. The setup references are drafting guides, not project runbooks.
6. Put each mandatory restriction in the section that controls its action. Give each policy and tool pointer a trigger: when the agent reads it.
7. For a private policy, record only what the visibility rules permit. Check that the intended reader can open the authoritative rule.
8. Show a preview: the line count of `AGENTS.md`, the project files that you will create, changed rules and pointers, changed visibility and compatibility gaps. Mark new or changed permissions and mandatory restrictions. On a rerun, also list the permissions and restrictions that stay the same.
9. Show the installation as a separate set of actions. Get approval for each set.

Approval of the rules or the installation does not approve implementation, publication or global changes.

**Done when:** the owner approved the affected rules and files, and separately any installation. An open conflict blocks only its own action.

## 4. Apply the changes

1. Read the target files again and merge only the approved edits.
2. On an initial setup, create or reuse the root `AGENTS.md`, `CONTEXT.md` and `LESSONS.md` as [project artifacts](references/project-artifacts.md) describes. Fill memory from the actual discussion. Create the approved files under `<agent-docs>/project/`.
3. On a rerun, keep unrelated settings and history. If the core block version in `AGENTS.md` differs from [core rules](references/core-rules.md), show the difference. After approval, replace only the block.
4. Apply the approved loading and visibility changes. Create plans, specs, tickets, glossaries and ADRs only when a task needs them. A move or a storage migration needs its own approval.
5. If the user approved installation, follow [deployment](references/skills.md). Reuse compatible skills, keep license notices and report partial failures.
6. Add a writing-style pointer only when its target file is readable.

**Done when:** each approved edit and installation has an observed result or a named blocker.

## 5. Verify and hand over

1. Check that `AGENTS.md` has the core block with all fields filled, stays under 300 lines, and gives every pointer a trigger.
2. Check local pointers, artifact paths, client loading where you can observe it, and skill discovery and prerequisites.
3. Check that each setting has one owner section and that the user's additions are present.
4. Check the cases that apply:
   - **Rerun:** unrelated settings and installations stay as they were.
   - **Conflict:** a project restriction wins over a skill default or a proposed permission, and the affected action is blocked.
   - **Home repository:** each child keeps its own instructions, and each session and worker can read the shared pointers.
   - **Automation:** every setting has an answer. With `manual`, `implement` launches nothing automatically.
   - **Review coverage:** the pre-commit review covers the intended files at the agreed checkpoint, also with another reviewer or endpoint.
   - **Reach:** each added skill, tool, MCP integration and policy pointer is reachable by its reader, including delegated workers, or is recorded as a prerequisite.
   - **Gaps:** each missing helper, source or separate session is recorded with its blocked step or agreed handoff.
5. For memory or writing changes, also use the checks in their references.
6. Tell the user which checks were static and which ran live. Get approval before you launch a client or a helper as a probe.

**Done when:** you reported the saved files, the changed settings, the installation and discovery results, the limits of verification and the blocked actions. Tell the user how to run setup again: `$setup-workflow` in Codex, `/setup-workflow` in Claude Code. Stop after setup.
