# Worker procedure

You write the code for one assignment in a separate session. The orchestrator gave you a brief: the task sources, the boundaries, the confirmed steps, the starting commit and the expected report. In direct mode the orchestrator follows this file itself.

Read the project instructions and the brief before you edit. If the brief is unclear or conflicts with the project rules, ask the orchestrator. Ask the user only if the brief allows it.

Run only the steps that the brief confirms. If a step cannot run, report the blocker and continue the steps that do not depend on it.

## 1. Prepare

Use the starting commit from the brief as the review base. Track the exact file paths that your assignment owns.

**Done when:** you know the base, the owned paths and the acceptance checks of the assignment.

## 2. Write the code

Write or update tests when the assignment requires them. Follow the project's testing procedure. If TDD is confirmed, use `tdd` at the seams from the brief. If the project runs TDD in a subagent, that subagent writes only the failing tests.

To run a skill in a subagent, give it the path from the `skill` setting of that skill's section. Tell it to read the file in full and follow it, and pass its inputs. Do not summarize the skill in the brief.

Run the typecheck and single test files regularly.

**Done when:** the assignment is implemented and its tests pass.

## 3. Simplify

If `simplify-codebase` is confirmed, run it in a subagent with a fresh context, unless its section sets another `execution`. Use the agent from its `finder` setting. Pass the starting commit and the owned file paths. The subagent only finds simplifications and returns them. It does not edit files. Wait for its findings and do not edit those files meanwhile.

Apply the findings yourself by step 6 of `simplify-codebase`. Keep its proposals for your report. The user decides about them.

**Done when:** every finding is applied or skipped with a reason, and the checks pass.

## 4. Run the full test suite

Run the full test suite of your scope.

**Done when:** the suite passed, or you know which tests fail and why.

## 5. Standards review

If the Standards review is confirmed, run `code-review` from this session with the Standards axis only. Its reviewer is a fresh subagent with the `standards-reviewer` setting. Review a working-tree snapshot of the owned paths against the starting commit.

If the `followup` setting of `code-review` is `fix-and-rereview`, fix the findings that you may fix. Run the full test suite again, then review again, up to the `rounds` setting (`3` by default). If the follow-up is `report`, or you reach the round limit, put the open findings in your report.

**Done when:** the review has no open findings within your authority, or the open findings are in your report.

## 6. Commit or hand off

Commit only if the brief allows it. Otherwise leave the changes in your branch or worktree for the orchestrator.

## 7. Report

Report to the orchestrator:

- the branch, the commits or the changed paths;
- the tests and checks that ran, with their results;
- the simplifications that you applied or skipped, and the proposals for the user;
- the Standards review outcome and any open findings;
- the steps that did not run, and the blockers.

## 8. Fix Spec findings

The orchestrator can return Spec findings to this session. Fix them and run the full test suite again. If the Standards review is confirmed and its follow-up is `fix-and-rereview`, review again by step 5. Then report again by step 7. In direct mode, return to step 5 of `implement` instead.
