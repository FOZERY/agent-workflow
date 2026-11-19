# Skill selection and installation

Read this file when the selected skills, clients, scope or installation change.
`setup-workflow` works alone. Each Matt-derived skill can be installed alone, but it keeps its runtime prerequisites. Before you call a route ready, read the skill's real calls and the [catalog dependencies](catalog.md#dependencies).

## Select the skills

1. After the project purpose and task sources are agreed, configure writing through [writing routes](writing.md).
2. Offer the skills from [the catalog](catalog.md) as one multi-select, before the skill-specific questions. Add a "no other skills" option and the skills that the user suggests.
3. For each skill, show its purpose, its installation status and your recommendation. Leave every option unselected until the user selects it. Catalog groups organize the list; they are not bundles.
4. Offer `ask-workflow` as an optional guide for workflow questions. It installs alone, before or after setup, and runs no procedures. Its selection selects no other skill.
5. If visual design support is relevant, offer `excalidraw-diagram`. If the user selects it, use [diagram configuration](diagrams.md).
6. Use the selection to decide which skill-specific questions apply. If a later answer makes a selected skill unsuitable, return to the selection before final approval.

Rules for the selection:

- Every skill is optional. No selection means no installation. Existing skills and instructions stay.
- A route can need an extra skill that the project approves. Explain each such prerequisite separately.
- Check installation and discovery for each client separately.
- A global skill can be unneeded or not permitted in this project. To turn off a workflow, change `AGENTS.md`. Keep the shared global skill.
- Installation runs no skill and grants no permission for its actions.

## Packages and project rules

1. The Matt-derived skills keep their original calls: `wayfinder` calls `domain-modeling` and `prototype`, `tdd` calls `codebase-design`. The kit has these helper skills, but the client must have them installed too.
2. Check the original prerequisites of each skill and the extra requirements of the approved `AGENTS.md`.
3. If a prerequisite is missing, ask the user to approve a source and installation, or record the route as unavailable.
4. Record roles, paths, languages, writing routes and extra skills in `AGENTS.md` or in project files that it links.
5. Keep installed skill files unchanged. Restore no removed helper and replace no required procedure during setup. Changes to a skill are separate kit maintenance.

## Package source

1. [The catalog](catalog.md) lists the skills of this kit version. Before you plan, check that each selected skill exists in the source. An old setup summary does not prove that a skill exists.
2. The default source is `FOZERY/agent-workflow`, unless the user agreed another source.
3. For the first install, only `setup-workflow` is needed. Install another skill only when the user selected it or the approved `AGENTS.md` requires it. Credits to original sources are not install targets.
4. Find the source that installed `setup-workflow`. Read its `source` in the installer lock file: `skills-lock.json` in the project, or `~/.agents/.skill-lock.json` for a user-wide install. Install the other skills from the same revision.
5. If the lock file names no usable source, or the remote is empty, tell the user and ask for the path to a local checkout.
6. For each approved skill, record its source, version, compatibility and full reference files. Keep its provenance and notices.
7. If another source has a skill with the same name, ask the user before you use it. A same name does not make two skills the same.
8. For `excalidraw-diagram`, keep all references, the renderer, the four bundled libraries and the provenance notice. Some upstream material has no stated license, and the kit's MIT license does not cover it. Read the notice before redistribution. A same-named upstream global copy is a different skill; replace it only with the user's approval.
9. If a skill is missing or not compatible, tell the user which route it affects and what decision is needed. Continue the unrelated work.

Installing skills does not permit publishing the repository.

## Clients and scope

1. Offer each supported client as a separate option: Claude Code, Codex, OMP. Add a client that the user asks for if it has a documented install method. A client found on the machine is not selected until the user selects it.
2. For each client and skill, offer project or user-wide scope where the client supports it. Recommend by situation:
   - **Personal machine:** user-wide. Every project runs the same kit version. Each project's rules still come from its own `AGENTS.md`.
   - **Team repository:** project scope, with the skill directories tracked in Git. Every member runs the same version.
3. If the owner asks, different skills can use different scopes.
4. Inspect only the install locations that the user permitted. Find the supported installer or the documented native method and the exact destination paths.

### Check same-name copies

A copy with the same name from another source can hide a selected skill or break the approved procedure. Check each selected name, for each client, in both scopes. A name collision does not make an unrelated skill a dependency.

