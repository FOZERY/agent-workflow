# Skill catalog and project composition

Read this file when you select skills or configure their project settings. Before you call a route usable, check the real skill calls and the [installation status](skills.md#check-same-name-copies).

## Selectable skills

Discuss only the relevant groups. Use the client's choice tool when it helps. Every skill is optional. Add the skills that the user suggests, and check their real source and procedure.

| Group | Skills |
| --- | --- |
| Setup and guidance | `home-repo-init`, `setup-workflow`, `ask-workflow` |
| Task exploration | `grilling`, `grill-with-docs`, `domain-modeling`, `research`, `prototype`, `wayfinder`, `to-plan`, `to-spec`, `to-tickets` |
| Optional visual support | `excalidraw-diagram` |
| Implementation | `implement`, `implement-with-swarm`, `tdd`, `codebase-design`, `simplify`, `code-review` |
| Retrospective and maintenance | `retro`, `cleanup`, `refactor-docs` |

- A group is not a dependency.
- Create a section in `AGENTS.md` for every selected skill.
- Ask about tools and MCP integrations separately from the skills. Record their approved purpose and prerequisites in `AGENTS.md`, not as kit dependencies.
- `to-plan` saves one implementation plan with its task. It needs no spec, no tickets and no other skill. For plan-based work, agree an executor that takes the plan and its source task.
- `implement-with-swarm` uses the existing task sources. Make `implement` available to each worker. Configure the worker mode and the integration rules.
- `home-repo-init` creates or revises a multi-repository home: navigation, approved shared material and client entry points. The user runs it manually and separately. `setup-workflow` can configure the home's procedures later. Neither skill calls the other.

## Writing skills

`human-text`, `asd-ste100` and `writing-for-agents` are separate writing skills. [Writing routes](writing.md) proposes them for conversation, artifacts and reusable rules in the project's `AGENTS.md`. `setup-workflow` needs `asd-ste100` and `writing-for-agents` to write `AGENTS.md`. `human-text` stays optional.

## Diagrams

`excalidraw-diagram` is an optional bundled skill. The original skills do not need it. Use [diagram configuration](diagrams.md) for relationships and alternatives, interfaces, interaction architecture or a prototype sketch. Skill sections link to one diagram policy. Selection of the skill is not consent to draw, and setup does not have to install it.

## Dependencies

These skills call the listed skills. Check that the client and its worker sessions have them.

| Caller | Calls |
| --- | --- |
| `grill-with-docs` | `grilling` and `domain-modeling` |
| `wayfinder` | `grilling` and `domain-modeling` for discussion; `research` and `prototype` for their ticket types; skills named in the map Notes |
| `tdd` | `codebase-design`, only when the interface or seam is in question |
| `implement` | `tdd` where it applies, `simplify` when its trigger is `auto`, and `code-review` |
| `implement-with-swarm` | `implement` in each worker: `/implement` in a session worker, the `SKILL.md` path in a subagent worker |
| `retro` | `writing-for-agents` |

1. The other skills have no fixed calls. Project rules or map Notes can add prerequisites.
2. `domain-modeling`, `prototype` and `codebase-design` call no other skills. Each one also works alone.
3. Restore no removed helper, download no substitute and patch no caller as a hidden setup step.
4. Before you agree a route, read its real requirements for tracker publication, commits, worktrees and branch pushes.
5. Project rules own permissions and writing choices. Installation grants neither.
6. If an installed or source version of a skill differs from the kit's version, read its real calls instead of this table.
