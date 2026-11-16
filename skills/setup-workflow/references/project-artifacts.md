# Core project artifacts

Read on initial setup and when changing instruction ownership, project memory, its loading or retention. These three artifacts are part of repository preparation, independent of which optional skills are selected.

## Layout and instruction loading

Choose one project agent-documentation directory, defaulting to `.docs/`. The owner may change the directory, but the workflow's memory filenames are fixed: `CONTEXT.md` and `LESSONS.md`, directly inside it. Root `AGENTS.md` stays at the repository root. The default layout is:

```text
AGENTS.md
.docs/
  CONTEXT.md
  LESSONS.md
```

Reuse existing `CONTEXT.md` and `LESSONS.md` at the selected directory only when their declared roles match this contract. For differently named records or conflicting contents, agree preservation and any migration before writing; they are source material, not alternative canonical filenames. Preserve accepted facts and existing policy, and never overwrite or rename records merely to fit the layout. If the required layout is forbidden, report that setup gap for an owner decision rather than silently choosing other filenames or creating competing memory stores.

Root `AGENTS.md` holds the configured workflow contract, using the semantic sections in the setup skill's draft step. Keep mandatory permissions visible there or link applicable existing procedures. Context and lessons are memory, not additional policy owners. Use the selected agent-documentation directory for new supporting detail when useful, without automatically moving established sources.

Establish how each selected client loads root `AGENTS.md`:

| Client | How root `AGENTS.md` loads |
| --- | --- |
| Codex | Natively. |
| Claude Code | Natively from v2.1.277, but only when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` exists in the working directory or above. When one exists, or the session cannot read `AGENTS.md`, add the line `@AGENTS.md` to the project's `CLAUDE.md`. See [Claude Code memory](https://code.claude.com/docs/en/memory). |
| OMP | Natively in the main session. Task subagents do not receive it; see [writing activation](human-text.md#discover-and-plan). |

Preserve existing client wrappers and add only the import or pointer the table requires. If another file already owns shared instructions, resolve ownership with the owner before changing it; do not duplicate policies or silently move them. If shared instructions cannot change, agree an allowed local mechanism and report the limitation. Preview client integration edits separately from installation effects and label loading unverified where it cannot be observed.

Put the memory pointers below in root `AGENTS.md` with concrete repository-root-relative paths. In this reference, `<agent-docs>` means the selected directory, not a literal output path. Substitute its actual name; retain the two fixed filenames.

| Reading trigger | Target and purpose |
| --- | --- |
| Starting or resuming a task session | Read `<agent-docs>/CONTEXT.md` to recover recent work, decisions, open questions and next actions; verify task/code state against current sources. |
| Before recommending an approach or making a choice to which prior experience applies | Read relevant topics in `<agent-docs>/LESSONS.md`; inspect its topic headings first when relevance is unknown. |
| Before changing domain or architectural behavior | Follow the project's domain pointer to the relevant glossary and accepted ADRs, where those sources exist. |

These are task-boundary or decision triggers, not instructions to reload every document on every turn.

Only when the owner opts into session-wide `human-text`, add the short session-start trigger from [writing activation](human-text.md) to root `AGENTS.md` or the explicitly selected global source, after installation. Preserve document formats and approval rules without copying the style guide. A selected skill's required style dependency is a separate package decision; it does not authorize this pointer or add calls to unrelated skills.

## CONTEXT.md: recent conversation continuity

Maintain a concise chronological sequence, oldest first, appending newer entries. Each entry records:

- The actual date and time, including timezone, and task identifier/link when applicable; otherwise a clear discussion topic.
- What was discussed or done and its observed outcome. Distinguish completed work from intended work, and confirmed decisions from proposals.
- Open questions, blockers and the next action or discussion, where relevant.
- Pointers to authoritative tasks, decisions, lessons and evidence instead of copied transcripts or duplicate policy.

Read it on session start/resumption and update at the agreed checkpoints, including before an approved handoff or context boundary. Agree the writer, update permission and retention during setup. Condense older material under the agreed policy while preserving unresolved items and source links. A summary records its creation time and covered period rather than inventing event timestamps. Context records what happened; it neither grants permissions nor proves the present code state.

## LESSONS.md: curated long-term project memory

Organize by topic, not by session. Retain confirmed project-specific preferences, durable agreements that are not mandatory procedures, and verified practical lessons worth reusing. Each entry identifies its date, source/task or explicit owner confirmation, applicable scope/conditions, and whether it remains current. Label any retained superseded item and point to its replacement; otherwise prune obsolete material under the agreed retention policy.

Use these entries to inform choices within current requirements and mandatory project rules. New behavior constraints belong in the workflow contract or the applicable procedure after its required approval. Keep general personal preferences in their existing global source rather than copying them into every project. Cache unwritten experience and rationale, not facts cheaply discoverable from configuration or current code.

Record accepted preferences as the owner's preferences, not universal engineering facts. Keep unconfirmed guesses and tentative lessons in recent context for discussion instead of promoting them to durable memory. When a record becomes an ADR, requirement or mandatory rule, its authoritative content moves to that source; retain only a useful pointer in lessons.

## Routing and update authority

When the owner says "remember this", classify the content and scope. Clarify only a genuinely ambiguous destination, applicability or authorization:

| Content | Authoritative destination |
| --- | --- |
| Recent discussion, unfinished thought or next action | `<agent-docs>/CONTEXT.md` |
| Confirmed project preference or verified reusable experience | `<agent-docs>/LESSONS.md` |
| Mandatory workflow, workspace, permission or repository rule | Root `AGENTS.md` or the applicable existing procedure |
| Consequential technical decision with meaningful alternatives and trade-offs | The approved ADR location, using the project's decision/approval process |
| Required product behavior or work to perform | The authoritative specification or task tracker |

A retrospective produces candidates, not automatically accepted rules. Save approved outcomes to the appropriate destination, and leave unresolved proposals in context. Prefer a deterministic check for a mechanically detectable mistake where authorized; memory is not a substitute for that check.

Agree who writes each artifact and when. With concurrent agents, default to one coordinating writer for shared context and lessons; other agents send sourced findings to that writer. Agree whether routine context updates and recording already-confirmed lessons have standing permission, and what requires fresh approval. Memory configuration does not authorize global client-setting changes, external writes or broader filesystem access. Omit secrets and full private transcripts. Resolve material conflicts with the owner rather than silently replacing a rule with a remembered preference.

## Initial creation and reconfiguration

After approval, follow the installed `writing-for-agents` skill to create or update root `AGENTS.md` and necessary client integration, and create/reuse `CONTEXT.md` and `LESSONS.md` in the selected directory. Seed context with the actual discussion and remaining questions; populate lessons only with confirmed durable items. If there are none, use a heading and an explicit statement that none have been confirmed. Agree tracked, project-ignored or local-only visibility for each affected file.

Check that every intended reader can reach the referenced artifacts. Use an allowed local loading pointer for a local-only setup rather than publishing a shared pointer to private files.

On reruns, preserve existing chronology and accepted lessons. Show the configured directory, missing files and loading/ownership gaps before asking what to change. A directory change is a migration requiring approval for affected paths and pointers; preserve history and resolve destination collisions first. File renaming is not a configuration option. Unapproved migration, conflicting ownership or forbidden writes block only the affected actions; report them without resetting history or creating duplicate stores.
