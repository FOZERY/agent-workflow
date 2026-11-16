---
name: setup-workflow
description: "Configure or revise a project's agent workflow, select its skills and install the approved packages."
argument-hint: "[project context or settings to change]"
disable-model-invocation: true
---

# Setup Workflow

Adapt the engineering workflow to the project: its sources, artifacts, permissions, human checkpoints and delivery rules. The user supplies knowledge and decisions; you write the instructions. Use the same procedure for a new project, an existing repository or a targeted revision.

This is a prompt-driven setup, not a permission mechanism. Work within applicable instructions and technical access controls. Configuration edits and skill installation are separate approved action sets; neither authorizes subsequent implementation or publication.

## Process

### 1. Explore

On initial setup, inspect the current working scope before asking the user to describe discoverable facts. On a rerun, first read the accepted configuration and the installer lock files (`skills-lock.json` in the project, `~/.agents/.skill-lock.json` user-wide) needed for the status overview; defer additional exploration until the owner selects a change. Use the following discovery list only as relevant to that overview or the selected change:

- Existing agent instructions, their includes and ownership; product documentation and links; repository layout; scripts, check configurations and CI.
- Repository identity and remotes, existing artifact conventions and prior workflow configuration. Keep credentials and private remote details out of summaries.
- Available skill packages, declared dependencies, known installations and authorized integrations relevant to this project. Distinguish implemented packages from roadmap entries, installed skills from enabled workflows, and capability from permission. Inspect additional client installation locations only within the agreed access scope.

On initial setup, or a rerun affecting instruction ownership or project memory, read [the core project-artifact contract](references/project-artifacts.md). Resolve existing instruction ownership and each client's loading mechanism. Put the workflow contract in repository-root `AGENTS.md`, preserving existing policies and client wrappers without duplication. For a personal setup in a company repository, agree an allowed local mechanism instead of assuming shared files may change.

Stay within the current scope; ask before exploring additional repositories or connecting new services. Use available, authorized read access. Report unavailable sources without inventing their contents. Treat existing `CONTEXT.md` and `LESSONS.md` files according to their declared roles, not their names alone.

**Done when:** you can show what exists, which rules apply, which instructions own the configuration, and which facts or decisions are missing. Unresolved ownership blocks affected writes, not unrelated discussion.

### 2. Present findings and interview

On initial setup, summarize what you found, then discuss the topics below in order. Use a free conversation, not a questionnaire the user must complete. Ask a small, coherent round, recommend concrete choices, explain their consequences and wait for the answer. Accept answers covering later topics; revisit earlier choices when necessary. Reuse established facts and rules rather than asking the user to repeat them.

On a rerun, first show a status overview: accepted project rules and their sources, core artifact/loading status, enabled workflows and selected skills, known deployments by client/scope, and missing configuration, packages or access verification. Distinguish an unresolved choice from an uninstalled package or unavailable integration. Ask: "What would you like to change or finish configuring?"

Use the answer to establish the affected topics and dependencies for the entire run: interview, draft, installation and verification. Missing or newly available options are information, not a mandate to reconfigure everything. Preserve accepted settings outside this change. If the user wants only the overview, finish without edits or installation. A language-only change does not reopen tracker permissions, reinstall skills or require unrelated scenario checks.

#### A. Project and working scope

Close gaps in product purpose, users, business boundaries and the repositories or environments involved.

Ask what the existing documentation does not answer: "What should I understand about this product and its users? Which repositories and directories are in scope, and where may I make changes? Which product or documentation links matter?"

Capture a short project description and working boundaries. Reuse existing product documentation; propose a separate overview only for missing context. An undeveloped project needs no invented stack or architecture.

#### B. Tasks, requirements and artifact sources

Determine where work comes from, who owns its content and which actions the agent may perform.

Ask: "Do you bring an implementation-ready ticket, or do we develop requirements together? Where are requirements and tasks authoritative? May I read, create, edit, comment on, transition or close them? What should happen when requirements are incomplete?"

Offer GitHub, GitLab, local Markdown or another existing system such as Jira. A remote suggests an option, not a decision. For each needed artifact type, agree its owner, authoritative location, access method and allowed operations: requirements/specs, implementation tickets, decision maps, research, domain vocabulary, ADRs, architecture reports, diagrams, prototypes, conversation context and long-term project lessons. External links are valid locations; local duplicates are not required.

Explain the resulting route: analyst-owned, read-only requirements can bypass `to-spec` and `to-tickets`; an idea can use them when authorized. Identify unavailable or conflicting skills without pretending their prompts already implement the new contract.

