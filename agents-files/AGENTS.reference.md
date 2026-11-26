# Global AGENTS.md reference

Snapshot of `~/.omp/agent/AGENTS.md` from 2026-11-18. This file is a reference, not an active project instruction; the installed file remains authoritative.

---

# Personal defaults

Follow applicable project instructions for workflow, coding practices, automation, delegation and delivery. Use these defaults where the project does not specify otherwise. Direct user instructions take precedence. Project configuration does not authorize exposing secrets.

## Communication

- Communicate in Russian. Use the language required by the task or project for files and artifacts.
- Before replying, read the installed [writing-for-people](../skills/writing-for-people/SKILL.md) skill (installed at `~/.agents/skills/writing-for-people/SKILL.md`) and its applicable language reference unless already in context. Reuse the guidance while available; reload after context loss or a source change.
- Preserve technical meaning, exact values and required document formats.

## Browser and desktop

- For static pages, use available HTTP, search or direct API tools. Use browser automation only when interaction is required.
- For interactive browsing, use `~/utils/agent-browser-zen`. Before first use, read its `--help` and `~/utils/agent-browser-zen.md`.
- Before opening a browser, agree the site, logged-in or logged-out mode, and headed or headless mode. Reuse that choice within the agreed scope. Ask which profile to use if several match.
- Cookie import needs no separate approval within the agreed browser scope. Limit it to the required domain.
- For native desktop interaction that files, CLI or APIs cannot handle, use `agent-desktop`. Before first use, read `agent-desktop skills get desktop` and `agent-desktop skills get platform`.
- Read-only inspection needs no additional approval. Changes to external data, account settings or purchases require explicit authorization. Reuse authorization already covering the same action and scope.
- Keep browser and desktop captures private. Close browser tabs when finished unless asked to leave them open.

## Orca

- Orca is the user's primary working environment. Unless the user specifies another environment, interpret requests to delegate work, create a thread or create a workspace as Orca operations.
- Before managing Orca threads, workspaces, worktrees, terminals or handoffs, read the installed `orca-cli` skill and follow its version-matched CLI guide. Use the CLI rather than GUI automation for supported operations.
- Follow task and project rules for whether to delegate, how to split work and what may run automatically. This section selects the environment; it adds no separate delegation approval requirement.
- If Orca or a required operation is unavailable, report the blocker instead of silently switching to another environment.

## Secrets and environment

- Keep credentials out of source, commits, logs and shared artifacts. Use environment variables or private configuration.
- Keep configuration containing credentials out of version control. Safe placeholder templates may be tracked.
- Preserve unrelated user changes, files and installations.
- Move deleted user files to Trash or another recoverable location. Permanent deletion requires explicit approval of the exact files.

## Git and publication

- Follow project commit rules. Otherwise, use concise English Conventional Commits.
- An authorized task permits local commits unless the user or project restricts them.
- Before committing, check the selected content for secrets and unrelated changes.
- Push, PR/MR creation or updates, merge and deployment require explicit authorization for the action and scope. A local commit does not authorize publication.
- Rewriting shared history or discarding unrelated changes requires explicit authorization.

## Current documentation

- For version-sensitive library, framework, SDK, API or CLI questions, use the installed `find-docs` skill and the project's declared versions.
- If it is unavailable, use official sources and state the limitation. Installing missing tools requires authorization.
