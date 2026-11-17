# Reference structure for generated AGENTS.md

Read before drafting a project contract. This outline is not active policy or a set of default permissions.
Fill applicable fields from the conversation. Omit unselected skill sections and unresolved template fields.
Preserve existing headings and user additions; add a named section for another selected skill when needed.
Keep common sources and permissions in shared sections. Skill sections hold only project-specific settings and differences.

## Automation settings

These are instructions interpreted by the agent, not runtime configuration flags. Record agreed values under the owning skill:

| Section | Setting | Values and meaning |
| --- | --- | --- |
| `tdd`, `code-review` | `trigger` | `auto`: implementation starts this activity at its applicable stage. `manual`: implementation leaves it to a separate user invocation. |
| `tdd`, `code-review` | `execution` | `current-session`: run here. `subagent`: delegate through the client. `separate-session`: use a separate thread/session or prepare an agreed user-started handoff. |
| `code-review` | `followup` | `report`: return findings and wait. `fix-and-rereview`: correct authorized findings and repeat review within the agreed cycle limit. |

Omitted settings retain the selected skill's defaults; omission does not mean `manual`.
TDD is a test–implementation cycle, not a complete test-writing phase before implementation.
Manual invocation remains available regardless of the automatic trigger.
Execution settings do not grant delegation permission or erase nested requirements of the selected skill.
Check actual capabilities and dependencies before calling a route usable. Report incompatible mandatory steps.
For `fix-and-rereview`, agree correction scope, a cycle limit and stop conditions for disputed requirements or unavailable checks.
The user accepts the work. Review procedure or skill choice is ordinary prose; there is no `review.skill` or `review.required` flag.

## Review coverage

Agree how to select the comparison base, the endpoint (committed revision or working tree), included/excluded changes and the checkpoint relative to commits.
Check that the selected procedure covers that scope at the checkpoint. The bundled `code-review` compares `<base>...HEAD`, which excludes uncommitted work; `implement` calls it before committing.
For pre-commit review, agree an explicit project procedure that covers the intended staged, unstaged and untracked changes, or select a compatible reviewer.
Otherwise, leave the route blocked. Setup does not authorize a commit merely to make review runnable.

## Outline

Replace angle-bracket fields with agreed rules. Include only selected settings and add reading triggers to practice links.
Render each chosen automation setting with its operational meaning in the generated contract; readers must not need this setup reference to interpret it.
Use [writing routes](writing.md) for the approved style pointers and [project artifacts](project-artifacts.md) for memory details.

```markdown
# <Project name>

## Project
<Product purpose, working scope and authoritative documentation pointers.>

## Project instructions
The Skills sections define project-specific settings for the named skills.
Use the skill's defaults for settings not specified here.
Keep its remaining procedure unchanged.
If a required step cannot satisfy applicable constraints, report the conflict.

## Sources and artifacts
<Authoritative requirements, tracker, specification, ticket and research locations.>
<Decision maps, glossary and ADR sources where used.>
<Artifact owners, formats, visibility and existing operation procedures.>

## Working agreement
<Task start rules, autonomy and human checkpoints.>
<Read-only exploration and implementation delegation permissions.>
<Concurrent-work ownership, environment boundaries and external-write permissions.>
The user decides whether to accept the work.
<Pass applicable project rules and readable practice/skill pointers to delegated workers.>

## Writing
<Conversation language and human-text startup pointer, if selected.>
<Artifact language and asd-ste100 pointer, if selected.>
<writing-for-agents pointer for rules, if selected.>

## Skills

### grilling
<Project discussion context and decision boundaries, if needed.>

### grill-with-docs
<Documents to consult and their authority.>
<Where to propose or record agreed terms and decisions; who approves changes.>

### domain-modeling
<Authoritative glossary and ADR locations, formats and domain contexts.>
<Approval and write rules for resolved terms and consequential decisions.>

### research
<Permitted sources, evidence expectations and report destination.>
<Delegation preferences within the working agreement.>

### wayfinder
<Map, child-ticket and dependency representation.>
<Claim and resolution procedures; experiment, branch and publication constraints.>

### prototype
<Permitted experiment surfaces, data and environment boundaries.>
<Artifact location, viewing method and capture/integration permissions.>

### to-spec
<Requirement sources, specification format, destination and publication procedure.>

### to-tickets
<Ticket format, granularity, dependency representation and destination.>
<Approval, readiness vocabulary and publication procedure.>

### codebase-design
<Existing interface conventions, architecture constraints and relevant ADRs.>
<Testability examples and permissions for exploring alternative designs.>

### tdd
trigger: <auto | manual>
execution: <current-session | subagent | separate-session>

<Test types and boundaries, representative tests and when to read the testing guide.>
<Command sources, infrastructure, fixture and mocking constraints.>

### implement
<Expected task inputs and implementation boundaries.>
Use the TDD and review settings in this document.
<Checkpoints before returning the result to the user.>

### implement-spec
<Authoritative specification and ticket graph.>
<Branch, worktree, delegation and integration arrangements.>
Use the TDD and review settings in this document.
<Checkpoints before returning the integrated result to the user.>

### code-review
trigger: <auto | manual>
execution: <current-session | subagent | separate-session>
followup: <report | fix-and-rereview>

<Agreed review procedure, including another skill if selected.>
<Before review, read these standards, practices, examples and requirement sources.>
<Comparison-base rule, endpoint, included/excluded changes, checkpoint relative to commits and evidence requirements.>
<For fix-and-rereview: correction authority, cycle limit and stop conditions.>

### retro
<Session evidence and retrospective scope.>
<Where proposed improvements and approved outcomes belong.>
<Who records approved outcomes and may change project instructions.>

## Git and delivery
<Commit convention and permitted checkpoints.>
<Separate commit, push, PR/MR, merge and deployment permissions.>
<Reading pointers to existing delivery procedures and templates.>

## Project memory
At session start or resumption, read <agent-docs>/CONTEXT.md.
Verify the current task and code against their authoritative sources.
Before a decision that depends on prior experience, read relevant <agent-docs>/LESSONS.md topics.
<Memory writer, update checkpoints, approval, retention and concurrent-writer coordination.>
<CONTEXT.md records recent events, outcomes, open questions and source pointers.>
<LESSONS.md records confirmed experience and preferences with source and scope.>
Neither file overrides requirements, accepted decisions or mandatory project rules.
```

For another selected skill, add its exact name under `Skills`, project sources, settings and reading triggers.
For an additional coding practice, link its authoritative source in the relevant skill section rather than copying the guide.
Unresolved additions identify their blocked action and owner; they do not become placeholder instructions.
