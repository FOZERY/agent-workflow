---
name: pr
description: "Prepare, create or update a pull request or merge request using the project's delivery procedure. Use for PR/MR content, publication or an authorized ready-for-PR handoff."
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

# Pull requests and merge requests

## 1. Resolve the project procedure

Read root `AGENTS.md` (or the project's `CLAUDE.md`) and its applicable delivery, commit, quality and PR/MR references. Use the project's template, naming rules, examples, participants and publication method. Ask only for missing or conflicting decisions; an absent setup does not require running the whole setup interview.

Establish the requested outcome: content only, create a PR/MR, or update an existing one. Follow the project's checkpoint and approval rules, including early drafts where allowed. Without a project rule, prepare content only and ask before any commit, push or remote write. Skill invocation and task readiness do not grant permissions beyond the request and applicable policy. Commit, push, publication, participant changes and merge have separate authority.

**Done when:** the outcome, procedure and permitted actions are known; unresolved authority blocks the affected action, not read-only preparation.

## 2. Resolve the changes and targets

Inspect the task, selected worktree, current branch, commits and working-tree changes to establish the intended comparison scope. For publication, resolve the source repository, remote and branch to push separately from the destination repository and base branch for merging, including forks. Show resolved targets and ask when ambiguous or when project policy requires confirmation. For content-only preparation, unresolved delivery targets can remain explicit as long as the change being described is known.

Inspect the full proposed change against the agreed comparison base, not just the last commit. Identify unrelated commits, uncommitted work or missing commits before publication; follow the project commit policy or hand off to the human rather than silently including, discarding or rewriting changes. Before creating a request, check for an existing PR/MR for the same source and destination; update it only within the authorized scope.

**Done when:** the intended change scope is known. Resolve targets, existing-request status and scope mismatches before publication; for content-only preparation, identify any unresolved delivery fields without blocking a draft of the known change.

## 3. Satisfy the delivery gates

For publication, follow the project's order for checks, review, human acceptance and hooks. Run authorized required commands using their project configuration. Keep native Git hooks enabled for operations that trigger them; execute any separate project-prescribed checks at their specified checkpoint. Reuse valid evidence for the same revision where policy allows it; rerun affected checks if the changes invalidate it.

Report failures and unavailable checks. Stop the gated operation rather than bypassing hooks, changing check configuration or treating pending results as success. Checks that run only after publication remain pending until their actual results are available. A draft with pending checks is allowed only by the project's procedure. Installing missing tools or making corrective code changes follows the project's separate permissions.

For content-only preparation, use available evidence and list unmet publication prerequisites in the handoff. Run checks only when the request or project procedure authorizes them for preparation. A request for title/body text does not itself authorize hooks, commits, pushes or remote writes.

**Done when:** prerequisites for the next action are met, or the blocker and permitted handoff are explicit.

## 4. Prepare the title, body and metadata

Use the authoritative project template and examples. Keep commit-message and PR-title conventions distinct. Include task references, observed evidence, remaining limitations and relevant merge risk in the project's required sections. Use closing keywords only when the corresponding tracker transition is authorized. If the project has no format, use the repository's template (`.github/pull_request_template.md` or `.gitlab/merge_request_templates/`) when present, otherwise [the default body format](references/body-format.md).

Resolve assignees, reviewers and labels through the project's ownership rules and available platform data. Preserve existing metadata outside the requested change and respect automated assignment. Distinguish recommendations from changes the agent may apply.

**Done when:** the title, body and required metadata match the actual change and project rules. For content-only or human-owned publication, hand over these materials and remaining actions, then stop.

## 5. Publish and verify

Obtain any approval still required for the concrete targets and effects. Commit only where the project procedure and authorization call for it. Push the intended source branch if needed, then create or update the PR/MR through the project's authorized CLI, API, MCP or automation. Use the agreed draft/ready state and metadata. Keep history rewriting, merge, deployment and branch cleanup outside this operation unless separately requested and authorized.

Read back the remote result: URL, source and base, title/body, draft state and requested metadata. If a write returns an uncertain result, inspect the remote state before retrying to avoid duplicate PRs. Follow the project's post-publication CI procedure and report pending or failed checks without claiming acceptance or merge.

**Done when:** publication and requested fields are verified, or the exact partial result and blocker are reported. Return the PR/MR link, performed actions, check status and remaining human decisions; distinguish saved local content from a published request.
