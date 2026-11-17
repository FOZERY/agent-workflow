# Migration safeguards

Read this reference before planning copies, migrations, or removals.
A **copy** retains current authority unless approved otherwise. A **migration** changes authority and updates its consumers.

## Plan the change

Identify references outside the home among each item's consumers.
For packages, compare the complete selected file set, not only `SKILL.md`.
Add the source revision or content fingerprint, consumer updates, and recovery location to the plan row.
Resolve destination conflicts through an approved merge, alternate destination, or exclusion.

An approved package copy must retain internal references, assets, and legal notices.
Check redistribution terms. An absent license does not grant redistribution rights.
Package links must stay within authorized roots. If a required component is secret or inaccessible, block the row rather than copy an incomplete package.

## Apply without losing originals

Include source fingerprints and revisions in the pre-write state check.
Create the destination while retaining the original, then compare it against the approved source or reconciled result.
Update approved consumer pointers and verify their supported loading mechanisms from each actual start location and worktree/sandbox.
Existing authority remains until the approved replacement and its required consumer changes succeed.

Record the source branch/revision for child edits. A branch does not preserve untracked or uncommitted source content.
If dirty state prevents a safe isolated change, block the row for an owner decision.

## Cleanup gate

Retain originals until all conditions hold:

- Target contents, references, package completeness, and legal notices pass the planned integrity checks.
- Every identified consumer reaches the target through its supported mechanism, including child-start sessions and workers.
- The owner approves the exact removal paths and resulting authority change.
- A recoverable removal method and restoration location are recorded for those exact paths.

Unknown, inaccessible, or unverified consumers block cleanup. A successful copy or readable link does not prove client loading.
Use recoverable removal. Keep recovery material out of unintended publication scope.
Remove only approved shared sections, not whole instruction files containing unrelated or repository-specific rules.
Permanent deletion requires explicit approval for the exact files.

## Recovery

If a destination or consumer check fails, stop dependent rows and retain originals.
Restore only this operation's authorized edits when restoration cannot overwrite intervening user changes.
Otherwise, report affected paths and the recovery procedure for an owner decision.
In the final report, distinguish a retained copy or partial migration from completed migration and cleanup.
