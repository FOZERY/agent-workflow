# Installation and project setup

[Overview](../README.md) · [Workflow](../FLOW.md) · [Catalog](SKILLS.md)

You do not write `AGENTS.md` by hand. You bring knowledge of the project and make the decisions. The agent reads what it can find, asks about the rest, drafts the rules and proposes the installation separately.

## Install the setup skill

The installer is [`skills@1.9.0`](https://registry.npmjs.org/skills/1.9.0); it needs Node.js 22.20+. Its [pinned command reference](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/commands.md) lists the sources and flags.

From the target project, with a local copy of this kit:

```bash
npx skills@1.9.0 add ~/projects/agent-workflow --skill setup-workflow --agent codex
```

- For Claude Code, use `--agent claude-code`. Without `--agent`, the installer asks.
- `--global` installs for your user. Without it, the skill goes into the project in the current directory.
- `npx skills@1.9.0 add ~/projects/agent-workflow --list` lists the packages without installing them.

The public source `FOZERY/agent-workflow` had no published skills on 2026-11-16. Once it has them, check that it contains the packages you expect. For a repeatable install, use a checkout at a known commit instead of the latest remote version.

### Choose the scope

- **Personal machine:** install the kit user-wide. Every project gets the same version; each project's rules still come from its own `AGENTS.md`.
- **Team repository:** install into the project and commit the skill folders, so everyone runs the same version.

Keep one copy per name. A user-wide copy can shadow a project copy, and duplicate Codex names can be ambiguous. Check selected packages and their actual upstream dependencies through [the same-name check](../skills/setup-workflow/references/skills.md#check-same-name-copies).

### Keep the licenses

Preserve bundled licenses. For packages without one, include the applicable root third-party notice alongside installation or export. See [distribution requirements](../THIRD_PARTY_NOTICES.md#distribution).

### OMP and other clients

Take the agent identifier from the installer's [supported-agent list](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/agents.md); this kit does not claim an `--agent omp` target. For OMP, agree a native installation method and folder, and copy the whole package with the notices. Discovery from `.omp/skills/<name>/SKILL.md` worked in isolated test projects; other profiles and client versions are untested.

### Start setup

Run `/setup-workflow`, or `$setup-workflow` in Codex. Reload skills first if your client needs it. A package's `agents/openai.yaml` is client metadata, not a separate agent.

## Optional home for multiple repositories

A home repository provides navigation and approved shared materials for work across repositories.
[`home-repo-init`](../skills/home-repo-init/SKILL.md) is a standalone, manual setup-stage option. It is not a prerequisite for this workflow.
The [package](../skills/home-repo-init/SKILL.md) and [source ledger](UPSTREAM.md) describe its inspiration from AI Hero's “The Home Repo Pattern.”
Install it by selecting `--skill home-repo-init` in the command above, with the intended client and scope.
Invoke `/home-repo-init`, or `$home-repo-init` in Codex. Installation alone does not start it.

Initialize or revise the home first. Then optionally invoke `setup-workflow` to configure its procedures, permissions and selected packages.
Use `to-plan` for a specific task's implementation plan. Home initialization does not create empty workflow memory files.
Maintaining this kit does not initialize a home or authorize global skill installation.

The skill inventories only authorized, bounded roots and stays read-only until you approve a plan.
It asks missing decisions in dependency order, rather than asking every possible question:

| Decision | What must be clear |
| --- | --- |
| Search and selection | Authorized roots and member repositories; the agent inspects worktrees, submodules and dirty state |
| Home and audience | New or existing location, personal or team use and intended audience; the agent verifies remote visibility where possible |
| Clients and readers | Intended clients and session starts; the agent checks actual loading behavior and worker access |
| Shared material | Ownership, authority, exact copies versus divergent variants, and explicit approval for any copy or migration |
| Paths and artifacts | Portable repository pointers, nested-path tracking boundaries and the location of cross-repository task artifacts |
| Optional operations | Separate approval for cleanup, clones, local branches, commits, remote creation or publication |

The default is pointers and reuse. Child code, history, remotes, trackers and repository-specific rules stay where they are.
Existing documents remain authoritative until an approved migration. Published packages stay installed by default.
Scope and duplicate relationships are separate classifications. A newer timestamp or commit does not establish authority.
Secrets remain unread and unstored. Remote pointers omit embedded credentials.
Provider metadata can establish visibility. A remote URL alone cannot.

Review the source, destination, action, authority, integrity check, readers, branch and recovery method for every proposed change.
Also review the home `AGENTS.md` and client loading pointers.
Home instructions require reading child instructions before work. They do not claim universal precedence over child rules.
A home pointer does not prove that a child-start session or worker can load shared instructions or discover skills.
Verify those readers' actual paths and installation scope before claiming the route is ready.

Repository pointers do not authorize clones, pulls or submodules.
A missing clone needs approval for its source and destination.
Cleanup needs separate approval after the destination and all consumers are verified. Use recoverable removal and preserve dirty changes.
Git commits, remote creation and pushes are not automatic.
Reruns propose only deltas and preserve unrelated content in an existing home.

## What setup asks about

The [setup prompt](../skills/setup-workflow/SKILL.md) asks only about applicable decisions that existing rules do not settle.
It gives each decision with known options its own question. You can describe a different procedure or link to its source.
For example, local commits can be allowed after checks while pushes still need your approval and merges stay with a human.

| Topic | What gets decided |
| --- | --- |
| Project and sources | Purpose, working scope, authoritative requirements, tracker and artifact locations |
| Working agreement | Mandatory company and project rules, autonomy, human checkpoints, delegation, concurrent work and external-write permissions |
| Selected skills and tools | Skill settings, additional tools and MCP integrations, permitted actions, project practices and reading pointers |
| Implementation plans | Task-linked location, naming, visibility, approval, revisions and receiving executor; no mandatory spec or tickets |
| Optional diagrams | Whether to select `excalidraw-diagram`; delegation, task-artifact paths, libraries and rendering permissions |
| Testing | Test types, representative tests, command sources and infrastructure constraints |
| Review | Requirement and standards sources, preferred procedure, comparison-base rule, endpoint, review checkpoint and permitted corrections |
| Git and delivery | Separate permissions for commit, push, opening or updating a PR/MR, merge, deployment and branch cleanup |
| Writing and memory | Languages, writing routes, context and lessons, update authority and visibility |

You can add requirements outside these topics. Setup puts them in the relevant shared or skill-specific section.
It checks selected packages and capabilities without launching a live agent merely to prove availability.

Give Setup links to policies, runbooks, project documentation or skills. If a rule is unwritten, describe what it applies to and what the agent must do.
Setup lists changes to permissions and restrictions in its preview. A targeted rerun preserves unrelated rules and permissions.
If mandatory rules conflict and the applicable authority cannot resolve the conflict, Setup blocks that action without changing unrelated work.
For an extra tool or MCP integration, name it and describe its purpose. Setup records its usage limits or reports it as a prerequisite, without connecting or granting access.

### Automation settings

Setup asks separate questions about the trigger and execution location for each activity.
It asks about the TDD trigger first, then its location, followed by the review trigger and its location.
It asks only the applicable questions that remain unanswered.
TDD and review each have `trigger` and `execution` settings.
`trigger` selects automatic use during implementation or a separate manual invocation.
`execution` selects the current session, a subagent or a separate session.
Review also has `followup`: report findings, or make authorized fixes and re-review.

The [setting definitions](../skills/setup-workflow/references/AGENTS.md#automation-settings) specify their meanings and limits.
The user decides whether to accept the work. Review procedure selection is prose, not a `review.skill` flag.
TDD remains a test–implementation cycle, not a separate bulk test-writing phase.
If a setting is omitted, the skill's default applies. Explicit `manual` is a different choice.
Setup records settings in `AGENTS.md`; it adds no runtime flag parser or thread-creation service.
Setup also [matches review coverage to its checkpoint](../skills/setup-workflow/references/AGENTS.md#review-coverage). A review that compares only commits cannot verify uncommitted implementation changes.

### Task plans without specifications or tickets

Select `to-plan` for an existing task that needs an implementation approach and ordered work.
It saves one Markdown artifact with that task's other records, using the project's location and permissions.
Setup agrees who can approve or revise it and how the chosen executor receives the plan and source task.
The skill's [storage defaults](../skills/to-plan/SKILL.md#1-establish-the-task-and-destination) apply when the project has no convention.

Plan-based execution is a project-configured route, not a new input automatically accepted by every original skill.
`implement-spec` still needs a specification and ticket graph. Planning alone starts no implementation.

### Optional design diagrams

Select bundled `excalidraw-diagram` if diagrams would help your design discussions.
Setup adds one project policy and links relevant skill sections to it. It leaves the reusable upstream prompts unchanged.
The [diagram interview](../skills/setup-workflow/references/diagrams.md) covers relationships, alternatives, interfaces and interaction architecture.
A prototype sketch supports the runnable experiment; it does not replace it.

Package approval is separate from consent to each diagram. The agent offers a diagram when useful, and you can decline.
An explicit diagram request counts as consent. Generation always runs in a separate subagent, keeping drawing details out of the design discussion.
Without that capability, the agent reports the diagram blocker and continues in text; it does not draw inline.

Setup checks worker access, artifact paths, renderer dependencies, browser availability and required network permissions.
The worker saves an editable `.excalidraw` file and PNG preview beside the parent artifact, using configured paths.
It returns paths, visual-check results and caveats. Text remains authoritative for decisions.

The package includes four libraries and a provenance notice. Some upstream material has no stated license; do not assume all files are MIT-licensed.
Approve any installation changes separately. Setup does not silently replace a same-named upstream global installation.

### Writing routes

The three writing packages work independently. Setup can assign them these project roles in `AGENTS.md`; installing setup alone does not require or activate them.

| Output | Skill | When it loads |
| --- | --- | --- |
| Conversation | `human-text` | At the first prompt, before the first reply |
| Artifacts, including docs, ADRs, specs, tickets, context and lessons | `asd-ste100` | Before drafting or editing the artifact |
| Rules, including skills, `AGENTS.md` and procedural references | `writing-for-agents` | Before drafting or editing rules |

The artifact skill contains concise principles and before/after examples. Routine writing needs no standard, dictionary or research retrieval. The sources reference serves package maintenance and explicit provenance or full-conformance requests.
ASD-STE100 is English. Non-English artifacts retain the required language and use an adaptation.
Full conformance needs the official standard and a terminology review; a short sentence or successful install is not proof.
The [writing contract](../skills/setup-workflow/references/writing.md) covers client loading, scope and helper instructions.
Approve package selection and project pointers separately from global activation. The reusable prompts remain unchanged; the project's `AGENTS.md` assigns scope, language and loading triggers.

## What setup creates

A new setup uses this layout by default:

```text
AGENTS.md
.docs/
  CONTEXT.md
  LESSONS.md
```

| File | What belongs there | What does not |
| --- | --- | --- |
| Root `AGENTS.md` | Workflow rules, permissions, roles, approval points, links to mandatory procedures | A copied chat; configuration the agent can read itself |
| `CONTEXT.md` | Recent work by date and time zone, task links, outcomes, open questions, next steps | Proof that the code still matches an old note |
| `LESSONS.md` | Confirmed lessons and preferences by topic, with date, source, scope and status | Guesses or hidden mandatory rules |
| Glossary and ADRs | Domain terms; important decisions with alternatives and trade-offs | Passing preferences or routine detail |
| Specs and tickets | Required behavior and work, in their own source | Copies of analyst-owned Jira or Confluence records |
| Implementation plan | Task source, approach, ordered work packages, dependencies and checks | A duplicate spec, tracker tickets or an execution permission |

Only the memory folder can change; the file names stay fixed and `AGENTS.md` stays at the root. In this kit repository, `docs/` is documentation for people; `.docs/` is the memory folder in your project.

Setup keeps existing documents and client wrappers. A file with an old name is renamed only through an agreed migration. Setup reuses existing runbooks and creates supporting documents only where they help; it does not create empty plans, specs, ADRs or trackers.

The [reference AGENTS.md structure](../skills/setup-workflow/references/AGENTS.md) contains shared rules and named skill sections.
Setup fills applicable sections from agreed facts and adds sections or practice pointers for user additions. It grants no default permissions.

A leading dot does not make files private. Agree whether they are tracked, listed in `.gitignore` or in the local `.git/info/exclude`. Ignore rules do not untrack existing files or remove history. Global client settings and built-in memory are configured separately.

## Approval and installation

You review two plans: changes to the rules and supporting files, and the skill installation. You can approve either one alone. A compatible installed skill is reused; a user-wide upgrade affects other projects and needs its own agreement.

Our `setup-workflow` can install alone. Twelve Matt-derived packages add only the project-instructions paragraph; their original procedures and calls remain.
Check the [catalog](SKILLS.md#dependencies) before calling a route ready. Required missing helpers or conflicting mandatory steps remain explicit blockers.
Some prompts retain the original `/setup-matt-pocock-skills` command. Our setup is not an installed alias.
The kit includes `research`, `domain-modeling`, `prototype` and `codebase-design` for the relevant workflow branches. Setup proposes required missing deployments with the selected callers; it does not silently install them.

Setup installs nothing when no extra package is selected. It creates no remote repositories, issues, labels, PRs or features.
If deployment fails or is declined, only the project route that needs that package remains unavailable.

## Example projects

- **Company project with ready requirements.** Keep source and permission ownership in the project contract. Inspect original implementation and publication steps before claiming compatibility with a read-only tracker.
- **Personal project from an idea.** Select relevant skills, then approve their prerequisites and operations explicitly. Ownership does not grant unlimited automation.
- **Small experiment.** Wayfinder calls `prototype` for prototype tickets and `research` for research tickets. Inspect their artifact, branch and publication requirements against project permissions.

## Rerun and troubleshooting

Run setup again to see the current settings, missing configuration or skills and what is still unverified. Then say what to change; unrelated settings and installations stay as they are.

- **A skill is not offered.** Check, in order: is the source available, is it installed, does the client discover it, is it manual-only or a helper, does a same-named copy in another scope shadow it. A short list in the model's view does not prove the skill is missing.
- **The wrong version of a skill runs.** Look for a same-named copy in the other scope or a skill bundled with the client, such as Claude Code's own `code-review`, and rerun setup's same-name check.
- **The reviewer does not start.** Check the model or profile, the permission to delegate and access to the required skills. Self-review does not replace it.
- **Setup cannot write project instructions.** Agree another allowed local loading method, or hand the proposed changes to the owner. Setup does not create a second source of rules silently.
- **A check or publication is blocked.** The agent stops that operation and reports it. Passing tests or accepted work do not allow push, PR or merge.
- **You need advice, not configuration.** Use `ask-workflow`; it explains the kit without running setup or installing anything.
