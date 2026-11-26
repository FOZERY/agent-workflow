---
name: research
description: Research a question outside the project against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, use this skill's defaults. In your report, say once that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex).

Spin up a **background agent** to do the research, so you keep working while it reads. Start it with a fresh context window. If you already run as a subagent, or the harness cannot start one, do the research yourself.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repo already keeps such notes; match the existing convention. If there is none, save it as `research/<topic-slug>.md` in the project's agent-docs directory (`.docs` by default).
4. Return the file path and a short answer to the question.

When the agent returns, give the user the path and the short answer.
