# Home structure and loading

Read this reference before previewing home files or client integration.

## Structure and paths

Start with `AGENTS.md`: purpose, repository pointers, and required reading rules.
Use plain pointers, not submodules, nested clones, or synchronization commands.
Prefer a dedicated sibling directory for a new home. If an existing home contains child working directories, plan their exclusion from home Git tracking before initialization or staging.
Ignore rules do not untrack existing files. Already tracked child content needs an explicit ownership/migration decision, not an automatic cleanup.
Add area indexes only when the direct list becomes difficult to navigate. Around 20 repositories is a heuristic, not a threshold.
Give each area index a task-based reading trigger.

Select paths that match the approved audience and layout:

- Fixed sibling layout: resolve relative paths from the containing document, not the working directory.
- Different team layouts: map stable repository identities to each user's local paths.
- Personal absolute paths: state the portability limit.

Keep private workstation paths and machine-local mappings outside shared versioned content unless publication is approved.
Broader exposure requires authorization for repository names, URLs, and document contents as well as files.
Reuse the agreed cross-repository artifact location and its ownership convention. Link to existing tasks rather than moving or recreating them.

## Client loading

For each actual client and start location, record the loaded file, scope, supported pointer mechanism, and configuration/documentation evidence.
Record installed skill locations, versions, discovery scope, and any unavailable paths or unverified behavior.
Use verified current client support, not guessed version-specific include syntax.
A Markdown link does not prove automatic loading. A home skill directory does not prove installation or discovery in child sessions.
If automatic loading is unsupported, supply a precise manual startup instruction and identify that manual step.
A one-line pointer must instruct the reader to read its target.

For child-start sessions, preview an explicit child entrypoint pointer or startup handoff.
For workers, pass applicable home context and require child instructions before repository work.
An accessible coordinator path does not prove access from another worktree or sandbox.
Home rules do not universally override child rules. Refer conflicting authorities to their owners rather than inventing precedence.

## Example home AGENTS.md

Resolve every bracketed field before previewing generated files. Omit empty optional sections and include every selected repository.

```markdown
# [Project] home

This repository provides navigation for [project purpose]. Child code remains in its own repositories.
Paths below resolve from this file unless a row names the approved local path mapping.

## Before repository work

1. Locate the selected repository and worktree from the index.
2. Read its instruction entrypoint and all applicable directory instructions before working there.
3. Read shared references only for the triggers listed below.
4. Report conflicting instructions to their owners before proceeding with the conflicting action.

These home instructions are not automatically loaded by sessions started in sibling repositories.
For a child-start session or delegated worker, supply [verified startup pointer or explicit handoff procedure].

## Repositories

- [Repository name] — [purpose]. Location: [approved path or mapping entry]. Source: [sanitized remote or none]. Read [child instruction path] before work.
- [Repository name] — [purpose]. Location: [approved path or mapping entry]. Source: [sanitized remote or none]. Read [child instruction path] before work.

If a repository is missing, request clone permission for its source and destination.
Use only the approved sanitized source in the repository row. A pointer does not authorize network or Git changes.

## Shared references

- Before [specific task], read [authoritative shared document path]. Owner: [owner]. Scope: [scope].
- For [specific skill use], use [verified installed package identity and location]. Its discovery method is [verified method].

## Cross-repository artifacts

Store new cross-repository task artifacts in [approved location] under [owner's existing convention].
Keep repository-specific tasks and trackers in their established locations.
```

If a child has no instruction file, state the observed absence instead of inserting a fictitious path.
Creating a child instruction file requires its own approved row.
Keep sanitized clone sources in repository rows when a separate source index adds no value.
