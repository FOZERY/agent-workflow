# Issue tracker: local Markdown

Use the task, spec and plan locations that `AGENTS.md` records. Keep an existing layout.
Propose the defaults below only when the user selects local tracking and the project has no convention. Record the accepted paths before other skills use them.

## Layout and authority

1. Default task directory: `<agent-docs>/<feature-slug>/`, which is `.docs/<feature-slug>/` by default. The spec is `spec.md` in that directory.
2. Each implementation ticket is one file `issues/<NN>-<slug>.md`, numbered from `01` in dependency order. Record a different project layout explicitly in the skill settings.
3. `to-plan` keeps its plan in the same task directory under the agreed name. The skill owns its fallback path. A spec or an `issues/` directory need not exist.
4. Reference tasks by stable IDs or paths. Record discussion, status and dependencies in the agreed fields.
5. A project can use other paths or external requirements. A Jira ticket or Confluence spec stays authoritative when it is the agreed source. Create no local copy to get around a denied write.
6. Agree who can create and edit each artifact, and which fields or state changes need a human. Local files follow the same permissions as any other artifact.
7. Git visibility follows the agreement for each artifact. The directory name does not make files tracked or ignored.

## Read and find work

1. Fetch a ticket by its path or ID and read its relevant discussion.
2. Find work by the agreed directory, state and dependency conventions, not by filename order alone.
3. Keep other writers' edits. Follow the project's claim and ownership rules.
4. Record the readiness labels that the selected planning skills need. Their default is `ready-for-agent`; agree a project equivalent if needed. A readiness label does not permit implementation or publication.

## Publish and update

1. When a skill says "publish" a spec or ticket, create or update the Markdown file only if local storage is its agreed home and the user permitted that write. Apply the content, readiness and approval rules.
2. A plan records implementation work and creates no tickets. Approval of a plan does not permit its execution.
3. Add comments under `## Comments`. Keep the earlier comments as they are.
4. Apply only permitted state changes. Closing, deleting and migrating a task are separate decisions. A file with a similar name does not prove duplicate work or a resolved issue.
5. During setup, configure these conventions only. Create task directories, plans, specs and tickets when real work needs them.

## Wayfinding, when enabled

These defaults keep the upstream map and child shape. Adapt names and states to existing project conventions.

- **Map:** the agreed local map file, for example `.docs/planning/<effort>/map.md` when a new location is needed.
- **Children:** decision sections or linked files, with stable references and a type: research, prototype, grilling or task. A separate file for each question is optional.
- **State:** explicit open, claimed and resolved states, or the project's equivalents. A claim names the responsible actor under the coordination rules.
- **Blocking:** a `Blocked by:` field with concrete child IDs or paths. A child is unblocked only when its blockers meet the agreed resolution condition.
- **Frontier:** open, unblocked, unclaimed children in the agreed order.
- **Claim:** save the permitted claim before you start. If local writes are forbidden, the owner claims the child, or the step stays blocked.
- **Resolve:** add the answer under `## Answer`, record the permitted resolved state and add a short linked pointer to the map's decision index. The full answer stays in the child.

A file on disk does not prove that its content, claim or status is current. Read the affected records again before an update. If claims conflict, ask the owner; overwrite no other participant's record.
