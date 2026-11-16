# Issue tracker: GitHub

Use the GitHub repository and approved access method declared by the project. Requirements and implementation tickets may share GitHub Issues or have different authoritative sources; follow their individual contracts. An external spec does not need a duplicate issue body.

## Target and permissions

Resolve the exact repository before every write; pass that target explicitly when the client could otherwise select an upstream repository or another clone. A remote is a discovery hint, not authorization. Existing MCP access may be the project's approved interface instead of `gh`.

Keep the project's read/create/edit/comment/label/assign/link/transition/close permissions explicit. The operations below are a vocabulary and CLI reference, not grants. A read-only workflow produces findings and proposed actions for a human. Missing access, unsupported operations and unclear targets block the affected action.

## Operations when using gh

Verify the installed CLI's support and use the agreed repository target:

- **Read**: `gh issue view <number> --json number,title,body,labels,comments,assignees,state`.
- **Find work**: `gh issue list --state open --json number,title,body,labels,assignees`, with project-approved filters; query other states when the procedure requires them.
- **Create**: `gh issue create --title "..." --body "..."`; use the agreed issue type/template and a safe multiline body.
- **Edit or comment**: `gh issue edit` or `gh issue comment <number> --body "..."`, only for the approved fields/action.
- **Label**: `gh issue edit <number> --add-label "..."` or `--remove-label "..."`; use the project role mapping. Creating a missing label is a separate operation.
- **Assign**: `gh issue edit <number> --add-assignee <login>` when the project permits a claim/assignment.
- **Close**: post the required explanation if authorized, then `gh issue close <number>`. An approved recommendation alone does not authorize either mutation.

GitHub issues and PRs share a number space. Resolve an ambiguous reference to its actual type before using issue or PR operations.

## Relationships and blocking

Prefer the project's native sub-issues and dependencies when supported. GitHub CLI 2.94+ provides `gh issue create --parent <parent>` and `gh issue edit <parent> --add-sub-issue <child>`; dependency options include `--blocked-by` on create and `--add-blocked-by` on edit. Verify availability rather than upgrading the CLI implicitly.

For an approved API implementation, sub-issue and dependency writes require the relevant issue database ID, not its display number or node ID. Use the documented endpoint for the deployed service/client instead of guessing a request. If native relationships are unavailable, agree a visible body/task-list convention with the owner before relying on it.

A dependency is satisfied only when its blocking work meets the project's completion rule. A linked issue or existing fix ticket does not prove that the affected system is fixed.

## Triage

Before triaging, read the declared project procedure for request types, evidence, routing, overlapping work, outcomes and escalation. Use the separate vocabulary mapping; labels do not replace that procedure.

Incoming PRs are a triage surface only if the project includes them. Agree which authors and states belong in discovery; do not treat the team's own delivery PRs as incoming requests by default. Read the PR body, comments and diff through the approved method. Preparing PR content is a separate workflow with its own format.

## Publishing and fetching

When an enabled skill says to publish a spec or ticket, create/update a GitHub issue only if GitHub is that artifact's agreed source and the specific mutation is authorized. Otherwise prepare a proposal for its owner or stop the dependent action; do not create a local duplicate to evade the restriction.

When a skill says to fetch a ticket, read its full relevant content and discussion. Use the project's entry/readiness rules, not a label's name alone, to decide what may happen next.

## Wayfinding, when enabled

These operations apply only if the project locates its decision map in GitHub. Using GitHub for implementation tasks does not require storing maps there. With read-only access, inspect sources and return proposed map updates to the authorized owner.

- **Map**: one issue holding the destination, notes and decision index, using the agreed map label/type. It indexes answers rather than duplicating them.
- **Children**: decision issues for research, prototype, grilling or task work, related to the map through native sub-issues or the agreed fallback. Link assets instead of pasting full documents.
- **Blocking**: native dependencies or the accepted explicit convention.
- **Frontier**: open, unblocked, unclaimed children in the agreed order; inspect blockers and ownership, not just a label query.
- **Claim**: the project's approved assignment/claim operation before work, if authorized; otherwise a human claims it.
- **Resolve**: record the answer, apply the permitted completion transition and add a short linked pointer to the map. If any required write is forbidden, the dependent step stays human-owned or unavailable.

Create neither missing labels nor maps merely because this guide is present. The configured workflow and permissions determine whether these operations apply.
