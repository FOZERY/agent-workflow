# Core project artifacts

Read this file on an initial setup and when you change the instruction owner, project memory, its loading or its retention.
Every project has these three artifacts, whatever skills the user selects: the root `AGENTS.md`, `CONTEXT.md` and `LESSONS.md`.

## Layout

The agent-documentation directory is `.docs/` by default. The owner can choose another directory.
The memory filenames are fixed: `CONTEXT.md` and `LESSONS.md`, directly in that directory. `AGENTS.md` stays at the repository root.

```text
AGENTS.md
.docs/
  CONTEXT.md
  LESSONS.md
  project/        long project rules, see the AGENTS.md structure
```

In this file, `<agent-docs>` means the selected directory. In `AGENTS.md`, write its real path from the repository root.

Existing memory files:

1. If `CONTEXT.md` and `LESSONS.md` already exist in the selected directory and their roles match this file, reuse them.
2. If memory records have other names or conflicting content, agree with the owner how to keep them and whether to migrate them before you write. Use them as source material. Keep their accepted facts and policy.
3. Keep existing records as they are. Overwrite or rename a record only after the owner approves a migration.
4. If the project forbids the required layout, report the gap to the owner. Create no other memory files in its place.

## AGENTS.md

`AGENTS.md` holds the workflow contract. Use the sections from [the AGENTS.md structure](AGENTS.md).

