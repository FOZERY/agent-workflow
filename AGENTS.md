# Maintaining agent-workflow

This repository contains reusable English skill prompts and their documentation, not an application or an autonomous orchestrator. Its packages, invocation modes and project composition are indexed in [docs/SKILLS.md](docs/SKILLS.md). Do not assume catalog contents are installed in the current client.

## Read by task

- Before changing a workflow procedure or its documentation, read [FLOW.md](FLOW.md), the affected `skills/<name>/SKILL.md` and its relevant references. Skill prompts define executable instructions; FLOW defines their documented composition. Resolve disagreements explicitly rather than silently changing the contract through prose.
- Before adding, removing or changing a skill, follow [docs/MAINTENANCE.md](docs/MAINTENANCE.md). Update its catalog entry, project compositions and client metadata together.
- Before comparing or importing upstream changes, read [docs/UPSTREAM.md](docs/UPSTREAM.md). Use its pinned baselines and original source links; the upstream default branch is a candidate, not an accepted update.
- Before copying, exporting or changing attribution, read [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [LICENSE](LICENSE). Retain inherited credits, including HumanLayer's PR-format material.

## Editing contracts

At the first prompt of a session, before replying, read [human-text](skills/human-text/SKILL.md) and its applicable language reference unless already in context. Use it for conversation. Before artifact prose, read [asd-ste100](skills/asd-ste100/SKILL.md); this includes docs, ADRs, specs, tickets, `CONTEXT.md` and `LESSONS.md`. Before reusable rules, read [writing-for-agents](skills/writing-for-agents/SKILL.md); this includes skills, `AGENTS.md` and procedural references. Classify mixed sections by purpose. Reuse guidance while available; reload it after context loss or a source change.

Preserve the pinned package layout and client metadata of Matt-derived skills. The exact-copy set and approved adaptations are recorded in [docs/UPSTREAM.md](docs/UPSTREAM.md). Twelve packages add only the agreed project-instructions paragraph. Keep their remaining source unchanged unless the owner authorizes more. `grilling` and `setup-workflow` have separate local adaptations.

For local packages and repository documentation, keep prose in English and supporting material under `references/`. Preserve imported source-language examples. Keep project-specific roles, languages, paths, permissions and additional writing routes in the consumer project's `AGENTS.md`; do not rewrite vendored prompts for a consumer project.

Matt-derived packages retain their original action defaults and skill calls. Specified project settings guide the twelve adapted packages; unspecified settings retain upstream defaults. Verify required helpers in the target client and report blocked steps. Installation is not permission, and a project pointer alone is not evidence of runtime compatibility.

Root `AGENTS.md` remains the project instruction entrypoint. Consumer-project memory defaults to `.docs/CONTEXT.md` and `.docs/LESSONS.md`; only their shared directory is configurable. This repository's `docs/` is human-facing documentation. Maintaining the kit does not mean running its setup against itself or creating consumer artifacts.

## Verification and delivery

Run the narrow maintenance checks. Compare Matt-derived packages with their pinned source, accounting only for recorded adaptations. Check metadata, bundled links, external prerequisites, notices and isolated installation separately from live behavior. Get approval before a probe that launches substantive agents or changes external state.

Report what was actually verified and any behavior not exercised. A guide must not claim a hook, installer feature, update daemon or permission mechanism that does not exist.

Keep unrelated changes and installations intact. Removing a package from the kit does not authorize removing user-wide installations; use recoverable removal for files. Local commits follow the user's current instructions; push, PR/MR creation and merge require explicit authorization. Never include credentials or private project data in examples or commits.