#### C. Workflow skills and installation targets

On initial setup, after discussing project purpose and task sources, read [skill selection and installation](references/skills.md). Follow [existing-installation checks and optional writing activation](references/human-text.md) before asking whether or where to install `human-text`. Offer the selectable skills from [the kit catalog](references/catalog.md) as an optional multi-select before conditional workflow branches; any subset or none is valid. Explain omissions and dependency conflicts without silently adding packages.

On a rerun, read these references only when the requested change affects skills, writing activation, clients, scope or deployment. Preserve a suitable existing style installation and effective global trigger. Explain gaps and propose only necessary approved changes; do not silently substitute an upstream package for an unavailable adaptation.

For enabled wayfinding, specification or decomposition routes, read [the planning-procedure interview](references/planning.md). Establish the applicable map/task representation, authorship, experiment boundaries and decision/report gates. Configure only selected routes.

#### D. Project triage, when used

Discuss this only if incident or request triage is part of the project's workflow. Installation alone does not authorize it.

Read [the project triage interview](references/triage.md) for this branch. Establish the existing procedure, its evidence and routing rules, related-work checks, permitted outcomes and human decisions before mapping labels. A label vocabulary alone is not a triage contract.

#### E. Domain documents and visuals

Read existing glossary and ADR conventions. Ask about missing ownership, locations and approval rules. For a new layout, propose one glossary and one ADR location; discuss multiple contexts only when the project actually needs them.

Explain that a glossary holds vocabulary, a spec describes the change, and an ADR records a consequential decision and its trade-offs. Agree where diagrams live, which tools are allowed, where editable sources belong and how documents link to them. Offer local Markdown/Mermaid, draw.io, Excalidraw or Miro as choices, not requirements. External publication needs its own authorization.

Configure future locations without generating empty glossary, ADR, spec or prototype files.

#### F. Working relationship and permissions

Ask: "After receiving a task, should I continue through agreed stages or wait for a separate start? Which plans and decisions need your approval? What should I explain before acting, and what must you inspect yourself?"

Set human checkpoints, permitted delegation, working-copy ownership and integration responsibility. Determine the required language for human-facing work and generated instructions from existing policy; ask if missing. This skill remains in English. Avoid duplicating global preferences already in force.

Configure routine read-only exploration separately from selecting `research`. Show existing defaults and ask about missing choices: "May read-only subagents inspect files, search repositories and gather web/documentation facts without asking each time? Should they handle substantial reading to conserve the main context? Use the harness preset, or a particular available role/model? Which sources and access boundaries apply?" Keep reasoning effort automatic within existing user/project limits unless the owner requests an override.

Capture the agreed exploration policy in root `AGENTS.md` or its workflow reference, even when `research` is not selected. Prefer delegated substantial reading/search when agreed, not a separate agent for every small file. Give helpers bounded questions and request compact findings, source pointers and uncertainty; no file is required for routine exploration. Verify the selected role's actual capabilities, preserve approval requirements and reference native profile settings rather than duplicating them. Deep `research` is a separate report-producing procedure; its reader and writer may be different agents.

If the owner enables session-wide `human-text`, draft only its short session-start reading pointer in the deployment plan, not a copy of the style guide. Defer new activation text until the end of setup, after the package is installed and readable. A skill that requires the package loads it for its own work; that dependency does not authorize a session-wide pointer. Required document structure, technical meaning and approval rules remain authoritative. Declining activation leaves existing personal instructions unchanged.

Discuss code edits, dependency installation, environment changes and external writes separately. For Git and delivery, settle commit, push, PR/MR creation or updates, merge and deployment independently, including target repositories/branches and approval requirements. An authorized commit does not imply an authorized push. Missing authorization is not permission. User preferences cannot relax applicable company or higher-priority restrictions.

#### G. Quality and acceptance

Show discovered standards and checks. Ask: "Which checks are required for which changes? What requires human or independent review? What counts as accepted, and what should I do when a required check is unavailable or fails?"

Record the required evidence, checkpoints and escalation conditions. Reference tool configuration and established commands rather than copying their contents into instructions. Agree any missing conventions. Repeated technical procedures may become project skills; ordinary code rules need not become skills.

For selected `tdd`, `implement`, `implement-spec` or `code-review` routes, read [the testing and review interview](references/implementation.md). Agree test scope and infrastructure limits, independent test authorship when selected, reviewer profile/model and required project skills, automatic correction boundaries and the human-acceptance cycle. Record these as project rules; a lesson or skill installation alone does not authorize them.

