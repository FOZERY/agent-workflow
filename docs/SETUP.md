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

## What setup asks about

The [setup prompt](../skills/setup-workflow/SKILL.md) guides a free conversation, not a fixed questionnaire.
The agent reads existing rules and examples, then asks about missing decisions.

| Topic | What gets decided |
| --- | --- |
| Project and sources | Purpose, working scope, authoritative requirements, tracker and artifact locations |
| Working agreement | Autonomy, human checkpoints, delegation, concurrent work and external-write permissions |
| Selected skills | Project-specific settings, additional skills, coding practices and reading pointers |
| Testing | Test types, representative tests, command sources and infrastructure constraints |
| Review | Requirement and standards sources, preferred procedure, scope and permitted corrections |
| Git and delivery | Commit checkpoints and convention; separate push, PR/MR, merge and deployment permissions |
| Writing and memory | Languages, writing routes, context and lessons, update authority and visibility |

You can add requirements outside these topics. Setup puts them in the relevant shared or skill-specific section.
It checks selected packages and capabilities without launching a live agent merely to prove availability.

### Automation settings

TDD and review each have `trigger` and `execution` settings.
`trigger` selects automatic use during implementation or a separate manual invocation.
`execution` selects the current session, a subagent or a separate session.
Review also has `followup`: report findings, or make authorized fixes and re-review.

The [setting definitions](../skills/setup-workflow/references/AGENTS.md#automation-settings) specify their meanings and limits.
The user decides whether to accept the work. Review procedure selection is prose, not a `review.skill` flag.
TDD remains a test–implementation cycle, not a separate bulk test-writing phase.
If a setting is omitted, the skill's default applies. Explicit `manual` is a different choice.
Setup records settings in `AGENTS.md`; it adds no runtime flag parser or thread-creation service.

### Writing routes

The three writing packages work independently. Setup can assign them these project roles in `AGENTS.md`; installing setup alone does not require or activate them.

| Output | Skill | When it loads |
| --- | --- | --- |
| Conversation | `human-text` | At the first prompt, before the first reply |
| Artifacts, including docs, ADRs, specs, tickets, context and lessons | `asd-ste100` | Before drafting or editing the artifact |
| Rules, including skills, `AGENTS.md` and procedural references | `writing-for-agents` | Before drafting or editing rules |

The artifact skill contains concise principles and before/after examples. It does not bundle the standard or its dictionary.
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

Only the memory folder can change; the file names stay fixed and `AGENTS.md` stays at the root. In this kit repository, `docs/` is documentation for people; `.docs/` is the memory folder in your project.

Setup keeps existing documents and client wrappers. A file with an old name is renamed only through an agreed migration. Setup reuses existing runbooks and creates supporting documents only where they help; it does not create empty specs, ADRs or trackers.

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
