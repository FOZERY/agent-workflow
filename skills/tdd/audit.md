# Audit tests

Read this file for these tasks: audit or prune existing tests, find implementation coupling or test-only production hooks, judge proposed coverage. It is not part of the red → green loop. The loop in [SKILL.md](SKILL.md) owns how to write a test. This file owns whether a test adds proof and which suite should hold that proof.

Audit **independent proof**. For each test ask: what bug would escape if this test disappeared?

The result is a map from each contract to the tests that protect it, with evidence for what to keep, repair, combine or remove. Fewer tests is not the goal. The goal is less maintenance for the same or better confidence.

## Workflow

1. **Bound the audit.** Read the project instructions. Pick one production responsibility. Find its tests, fixtures, shared suites and the CI rules that select them. Record the starting revision, the local changes and the test results before you edit. Separate existing failures from checks that could not run.
2. **Trace the claim.** Read each candidate in full, including parameter rows. Read it next to the production entry point and the code that it reaches. Check the callers, the sibling implementations, the overlapping coverage and the history of why the test exists. Write down what the assertions detect, even when the name promises something else.
3. **Record a disposition before you edit.** Use the evidence record below. Share a material finding when you find it. An audit-only request ends with the evidence and a proposed batch, not with deletions.
4. **Choose the surviving owner.** Look across the records for whole redundant layers, not only weak assertions. Name the suite that owns each contract and the unique cases it must absorb. Prefer a real path with controlled external dependencies over a replay of internal collaborators. Add a second layer only for a failure that the owner cannot expose, such as routing or lifecycle behavior.
5. **Change one coherent boundary.** Move the unique cases into the surviving suite before you remove their old home. Extend existing cases and fixtures instead of cloning setup. In the same batch, remove test hooks and support code that nothing needs now. Check the production consumers before you delete an export, wrapper, reset function, global or injection parameter. Update test discovery and CI registration when you move a suite.
6. **Prove preservation.** Compare the removed assertions with the survivors. Look for lost contracts and for assertions that cannot fail for the intended reason. Falsify each repaired or moved regression test: break the production code on purpose, confirm that the test fails, then restore the original bytes. Report baseline failures separately. Investigate every new failure. Run the owner suite, the sibling suites and the required project checks.
7. **Close the batch.** Run `code-review` on the result. Compare the evidence record with what shipped. Report unresolved failures and checks that did not run. A smaller suite that passes does not prove that the removed coverage was redundant. The contract map and the preservation evidence do.

## Evidence record

For each candidate, record these items: its location and name, the failure that it can actually detect, and the reason it exists. Add the production consumers of any supporting hook. Then record a decision.

- **Keep.** Name the contract that it protects independently. Moving the file does not change this decision.
- **Repair.** The contract stays. Replace an assertion that is weak, misleading or attached to the wrong boundary.
- **Combine.** Name the destination suite and the unique cases that it must prove before the original goes away.
- **Remove.** Name the stronger surviving proof, or show that there is no contract to protect. Suspicion of duplication is not enough.

Add the source and history evidence, the cleanup that the change unlocks, the risk and the validation command. Missing evidence stays an open question. It never becomes a deletion.

## What earns retention

A contract can be behavior, compatibility or an operating rule. Examples: API and SDK shape, wire bytes, prompts, defaults, configuration, migrations, storage, security, platform behavior, cross-language agreement, package contents, release rules, architecture boundaries and observable ordering. A static assertion can be the cheapest independent proof of such a contract.

Ask whether the test survives an internal rename and still detects a broken external promise. Exact bytes can be essential to a protocol. Exact private identifiers usually are not. A test is not removable only because it is slow or because it looks like the implementation. Do not add a refactor-sensitive test when the real contract can be exercised directly.

A failing test can show a product defect. Reproduce and investigate it. Never remove a valid claim to make the audit pass. Fix an in-scope defect in a separate change, with a failing control and a passing fix on the same harness. Record an unrelated defect as a follow-up and keep its test.

## Whole-subsystem sweeps

Scale the accounting before you scale the edits.

- List every test that the subsystem owns, including cases in shared suites and in integration, QA or live harnesses. Assign each one to one production responsibility, even when the file prefixes disagree. Record the baseline outcomes and the size of tests and support code.
- Give every declaration a disposition and evidence. A parameter table can share one record only when all rows deserve the same decision. Then read across the records to choose the surviving suites and the retired layers.
- If agents are available, delegate the read-only discovery by responsibility. Keep edits to shared fixtures under one owner. Each batch must add no unexplained failure.
- Use an independent reviewer to compare the removed coverage with its new owners. Resolve every reported gap with restored proof, or with source evidence that rejects the gap. Show that each restored contract catches a deliberate defect.
- If the base branch advances, read the new cases in any file that you remove and carry their contracts forward. Then rerun the subsystem checks on the resulting revision.

Claim a complete audit only when the list has no unexamined entry.

## Done

Hand off these items: the contract map, the decisions and reasons, and the production simplifications. Add the valuable tests that you kept on purpose, the preservation gaps and how you resolved them, and the verification that you actually ran. For a broad sweep, add the before and after size of production, tests and support code, separately. Size describes the result. It never sets a deletion target.
