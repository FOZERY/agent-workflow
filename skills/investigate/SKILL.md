---
name: investigate
description: "Study a task or a part of the code before work: find where it came from and how the code works, save the facts and explain them in plain words."
argument-hint: "[task reference, link or question]"
disable-model-invocation: true
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

# Investigate

Study a task before the user discusses or plans it. Subagents gather the facts. You save the facts in a file and explain the task to the user in plain words, as to a senior engineer who does not know this system. Leave the code, the tracker and other records unchanged.

## 1. Pin the question

1. Read the task, ticket, link or question from the user. If the user gives a ticket reference, fetch the ticket and state its title.
2. Write the question in one sentence. For a task: what must change and why. For a part of the code: what the user wants to understand.
3. Read the `investigate` section of `AGENTS.md` for the history sources and how to reach each one. If there is no section, use the git history and the code, and say so.

**Done when:** you have the question in one sentence and the list of sources.

## 2. Send the researchers

If the `execution` setting is `current-session`, or subagents are not available, do both parts yourself by [RESEARCHER.md](RESEARCHER.md). Otherwise:

1. Start two subagents with a fresh context, in parallel, with the agent from the `researcher` setting. Give each one the question, the task link, the sources and the absolute path of `RESEARCHER.md`. Tell it to read that file in full and do its part.
   - The history researcher does the part "History".
   - The code researcher does the part "Code".
2. For a small question about one place, start one subagent for both parts.

**Done when:** each report came back, or you know which one is missing and why.

## 3. Save the facts

Combine the reports into one facts file. Keep every source link and every `inference` mark. Add no fact that no report has. If two reports or sources disagree, keep both with their sources and add the conflict to the open questions.

- For a task, save `facts.md` with the other artifacts of the task, where `to-plan` saves its plan. The default is `<agent-docs>/<task-slug>/facts.md`, where `<agent-docs>` is the project's agent-docs directory, `.docs` by default. If the file exists, update it.
- For a question without a task, save the file only if the user asks.

Use these sections, and drop an empty one:

1. **Task:** what is asked, with the source link.
2. **Origin:** where the task came from, related tickets and discussions.
3. **How the code works now:** modules, flow, the place for the change and what depends on it.
4. **Why it is this way:** decisions and their reasons, with sources.
5. **Tried before:** earlier attempts, reverts and open bugs.
6. **Open questions:** risks, and what the sources do not answer.

**Done when:** every fact in the file has a source or an `inference` mark.

## 4. Explain

1. Start with the essence of the task in two or three sentences. If the facts contradict the user's question, say that first.
2. Explain how the part of the system works, then why it is this way. For a task, add how you would approach it.
3. Write the explanation by the `writing-for-people` skill if it is installed.
4. For a flow with three or more parts, draw Mermaid diagrams in steps. Each next diagram adds one part to the one before.
5. Say "inference" wherever the facts file marks one.
6. Give the short answer first. Go deeper when the user asks.
7. End with the open questions and the path of the facts file.

If a researcher reported a source that took many manual steps, or you reached one that way, propose a script for it to the user:

- what it takes and returns, for example a service and a time range in, the logs as JSON out;
- what it calls: the source's API or CLI first, browser automation only when there is no API;
- where it lives: the project's scripts folder, or one that the user names.

Write the script only after the user approves. Read credentials only from the variables or the config that the `investigate` section names. Then add one line to that section: the source that the script opens, and its command.

Stop after the explanation. The user chooses the next step, for example `grilling`, `to-plan` or `implement`.
