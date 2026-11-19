# Delivery settings

Read this file when you configure or change Git and delivery behavior.

1. First read the project instructions, contribution rules, branch protection, delivery procedures, hooks, templates and ownership rules.
2. For each rule that these sources settle, cite the source.
3. Show proposed changes, unchanged rules and conflicting sources.
4. Keep an action blocked until its conflict is resolved.

## Permissions

Ask one question for each open action. Ask only the questions that apply:

| Action | Question | Also identify |
| --- | --- | --- |
| Commit | Can the agent create commits? | Repositories, branches and changes |
| Push | Can the agent push? | Remotes and branches |
| Open PR/MR | Can the agent open a pull or merge request? | Repository, source and target branch rules |
| Update PR/MR | Can the agent update an existing request? | Which requests and which updates |
| Merge | Can the agent merge a request? | Targets and required approvals |
| Deploy | Can the agent deploy? | How to select the release or revision, and which environments |
| Branch cleanup | Can the agent clean up branches? | Local or remote, which branches, and the retention or deletion approvals |

For each question, offer these options:

- **Allowed by a standing rule:** the agent does the action within an explicit scope and conditions. Cite the rule, or state the proposed conditions for approval.
- **Approval each time:** the agent asks the approver before each action.
- **Human only:** a named human role does the action.
- **Other:** the user describes the policy or links its source.

Record for each permitted action:

1. The actor and the permission.
2. The scope, the rule that selects targets, and the conditions.
3. The checkpoint, recorded separately from the permission.

Rules for permissions:

- Record only targets that the rule selects. Guess no future targets.
- Permission for one action does not cover another.
- Task acceptance, passed checks, setup approval and installation grant no delivery permission.
- If a permission is open, the agent does not do the action.

## Timing and safeguards

1. If timing is open, ask, for example: "When can authorized commits begin?" Offer the checkpoints that fit: at agreed milestones during implementation, after the required checks and review pass, or after the user accepts the result. These are examples, not defaults.
2. If no checkpoint fits, ask for a custom checkpoint or its source.
3. If it is still open, ask whether intermediate commits are allowed.

Agree the safeguards that apply:

- **Commits:** reuse the rules for message language, convention, grouping and signing. Link accepted examples when they help.
- **Checks:** keep existing checks, hooks and branch protection. Record what the agent does when a check or hook fails or is unavailable. Neither case permits a bypass.
- **PR/MR content:** keep the template, the title and body rules, the evidence, task links and permitted closing keywords. Commit and PR title conventions can differ.
- **Participants:** use existing ownership and reviewer rules. Ask what to do when ownership is missing, and whether the agent can propose or set metadata.

## Record the agreement

1. Record a short agreement in `## Git and delivery` of the root `AGENTS.md`.
2. Add a reading pointer to each existing procedure, with its action as the trigger.
3. Create a separate project document only when the agreed detail needs one.
4. Keep unrelated work and secrets out of commits. Keep the client's approved way to commit selected changes.
5. Compare the commit, tracker and working-copy steps of the selected skills with these rules. Report each required step that the rules do not permit.

**Done when:** each applicable action has a sourced rule or a recorded gap. Each permitted action has an actor, a scope, a target rule and a checkpoint. Each open permission, target or check has a stop condition. Setup did none of these actions itself.
