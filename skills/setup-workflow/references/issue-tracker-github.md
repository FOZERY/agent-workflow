# Issue tracker: GitHub

Use the GitHub repository and the access method that the project declares.
Requirements and implementation tickets can both live in GitHub Issues, or have different sources. Follow the agreement for each one. An external spec needs no copy in an issue body.

## Target and permissions

1. Before every write, find the exact repository. Pass it explicitly when the client could select an upstream repository or another clone. A remote helps you find the repository; it does not permit a write.
2. If the project uses an approved MCP access, use it instead of `gh`.
3. Keep each permission explicit: read, create, edit, comment, label, assign, link, change state, close. The commands below are a reference, not permissions.
4. In a read-only workflow, give the findings and the proposed actions to a human.
5. Missing access, an unsupported operation or an unclear target blocks that action.

## Operations with gh

Check that the installed CLI supports each option. Use the agreed repository.

- **Read:** `gh issue view <number> --json number,title,body,labels,comments,assignees,state`.
- **Find work:** `gh issue list --state open --json number,title,body,labels,assignees`, with the approved filters. Query other states when the procedure needs them.
- **Create:** `gh issue create --title "..." --body "..."`. Use the agreed issue type or template and a safe multiline body.
- **Edit or comment:** `gh issue edit` or `gh issue comment <number> --body "..."`, only for the approved fields and actions.
- **Label:** `gh issue edit <number> --add-label "..."` or `--remove-label "..."`. Use the project's label mapping. Creating a missing label is a separate operation.
- **Assign:** `gh issue edit <number> --add-assignee <login>`, when the project permits claims.
- **Close:** if permitted, post the required explanation, then run `gh issue close <number>`. An approved recommendation does not permit either write.

Issues and PRs in GitHub share one number space. If a reference is ambiguous, find its real type before you use issue or PR operations.

## Relationships and blocking

1. Prefer the native sub-issues and dependencies when the project supports them. GitHub CLI 2.94+ has `gh issue create --parent <parent>` and `gh issue edit <parent> --add-sub-issue <child>`. For dependencies, it has `--blocked-by` on create and `--add-blocked-by` on edit. Check that they exist; upgrade the CLI only with approval.
2. Through the API, sub-issue and dependency writes need the issue's database ID, not its number or node ID. Use the documented endpoint for the deployed service and client. Guess no request.
3. If native relationships are not available, agree a visible body or task-list convention with the owner before you rely on it.
4. A dependency is satisfied only when the blocking work meets the project's completion rule. A linked issue or a fix ticket does not prove that the system is fixed.

## Readiness

Record the readiness labels that the selected planning skills need. Their default is `ready-for-agent`; agree a project equivalent if needed. A readiness label does not permit implementation or publication.

## Publish and fetch

1. When a skill says "publish" a spec or ticket, create or update a GitHub issue only if GitHub is the agreed home of that artifact and the user permitted that write.
2. Otherwise, prepare a proposal for the owner or stop the dependent action. Create no local copy to get around the restriction.
3. When a skill says "fetch" a ticket, read its full relevant content and discussion.
4. Decide the next step by the project's entry and readiness rules, not by a label name alone.

## Wayfinding, when enabled

These operations apply only if the project keeps its decision map in GitHub. Implementation tickets in GitHub do not require the map there. With read-only access, inspect the sources and return proposed map updates to the owner.

- **Map:** one issue with the destination, notes and decision index, with the agreed map label or type. It indexes the answers and does not copy them.
- **Children:** decision issues for research, prototype, grilling or task work, linked to the map through native sub-issues or the agreed fallback. Link assets; paste no full documents.
- **Blocking:** native dependencies or the agreed explicit convention.
- **Frontier:** open, unblocked, unclaimed children in the agreed order. Check blockers and ownership, not only a label query.
- **Claim:** before work, the approved assignment or claim operation, if permitted. Otherwise a human claims the child.
- **Resolve:** record the answer, apply the permitted completion state and add a short linked pointer to the map. If a required write is forbidden, a human does that step, or it stays unavailable.

This guide creates no labels and no maps. The configured workflow and permissions decide whether these operations apply.
