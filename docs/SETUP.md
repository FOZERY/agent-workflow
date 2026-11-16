# Installation and project setup

[Overview](../README.md) · [Workflow](../FLOW.md) · [Catalog](SKILLS.md)

You do not write `AGENTS.md` by hand. You bring knowledge of the project and make the decisions. The agent reads what it can find, asks about the rest, drafts the rules and proposes the installation separately.

## Install the setup skill

The installer is [`skills@1.9.0`](https://registry.npmjs.org/skills/1.9.0); it needs Node.js 22.20+. Its [pinned command reference](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/commands.md) lists the sources and flags.

From the target project, with a local copy of this kit:

```bash
npx skills@1.9.0 add ~/projects/agent-workflow --skill setup-agents-workflow --skill writing-for-agents --agent codex
```

- For Claude Code, use `--agent claude-code`. Without `--agent`, the installer asks.
- `--global` installs for your user. Without it, the skill goes into the project in the current directory.
- `npx skills@1.9.0 add ~/projects/agent-workflow --list` lists the packages without installing them.

The public source `FOZERY/agent-workflow` had no published skills on 2026-11-16. Once it has them, check that it contains the packages you expect. For a repeatable install, use a checkout at a known commit instead of the latest remote version.

### Choose the scope

- **Personal machine:** install the kit user-wide. Every project gets the same version; each project's rules still come from its own `AGENTS.md`.
- **Team repository:** install into the project and commit the skill folders, so everyone runs the same version.

Keep one copy per skill name. In Claude Code a user-wide skill wins over a project skill with the same name; in Codex two copies make `$name` ambiguous. For example, an upstream `code-review` or `grilling` installed user-wide replaces this kit's version, and `implement` stops at review. Setup checks both scopes for every selected skill and asks how to resolve each conflict; see [the same-name check](../skills/setup-agents-workflow/references/skills.md#check-same-name-copies).

### Keep the licenses

The installer may copy only the skill folders. Keep the kit's `LICENSE` and `THIRD_PARTY_NOTICES.md` next to the installed copies, starting with the setup skill itself; the installer's receipt shows where the skills went. See [distribution requirements](../THIRD_PARTY_NOTICES.md#distribution).

### OMP and other clients

Take the agent identifier from the installer's [supported-agent list](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/agents.md); this kit does not claim an `--agent omp` target. For OMP, agree a native installation method and folder, and copy the whole package with the notices. Discovery from `.omp/skills/<name>/SKILL.md` worked in isolated test projects; other profiles and client versions are untested.

### Start setup

Run `/setup-agents-workflow`, or `$setup-agents-workflow` in Codex. Reload skills first if your client needs it. A package's `agents/openai.yaml` is client metadata, not a separate agent.

## What setup asks about

The [setup prompt](../skills/setup-agents-workflow/SKILL.md) defines the interview. The agent asks only about the topics that apply:

| Topic | What gets decided |
| --- | --- |
| Product and scope | What the product does; repositories, folders and environments; links to existing documentation |
| Tasks and requirements | Where tasks come from; who owns specs; read, create, edit, comment and status rights for each source |
| Skills and installation | Which skills, their dependencies, existing copies, clients and project or user-wide scope |
| Triage, if selected | Incident evidence, releases, routing, related work, duplicates and when to escalate |
| Domain and design | Who owns the glossary and ADRs, accepted decisions, diagram formats, board access and publication rights |
| Collaboration | Where a human checks the work; read-only exploration versus delegated work; implementation roles |
| Testing and review | Test levels, fixtures, coverage priorities, infrastructure limits, reviewer model, extra review skills, which fixes the agent may make itself |
| Git and delivery | When and who commits, message format, hooks, push targets, PR/MR templates and metadata, separate publish and merge rights |
| Memory and visibility | Who writes context and lessons, retention, paths, whether files are tracked, ignored or local |

The agent reads commands and configuration itself instead of asking you to list them. Sources it cannot reach and missing permissions are reported as gaps. Choosing a reviewer model does not make it available: setup checks that the agent can actually launch it and records it as blocked otherwise.

### Plain writing

Setup looks for a compatible `plain-writing` user-wide, then in the project, and asks where to install it if there is none. Installing it and enabling it for every session are separate decisions; the session pointer is added only once the package is readable. `implement`, `implement-spec` and `refactor-docs` use it for their own text without enabling it for the session. If you decline, your personal instructions stay as they are.

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

A leading dot does not make files private. Agree whether they are tracked, listed in `.gitignore` or in the local `.git/info/exclude`. Ignore rules do not untrack existing files or remove history. Global client settings and built-in memory are configured separately.

## Approval and installation

You review two plans: changes to the rules and supporting files, and the skill installation. You can approve either one alone. A compatible installed skill is reused; a user-wide upgrade affects other projects and needs its own agreement.

All top-level skills are optional. Required dependencies of a selected skill are installed or verified first ([list](SKILLS.md#dependencies)): `implement` and `implement-spec` need `code-review` and `plain-writing`, `refactor-docs` needs `plain-writing`, standalone `code-review` needs neither. `tdd` stays optional and runs only on your request.

Setup does not create remote repositories, issues, labels, PRs or features. With nothing selected, nothing is installed. A failed dependency blocks only the skill that needs it.

## Example projects

- **Company project with ready requirements.** Jira and Confluence stay the source; set read-only access if writes are forbidden. Skip `to-spec` and `to-tickets` and select `implement`. Record who accepts the work and the separate commit, push and PR permissions. `triage` can compare active work without changing statuses.
- **Personal project from an idea.** Use `grilling` or `wayfinder` where something is unclear, then `to-spec` and `to-tickets` if useful. Set the reviewer, test scope and publication permissions explicitly: owning the project does not mean unlimited automation.
- **Small experiment.** Edit as usual or use a `wayfinder` prototype ticket; the implementation skills are not needed. If you do select `implement` or `implement-spec`, their review and acceptance gates still apply.

## Rerun and troubleshooting

Run setup again to see the current settings, missing configuration or skills and what is still unverified. Then say what to change; unrelated settings and installations stay as they are.

- **A skill is not offered.** Check, in order: is the source available, is it installed, does the client discover it, is it manual-only or a helper, does a same-named copy in another scope shadow it. A short list in the model's view does not prove the skill is missing.
- **The wrong version of a skill runs.** Look for a same-named copy in the other scope or a skill bundled with the client, such as Claude Code's own `code-review`, and rerun setup's same-name check.
- **The reviewer does not start.** Check the model or profile, the permission to delegate and access to the required skills. Self-review does not replace it.
- **Setup cannot write project instructions.** Agree another allowed local loading method, or hand the proposed changes to the owner. Setup does not create a second source of rules silently.
- **A check or publication is blocked.** The agent stops that operation and reports it. Passing tests or accepted work do not allow push, PR or merge.
- **You need advice, not configuration.** Use `ask-workflow`; it explains the kit without running setup or installing anything.
