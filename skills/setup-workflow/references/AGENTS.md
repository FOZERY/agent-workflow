# Structure of the generated AGENTS.md

Read this file before you draft a project's `AGENTS.md`. The outline below is a template. It is not active policy and grants no permissions.

## Drafting rules

1. **Size.** Keep the file under 300 lines, including the core block. Put each procedure, standard, example list and long fact set in `<agent-docs>/project/` and link it.
2. **Content.** The file holds five things: what the project is, its mandatory constraints and permissions, its main commands and tools, the workflow, and a table of pointers to details. The workflow is the core block and the skill sections. Everything else goes to a project file or stays in its existing source.
3. Fill the fields from the setup conversation. Omit the sections of unselected skills and every field without an agreed answer.
4. Keep existing headings and the user's additions.
5. Keep shared sources, paths and permissions in the shared sections. A skill section holds only the settings and facts of that skill.
6. Write a section for every selected skill, also when it has no other setting. If the skill has no `trigger` setting, start the section with one filled line in this format: `Runs: <manual: the user calls the skill | auto: <caller> calls it at <stage>>. Phase: <phase from the phase list, or "any" for a skill outside it>.` The outline shows this line as `Runs: <runs>. Phase: <phase>.` Then give the values of its settings and at most five lines of project facts. Move a longer procedure to a project file and point to it.
7. For a selected skill that the outline does not list, add a section with its exact name.
8. Write the value of a setting only. Its meaning stays in `### Skill settings` of the core block.
9. Give each pointer a trigger: "Read X when Y."
10. List only the commands that an agent needs often, and name the file that holds the rest. Do not copy what the environment already holds, such as the full script list or config values.
11. For writing-style pointers, use [writing routes](writing.md). For memory, use [project artifacts](project-artifacts.md). For diagrams, use [diagram configuration](diagrams.md).
12. For a multi-repository home, keep its navigation owner and add the `Related repositories` section. Omit that section for one repository.
13. For an extra coding practice, link its source in the relevant skill section. Do not copy the guide.
14. For an addition without an agreed answer, record the blocked action and its owner. Write no placeholder instruction.

## Project files

Project rules that are too long for `AGENTS.md` go to `<agent-docs>/project/`. These names are defaults. The owner can choose others.

| File | Holds | Read when |
| --- | --- | --- |
| `architecture.md` | Modules, boundaries, data flow, external systems | You change a module boundary or add a module. |
| `standards.md` | Coding standards, practices, examples | You write or review code. |
| `testing.md` | Test types, seams, infrastructure, mocking limits | You write or change a test. |
| `delivery.md` | Commit convention, PR and deploy procedure, templates | You commit, push or open a PR. |
| `review.md` | Review standards, comparison base, evidence rules | Before review. |

Create a file only when the project has content for it. If an existing source holds the content, link it and do not copy it.

## Automation settings

