---
name: setup-workflow
description: "Configure or revise a project's agent workflow, select its skills and install the approved packages."
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

Use a free conversation in small rounds. Recommend choices and explain consequences. Ask only about missing decisions; accept answers that cover several topics.

### Shared rules

Establish:

- Product purpose, working boundaries and authoritative requirements.
- Artifact locations, owners, formats and tracked, ignored or local visibility. Preserve external sources without duplicate local records.
- Autonomy and human checkpoints; distinguish read-only exploration from implementation delegation and external writes.
- Conversation, artifact and instruction languages. When configuring styles, read [writing routes](references/writing.md).
- Context and lessons: shared directory, reading and update checkpoints, writer and approval scope. Follow the project-artifact contract.

For Git workflows, read [delivery settings](references/delivery.md) only when those settings are missing or changing.

### Skill-specific rules

Use [the catalog](references/catalog.md) to discuss applicable skills, including user-suggested packages. For installation or client/scope changes, read [deployment](references/skills.md).

Read the selected prompts before proposing settings. Establish the sources, output location, project practices and permitted operations each needs. Keep shared paths and permissions in one place; skill sections contain only their specific settings and differences.

For `tdd`, ask: "How do we work with tests here? Which test types and existing examples should guide us? What infrastructure or mocking constraints apply?" Inspect test commands rather than asking the user to transcribe them. Keep the red–green method; do not introduce independent test authorship.

For review, ask which requirements, coding practices and examples guide it. Discuss the procedure freely, including another skill if the user prefers. Agree [review coverage and its checkpoint](references/AGENTS.md#review-coverage); record the procedure as prose, not a package-name flag.

For implementation routes, agree automatic or manual TDD and review, where each runs, and whether review only reports or leads to fixes and another review. Use the setting meanings in [the AGENTS.md reference](references/AGENTS.md#automation-settings). The user decides whether to accept the work.

For `to-plan`, agree the task-linked plan location, naming, visibility, approval and revision rules. Keep plans with the task's other artifacts where permitted, without requiring a spec or tickets. Agree the receiving executor and its input contract: plan plus source task, not a replacement specification or ticket graph. Configure that route in project instructions; leave installed skill prompts unchanged.

For visual design support, offer the optional bundled `excalidraw-diagram` package. If selected or its settings change, read [diagram configuration](references/diagrams.md). Agree one project policy and link applicable skill sections to it; package approval is not consent to generate a diagram.

For tracker-backed planning routes, agree tracker operations, specification/ticket formats and decision-map handling. Use only the selected tracker seed when no adequate project procedure exists:

- [GitHub](references/issue-tracker-github.md)
- [GitLab](references/issue-tracker-gitlab.md)
- [Local Markdown](references/issue-tracker-local.md)

For another tracker, derive the procedure from its agreed sources and access method. Keep readiness vocabulary required by selected skills; setup does not configure incident triage. Read [domain documents](references/domain.md) only when glossary or ADR conventions need configuration.

Check skill dependencies, client capabilities and implementation-to-review handoffs against proposed settings. A required helper may be absent, a comparison may exclude the intended changes, or a mandatory operation may be forbidden. Identify the blocked step rather than silently substituting another procedure. A separate-session choice requires either client support or a user-started handoff; setup does not promise thread creation.

### User additions

Ask: "What other practices, skills, examples or constraints should this project use?"

Record additions in the relevant shared or skill-specific section. Add a section for another selected skill when needed. Give each pointer a reading trigger. Preserve user intent and resolve contradictions before drafting affected rules.

**Done when:** every applicable topic has an agreed answer, an authoritative source, or an explicit gap with its affected action. No unselected workflow is required merely to complete the interview.

## 3. Draft and approve

Read [the AGENTS.md structure](references/AGENTS.md). Draft shared rules and sections for selected skills with project-specific settings. Fill agreed facts, omit inapplicable sections and leave unspecified settings at the skill's defaults. Use the project's effective writing rules.

Keep root instructions short. Link existing practices before proposing supporting files. Store detailed new procedures under the agreed agent-documentation directory only when needed. The setup references guide drafting; they are not the consumer project's runbooks.

Show the proposed configuration edits, loading pointers, visibility changes and compatibility gaps. On a rerun, show what changes and what stays. Present installation as a separate bounded action set. Obtain approval for each requested set; neither authorizes subsequent implementation, publication or global changes.

**Done when:** the owner has approved the affected rules and files, and separately any deployment. Unresolved conflicts block their affected actions, not unrelated setup work.

## 4. Apply the agreed changes

Re-read target files for intervening changes and merge only approved edits. On initial setup, create or reuse root `AGENTS.md`, `CONTEXT.md` and `LESSONS.md` according to the artifact contract. Seed memory from the actual discussion. On reruns, preserve unrelated settings and history.

Apply approved loading and visibility changes. Create no empty future plans, specs, tickets, glossaries or ADRs. Moves and storage migrations require their own agreement.

If installation was approved, follow the deployment reference. Reuse compatible packages, preserve notices and report partial failures. Finalize writing activation pointers only when their targets are readable. Leave reusable package prompts unchanged.

**Done when:** each approved edit and deployment has an observed result or a specific blocker.

## 5. Verify and hand over

Check local pointers, configured artifact paths, client loading where observable, and selected package discovery and prerequisites. Confirm that per-skill settings have one owner and user additions are represented. A project instruction is not an access-control mechanism or proof of model adherence.

Walk through only relevant cases:

- Initial setup versus a targeted rerun; unrelated settings and installations stay intact.
- A home repo coordinates several children: preserve their instruction ownership and verify shared pointers from each intended session or worker.
- No project setting: use the skill's default. Explicit `manual`: no automatic launch by implementation.
- TDD uses the agreed tests and examples without adding a separate test-author procedure.
- Review reports only, or fixes and re-reviews within the agreed authority and cycle limit; user acceptance remains separate.
- The selected comparison covers the intended changes at the review checkpoint; a committed-only diff cannot verify uncommitted work.
- A requested helper, source or separate session is unavailable: identify the blocked step or agreed handoff.
- An extra skill or coding-practice pointer is needed: the intended reader, including a delegated worker, can reach it.
- A task needs only an implementation plan: its artifact stays with that task, and the chosen executor can consume it without a new spec or tickets.
- Optional diagrams: selection alone starts nothing; declined offers produce no diagram writes or dispatch. Consent uses a separate worker with readable sources/assets and a permitted output/rendering path; missing capability blocks only the diagram.
- A required action conflicts with project permissions: report it without inventing a substitute or bypass.

For memory or writing changes, also use the verification guidance in their references. Distinguish a static walkthrough from live execution. Obtain approval before launching a client or substantive helper as a probe.

**Done when:** report saved files, changed settings, deployment/discovery results, verification limits and blocked actions. Explain how to rerun `$setup-workflow` in Codex or `/setup-workflow` where supported. Stop after setup.
