---
name: cleanup-artifacts
description: Review stale project artifacts and remove the approved ones recoverably.
disable-model-invocation: true
---

# Cleanup artifacts

Review working artifacts: research notes, temporary plans, task notes, handoffs, reports and generated diagrams. Start read-only. Running this skill gives no permission to delete: only the owner's approval of exact paths does. Leave text rewrites to `refactor-docs`.

## 1. Find the scope

1. Read the project instructions for artifact locations, owners and retention rules. If there are none, use `.docs/` and say so.
2. List the artifact folders. Check `.docs/` and every other configured location.
3. Resolve paths and symlinks.
4. Leave these out: source code, dependencies, build caches, `.git`, worktrees, folders that tools manage, and external systems.
5. Treat specs, tickets, instructions and legal records as sources, not as candidates.

If the project has no retention rule, judge each candidate on its own. Propose a new retention rule separately.

**Done when:** you know the artifact folders, their owners and the retention rules, and you named what you cannot read.

## 2. Check each candidate

1. Read the candidate. Find its purpose, task, owner, status, unique facts and any replacement.
2. Check its status against current sources. Age, a finished task, a `deprecated` label or a similar file name is not a reason to remove it.
3. Search for links to it: pointers, indexes, embeds and images. Write where you searched in the evidence column. No match in that scope does not prove that nobody outside uses it.
4. Compare supposed duplicates by content and purpose, not by file name.

Apply these rules by type:

- **ADRs:** keep accepted and superseded ADRs with their replacement links. Follow the project's archive procedure if it has one.
- **`CONTEXT.md`:** prune only under the agreed retention rule. Keep open questions, next actions, task links and dates. Show the exact entries before you prune.
- **`LESSONS.md`:** keep current lessons at any age. Prune only an entry that is shown to be obsolete or a duplicate.
- **Working artifacts:** remove one only after a verified replacement or an expired retention rule, and after its unique facts are kept somewhere.
- **Someone else's work:** leave an active artifact of another agent or person in place. Untracked or ignored files are not disposable. Unknown owner or status means keep.

**Done when:** each proposed change has a reason with its source, its link impact and the place where its unique facts stay. Each uncertain candidate stays, with the missing evidence named.

## 3. Show the plan and get approval

Show the plan in the chat. Write a report file only if the user or the project asks for one.

| Path or entries | Action | Evidence and kept source | Link repairs | Recovery location |
| --- | --- | --- | --- | --- |

1. List the candidates that you propose to change, and each kept candidate that the user could question. Use one action per row: keep, archive, move to Trash, or prune named entries. For a kept row, write `none` in the recovery column.
2. Expand a folder into its files.
3. Include every link repair and recovery copy in the plan.
4. If the user asked only for a review or a report, stop here. Otherwise ask the owner to approve the exact paths and actions.

A general request such as "clean the repository" does not approve the list.

**Done when:** the owner approved a change set, declined it, or got the review.

## 4. Apply the approved changes

1. Before each change, check that the candidate, its owner and its links still match the plan. If not, skip that action and update its plan.
2. Move files to the Trash or to an approved archive. Use destinations that cannot overwrite a file.
3. Record each original path and destination as a restore map.
4. Before you prune entries in place, save a recovery copy.
5. Make only the link repairs in the plan.

Git history is not a backup, especially for untracked files. This skill never deletes permanently. An archive, an ignore rule, shared memory or a remote record needs its own approval.

**Done when:** each action has an observed result and a recovery path. If an action failed, report what was done and what was not.

## 5. Check and report

1. Check that kept instructions, indexes, links and diagram assets still resolve.
2. Run the project's documentation or link check if it has one.
3. Check that each recovery copy has the original content.
4. Report the changed paths, the kept and blocked candidates, the checks and the restore method.

If nothing qualifies, say so. Make no change and no report file.
