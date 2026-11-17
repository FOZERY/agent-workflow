# Delivery settings

Read when configuring or changing Git and delivery behavior. Check project instructions, contribution rules, branch protections, delivery procedures, hooks, templates and ownership rules first. Cite the source for each settled rule. Show proposed changes, unchanged rules and any conflicting sources. Leave the affected action blocked until its conflict is resolved.

## Permissions

Ask one question per unresolved action. Use only the applicable questions in each round:

- **Commit:** May the agent create commits? Identify the permitted repositories, branches and changes.
- **Push:** May the agent push? Identify the permitted remotes and branches.
- **Open PR/MR:** May the agent open a pull or merge request? Identify the repository and source and target branch rules.
- **Update PR/MR:** May the agent update an existing pull or merge request? Identify eligible requests and permitted updates.
- **Merge:** May the agent merge a pull or merge request? Identify the permitted targets and required approvals.
- **Deploy:** May the agent deploy? Identify how to select the release or revision and which environments are permitted.
- **Branch cleanup:** May the agent clean up branches? Distinguish local and remote branches. Identify eligible branches and required retention or deletion approvals.

For each question, name the action and offer its compatible options in the form or in chat:

- **Allowed under a standing rule:** The agent may do this only within explicit scope and conditions. Cite the rule or state the proposed conditions for approval.
- **Approval each time:** The agent asks the authorized approver before each instance of this action.
- **Human only:** The designated human role performs this action.
- **Other:** Describe the policy in your own words or link its authoritative source.

Record the actor and permission separately from the checkpoint. For each permitted action, record its scope, target-selection rule, conditions and checkpoint. Do not guess future targets. Permission for one action does not cover another. Task acceptance, passing checks, setup approval and installation do not grant delivery permission. If permission is unresolved, do not perform the action.

## Timing and safeguards

Ask about timing only where it remains open. For example: “When may authorized commits begin?” Offer compatible checkpoints, such as agreed milestones during implementation, after required checks and review pass, or after the user accepts the result. These are examples, not defaults. If none fits, ask for a custom checkpoint or source. Confirm whether intermediate commits are allowed if that is still open.

- **Commits:** Reuse rules for message language, convention, grouping and signing. Link accepted examples when useful.
- **Checks:** Keep existing checks, hooks and branch protections. Record what to do when a check or hook fails or is unavailable. Neither condition authorizes a bypass.
- **PR/MR content:** Keep the authoritative template, title and body requirements, evidence, task links and permitted closing keywords. Commit and PR-title conventions can differ.
- **Participants:** Use existing ownership and reviewer rules. Ask how to resolve missing ownership and whether the agent may propose or apply metadata.

Record the concise agreement under Git and delivery in root `AGENTS.md`. Add action-specific reading pointers to existing procedures. Create a supporting project document only when the agreed detail needs one.

Keep unrelated work and secrets out of commits. Preserve the client's approved selective-commit mechanism. Compare selected skills' commit, tracker and working-copy steps with these rules. Report each required action that the agreed rules do not permit.

**Done when:** each applicable action has a sourced rule or an explicit gap. Each permitted action has an actor, scope, target-selection rule and checkpoint. Unresolved permission, targets or checks have a stop condition. Setup has performed none of these actions.
