# Skill catalog

[Overview](../README.md) · [Workflow](../FLOW.md) · [Setup](SETUP.md) · [Original sources](UPSTREAM.md)

Each name links to the skill's prompt, which defines its exact behavior. This is the kit's catalog, not a list of what is installed on your machine.

The catalog groups task skills into four phases: setup, task exploration, implementation and retrospective.
Use only the phases the task needs. Writing and diagram support form separate groups, not additional phases.

Invocation modes:

- **Manual:** only you start it (`disable-model-invocation: true`).
- **Agent or manual:** the agent may pick it on its own, or you call it.

No mode grants permission for what the skill does.

## 1. Setup

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [home-repo-init](../skills/home-repo-init/SKILL.md) | Manual | Establish or revise a navigation and shared-material home for multiple repositories | Read-only inventory and proposed changes; approved home structure without moving child code |
| [setup-workflow](../skills/setup-workflow/SKILL.md) | Manual | Agree project rules, permissions, per-skill settings and tool prerequisites | Approved `AGENTS.md`, project memory and separately approved skill installation |
| [ask-workflow](../skills/ask-workflow/SKILL.md) | Manual | Explain the workflow, compare skills, choose the next step | Advice only; runs nothing and needs no other skill |

`ask-workflow` can also explain the next step during any other phase.

`home-repo-init` is optional and standalone. Initialize the home first, then use `setup-workflow` if its workflow procedures need configuration.
Use `to-plan` for an individual task plan, not home structure. Home navigation preserves child instructions and requires verified access from each session or worker.
The [package](../skills/home-repo-init/SKILL.md) and [source ledger](UPSTREAM.md) record the AI Hero article as conceptual inspiration.

## 2. Task exploration

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [grilling](../skills/grilling/SKILL.md) | Agent or manual | Challenge an idea and find decisions you have not made yet | Agreed understanding; no file by default |
| [grill-with-docs](../skills/grill-with-docs/SKILL.md) | Manual | Interview with domain records | Calls the included `grilling` and `domain-modeling` skills |
| [domain-modeling](../skills/domain-modeling/SKILL.md) | Agent or manual | Clarify domain terms and consequential decisions | Maintained glossary and ADRs; helper for `grill-with-docs` and `wayfinder` |
| [research](../skills/research/SKILL.md) | Agent or manual | Primary-source investigation, including wayfinder research tickets | A fresh background agent writes a cited Markdown report |
| [prototype](../skills/prototype/SKILL.md) | Agent or manual | Answer a design question through a throwaway logic or UI prototype | A concrete experiment and recorded decision; helper for Wayfinder prototype tickets |
| [wayfinder](../skills/wayfinder/SKILL.md) | Manual | Explore a large effort through decision tickets | Original map, tracker, grilling/domain-modeling, research and prototype procedures |
| [to-plan](../skills/to-plan/SKILL.md) | Manual | Plan an existing task without creating a spec or tickets | One saved task-linked Markdown plan with work packages, dependencies and checks; no implementation |
| [to-spec](../skills/to-spec/SKILL.md) | Manual | Synthesize the agreed discussion | Confirmed test seams and a specification published to the tracker |
| [to-tickets](../skills/to-tickets/SKILL.md) | Manual | Split work into vertical slices | Approved dependency-ordered tickets using upstream publication conventions |

`wayfinder` tickets ask questions; implementation tickets describe work. A ready task can skip spec/ticket authoring and use `to-plan` when planning is useful, or go directly to execution. Configure an executor to read the plan and its source task; `implement-spec` still requires its specification and ticket graph.

