# Delivery settings

Read when configuring or changing Git and delivery behavior. Reuse contribution rules, commit validation, hooks, PR/MR templates and ownership rules before asking about gaps.

Agree only what those sources do not settle:

- **Commits:** who commits, at which checkpoint, whether intermediate commits are allowed, message language/convention, grouping and signing. Reference accepted examples when useful.
- **Checks:** which existing checks or hooks gate each action, and what happens when they fail or are unavailable. A failed hook does not authorize bypassing it.
- **PR/MR content:** the authoritative template, title/body requirements, evidence, task links and permitted closing keywords. Commit and PR-title conventions can differ.
- **Delivery:** separate permissions for commit, push, PR/MR creation or updates, merge, deployment and branch cleanup. Record target-selection rules, not a guessed future branch.
- **Participants:** use existing ownership/reviewer rules. Ask how to resolve missing ownership and whether metadata may be proposed or applied.

Record the concise agreement under Git and delivery in root `AGENTS.md`. Add action-specific reading pointers to existing procedures. Create a supporting project document only when the agreed detail needs one.

Keep unrelated work and secrets out of commits. Preserve the client's approved selective-commit mechanism. Installation or setup approval grants no delivery permission. Compare selected skills' commit, tracker and working-copy steps with these rules and report incompatible required actions.

**Done when:** each enabled delivery action has a source, checkpoint and actor/permission; unresolved targets or checks have a stop condition. Setup has performed none of those actions.
