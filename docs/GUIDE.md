# Skill guide

[Overview](../README.md) · [Workflow routes](FLOW.md) · [Русская версия](GUIDE.ru.md)

This guide describes each skill in the order of the workflow: set up, understand, discuss, plan, implement, improve, write. Each entry says what the skill does, who starts it and what you get, with an example prompt.

A command with `/` works in Claude Code. In Codex, type `$` instead of `/`. A skill marked "the agent can start it" also runs when your request fits its description, without the command.

## Set up

### `/setup-workflow`

Configures the workflow for a project. It asks about your rules, checks, permissions, Git delivery, fact sources and the agents for each step. Then it offers the skills, installs the approved ones and writes the root `AGENTS.md` with the shared rules block and one section per skill. Run it again when your rules change or after a kit update.

```text
/setup-workflow
```

### `/setup-home-repo`

Makes a home repository for a project that spans several repositories. The home holds navigation, shared material and entry points for each client. It does not move the code or the rules of the child repositories. Run `/setup-workflow` in the home afterwards if it needs workflow rules.

```text
/setup-home-repo the app is in ../web, ../api and ../infra
```

### `/ask-workflow`

Answers a question about the workflow and recommends the next skill, with the command to run. It reads the project's `AGENTS.md` and the installed skills. It starts nothing.

```text
/ask-workflow I have a bug report in GitHub issue #42. Where do I start?
```

## Understand

### `/investigate`

Studies a task before you discuss it. Two researchers read the task's history (tickets, commits, merge requests, wiki, chats, logs, as configured in setup) and the code around it. For a task, the skill saves the facts with their sources in `facts.md` next to the task. For a question without a task, it saves the file only if you ask. It then explains the task to you in plain words, with diagrams where they help. `implement` later gives that file to its workers.

```text
/investigate JIRA-1234
/investigate how do lesson reminders get sent?
```

### `/recall`

Rebuilds where your recent work on a topic stands. It reads `CONTEXT.md`, the recent session transcripts of the project and, for a named feature or bug, the shared record: the tracker, merge requests and the other sources from the `investigate` settings. It checks each branch, PR and ticket against its current state and gives a short brief: summary, threads with their status, problems that repeat, and the next step. It changes nothing.

```text
/recall
/recall the export work from last week
```

### `research`

Answers a question from primary sources, such as official docs, specs and source code, and saves a cited report in the repository. Use it for facts outside the project. The agent can start it.

```text
Research how Telegram bots can create forum topics in private chats. Cite the Bot API.
```

## Discuss

### `grilling`

Asks you questions, round by round, until every open decision of an idea is settled. Each question comes with a recommended answer. It looks up facts itself and asks you only for decisions. The agent can start it.

```text
Grill me on this plan: move notifications to a queue.
```

### `/grill-with-docs`

The same interview as `grilling`. It also writes new terms to `GLOSSARY.md` and offers an ADR for a decision that is hard to reverse.

```text
/grill-with-docs the billing period model
```

### `domain-modeling`

Keeps one name for each concept in `GLOSSARY.md` and records hard-to-reverse decisions as ADRs. It challenges a term that conflicts with the glossary and checks claims against the code. The agent starts it when a discussion is about terms or decisions.

```text
Is a "group lesson" a lesson or a series? Update the glossary.
```

### `prototype`

Builds throwaway code to answer a design question. For logic, it makes one HTML file that walks a state model through its hard cases. For UI, it shows several variants on one page with a switcher. The decision goes into the real code, the prototype does not. The agent can start it.

```text
Prototype the lesson status transitions for cancel, move and restore.
```


## Plan

### `/to-plan`

Saves an implementation plan for one task next to the task: approach, steps, checks and open decisions. It needs no spec or tickets. The plan stays `Proposed` until you approve it, and approval does not start the work.

```text
/to-plan JIRA-1234
```

### `/to-spec`

Turns the discussion so far, or a finished `wayfinder` map, into a spec. It checks the test seams with you, shows the draft and publishes it to the tracker after your approval.

```text
/to-spec
```

### `/to-tickets`

Splits a plan, a spec or the discussion into thin tickets, each with its blocking tickets. It shows the set for approval before it publishes.

```text
/to-tickets from .docs/billing/plan.md
```

### `/wayfinder`

Maps an effort that is too large and too unclear for one session. It creates a map ticket and decision tickets, then resolves them one at a time. When the map is done, it recommends `to-spec` or `to-plan`.

```text
/wayfinder move from SQLite to Postgres
```

## Implement

### `implement`

