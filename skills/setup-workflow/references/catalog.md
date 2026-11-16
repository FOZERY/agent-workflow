# Kit catalog and dependencies

Read this when offering skills, planning installation or checking a caller's prerequisites. It lists this kit's packages. A same-named skill from another source is a different package; check it with the [same-name check](skills.md#check-same-name-copies).

## Selectable skills

Offer these as four multi-select questions, one per group. Each option is one line below; an option joined with `+` installs both skills. The layout fits a native question tool limited to 4 questions of 4 options; a text list keeps the same groups.

| Question | Options |
| --- | --- |
| Planning | `grilling`; `grill-with-docs`; `to-spec` + `to-tickets`; `wayfinder` |
| Analysis | `research` |
| Implementation and delivery | `implement` + `implement-spec`; `tdd`; `code-review` |
| Memory, documents and guidance | `retro`; `cleanup`; `refactor-docs`; `ask-workflow` |

Split a joined option when the owner asks for only one of its skills. `setup-workflow` is already running and `human-text` is settled earlier in the interview, so neither appears in these questions.

## Helper skills

`writing-for-agents` is installed together with `setup-workflow` at bootstrap, because setup follows it to write `AGENTS.md`, `CONTEXT.md` and `LESSONS.md`. It stays user-invocable and is not offered in the selection questions.

## Dependencies

This table is the kit's dependency graph. Install the full set for every selected caller, following it transitively.

| Caller | Required packages |
| --- | --- |
| `grill-with-docs` | `grilling` |
| `wayfinder` | `grilling`, `research` |
| `implement`, `implement-spec` | `code-review` with its bundled `references/implementation-cycle.md`; `human-text` for the parent's walkthrough |
| `refactor-docs` | `human-text` with its language references |
| `retro` | `writing-for-agents` |

Every other package has no required skill. `implement` and `implement-spec` read `tdd` only when the user asks for TDD, so install it with them when the user wants that option. It is not a required dependency. A project may add review skills that the configured reviewer must load; those come from the project contract, not this table.

If an installed or source version of a package differs from this kit's, read its actual skill calls instead of relying on this table.
