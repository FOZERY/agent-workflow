# Skill catalog

[Overview](../README.md) · [Workflow](../FLOW.md) · [Setup](SETUP.md) · [Original sources](UPSTREAM.md)

Each name links to the skill's prompt, which defines its exact behavior. This is the kit's catalog, not a list of what is installed on your machine.

The catalog groups task skills into four phases: setup, task exploration, implementation and retrospective.
Use only the phases the task needs. Writing skills form a separate group and can apply in any phase.

Invocation modes:

- **Manual:** only you start it (`disable-model-invocation: true`).
- **Agent or manual:** the agent may pick it on its own, or you call it.

No mode grants permission for what the skill does.

## 1. Setup

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [setup-workflow](../skills/setup-workflow/SKILL.md) | Manual | Discuss project practices, per-skill settings and additional user requirements | Approved `AGENTS.md`, project memory and separately approved installation |
| [ask-workflow](../skills/ask-workflow/SKILL.md) | Manual | Explain the workflow, compare skills, choose the next step | Advice only; runs nothing and needs no other skill |

`ask-workflow` can also explain the next step during any other phase.

## 2. Task exploration

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [grilling](../skills/grilling/SKILL.md) | Agent or manual | Challenge an idea and find decisions you have not made yet | Agreed understanding; no file by default |
| [grill-with-docs](../skills/grill-with-docs/SKILL.md) | Manual | Interview with domain records | Calls the included `grilling` and `domain-modeling` skills |
| [domain-modeling](../skills/domain-modeling/SKILL.md) | Agent or manual | Clarify domain terms and consequential decisions | Maintained glossary and ADRs; helper for `grill-with-docs` and `wayfinder` |
| [research](../skills/research/SKILL.md) | Agent or manual | Primary-source investigation, including wayfinder research tickets | A fresh background agent writes a cited Markdown report |
| [prototype](../skills/prototype/SKILL.md) | Agent or manual | Answer a design question through a throwaway logic or UI prototype | A concrete experiment and recorded decision; helper for Wayfinder prototype tickets |
| [wayfinder](../skills/wayfinder/SKILL.md) | Manual | Explore a large effort through decision tickets | Original map, tracker, grilling/domain-modeling, research and prototype procedures |
| [to-spec](../skills/to-spec/SKILL.md) | Manual | Synthesize the agreed discussion | Confirmed test seams and a specification published to the tracker |
| [to-tickets](../skills/to-tickets/SKILL.md) | Manual | Split work into vertical slices | Approved dependency-ordered tickets using upstream publication conventions |

`wayfinder` tickets ask questions; implementation tickets describe work. A ready spec from an analyst skips `to-spec` and `to-tickets`.

## 3. Implementation

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [tdd](../skills/tdd/SKILL.md) | Agent or manual | Test-first red–green cycles | One test and minimal implementation at a time; conditional `codebase-design` call |
| [codebase-design](../skills/codebase-design/SKILL.md) | Agent or manual | Reason about module interfaces, depth and testability | Shared design vocabulary and supporting methods; conditional helper for TDD |
| [implement](../skills/implement/SKILL.md) | Manual | Implement a task | Calls TDD where possible, reviews and commits to the current branch |
| [implement-spec](../skills/implement-spec/SKILL.md) | Manual | Implement a ticket graph | Integration branch, ticket worktrees, TDD, review and upstream delivery/cleanup |
| [code-review](../skills/code-review/SKILL.md) | Agent or manual | Review a committed diff against a fixed point | Parallel Standards and Spec review agents; no bundled local acceptance cycle |

These skills add a project-instructions paragraph to their upstream procedures. Specified project settings apply; other settings retain upstream defaults. Original dependencies remain. They do not contain the former local independent-test-author or three-round acceptance cycle.

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

## Dependencies

The fourteen M1-derived Matt packages retain original procedures, dependencies and layout. Twelve add only the [project-instructions paragraph](UPSTREAM.md#current-package-policy).
The [setup catalog](../skills/setup-workflow/references/catalog.md#dependencies) records their calls. All fixed helper dependencies are included in the kit.
They must still be installed in the target client. Wayfinder can require additional skills named in a map's Notes. Installation does not establish runtime readiness.

Our setup and local writing packages remain separately installable. Setup records approved project combinations and permissions without modifying the original prompts.
Original packages without a bundled license require the applicable root notice alongside an export.
