# Reference structure for generated AGENTS.md

Read before drafting a project contract. This outline is not active policy or a set of default permissions.
Fill applicable fields from the conversation. Omit unselected skill sections and unresolved template fields.
Preserve existing headings and user additions; add a named section for another selected skill when needed.
Keep common sources and permissions in shared sections.
Write a section for every selected skill, also when it has no other project setting. Each section starts with a `Runs:` line: who starts the skill and in which phase. Then it gives the project settings that the skill uses.

## Automation settings

These are instructions interpreted by the agent, not runtime configuration flags. Record agreed values under the owning skill:

| Section | Setting | Values and meaning |
| --- | --- | --- |
| `tdd`, `code-review` | `trigger` | `auto`: implementation starts this activity at its applicable stage. `manual`: implementation leaves it to a separate user invocation. |
| `tdd`, `code-review` | `execution` | `current-session`: run here. `subagent`: delegate through the client. `separate-session`: use a separate thread/session or prepare an agreed user-started handoff. |
| `tdd` | `execution: subagent` | A subagent writes each failing test from the requirements and the interface only. It does not get the implementation plan. The current session writes the code that makes the test pass. |
| `code-review` | `reviewer` | The agent, model and reasoning effort that review, for example a Claude subagent on a named model or Codex in a separate Orca session. |
| `code-review` | `followup` | `report`: return findings and wait. `fix-and-rereview`: correct authorized findings and repeat review. |
| `code-review` | `rounds` | The maximum number of fix-and-review rounds. Default: `3`. After the last round, the agent stops and asks the user. |
| Workflow rules | `search` | `current-session`: search here. `subagent`: send bulk lookups to the named search agent and model. Recorded in the core block, not in a skill section. |

Setup asks every setting in this table for each selected skill. Record an answer for each one.
TDD is a test–implementation cycle, not a complete test-writing phase before implementation.
Manual invocation remains available regardless of the automatic trigger.
Execution settings do not grant delegation permission or erase nested requirements of the selected skill.
Check actual capabilities and dependencies before calling a route usable. Report incompatible mandatory steps.
The user accepts the work. Review procedure or skill choice is ordinary prose; there is no `review.skill` or `review.required` flag.

## Review coverage

Ask the applicable unanswered questions separately:

1. When should review run relative to the commit: before, after, or at both checkpoints?
2. At each checkpoint, what does it compare: committed revisions, or a base and the working tree?
3. How is the base selected: the target branch, a named revision, or a project rule?
4. Which changes are in or out of scope? For working-tree review, specify staged, unstaged and untracked changes.
5. Should the reviewer report findings and wait, or may the agent make authorized corrections and request another review?

If the user chooses fixes and another review, agree correction scope, a round limit (default 3) and stop conditions, including disputed requirements or unavailable checks. Report-only review does not authorize corrections. Use the project's own procedure when these options do not fit.

The bundled `implement` requests a scoped working-tree snapshot for its pre-commit review by default. The bundled `code-review` can capture intended staged, unstaged and nonignored untracked changes. Branch and PR review use a committed comparison unless the agreed procedure selects a different endpoint.
If a project selects another reviewer or requires different coverage, confirm that its procedure can review the intended files at that checkpoint. If not, report the gap and leave the affected route blocked. Setup does not authorize a commit merely to make review runnable.

## Outline

Replace angle-bracket fields with agreed rules. Include only selected settings and add reading triggers to practice links.
Render each chosen automation setting with its operational meaning in the generated contract; readers must not need this setup reference to interpret it.
Use [writing routes](writing.md) for the approved style pointers and [project artifacts](project-artifacts.md) for memory details.
For optional diagrams, use [diagram configuration](diagrams.md). Include the `excalidraw-diagram` section only when selected, and retain diagram pointers only in applicable selected skill sections. Resolve its package pointer, delegation route and output rules from agreed settings; do not add diagram flags.
For a multi-repository home, preserve its navigation owner and include the conditional Related repositories section. Omit it for a single-repository setup.

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

For another selected skill, add its exact name under `Skills`, project sources, settings and reading triggers.
For an additional coding practice, link its authoritative source in the relevant skill section rather than copying the guide.
Unresolved additions identify their blocked action and owner; they do not become placeholder instructions.
