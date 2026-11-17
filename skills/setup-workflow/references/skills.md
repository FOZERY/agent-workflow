# Skill selection and installation

Read when packages, clients, scope or deployment change. Setup itself works alone. Original Matt packages can be installed individually but retain their runtime prerequisites; inspect the actual calls and [catalog](catalog.md#dependencies) before declaring readiness.

## Choose the workflow, not just packages

After discussing project purpose and task sources, follow [project writing configuration](writing.md). Then offer engineering packages from [the catalog](catalog.md) before conditional workflow interviews. Show purpose, installation status and recommendation. A group or joined option does not create a dependency.

Ask which skills the project needs, including user-suggested packages. Use a native choice tool or a conversation as appropriate; the catalog groups are a guide, not a fixed questionnaire.

All package selections are optional. Do not preselect recommendations as decisions. The project can approve additional prerequisites for a configured route; explain those separately. Selecting no package means no installation, without removing existing skills or instructions.

Use the owner's selection to determine which conditional workflow interviews apply. Revisit the selection before final approval only if later interview answers change its suitability.

Offer `ask-workflow` as an optional guide for workflow questions and next-step advice. It can be installed on its own before or after setup, has no required skill dependencies and recommends procedures without executing them. Selecting it does not select the rest of the catalog.

Offer bundled `excalidraw-diagram` only when visual design support is relevant. Use [diagram configuration](diagrams.md) for its conditional interview and readiness checks. Selecting it does not grant per-diagram consent or select other packages.

Keep three decisions distinct:

- **Selected for this project:** the owner's chosen procedures and any separately approved dependencies.
- **Installed and discoverable:** what is actually available to each selected client and scope.
- **Authorized behavior:** what the project permits that procedure to do.

A globally installed skill can be unnecessary or unauthorized in this project. Disabling a workflow does not mean deleting a shared global skill. Installation neither invokes a skill nor grants its actions.

## Separate packages from project requirements

The twelve project-aware Matt adaptations add only the agreed project-instructions paragraph. Original skill calls remain, including `domain-modeling` and `prototype` in Wayfinder and `codebase-design` in TDD. These helpers are included in the kit but must still be installed for the target client.

Check both original prerequisites and extra requirements of the approved project contract.
If a prerequisite is absent, obtain a bounded source/install decision or leave the affected route unavailable.
Do not silently restore removed helpers, replace required procedures or modify package prompts during setup.

Record roles, paths, language, writing routes and additional skills in root `AGENTS.md` or its project-owned references.
Do not rewrite installed reusable prompts for each project. Package maintenance is a separate change.
Installation neither invokes a skill nor authorizes global instruction edits.

## Establish the package source

The [kit catalog](catalog.md) lists the packages of this setup's kit version. Confirm that each selected package exists in the installation source before planning; an old setup summary is not evidence of availability.

For this catalog, use `FOZERY/agent-workflow` as the default source unless another was agreed. Bootstrap needs only `setup-workflow`. Install other packages only when individually selected or explicitly required by the approved project contract. Original-source credits are not installation targets.

Resolve a published revision or an approved local checkout before planning installation. Start from the source the bootstrap used: the `setup-workflow` entry in the installer lock file, `skills-lock.json` in the project or `~/.agents/.skill-lock.json` for a user-wide install, records its `source`. Install the remaining packages from that same revision. If the lock names no usable source or the remote is empty, report that and ask for the local checkout path. Installing skills does not authorize publishing the repository.

For each approved package, identify the source, version, compatibility and complete references. Preserve provenance and notices. Ask before substituting a same-named package from another source; never treat an upstream package as interchangeable merely because its name matches.

For `excalidraw-diagram`, preserve its full references, renderer, four bundled libraries and provenance notice. Some upstream material has no stated license; the repository's MIT license does not cover it automatically. Review the package notice before redistribution. A same-named upstream global installation is not the bundled workflow adaptation and must not be silently replaced.

If a package is missing or incompatible, explain the affected project route and the decision needed. Continue unrelated work without fabricating installation or readiness.

## Choose clients, scope and changes

Ask only for unresolved client and scope choices. Reuse accepted deployment and activation decisions. Recommend scope by setting:

- **Personal machine:** install user-wide, so every project runs the same kit version. Each project's rules still come from its own `AGENTS.md`.
- **Team repository:** install into the project and track the skill directories in Git, so every member runs the same version.

Different skills may use different scopes when the owner asks. Inspect only authorized installation locations for the chosen clients and establish the supported installer or documented native method with exact destinations. Each client has its own paths, and detecting a client does not select it.

### Check same-name copies

A same-named copy from another source can shadow a selected package or violate the approved project procedure. Check each selected name for each target client in both scopes; a collision does not make an unrelated skill a package dependency.

| Client | Project skills | User-wide skills | Same name in both scopes |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | The user-wide copy runs; a project copy cannot override it. |
| Codex | `.agents/skills/` | `~/.agents/skills/`, `~/.codex/skills/` | Both load, and `$name` becomes ambiguous and does not resolve by name. |
| OMP | `.omp/skills/` | `~/.omp/agent/skills/` | Unverified; read the current OMP skill documentation before relying on precedence. |

Claude Code also has a bundled `code-review`. An installed selected copy replaces `/code-review`, while `/review` keeps the client's bundled behavior. Inspect the effective version when an original implementation calls review; there is no longer a self-contained local reviewer fallback.

Identify each copy's origin through the `source` of its installer lock entry, its symlink target, or a content comparison with this kit's package. A copy counts as the kit's when its source is this kit or its content matches the kit package. Keep a matching kit copy instead of reinstalling it.

When another copy shadows or collides with a kit package, show its path, origin and effect, and let the owner choose:

- Replace the user-wide copy with the kit's. This changes every project that uses it; move the old copy to a recoverable location.
- Move the kit installation to user-wide scope.
- Keep the other copy and record the dependent route as unavailable.

Install exactly one copy per name for each client. In a team repository, record in the contract which skill names a personal install would shadow, so members can check their own machines.

Prepare a bounded plan listing approved packages and reasons, reused copies, versions, clients, scopes, paths, install/copy/link method, runtime, network effects, lock files and bundled notices. Show project-required combinations and instruction pointers separately. Availability of a package does not authorize editing instructions.

## Obtain installation approval

Present installation separately from the contract edits. Ask which parts the owner approves; one reply can explicitly approve both sets. Configuring a workflow or saving a desired skill list alone does not authorize installation. Conversely, an approved, bounded installation needs no repeated per-command confirmation unless its scope or effects change.

If the owner declines installation, save only approved configuration and report the missing skills and dependent workflows. Do not call desired packages installed. Installing a new tool, downloading an installer through `npx`, replacing an existing skill, updating a global copy or modifying client settings must be included in approval, not hidden prerequisites.

## Execute the approved plan

After configuration, execute only the approved deployment. Packages can install independently. If a configured route has project prerequisites, verify those before calling that route ready; continue unrelated approved installs after a failure.

Copy complete package directories in their original layout. Preserve bundled notices where present. For packages without a license file, include the root third-party notice alongside them as part of the approved install or export.

Use `npx skills` for clients it supports. The reviewed npm release is `skills@1.9.0`, requiring Node.js 22.20 or newer; use the approved version and consult its [command reference](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/commands.md) and [supported-agent paths](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/agents.md). Our skill repository is its source; a separate npm package for this kit is not required.

Build `npx skills@1.9.0 add` with the agreed source, exact approved `--skill` names and selected `--agent` clients. The installer does not infer project composition. For example, either package can install alone:

```bash
npx skills@1.9.0 add FOZERY/agent-workflow --skill human-text --agent codex
npx skills@1.9.0 add FOZERY/agent-workflow --skill asd-ste100 --agent codex
```

Use `--global` only for approved global destinations and `--copy` when that installation method was agreed. Non-interactive `--yes` is acceptable only after the exact plan is approved. Avoid all-skills/all-agents selectors. Account for lock files, canonical copies and symlinks in the approved write set. For an unsupported client, agree a documented installation method instead of guessing a compatible agent name. Do not download or execute a CLI outside the approved tool/download scope.

On partial failure, report each successful, failed and unattempted operation. Do not delete working installs, undo unrelated changes or claim rollback without authorization. A blocked install blocks its dependent procedures, not unrelated local work.

## Verify deployment

Inspect the requested package files, bundled references, notices, lock entries and client discovery. Repeat the [same-name check](#check-same-name-copies). Distinguish present, discoverable and tested by invocation. Check additional project prerequisites only for a route that requires them. Explain reload requirements; do not launch another agent or mutating workflow merely to test discovery.

For selected diagrams, also check worker-visible sources/assets, the configured artifact destination and renderer/browser/network prerequisites through [diagram configuration](diagrams.md). Package discovery alone does not establish that a separate worker can generate and inspect a preview.

Report which requested skills are ready for the agreed use, which are installed but not yet discovery-verified, and which are unavailable or incompatible. The installer lock files are the deployment record; keep no second copy of their data.

**Done when:** each approved package has an observed installation/discovery result or precise blocker; configured project routes are checked separately. Unchanged installations are preserved, no unselected package was added, and installation granted no operational permission.
