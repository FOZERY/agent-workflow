---
name: to-tickets
description: Decompose agreed requirements into verifiable tickets with explicit dependencies, using the project's task format, readiness criteria and publication permissions.
disable-model-invocation: true
---

# To Tickets

Break a plan, spec, or conversation into a set of **tickets**: tracer-bullet vertical slices, each declaring the tickets that **block** it.

Read root `AGENTS.md` and its requirement, tracker and artifact pointers. Establish the authoritative input, existing related work, ticket format, dependency mechanism, readiness/start rules and write permissions. Reuse existing tickets; propose amendments or missing work rather than creating a competing task graph. If the project settles none of these, use the [defaults](#defaults).

## Defaults

Use these when the project instructions settle nothing for tickets, and mention once that `setup-agents-workflow` can configure the project. Confirm with the user before the first file write.

- **Input:** the current conversation, or the spec the user references.
- **Location:** `.docs/tasks/<feature-slug>/`, one file per ticket named `<NN>-<slug>.md` and numbered in dependency order, so blockers come first. Use the local ticket template below with `Status: open`.
- **Dependency-ready:** every ticket in **Blocked by** has `Status: done`.
- **Approval:** iterate on the breakdown with the user until they approve it, then write the files.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Identify any necessary preparatory work as a proposal, with its reason and acceptance criteria. Decomposition does not authorize prefactoring the code.

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets.

<vertical-slice-rules>

- Each feature slice cuts a narrow but COMPLETE path through the layers actually needed for that behavior; do not invent UI, schema or other work irrelevant to the task
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Put genuinely prerequisite work before its dependents; do not add prefactoring solely as a preferred style

</vertical-slice-rules>

Give each ticket its **blocking edges**: work whose accepted outcome is required before this ticket is eligible. No blockers means dependency-ready, not permission to start. Use the project's acceptance and ownership rules, not merely an open/closed label.

**Wide refactors may need another shape.** Use the project's migration/compatibility strategy rather than forcing vertical slices. Where compatibility requires expand-contract, represent expansion, bounded migrations and final contraction explicitly; otherwise prefer the agreed clean cutover. An integration branch, parallel execution or shared working copy requires its own project procedure, not an assumption made by decomposition.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct: does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Confirm the breakdown at the project's required checkpoint. Reuse explicit approval of the same scope; mark unresolved acceptance or dependency decisions instead of inventing them.

### 5. Deliver the approved breakdown

Use the project's required representation and authorized writer. For local artifacts, follow the agreed location, grouping, identifiers and format; propose `.docs/` only when a new local location is needed. For a writable tracker, create only approved missing records and relationships, resolving real identifiers before wiring their references. With read-only access, present the proposed tickets and updates for the owner without silently making a local shadow tracker.

Apply labels, assignment and readiness only through project rules. Explain any missing approval or evidence. Present the **frontier** of dependency-ready tickets and its blockers; do not dispatch implementation from this skill. Do not close or otherwise modify the parent requirement as a side effect of decomposition.

The following templates are examples where the project has no prescribed form; adapt status names and required fields to its contract.

<local-ticket-template>

# <NN>: <Ticket title>

**What to build:** the end-to-end behaviour this ticket makes work, from the user's perspective, not a layer-by-layer implementation list.

**Blocked by:** prerequisite references, or "None (dependency-ready; project start rules still apply)".

**Status:** the project-defined initial state, with pending approvals stated separately.

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

<issue-template>

## Parent

A reference to the parent issue on the tracker (if the source was an existing issue, otherwise omit this section).

## What to build

The end-to-end behaviour this ticket makes work, from the user's perspective, not layer-by-layer implementation.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each prerequisite, or "None (dependency-ready; project start rules still apply)". Omit duplicated text only when the native edges are visible to the intended reader.

</issue-template>

Prefer stable behavior and source pointers over copied implementation detail. Include exact paths/contracts where needed to identify scope. A decision-rich prototype snippet may be included with its source and limitations; do not copy a whole demo into the ticket.

**Done when:** the accepted work and existing tickets are accounted for, dependencies and acceptance criteria are explicit, and each output is saved through the authorized procedure or clearly returned as an unpublished proposal. Readiness is separate from permission to execute.
