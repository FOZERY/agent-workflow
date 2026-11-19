# Issue tracker: GitLab

Use the GitLab instance, project and access method that the project declares.
Specs can live elsewhere while implementation issues live in GitLab. Keep each artifact in its own source; copy no external requirements.

## Target and permissions

1. Before every write, find the exact instance and project, also for forks and self-hosted hosts. Pass the target explicitly when the client could select another project.
2. A remote or a logged-in `glab` session does not permit a write.
3. If the project uses an approved MCP access, use it instead of `glab`.
4. Keep each permission explicit: read, create, edit, comment, label, assign, link, change state, close. The commands below are a reference, not permissions.
5. In a read-only workflow, give the findings and the proposed changes to the owner.
6. An unsupported operation or an unclear target blocks that action. Use no other write channel instead.

## Operations with glab

Check each option against the installed CLI and the GitLab instance.

- **Read:** `glab issue view <number> --comments`. Request JSON only through supported output options.
- **Find work:** `glab issue list -O json`, with the approved state and label filters, where supported.
- **Create:** `glab issue create --title "..." --description "..."`. Use the agreed template and multiline content.
- **Comment:** `glab issue note <number> --message "..."`. GitLab calls comments notes.
- **Edit, label or assign:** the matching `glab issue update` options, only for permitted fields. The upstream label options are `--label` and `--unlabel`. Map roles to existing project labels. Creating a label needs separate permission.
- **Close:** if permitted, post the required explanation first, then run `glab issue close <number>`. A recommendation does not permit either write.

Issues and MRs in GitLab have separate number spaces. Find both the item type and the project. MR operations use `glab mr`, for example `view`, `diff`, `note` and `update`. Check their options; do not translate issue commands mechanically.

## Relationships and blocking

1. Use the project's native links or parent and child hierarchy when available. The upstream link example is `glab issue create --linked-issues <map> --link-type relates_to`.
2. If the project uses a body convention, record an explicit parent pointer and dependencies with real IDs.
3. Native blocking links depend on the GitLab tier and instance. Where available and permitted, post the `/blocked_by #<blocker>` quick action in an issue note. A quick action is a write, not a read.
4. If native blocking is not available, agree an explicit `Blocked by` convention. Claim no native link that does not exist.
5. Check the real state of each blocker against the project's completion rule. A fix issue that exists, is closed or is merged does not prove deployment or incident resolution.

## Readiness

Record the readiness labels that the selected planning skills need. Their default is `ready-for-agent`; agree a project equivalent if needed. A readiness label does not permit implementation or publication.

## Publish and fetch

1. When a skill says "publish", create or update a GitLab issue only if GitLab is the agreed home of that artifact and the user permitted that write.
2. Otherwise, prepare a proposal or ask the owner. Create no local copy to get around a read-only policy.
3. When a skill says "fetch" a ticket, read the issue and its relevant comments from the correct project.
4. Before implementation, follow the project's readiness and human-checkpoint rules.

## Wayfinding, when enabled

These operations apply only if the project keeps its decision map in GitLab. Implementation tickets and decision maps can live in different places. Read-only access permits inspection and proposals, not the writes below.

- **Map:** a map issue or a supported parent artifact that the project selects, with the destination, notes and decision index. Assume no access to epics.
- **Children:** linked decision issues for research, prototype, grilling or task work, with the agreed types or labels and parent pointers.
- **Blocking:** native links where supported, otherwise the agreed explicit convention.
- **Frontier:** open, unblocked, unclaimed children in the agreed order. Check linked blockers and ownership.
- **Claim:** before work, the approved assignment or claim operation. If agent writes are forbidden, a human claims the child.
- **Resolve:** record the answer, apply the permitted completion state and add a short linked pointer to the map. If a required write is not permitted, a human does that step, or the dependent step stays blocked.

During setup, this guide initializes no remote, creates no labels, opens no issues and changes no instance or project settings.
