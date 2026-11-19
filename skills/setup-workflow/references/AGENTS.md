# Structure of the generated AGENTS.md

Read this file before you draft a project's `AGENTS.md`. The outline below is a template. It is not active policy and grants no permissions.

## Drafting rules

1. Fill the fields from the setup conversation. Omit the sections of unselected skills and every field without an agreed answer.
2. Keep existing headings and the user's additions.
3. Keep shared sources and permissions in the shared sections.
4. Write a section for every selected skill, also when it has no other setting. Start it with the `Runs:` line: who starts the skill and in which phase. Then give the project settings of that skill.
5. For a selected skill that the outline does not list, add a section with its exact name.
6. Write each automation setting together with its meaning, so that a reader of `AGENTS.md` does not need this file.
7. Give each pointer to a practice or policy a trigger: when the agent reads it.
8. For writing-style pointers, use [writing routes](writing.md). For memory, use [project artifacts](project-artifacts.md).
9. For diagrams, use [diagram configuration](diagrams.md). Add the `excalidraw-diagram` section only when the user selected it. Add diagram pointers only to the sections of selected skills that use diagrams.
10. For a multi-repository home, keep its navigation owner and add the `Related repositories` section. Omit that section for one repository.
11. For an extra coding practice, link its source in the relevant skill section. Do not copy the guide.
12. For an addition without an agreed answer, record the blocked action and its owner. Write no placeholder instruction.

## Automation settings

The agent reads these settings as instructions. They are not runtime flags. Setup asks every setting for each selected skill and records an answer for each one under the owning skill.

| Section | Setting | Values and meaning |
| --- | --- | --- |
| `tdd`, `code-review` | `trigger` | `auto`: `implement` starts the activity at its stage. `manual`: the user starts it. |
| `tdd`, `code-review` | `execution` | `current-session`: run in this session. `subagent`: run in a subagent of the client. `separate-session`: run in a separate session, or prepare an agreed handoff that the user starts. |
| `tdd` | `execution: subagent` | A subagent writes each failing test from the requirements and the interface only. It does not get the implementation plan. The current session writes the code that makes the test pass. |
| `code-review` | `reviewer` | The agent, model and reasoning effort that review. For example, a Claude subagent on a named model, or Codex in a separate Orca session. |
| `code-review` | `followup` | `report`: return the findings and wait. `fix-and-rereview`: fix the authorized findings and review again. |
| `code-review` | `rounds` | The maximum number of fix-and-review rounds, `3` by default. After the last round, the agent stops and asks the user. |
| Workflow rules | `search` | `current-session`: search in this session. `subagent`: send bulk lookups to the named search agent and model. Setup records it in the core block, not in a skill section. |

- TDD alternates one test and one implementation step. It is not a test-writing phase before implementation.
- The user can always start `tdd` or `code-review` manually, whatever the trigger.
- An execution setting does not grant delegation permission. The skill's own nested steps still apply.
- Before you call a route usable, check the real capabilities and dependencies. Report each mandatory step that cannot run.
- The user accepts the work.
- Write the review procedure and the choice of review skill as prose. There is no `review.skill` or `review.required` flag.

## Review coverage

Ask each question that is not answered yet, as a separate question:

1. When does review run: before the commit, after it, or at both points?
2. At each point, what does it compare: commits, or a base and the working tree?
3. How is the base selected: the target branch, a named revision, or a project rule?
4. Which changes are in scope? For working-tree review, say which of staged, unstaged and untracked changes are included.
5. Does the reviewer report and wait, or can the agent fix authorized findings and request another review?

If the user selects fixes and another review, agree what the agent can fix, the round limit (`3` by default) and the stop conditions. Stop conditions include a disputed requirement and a check that cannot run.
Report-only review gives no permission to fix. If these options do not fit, use the project's own procedure.

By default, `implement` asks for a working-tree snapshot of the task files for its pre-commit review. `code-review` captures the intended staged, unstaged and non-ignored untracked changes. Branch and PR review compare commits, unless the agreed procedure selects another endpoint.

