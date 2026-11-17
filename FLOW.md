# Workflow and package composition

The repository combines Matt-derived skills, local setup and writing tools.
The [catalog](docs/SKILLS.md) describes invocation and prerequisites. The [source ledger](docs/UPSTREAM.md) records exact copies and minimal adaptations.

## Project setup

`setup-workflow` reads existing rules, discusses missing decisions and previews configuration separately from installation.
Root `AGENTS.md` holds shared rules and sections for selected skills. User additions can name other skills, coding practices and examples.
The [reference structure](skills/setup-workflow/references/AGENTS.md) defines that organization and the automation settings. It grants no permissions.
Context and lessons share the selected directory, default `.docs/`.

The project can assign conversation to `human-text`, artifact prose to `asd-ste100`, and reusable rules to `writing-for-agents`.
The [writing contract](skills/setup-workflow/references/writing.md) defines optional integration and loading triggers.
Neither installing a package nor saving desired configuration grants operational permission.

## Project settings and defaults

Twelve skills read project instructions before starting: `code-review`, `implement`, `implement-spec`, `research`, `retro`, `tdd`, `to-spec`, `to-tickets`, `wayfinder`, `domain-modeling`, `prototype` and `codebase-design`.
Specified sources, paths and workflow settings apply; unspecified settings retain upstream defaults.
That paragraph is their only change from M1. `grill-with-docs` and `writing-for-agents` remain exact copies.
The kit includes all fixed helper dependencies; check [the required client installations](skills/setup-workflow/references/catalog.md#dependencies).

- `grilling` remains our adapted interview and can run without setup.
- `grill-with-docs` delegates to other skills rather than containing our previous interview procedure.
- `wayfinder` calls `grilling`, `domain-modeling`, `research` and `prototype` on their original branches.
- `tdd` consults `codebase-design` when the interface or test seam is in question.
- `to-spec` and `to-tickets` use project artifact settings where specified, with upstream formats and publication defaults elsewhere.
- `implement` and `implement-spec` use the agreed TDD and review settings; their other upstream steps remain.
- `retro` proposes environment improvements. Recording approved outcomes in project memory needs an explicit project rule.

## Project compatibility

Setup reads the selected skills before promising a configured route.
It discusses automatic or manual TDD/review, execution location and reporting versus authorized fixes with another review.
Test practices and review sources come from the project. The user accepts the work; acceptance is not a flag.
It [matches review coverage to the implementation checkpoint](skills/setup-workflow/references/AGENTS.md#review-coverage), including whether the intended changes are committed or in the working tree.

Setup does not rewrite installed packages. An unavailable helper or conflicting mandatory step must be reported.
Settings are prompt instructions, not an execution engine. Delegated workers need the applicable rules and readable source pointers.

## Verification limits

Byte equality establishes that the packages match the pinned source.
Installation and metadata checks establish packaging and discovery, not model adherence or runtime readiness.
Missing prerequisites and unexercised client capabilities remain explicit.
The repository installs no scheduler, update service or permission mechanism.

