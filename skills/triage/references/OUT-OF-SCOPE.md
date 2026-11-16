# Out-of-Scope Knowledge Base

Use the project's existing rejection/decision history for durable reasons a request was declined. It may be a tracker record, runbook, ADR or approved local document; no dedicated directory is required. Read root `AGENTS.md` and its triage/history pointers for ownership, location, format and permissions. Such records serve two purposes:

1. **Institutional memory**: why a feature was rejected, so the reasoning isn't lost when the issue is closed
2. **Deduplication**: when a new issue comes in that matches a prior rejection, the skill can surface the previous decision instead of re-litigating it

## Optional local representation

The following directory and sample format are illustrations only for a project that has agreed a local store. Preserve an existing source rather than creating a parallel knowledge base. If a new local location is useful, agree it before writing, normally under the project's `.docs/` namespace.

```
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

Where a local concept register is selected, grouping multiple requests under one concept can avoid duplication. Otherwise use the project's grouping and linking method.

## File format

Follow the project's record format. Capture the decision, rationale, scope, date/owner where required and source links clearly; include only technical detail needed to understand the reason. The sample below illustrates content, not a mandatory schema.

````markdown
# Dark Mode

This project does not support dark mode or user-facing theming.

## Why this is out of scope

The rendering pipeline assumes a single color palette defined in
`ThemeConfig`. Supporting multiple themes would require:

- A theme context provider wrapping the entire component tree
- Per-component theme-aware style resolution
- A persistence layer for user theme preferences

This is a significant architectural change that doesn't align with the
project's focus on content authoring. Theming is a concern for downstream
consumers who embed or redistribute the output.

```ts
// The current ThemeConfig interface is not designed for runtime switching:
interface ThemeConfig {
  colors: ColorPalette; // single palette, resolved at build time
  fonts: FontStack;
}
```

## Prior requests

- #42: "Add dark mode support"
- #87: "Night theme for accessibility"
- #134: "Dark theme option"
````

### Naming the file

For a newly agreed file-per-concept store, use a recognizable descriptive filename. Preserve established identifiers and naming in an existing store.

### Writing the reason

The reason should be substantive: not "we don't want this" but why. Good reasons reference:

- Project scope or philosophy ("This project focuses on X; theming is a downstream concern")
- Technical constraints ("Supporting this would require Y, which conflicts with our Z architecture")
- Strategic decisions ("We chose to use A instead of B because...")

The reason should be durable. Avoid referencing temporary circumstances ("we're too busy right now"); those aren't real rejections, they're deferrals.

## Consult the history

During triage, search the relevant project history for the affected concept. Compare reasons and scope, not merely keywords; cite the actual prior record and ask the responsible person when applicability is uncertain.

- **Confirmed applicable:** recommend the corresponding disposition and any link to this request.
- **Reconsidered:** propose a superseding decision or status update, preserving the prior rationale and provenance.
- **Related but distinct:** explain the difference and continue evaluating the request.

A past rejection is evidence, not automatic authority to reject or close new work. Distinguish durable rejection from temporary deferral, duplicate work and a behavior already implemented; the latter still needs relevance/deployment evidence for an incident.

## Record an accepted outcome

When the project requires a durable rejection record, use the authorized source and writer after its decision checkpoint. Link the request, rationale and responsible decision. Reuse a matching record where appropriate.

Commenting, labeling, closing, creating records and updating prior decisions are distinct effects under project permissions. With read-only access, present proposed text and transitions for the owner; do not create an unapproved local substitute.

## Preserve decision history

When a decision changes, follow the project's supersession/archival process. Preserve useful provenance and replacement links instead of deleting history merely because the new request proceeds. Retiring a local file follows the project's lifecycle and recoverable-deletion rules. Reopening or closing historical tracker items is a separate authorized action.
