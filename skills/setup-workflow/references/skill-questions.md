# Questions for optional skills

Read the part for a skill only when the user selects that skill or changes its settings.
Record each answer in the skill's section of the project's `AGENTS.md`.

## investigate

1. Ask: "Where does the agent find facts about a task? For each source, say how to open it, so that a new agent can use it. For example: git, merge requests, the tracker, the wiki, chats, logs, staging."
2. If the answer about a source is unclear, ask about that source.
3. Record each source in the user's words, with the steps to open it.
4. For a credential, record only the name of the variable or config that holds it.
5. If the user names production, ask whether the agent may read it.
6. Agree where the facts file lives. Default: `facts.md` with the other artifacts of the task.
7. Ask where the researchers run: in subagents (recommended) or in the current session. Record the answer as `execution`.
8. If they run in subagents, ask which agent, model and reasoning effort they use. Record the answer as `researcher`.

## verify

1. Ask: "After implementation, how do we check here that a feature works? For example: run it locally with test data, run the e2e path, check it in a test namespace, deploy to staging." Accept several answers for different kinds of change.
2. For each place, ask how the agent reaches it and which tools it uses, so that a new agent can repeat it. For example: the kubectl context, the browser tool, test users, the test queries of a migration.
3. For a credential, record only the name of the variable or config that holds it.
4. Ask which actions need the user's approval, for example a deploy to staging or writes to a shared environment. If the user names production, ask whether the agent may act there.
5. Check statically that the agent can reach each place and tool: the config entry, the context name, the command on `PATH`. A live probe needs the user's approval. Record each gap as a blocker of that place.
6. Record a short procedure in the `verify` section. Move a longer one to `<agent-docs>/project/verification.md`.

## to-plan

1. Agree the plan location and naming. Keep the plan with the other artifacts of its task where the project permits.
2. Ask about visibility. Offer only the allowed options: tracked in Git, ignored in the repository, or an approved private location.
3. Ask about approval. Options: the agent saves a draft for review (recommended), or the user approves the plan before the agent saves it. Use the project's procedure for other checkpoints.
4. Ask who can change an approved plan. Options: the agent within agreed limits, the agent with approval for each change, or the plan owner only.
5. Agree the executor that receives the plan. Check that it can take the plan and the source task without a new spec or tickets.

## Trackers: to-spec, to-tickets, wayfinder, implement

For `implement`, ask only when it updates the tickets of its tasks.

1. Ask which sources own the requirements and the tickets.
2. If `wayfinder` is selected, ask where its decision map belongs.
3. List the tracker operations that the selected skills need: read, create, edit, comment, label, assign, link, change state, close.
4. For each operation, ask for one option: allowed within a named scope, needs separate approval, or human only. Ask only about operations that the selected skills need.
5. Record that a readiness label does not authorize starting work or publishing.
6. If the project has no adequate tracker procedure, use the seed for the selected tracker:
   - [GitHub](issue-tracker-github.md)
   - [GitLab](issue-tracker-gitlab.md)
   - [Local Markdown](issue-tracker-local.md)
7. For another tracker, write the procedure from its agreed sources and access method.

Keep the readiness labels that the selected skills need. Setup does not configure incident triage.
Read [domain documents](domain.md) only when glossary or ADR conventions need configuration.
