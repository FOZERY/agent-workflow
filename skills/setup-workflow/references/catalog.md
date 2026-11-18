# Package catalog and project composition

Read when selecting packages or configuring their project settings. Check the actual skill calls and [deployment status](skills.md#check-same-name-copies) before declaring a route usable.

## Selectable skills

Discuss only relevant groups. Use a native choice tool when useful, without forcing a fixed questionnaire. Each package is optional; include user-suggested skills and check their actual source and procedure.

| Group | Packages |
| --- | --- |
| Setup and guidance | `home-repo-init`, `setup-workflow`, `ask-workflow` |
| Task exploration | `grilling`, `grill-with-docs`, `domain-modeling`, `research`, `prototype`, `wayfinder`, `to-plan`, `to-spec`, `to-tickets` |
| Optional visual support | `excalidraw-diagram` |
| Implementation | `implement`, `implement-with-swarm`, `tdd`, `codebase-design`, `code-review` |
| Retrospective and maintenance | `retro`, `cleanup`, `refactor-docs` |

Group membership is not a dependency. Create project-specific sections only for selected skills that need settings.
Ask about tools and MCP integrations separately from package selection. Record their authorized purpose and prerequisites in the project contract, not as kit dependencies.
`to-plan` saves one task-linked implementation plan. It requires neither a specification nor tracker tickets and has no fixed skill dependencies.
For plan-based execution, agree on a receiver that accepts the plan and its source task.

`implement-with-swarm` uses existing task sources. Make `implement` available to each worker and configure the worker modes and integration rules.

`home-repo-init` creates or revises a multi-repository home: navigation, approved shared material and client entrypoints.
It is standalone and manually invoked. `setup-workflow` can configure that home's procedures afterward, but neither skill requires or invokes the other.
Task planning remains separate; use `to-plan` only when a task needs an implementation plan.

## Writing choices

`human-text`, `asd-ste100` and `writing-for-agents` are separate writing packages.
The [writing contract](writing.md) proposes their use for conversation, artifacts and reusable rules in the consumer project's `AGENTS.md`.
`setup-workflow` itself needs none of them and can be installed alone.

## Diagram choice

`excalidraw-diagram` is a bundled optional package, not a required helper of the original skills.
Use [diagram configuration](diagrams.md) for relationships and alternatives, interfaces, interaction architecture or a supporting prototype sketch.
Project skill sections link to one `excalidraw-diagram` policy. Selecting the package does not authorize individual diagrams or require setup to install it.

## Dependencies

These procedures require access to the listed packages. Verify availability in the target client and its worker sessions.

| Caller | Calls and availability |
| --- | --- |
| `grill-with-docs` | `grilling` and `domain-modeling` |
| `wayfinder` | `grilling` and `domain-modeling` for discussion; `research` and `prototype` for their ticket types; additional skills named in map Notes |
| `tdd` | Conditional `codebase-design` call when the interface or seam is in question |
| `implement` | `tdd` where possible and `code-review` |
| `implement-with-swarm` | Explicit `implement` request per worker, or readable access to the same procedure for workers that cannot invoke manual skills |
| `retro` | `writing-for-agents` |

Other retained packages have no fixed inter-skill call in their own procedure. Project rules or task-specific map Notes can add prerequisites.
The included `domain-modeling`, `prototype` and `codebase-design` helpers have no additional fixed skill calls. They are available individually as well as through their callers.
Do not restore removed helpers, download substitutes or patch callers as an implicit setup step.
Some prompts retain `/setup-matt-pocock-skills`; our `/setup-workflow` is not an installed alias.
Read actual tracker publication, commit, worktree and branch-push requirements before agreeing a route.
Project rules still own permission and additional writing choices. Installation grants neither.

If an installed or source version of a package differs from this kit's, read its actual skill calls instead of relying on this table.