#### H. Commit policy and PR/MR procedure

For projects using Git, read [the commit-policy interview](references/commits.md), including when the human makes commits. Agree the checkpoint, actor/approval, message convention and examples, change grouping, check/hook sources and failure behavior. Record this as project policy, not a new skill or permission to commit during setup.

When the agent will prepare or publish PRs/MRs, read [the project PR/MR interview](references/pull-requests.md). Agree the authoritative template, title/body examples, evidence, participants, labels, preparation trigger, source/destination selection and publication method. Commit-message and PR-title conventions are separate. Connect both procedures to the quality/delivery gates and action permissions already discussed, including hooks and draft/ready transitions. Setup configures these actions without performing them.

#### I. Project memory and Git visibility

Explain the core layout: root `AGENTS.md` is fixed at the repository root; `CONTEXT.md` and `LESSONS.md` have fixed filenames and live together in the selected agent-documentation directory, default `.docs/`. Ask which directory to use, not what to name these files. Follow the artifact contract's role boundaries, reading triggers, preservation and migration rules; these artifacts do not depend on optional skill selection.

Ask which existing records must be preserved, who updates context and lessons, at which checkpoints, what has standing write permission and what needs approval, and how old material is condensed or superseded. Confirm the contract's loading path, relevant ADR pointers and concurrent-writer coordination. Ask whether built-in automatic memory is used; its answer does not replace the three artifact roles or authorize global setting changes.

When `retro` is selected, explain that it discusses evidence and writes confirmed reusable outcomes to `LESSONS.md`, with a brief recent summary and open questions in `CONTEXT.md`. Agree its writer and approval scope using the same memory policy. Mandatory rule changes still need approval at their authoritative source; installing retro grants no broader write access.

For every proposed local artifact or artifact directory, ask whether it is shared and tracked, ignored project-wide through `.gitignore`, or excluded only locally through `.git/info/exclude`. Explain that ignore rules do not untrack files or remove history. A sensitive tracked file requires a separate remediation decision, not an automatic Git operation.

Agree these choices; do not infer them from the project's personal or company status. Configuring memory behavior here does not authorize changing global client settings.

**Done when:** on initial setup every relevant topic, or on a rerun every affected topic, has an agreed answer, an authoritative existing rule or an explicit not-applicable outcome. Identify remaining gaps and the actions blocked by them; continue only with unaffected setup work.

### 3. Invite additions

On initial setup, ask: "What important project knowledge, constraints or expectations have we not discussed? You can describe them freely." On a rerun, invite additions or corrections concerning the requested change without reopening unrelated topics.

Fit additions into the contract, preserve their meaning, and resolve contradictions with the owner before drafting affected rules. The user does not need to write Markdown or know skill internals.

**Done when:** the user has had an explicit opportunity to add or correct information, and conflicting requirements are resolved or marked as blockers for the affected actions.

### 4. Draft the project contract

Write concise, executable instructions from the discussion, following the installed `writing-for-agents` skill. Keep each rule in one authoritative place. On initial setup, cover every required topic below inline or by an explicit pointer; an existing project's headings need not match this table. On a rerun, draft only the agreed changes and dependent updates, preserving other content. Report pre-existing gaps outside that scope without forcing a full migration.

| Section for a new contract | Required content |
| --- | --- |
| Project | Brief purpose, product boundaries and pointers to the detailed description |
| Working scope | Repositories, directories, environments and permitted change boundaries |
| Sources and artifacts | Requirement/task authority; needed artifact locations, owners, access rights and Git visibility |
| Working process | Entry points, enabled workflows and required skills/dependencies, deployment source/client/scope pointers, project triage pointer where used, autonomy, human checkpoints, read-only exploration permissions/profile and return format, other delegation and language rules |
| Quality and acceptance | Testing levels, coverage priorities and infrastructure limits; standards/check sources; reviewer profile/model and required review skills, dispatch permission, correction authority, human acceptance and escalation |
| Git and delivery | Commit checkpoint, actor/approval, message-convention source, grouping and check/hook sources; PR/MR procedure and format/metadata pointer where used; separate targets and permissions for commit, push, PR/MR, merge and deployment |
| Continuity and lessons | Selected agent-documentation directory with fixed `CONTEXT.md` and `LESSONS.md` filenames; concrete reading/updating triggers, writer, approval, retention and any approved migration |