The agent reads these settings as instructions, not as runtime flags. Their meanings live in `### Skill settings` of the [core block](core-rules.md#block). Each section holds these settings:

| Section | Settings |
| --- | --- |
| `investigate` | `execution`, `researcher` |
| `implement` | `worker` |
| `verify` | `trigger`, `execution`, `skill` |
| `tdd` | `trigger`, `execution`, `skill` |
| `simplify-codebase` | `trigger`, `execution`, `skill`, `finder` |
| `code-review` | `trigger`, `skill`, `standards-reviewer`, `spec-reviewer`, `followup`, `rounds` |
| Workflow rules | `search`, recorded in the core block and not in a skill section |

## Review coverage

Ask each question that is not answered yet:

1. When does review run: before the commit, after it, or at both points?
2. At each point, what does it compare: commits, or a base and the working tree?
3. How is the base selected: the target branch, a named revision, or a project rule?
4. Which changes are in scope? For working-tree review, say which of staged, unstaged and untracked changes are included.

The follow-up and the round limit are questions 7 and 8 in step 2.3 of [setup](../SKILL.md#23-implementation-tdd-simplify-and-review).
For `fix-and-rereview`, also agree what the agent can fix and the stop conditions. Stop conditions include a disputed requirement and a check that cannot run.
Report-only review gives no permission to fix. If these options do not fit, use the project's own procedure.

By default, `implement` asks for a working-tree snapshot of the task files for its pre-commit review. `code-review` captures the intended staged, unstaged and non-ignored untracked changes. Branch and PR review compare commits, unless the agreed procedure selects another endpoint.

If the project selects another reviewer or other coverage, check that its procedure can review the intended files at that point. If it cannot, report the gap and keep the route blocked. Setup does not make a commit only so that review can run.

## Outline

Replace each angle-bracket field with the agreed rule.

```markdown
# <Project name>

## Project
<What the project is and who uses it, in 2-4 sentences. Stack. Pointers to the authoritative requirements, glossary and ADRs.>

## Constraints
<Mandatory restrictions and when to check them. Link the authoritative rule. Do not copy private policy.>
<Autonomy and human checkpoints. Permissions for read-only exploration, implementation delegation, concurrent work and external writes.>
<Environment boundaries.>
The user decides whether to accept the work.

## Commands and tools
| Task | Command |
| --- | --- |
| <Typecheck, one test file, full tests, lint, run locally> | <command> |

<Shared tools and MCP integrations: purpose, trigger, approved targets and data, allowed actions, prerequisite. Put skill-specific tools under the owning skill.>

## Project rules
Read a file when its trigger applies.
| Source | Read when |
| --- | --- |
| <`<agent-docs>/project/...` file, tracker, specification, ticket, plan, research, glossary or ADR source> | <trigger> |

<Artifact owners, formats and visibility, if they are not obvious from the table.>

## Workflow rules
`## Workflow rules` is mandatory for every session and every skill.
<Copy the block from [core rules](core-rules.md) with its markers and fill its fields.>

## Related repositories
<Home or repository-index pointer, with each repository's purpose and agreed portable location.>
<Before child work, read its applicable instructions. Shared-rule and skill loading for child-start sessions and workers.>
<Ownership and access rules for cross-repository task artifacts. Cloning and worktree permissions remain separate.>

## Writing
<Conversation language and writing-for-people startup pointer, if selected.>
<Artifact language and writing-technical pointer, if selected.>

## Skills
Each selected skill has a section below. Before you run a skill, read its section.
The section wins over the skill's own defaults. Keep the rest of the skill's procedure unchanged.
If a required step cannot satisfy applicable constraints, report the conflict.

### setup-home-repo
Runs: <runs>. Phase: <phase>.
<Approved inventory roots, home membership and shared-material ownership when this skill is selected.>
<Migration boundaries and required approval; existing child code, instructions and installed skills retain their owners.>

### investigate
Runs: <runs>. Phase: <phase>.
execution: <subagent | current-session>
researcher: <agent, model and reasoning effort for the researcher subagents>
The agent only reads every source below.
<Each source in the user's words, with the steps to open it.>
<Whether the agent may read production.>
<Facts file location, if not the default.>

### grilling
Runs: <runs>. Phase: <phase>.
<Project discussion context and decision boundaries, if needed.>
For relationships or alternatives worth visualizing, use [draw-diagram](#draw-diagram).

### grill-with-docs
Runs: <runs>. Phase: <phase>.
<Documents to consult and their authority.>
<Where to propose or record agreed terms and decisions; who approves changes.>
For relationships or alternatives worth visualizing, use [draw-diagram](#draw-diagram).

### domain-modeling
Runs: <runs>. Phase: <phase>.
<Authoritative glossary and ADR locations, formats and domain contexts.>
<Approval and write rules for resolved terms and consequential decisions.>
For domain relationships or decision alternatives worth visualizing, use [draw-diagram](#draw-diagram).

### research
Runs: <runs>. Phase: <phase>.
<Permitted sources, evidence expectations and report destination.>
<Delegation preferences within the working agreement.>

### wayfinder
Runs: <runs>. Phase: <phase>.
<Map, child-ticket and dependency representation.>
<Claim and resolution procedures; experiment, branch and publication constraints.>
For relationships or alternatives worth visualizing, use [draw-diagram](#draw-diagram).

### prototype
Runs: <runs>. Phase: <phase>.
<Permitted experiment surfaces, data and environment boundaries.>
<Artifact location, viewing method and capture/integration permissions.>
For a supporting sketch, use [draw-diagram](#draw-diagram); it does not replace the runnable prototype.

### to-plan
Runs: <runs>. Phase: <phase>.
<Task-linked plan location, naming, visibility, approval and revision rules.>
<Receiving executor and the instructions that let it consume the plan plus its source task.>
For interactions or architecture worth visualizing, use [draw-diagram](#draw-diagram).

### to-spec
Runs: <runs>. Phase: <phase>.
<Requirement sources, specification format, destination and publication procedure.>
For interactions or architecture worth visualizing, use [draw-diagram](#draw-diagram).

### to-tickets
Runs: <runs>. Phase: <phase>.
<Ticket format, granularity, dependency representation and destination.>
<Approval, readiness vocabulary and publication procedure.>

### draw-diagram
Runs: <runs>. Phase: <phase>.
<Readable installed package entrypoint. Designated delegation tool, including Orca if selected.>
<Task-artifact destination, naming, visibility and revision rules. Approved libraries and rendering permissions.>
Draw only after the user consents. An explicit request for the diagram counts as consent. Package selection is not consent.
After consent, follow the linked package procedure: a separate subagent generates and checks the diagram.
If a prerequisite is missing, report a diagram-only blocker and continue in text.
Decisions and contracts stay authoritative in text. A diagram neither replaces a runnable prototype nor approves the design.

### tdd
trigger: <auto | manual>
execution: <current-session | subagent | separate-session>
skill: <installed path of tdd/SKILL.md per client>

Test types, seams, infrastructure and mocking limits: read `<agent-docs>/project/testing.md` when you write a test.

### implement
Runs: <runs>. Phase: <phase>.
worker: <agent, model and reasoning effort for workers>

<Expected task inputs and implementation boundaries.>
<If plan-based execution is selected: read the approved plan and source task as implementation input. Recheck relevant code before editing.>
Use the TDD, simplify and review settings in this document.
Workers read `<installed path of implement/WORKER.md per client>`.
<Session tool for workers, approval for dispatch, and branch, worktree or workspace isolation rules.>
<Integration owner, target branches and delivery procedure per repository.>
<Checkpoints before returning the result to the user.>

### verify
trigger: <auto | manual>
execution: <current-session | subagent | separate-session>
skill: <installed path of verify/SKILL.md per client>

<Where to check: local run with test data, end-to-end run, test namespace or staging. How to reach it, in the user's words.>
<Tools and access: for example the kubectl context and namespace, the browser tool, test users. Credentials only as variable or config names.>
<Actions that need approval, for example a deploy to staging or writes to a shared environment.>
<Evidence location, if not `.verify/<run>/`.>
Long procedure: read `<agent-docs>/project/verification.md` before a check.

### simplify-codebase
trigger: <auto | manual>
execution: <current-session | subagent | separate-session>
skill: <installed path of simplify-codebase/SKILL.md per client>
finder: <agent, model and reasoning effort for the simplification finder>

Coding standards and code that simplify-codebase must leave alone: read `<agent-docs>/project/standards.md` before simplifying.
<Who consumes the code: published interfaces, released versions, stored data, and which input is untrusted. Compatibility or migration code that must stay.>
<Checks to run after the edits.>

### code-review
trigger: <auto | manual>
skill: <installed path of code-review/SKILL.md per client>
standards-reviewer: <agent, model and reasoning effort for the Standards axis>
spec-reviewer: <agent, model and reasoning effort for the Spec axis>
followup: <report | fix-and-rereview>
rounds: <number, default 3>

<Agreed review procedure, including another skill if selected.>
Standards, comparison base, endpoint, scope, checkpoint and evidence rules: read `<agent-docs>/project/review.md` before review.
<For fix-and-rereview: correction authority and stop conditions.>

### retro
Runs: <runs>. Phase: <phase>.
<Session evidence and retrospective scope.>
<Where proposed improvements and approved outcomes belong.>
<Who records approved outcomes and may change project instructions.>

## Git and delivery
<Commit convention and permitted checkpoints.>
<Separate commit, push, PR/MR, merge and deployment permissions.>
Procedures and templates: read `<agent-docs>/project/delivery.md` when you commit, push or open a PR.

## Project memory
The Workflow rules section sets when to read and update memory.
<Memory writer, update checkpoints, approval and retention.>
`CONTEXT.md` and `LESSONS.md` never override requirements, accepted decisions or mandatory project rules.
```
