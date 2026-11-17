# agent-workflow

Workflow skills for coding agents, based on [Matt Pocock's skills](https://github.com/mattpocock/skills), with project setup and writing tools.
Twelve Matt packages add only a project-instructions paragraph; `grill-with-docs` and `writing-for-agents` remain exact copies.
The kit includes their fixed helper dependencies. These are prompts, not permission enforcement; check client installations and project permissions before execution.

## How it works

1. Install the packages you need and check their prerequisites.
2. Use `grilling` directly for an interview, or our `setup-workflow` to configure project rules in `AGENTS.md`.
3. Use configured project settings where specified and the skill's defaults elsewhere. Check prerequisites and required actions before running it.

Setup records shared rules and named skill sections in `AGENTS.md`. TDD and review can be automatic or manual.
Review can report findings or lead to authorized fixes and another review. The user decides whether to accept the work.

## Install

You need Node.js 22.20+ and a local copy of this repository. Install either writing skill on its own:

```bash
npx skills@1.9.0 add ~/projects/agent-workflow --skill human-text --agent codex
npx skills@1.9.0 add ~/projects/agent-workflow --skill asd-ste100 --agent codex
```

The installer can select any catalog package, including `setup-workflow`. Some original skills need additional packages at execution time.
Use `--agent claude-code` for Claude Code. Add `--global` only for an intended user-wide installation.

To configure the project, install and run `/setup-workflow` (`$setup-workflow` in Codex). It:

1. Reads existing instructions, documentation, scripts and CI.
2. Discusses missing decisions: test practices, automation, permissions, artifact locations and any additional skills or coding guidance.
3. Shows the draft rules and, separately, the list of skills to install.
4. After approval, writes the project rules and installs only the approved packages.

The result:

```text
AGENTS.md          project rules for the agent
.docs/CONTEXT.md   recent work and open questions
.docs/LESSONS.md   confirmed lessons
```

You can choose another folder instead of `.docs/`; the file names stay fixed. Jira, Confluence and other existing sources stay the source of truth. Run setup again to see the current settings and change some of them; the rest stays as it was.

The project can assign conversation to `human-text`, artifacts to `asd-ste100` and reusable rules to `writing-for-agents`.
Setup records approved triggers and additional requirements in `AGENTS.md`; it does not modify the reusable skill prompts.

Preserve bundled licenses. For packages without one, copy the applicable [third-party notice](THIRD_PARTY_NOTICES.md#distribution) alongside installation or export.
Scope choice, OMP and setup details are in [SETUP.md](docs/SETUP.md).

## Which skill to use

[The skill catalog](docs/SKILLS.md) lists every skill and what it produces. If you are unsure, install `ask-workflow` and ask it:

```text
/ask-workflow I have an approved task from Jira. What should I use next?
```

It recommends a skill and stops; it does not start the work.

## Documentation

| Read | For |
| --- | --- |
| [Workflow](FLOW.md) | How the steps connect: planning, tests, review, acceptance, delivery |
| [Skill catalog](docs/SKILLS.md) | Every skill, its result, how it is invoked and what it depends on |
| [Installation and setup](docs/SETUP.md) | Install scope, what setup asks, the files it creates, troubleshooting |
| [Maintaining the kit](docs/MAINTENANCE.md) | Changing skills and checking the change |
| [Upstream sources](docs/UPSTREAM.md) | Original skills, pinned revisions and what was changed locally |
| [Repository instructions](AGENTS.md) | Rules for agents that maintain this repository |

## Status and license

Package metadata and discovery were checked in isolated test projects. A full run from setup to PR has not been tested, and clients may behave differently. The repository installs no hooks, background updates or services.

Original contributions are [MIT-licensed](LICENSE). Third-party material keeps its [copyright notices and MIT terms](THIRD_PARTY_NOTICES.md). Read [UPSTREAM.md](docs/UPSTREAM.md) before redistributing or updating the adapted skills.
