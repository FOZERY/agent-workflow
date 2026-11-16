# Skill selection and installation

Read this on initial setup, or when the user changes the workflow's skill set, target clients, installation scope or deployment. The setup skill itself needs no other skills to conduct this interview. Installing the selected workflow's dependencies is a separate, approved stage after its configuration is saved.

## Choose the workflow, not just packages

After discussing project purpose and task sources, follow [existing-installation checks and optional writing activation](human-text.md). Then offer the selectable skills from [the kit catalog](catalog.md) before conditional workflow interviews, using its four-question layout. Show each option's purpose, known installation status and recommendation. Helper skills come in only as dependencies of the selected callers.

Ask: "Which skills would you like to use in this project?" Use the client's native multi-select question tool when available, one question per catalog group in a single call. Otherwise show the same groups as a numbered list and accept names, numbers or `none`; plain Markdown checkboxes are not interactive controls.

Every top-level skill is optional; there is no mandatory baseline or fixed pipeline. Once a skill is selected, its required dependencies are mandatory for that selection, not independent optional checkboxes. Offer recommendations without treating them as selections, and preselect only owner-requested suggested defaults. If the owner declines standalone style integration and selects no other packages, skip installation entirely. An empty engineering selection does not cancel a separately approved style installation.

Use the owner's selection to determine which conditional workflow interviews apply. Revisit the selection before final approval only if later interview answers change its suitability.

Offer `ask-workflow` as an optional guide for workflow questions and next-step advice. It can be installed on its own before or after setup, has no required skill dependencies and recommends procedures without executing them. Selecting it does not select the rest of the catalog.

Keep three decisions distinct:

- **Selected for this project:** the owner's chosen procedures and any separately approved dependencies.
- **Installed and discoverable:** what is actually available to each selected client and scope.
- **Authorized behavior:** what the project permits that procedure to do.

A globally installed skill can be unnecessary or unauthorized in this project. Disabling a workflow does not mean deleting a shared global skill. Installation neither invokes a skill nor grants its actions.

## Explain omissions and resolve dependencies

Before confirming the set, explain relevant omissions once, without pressuring the owner to select more. Without `grilling`, its standalone interview procedure is unavailable, but setup still conducts its own interview. Without `implement`, that implementation command is unavailable; other project-authorized ways of implementing work are not automatically prohibited.

Take each selected skill's required packages from [the dependency table](catalog.md#dependencies) and follow them transitively until the set is complete. For a package version that differs from this kit's, read its actual skill calls instead.

The `human-text` dependency of `implement` and `implement-spec` serves the parent's walkthrough only; it neither enables session-wide style activation nor becomes a requirement of standalone `code-review`. The configured reviewer must also be able to load any additional review skills the project requires. Explain that selecting an implementation route includes independent review, an explanation of the result and human acceptance.

Show each selected skill's dependency chain, why each dependency is required, and its installation/discovery status for each target client. Reuse compatible, loadable global or project installations instead of adding duplicate copies. Plan shared dependencies once. A package installed for one client does not satisfy another client's requirement unless that client can actually load it.

If a required dependency was unchecked or is missing, explain that the caller cannot be installed for use without it. Ask the owner to approve the complete bundle, use an already available compatible dependency, drop the caller, or keep the requested route configured but undeployed. An alternative is valid only where the caller actually supports it. Approval of one selected skill is not silent approval to download its prerequisites or change global style instructions.

Never deploy a new caller while its required dependencies are missing, incompatible, unreadable or unapproved. If the owner keeps an unresolved selection, record the route as unavailable and leave that caller uninstalled; unrelated selections can proceed. Existing incomplete installations are reported, not deleted or claimed ready. Missing dependencies do not make the whole catalog mandatory.

## Establish the source and dependency closure

The [kit catalog](catalog.md) lists the packages of this setup's kit version. Confirm that each selected package exists in the installation source before planning; an old setup summary is not evidence of availability.

For this workflow, use `FOZERY/agent-workflow` as the default repository source, not the upstream authors' repositories. Bootstrap installs `setup-workflow` and `writing-for-agents`; setup installs only the owner's selected packages, their dependencies and `human-text` if accepted. Credits are not installation targets. Agree any different source explicitly.

Resolve a published revision or an approved local checkout before planning installation. Start from the source the bootstrap used: the `setup-workflow` entry in the installer lock file, `skills-lock.json` in the project or `~/.agents/.skill-lock.json` for a user-wide install, records its `source`. Install the remaining packages from that same revision. If the lock names no usable source or the remote is empty, report that and ask for the local checkout path. Installing skills does not authorize publishing the repository.

For each selected skill and dependency, identify the source, reviewed version or commit, actual package and compatibility with project policy and the target client. Preserve provenance and bundled support files. An unchanged upstream skill is not interchangeable with a planned project-aware adaptation. Ask before selecting an external replacement; never silently fetch a same-named skill to fill a gap.

If a package is missing or incompatible, explain the affected workflow and the available decision: an explicitly approved compatible source, a different agreed route or keeping that dependent workflow unavailable. Continue unaffected setup; do not fabricate an installation or declare that workflow ready.

## Choose clients, scope and changes

Ask only for unresolved choices: which agents receive the skills, and in which scope. Reuse the `human-text` installation and activation choices already established. Recommend a scope by setting:

- **Personal machine:** install user-wide, so every project runs the same kit version. Each project's rules still come from its own `AGENTS.md`.
- **Team repository:** install into the project and track the skill directories in Git, so every member runs the same version.

Different skills may use different scopes when the owner asks. Inspect only authorized installation locations for the chosen clients and establish the supported installer or documented native method with exact destinations. Each client has its own paths, and detecting a client does not select it.