- Keep mandatory permissions in `AGENTS.md`, or link the existing procedures that hold them.
- `CONTEXT.md` and `LESSONS.md` are memory. They hold no policy.
- Put detailed project rules in `<agent-docs>/project/`, as [the AGENTS.md structure](AGENTS.md#project-files) describes. Leave established sources where they are. A move needs approval.

Implementation plans are task artifacts, not memory. A remote requirement stays authoritative: link it from the plan and do not copy it. For `to-plan` settings, use [skill questions](skill-questions.md#to-plan).

## Client loading

Find out how each selected client loads the root `AGENTS.md`. Use the user-wide column only when the user selected global changes in [writing routes](writing.md#instruction-loading).

| Client | How it loads the project `AGENTS.md` | User-wide instruction source |
| --- | --- | --- |
| Codex | Natively. | The first non-empty `AGENTS.override.md` or `AGENTS.md` under the effective `CODEX_HOME`. See [instruction discovery](https://developers.openai.com/codex/guides/agents-md/). |
| Claude Code | Natively from v2.1.277, but only when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` exists in the working directory or above it. If one exists, or the session cannot read `AGENTS.md`, add the line `@AGENTS.md` to the project's `CLAUDE.md`. | The loaded user instructions, normally `~/.claude/CLAUDE.md`. Follow configured directories and imports. |
| OMP | Natively in the main session. Task subagents do not get it. | The native agent-directory instructions, normally under `~/.omp/agent`. Follow profiles and `PI_CODING_AGENT_DIR`. Check client behavior before you rely on precedence. |

For Claude Code, see [Claude Code memory](https://code.claude.com/docs/en/memory).

1. Keep existing client wrappers. Add only the import or pointer that the table requires.
2. If another file already owns the shared instructions, agree the owner with the user before you change it. Keep each policy in one place.
3. If the shared instructions cannot change, agree an allowed local mechanism and report the limitation.
4. Show client loading edits separately from installation. If you cannot observe that loading works, mark it as not verified.

## Reading triggers

The [core rules](core-rules.md) block tells the agent when to read memory. Keep that rule only there.

Add this pointer to `AGENTS.md` where the project has domain sources: before a change to domain or architectural behavior, read the relevant glossary and accepted ADRs.

## Multi-repository homes

A home repository coordinates related repositories. Their code, history, trackers and repository rules stay in the child repositories.

1. Use `setup-home-repo` only when the user asks to create a home or migrate material. Setup keeps the existing navigation and ownership.
2. In a home, configure only the shared procedures and sources agreed for its scope. Child test commands, exceptions and domain records stay with their owners.
3. Before work in a child, the agent reads the child's instructions. If home and child procedures conflict, resolve it with the owner. The home does not override the child by default.
4. Agree where cross-repository task artifacts live and who writes them. A shared plan links child tasks and contracts and does not copy their requirements.
5. Home memory records coordinated work. Each child keeps its own memory and history unless the owner approves a migration.
6. Check access and loading from the home, from each selected child session and from delegated workers. A navigation pointer does not load a sibling's instructions or skills. Add explicit pointers or deployments where needed.
7. Use portable paths for team layouts. Keep machine-specific paths in approved local configuration.
8. Record a missing repository as a navigation gap. A clone URL does not permit clone, pull, worktree creation or publication.
9. Keep related-repository pointers in the contract. Configure only the requested scope. Create no empty artifacts in the children.

## CONTEXT.md

`CONTEXT.md` keeps recent work between sessions. Write entries in time order, oldest first, and add new entries at the end. Each entry has:

- The actual date and time with time zone, and the task ID or link. If there is no task, a clear topic.
- What was discussed or done, and the observed result. Keep done work apart from planned work, and decisions apart from proposals.
- Open questions, blockers and the next action, where they exist.
- Pointers to tasks, decisions, lessons and evidence. No copied transcripts or policy.

Update the file at the agreed checkpoints and within the agreed write authority. The core rules add one checkpoint: before a handoff, a context boundary or the end of a task.
Condense old entries by the agreed retention rule. Keep open items and source links. A summary records when it was written and which period it covers.
`CONTEXT.md` records what happened. It grants no permissions and does not prove the current state of the code.

## LESSONS.md

`LESSONS.md` keeps long-term project experience. Every session reads all of it, so keep it short.

1. Group entries by topic, not by session.
2. Keep project preferences that the owner confirmed, durable agreements that are not mandatory procedures, and verified lessons worth reuse.
3. Write a lesson in the cases listed in the core rules: the user settled a disputed question, the user corrected the agent, or a problem appeared a second time. Keep other guesses in `CONTEXT.md` for discussion.
4. Each entry has its date, its source (task or owner confirmation), where it applies, and whether it is still current.
5. Mark a superseded entry and point to its replacement, or remove it by the retention rule.
6. Record preferences as the owner's preferences, not as general engineering facts.
7. Record experience and reasons that the code and configuration do not show. Leave out facts that one look at the code gives.
8. Keep general personal preferences in their global source. Do not copy them into each project.
9. When a lesson becomes an ADR, a requirement or a mandatory rule, move its content there. Keep only a pointer in `LESSONS.md`.
10. A new constraint on agent behavior goes into `AGENTS.md` or the relevant procedure after approval, not into `LESSONS.md`.

## Where content goes

When the owner says "remember this", decide the destination from the content. Ask only if the destination, scope or permission is unclear.

| Content | Destination |
| --- | --- |
| Recent discussion, unfinished thought, next action | `<agent-docs>/CONTEXT.md` |
| Confirmed project preference or verified reusable experience | `<agent-docs>/LESSONS.md` |
| Mandatory workflow, workspace, permission or repository rule | Root `AGENTS.md` or the existing procedure |
| Technical decision with real alternatives and trade-offs | The approved ADR location, through the project's decision process |
| Required product behavior or work to do | The specification or task tracker |
| Approach, ordered work and checks for an existing task | The task's implementation plan |

A retrospective gives proposals, not accepted rules. Save approved outcomes to their destination. Keep open proposals in `CONTEXT.md`.
If a mistake can be detected mechanically, prefer an automatic check where permitted. Memory does not replace that check.

## Memory decisions

Agree each decision separately for `CONTEXT.md` and for `LESSONS.md`:

| Decision | Options |
| --- | --- |
| Writer | The owner, the coordinating agent, or a named maintainer. |
| Agent update authority | Standing permission for agreed routine updates, approval for each update, or no agent writes. For standing permission, record what it covers and what still needs approval. For lessons, this is the lessons variant in [core rules](core-rules.md): the agent asks first, or the agent writes and tells the user. |
| Git visibility | Tracked; untracked with a shared ignore rule; or untracked with a local-only exclusion. This choice does not permit a commit, publication or a tracking change to an existing file. |

1. Agree the update checkpoints and the retention rule for each file, in the project's terms or by a link to its procedure.
2. With several agents at the same time, one coordinating agent writes the memory. The other agents send it their findings with sources.
3. Memory settings do not permit global client changes, external writes or wider file access.
4. Keep secrets and full private transcripts out of memory.
5. If a remembered preference conflicts with a rule, resolve it with the owner. The rule stays until the owner decides.

## Initial setup and reruns

Initial setup, after approval:

1. Create or update the root `AGENTS.md` and the needed client loading.
2. Create or reuse `CONTEXT.md` and `LESSONS.md` in the selected directory. Follow the project's writing rules and the agreed Git visibility of each file.
3. Fill `CONTEXT.md` from the actual setup discussion and its open questions.
4. Fill `LESSONS.md` only with confirmed durable items. If there are none, write that no lessons are confirmed yet.
5. Configure the task artifact paths. Create plans, specifications and tickets only when a task needs them.
6. Check that every intended reader can open the referenced artifacts. For a local-only setup, use an allowed local pointer. Keep pointers to private files out of shared files.

Rerun:

1. Keep the existing history and accepted lessons.
2. Show the configured directory, missing files and loading or ownership gaps. Then ask what to change.
3. A directory change is a migration. Get approval for the affected paths and pointers, keep the history and resolve name collisions first.
4. The memory filenames stay fixed.
5. An unapproved migration, an ownership conflict or a forbidden write blocks only its own action. Report it. Keep the history and create no second memory store.
