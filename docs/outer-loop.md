# Outer loop design

Status: Agreed design. Implementation has not started.
Date: 2026-11-22.

This document describes how a person runs several personal code projects through long-lived agents.
The outer loop receives work, tracks it and asks the person for decisions.
The inner loop is the existing kit workflow: a session next to the code plans, implements, reviews and opens a pull request (PR).

The design does not depend on one bot or harness.
The sections [Open questions](#open-questions) and [Sources](#sources) record what is not decided and where the facts come from.

## Scope

In scope:

- Personal projects that contain code.
- One server that runs the assistant, the project agents, the stream leads and the board.
- Access from a phone through a messenger, with voice messages.

Out of scope:

- Projects without code, for example travel planning.
- The verification design. It is a separate discussion during implementation.

## Roles

### Person

- Gives tasks by voice or text.
- Must act at two gates: the start of a code change ("go") and the PR merge.
- Can give "go" in the assistant chat, in the project thread or in a stream lead session. The agent that receives it tells the project agent.
- Owns the statuses in the source trackers, for example GitHub Issues.

### Assistant

There is one assistant. It runs on the server.

- Holds the main thread with the person.
- Routes requests to the project agents. It does not do work inside a project.
- Reads the board and builds summaries and the list of items that wait for the person.
- Asks a project agent directly only when the person asks for information that is not on the board.
- Creates a new project when the person asks. The person confirms each step that gives access.
- Keeps its long-term memory and the project registry as files in its private repository.
  The registry gives the root path, the agent address and the source tracker of each project.
  The bot's own memory is a cache.

### Project agent

There is one project agent for each project.

- Holds the project thread with the person.
- Reads the code, commits, PRs and CI results. It does not change code.
- Reads the source tracker. It does not change it. If the person closes or pauses a task there, the project agent stops the related work.
- Wakes on events, for example a new issue, a CI failure or a PR comment.
  If a source has no events, the project agent checks it on a schedule. It also works when the person asks.
- Sorts new work. If a bug needs reproduction, it starts an investigation without a "go" from the person.
  An investigation reproduces the bug and finds the cause. It does not change code. It stays within an investigation budget.
- Proposes "fix" or "discuss" for each item and sets the card to `Needs you`.
- After "go", starts a work stream or puts it in the queue.
- Enforces the limit of active work streams for the project.
- Is the only writer of the cards of its project.
- Relays discussion messages between the person and the stream lead word for word, in both directions.

### Stream lead

A work stream is one epic, one feature or one group of related bugs. A single bug is a stream with one task.
There is one stream lead session for each work stream. The project agent adds a related task to an existing stream instead of a new session.

- Runs next to the code on the server.
- Follows the workflow and rules of the project root, for example its `AGENTS.md`.
- Coordinates the work. It does not write code itself. Workers write the code.
- Reports each stage change to the project agent.
- Handles CI failures, merge conflicts and review comments until the merge.
- Stays available until the merge. The project agent stores the session ID on the card, so a later message can resume the session.
- After the merge, writes the result and lessons to the project files. Then the session closes.

### Workers

The stream lead runs the `implement` skill as its orchestrator. Workers are separate sessions that follow `implement/WORKER.md`.

## State

### Board

- One [Backlog.md](https://github.com/MrLesk/Backlog.md) board holds the cards of all personal projects.
- Each card has a project tag (the Backlog.md `projects` setting).
- The board is in the assistant repository. Card changes are committed to git.
- The board only shows state. The person gives commands in the chat, not on the board.
- Each project agent writes only the cards of its own project. The assistant only reads the board.

One card describes one work stream. It contains:

- the project tag;
- links to the source tasks;
- the stage;
- the reason and a link when the stage is `Needs you`;
- the stream lead session ID;
- the link to the discussion topic;
- the PR link.

### Stages

| Stage | Meaning |
| --- | --- |
| `New` | The project agent received the item. Sorting or investigation is in progress. |
| `Needs you` | The person must act. The card gives the reason: "go" or discussion. |
| `Queued` | The person gave "go", but the project is at its limit of active streams. |
| `In progress` | A stream lead session runs the stream. Review also happens in this stage. |
| `Ready to merge` | The PR is ready. The person must merge it. |
| `Done` | The PR is merged. The stream lead session is closed. |

A project can rename or remove stages in its own rules.

### Project root

The project root is the repository of the project.
If a project has several repositories, the project root is a home repository that links them.
The project root holds the project rules (`AGENTS.md`), `CONTEXT.md` and `LESSONS.md`.

## Messenger

The messenger is Telegram.

- The private chat with the assistant bot is the main thread.
- Each project has its own bot. In the private chat with a project bot, the General topic is the project thread.
- When a work stream needs discussion, the project agent creates a topic for it in the same private chat. The topic closes after the merge.
- The project bots are in a Telegram chat folder named "Projects".
- Voice messages become text before the agent reads them.

Telegram topics cannot contain other topics. For this reason, each project has its own bot instead of one group with a topic for each project.

## Work stream lifecycle

1. An event or a schedule wakes the project agent, or the person gives a task.
2. The project agent creates a card in `New` and reads the related code.
3. If the item needs reproduction, the project agent starts an investigation within the budget.
4. The project agent proposes "fix" or "discuss" and sets the card to `Needs you`.
5. The person gives "go".
6. If the project is at its stream limit, the project agent sets the card to `Queued`. Otherwise, it starts a stream lead session and sets the card to `In progress`.
7. If the stream needs discussion, the project agent opens a topic and relays the messages word for word. At the desk, the person can open the stream lead session directly.
8. The stream lead runs the project workflow and opens a PR.
9. When the PR is ready, the project agent sets the card to `Ready to merge`.
10. The person merges the PR.
11. The project agent sets the card to `Done`. The stream lead writes the result and lessons, and the session closes. The next `Queued` stream starts.

## Open questions

1. **Verification.** `verify` checks each change by the procedure that the project agreed in setup, and `implement` runs it. Still open: when the person looks at the evidence.
2. **Limits.** Set the number of active streams for each project and the investigation budget.
3. **Runtime.** [Hermes Agent](https://github.com/NousResearch/hermes-agent) is the candidate for the assistant and the project agents. Its documentation states:
   - one profile for each agent, with its own bot token, memory, skills and schedules;
   - each Telegram topic, including topics in private chats with a bot, is a separate session;
   - speech-to-text for Telegram voice messages;
   - cron schedules and webhooks that can target a profile;
   - built-in memory of about 2,200 characters, which agrees with "bot memory is a cache".

   Its documentation does not describe a driver for Claude Code. Its Codex runtime is optional.
   Check how a project agent starts a stream lead session and resumes it by session ID, for example through the headless mode of the agent CLI.
4. **Board checks.** Before installation, check that two project agents can create cards at the same time without an ID conflict. Check that the web view can filter by project. Use a Backlog.md release that is at least two weeks old.
5. **Orca.** Orca bots talk only through the chat inside the Orca app, so they are not part of this outer loop. Orca can stay a desk tool. It was not checked whether Orca can attach to sessions on the server.
6. **Server.** Choose the hosting, the private access path and the backups.

## Sources

- Lauren Tan, live stream on her SpaceX workflow: <https://www.youtube.com/live/MN9dGgmLyso>.
  Her outer loop is a bot with routines that watch external sources and start projects.
  Her inner loop is a coordinator agent that delegates to subagents.
  She advises giving related tasks to one coordinator.
- Lauren Tan, "All Code Is Slop (Except Mine)": <https://youtu.be/O_zcc6Xl12g>.
- Matt Pocock, "The Home Repo": <https://youtu.be/hWe-j78vNpc>. One repository links the other repositories of a project.
- Hermes Agent documentation: <https://github.com/NousResearch/hermes-agent>, folder `website/docs/`.
- Backlog.md documentation: `README.md` and `ADVANCED-CONFIG.md` in <https://github.com/MrLesk/Backlog.md>.
- Telegram Bot API and its changelog: <https://core.telegram.org/bots/api>. Bot API 9.3 and 9.4 added topics in private chats with bots.

This design differs from Lauren Tan's setup in three points:

- There is a separate project agent between the assistant and the stream leads.
- The person must give "go" before a code change.
- The person merges each PR.
