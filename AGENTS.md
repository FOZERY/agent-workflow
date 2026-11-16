# Maintaining agent-workflow

This repository contains reusable English skill prompts and their documentation, not an application or an autonomous orchestrator. Its supported packages, invocation modes and dependencies are indexed in [docs/SKILLS.md](docs/SKILLS.md). Do not assume catalog contents are installed in the current client.

## Read by task

- Before changing a workflow procedure or its documentation, read [FLOW.md](FLOW.md), the affected `skills/<name>/SKILL.md` and its relevant references. Skill prompts define executable instructions; FLOW defines their documented composition. Resolve disagreements explicitly rather than silently changing the contract through prose.
- Before adding, removing or changing a skill, follow [docs/MAINTENANCE.md](docs/MAINTENANCE.md). Update its catalog entry, callers, dependencies and client metadata together.
- Before comparing or importing upstream changes, read [docs/UPSTREAM.md](docs/UPSTREAM.md). Use its pinned baselines and original source links; the upstream default branch is a candidate, not an accepted update.
- Before copying, exporting or changing attribution, read [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [LICENSE](LICENSE). Retain inherited credits, including HumanLayer's PR-format material.

## Editing contracts

Write and edit skills and agent instructions following [writing-for-agents](skills/writing-for-agents/SKILL.md). For human-facing text, follow [human-text](skills/human-text/SKILL.md) and its applicable language reference. Keep repository prose and agent instructions in English; preserve source-language examples where they are part of an imported language guide. Keep `SKILL.md` at package root and supporting material under `references/`. `agents/openai.yaml` is client metadata, not an execution agent.

Keep reusable skills project-aware. Project sources and procedures control artifact locations, test scope and authority; changes must not introduce automatic publication, mandatory infrastructure or blanket approval. Preserve the specific independent-review/human-acceptance gates of the implementation routes unless the owner explicitly changes that contract.

Prefer targeted adaptations to wholesale upstream replacement. Define required behavior with observable completion criteria and conditional references. Keep one owner for each rule; use links rather than duplicating full procedures across skills, documentation and generated instructions.

Root `AGENTS.md` remains the project instruction entrypoint. Consumer-project memory defaults to `.docs/CONTEXT.md` and `.docs/LESSONS.md`; only their shared directory is configurable. This repository's `docs/` is human-facing documentation. Maintaining the kit does not mean running its setup against itself or creating consumer artifacts.

## Verification and delivery

Run the narrow checks described in the maintenance guide for the affected contract. Check Markdown links, metadata, dependency closure and client discovery separately from live behavior. Use isolated temporary projects for installation/discovery checks; preserve licenses in exported packages. Get approval before a live probe that launches substantive agents or changes external state.

Report what was actually verified and any behavior not exercised. A guide must not claim a hook, installer feature, update daemon or permission mechanism that does not exist.

Keep unrelated changes and installations intact. Removing a package from the kit does not authorize removing user-wide installations; use recoverable removal for files. Local commits follow the user's current instructions; push, PR/MR creation and merge require explicit authorization. Never include credentials or private project data in examples or commits.
