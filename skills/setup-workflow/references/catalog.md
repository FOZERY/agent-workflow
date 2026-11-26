# Skill catalog and project composition

Read this file when you select skills or configure their project settings.

## Selectable skills

Every skill is optional. For a skill that the user suggests, check its real source and procedure. Groups organize the list. A group is not a bundle and not a dependency.

| Group | Skills |
| --- | --- |
| Setup and guidance | `setup-home-repo`, `setup-workflow`, `ask-workflow` |
| Task exploration | `investigate`, `recall`, `grilling`, `grill-with-docs`, `domain-modeling`, `research`, `prototype`, `wayfinder`, `to-plan`, `to-spec`, `to-tickets` |
| Implementation | `implement`, `tdd`, `simplify-codebase`, `verify`, `code-review` |
| Retrospective and maintenance | `retro`, `cleanup-artifacts`, `refactor-codebase`, `refactor-docs` |
| Writing | `writing-for-people`, `writing-technical`, `writing-for-agents`, `rephrase` |

- `ask-workflow` is an optional guide for workflow questions. It installs alone, before or after setup, and runs no procedures. Its selection selects no other skill.
- `setup-home-repo` creates or revises a multi-repository home: navigation, approved shared material and client entry points. The user runs it manually and separately. `setup-workflow` can configure the home's procedures later. Neither skill calls the other.
- `verify` checks a change in the running product by the procedure that setup records in its section: where to check, with which tools and which actions need approval.
- `writing-for-people`, `writing-technical` and `writing-for-agents` are separate writing skills. Configure their project use through [writing routes](writing.md). Setup recommends `writing-for-people` when it is not installed; the user can decline it.
- `rephrase` restates the last reply in plain words. The user runs it. It follows `writing-for-people` when that skill is installed.
- `to-plan` saves one implementation plan with its task. It needs no spec, no tickets and no other skill.

## Dependencies

These skills call the listed skills. Check that the client and its worker sessions have them.

| Caller | Calls |
| --- | --- |
| `setup-workflow` | `writing-technical` and `writing-for-agents`, to write `AGENTS.md` and the project files |
| `grill-with-docs` | `grilling` and `domain-modeling` |
| `wayfinder` | `grilling` and `domain-modeling` for discussion; `research` and `prototype` for their ticket types; skills named in the map Notes |
| `implement` | The steps that the user confirms in its step 3, with the trigger as the default: `tdd`, `simplify-codebase`, `verify` and `code-review`, with the Standards axis in each worker and the Spec axis in the orchestrator |
| `refactor-codebase` | `grilling`, `simplify-codebase` and `implement`, with the skills that `implement` calls; `domain-modeling` where the project selected it |
| `retro` | `writing-for-agents`; it gives the user a `/setup-workflow` command for changes to the core block or skill settings |

1. The other skills have no fixed calls. Project rules or map Notes can add prerequisites.
2. `domain-modeling` and `prototype` call no other skills. Each one also works alone.
3. Before you agree a route, read its real requirements for tracker publication, commits, worktrees and branch pushes.
4. If an installed or source version of a skill differs from the kit's version, read its real calls instead of this table.