### Check same-name copies

A same-named skill from another source breaks the kit's callers even when the kit's own copy is installed. For example, an upstream `code-review` lacks `references/implementation-cycle.md`, so `implement` stops at review. Check every selected skill and every dependency, for each target client, in both scopes:

| Client | Project skills | User-wide skills | Same name in both scopes |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | The user-wide copy runs; a project copy cannot override it. |
| Codex | `.agents/skills/` | `~/.agents/skills/`, `~/.codex/skills/` | Both load, and `$name` becomes ambiguous and does not resolve by name. |
| OMP | `.omp/skills/` | `~/.omp/agent/skills/` | Unverified; read the current OMP skill documentation before relying on precedence. |

Claude Code also ships a bundled `code-review`. An installed kit `code-review` replaces it for `/code-review`, while the bundled alias `/review` keeps running the bundled skill. Without a kit copy, `/code-review` runs the bundled skill, which lacks the implementation cycle.

Identify each copy's origin through the `source` of its installer lock entry, its symlink target, or a content comparison with this kit's package. A copy counts as the kit's when its source is this kit or its content matches the kit package. Keep a matching kit copy instead of reinstalling it.

When another copy shadows or collides with a kit package, show its path, origin and effect, and let the owner choose:

- Replace the user-wide copy with the kit's. This changes every project that uses it; move the old copy to a recoverable location.
- Move the kit installation to user-wide scope.
- Keep the other copy and record the dependent route as unavailable.

Install exactly one copy per name for each client. In a team repository, record in the contract which skill names a personal install would shadow, so members can check their own machines.

Prepare a bounded plan listing selected roots and their required dependency closure, reasons for prerequisite additions, reused installations, sources/versions, clients, scopes, paths, install/copy/link method, installer/runtime, network effects, lock files and legal-notice destinations. Include style instruction targets and exact pointer text only when session-wide writing activation was selected; a required style package alone does not authorize a pointer. Avoid duplicating lock-file facts in permanent instructions.

## Obtain installation approval

Present installation separately from the contract edits. Ask which parts the owner approves; one reply can explicitly approve both sets. Configuring a workflow or saving a desired skill list alone does not authorize installation. Conversely, an approved, bounded installation needs no repeated per-command confirmation unless its scope or effects change.

If the owner declines installation, save only approved configuration and report the missing skills and dependent workflows. Do not call desired packages installed. Installing a new tool, downloading an installer through `npx`, replacing an existing skill, updating a global copy or modifying client settings must be included in approval, not hidden prerequisites.

## Execute the approved plan

After the configuration stage, execute the approved bundle yourself. Install or verify prerequisites first, then install each caller only after its required dependencies are loadable by the same target client. A bundle is one approved deployment, not necessarily one CLI command. Stop an affected caller if a prerequisite fails; continue independent approved bundles and report partial results. Keep complete package directories, support files and notices, preserve unrelated installations and edits, and stop an operation if its effects differ from approval.

For separate skill installation or export, preserve applicable copyright notices and full license terms even when the source stores them centrally. This kit uses repository-root `LICENSE` for original contributions and `THIRD_PARTY_NOTICES.md` for inherited material; preserve both in approved accompanying distribution material, including any retained package credits. A shared notice for several skills is sufficient when its coverage is clear. Do not assume a skill-directory-only installer also copies root files. Include these copies in the approved plan; if the required notices cannot be preserved, block the affected distribution rather than omit them.

Use `npx skills` for clients it supports. The reviewed npm release is `skills@1.9.0`, requiring Node.js 22.20 or newer; use the approved version and consult its [command reference](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/commands.md) and [supported-agent paths](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/docs/agents.md). Our skill repository is its source; a separate npm package for this kit is not required.

Build `npx skills@1.9.0 add` with the agreed repository/revision or local source, exact approved names through `--skill`, and selected clients through `--agent`. Include dependencies only after bundle approval; `npx skills` does not infer this workflow's dependency graph. For example, after publication, if project-level Codex needs both `refactor-docs` and its missing dependency:

```bash
npx skills@1.9.0 add FOZERY/agent-workflow --skill human-text --agent codex
```

Verify that Codex can load the dependency and its references before installing the caller:

```bash
npx skills@1.9.0 add FOZERY/agent-workflow --skill refactor-docs --agent codex
```

Use `--global` only for approved global destinations and `--copy` when that installation method was agreed. Non-interactive `--yes` is acceptable only after the exact plan is approved. Avoid all-skills/all-agents selectors. Account for lock files, canonical copies and symlinks in the approved write set. For an unsupported client, agree a documented installation method instead of guessing a compatible agent name. Do not download or execute a CLI outside the approved tool/download scope.

On partial failure, report each successful, failed and unattempted operation. Do not delete working installs, undo unrelated changes or claim rollback without authorization. A blocked install blocks its dependent procedures, not unrelated local work.

## Verify deployment

Inspect package files, references, installer lock entries and the selected client's discovery mechanism for every requested root and its transitive prerequisites. Repeat the [same-name check](#check-same-name-copies) so each name resolves to the kit copy. Distinguish present on disk, discoverable and tested by invocation. A caller is ready only when its required closure is loadable in that client's effective scope. Explain reload requirements; do not launch another agent or exercise a mutating workflow just to test discovery without permission.

Report which requested skills are ready for the agreed use, which are installed but not yet discovery-verified, and which are unavailable or incompatible. The installer lock files are the deployment record; keep no second copy of their data.

**Done when:** the selected roots and required dependency closure are explicit for each client, every deployment effect was approved, and each requested bundle is verified or has a precise blocker. No new caller was deployed without its prerequisites; unchanged installations are preserved and no workflow gains permissions from installation.
