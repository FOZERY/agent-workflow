# Skill catalog and project composition

Read this file when you select skills or configure their project settings.

## Selectable skills

Every skill is optional. For a skill that the user suggests, check its real source and procedure. Groups organize the list. A group is not a bundle and not a dependency.

| Group | Skills |
| --- | --- |
| Setup and guidance | `home-repo-init`, `setup-workflow`, `ask-workflow` |
| Task exploration | `investigate`, `grilling`, `grill-with-docs`, `domain-modeling`, `research`, `prototype`, `wayfinder`, `to-plan`, `to-spec`, `to-tickets` |
| Optional visual support | `excalidraw-diagram` |
| Implementation | `implement`, `tdd`, `simplify-codebase`, `code-review` |
| Retrospective and maintenance | `retro`, `cleanup`, `refactor-codebase`, `refactor-docs` |

- `ask-workflow` is an optional guide for workflow questions. It installs alone, before or after setup, and runs no procedures. Its selection selects no other skill.
- `home-repo-init` creates or revises a multi-repository home: navigation, approved shared material and client entry points. The user runs it manually and separately. `setup-workflow` can configure the home's procedures later. Neither skill calls the other.
- `human-text`, `asd-ste100` and `writing-for-agents` are separate writing skills. Configure their project use through [writing routes](writing.md). Setup recommends `human-text` when it is not installed; the user can decline it.
- `excalidraw-diagram` is an optional bundled skill. No other skill needs it, and setup does not have to install it. Configure it through [diagram configuration](diagrams.md).
- `to-plan` saves one implementation plan with its task. It needs no spec, no tickets and no other skill.

## Dependencies

These skills call the listed skills. Check that the client and its worker sessions have them.

| Caller | Calls |
| --- | --- |
| `setup-workflow` | `asd-ste100` and `writing-for-agents`, to write `AGENTS.md` and the project files |
| `grill-with-docs` | `grilling` and `domain-modeling` |
| `wayfinder` | `grilling` and `domain-modeling` for discussion; `research` and `prototype` for their ticket types; skills named in the map Notes |
| `implement` | `tdd` where it applies, `simplify-codebase` when its trigger is `auto`, and `code-review`: the Standards axis in each worker, the Spec axis in the orchestrator |
| `refactor-codebase` | `grilling`, `simplify-codebase` and `implement`; `domain-modeling` where the project selected it |
| `retro` | `writing-for-agents` |

1. The other skills have no fixed calls. Project rules or map Notes can add prerequisites.
2. `domain-modeling` and `prototype` call no other skills. Each one also works alone.
3. Before you agree a route, read its real requirements for tracker publication, commits, worktrees and branch pushes.
4. If an installed or source version of a skill differs from the kit's version, read its real calls instead of this table.
