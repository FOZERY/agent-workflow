# Upstream sources and adaptations

[Overview](../README.md) · [Maintenance procedure](MAINTENANCE.md#track-upstream-without-overwriting-local-policy) · [Legal notices](../THIRD_PARTY_NOTICES.md)

This kit adapts upstream skills; it is not a mirror, and the upstream authors do not endorse it. The revisions below show where material came from; they do not promise that later upstream changes are included. Sources and licenses were last inspected on 2026-11-16.

## Current package policy

`grill-with-docs` and `writing-for-agents` remain exact full copies of M1 `5863806dd4e15c63174bee4e7515a4256792ecfa`.

Ten packages add only the project-instructions paragraph below to their original `SKILL.md`: `implement-spec`, `research`, `retro`, `tdd`, `to-spec`, `to-tickets`, `wayfinder`, `domain-modeling`, `prototype` and `codebase-design`. Their remaining bytes, supporting files and client metadata match M1.

> Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

`code-review` and `implement` also include that paragraph and have scoped pre-commit review adaptations:

- `code-review` pins a scoped working-tree snapshot before a commit. The two review axes use the same tree. Committed comparisons still use pinned base and head commits. Client metadata now describes both endpoints.
- `implement` passes the source task, review base and owned paths. It uses the snapshot by default and checks that the reviewed content is what it commits. Project rules can still select a different procedure.

The snapshot design was informed by [Kirill's `code-review` at `1d44154`](https://github.com/KirillSachkov/agent-kit/blob/1d4415445e3686b53110fd10a013fae6344e95cb/skills/engineering/code-review/SKILL.md). This is a design reference, not an imported prompt or a new accepted baseline.
TDD and Wayfinder retain their original helper calls. The three restored helpers include all upstream supporting files.
Without project settings, the documented package defaults apply. Setup is not a new prerequisite.
`grilling` and `setup-workflow` have broader local adaptations. Other local packages retain their own contracts.
All fixed skill dependencies are included in the kit. Client installation, capabilities and permissions still require verification.
`triage`, `pr` and `improve-codebase-architecture` remain absent.
Historical records below describe earlier versions; this policy defines the current package sets.

## Baseline ledger

| Key | Repository and immutable revision | Meaning |
| --- | --- | --- |
| M0 | [mattpocock/skills `a496f5513d4a4cf889bc48e189e579f4b0bdf6aa`](https://github.com/mattpocock/skills/tree/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa) | Source baseline for setup; triage and PR procedures were also consulted at this revision |
| M1 | [mattpocock/skills `5863806dd4e15c63174bee4e7515a4256792ecfa`](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) | Imported package baseline for the Matt-derived packages listed below |
| K1 | [KirillSachkov/agent-kit `3b5e37249118aff3d3dfb547977939145524d525`](https://github.com/KirillSachkov/agent-kit/tree/3b5e37249118aff3d3dfb547977939145524d525) | Setup/project-aware adaptation reference and plain-writing import baseline |
| K2 | [KirillSachkov/agent-kit `c66fb95e097380806262888dac95f9c63048aae3`](https://github.com/KirillSachkov/agent-kit/tree/c66fb95e097380806262888dac95f9c63048aae3) | Workflow-guide reference consulted for ask-workflow; not a new baseline for other packages |
| H1 | [humanlayer/skills `bba9d13ab34f0a87f1cc33df4dd196372393ddfc`](https://github.com/humanlayer/skills/tree/bba9d13ab34f0a87f1cc33df4dd196372393ddfc) | Verified show-me/license reference; the exact revision copied by Matt is not stated |
| E1 | [coleam00/excalidraw-diagram-skill `8646fcc9f74f38539c6cdb4c969723336a96ddcd`](https://github.com/coleam00/excalidraw-diagram-skill/tree/8646fcc9f74f38539c6cdb4c969723336a96ddcd) | Imported diagram generation reference and renderer; no declared upstream license |
| E2 | [excalidraw/excalidraw-libraries `297a349eaff859e678f78d4dbc8e68df5fce42e5`](https://github.com/excalidraw/excalidraw-libraries/tree/297a349eaff859e678f78d4dbc8e68df5fce42e5) | Verified source for four owner-supplied component libraries, with bundled MIT notice |

Current upstream branches: [Matt](https://github.com/mattpocock/skills), [Kirill](https://github.com/KirillSachkov/agent-kit), [HumanLayer](https://github.com/humanlayer/skills). Pin a candidate to a commit before comparing and follow the [update procedure](MAINTENANCE.md#track-upstream-without-overwriting-local-policy); a newer HEAD alone is no reason to change this ledger.

## Package source map

| Local package | Original prompt | Baseline |
| --- | --- | --- |
| [setup-workflow](../skills/setup-workflow/SKILL.md) | [Matt setup](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/setup-matt-pocock-skills/SKILL.md), [Kirill setup adaptation](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/skills/engineering/setup-matt-pocock-skills/SKILL.md) | M0, K1 |
| [grilling](../skills/grilling/SKILL.md) | [Matt: productivity/grilling](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md) | M1 |
| [grill-with-docs](../skills/grill-with-docs/SKILL.md) | [Matt: engineering/grill-with-docs](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/grill-with-docs/SKILL.md) | M1 |
| [domain-modeling](../skills/domain-modeling/SKILL.md) | [Matt: engineering/domain-modeling](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md) | M1 |
| [prototype](../skills/prototype/SKILL.md) | [Matt: engineering/prototype](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/prototype/SKILL.md) | M1 |
| [codebase-design](../skills/codebase-design/SKILL.md) | [Matt: engineering/codebase-design](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md) | M1 |
| [research](../skills/research/SKILL.md) | [Matt: engineering/research](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/research/SKILL.md) | M1 |
| [wayfinder](../skills/wayfinder/SKILL.md) | [Matt: engineering/wayfinder](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wayfinder/SKILL.md) | M1 |
| [to-spec](../skills/to-spec/SKILL.md) | [Matt: engineering/to-spec](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-spec/SKILL.md) | M1 |
| [to-tickets](../skills/to-tickets/SKILL.md) | [Matt: engineering/to-tickets](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md) | M1 |
| [implement](../skills/implement/SKILL.md) | [Matt: engineering/implement](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement/SKILL.md) | M1 |
| [implement-spec](../skills/implement-spec/SKILL.md) | [Matt: engineering/implement-spec](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement-spec/SKILL.md) | M1 |
| [tdd](../skills/tdd/SKILL.md) | [Matt: engineering/tdd](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md) | M1 |
| [code-review](../skills/code-review/SKILL.md) | [Matt: engineering/code-review](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md) | M1 |
| [retro](../skills/retro/SKILL.md) | [Matt: engineering/retro](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/retro/SKILL.md) | M1 |
| [writing-for-agents](../skills/writing-for-agents/SKILL.md) | [Matt: productivity/writing-for-agents](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL.md) | M1 |
| [human-text](../skills/human-text/SKILL.md) | [Kirill communication/plain-writing](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/skills/communication/plain-writing/SKILL.md) | K1 |
| [ask-workflow](../skills/ask-workflow/SKILL.md) | Locally authored; [ask-matt](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md) and [Kirill ask](https://github.com/KirillSachkov/agent-kit/blob/c66fb95e097380806262888dac95f9c63048aae3/skills/engineering/ask/SKILL.md) informed its advisory role | M1/K2 references only |
| [cleanup](../skills/cleanup/SKILL.md) | Locally authored artifact-maintenance procedure | No imported package baseline |
| [refactor-docs](../skills/refactor-docs/SKILL.md) | Locally authored, self-contained document-editing procedure | No imported package baseline |
| [to-plan](../skills/to-plan/SKILL.md) | Locally authored task-linked implementation-planning procedure | No imported package baseline |
| [asd-ste100](../skills/asd-ste100/SKILL.md) | Original instructions and software examples, informed by official ASD-STE100 sources | Issue 9, 2025-01-15, consulted; no standard or dictionary bundled |
| [excalidraw-diagram](../skills/excalidraw-diagram/SKILL.md) | Local consent/delegation entrypoint; retained [generation prompt and renderer](https://github.com/coleam00/excalidraw-diagram-skill/tree/8646fcc9f74f38539c6cdb4c969723336a96ddcd) and [credited component libraries](../skills/excalidraw-diagram/references/libraries.md#provenance) | E1, E2; mixed rights, see package notice |
| [home-repo-init](../skills/home-repo-init/SKILL.md) | Original instructions informed by AI Hero's [The Home Repo Pattern](https://www.aihero.dev/the-home-repo-pattern) | Conceptual article reference, updated 2026-11-12; no imported prompt or code |

The fourteen M1-derived packages retain upstream layout and metadata except for the adaptations above. Where the original `/setup-matt-pocock-skills` prompts remain, they were not renamed to `/setup-workflow`.

Kirill's [engineering adaptations at K1](https://github.com/KirillSachkov/agent-kit/tree/3b5e37249118aff3d3dfb547977939145524d525/skills/engineering) inform project-owned sources, permissions, test policy, working-copy ownership and review scope. They are comparison references, not evidence that every package was copied wholesale. The [source setup directory](https://github.com/KirillSachkov/agent-kit/tree/3b5e37249118aff3d3dfb547977939145524d525/skills/engineering/setup-matt-pocock-skills) informed the retained domain and GitHub/GitLab/local tracker seeds. The triage seed and extended interviews were retired during setup simplification.

`human-text` derives from the imported plain-writing package and retains its Russian reference. It remains separately maintained. `writing-for-agents` now exactly matches M1, including its original broad document scope and root-level `SKILL-MECHANICS.md`.

## Nested PR attribution

The removed PR package included visual examples and placement guidance from Dex Horthy / HumanLayer's [show-me](https://github.com/humanlayer/skills/blob/bba9d13ab34f0a87f1cc33df4dd196372393ddfc/plugins/show-me/skills/show-me/SKILL.md), via [Matt's PR credits](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr/CREDITS.md). The exact copied revision is unknown. The root notices retain the attribution and MIT terms.

## Historical local adaptation record

The records below describe earlier local versions. For restored packages, the current package policy above supersedes these adaptations. Local setup and grilling adaptations remain separately maintained.

### Setup: preserved structure

- User-invoked, prompt-driven setup: explore, discuss missing decisions, preview, write and report.
- Tracker selection, conditional triage vocabulary and domain-document conventions.
- Canonical instruction ownership, existing project policy and targeted reconfiguration.

### Adaptations

- Renamed to `setup-workflow`; invoking either upstream setup is not required.
- Expanded the interview to product purpose/scope, artifact ownership and permissions, autonomy, human checkpoints, checks, Git/delivery, conversation continuity and file visibility.
- Added conditional project-triage questions about incident sources, ownership/routing, relevance, overlapping work, evidence, permissions and escalation before label mapping.
- Added conditional PR/MR setup questions covering templates, naming examples, evidence, metadata, delivery targets, gates, hooks and permissions.
- Added a project commit-policy interview covering actor/approval, commit timing relative to checks/review, message convention and references, grouping and hook failures. The resulting policy lives in root instructions or their authoritative project references; no commit skill or automatic Git action is introduced.
- Required project-procedure pointers and compatibility checks for those branches; reused existing runbooks and templates instead of imposing new files.
- Added a fixed contract schema. The agent writes the document; the user supplies knowledge, decisions and approval.
- Preserved the five seed filenames under `references/`, with project-owned sources, read-only workflows, conditional triage/wayfinding and lazy records. Only applicable seeds are used; adequate existing documents remain authoritative.
- Separated configuration edits from execution: no automatic remote initialization, label/issue publication or unapproved installation/settings changes. Skill installation is approved separately for named packages, sources, dependencies, clients, scopes and destinations.
- Preserved ready-made, read-only requirements as a valid entry point without duplicate specs or tickets.
- Treated `CONTEXT.md` by its declared role, not as a legacy glossary. Its lifecycle and sharing require agreement.
- Added per-step completion criteria and explicit limits on verification claims.
- Made every package independently installable. Setup records approved project combinations and reading triggers in root `AGENTS.md`, without requiring companions or rewriting package prompts. Existing installations, current rules and global approval boundaries remain intact.
- Separated selected procedures, actual deployment/discovery and authorized behavior.
- Made reruns begin with configured/missing status and the owner's requested change; the affected scope limits the interview, draft, installation and verification.
- Added optional OpenAI metadata with manual-only invocation policy; it defines no additional agent.
- Shipped selection groups and project-composition guidance inside `references/catalog.md`, so setup works without repository `docs/`. Same-name checks cover selected packages per client and scope. Package `LICENSE` files now permit complete separate distribution; central records retain provenance.
- Kept `SKILL.md` at package root and supporting Markdown under `references/`. Provenance stays centralized; each package now includes the applicable license terms for standalone distribution.

### Other packages and shared contracts

- `grilling`: added an opening step to establish the discussion's intended outcome, scope and relevant expected behavior. `grill-with-docs` uses it while clarifying terminology and decisions under project rules.
- `research`: narrowed the trigger to in-depth, report-producing investigation rather than routine lookups. Retained primary-source research and a Markdown result; added evidence synthesis, explicit uncertainty and project-owned locations, permissions and delegation profiles. Read-only researchers return findings to an authorized writer instead of being required to write. Setup configures ordinary read-only exploration separately, including its approval policy, optional role/model preference and compact return format, without requiring the research skill.
- `wayfinder`: preserved the destination/frontier decision-map method while allowing project-defined map and ticket representations, ownership, acceptance and read-only proposal delivery. The map and tickets can link to an authoritative ADR or other answer instead of duplicating it. Removed mandatory research branches/pushes and automatic tracker mutations; quick exploration is distinct from report-producing research.
- `to-spec` and `to-tickets`: retained synthesis, acceptance criteria and dependency-aware decomposition; removed automatic readiness/publication, prescribed local layout and execution handoff. Analyst-owned requirements and existing task graphs remain authoritative; missing write access yields a proposal rather than duplicate records.
- `tdd` and its references: made invocation user-only and testing scope, fixtures, mocking and infrastructure project-owned. Added independent test authorship by a fresh test-author subagent with a requirements-only brief and an evidence-based red/green exchange, restoring upstream's one-behavior cycle and minimal green step; removed automatic integration-test preference and blanket bans on internal unit-test boundaries.
- `implement` and `implement-spec`: retained project sources, working-copy ownership, bounded checks, optional test-first work, independent review and human acceptance. Each now bundles the complete review brief and cycle instead of requiring a separate review or writing package. Project-selected extra skills remain project requirements. Automatic commits, publication, tracker closure and workspace cleanup remain excluded.
- `code-review`: retained separate Standards and Spec axes, added scoped uncommitted-change review, stable base/endpoint, project review skills, evidence-backed correction categories and repeat review carrying human feedback. Missing mandatory coverage blocks the implementation gate even when the available scope yields no findings. The parent launches the reviewer through the client's subagent tool; without subagents, a user-run review session with the parent's brief counts, and the parent stops for the human after three review rounds. Replaced mandatory nested review agents and universal smell rules with project-configured review. Project-aware sources and full-change review were informed by [Kirill Sachkov's engineering adaptations](https://github.com/KirillSachkov/agent-kit/tree/3b5e37249118aff3d3dfb547977939145524d525/skills/engineering); independent test threads and the explicit acceptance cycle are local workflow decisions.
- Setup now interviews for test levels and infrastructure limits, reviewer role/model and supplementary skills, dispatch permission, deterministic correction authority and human acceptance. Model/profile availability and package dependencies are verified separately from live execution.
- `retro`: replaced environment-only recommendations and the required writing-guide skill with an evidence-based discussion and approved updates to `LESSONS.md` and `CONTEXT.md`. Mandatory rules, ADRs and requirements retain their own authority; removed unconditional hook/CI findings and reviewer-only standards enforcement.
- Removed the imported `handoff` package; continuity uses context and source pointers. Writing packages are standalone. The project can select rule and memory styles through `AGENTS.md`, rather than through bootstrap dependencies.
- Added defaults to `wayfinder`, `to-tickets`, `to-spec`, `code-review`, `implement`, `implement-spec` and `research`. These include the wayfinder claim of the first unblocked, unclaimed ticket and `grilling` as the fallback type; dependency-ordered ticket files and the approval loop in `to-tickets`; confirming the test boundary in `to-spec`; merge-base review and spec discovery through commit references; narrow checks during work and the full set before review; and reuse of an existing research folder.
- Replaced the undefined "instruction owner" with root `AGENTS.md` (or the project's `CLAUDE.md`), removed the undefined "advisor" role, and named OMP as the oh-my-pi coding agent. `grilling` uses the native question tool only when the whole frontier fits its limits; `code-review` run as a subagent returns questions to its caller as blockers.

### PR and workflow guide


`ask-workflow` is an advice-only, user-invoked guide for the current kit, with no package dependency. It reads available prompts before detailed advice and distinguishes discovery, selection and permission. The upstream guide prompts and topic references were not copied into it.

### 2026-11-17: separate writing routes

Added the original `asd-ste100` package after research into official Issue 9 rules, the STEMG FAQ and its June 2026 AI white paper.
The [research record](../skills/asd-ste100/references/sources.md) links the inspected sources and states verification limits.
The package contains concise principles and original before/after examples. It does not contain the standard or its dictionary.
No third-party STE skill was imported, and no existing upstream baseline changed.

Conversation uses `human-text`, loaded before the first reply.
Artifact prose uses `asd-ste100`, including ADRs, reports, specs, tickets, context and lessons.
Reusable rules use `writing-for-agents`. This is an explicit contract change from optional general writing activation and agent-audience-based routing.
Required non-English artifacts retain their language and use an adaptation rather than a claim of English conformance.

The initial compulsory writing bundle was superseded by the standalone-package contract below. The three routes remain a proposed project composition, not intrinsic dependencies.
The setup package includes `references/AGENTS.md` as a structural reference; it does not preselect permissions or create consumer artifacts in this repository.
Implementation review, human acceptance and publication permissions are unchanged.

### 2026-11-17: standalone package contract

Every skill can install alone, including `setup-workflow`.
Removed unconditional cross-skill loads and sibling-package runtime links.
The three writing skills no longer route users into companion packages.
Setup writes approved package roles, paths, languages, loading triggers and additional requirements into the consumer project's `AGENTS.md`.
It does not patch reusable prompts for each project.

The interview-with-docs package now contains its own interview procedure.
Wayfinding contains its evidence-gathering and human-decision procedures.
Each implementation package bundles the same canonical review cycle, including reviewer instructions and the separate-session fallback.
The independent-review, correction, three-round escalation and human-acceptance gates are unchanged.
Each package includes a complete license notice for distribution without repository-root files.
No upstream baseline moved and no new upstream skill was imported.


### 2026-11-17: restore eleven exact Matt packages

Owner-approved cutover from local adaptations to complete M1 package copies. No source revision was advanced.
Local extra references, bundled cycle copies and package license additions were removed with the old folders.
Upstream dependencies, invocation metadata, action defaults and supporting-file locations were restored unchanged.
`grilling`, our setup package and the five local/non-Matt packages were excluded. No deleted helper was reintroduced.
Catalogs and compatibility guidance now distinguish an exact install from a runtime-ready dependency set.
Root legal notices accompany exports where the original package contains no license file.


### 2026-11-17: project-settings adaptation and setup simplification

The owner approved the single project-instructions paragraph for nine M1 packages. No baseline revision moved.
The original procedures, calls, metadata and supporting files remain unchanged beyond that addition.

Setup now uses five steps and generates shared project rules plus named skill sections.
It records TDD/review triggers and execution location, and review followup behavior.
Review procedure selection remains prose; user acceptance is not a flag.
Additional user-selected skills and coding practices receive relevant sections and reading pointers.

Retired the triage interview and role-map seed. Replaced planning and implementation interviews with focused setup questions.
Combined commit and PR/MR interviews into a short delivery reference. Removed stale retro-memory and independent-test-author claims.
Readiness vocabulary remains because `to-spec` and `to-tickets` still use it.
Setup changes consumer instructions, not installed package prompts. Configuration and installation remain separately approved.

### 2026-11-17: remove the research package

Removed `research` from the kit, its selectable catalogs and the generated instruction outline.
Its original source was [Matt's M1 research package](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/research).
Historical adaptation records remain above.

The kit focuses on workflow and its supporting writing skills. `writing-for-agents`, `asd-ste100` and `human-text` remain.
Wayfinder's original research calls remain unchanged and require a compatible external skill. Setup must check that prerequisite before calling the branch usable.
The removed package was moved to a recoverable location. User-wide installations were not changed.

### 2026-11-17: restore research as a workflow dependency

The owner reversed the research removal after confirming wayfinder's explicit calls.
Restored the complete package, including its project-instructions paragraph and original metadata, plus catalog and setup entries.
Other removed packages and user-wide installations remain unchanged.

### 2026-11-17: remove specialist helper requirements from TDD and Wayfinder

Approved the targeted dependency changes listed in the current package policy without advancing M1.
TDD keeps its test cycle and seam confirmation. Wayfinder keeps research, grilling, ticket types and tracker operations.
Prototype tickets keep human participation and decision evidence, using an agreed method rather than a fixed package.
`grill-with-docs` remains unchanged. The owner has not decided whether to restore its `domain-modeling` dependency.

### 2026-11-17: restore workflow helpers and original callers

Restored complete M1 packages for `domain-modeling`, `prototype` and `codebase-design`, each with only the agreed project-instructions paragraph.
Restored the original TDD and Wayfinder helper calls, reversing the preceding dependency adaptation. Their project paragraphs remain.
The kit now includes the fixed helper dependencies of these procedures. Setup can configure each helper in its named project section.
`grill-with-docs` remains unchanged and can use the restored domain helper. Other removed packages and global installations were not restored.

### 2026-11-17: clarify local writing and review configuration

Kept routine `asd-ste100` writing self-contained. Its source reference now has an explicit maintenance, provenance or conformance-review trigger.
Corrected the Redis example to preserve a proposed decision rather than weaken it to an option.
Limited `human-text` questions to missing user decisions or permissions. Already authorized work can continue.
Added project memory to the `refactor-docs` reference trigger.
Corrected `ask-workflow` guidance about pre-commit review. Setup now agrees the comparison-base rule, endpoint and checkpoint, then checks caller/reviewer compatibility.
Matt-derived package prompts remain unchanged. An incompatible review route needs an explicit project procedure or a compatible reviewer; setup does not commit work to bypass the gap.

### 2026-11-17: add lightweight task implementation plans

Added the standalone, manually invoked `to-plan` package with bundled MIT terms and client metadata.
It saves one Markdown plan with the task's artifacts, reuses project storage and permission rules, and needs neither a specification nor tickets.
Setup configures plan storage, approval, revisions and the receiving executor. Advice and catalogs expose the optional route without changing Matt's prompts.
The design uses the concise-plan and checkable-handoff principles compared in [OpenAI's historical create-plan](https://github.com/openai/skills/blob/aac2078f9f293e5335f5efe33148f40d75b56389/skills/.experimental/create-plan/SKILL.md), [HumanLayer's outline documentation](https://docs.humanlayer.com/reference/skills-workflows#structure-outline) and [Superpowers writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md).
These are conceptual references, not imported packages or runtime dependencies. No upstream templates or code were copied, and no upstream baseline advanced.

### 2026-11-18: clarify multi-service plan ownership

Multi-service plans keep one shared artifact with service/repository responsibility boundaries, provider/consumer contracts, shared-schema ownership, integration order and cross-service checks. Executor roles propose a work split without launching agents. A usable handoff verifies access from the participating repositories or worktrees.

### Optional delegated design diagrams

Added `excalidraw-diagram` as an optional design helper, not a workflow phase.
The coordinator offers a relevant diagram and waits for consent; only a separate worker generates and visually checks it.
The worker returns artifact paths, a short check result and unresolved questions. Declined or blocked diagrams do not block the original discussion.

The E1 `SKILL.md` is retained unchanged as `references/generation.md`, and its README as `references/upstream-README.md`.
The six original reference/renderer files retain their bytes and paths. A new short entrypoint owns consent, delegation and project storage.
Four owner-supplied `.excalidrawlib` files byte-match E2. Their credits and MIT notice ship in the package.
E1 has no declared license. Inclusion does not grant redistribution rights; see [the package notice](../skills/excalidraw-diagram/NOTICE.md).

Setup connects selected design skills through the generated project contract; Matt-derived prompts and baselines remain unchanged.
The local `to-plan` now permits an explicitly approved diagram-only subagent while preserving its prohibition on starting implementation.
The upstream global installation is not replaced by this repository change.

### Multi-repository home initialization

Added the standalone, manually invoked `home-repo-init` skill, informed by [The Home Repo Pattern](https://www.aihero.dev/the-home-repo-pattern).
The article's inspected metadata reports an update at `2026-11-12T10:30:12.788Z`. This is a conceptual source, not a copied skill or an imported baseline.
The new prompt and examples are original; no article prompt or third-party implementation is bundled.

The skill inventories approved roots, agrees home membership and shared-material ownership, then previews changes before writing.
Unlike the article's setup prompt, it does not scan the whole home directory by default or select a canonical variant solely by recency.
Installed packages stay installed by default. Child cleanup, cloning, local Git actions and publication require their applicable approval.
Navigation does not establish instruction inheritance or skill discovery in child sessions; verification covers those readers separately.

Home structure is distinct from workflow configuration and task planning. Setup can configure an existing home without absorbing child policies.
No Matt-derived prompt or accepted source baseline changed.