When a needed contract has no adequate existing source, read the corresponding seed below and adapt it to the interview decisions. These are starting points, not extra skills or permission grants. Proposed new paths use the default `.docs/` namespace; substitute the selected directory while retaining the fixed memory filenames. Preserve established external or other project-document sources.

| Needed contract | Seed to read | Default new document, only if agreed |
| --- | --- | --- |
| Core workflow contract, context and lessons | [project-artifacts.md](references/project-artifacts.md) | Root `AGENTS.md`, `.docs/CONTEXT.md`, `.docs/LESSONS.md`, with client integration only where needed |
| Domain/glossary and ADR consumption | [domain.md](references/domain.md) | `.docs/agents/domain.md` |
| GitHub tracker operations | [issue-tracker-github.md](references/issue-tracker-github.md) | `.docs/agents/issue-tracker.md` |
| GitLab tracker operations | [issue-tracker-gitlab.md](references/issue-tracker-gitlab.md) | `.docs/agents/issue-tracker.md` |
| Local Markdown tracker operations | [issue-tracker-local.md](references/issue-tracker-local.md) | `.docs/agents/issue-tracker.md` |
| Triage role mapping, when used | [triage-labels.md](references/triage-labels.md) | `.docs/agents/triage-labels.md` |

Write only the selected, substantive contracts at the accepted project locations. Materialize concrete sources, paths, targets and allowed operations; discard irrelevant alternatives and seed proposals. Never copy all tracker variants into the project or turn reference commands into authorized actions. Existing runbooks remain authoritative. For Jira, Confluence or another system, write the contract from the agreed sources/access method rather than pretending a GitHub/GitLab seed applies. Reuse its captured operation requirements without inventing API syntax.


Use the following output rules:

- Keep root `AGENTS.md` short. Use the selected agent-documentation directory for proposed new supporting documents; the default examples are `.docs/project.md` for missing product context and `.docs/agents/workflow.md` for extensive workflow detail. A small project may need neither. Preserve established tracker/domain sources and pointers unless their migration is approved. Agree Git visibility separately: a leading dot does not imply an ignore rule.
- Write pointers with triggers: what to read before which action. Keep universally needed guardrails visible; a permission restriction must not depend on an optional skill being invoked.
- Record owner-selected procedures, optional writing activation and explicitly approved dependencies separately from deployment status and permissions. No top-level skill is mandatory; selected callers require their approved dependencies. Reference installer receipts or lock files for actual package versions instead of duplicating them. Missing dependencies or incompatible selected skills block their dependent routes, not unrelated work. A globally discoverable skill does not enable a disabled workflow.
- For applicable Git workflows, keep the commit checkpoint and permission limits visible; record the concise message/grouping rule inline or require reading its existing project source before preparing a message or committing. For enabled triage and PR/MR workflows, require reading the project procedure before the respective action. Point to agreed project sources, not these setup interview guides. Reuse existing runbooks/templates, add supporting documents only when useful, and surface incompatible skill prompts.
- For enabled tracker workflows, use the selected seed to capture required operations and dependency/claim conventions, retaining only supported, authorized methods. A required write that is forbidden stays human-owned or blocks that step. Domain rules use the selected project sources; missing optional records do not require empty files.
- Apply user additions in the relevant section or a focused extension. Use the agreed document language. Preserve unrelated instructions and client wrappers. A new local-only contract needs an agreed loading path; a filename alone does not establish automatic discovery.

An unknown permission stays unauthorized. Describe a genuine remaining blocker and the affected action instead of inserting a blank template or making the user finish the document.

**Done when:** every required topic for initial setup, or affected topic for a rerun, is covered; each new or changed pointer has a reading trigger, each rule has one owner, and every proposed file has a purpose and agreed visibility. Account for root `AGENTS.md` and the two fixed-name memory files in the selected directory, including legacy-source preservation, approved migration or explicit blockers. The draft is written by you, not delegated back to the user.

### 5. Preview and obtain approval

Show two bounded action sets where applicable: proposed project contract/supporting/ignore edits, and the deployment plan. Include style installation and pointer text only when selected, with project/global scope, clients and affected profiles explicit. Project configuration approval alone does not authorize user-wide activation. Explain routes, checkpoints and limitations; on a rerun show changes and preserved settings.

Obtain explicit agreement to each requested action set; one reply can approve both. Configuration approval alone does not authorize installation. If the user declines installation, retain only approved configuration and explain missing deployments and affected routes. If they change a choice, revise the affected draft or install plan before approval. If they cancel setup, leave it unchanged. Discussion alone does not activate proposed rules.

