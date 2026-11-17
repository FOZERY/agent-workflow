# Maintaining the kit

[Overview](../README.md) · [Repository instructions](../AGENTS.md) · [Upstream baselines](UPSTREAM.md)

A prompt change is a behavior change, even when only Markdown changes. A successful install does not show that a model follows the procedure.

## Which file owns what

| File or directory | Owns |
| --- | --- |
| `skills/<name>/SKILL.md` | Invocation metadata, the ordered procedure, action limits and completion criteria |
| `skills/<name>/references/` | Conditional guidance, templates and shared supporting procedures |
| `skills/excalidraw-diagram/` | Optional diagram procedure, worker-only generation guidance, renderer and bundled libraries with provenance |
| `skills/home-repo-init/` | Optional manual home inventory, navigation, sharing decisions and approved changes; no workflow-policy or task-planning replacement |
| `skills/<name>/agents/openai.yaml` | Optional client-facing name, description and invocation policy |
| `FLOW.md` | How the skills connect, phase boundaries and the implementation review loop |
| `skills/setup-workflow/references/catalog.md` | Package selection groups and optional project combinations |
| `docs/SKILLS.md` | Human-facing package catalog, invocation modes, purpose and standalone installation contract |
| `docs/SETUP.md` | Installation, configuration and the files setup creates |
| `skills/setup-workflow/references/writing.md` | Proposed project writing routes, loading triggers and approval |
| `skills/setup-workflow/references/AGENTS.md` | Reference structure for a generated project contract, not live repository policy |
| `docs/UPSTREAM.md` | Original sources, pinned baselines and adaptation decisions |
| `THIRD_PARTY_NOTICES.md` | Attribution scope, copyright notices and inherited license terms |
| `LICENSE` | License for this project's original contributions |
| Root `AGENTS.md` | Maintainer instructions and mandatory reading pointers, not the full catalog |

The setup skill's references describe contracts for consumer projects; they are not this repository's own rules. Editing a workflow prompt does not mean running that workflow here.