## 3. Implementation

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [tdd](../skills/tdd/SKILL.md) | Agent or manual | Test-first red–green cycles | One test and minimal implementation at a time; conditional `codebase-design` call |
| [codebase-design](../skills/codebase-design/SKILL.md) | Agent or manual | Reason about module interfaces, depth and testability | Shared design vocabulary and supporting methods; conditional helper for TDD |
| [implement](../skills/implement/SKILL.md) | Manual | Implement a task | Calls TDD where possible and defaults to reviewing a scoped working-tree snapshot before an authorized commit |
| [implement-spec](../skills/implement-spec/SKILL.md) | Manual | Implement a ticket graph | Integration branch, ticket worktrees, TDD, committed review after ticket merges and upstream delivery/cleanup |
| [code-review](../skills/code-review/SKILL.md) | Agent or manual | Review a pinned working-tree snapshot or an explicit committed branch, PR or commit | Standards and Spec reviewers compare the same pinned changes against a fixed base |

The working-tree endpoint includes intended staged, unstaged and nonignored untracked changes within the task's file scope. It leaves the real Git index unchanged.
Explicit project settings apply. The bundled procedures do not include the former local independent-test-author or three-round acceptance cycle.

## 4. Retrospective

Use `retro` to examine a session's evidence and propose improvements.
The maintenance tools below can also run between tasks; they are not mandatory retrospective steps.

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [retro](../skills/retro/SKILL.md) | Manual | Improve the agent environment from session evidence | Calls `writing-for-agents` and presents prioritized improvement candidates |
| [refactor-docs](../skills/refactor-docs/SKILL.md) | Agent or manual | Improve documentation and factual memory without changing meaning | Self-contained editing procedure; additional styles come from the task or project |
| [cleanup](../skills/cleanup/SKILL.md) | Manual | Retire outdated working files | A proposed plan, then only the approved, recoverable changes |

`handoff` is not part of the kit. Setup does not remove your own skill with that name.

## Writing skills

These skills guide how text is written, independently of the current task phase.

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [asd-ste100](../skills/asd-ste100/SKILL.md) | Agent or manual | Technical prose for people or agents, including docs, ADRs, specs, tickets and memory | Standalone STE-based guidance with principles and before/after examples; no automatic conformance claim |
| [writing-for-agents](../skills/writing-for-agents/SKILL.md) | Agent or manual | Write documents that agents consume | Exact upstream writing guidance and sibling `SKILL-MECHANICS.md` |
| [human-text](../skills/human-text/SKILL.md) | Agent or manual | Clear, natural replies, explanations and prose for people | A standalone writing style; project instructions decide its scope and startup loading |

## Diagram support

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [excalidraw-diagram](../skills/excalidraw-diagram/SKILL.md) | Agent or manual | Offer a useful design diagram; delegate drawing only after user consent | Editable `.excalidraw` source and PNG preview beside the parent artifact, with visual-check results and caveats |

This optional package includes four [libraries](../skills/excalidraw-diagram/references/libraries.md). It is not an external skill prerequisite.
Selection or installation does not authorize drawing. An explicit diagram request counts as consent.
An approved request uses a separate drawing subagent; declined requests continue without diagram work.
Unavailable delegation, required assets or render permission block only this branch. There is no same-context generation fallback.
Decisions and contracts remain in text; a diagram does not replace a prototype or imply user acceptance.
See [project setup rules](../skills/setup-workflow/references/AGENTS.md) and the package prompt for permissions, renderer prerequisites and the compact worker handoff.

## Dependencies

The [source ledger](UPSTREAM.md#current-package-policy) records the M1 baselines and local adaptations, including the changes to `code-review` and `implement`.
The [setup catalog](../skills/setup-workflow/references/catalog.md#dependencies) records their calls. All fixed helper dependencies are included in the kit.
They must still be installed in the target client. Wayfinder can require additional skills named in a map's Notes. Installation does not establish runtime readiness.

Our setup and local writing packages remain separately installable. Setup records approved project combinations and permissions without modifying the original prompts.
`home-repo-init` requires no other skill or specific orchestration tool. Its optional handoff to `setup-workflow` is a user choice, not a dependency call.
Original packages without a bundled license require the applicable root notice alongside an export.
