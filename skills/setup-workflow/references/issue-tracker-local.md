# Issue tracker: local Markdown

Use the task/spec/plan locations agreed in the project contract. Preserve an existing layout. The conventions below are defaults to propose only when local tracking is selected and no convention exists; record concrete accepted locations before other skills use them.

## Layout and authority

- If no project layout is specified, use `<agent-docs>/<feature-slug>/` (default `.docs/<feature-slug>/`), with the specification at `spec.md`.
- Put one implementation ticket in each `issues/<NN>-<slug>.md`, numbered from `01` in dependency order. A different agreed project layout must be explicit in its skill settings.
- A selected `to-plan` route keeps its implementation plan in the same task directory under its agreed name. The skill owns the fallback path; a specification or `issues/` directory need not exist.
- Use stable task IDs or paths for references; record discussion, status and dependency information in the accepted fields.

A project may use different paths or externally owned requirements. A Jira ticket or Confluence spec remains authoritative when that is the accepted source; do not create a duplicate local version to bypass denied writes.

Agree who may create/edit each artifact and which fields or state changes require a human. Local files are not exempt from permissions. Their Git visibility follows the per-artifact agreement; neither this directory name nor this guide makes it automatically tracked or ignored.

## Reading and finding work

Fetch a ticket by its concrete path/ID and read its relevant discussion. Find work by the agreed directory, state and dependency conventions, not filename order alone. Preserve other writers' edits and respect the project's claim/ownership rules.

Record the readiness vocabulary required by selected planning skills. Their default is `ready-for-agent`; agree a project equivalent when needed. Readiness does not authorize implementation or publication.

## Publishing and updating

When a selected skill says to publish a spec or ticket, create/update the corresponding Markdown artifact only if local storage is its agreed home and the operation is authorized. Apply the required content, readiness and approval rules. A plan records implementation work without creating tickets; its approval is not permission to execute it.

Comments append to `## Comments` without rewriting history. Apply only permitted state changes. Closing, deleting or migrating a task are separate decisions; a similarly named file is not proof of duplicate work or a resolved issue.

Configure these conventions during setup without generating empty feature directories, plans, specs or tickets. Create them when substantive work actually needs them.

## Wayfinding, when enabled

The following defaults preserve the upstream map/child shape; adapt names and states to existing project conventions:

- **Map**: the agreed local map document, for example `.docs/planning/<effort>/map.md` when a new location is needed.
- **Children**: decision sections or linked files, with stable references and logical research, prototype, grilling or task types. A separate file per question is optional.
- **State**: explicit open, claimed and resolved states, or the existing project's equivalents. Claim records must identify the responsible actor under its coordination rules.
- **Blocking**: a `Blocked by:` field with concrete child IDs/paths. A child is unblocked only when its listed blockers satisfy the agreed resolution condition.
- **Frontier**: open, unblocked and unclaimed children in the agreed order.
- **Claim**: save the authorized claim before starting; if local writes are forbidden, the owner claims it or the step remains blocked.
- **Resolve**: append the answer under `## Answer`, record the allowed resolved state and add a short linked pointer to the map's decision index. Detailed answers remain in the child rather than being copied into the map.

A file existing on disk does not establish that its contents, claim or status are current. Re-read affected records before updates and escalate conflicting claims instead of overwriting another participant.