**Done when:** the owner has approved the specific configuration edits and, separately, any planned skill installation and its effects. Unchanged or unrequested action sets need no approval prompt. This does not authorize creating issues, labels, remotes or boards, publishing data or changing tools/settings outside the approved install plan.

### 6. Write the agreed configuration

Recheck the files you will modify for intervening changes, then apply only the approved edits. Merge with the current contents instead of overwriting another writer's work. Preserve the file that owns the project instructions, existing navigation and unrelated rules; create neither a competing authority file nor duplicate configuration blocks.

On initial setup, create or reuse the three core artifacts and their loading pointer as defined by the artifact contract, initializing memory from the actual setup discussion. On reruns, update only agreed affected artifacts and preserve other records. Create additional supporting documents only when approved and substantive. Leave future specs, tasks, glossary entries and ADRs to their actual work. Apply only approved ignore edits. File moves, deletions, untracking and storage migrations need separate agreement.

**Done when:** the agreed configuration edits are saved without unapproved changes, or this stage required no edits. Desired skills are not reported as installed. If a write fails, report exactly what was and was not saved; do not claim an atomic or complete setup.

### 7. Install the approved skills, when requested

If package deployment or optional writing activation was approved, follow [skill selection and installation](references/skills.md) after saving project configuration. Only when style activation was selected, also follow [writing activation](references/human-text.md): install or verify `human-text`, then add its approved project/global pointer at the end of setup. Perform only approved changes and preserve working installations and unrelated instructions. A pointer-only gap needs no reinstall. If changes were declined or unnecessary, skip them and report actual status.

**Done when:** each requested deployment has an observed result or precise blocker, including its dependencies and client discovery status. Report partial success accurately. Installation neither invokes the installed workflows nor grants them permissions.

### 8. Verify and hand over

Check the saved files against the approved draft, resolve local pointers and confirm the chosen loading path where the client exposes it. Use only authorized, non-mutating access checks for external sources; otherwise label access unverified. Check ignore behavior where applicable without staging, committing or changing tracked state.

On initial setup, walk through representative cases against the contract: a small fix, a ready-made spec, a larger idea, a failed required check and a forbidden publication. On a rerun, check only cases affected by the agreed change and its dependencies. Explain the permitted route, human checkpoint or stop for each checked case. Reasoning through cases is not a live execution test of other skills or access-control enforcement.

When triage is enabled and relevant to this setup change, also consider an unreproduced incident with an in-progress fix and overlapping work in another team: neither proves resolution nor permits a duplicate implementation. When PR/MR workflow settings change, consider content-only handoff with publication forbidden, a failed pre-push hook, an ambiguous base branch and an existing draft with pending CI. Check that the procedure resolves targets, gates and allowed actions without bypassing checks or creating duplicate requests.

When testing or implementation review settings change, walk through the affected cases in [the testing and review interview](references/implementation.md), including optional TDD, unavailable reviewers and feedback that requires a new review. Verify that required packages are discoverable by the reviewer as well as the parent; do not launch a live review merely to test configuration without approval.

When artifact roles, memory policy or loading change, walk through resuming a session, remembering a confirmed preference, proposing a mandatory rule and encountering a conflicting ADR. Verify the destination, approval and reading trigger for each. Check that root `AGENTS.md` points to `CONTEXT.md` and `LESSONS.md` in the selected directory, not unconditionally to `.docs/`. Check a non-default directory too; both filenames stay fixed. Confirm client wrappers reach the root contract without duplicating it, and report loading as unverified where it cannot be observed.

When writing activation changes, check declined integration, missing-package and pointer-only cases, an existing working setup, a shadowing profile/override and any requested helper coverage. Confirm initial loading and reload after context loss or source changes, rather than a read before every message. Verify each targeted client separately and distinguish saved pointers/discovery from observed style adherence; do not launch live clients or helpers without approval for that probe.

**Done when:** you can identify the saved instruction entrypoint and workflow contract, context and lessons status, support documents, selected skills and their deployment/discovery results, verified checks, unverified capabilities and blocked actions. On a rerun, report the changes and preserved settings. Tell the user how to start permitted work and how to invoke setup again in their selected client: `$setup-workflow` in Codex, or `/setup-workflow` where slash invocation is supported. A repeat invocation shows the current setup and allows revising it. Stop after setup; do not begin a feature or deliver changes automatically.