The [source policy](UPSTREAM.md#current-package-policy) distinguishes exact copies from twelve paragraph-only adaptations.
Compare complete file sets against the pinned source. For adapted packages, remove only the agreed project-instructions paragraph before byte comparison.
Preserve original skill calls and check dependency closure. Included helpers still need installation in the consumer's client; setup does not patch package prompts.
Broader local packages remain separately maintained. The former bundled implementation cycle is absent.
Packages without bundled licenses need the root third-party notice alongside their exports.

## Make a change

1. Find the user-visible behavior and the skills that call the affected one. Read their prompts, references and the relevant FLOW section. Decide whether this is a wording fix or a contract change.
2. A change to invocation mode, required dependencies, artifacts, model choice, human gates or publication is a contract change. Say so explicitly instead of hiding it in a refactor.
3. Edit the owning prompt or reference. Keep definitions, caveats and decision rules together; link to branch-specific detail instead of copying a process.
4. Update package catalogs, prerequisites and metadata descriptions. Preserve exact upstream metadata for vendored packages. Verify required references against that package's original layout.
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
5. For a vendored original, choose a complete pinned revision only with owner approval and preserve its bytes. For local adaptations, choose adopt, adapt, reject or defer explicitly. Do not silently apply a local fix or change the original's action contract.
6. Apply the approved changes selectively. Move a baseline forward only after all its incoming changes are handled; record per-package exceptions instead of claiming the whole repository moved to one revision.
7. Check the changed routes and record the result. Updating consumer projects is a separate approved step: check local customization, scope, discovery and dependency compatibility first.

Record each update in UPSTREAM.md, in the baseline row or a dated subsection: affected packages, old, candidate and accepted revisions, key decisions, impact on local contracts, license changes and the checks performed. A deferred candidate stays a candidate. If the source does not state the copied revision, do not invent one.

## Narrow checks

For each changed package or document:

- Parse YAML frontmatter and client metadata. Check the name, description and invocation mode, and that the files agree.
- Resolve local Markdown links and anchors; check new or changed external links. Check referenced package names and required bundled files.
- Match both catalogs to package folders and actual skill calls. List absent external prerequisites explicitly. Do not claim every original is self-contained or has the previous local review/acceptance cycle.
- Check Mermaid with a parser or renderer and look at the result when possible. Walk the graph against the real gates: ready requirements can skip planning, failed checks cannot reach acceptance, accepted work can stop without publication. If no renderer was used, report the visual check as not done.
- Export each affected package into an isolated temporary source and test installation/discovery with its legal notice alongside it. Report runtime prerequisite gaps separately. Do not install missing external skills or change user-wide installations as a test.
- For changed prompt behavior, walk through representative cases first. A live agent run, if approved, uses a bounded scenario and records what the agent actually did; a walkthrough on paper is not a behavior test.

There is no permanent test runner or CI here; pick the checks that fit the change. Agree new tools or external actions before adding them.

## Scenarios by affected contract

| Change | Cases to consider |
| --- | --- |
| Setup or deployment | Existing project instructions; targeted rerun; declined installation; missing dependency; same-named global and project copies; unsupported client |
| Setup interview and policy | Independent choices; custom policy by link or prose; commit allowed but push needs approval and merge is human-only; tool discovered but write not authorized; conflicting mandatory rule blocks only its action; targeted rerun retains existing permissions |
| Home inventory | Bounded authorized roots; existing home with delta-only rerun; `.git` files, worktrees and submodules deduplicated by repository identity; path collisions |
| Home visibility | Personal versus team audience; private repository names and documents; unknown provider visibility; remote credentials sanitized; secrets unread |
| Home material | Shared scope versus duplicate relationships; exact copies versus divergent variants; ownership conflicts; no newest-timestamp winner; installed packages retained |
| Home change approval | Read-only proposal; explicit copy or migration authority; dirty child preserved; approved local branch/worktree where needed; no cleanup approval means no removal |
| Home paths and Git | Portable paths; child nested inside home with explicit tracking boundaries; missing repository without clone permission; no implicit submodule, pull, commit, remote creation or push |
| Home reader access | Child instructions before work; no universal home override; child-start session and delegated worker access to shared instructions, task artifacts and complete skill packages; no assumed sibling discovery |
| Home cleanup | Destination integrity and every consumer verified before separately approved recoverable removal; legal notices retained; existing documents authoritative until approved migration |
| Requirements and planning | Read-only analyst source; existing tickets; task-only plan without a spec or tickets; existing plan revision; non-default task-artifact paths; blocked plan write; saved artifact versus chat-only draft; executor input compatibility; forbidden tracker change |
| Testing and implementation | Auto/manual TDD; representative tests; current-session/subagent/separate-session execution; unavailable capabilities |
| Review and followup | Comparison-base rule; committed versus working-tree endpoint; pre-commit coverage; auto/manual review; report versus fix-and-rereview; correction scope and cycle limits; user acceptance; required unavailable helper |
| PR/MR delivery | Text-only request; unclear base branch; failed hook; existing draft; pending CI; no merge permission |
| Memory or maintenance | Unconfirmed lesson; conflict with current rules; two writers at once; recoverable artifact removal; non-default memory folder |
| Workflow advice | Question before setup; missing package; manual-only skill missing from automatic discovery; home structure versus workflow procedures versus task plan; advice without execution or repository inventory |
| Optional design diagrams | Useful offer versus unnecessary phase; selected package without generation consent; yes or explicit request launches a separate drawing worker; no means no dispatch or diagram writes; unavailable agent, skill, assets or render permission blocks only drawing; no same-context fallback |
| Diagram context and artifacts | Coordinator reads only the short entrypoint and sends facts/status, pointers, question/audience, paths and allowed libraries; only worker loads generation guidance/library JSON; compact return contains paths, visual checks and caveats; configured parent-artifact paths; drawing consent versus design acceptance or implementation permission |
| Writing routes | First-prompt conversation; routine STE-based writing without external STE sources; explicit provenance/conformance request; an artifact draft in chat; context and lessons versus rules; mixed documents; non-English artifacts; missing or declined writing packages; a helper without inherited instructions; an authorized next action versus a missing user decision |
| Per-skill settings | No project rules; omitted versus manual setting; additional skill or coding-practice pointer; targeted rerun preserving unrelated sections |

## Export and release

Keep root legal files with repository releases. For originals without bundled notices, ship the applicable root third-party notice alongside exported packages. Preserve original package contents and complete supporting files. Local packages retain their bundled license notices.

Before publishing, check the content for secrets and private project data, confirm the source revision and package contents, and get permission to publish. After publishing, update the availability note in README and SETUP.md and check the documented remote install source. A local commit does not allow push, PR or release.

In the completion report, list separately: changed files, package discovery, static contract checks, live behavior evidence and unverified client capabilities. Do not describe the kit as an enforced autonomous system.
