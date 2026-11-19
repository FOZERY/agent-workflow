---
name: setup-workflow
description: "Configure or revise a project's agent workflow, permissions, tool requirements and approved skill installation."
argument-hint: "[project context or settings to change]"
disable-model-invocation: true
---

# Setup Workflow

Configure a project's agent instructions through conversation. Read what the project already defines, ask for missing decisions, and write the agreed rules in root `AGENTS.md`. Use the same process for initial setup and targeted changes.

This package works alone. Setup configures skill use; it does not rewrite installed skills or execute their workflows. Configuration, installation and operational permissions are separate decisions.

## 1. Establish the current setup

Inspect the working scope: existing instructions and client loading, product documentation, task sources, repository layout, checks and representative tests. Reuse authoritative sources instead of asking the user to repeat them.

For initial setup or changes to instruction ownership or memory, read [project artifacts](references/project-artifacts.md). Preserve existing instructions, client wrappers and records. In a company repository with restricted shared files, agree an allowed local loading mechanism.

For a project spanning repositories, identify whether this setup targets the coordinating home repo or one child. Follow [home-repo boundaries](references/project-artifacts.md#multi-repository-homes) and preserve existing navigation. If a home must first be created or reorganized, recommend a separate user invocation of `home-repo-init`; do not perform that migration as workflow configuration.

On a rerun, show current settings, known package availability and unresolved gaps, then ask what the user wants to change. Limit subsequent reading, questions, edits and verification to that change and its dependencies. An overview-only request ends without writes.

**Done when:** the working scope, instruction owner, existing settings and requested change are clear. Report inaccessible sources as gaps.

## 2. Discuss the project and selected skills

Ask only the applicable questions that existing rules or explicit answers have not settled. Use small rounds.
For a decision with known options, give a separate question or form control with the allowed choices. Explain their practical effects.
When the choices do not fit, let the user describe their workflow or point to its source. Use open questions for project-specific details.
Accept one reply that settles several questions. A recommendation, silence or an unanswered permission question does not grant permission.

### Shared rules

Before proposing workflow choices, ask which company or project rules the setup must preserve. On a targeted rerun, ask only about gaps that affect the change.
Accept links or paths to policies, runbooks, project instructions or skills. Accept a description in the user's own words when no written source exists.
Read the relevant sources through approved access. Distinguish mandatory rules from preferences. Identify what each rule applies to and when the agent must check it.
If rules conflict, follow the established authority. If the conflict remains unresolved, show both sources and block the affected action until the responsible owner resolves it.
Do not use a preferred option or a skill default to override a mandatory rule.

Establish:

- Product purpose, working boundaries and authoritative requirements.
- Artifact locations, owners, formats and tracked, ignored or local visibility. Preserve external sources without duplicate local records.
- Autonomy and human checkpoints. Ask separately about read-only exploration and implementation delegation: within agreed limits, with separate approval, or not allowed for the agent. Confirm any applicable scope and checkpoints. For writes, use the action-specific delivery, tracker or tool rules.
- Conversation, artifact and instruction languages. When configuring styles, read [writing routes](references/writing.md).
- Context and lessons: shared directory, reading and update checkpoints, writer and approval scope. Follow the project-artifact contract.
- Lessons: ask "When a disputed question is settled or you correct me, should I ask before I write a lesson, or write it myself and tell you?" Record the answer with the lessons variant from [core rules](references/core-rules.md).

For Git workflows, read [delivery settings](references/delivery.md) only when those settings are missing or changing.

### Skill-specific rules

Use [the catalog](references/catalog.md) to discuss applicable skills, including user-suggested packages. For installation or client/scope changes, read [deployment](references/skills.md).

Read the selected prompts before proposing settings. Establish the sources, output location, project practices and permitted operations each needs. Keep shared paths and permissions in one place; skill sections contain only their specific settings and differences.

For `tdd`, ask: "How do we work with tests here? Which test types and existing examples should guide us? What infrastructure or mocking constraints apply?" Inspect test commands rather than asking the user to transcribe them. Keep the red–green method. If TDD runs in a subagent, that subagent writes only the failing tests, from the requirements and the interface.

For review, ask which requirements, coding practices and examples guide it. Accept a project procedure or another review skill as the source. Record the procedure as prose, not a package-name flag.

For implementation routes, ask every question below. Each question is required, also on an initial setup where the user gives no preference. Ask each one as a separate form question with its allowed choices:

1. TDD trigger: does `implement` start TDD automatically, or only when the user asks?
2. TDD location: the current session, a subagent that writes only the failing tests, or a separate session?
3. Review trigger: does `implement` start review automatically, or only when the user asks?
4. Review location: the current session, a subagent, or a separate session?
5. Reviewer: which agent, model and reasoning effort review? List what the harness and Orca offer.
6. Review follow-up: report findings and wait, or fix and review again?
7. Review rounds: how many fix-and-review rounds before the agent stops and asks? Offer `3` as the default.

Agree which implementation routes each trigger covers.

If `implement-with-swarm` is selected, ask whether workers run as separate sessions or as subagents. Then check nesting:

1. Find out which harness runs the workers and how deep subagents can launch subagents in it. Read the harness documentation. If it does not say, ask the user's approval for a short probe.
2. A worker that runs `implement` with TDD or review in subagents needs one more level of subagents. If the harness cannot give that level, warn the user before you record the settings.
3. Offer these options and record the user's choice in the `implement` and `implement-with-swarm` sections:
   - Run workers as separate sessions, for example in Orca. Each worker session launches its own subagents.
   - Keep subagent workers. Each worker runs TDD in its own context, and the architect launches the reviewers for each worker's result.
   - Keep subagent workers. The user starts `/code-review` for each worker's result.

Before you record an answer, check that the selected skill can run it. For example, `code-review` runs its two reviewers as subagents. If the harness cannot launch them from the selected location, show the gap and ask the user to choose another location.
Then use the [review questions](references/AGENTS.md#review-coverage) for coverage, timing and followup. Use the [automation settings](references/AGENTS.md#automation-settings) for the meanings of the answers. The user decides whether to accept the work.

For `to-plan`, agree the task-linked location and naming. Ask separately about visibility, plan approval and who can revise an approved plan.
For visibility, offer only allowed choices: tracked in Git, ignored in the repository, or in an approved private location.
For approval, ask whether a draft can be saved for review or approval is required before saving. Use the project's procedure for any other checkpoint.
For revisions, distinguish edits within agreed limits, edits requiring approval, and edits by the plan owner only.
Agree the receiving executor and the separate authorization to start implementation. Check that it can take the plan and source task without requiring a new spec or tickets.
Keep plans with the task's other artifacts where permitted. Configure the handoff in project instructions without changing installed skill prompts.

For visual design support, offer the optional bundled `excalidraw-diagram` package. If selected or its settings change, read [diagram configuration](references/diagrams.md). Agree one project policy and link applicable skill sections to it; package approval is not consent to generate a diagram.

For tracker-backed planning, ask which sources own the requirements and tickets. If `wayfinder` is selected, ask where its decision map belongs separately.
For each needed tracker operation, distinguish allowed within a named scope, separate approval, and human-only. Ask only about operations the route needs.
Include reading, creating, editing, commenting, labeling, assigning, linking, changing state and closing as applicable. A readiness label does not authorize starting work or publishing.
Use only the selected tracker seed when no adequate project procedure exists:

- [GitHub](references/issue-tracker-github.md)
- [GitLab](references/issue-tracker-gitlab.md)
- [Local Markdown](references/issue-tracker-local.md)

For another tracker, derive the procedure from its agreed sources and access method. Keep readiness vocabulary required by selected skills; setup does not configure incident triage. Read [domain documents](references/domain.md) only when glossary or ADR conventions need configuration.

### Search

Ask: "Should bulk searches across files, logs and the web run in the current session or in a subagent?"
If the user chooses a subagent, list the search agents that the harness offers: user-defined agents, built-in search roles and the cheaper models. Ask which agent and model to use. Record the answer in the core block, using the subagent variant from [core rules](references/core-rules.md).

### Additional skills and tools

Before finalizing the selected routes, ask: "Do we need any other skills, tools or MCP integrations for this repository? Give a name, a link or a short description, or say none."
For each addition, agree its purpose, when to use it and its allowed actions. Distinguish an available integration from one that needs setup. Ask which targets and data it can access when that is not already defined.
Check whether the intended client and delegated workers can reach the skill, tool and relevant instructions. Do not request or record credentials.
Record missing tools or MCP configuration as prerequisites for separately authorized work. Mentioning a tool does not authorize installing, connecting or using it.
Ask for any remaining practices or examples not covered by the interview.

Check skill dependencies, client capabilities and implementation-to-review handoffs against proposed settings. A required helper may be absent, a comparison may exclude the intended changes, or a mandatory operation may be forbidden. Identify the blocked step rather than silently substituting another procedure. A separate-session choice requires either client support or a user-started handoff; setup does not promise thread creation.

**Done when:** every applicable topic has an agreed answer, an authoritative source, or an explicit gap with its affected action. No unselected workflow is required merely to complete the interview.

## 3. Draft and approve

Read [the AGENTS.md structure](references/AGENTS.md) and [core rules](references/core-rules.md). Put the core block in the `## Workflow rules` section with its fields filled. Build its phase list from the selected skills. Write a section under `## Skills` for every selected skill, starting with its `Runs:` line. Draft shared rules and sections for selected skills with project-specific settings. Fill agreed facts and omit inapplicable sections. Use skill defaults only where they fit existing rules and permissions. Use the project's effective writing rules.

Keep root instructions short. Link existing practices before proposing supporting files. Store detailed new procedures under the agreed agent-documentation directory only when needed. The setup references guide drafting; they are not the consumer project's runbooks.
Record mandatory restrictions in the controlling shared or skill-specific section. Give each policy and tool pointer a trigger.
If a policy is private, record only what the project's visibility rules permit. Verify that the intended reader can reach the authoritative rule.

Preview the rule and pointer changes, visibility changes, and compatibility gaps. Call out new or changed permissions and mandatory restrictions. On a rerun, show which applicable permissions and restrictions stay unchanged. Present installation as a separate bounded action set. Obtain approval for each requested set. Neither set authorizes later implementation, publication or global changes.

**Done when:** the owner has approved the affected rules and files, and separately any deployment. Unresolved conflicts block their affected actions, not unrelated setup work.

## 4. Apply the agreed changes

Re-read target files for intervening changes and merge only approved edits. On initial setup, create or reuse root `AGENTS.md`, `CONTEXT.md` and `LESSONS.md` according to the artifact contract. Seed memory from the actual discussion. On reruns, preserve unrelated settings and history. If the core block version in `AGENTS.md` differs from [core rules](references/core-rules.md), show the difference and replace only the block after approval.

Apply approved loading and visibility changes. Create no empty future plans, specs, tickets, glossaries or ADRs. Moves and storage migrations require their own agreement.

If installation was approved, follow the deployment reference. Reuse compatible packages, preserve notices and report partial failures. Finalize writing activation pointers only when their targets are readable. Leave reusable package prompts unchanged.

**Done when:** each approved edit and deployment has an observed result or a specific blocker.

## 5. Verify and hand over

Check that `AGENTS.md` has the core block with all fields filled. Check local pointers, configured artifact paths, client loading where observable, and selected package discovery and prerequisites. Confirm that per-skill settings have one owner and user additions are represented. A project instruction is not an access-control mechanism or proof of model adherence.

Walk through only relevant cases:

- Initial setup versus a targeted rerun; unrelated settings and installations stay intact.
- A known option uses its own question. A custom policy supplied as prose or a link keeps its scope and approval conditions.
- A project or company restriction conflicts with a skill default or proposed permission: preserve the rule and block the affected action if the conflict is unresolved.
- A home repo coordinates several children: preserve their instruction ownership and verify shared pointers from each intended session or worker.
- Every automation setting has a recorded answer. Explicit `manual`: no automatic launch by implementation.
- TDD uses the agreed tests and examples. With subagent TDD, the subagent writes only the failing tests.
- Review reports only, or fixes and re-reviews within the agreed authority and round limit; user acceptance remains separate.
- Default pre-commit review uses the intended working-tree snapshot. If a project selects a different reviewer or endpoint, check its coverage at the agreed checkpoint.
- A requested helper, source or separate session is unavailable: identify the blocked step or agreed handoff.
- An added skill, tool, MCP integration or policy pointer is available to the intended reader, including delegated workers, or reported as a prerequisite. Availability is not permission to act.
- A task needs only an implementation plan: its artifact stays with that task, and the chosen executor can consume it without a new spec or tickets.
- Optional diagrams: selection alone starts nothing; declined offers produce no diagram writes or dispatch. Consent uses a separate worker with readable sources/assets and a permitted output/rendering path; missing capability blocks only the diagram.
- A required action conflicts with project permissions: report it without inventing a substitute or bypass.

For memory or writing changes, also use the verification guidance in their references. Distinguish a static walkthrough from live execution. Obtain approval before launching a client or substantive helper as a probe.

**Done when:** report saved files, changed settings, deployment/discovery results, verification limits and blocked actions. Explain how to rerun `$setup-workflow` in Codex or `/setup-workflow` where supported. Stop after setup.
