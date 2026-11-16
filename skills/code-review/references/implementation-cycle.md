# Implementation review and acceptance cycle

Read this as the parent/coordinator of `implement` or `implement-spec`. The reviewer itself follows `code-review/SKILL.md`. This is the shared completion procedure for both implementation skills, not another skill to install.

## 1. Dispatch independent review

After implementation and required checks, launch a fresh reviewer subagent yourself. This is a required step of these implementation routes, not an optional self-review. Use the client's subagent mechanism: the Agent tool in Claude Code, `spawn_agent` in Codex, a task subagent in OMP. Take the reviewer role and model from the project contract; without one, use the client's general-purpose subagent with its default model. An existing project hook may replace this launch only when it is configured and verified.

If the contract's model is unavailable, ask the user before substituting another. If the client cannot launch subagents or the contract forbids delegation, give the user the review brief below and ask them to run `/code-review` (`$code-review` in Codex) in a new session with it, then paste the result back. That result counts as the independent review for the revision the brief names. Your own review of your work never counts. Setup may grant standing permission for this bounded review so repeated approval is unnecessary.

Give the reviewer:

- The `code-review` skill and required project review skills, with loadable paths or their relevant contents.
- Project instructions and triggered standards, test and review references. Supply them explicitly when child contexts do not inherit them.
- Task/spec, acceptance criteria, accepted decisions and any previous findings and human feedback.
- Exact repository/worktree, original task base, stable endpoint or scoped working-tree snapshot, included paths and exclusions.
- Actual check results and their revision, known limitations and read-only boundaries.

Keep the brief self-contained without copying the implementation conversation. Ensure the supplied view includes intended staged, unstaged and untracked changes. Wait for the real review result; a dispatch receipt alone is not evidence of review.

**Done when:** an independent reviewer, a subagent or a user-run session, has returned findings for the current complete change, or the review gate is explicitly blocked.

## 2. Resolve findings within authority

Assess each finding against its evidence and project rules. Apply the reviewer's deterministic-correction category only when the rule uniquely determines the fix and the project permits automatic correction. Without a project rule, apply the project's formatter and linter autofixes and fixes that a documented rule determines uniquely without changing behavior; list every other finding for the human. Preserve behavior, scope and unrelated work. A small diff or a low-severity label does not prove a correction is safe.

The parent or an authorized implementer makes those corrections, not the reviewer. Retain a brief finding disposition: fixed, needs human decision, or not applicable with evidence. Uncertainty, conflicting rules and behavior/design choices go to the human; do not quietly dismiss a blocker.

Run affected checks after corrections and obtain a new fresh-context review of the updated full change, including prior findings and dispositions. If the same issue persists, reviewers disagree or the fix expands scope, escalate to the human. Count review rounds, one per reviewer result: after the third round without reaching ready for human review, stop and ask the human how to proceed, listing the open findings. If they say to continue, allow three more rounds.

**Done when:** justified automatic fixes are verified and reviewed, and all remaining decisions or blockers are identified.

## 3. Explain the implementation, then ask for decisions

Before writing this handoff, load the parent's installed `human-text` skill and applicable language reference unless they are already in context. Resolve a missing dependency with the user; do not silently install it. This use requires no session-wide or global style activation.

After permitted corrections and their checks/review, explain the current implementation before listing remaining findings, whether or not any remain. Base the explanation on the current code and observed results. Cover:

1. **What changed:** the behavior now implemented and how it differs from before. Identify the actual result, such as changed application behavior, a migration or a generated artifact; distinguish completed work from pending work.
2. **How it works:** explain the main path through the changed components and the important implementation choices in ordinary language. Explain technical terms where needed; a list of edits or agent actions is not an explanation of the mechanism.
3. **Where to look:** link the key files or symbols, say what each contributes and what the human should inspect there. Point out relevant behavior boundaries, assumptions, migrations or risks rather than listing every touched file.
4. **What was verified:** give the checks and observed results, important limits, and a brief account of automatic review corrections. Distinguish working code from an untested claim.
5. **What remains:** present unresolved findings, blockers and human decisions with evidence and meaningful options. If there are no remaining actionable review findings, say so for the reviewed scope; missing mandatory coverage still blocks readiness.

Use the project's language and presentation conventions. A small change needs a short explanation, not five compulsory headings. For a specification, explain the integrated result and how its slices fit together, not a log of subagent activity. Keep this in the conversation unless the user or project requires a separate report.

When required checks and mandatory independent-review coverage are complete for the current revision and no unresolved blocker remains, report **ready for human review**. Missing required sources, skills or evidence keep that gate blocked even if the reviewer found no defects in the available scope. This is a conversational handoff unless the project separately authorizes a tracker status update.

The human's decisions and feedback become constraints for the next implementation pass. Apply the agreed changes, run affected checks and obtain a fresh-context review carrying those answers and previous findings. Update the walkthrough for the new revision, focusing on what changed instead of repeating unchanged detail. A quiet reviewer or passing test does not replace human acceptance.

**Done when:** the handoff explains the implemented outcomes and mechanism, links the key code with inspection guidance, and states verification limits and every remaining finding or decision. While awaiting acceptance or a blocking decision, the task remains in review or blocked, not complete.

## 4. Record acceptance and stop or deliver as requested

Implementation is complete when required gates are satisfied and the human explicitly accepts the current reviewed revision, asks to commit that revision, or explicitly confirms the task is finished. A request for an intermediate/WIP commit is not acceptance; use project commit policy and continue the task. If the human ends incomplete work, report it as stopped with remaining scope, not successfully implemented.

Execute an authorized commit request under project commit rules. Acceptance alone does not request a commit or publication. Report actual commit status and keep push, PR/MR, merge and tracker transitions under their separate permissions.

**Done when:** the accepted or stopped state is clear, any requested authorized commit has an observed result, and remaining delivery actions are named without being performed implicitly.