Implements an agreed task. The session is the orchestrator:

1. It reads the task, the plan or tickets, and the `investigate` facts file if there is one.
2. It picks a size: trivial (edit and stop), small (writes it itself), normal (one worker) or large (several workers).
3. It asks you once to confirm the mode, the steps and the test seams. You can turn off steps for a simple task.
4. Workers write the code in separate sessions by `implement/WORKER.md`: tests, simplification, the full test suite and the Standards review.
5. With several workers, it integrates the parts into one tree.
6. On that tree, it checks the result against the task (the Spec review), then runs `verify` on the changed behavior, if it is on. Then it commits if allowed and reports with the evidence.

The agent starts it when you ask for a change.

```text
Implement JIRA-1234 by the plan in .docs/jira-1234/plan.md.
```

### `tdd`

Test-first, and only tests that prove real behavior. Before each test it names the bug that the test must catch. It prefers integration tests that run a real flow of the application and module tests through a public interface, and mocks only external services, time and randomness. One failing test, then the smallest code that passes it, at the seams that you confirmed. For a bug, the first test reproduces it. For configuration and glue code it writes no test and names the check it used instead. It can also review existing tests by the same rules and remove the ones that prove nothing. `implement` runs it when the project's setting says so. The agent can start it.

```text
Add the late-homework rule test-first.
Audit the tests in src/billing and remove the ones that prove nothing.
```

### `simplify-codebase`

Finds what to simplify in changed code: deep nesting, unclear names, duplication, and guards or abstractions that nobody needs. A finder subagent lists the findings, and the session that wrote the code applies them one at a time with the tests. Larger removals come to you as proposals. `implement` runs it when the project's setting says so. The agent can start it.

```text
Simplify what we changed in this branch.
```

### `verify`

Checks that a change works in the running product, not only in the tests. How to check is agreed in `setup-workflow`: run locally with test data, run the e2e path, check in a test namespace through `kubectl` and `agent-browser`, or deploy to staging. What to check comes from the task: the skill lists the behaviors from the acceptance checks, you confirm them and the actions that need approval, and it reports each result with evidence. `implement` runs it when the project's setting says so. The agent can start it.

```text
Verify the lesson cancellation in the test namespace.
```

### `code-review`

Reviews a diff on two axes: Standards (the project's coding rules) and Spec (does it do what the task asked). Each axis runs in a fresh subagent. In `implement`, each worker runs Standards and the orchestrator runs Spec. The agent can start it.

```text
Review this branch against main.
```

## Improve

### `/retro`

Reads recent sessions (their transcripts, `CONTEXT.md`, `LESSONS.md` and Git history) and finds mistakes that were found and fixed. It turns each lasting lesson into an instruction: a rule in a skill, a new skill, a project rule or a lesson. It edits only what you approve and records the retro in `CONTEXT.md`. For a change to the core block or a skill setting, it gives you a `/setup-workflow` command.

```text
/retro
/retro last two weeks, the billing work
```

### `/refactor-codebase`

After a stage of work, finds where the structure of the code makes change hard: shallow modules, broken project rules, poor practices of the stack. It also collects simplifications and changes nothing yet. You pick one candidate or the simplifications, discuss it with `grilling`, and `implement` rewrites it with the behavior kept.

```text
/refactor-codebase since tag v0.3
```

### `/refactor-docs`

Rewrites documents and project memory for clarity and structure. It keeps every decision, requirement and fact, and checks the result against the original.

```text
/refactor-docs docs/architecture.md
```

### `/cleanup-artifacts`

Reviews stale working files: notes, plans, reports, diagrams. It shows a plan with the evidence for each file. It moves only the files that you approve to the Trash or an archive, and keeps a restore map.

```text
/cleanup-artifacts review only
```

## Write

### `writing-for-people`

Rules for replies and explanations: the result first, plain words, one fact per sentence, no machine habits. A numbered list of habits with examples, in English and Russian. Point to it from your instructions so that the agent reads it before the first reply.

### `writing-technical`

Rules for technical documents, skills, `AGENTS.md`, specs and tickets, based on ASD-STE100 controlled English: one idea per sentence, the condition before the action, real names, numbered steps. It has a Russian reference.

### `writing-for-agents`

A procedure for writing a skill or `AGENTS.md`: find the job, choose who starts it, write the frontmatter and body, prune every sentence that does not change the agent's behavior, check the links and test the skill on a fresh agent. Sentence style comes from `writing-technical`.

### `/rephrase`

Restates the last reply in plain words. It keeps every fact and decision.

```text
/rephrase
```
