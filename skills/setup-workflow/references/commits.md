# Project commit policy interview

Read when configuring or revising how changes become commits, including workflows where the human commits and the agent only prepares a message. This is a setup reference, not a separate skill or permission to commit during setup.

## Reuse project evidence

Inspect existing contribution rules, commit-message validation, hook configuration and applicable delivery instructions within the approved scope. Reuse their authoritative sources; do not copy validator settings or hook bodies into `AGENTS.md`. Recent commits and owner-provided examples illustrate the convention but do not override documented rules. Ask the owner for references or accepted examples when the convention is not established.

## Establish the checkpoint and authority

Ask: "Who creates commits here: you, the agent with standing permission, or the agent after a separate approval? At which checkpoint: during work, after checks, after agent review, or after human acceptance? Are intermediate/WIP commits allowed? What must be handed over when only a message may be prepared?"

Record the chosen sequence and the evidence that must cover the committed content. There is no universal commit-after-review or commit-before-review rule. Preparing a message, creating a local commit, pushing and publishing a PR/MR are distinct effects. A ready task or completed check does not grant an otherwise missing permission.

## Establish message format and change grouping

Ask: "Which format and language apply to the subject and body? Are types/scopes, task identifiers, breaking-change notes, trailers or signing required? Can you point to the rule and representative accepted messages? Should one task be one commit, several coherent commits, or later squashed?"

Use the project's convention. Offer Conventional Commits only as a fallback for agreement where no rule exists, not as a mandatory format for every project. Capture unwritten requirements and exceptions while pointing to machine-enforced settings. Commit grouping and eventual PR squash/merge policy can differ. Rewriting existing history needs its own project authorization.

## Establish checks and content boundaries

Ask: "Which checks and hooks must pass before or during a commit, and where are they configured? What happens when a hook fails or cannot run? Which branch/worktree and changes belong to the task?"

Connect these answers to the quality and ownership rules already agreed. Keep unrelated staged/unstaged work outside the task's commit; use the client's approved selective-commit mechanism. Check the proposed content for secrets. Report failed/unavailable checks and block the affected commit where required; formatting or task completion does not authorize bypassing hooks, changing validators or weakening checks. Inspecting hook configuration does not execute it.

## Capture the rule in project instructions

In root `AGENTS.md` or the existing workflow owner, record the commit checkpoint, actor/approval, message-convention source, grouping and required check/hook sources. Keep permission limits visible. If details already live in contribution/delivery documentation, add a mandatory trigger to read those rules before preparing a message or committing; otherwise write the concise agreed rule inline. A separate project policy file is needed only when useful and approved.

Keep PR/MR title, description, participants and publication rules in their own contract. Do not infer a PR title from a commit message or assume both use the same convention. Check selected implementation skills for unconditional commit instructions conflicting with this policy; surface the necessary adaptation instead of claiming a pointer already fixed their prompts.

**Done when:** commit authority and checkpoint, message format/source, change grouping, required checks/hooks and failure behavior are explicit, and the instruction owner exposes them before commit preparation/execution. Setup has created no commits, rewritten no history and published nothing.
