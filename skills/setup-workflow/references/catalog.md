# Package catalog and project composition

Read when selecting packages or configuring their project settings. Check the actual skill calls and [deployment status](skills.md#check-same-name-copies) before declaring a route usable.

## Selectable skills

Discuss only relevant groups. Use a native choice tool when useful, without forcing a fixed questionnaire. Each package is optional; include user-suggested skills and check their actual source and procedure.

| Group | Packages |
| --- | --- |
| Setup and guidance | `setup-workflow`, `ask-workflow` |
| Task exploration | `grilling`, `grill-with-docs`, `domain-modeling`, `research`, `prototype`, `wayfinder`, `to-spec`, `to-tickets` |
| Implementation | `implement`, `implement-spec`, `tdd`, `codebase-design`, `code-review` |
| Retrospective and maintenance | `retro`, `cleanup`, `refactor-docs` |

Group membership is not a dependency. Create project-specific sections only for selected skills that need settings.

## Writing choices

`human-text`, `asd-ste100` and `writing-for-agents` are separate writing packages.
The [writing contract](writing.md) proposes their use for conversation, artifacts and reusable rules in the consumer project's `AGENTS.md`.
`setup-workflow` itself needs none of them and can be installed alone.

## Dependencies

These are the original skill calls. All fixed helper packages are included in the kit; verify installation in the target client:

| Caller | Calls and availability |
| --- | --- |
| `grill-with-docs` | `grilling` and `domain-modeling` |
| `wayfinder` | `grilling` and `domain-modeling` for discussion; `research` and `prototype` for their ticket types; additional skills named in map Notes |
| `tdd` | Conditional `codebase-design` call when the interface or seam is in question |
| `implement` | `tdd` where possible and `code-review` |
| `implement-spec` | Per-ticket `tdd` and integrated `code-review` |
| `retro` | `writing-for-agents` |

Other retained packages have no fixed inter-skill call in their own procedure. Project rules or task-specific map Notes can add prerequisites.
The included `domain-modeling`, `prototype` and `codebase-design` helpers have no additional fixed skill calls. They are available individually as well as through their callers.
Do not restore removed helpers, download substitutes or patch callers as an implicit setup step.
Some prompts retain `/setup-matt-pocock-skills`; our `/setup-workflow` is not an installed alias.
Read actual tracker publication, commit, worktree and branch-push requirements before agreeing a route.
Project rules still own permission and additional writing choices. Installation grants neither.

If an installed or source version of a package differs from this kit's, read its actual skill calls instead of relying on this table.
