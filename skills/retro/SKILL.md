---
name: retro
description: "Discuss a work session and preserve confirmed, reusable project lessons."
disable-model-invocation: true
---

# Retrospective

Turn the session's experience into useful project memory. This is a user-invoked discussion, not an automatic rule-writing or cleanup step.

## 1. Establish context and memory ownership

Read root `AGENTS.md` (or the project's `CLAUDE.md`) and its memory pointers. Locate `LESSONS.md` and `CONTEXT.md` in the configured agent-documentation directory, default `.docs/`. Preserve the fixed filenames. If their location or update permissions are unknown, agree them before writing; do not create a competing memory store.

Use the current session unless the user names another task, session or period. Consult the relevant conversation, task records, review findings and actual check results through the harness's permitted history/source access. State missing evidence; do not infer unseen events or scan unrelated private sessions.

Read relevant existing lessons and recent context to avoid duplicate conclusions and identify earlier unresolved questions. Check current project rules before treating remembered experience as applicable.

**Done when:** the discussion scope, available evidence, memory locations and writing authority are known.

## 2. Discuss what is worth retaining

Identify consequential decisions, mistakes, successful approaches and repeated friction. For each candidate, explain what happened, its evidence, why it matters next time and the conditions where it applies. Distinguish observed results from hypotheses; an owner's preference is a preference, not a universal engineering fact.

Useful questions include:

- Did task understanding or a decision prevent rework, or cause it?
- Were test scope, fixtures or infrastructure disproportionate to the agreed behavior?
- Did review, delegation or human checkpoints miss information or surface it too late?
- Was a source hard to find, an instruction ambiguous, or tooling unnecessarily expensive?
- Could an existing check or clearer pointer prevent a recurring mistake?

Discuss the most consequential candidates first and ask the user to confirm or correct the interpretation. Reuse already-confirmed decisions rather than asking for the same approval again. The absence of a hook or CI job is not itself a defect; propose automation only for an observed need within project constraints. Implementation and review both follow applicable coding rules.

**Done when:** each candidate is confirmed, rejected or explicitly unresolved, with its scope and rationale clear. No useful new lesson is a valid outcome.

## 3. Route and save agreed outcomes

Write each proposed entry following the installed `writing-for-agents` skill. Show the proposed updates and their destinations. Apply standing write permission only to the outcomes it covers; otherwise obtain approval. Invocation alone does not approve every proposed memory, policy or environment change.

- **`LESSONS.md`:** confirmed reusable experience and project preferences. Organize by topic and preserve the existing format. Each entry needs a date, source/task or owner confirmation, applicable conditions, concise lesson and current/superseded status. Merge with an equivalent entry rather than accumulating session summaries; clarify conflicts before replacing accepted conclusions.
- **`CONTEXT.md`:** a short chronological record of this retrospective, its actual date/time and timezone, task/topic, agreed outcome, unresolved questions and next action. Link to the lesson or authoritative decision instead of copying it. Keep uncertain candidates here for discussion, not as established long-term knowledge.
- **Project rules:** mandatory testing, review, workspace or permission changes belong in root `AGENTS.md` or their existing authoritative procedure. Propose them separately and edit only with the required approval. A lesson may retain the rationale and a pointer, not a competing rule.
- **ADRs, requirements and tasks:** consequential technical decisions and required product behavior keep their project-defined owners and locations. Preserve links; retrospective discussion does not automatically accept an ADR, rewrite a spec or create tracker work.

Use the agreed writer for shared memory and preserve concurrent changes. Keep entries brief, omit secrets and private transcripts, and avoid caching facts cheaply available in current configuration. Broader pruning, global preferences, skill edits, new hooks, services and external writes are separate changes, not side effects of saving a lesson.

If writing is forbidden or unavailable, return the proposed entries and exact intended destinations for the authorized person; do not claim they were saved.

**Done when:** approved outcomes are saved in their authoritative destinations or handed over as explicit proposals, with unresolved items preserved only where permitted.

## 4. Verify and close

Check saved entries against the agreed conclusions, their dates and source links. Confirm lessons contain durable experience rather than a transcript or hidden mandatory policy, and context contains the recent event rather than a second copy of the lesson. Check that no accepted rule was displaced by a remembered preference.

Report what was saved, updated, left unresolved or not written, with paths and any separately approved policy changes. Do not begin implementation, install tooling, commit or publish merely because the retrospective suggested an improvement.

**Done when:** the user can distinguish recorded lessons, recent context, accepted policy changes and remaining proposals.
