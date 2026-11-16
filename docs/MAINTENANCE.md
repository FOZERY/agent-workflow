# Maintaining the kit

[Overview](../README.md) · [Repository instructions](../AGENTS.md) · [Upstream baselines](UPSTREAM.md)

A prompt change is a behavior change, even when only Markdown changes. A successful install does not show that a model follows the procedure.

## Which file owns what

| File or directory | Owns |
| --- | --- |
| `skills/<name>/SKILL.md` | Invocation metadata, the ordered procedure, action limits and completion criteria |
| `skills/<name>/references/` | Conditional guidance, templates and shared supporting procedures |
| `skills/<name>/agents/openai.yaml` | Optional client-facing name, description and invocation policy |
| `FLOW.md` | How the skills connect, phase boundaries and the implementation review loop |
| `skills/setup-workflow/references/catalog.md` | Selectable skills and their groups, helper skills and the dependency graph |
| `docs/SKILLS.md` | Catalog for people: invocation modes, purpose and results; links to the dependency graph |
| `docs/SETUP.md` | Installation, configuration and the files setup creates |
| `docs/UPSTREAM.md` | Original sources, pinned baselines and adaptation decisions |
| `THIRD_PARTY_NOTICES.md` | Attribution scope, copyright notices and inherited license terms |
| `LICENSE` | License for this project's original contributions |
| Root `AGENTS.md` | Maintainer instructions and mandatory reading pointers, not the full catalog |

The setup skill's references describe contracts for consumer projects; they are not this repository's own rules. Editing a workflow prompt does not mean running that workflow here.

## Make a change

1. Find the user-visible behavior and the skills that call the affected one. Read their prompts, references and the relevant FLOW section. Decide whether this is a wording fix or a contract change.
2. A change to invocation mode, required dependencies, artifacts, model choice, human gates or publication is a contract change. Say so explicitly instead of hiding it in a refactor.
3. Edit the owning prompt or reference. Keep definitions, caveats and decision rules together; link to branch-specific detail instead of copying a process.
4. Update callers, dependencies and metadata. Naming a manual-only skill does not make it an automatic dependency. Required references must ship inside the package.
5. Update the catalogs, FLOW, the setup interview and user docs wherever the changed contract shows. Keep README short; detailed procedures live in their owning document.
6. For upstream-derived changes, follow the update procedure below and keep all inherited notices.
7. Run the checks for the affected routes and report exactly what you checked. Stop at the approved scope; commit and publication are separate actions.

To remove a package, first update or remove its callers, dependency entries and links. Keep provenance for material that other packages still use. Move the removed package to a recoverable place; do not touch users' global installations.

## Track upstream without overwriting local policy

Nothing in this repository watches or syncs upstream. Check upstream before a release, when an upstream fix looks relevant, or when the owner asks. A schedule or a bot needs its own agreement on scope and permissions.

1. Read [UPSTREAM.md](UPSTREAM.md). An imported baseline differs from a revision consulted only for ideas; an inspection date is not an acceptance.
2. Fetch the upstream revision into a separate read-only checkout or an allowed temporary folder. Resolve branches and tags to a commit and keep the exact URL. Never replace local skill folders with `main`.
3. Compare twice: **accepted baseline → candidate** shows the upstream changes, **accepted baseline → local package** shows our adaptations. Account for renamed packages and files moved under `references/`.
4. Review the whole package: references, metadata, licenses and credits. Look for new tool assumptions, required infrastructure, permissions, model choices, artifacts and dependency calls.
5. For each meaningful change, choose **adopt**, **adapt**, **reject** or **defer**, with a reason tied to this workflow. Do not bring back upstream automatic commits, fixed artifact paths or other defaults that conflict with the kit.
6. Apply the approved changes selectively. Move a baseline forward only after all its incoming changes are handled; record per-package exceptions instead of claiming the whole repository moved to one revision.
7. Check the changed routes and record the result. Updating consumer projects is a separate approved step: check local customization, scope, discovery and dependency compatibility first.

Record each update in UPSTREAM.md, in the baseline row or a dated subsection: affected packages, old, candidate and accepted revisions, key decisions, impact on local contracts, license changes and the checks performed. A deferred candidate stays a candidate. If the source does not state the copied revision, do not invent one.

## Narrow checks

For each changed package or document:

- Parse YAML frontmatter and client metadata. Check the name, description and invocation mode, and that the files agree.
- Resolve local Markdown links and anchors; check new or changed external links. Check referenced package names and required bundled files.
- Match both catalogs to the package folders: every package appears in `catalog.md` in a selection group or as a helper, and its dependency row matches the skills its prompt calls. Separately installed packages may not sit in sibling folders.
- Check Mermaid with a parser or renderer and look at the result when possible. Walk the graph against the real gates: ready requirements can skip planning, failed checks cannot reach acceptance, accepted work can stop without publication. If no renderer was used, report the visual check as not done.
- Test installation and discovery in an isolated temporary project, only for the affected packages, keeping the notices. Never change live user-wide installations as a test.
- For changed prompt behavior, walk through representative cases first. A live agent run, if approved, uses a bounded scenario and records what the agent actually did; a walkthrough on paper is not a behavior test.

There is no permanent test runner or CI here; pick the checks that fit the change. Agree new tools or external actions before adding them.

## Scenarios by affected contract

| Change | Cases to consider |
| --- | --- |
| Setup or deployment | Existing project instructions; targeted rerun; declined installation; missing dependency; same-named global and project copies; unsupported client |
| Requirements or triage | Read-only analyst source; incident that does not reproduce; overlapping active fix; forbidden tracker change |
| Testing or implementation | TDD declined; unit-only policy with SQL changes; independently written tests; missing reviewer model; stale review of uncommitted changes |
| Review and acceptance | Safe style fix next to a business decision; new human feedback; repeated finding; WIP commit versus acceptance |
| PR/MR delivery | Text-only request; unclear base branch; failed hook; existing draft; pending CI; no merge permission |
| Memory or maintenance | Unconfirmed lesson; conflict with current rules; two writers at once; recoverable artifact removal; non-default memory folder |
| Workflow advice | Question before setup; missing package; manual-only skill missing from automatic discovery; advice without execution |

## Export and release

Keep `LICENSE`, `THIRD_PARTY_NOTICES.md`, credits and complete package references in releases. When exporting single packages, include the applicable notices with the copied files; one shared notice is enough when its scope is clear and it actually ships with them.

Before publishing, check the content for secrets and private project data, confirm the source revision and package contents, and get permission to publish. After publishing, update the availability note in README and SETUP.md and check the documented remote install source. A local commit does not allow push, PR or release.

In the completion report, list separately: changed files, package discovery, static contract checks, live behavior evidence and unverified client capabilities. Do not describe the kit as an enforced autonomous system.