| Client | Project skills | User-wide skills | Same name in both scopes |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | The user-wide copy runs. A project copy cannot override it. |
| Codex | `.agents/skills/` | `~/.agents/skills/`, `~/.codex/skills/` | Both load, and `$name` is ambiguous. It does not resolve by name. |
| OMP | `.omp/skills/` | `~/.omp/agent/skills/` | Not verified. Read the current OMP skill documentation before you rely on precedence. |

Claude Code also has a bundled `code-review`. An installed copy of the kit's skill replaces `/code-review`. `/review` keeps the client's bundled behavior. When an original skill calls review, check which version is active. There is no local fallback reviewer.

1. Find the origin of each copy: the `source` in its lock entry, its symlink target, or a content comparison with the kit's skill.
2. A copy belongs to the kit when its source is this kit or its content matches the kit's skill. Keep such a copy; do not reinstall it.
3. If another copy hides or collides with a kit skill, show its path, origin and effect. Let the owner choose:
   - Replace the user-wide copy with the kit's copy. This changes every project that uses it. Move the old copy to a recoverable location.
   - Move the kit installation to user-wide scope.
   - Keep the other copy and record the dependent route as unavailable.
4. Install exactly one copy of each name for each client.
5. In a team repository, record in `AGENTS.md` which skill names a personal install would hide, so that members can check their machines.

## Install plan and approval

1. Prepare a bounded plan. List the approved skills and why, reused copies, versions, clients, scopes, paths, the install method (install, copy or link), runtime and network effects, lock files and bundled notices.
2. Show the skill combinations that the project requires and the instruction pointers as a separate part.
3. Show the installation separately from the `AGENTS.md` edits. For each set, offer three answers: approve as shown, approve a named subset, or do not approve. One reply can approve both sets explicitly.
4. Include in the plan every action that needs approval: a new tool, an `npx` download, a replaced skill, an updated global copy, changed client settings.

- A configured workflow or a saved list of wanted skills does not approve installation.
- An approved bounded plan needs no confirmation for each command, unless its scope or effects change.
- If the owner declines installation, save only the approved configuration. Report the missing skills and the workflows that depend on them. Call no skill installed that is not installed.

## Run the approved plan

1. Run only the approved installation. Skills install independently. If one install fails, continue the other approved installs.
2. Copy complete skill directories in their original layout. Keep the bundled notices. For a skill without a license file, add the root third-party notice next to it.
3. Use `npx skills` for the clients that it supports. The reviewed release is `skills@1.9.0`; it needs Node.js 22.20 or newer. Use the approved version. See its [command reference](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/commands.md) and [supported-agent paths](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/agents.md). The kit repository is the source; the kit has no npm package.
4. Build `npx skills@1.9.0 add` with the agreed source, the exact approved `--skill` names and the selected `--agent` clients. The installer does not know the project's selection. Each skill can install alone:

   ```bash
   npx skills@1.9.0 add FOZERY/agent-workflow --skill human-text --agent codex
   npx skills@1.9.0 add FOZERY/agent-workflow --skill asd-ste100 --agent codex
   ```

5. Use `--global` only for approved global destinations. Use `--copy` only when that method is agreed. Use `--yes` only after the user approved the exact plan. Name each skill and client explicitly; use no all-skills or all-agents selector.
6. Include lock files, canonical copies and symlinks in the approved write set.
7. For a client that `npx skills` does not support, agree a documented install method. Guess no agent name.
8. Download and run a CLI only within the approved tool and download scope.
9. On a partial failure, report each operation as done, failed or not tried. Keep working installs and unrelated changes. Claim no rollback without approval. A failed install blocks only the procedures that depend on it.

## Verify the installation

1. Inspect the skill files, bundled references, notices, lock entries and client discovery.
2. Repeat the [same-name check](#check-same-name-copies).
3. Report each skill as present, discoverable, or tested by invocation. Check extra project prerequisites only for routes that need them.
4. Tell the user if the client needs a reload. Launch no other agent or changing workflow only to test discovery.
5. For diagrams, also check through [diagram configuration](diagrams.md) that a worker can read the sources and assets, write to the artifact destination, and reach the renderer, browser and network it needs. Discovery alone does not prove that a worker can make and check a preview.
6. Report which skills are ready for the agreed use, which are installed but not verified, and which are unavailable or not compatible.

The installer lock files are the install record. Keep no second copy of their data.

**Done when:** each approved skill has an observed install and discovery result or a precise blocker, and the project routes are checked separately. Unchanged installations stay, no unselected skill was added, and installation granted no permission to act.
