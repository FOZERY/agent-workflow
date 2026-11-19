# Core workflow rules

This file is the single source of the rules that apply to every project that uses this kit.
Setup copies the block below into the `## Workflow rules` section of the project's root `AGENTS.md`.
These rules are mandatory. They live only in `AGENTS.md`; skills and other project files point to them and do not repeat them.

## How setup uses this file

1. Copy the block between the `agent-workflow:core` markers, with the markers.
2. Replace each angle-bracket field with the value agreed in setup:
   - `<agent-docs>`: the agent-documentation directory, `.docs` by default.
   - `<phases>`: the phase list below, with only the selected skills. Remove a phase that has no selected skill, except Setup and Accept.
   - `<search>`: one of the two search variants below.
   - `<lessons>`: one of the two lessons variants below.
   - `<review-rounds>`: the agreed review round limit, `3` by default.
3. Keep all other text as written. To change a rule for every project, edit this file and increase the version in the marker.
4. On a rerun, compare the marker version in `AGENTS.md` with this file. If they differ, show the difference and replace only the block. Keep the user's text outside the markers.

### Phase list

Link each skill name to its section under `## Skills` in the project's `AGENTS.md`.

```markdown
1. **Setup.** `setup-workflow` configures this file. `home-repo-init` creates a multi-repository home.
2. **Clarify.** `grilling`, `grill-with-docs`, `wayfinder`, `research`, `prototype`, `domain-modeling`, `codebase-design`.
3. **Plan.** `to-plan`, `to-spec`, `to-tickets`.
4. **Implement.** `implement` for one session, `implement-with-swarm` for an architect with workers. `tdd` runs inside implementation.
5. **Review.** `code-review`.
6. **Accept.** The user accepts the work. Commit, push and other delivery follow `## Git and delivery`.
7. **Improve.** `retro`, `cleanup`, `refactor-docs`.
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
<!-- agent-workflow:core v1 -->
setup-workflow owns this section. To change it, run setup again.

### Workflow
A task moves through these phases. A ready task starts at Implement.
The `## Skills` section tells each skill how to work in this project.

<phases>

### Session start
Before your first reply in a session, read `<agent-docs>/CONTEXT.md` and `<agent-docs>/LESSONS.md`.
After a context compaction or a resumed session, read them again.
Check their facts against the current code and task sources before you act on them.

### Search
<search>

### Delegated workers
Give each subagent or worker the path to this file, the task sources and the skill paths it must follow.
Some harnesses do not load `AGENTS.md` into subagents.
A subagent launches its own subagents only where `## Skills` says the harness supports it.

### Blockers
If a required step cannot run, stop that step and tell the user what blocks it.
Continue the steps that do not depend on it.

### Done
Say that work is done only after you run the agreed checks. Give their actual result.

### Review rounds
If review follow-up allows fixes, fix findings and review again for at most <review-rounds> rounds. After the last round, stop and ask the user.

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
