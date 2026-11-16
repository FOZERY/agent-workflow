# Upstream sources and adaptations

[Overview](../README.md) · [Maintenance procedure](MAINTENANCE.md#track-upstream-without-overwriting-local-policy) · [Legal notices](../THIRD_PARTY_NOTICES.md)

This kit adapts upstream skills; it is not a mirror, and the upstream authors do not endorse it. The revisions below show where material came from; they do not promise that later upstream changes are included. Sources and licenses were last inspected on 2026-11-16.

## Baseline ledger

| Key | Repository and immutable revision | Meaning |
| --- | --- | --- |
| M0 | [mattpocock/skills `a496f5513d4a4cf889bc48e189e579f4b0bdf6aa`](https://github.com/mattpocock/skills/tree/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa) | Source baseline for setup; triage and PR procedures were also consulted at this revision |
| M1 | [mattpocock/skills `5863806dd4e15c63174bee4e7515a4256792ecfa`](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) | Imported package baseline for the Matt-derived packages listed below |
| K1 | [KirillSachkov/agent-kit `3b5e37249118aff3d3dfb547977939145524d525`](https://github.com/KirillSachkov/agent-kit/tree/3b5e37249118aff3d3dfb547977939145524d525) | Setup/project-aware adaptation reference and plain-writing import baseline |
| K2 | [KirillSachkov/agent-kit `c66fb95e097380806262888dac95f9c63048aae3`](https://github.com/KirillSachkov/agent-kit/tree/c66fb95e097380806262888dac95f9c63048aae3) | Workflow-guide reference consulted for ask-workflow; not a new baseline for other packages |
| H1 | [humanlayer/skills `bba9d13ab34f0a87f1cc33df4dd196372393ddfc`](https://github.com/humanlayer/skills/tree/bba9d13ab34f0a87f1cc33df4dd196372393ddfc) | Verified show-me/license reference; the exact revision copied by Matt is not stated |

Current upstream branches: [Matt](https://github.com/mattpocock/skills), [Kirill](https://github.com/KirillSachkov/agent-kit), [HumanLayer](https://github.com/humanlayer/skills). Pin a candidate to a commit before comparing and follow the [update procedure](MAINTENANCE.md#track-upstream-without-overwriting-local-policy); a newer HEAD alone is no reason to change this ledger.

## Package source map

| Local package | Original prompt | Baseline |
| --- | --- | --- |
| [setup-workflow](../skills/setup-workflow/SKILL.md) | [Matt setup](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/setup-matt-pocock-skills/SKILL.md), [Kirill setup adaptation](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/skills/engineering/setup-matt-pocock-skills/SKILL.md) | M0, K1 |
| [grilling](../skills/grilling/SKILL.md) | [Matt: productivity/grilling](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md) | M1 |
| [grill-with-docs](../skills/grill-with-docs/SKILL.md) | [Matt: engineering/grill-with-docs](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/grill-with-docs/SKILL.md) | M1 |
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
| [refactor-docs](../skills/refactor-docs/SKILL.md) | Locally authored document-editing procedure; requires the separately attributed human-text package | No imported package baseline |

Matt packages were imported with their supporting files and client metadata. Supporting Markdown moved under local `references/`; setup invocation references changed to `setup-workflow`. Inspect the whole source package, not only its entry prompt, when updating.

Kirill's [engineering adaptations at K1](https://github.com/KirillSachkov/agent-kit/tree/3b5e37249118aff3d3dfb547977939145524d525/skills/engineering) inform project-owned sources, permissions, test policy, working-copy ownership and review scope. They are comparison references, not evidence that every local package was copied wholesale from Kirill. The [source setup directory](https://github.com/KirillSachkov/agent-kit/tree/3b5e37249118aff3d3dfb547977939145524d525/skills/engineering/setup-matt-pocock-skills) is relevant to the five local seeds: domain, GitHub/GitLab/local tracker and triage labels. Local interview guides, memory contract and installation policy extend those seeds.

`human-text/SKILL.md` and `references/ru.md` retain the imported plain-writing source text, including Russian examples, except for the package name and heading. `recap` and `setup-plain-writing` were not imported; our setup owns optional writing activation. The imported `handoff` package was removed from the kit; its presence in another installation is unrelated. `writing-for-agents` was removed and then restored on 2026-11-16, unchanged except that `SKILL-MECHANICS.md` moved under `references/` with its two links updated.

## Nested PR attribution

The removed PR package included visual examples and placement guidance from Dex Horthy / HumanLayer's [show-me](https://github.com/humanlayer/skills/blob/bba9d13ab34f0a87f1cc33df4dd196372393ddfc/plugins/show-me/skills/show-me/SKILL.md), via [Matt's PR credits](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr/CREDITS.md). The exact copied revision is unknown. The root notices retain the attribution and MIT terms.

## Local adaptation record

These local changes must survive an upstream update.

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
- Made all additional skills optional through owner-controlled selection. Setup explains `human-text` and asks whether to install/reuse it and activate a reading pointer at the end of setup, with explicit project/global scope. The pointer loads guidance initially and after context loss or source changes, reusing it otherwise. Existing installations and triggers are preserved; dependency warnings do not authorize silent additions. Declining style and selecting no other packages skips installation.
- Separated selected procedures, actual deployment/discovery and authorized behavior.
- Made reruns begin with configured/missing status and the owner's requested change; the affected scope limits the interview, draft, installation and verification.
- Added optional OpenAI metadata with manual-only invocation policy; it defines no additional agent.
- Shipped the selectable-skill groups and the dependency graph inside the package as `references/catalog.md`, so setup works without this repository's `docs/`. Added a same-name check across project and user-wide scopes for every selected skill and dependency, with per-client precedence, origin detection through installer lock files and an explicit owner choice for each conflict. Recommended user-wide installation on a personal machine and tracked project installation for a team repository.
- Kept `SKILL.md` at package root and supporting Markdown under `references/`. Centralized licenses and provenance here instead of per-skill `LICENSE` and `ORIGIN.md`.

### Other packages and shared contracts

- `grilling`: added an opening step to establish the discussion's intended outcome, scope and relevant expected behavior. `grill-with-docs` uses it while clarifying terminology and decisions under project rules.
- `research`: narrowed the trigger to in-depth, report-producing investigation rather than routine lookups. Retained primary-source research and a Markdown result; added evidence synthesis, explicit uncertainty and project-owned locations, permissions and delegation profiles. Read-only researchers return findings to an authorized writer instead of being required to write. Setup configures ordinary read-only exploration separately, including its approval policy, optional role/model preference and compact return format, without requiring the research skill.
- `wayfinder`: preserved the destination/frontier decision-map method while allowing project-defined map and ticket representations, ownership, acceptance and read-only proposal delivery. The map and tickets can link to an authoritative ADR or other answer instead of duplicating it. Removed mandatory research branches/pushes and automatic tracker mutations; quick exploration is distinct from report-producing research.
- `to-spec` and `to-tickets`: retained synthesis, acceptance criteria and dependency-aware decomposition; removed automatic readiness/publication, prescribed local layout and execution handoff. Analyst-owned requirements and existing task graphs remain authoritative; missing write access yields a proposal rather than duplicate records.
- `tdd` and its references: made invocation user-only and testing scope, fixtures, mocking and infrastructure project-owned. Added independent test authorship by a fresh test-author subagent with a requirements-only brief and an evidence-based red/green exchange, restoring upstream's one-behavior cycle and minimal green step; removed automatic integration-test preference and blanket bans on internal unit-test boundaries.
- `implement` and `implement-spec`: adopted project sources, working-copy ownership, bounded verification and optional TDD. Added required `code-review` and `human-text` dependencies: the shared cycle obtains fresh review, permits deterministic corrections, explains the implemented result and key code locations before remaining findings, and waits for human acceptance. The writing dependency belongs to the parent/coordinator, not standalone review, and does not enable global style activation. Removed automatic commits, draft PRs, tracker closure, resets and worktree cleanup. The task graph remains; parallelism and integration topology are project choices.
- `code-review`: retained separate Standards and Spec axes, added scoped uncommitted-change review, stable base/endpoint, project review skills, evidence-backed correction categories and repeat review carrying human feedback. Missing mandatory coverage blocks the implementation gate even when the available scope yields no findings. The parent launches the reviewer through the client's subagent tool; without subagents, a user-run review session with the parent's brief counts, and the parent stops for the human after three review rounds. Replaced mandatory nested review agents and universal smell rules with project-configured review. Project-aware sources and full-change review were informed by [Kirill Sachkov's engineering adaptations](https://github.com/KirillSachkov/agent-kit/tree/3b5e37249118aff3d3dfb547977939145524d525/skills/engineering); independent test threads and the explicit acceptance cycle are local workflow decisions.
- Setup now interviews for test levels and infrastructure limits, reviewer role/model and supplementary skills, dispatch permission, deterministic correction authority and human acceptance. Model/profile availability and package dependencies are verified separately from live execution.
- `retro`: replaced environment-only recommendations and the required writing-guide skill with an evidence-based discussion and approved updates to `LESSONS.md` and `CONTEXT.md`. Mandatory rules, ADRs and requirements retain their own authority; removed unconditional hook/CI findings and reviewer-only standards enforcement.
- Removed the imported `handoff` package from the distributed kit; session continuity uses project context and source pointers. Restored `writing-for-agents` unchanged: bootstrap installs it with setup, setup follows it to write `AGENTS.md`, `CONTEXT.md` and `LESSONS.md`, `retro` follows it for memory entries, and `refactor-docs` sends agent documents to it.
- Added defaults to `wayfinder`, `to-tickets`, `to-spec`, `code-review`, `implement`, `implement-spec` and `research`. These include the wayfinder claim of the first unblocked, unclaimed ticket and `grilling` as the fallback type; dependency-ordered ticket files and the approval loop in `to-tickets`; confirming the test boundary in `to-spec`; merge-base review and spec discovery through commit references; narrow checks during work and the full set before review; and reuse of an existing research folder.
- Replaced the undefined "instruction owner" with root `AGENTS.md` (or the project's `CLAUDE.md`), removed the undefined "advisor" role, and named OMP as the oh-my-pi coding agent. `grilling` uses the native question tool only when the whole frontier fits its limits; `code-review` run as a subagent returns questions to its caller as blockers.

### PR and workflow guide


`ask-workflow` is an advice-only, user-invoked guide for the current kit, with no package dependency. It reads available prompts before detailed advice and distinguishes discovery, selection and permission. The upstream guide prompts and topic references were not copied into it.
