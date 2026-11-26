---
name: writing-for-agents
description: Write or edit documents that agents read. Use when you create or change a skill, or edit AGENTS.md or CLAUDE.md.
---

# Writing for agents

Write a document that an agent follows the same way on every run. This skill decides what goes into the document and where. Write each sentence by the `writing-technical` skill.

## 1. Find the job

1. Look for a skill or a file that already does this job. If one exists, edit it instead of adding a new one.
2. Write down who reads the document, when it applies and what result it gives.
3. Give one skill one job. If two parts of the job start at different times or for different readers, make two skills.

**Done when:** you can state the job in one sentence.

## 2. Choose who starts the skill

- **The agent or another skill must start it.** Keep `description` with the cases when it applies. The description is in the agent's context in every session.
- **Only the user starts it.** Set `disable-model-invocation: true` and write a one-line description for a person. In Codex, also set `allow_implicit_invocation: false` under `policy` in `agents/openai.yaml`. Another skill cannot start a user-only skill.

Choose the user-only form unless the agent or another skill must start the skill.

## 3. Write the frontmatter

- Make `name` equal to the folder name.
- Start `description` with what the skill does. Then list each case when it applies, one case per trigger. Merge synonyms into one case.
- Keep in `description` only what decides whether to start the skill.

## 4. Write the body

- Write steps as a numbered list when the order matters, with one action per step. Add a `**Done when:**` line with a check as the last line of a step, only where the agent could stop too early without it.
- Write rules that apply at any time as a flat list.
- Tell the agent what to do. Give the reason only when the rule is unclear without it.
- Write the action to take. Keep a prohibition only for a hard limit, and put the action to take next to it.
- Move material that only some cases need into a file in the same folder. Point to it with its condition: "Read `X.md` when Y."
- Name another skill by its name or path. Do not restate its content.
- Point to facts that the agent can find, such as `package.json` scripts, config files and `--help` output. Write down only what the agent cannot find: an unwritten convention, a reason, a trap.
- Keep each fact in one place.

## 5. AGENTS.md and CLAUDE.md

- Every session reads the whole file. Keep only what applies to most tasks.
- Give each pointer its condition: "Read `X.md` when Y."
- Move procedures, standards and long lists into files, and point to them.
- Keep the file under the project's size limit.

## 6. Prune

Read every sentence and ask:

1. Does the agent act differently with this sentence than without it? If not, delete it.
2. Does this file or another skill already say it? Keep one place and point to it.
3. Can the agent find it in the environment? Point to the source.
4. Does it explain a reason? Keep it only if the rule is unclear without it.
5. Is it a prohibition? Rewrite it as the action to take.

If you are not sure, delete the sentence. Keep every limit that protects data, secrets or permissions.

**Done when:** every sentence passes all five questions.

## 7. Check

1. The frontmatter has `name` and `description`, `name` equals the folder name, and the invocation setting matches step 2.
2. Every link and every referenced file exists.
3. Every skill that the document starts exists, and the agent can start it.
4. If the repository lists its skills, for example in a README or a catalog, the list includes the change.

## 8. Test a procedure

If the document has steps, give a fresh subagent a small real task in a scratch repository or worktree. Forbid writes to trackers, remotes and the Trash, and tell it to assume the answer at each approval gate. Tell it to read the document in full and follow it. Compare its path with the steps. Fix each step where it took another path or stopped early.

Skip this step for a document that has only rules.

**Done when:** the run follows the steps, or you report why the test could not run.
