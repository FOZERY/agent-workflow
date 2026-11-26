# Core workflow rules

This file is the single source of the rules that apply to every project that uses this kit.
Setup copies the block below into the `## Workflow rules` section of the project's root `AGENTS.md`.
These rules are mandatory. They live only in `AGENTS.md`; skills and other project files point to them and do not repeat them.

## How setup uses this file

1. Copy the block between the `agent-workflow:core` markers, with the markers.
2. Replace each angle-bracket field with the value agreed in setup:
   - `<agent-docs>`: the agent-documentation directory, `.docs` by default.
   - `<phases>`: the phase list below, with only the selected skills. Remove a phase that has no selected skill, except Setup and Accept.
   - `<search>`: one of the two search variants below, with the agreed agent and model in its own field.
   - `<lessons>`: one of the two lessons variants below.
3. Keep all other text as written. To change a rule for every project, edit this file and increase the version in the marker.
4. On a rerun, compare the marker version in `AGENTS.md` with this file. If they differ, show the difference. After approval, replace only the block. Keep the user's text outside the markers.

### Phase list

Link each skill name that has a section under `## Skills` in the project's `AGENTS.md` to that section.

```markdown
1. **Setup.** `setup-workflow` configures this file. `setup-home-repo` creates a multi-repository home.
2. **Clarify.** `investigate`, `grilling`, `grill-with-docs`, `wayfinder`, `research`, `prototype`, `domain-modeling`.
3. **Plan.** `to-plan`, `to-spec`, `to-tickets`.
4. **Implement.** `implement`: the session is the orchestrator. It writes small changes itself and gives larger ones to workers. `tdd` and `simplify-codebase` run inside implementation.
5. **Review.** `code-review`: the worker checks the Standards axis, the orchestrator checks the Spec axis.
6. **Accept.** The user accepts the work. Commit, push and other delivery follow `## Git and delivery`.
7. **Improve.** `retro`, `cleanup-artifacts`, `refactor-codebase`, `refactor-docs`.
```

### Search variants

Subagent, with the agent and model agreed in setup:

```markdown
Send bulk read-only lookups to a search subagent: searches across many files or folders, long logs and test output, web and documentation searches.
Use <agent and model agreed in setup>. If it is not available, pick the first available of:
1. A search or research agent that the user defined in this harness.
2. The harness's built-in search role, such as Explore in Claude Code or scout in OMP.
3. A general subagent on the cheapest model that the harness offers.
Give the subagent the question and the scope. Ask for a short answer with paths and line numbers.
Do a lookup yourself when it takes one or two commands or when no subagent is available.
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

## Block

```markdown
<!-- agent-workflow:core v7 -->
setup-workflow owns this section. To change it, run setup again.

### Workflow
A task moves through these phases. A ready task starts at Implement.
If `## Skills` has an `implement` section, start the `implement` skill first when you begin to change code for a task. A trivial edit, such as a typo, does not need it.
The `## Skills` section tells each skill how to work in this project.

<phases>

### Skill settings
A skill section under `## Skills` can set these values:
- `trigger`: `auto` means `implement` starts the skill at its stage. `manual` means the user starts it.
- `execution`: where the skill runs. Values: `current-session`, `subagent` or `separate-session`. A separate session is a new session, or a handoff that the user starts. This value grants no permission to delegate.
- `skill`: the installed path of the skill's `SKILL.md`, for each client. A subagent that runs the skill reads this file.
- `worker`: the agent, model and reasoning effort of the `implement` workers.
- `researcher`: the agent, model and reasoning effort of the `investigate` researchers.
- `finder`: the agent, model and reasoning effort of the `simplify-codebase` finder.
- `standards-reviewer`, `spec-reviewer`: the agent, model and reasoning effort of each `code-review` axis.
- `followup`: `report` means return the findings and wait. `fix-and-rereview` means fix the authorized findings and review again.
- `rounds`: the limit for `fix-and-rereview`. See Review rounds.

### Questions
When the user must decide or answer, ask through the harness's question tool, such as `AskUserQuestion` in Claude Code. Put all open questions of one round into one call. Give each question its options and the effect of each, and make it readable without the text above it.
Ask in plain text only when the harness has no question tool, for example in a headless run.

### Session start
Before your first reply in a session, read `<agent-docs>/CONTEXT.md` and `<agent-docs>/LESSONS.md`.
After a context compaction or a resumed session, read them again.
Check their facts against the current code and task sources before you act on them.

### Search
<search>

### Delegated workers
Give each subagent or worker the path to this file, the task sources and the skill paths it must follow.
To run a skill in a subagent, give it the path to that skill's `SKILL.md` from the skill's section under `## Skills`. Tell it to read the file in full and follow it. Pass the inputs the skill needs, such as the scope, the base and the task sources. Do not summarize the skill in the brief.
Some harnesses do not load `AGENTS.md` into subagents.
A subagent launches its own subagents only where `## Skills` says the harness supports it.

### Blockers
If a required step cannot run, stop that step and tell the user what blocks it.
Continue the steps that do not depend on it.

### Done
Say that work is done only after you run the agreed checks. Give their actual result.

### Editing this file
Before you write or edit this file, read the installed `writing-docs` and `writing-for-agents` skills unless they are already in context. Apply both.
Keep this file under 300 lines. Put project details in `<agent-docs>/project/` and link them with a trigger.

### Review rounds
If review follow-up allows fixes, fix findings and review again, up to the `rounds` value of the `code-review` section. After the last round, stop and ask the user. A worker reports its open findings to the orchestrator, and the orchestrator asks the user.

### Session end
Before a handoff, a context boundary or the end of a task, update `<agent-docs>/CONTEXT.md` within the agreed update authority: what changed, what is open, what comes next.

### Lessons
Record a lesson in `<agent-docs>/LESSONS.md` when one of these happens:
- The user settles a disputed question and says which answer is right.
- The user corrects your approach.
- The same problem appears a second time.
<lessons>
Keep `LESSONS.md` short: every session reads all of it.
<!-- /agent-workflow:core -->
```
