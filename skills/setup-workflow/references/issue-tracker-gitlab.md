# Issue tracker: GitLab

Use the GitLab instance, project and approved access method declared by the project. Specs may live elsewhere while implementation issues live here. Preserve each artifact's authoritative source instead of duplicating external requirements.

## Target and permissions

Resolve the exact instance and project before every write, including forks and self-hosted hosts. Pass the agreed target explicitly where the client could choose another project. A remote or authenticated `glab` session is not a write grant. Use an existing approved MCP interface instead when the project specifies it.

Keep read/create/edit/comment/label/assign/link/transition/close permissions explicit. The operations below are reference material, not authorization. In a read-only workflow, present findings and proposed changes to the owner. An unsupported operation or unclear target blocks that action rather than permitting a different write channel.

## Operations when using glab

Verify options against the installed CLI and configured GitLab instance:

- **Read**: `glab issue view <number> --comments`; request JSON only through supported output options.
- **Find work**: `glab issue list -O json` with the project-approved state/label filters, when supported.
- **Create**: `glab issue create --title "..." --description "..."`, using the agreed issue template and multiline content.
- **Comment**: `glab issue note <number> --message "..."`; GitLab calls comments notes.
- **Edit, label or assign**: the relevant `glab issue update` options, only for authorized fields. The upstream label examples are `--label` and `--unlabel`; map roles to existing project names. Label creation needs separate authority.
- **Close**: post the required explanation first, if authorized, then `glab issue close <number>`. A recommendation does not authorize either operation.

GitLab issues and MRs have separate number spaces. Resolve both the item type and project. Merge-request operations use `glab mr`, such as `view`, `diff`, `note` and `update`; verify command options instead of mechanically translating every issue command.

## Relationships and blocking

Follow the project's native links or parent/child hierarchy when available. The upstream issue-link example is `glab issue create --linked-issues <map> --link-type relates_to`. If the project uses a body convention, record an explicit parent pointer and dependencies with real IDs.

Native blocking links can depend on GitLab tier and instance capabilities. Where available and authorized, GitLab supports the `/blocked_by #<blocker>` quick action in an issue note. If unavailable, agree an explicit `Blocked by` convention rather than claiming a native link exists. Posting a quick action is a mutation, not an ordinary read.

Check the actual state of all blockers against the project's completion criteria. A fix issue being present, closed or merged is not proof of deployment or incident resolution.

## Readiness

Record the readiness vocabulary required by selected planning skills. Their default is `ready-for-agent`; agree a project equivalent when needed. Readiness does not authorize implementation or publication.

## Publishing and fetching

An enabled skill's instruction to publish means create/update a GitLab issue only when this is the artifact's agreed home and the particular action is authorized. Otherwise prepare a proposal or ask its owner; do not bypass a read-only policy through local duplicates.

Fetching a ticket means reading the issue and relevant comments from the correct project. Follow the project's readiness and human-checkpoint rules before implementation.

## Wayfinding, when enabled

These operations apply only if the project locates its decision map in GitLab. Implementation tickets and decision maps may have different authoritative homes. Read-only access permits inspection and proposals, not the writes described below.

- **Map**: a project-selected map issue or supported parent artifact containing the destination, notes and decision index. Do not assume access to an epic feature.
- **Children**: linked decision issues for research, prototype, grilling or task work, using agreed types/labels and parent pointers.
- **Blocking**: native links where supported, otherwise the accepted explicit convention.
- **Frontier**: open, unblocked and unclaimed children in agreed order, including checks of linked blockers and ownership.
- **Claim**: the approved assignment/claim operation before work; a human performs it when agent writes are forbidden.
- **Resolve**: record the answer, apply the allowed completion transition and append a short linked context pointer to the map. Keep unauthorized required writes human-owned or block the dependent step.

This guide does not initialize a remote, create labels, open issues or change instance/project settings during setup.