If the project selects another reviewer or other coverage, check that its procedure can review the intended files at that point. If it cannot, report the gap and keep the route blocked. Setup does not make a commit only so that review can run.

## Outline

Replace each angle-bracket field with the agreed rule.

```markdown
# <Project name>

## Project
<Product purpose, working scope and authoritative documentation pointers.>

## Project instructions
`## Workflow rules` is mandatory for every session and every skill.
Each selected skill has a section under `## Skills`. Before you run a skill, read its section.
The section wins over the skill's own defaults. Keep the rest of the skill's procedure unchanged.
If a required step cannot satisfy applicable constraints, report the conflict.

## Workflow rules
<Copy the block from [core rules](core-rules.md) with its markers and fill its fields.>

## Sources and artifacts
<Authoritative requirements, tracker, specification, ticket, implementation-plan and research locations.>
<Decision maps, glossary and ADR sources where used.>
<Artifact owners, formats, visibility and existing operation procedures.>

## Related repositories
<Home or repository-index pointer, with each repository's purpose and agreed portable location.>
<Before child work, read its applicable instructions; explicit shared-rule and skill loading for child-start sessions and workers.>
<Ownership and access rules for cross-repository task artifacts; cloning and worktree permissions remain separate.>

## Working agreement
<Task start rules, autonomy and human checkpoints.>
<Mandatory project and company restrictions, their scope and when to check them. Link authoritative rules without copying private policy.>
<Read-only exploration and implementation delegation permissions.>
<Concurrent-work ownership, environment boundaries and external-write permissions.>
<Shared tools and MCP integrations: purpose, reading or usage trigger, approved targets and data, allowed actions and any prerequisite. Put skill-specific tools under the owning skill.>
The user decides whether to accept the work.
<Pass applicable project rules and readable practice/skill pointers to delegated workers.>

## Writing
<Conversation language and human-text startup pointer, if selected.>
<Artifact language and asd-ste100 pointer, if selected.>
<writing-for-agents pointer for rules, if selected.>

## Skills

Every section below starts with this line:

`Runs: <manual: the user calls the skill | auto: <caller> calls it at <stage>>. Phase: <phase from Workflow rules>.`

### home-repo-init
<Approved inventory roots, home membership and shared-material ownership when this skill is selected.>
<Migration boundaries and required approval; existing child code, instructions and installed skills retain their owners.>

