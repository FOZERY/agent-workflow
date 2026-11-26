---
name: verify
description: "Check that an implemented change works in the running product, the way the project agreed: locally with test data, end to end, in a test namespace or on staging. Use when implement calls it, or when the user asks to check that a change or a feature works."
argument-hint: "[task, change or behavior to check]"
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, use this skill's defaults. In your report, say once that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex).

# Verify

Prove that a change works in the running product, not only in the tests.

## 1. Read the procedure

1. Read the `verify` section and the files that it points to. They give the environments, the tools, the test data, the allowed actions and the evidence location.
2. If the project has no `verify` section, tell the user that the project has no agreed verification and suggest `/setup-workflow`. Propose a one-time check from what you find, such as the README and the test commands. Run it only after the user agrees.

**Done when:** you know the environment, the tools and the actions that need approval.

## 2. Choose what to check

1. If the caller gives a list of behaviors that the user already confirmed, use it and go to step 3.
2. From the acceptance checks of the task, list the behaviors to prove. Write each as an action and the result that a user or a system can observe. If the change touches an error path, add one check for it.
3. For each behavior, choose the environment and the tool from the procedure.
4. Show the list to the user through the question tool. In the same call, ask for each action that the procedure marks as needing approval, such as a deploy to staging.

**Done when:** the user or the caller confirmed the list and the approvals.

## 3. Prepare the environment

1. Follow the procedure: start the app, deploy, connect to the namespace or load the test data.
2. Check that you are in the right place: the cluster context, the namespace, the URL, the test account.
3. Check that the environment runs the change, for example by the commit, the image tag or the build version. Without a build, check that the running code comes from the tree that the caller gave you, or from the working tree with the change.

Act only on the environments and accounts that the procedure names. If the check needs another one, ask the user. Use credentials only from the variables or the config that the procedure names.

**Done when:** the environment is ready, runs the change and is the one that the procedure names.

## 4. Run the checks

1. Drive each behavior on the real path: the UI through the tool that the procedure names, such as `agent-browser` for web pages or `agent-desktop` for native apps, API requests, CLI commands, the test queries of the project. Read the tool's `--help` before the first use.
2. Capture the action and the result, not only the final screen. Check side effects too: rows, messages, files, jobs.
3. Save the evidence where the procedure says. Default: `.verify/<date>-<time>/`. If Git does not ignore `.verify/`, ask the user before you add it to `.git/info/exclude`.
4. If a check fails, check the environment first. If the environment is fine, record the failure as a finding. Keep each check as it was confirmed. To change a check, get the user's approval.

**Done when:** each behavior passed, failed with evidence, or is blocked with a reason.

## 5. Clean up and report

1. Stop what this run started: local processes, port forwards, browser sessions. Remove test data if the procedure says so. Keep the evidence.
2. Report to the caller or the user:
   - the environment and the build that you checked;
   - each behavior with its result and evidence path;
   - the blocked behaviors and the reasons;
   - what you did not check.
3. If you found a trap of the environment, such as a rollout delay, a cache or a flaky step, propose a line for the project's verification procedure. Write it only after the user agrees.

**Done when:** the user or the caller has the report.
