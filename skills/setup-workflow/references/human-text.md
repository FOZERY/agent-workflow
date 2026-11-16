# Optional human-text activation

Read on initial setup and when changing writing style, target clients, deployment or activation. Session-wide `human-text` activation is optional. A selected skill can still require its package for its own operation; resolve that requirement through [dependency planning](skills.md#explain-omissions-and-resolve-dependencies). Installing such a prerequisite does not authorize a session-wide pointer.

## Check existing installations first

Before asking about style installation, run the [same-name check](skills.md#check-same-name-copies) for `human-text` on the known target clients. Ask only for missing client information needed to locate their skills.

Report the found scope and path, package completeness and client discovery status. A copy for another client is not evidence of availability for this one. An inaccessible location has unknown status, not confirmed absence.

## Explain and ask

Explain that the skill guides human-facing replies and document prose: result first, natural language, less filler and repetition, and preservation of technical facts. It includes a Russian-language reference. Its closing-block conventions apply to conversations and written documents as specified by the installed skill. Project instructions can override its style defaults, and required document structure, technical meaning and permissions remain authoritative.

Show the discovered status before asking. If a suitable installation exists, offer to reuse it and ask only about missing activation; preserve an effective existing trigger without adding a duplicate. If neither global nor project scope has an installation, ask whether the owner wants the skill and, if yes, whether to install it globally or only in the project. Resolve unknown locations before claiming the skill is absent. Describe that only the pointer, not the full style text, goes into instructions. Installation alone does not activate a skill.

If the owner declines session-wide style integration, skip new style pointers and a standalone style installation; continue setup. If a later skill choice requires `human-text`, explain and approve that package dependency separately rather than treating the earlier answer as approval or silently dropping the prerequisite. Preserve existing packages and global rules: declining integration does not disable style already active elsewhere. On reruns, preserve accepted choices unless the requested change affects them.

If accepted, retain the discovered or chosen installation scope and settle only unresolved client and activation choices. Installation scope and instruction scope are separate: propose repository-root `AGENTS.md` for project activation; global instruction edits require separate explicit scope approval because they affect other repositories. An existing global installation does not authorize adding a project pointer.

## Discover and plan

Resolve the approved source/version and actual instruction loading. Preserve equivalent working installations and triggers. Resolve local modifications and aliases before replacement. Do not install missing clients or assume Claude, Codex and OMP share discovery.

For project activation, root `AGENTS.md` is the contract; use the existing client wrapper/import only where needed to load it. For explicitly selected global activation, verify the client's effective source:

| Client | User-wide instruction source to verify |
| --- | --- |
| Claude Code | Loaded user instructions, normally `~/.claude/CLAUDE.md`, honoring configured directories and imports. See [Claude memory documentation](https://code.claude.com/docs/en/memory). |
| Codex | First applicable non-empty `AGENTS.override.md` or `AGENTS.md` under effective `CODEX_HOME`, normally `~/.codex`. See [Codex instruction discovery](https://developers.openai.com/codex/guides/agents-md/). |
| OMP | Active native agent-directory instructions, normally under `~/.omp/agent`; honor profiles and `PI_CODING_AGENT_DIR`. Consult current `omp://context-files.md` and `omp://skills.md` when available. |

OMP filters context files named `AGENTS.md` out of task-subagent inputs. Do not promise helper coverage from an AGENTS-only pointer. If the owner wants that coverage, explain and separately approve an appropriate native `RULES.md` pointer or delegation-level instruction; do not add direct calls to every workflow skill. Verify package discovery separately, including `skill://human-text` availability, and do not guess an OMP skills-CLI target or change discovery settings without approval.

Show package installation and instruction activation as distinct effects in the deployment plan: source/version, clients/profiles, project/global destinations, complete package and legal notices, exact pointer text, files affected and reload requirements. This setup owns the optional integration; do not install or run `setup-plain-writing`.

## Activate at the end of setup

After deployment approval and project configuration, install only a missing or explicitly approved replacement package through the agreed installer. Use `npx skills` for supported clients and a verified native/shared-source method for OMP. A pointer-only gap requires no reinstall.

Only after the installed `SKILL.md` and its references are readable, add or update the approved pointer in root `AGENTS.md` or the selected global source. Adapt this short trigger to the agreed language and resolve the skill through the client's mechanism or installed path:

> Before the first human-facing reply or document, read the installed human-text skill and its applicable language reference unless they are already in context. Reuse them while they remain available; reload them after a context reset or source change. Apply their style while preserving technical meaning, required document structure and project approval rules.

Keep only the pointer in instructions, not the full style guide. Do not add a repository-private absolute path to shared instructions. Preserve unrelated rules and avoid duplicate triggers. If installation fails, leave new activation pointers unwritten and report the gap; do not leave a dangling global reference. A decision made during setup cannot retroactively style earlier replies: use the installed skill once available, and request a new session/reload where startup instructions require it.

## Verify and report

Check the complete package, local references, client discovery and the effective instruction target. Walk through global installation reuse, project-only installation reuse, neither scope installed, unknown locations, a broken or shadowed copy, declined integration, a pointer-only gap, scope changes and any requested helper coverage. For initial installation, ask for a scope only when both scopes are confirmed absent; reuse an existing suitable package without reinstalling it. Unrelated reruns must neither re-ask the style question nor reinstall or rewrite accepted activation.

Distinguish present files, discoverable skills and observed model adherence. Run a live activation probe only when its invocation and effects are approved; otherwise label behavior untested. Report installation and activation separately for each selected client/profile. An unavailable optional style does not block unrelated workflow configuration.
