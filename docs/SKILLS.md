# Skill catalog

[Overview](../README.md) · [Workflow](../FLOW.md) · [Setup](SETUP.md) · [Original sources](UPSTREAM.md)

Each name links to the skill's prompt, which defines its exact behavior. This is the kit's catalog, not a list of what is installed on your machine.

Invocation modes:

- **Manual:** only you start it (`disable-model-invocation: true`).
- **Agent or manual:** the agent may pick it on its own, or you call it.

No mode grants permission for what the skill does.

## Preparation and guidance

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [setup-workflow](../skills/setup-workflow/SKILL.md) | Manual | Configure or change project rules, permissions and installed skills | Approved `AGENTS.md`, project memory files and, approved separately, installed skills |
| [ask-workflow](../skills/ask-workflow/SKILL.md) | Manual | Explain the workflow, compare skills, choose the next step | Advice only; runs nothing and needs no other skill |

## Understanding and planning

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [grilling](../skills/grilling/SKILL.md) | Agent or manual | Challenge an idea and find decisions you have not made yet | Agreed understanding; no file by default |
| [grill-with-docs](../skills/grill-with-docs/SKILL.md) | Manual | Clarify domain terms and decisions through an interview | Agreed terms and decision records where the project allows |
| [research](../skills/research/SKILL.md) | Agent or manual | Deep investigation with reusable evidence | Dated Markdown report with sources, in an agreed location |
| [wayfinder](../skills/wayfinder/SKILL.md) | Manual | Work through a large uncertain effort with decision tickets | Decision map with open questions and linked evidence |
| [to-spec](../skills/to-spec/SKILL.md) | Manual | Turn an agreed discussion into requirements | Spec or amendments in the project's requirements source |
| [to-tickets](../skills/to-tickets/SKILL.md) | Manual | Split approved work into checkable slices | Tasks with real dependencies, or an unpublished proposal |

`wayfinder` tickets ask questions; implementation tickets describe work. A ready spec from an analyst skips `to-spec` and `to-tickets`.

## Implementation and delivery

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [tdd](../skills/tdd/SKILL.md) | Manual | Test-first cycles; a fresh subagent writes the tests | Tests, with the red and green runs actually observed |
| [implement](../skills/implement/SKILL.md) | Manual | Implement one agreed task | Checked code, independent review, an explanation and your acceptance |
| [implement-spec](../skills/implement-spec/SKILL.md) | Manual | Implement a spec and its slices | The same, for the integrated result of all slices |
| [code-review](../skills/code-review/SKILL.md) | Agent or manual | Review committed and uncommitted changes against standards and requirements | Read-only findings, split into safe fixes and decisions, with coverage limits |

TDD is optional; required checks are not. `implement` and `implement-spec` always end with independent review and your explicit acceptance. `code-review` also works on its own. There is no commit skill: commit rules come from the project.

## Writing and maintenance

| Skill | Invocation | Use it for | Result |
| --- | --- | --- | --- |
| [human-text](../skills/human-text/SKILL.md) | Agent or manual | Clear text and documents for people | The style applied to the requested text; enabling it for every session is a separate setup choice |
| [refactor-docs](../skills/refactor-docs/SKILL.md) | Agent or manual | Improve existing documents without changing their meaning | Targeted edits that keep facts and decisions |
| [writing-for-agents](../skills/writing-for-agents/SKILL.md) | Agent or manual | Write skills, `AGENTS.md`/`CLAUDE.md`, `CONTEXT.md` and `LESSONS.md` for agents | Installed with setup; setup and `retro` follow it when they write agent documents |
| [retro](../skills/retro/SKILL.md) | Manual | Discuss decisions, mistakes and lessons | Approved lessons and a short entry about recent work |
| [cleanup](../skills/cleanup/SKILL.md) | Manual | Retire outdated working files | A proposed plan, then only the approved, recoverable changes |

`handoff` is not part of the kit. Setup does not remove your own skill with that name.

## Dependencies

The dependency graph is in [the setup package's catalog](../skills/setup-workflow/references/catalog.md#dependencies), so setup has it in any project. The installer does not read it; setup does. Setup installs the selected skills with everything they require, reuses compatible installed copies and checks access before installing a skill that needs it. If you decline a required dependency, only the skill that needs it becomes unavailable.

A reviewer configured by the project also loads the review skills the project requires. Files in a skill's `references/` folder belong to that skill; they are not separate skills.