### grilling
<Project discussion context and decision boundaries, if needed.>
For relationships or alternatives worth visualizing, use [excalidraw-diagram](#excalidraw-diagram).

### grill-with-docs
<Documents to consult and their authority.>
<Where to propose or record agreed terms and decisions; who approves changes.>
For relationships or alternatives worth visualizing, use [excalidraw-diagram](#excalidraw-diagram).

### domain-modeling
<Authoritative glossary and ADR locations, formats and domain contexts.>
<Approval and write rules for resolved terms and consequential decisions.>
For domain relationships or decision alternatives worth visualizing, use [excalidraw-diagram](#excalidraw-diagram).

### research
<Permitted sources, evidence expectations and report destination.>
<Delegation preferences within the working agreement.>

### wayfinder
<Map, child-ticket and dependency representation.>
<Claim and resolution procedures; experiment, branch and publication constraints.>
For relationships or alternatives worth visualizing, use [excalidraw-diagram](#excalidraw-diagram).

### prototype
<Permitted experiment surfaces, data and environment boundaries.>
<Artifact location, viewing method and capture/integration permissions.>
For a supporting sketch, use [excalidraw-diagram](#excalidraw-diagram); it does not replace the runnable prototype.

### to-plan
<Task-linked plan location, naming, visibility, approval and revision rules.>
<Receiving executor and the instructions that let it consume the plan plus its source task.>
For interactions or architecture worth visualizing, use [excalidraw-diagram](#excalidraw-diagram).

### to-spec
<Requirement sources, specification format, destination and publication procedure.>
For interactions or architecture worth visualizing, use [excalidraw-diagram](#excalidraw-diagram).

### to-tickets
<Ticket format, granularity, dependency representation and destination.>
<Approval, readiness vocabulary and publication procedure.>

### codebase-design
<Existing interface conventions, architecture constraints and relevant ADRs.>
<Testability examples and permissions for exploring alternative designs.>
For interface boundaries worth visualizing, use [excalidraw-diagram](#excalidraw-diagram).

### excalidraw-diagram
<Readable installed package entrypoint; designated delegation tool, including Orca if selected.>
<Permitted task-artifact destination, naming, visibility and revision rules; approved libraries and rendering permissions.>
Diagrams are optional. Offer one when it would clarify a design question; a declined offer leaves the discussion unchanged.
Package selection is not consent to draw. An explicit request for the diagram counts as consent.
After consent, use the linked package's procedure to assign generation and visual checking to a separate subagent.
Only that worker reads generation references and library JSON. Keep the coordinator's brief and the returned paths, check result and caveats compact.
Check worker access, output paths and rendering permissions before dispatch. Report missing prerequisites as diagram-only blockers; continue in text without inline drawing.
Save editable `.excalidraw` and PNG files with the parent artifact under the configured paths.
Decisions and contracts remain authoritative in text. A diagram neither replaces a runnable prototype nor approves the design.

### tdd
trigger: <auto | manual>
execution: <current-session | subagent | separate-session>

<Test types and boundaries, representative tests and when to read the testing guide.>
<Command sources, infrastructure, fixture and mocking constraints.>

### implement
<Expected task inputs and implementation boundaries.>
<If plan-based execution is selected: read the approved plan and source task as implementation input. Recheck relevant code before editing.>
Use the TDD and review settings in this document.
<Nesting: when implement runs as a worker subagent, whether it can launch its TDD and review subagents in this harness, and the option the user chose if it cannot.>
<Checkpoints before returning the result to the user.>

### implement-with-swarm
<Task sources and architectural constraints, including shared contracts across repositories.>
<Allowed session tool and subagent mode, approval for dispatch, and branch, worktree or workspace isolation rules.>
<Integration owner, target branches and delivery procedure per repository.>
Start each worker with `/implement` (`$implement` in Codex) and its assignment. A worker subagent that cannot run a slash command reads `<path to implement/SKILL.md>` and follows it.
<Worker mode: separate sessions or subagents.>
<Nesting: harness, how deep subagents can launch subagents, and whether workers can launch their TDD and review subagents. If they cannot, the option the user chose.>
<Worker TDD and review rules, combined verification, and acceptance checkpoints.>

### code-review
trigger: <auto | manual>
execution: <current-session | subagent | separate-session>
reviewer: <agent, model and reasoning effort>
followup: <report | fix-and-rereview>
rounds: <number, default 3>

<Agreed review procedure, including another skill if selected.>
<Before review, read these standards, practices, examples and requirement sources.>
<Comparison-base rule, endpoint, included/excluded changes, checkpoint relative to commits and evidence requirements.>
<For fix-and-rereview: correction authority and stop conditions.>

### retro
<Session evidence and retrospective scope.>
<Where proposed improvements and approved outcomes belong.>
<Who records approved outcomes and may change project instructions.>

## Git and delivery
<Commit convention and permitted checkpoints.>
<Separate commit, push, PR/MR, merge and deployment permissions.>
<Reading pointers to existing delivery procedures and templates.>

## Project memory
The Workflow rules section sets when to read and update memory.
<Memory writer, update checkpoints, approval, retention and concurrent-writer coordination.>
<CONTEXT.md records recent events, outcomes, open questions and source pointers.>
<LESSONS.md records confirmed experience and preferences with source and scope.>
Neither file overrides requirements, accepted decisions or mandatory project rules.
```
