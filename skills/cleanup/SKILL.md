---
name: cleanup
description: Review obsolete project artifacts and perform an explicitly approved, recoverable cleanup.
disable-model-invocation: true
---

# Cleanup

Maintain working artifacts: research notes, temporary plans, task notes, handoffs, reports and generated diagrams. Start with a read-only review. Invoking this skill requests that review, not blanket permission to delete files. Prose editing and document restructuring are separate work.

## 1. Establish the scope

Read the applicable project instructions and their artifact, ownership and retention pointers. Identify the repository/worktree, requested artifact locations, active work and allowed actions. Reuse the configured layout; inspect `.docs/` where present rather than assuming it is the only artifact root.

Resolve paths and symlinks before including them. Keep inspection and changes within the permitted scope. Source code, dependencies, build caches, Git metadata and external systems are outside this artifact-cleanup procedure. Existing specs, tickets, instructions and legal records are authoritative inputs, not disposable working notes.

Use existing policy and the user's request to settle scope. Ask only about missing boundaries or permissions that affect the review. If retention is unspecified, assess individual candidates; propose any new retention rule separately instead of inventing an expiry period.

**Done when:** the artifact roots, ownership boundaries and applicable retention/approval rules are identified; inaccessible sources and unresolved boundaries are explicit.

## 2. Establish each candidate's lifecycle

Read candidate contents. Identify their purpose, associated task, current owner, status, unique information and any authoritative replacement. Verify status against available current sources. Age, a completed task, a `deprecated` label or a similar filename alone does not establish that a record can be discarded.

Trace incoming links, instruction pointers, indexes, embeds and image references within the accessible scope. Record where you searched; no matches in that scope do not prove that external readers have no references. For proposed moves, also account for outgoing relative links and companion assets. Compare supposed duplicates by content and purpose, not filenames.

Apply these distinctions:

- **Decision history:** retain accepted and superseded ADRs and their replacement links. Supersession is history, not a deletion signal. Follow any explicit project archiving procedure while preserving the decision record.
- **Recent context:** prune only under agreed retention. Preserve unresolved questions, next actions, task links and chronological timestamps. Preview the exact entries affected by partial pruning; do not invent event dates or silently summarize away open work.
- **Long-term lessons:** retain current durable knowledge regardless of age. Prune only demonstrably obsolete or redundant entries under the project's policy, keeping useful replacement pointers.
- **Working artifacts:** a verified replacement or expired project retention rule can support removal, but check unique findings, unresolved work and reference obligations first. Preserve unique information in place or in an approved archive; transferring it into another authoritative document needs an explicit plan.
- **Concurrent work:** leave another agent's or person's active artifacts unchanged. Untracked or ignored does not mean disposable. Unknown ownership or task status stays unresolved rather than becoming evidence for removal.

**Done when:** every proposed change has a sourced reason, identified reference impact and knowledge-preservation outcome. Uncertain candidates remain unchanged with the missing evidence stated.

## 3. Present the plan and obtain approval

Present the plan in the conversation; create a persistent report only if requested or required by project policy. For each proposed change show:

| Path or exact entries | Action | Evidence and retained source | Reference repairs | Recovery location |
| --- | --- | --- | --- | --- |

Choose keep, archive, move to Trash/quarantine, or prune specific entries. Explain important keep/blocked decisions as well. Expand directory proposals into their affected files so approval does not hide unrelated contents. Include any index, link or asset changes and any recovery copies in the same plan.

Ask the owner to approve the exact paths/entries and actions. Reuse explicit approval already covering that plan; review-only requests stop here. A generic request to clean the repository does not authorize the proposed deletion list, policy changes, external writes or publication.

**Done when:** the owner has selected an explicit change set, declined it, or received the requested review-only result. Proceed only with approved changes.

## 4. Apply approved changes recoverably

Before each change, check that the candidate and its ownership/reference assumptions still match the preview. If they changed, stop that action and refresh its plan; continue independent approved actions where safe. Preserve unrelated user edits.

Use system Trash or an approved recoverable archive/quarantine, with collision-safe destinations. Record original paths and destinations before moving files and keep a usable restoration map. Git history alone is not a backup, particularly for untracked files. Permanent deletion is outside this skill.

For approved in-place pruning or link repairs, retain an approved recovery copy before editing. Preserve chronology, source links and retained facts. Apply only the minimum reference repairs in the approved plan; this is not a prose rewrite or a workflow-policy migration. If a required reference cannot be repaired within that authority, leave the affected artifact in place and report the blocker.

Keep recovery material outside active artifact discovery where the project permits, and preserve existing tracking/ignore choices. Creating archives, editing ignore rules, changing shared memory or mutating remote records requires the corresponding approval; cleanup does not grant those permissions.

**Done when:** every attempted action has an observed result and a recovery path. On failure, report partial completion and leave unattempted files intact; do not claim rollback without performing it.

## 5. Verify and report

Check that retained instructions, indexes, task/decision links and diagram assets still resolve within the inspected scope. Check moved documents' relative links and run the project's narrow documentation/link check when available. Confirm recovery copies contain the original content, kept files were preserved and no approved item is silently missing from the outcome.

Report changed paths, retained/blocked candidates, checks performed, reference-check limits and the exact restoration method. Distinguish completed cleanup from recommendations and unverified external references. If nothing qualifies, report that result without manufacturing changes or a new report file.

**Done when:** each approved action is accounted for, the affected references are verified or their limitation is explicit, and the owner can recover every changed artifact.
