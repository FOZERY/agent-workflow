# Core workflow rules

This file is the single source of the rules that apply to every project that uses this kit.
Setup copies the block below into the `## Workflow rules` section of the project's root `AGENTS.md`.
These rules are mandatory. They live only in `AGENTS.md`; skills and other project files point to them and do not repeat them.

## How setup uses this file

1. Copy the block between the `agent-workflow:core` markers, with the markers.
2. Replace each angle-bracket field with the value agreed in setup:
   - `<agent-docs>`: the agent-documentation directory, `.docs` by default.
   - `<phases>`: the phase list below, with only the selected skills. Always keep `setup-workflow` in Setup. Remove a phase that has no selected skill, except Setup and Accept.
   - `<search>`: one of the two search variants below, with the agreed agent and model in its own field.
   - `<lessons>`: one of the two lessons variants below.
3. Keep all other text as written. To change a rule for every project, edit this file and increase the version in the marker.
4. On a rerun, compare the marker version in `AGENTS.md` with this file. If they differ, show the difference. After approval, replace only the block. Keep the user's text outside the markers.

### Phase list

Link each skill name that has a section under `## Skills` in the project's `AGENTS.md` to that section.

```markdown
1. **Setup.** `setup-workflow` configures this file. `setup-home-repo` creates a multi-repository home. `ask-workflow` recommends the next skill.
2. **Clarify.** `investigate`, `recall`, `grilling`, `grill-with-docs`, `wayfinder`, `research`, `prototype`, `domain-modeling`, `draw-diagram`.
3. **Plan.** `to-plan`, `to-spec`, `to-tickets`.
4. **Implement.** `implement`, with `tdd`, `simplify-codebase` and `verify` inside it.
5. **Review.** `code-review`, run by `implement`.
6. **Accept.** The user accepts the work. Commit, push and other delivery follow `## Git and delivery`.
7. **Improve.** `retro`, `cleanup-artifacts`, `refactor-codebase`, `refactor-docs`.
```

### Search variants

Subagent, with the agent and model agreed in setup:

```markdown
Send bulk read-only lookups to <agent and model agreed in setup>: searches across many files, long logs, web and documentation. If it is not available, use the cheapest search subagent of the harness. Ask for a short answer with paths and line numbers.
Do a lookup of one or two commands yourself.
```

Current session:

```markdown
Do searches in the current session.
```

### Lessons variants

The agent asks first:

```markdown
Propose the entry to the user. Write it only after the user confirms it.
```

The agent decides:

```markdown
Write the entry yourself. In the same reply, tell the user which entry you added, so that the user can remove it.
```

## Skill settings

A skill section under `## Skills` of a project's `AGENTS.md` can set these values. Write only the value in `AGENTS.md`. Each skill that reads a setting says how it acts on it.

- `trigger`: `auto` means `implement` starts the skill at its stage. `manual` means the step is off by default; the user starts the skill or turns the step on in `implement`.
- `execution`: where the skill runs: `current-session` or `subagent`. This value grants no permission to delegate.
- `skill`: the installed path of the skill's `SKILL.md`, for each client. A subagent that runs the skill reads this file.
- `worker`: the agent, model and reasoning effort of the `implement` workers.
- `researcher`: the agent, model and reasoning effort of the `investigate` researchers.
- `test-writer`: the agent, model and reasoning effort of the `tdd` subagent.
- `verifier`: the agent, model and reasoning effort of the `verify` subagent.
- `finder`: the agent, model and reasoning effort of the `simplify-codebase` finder.
- `standards-reviewer`, `spec-reviewer`: the agent, model and reasoning effort of each `code-review` axis.
- `followup`: `report` means return the findings and wait. `fix-and-rereview` means fix the authorized findings and review again.
- `rounds`: the limit of fix-and-review rounds for each review of a task. After the last round, the agent stops and asks the user.

## Block

```markdown
<!-- agent-workflow:core v11 -->
setup-workflow owns this section. To change it, run setup again.

### Workflow
A task moves through these phases. A ready task starts at Implement.
When you begin to change code for a task, start `implement` if `## Skills` has its section. A trivial edit, such as a typo, does not need it.
Before you run a skill, read its section under `## Skills`. The section wins over the skill's defaults.

<phases>

### Questions
When the user must decide, ask through the harness's question tool, such as `AskUserQuestion` in Claude Code. Put all questions of one round into one call, each with its options. Ask in plain text only when there is no question tool.

### Session start
Before your first reply, and again after a compaction or a resume, read `<agent-docs>/CONTEXT.md` and `<agent-docs>/LESSONS.md`. Check their facts against the code and the task sources before you act on them. They never override requirements, accepted decisions or mandatory rules.

### Search
<search>

### Delegated work
Give each subagent and worker the path to this file, the task sources and the `SKILL.md` paths that it must follow. Some harnesses do not load `AGENTS.md` into subagents.
A subagent launches its own subagents only where `## Skills` says that the harness supports it.

### Blockers and done
If a required step cannot run, stop it, tell the user what blocks it and continue the steps that do not depend on it.
Say that work is done only after you run the agreed checks. Give their actual result and the evidence.

### Memory
Before a handoff, a context boundary or the end of a task, update `<agent-docs>/CONTEXT.md` within the agreed authority: what changed, what is open, what comes next.
Record a lesson in `<agent-docs>/LESSONS.md` when the user settles a disputed question, when the user corrects your approach, or when the same problem appears a second time. <lessons> Keep `LESSONS.md` short.
Subagents and `implement` workers do not write these files. They report to the session that started them.

### Editing this file
Before you edit this file, read the installed `writing-technical` and `writing-for-agents` skills. Keep it under 300 lines. Put project details in `<agent-docs>/project/` and link them with a trigger.
<!-- /agent-workflow:core -->
```
