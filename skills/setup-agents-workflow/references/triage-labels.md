# Triage vocabulary

Use this mapping only when project triage is enabled. The triage procedure defines how decisions are made; this document maps their vocabulary to the project's existing labels or states. A mapping does not grant permission to classify, transition, comment on or close an item.

## Roles

The upstream defaults are a proposal for projects without established names:

| Canonical role | Default label | Meaning |
| --- | --- | --- |
| `needs-triage` | `needs-triage` | Requires evaluation |
| `needs-info` | `needs-info` | Requires specific additional information |
| `ready-for-agent` | `ready-for-agent` | Meets the project's criteria for delegated work |
| `ready-for-human` | `ready-for-human` | Requires the project's human-owned next step |
| `wontfix` | `wontfix` | Will not be acted on under the accepted decision |

During setup, replace defaults with agreed existing names or reference the authoritative mapping. Distinguish a label from a workflow status and record the approved transition method where applicable. A role that does not fit the project stays not applicable; do not invent a Jira status or force the upstream state machine onto incident management.

Map category terms such as bug, enhancement or incident only when the project uses them. For incoming PRs/MRs, establish the next-step meaning explicitly: human implementation, human review and permission to merge are not interchangeable.

## Use

Read the project triage procedure before choosing an outcome. Confirm the required evidence and human checkpoint, then apply only authorized metadata or state changes. A read-only agent can recommend a role without assigning it.

A ready label is not a permission grant, and `wontfix` is not an automatic instruction to close an incident or write a rejection file. Keep disposition criteria and reasons in the procedure or case record rather than duplicating them here.

Preserve existing vocabulary on reruns. Creating or renaming labels and changing workflow states need their own approval; agreeing this mapping during setup does not perform those actions.
