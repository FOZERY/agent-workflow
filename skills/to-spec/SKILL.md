---
name: to-spec
description: Synthesize an agreed discussion into a specification using the project's format, authoritative sources and publication permissions.
disable-model-invocation: true
---

Synthesize the current discussion and codebase understanding; do not start a new design interview. Read root `AGENTS.md` and its requirement, domain and artifact pointers for ownership, format, readiness criteria and write permissions. Record unresolved decisions explicitly rather than inventing answers.

If an analyst-owned or read-only specification already exists, preserve it as authoritative. Prepare only the requested summary, proposed amendments or clarification list; do not create a competing specification. If the project names no destination or format, use the [defaults](#defaults).

## Defaults

Use these when the project instructions settle nothing for specifications, and mention once that `setup-agents-workflow` can configure the project. Confirm with the user before the first file write.

- **Location:** `.docs/tasks/<feature-slug>/spec.md`, beside the tickets that `to-tickets` writes.
- **Format:** the template below, with only the relevant sections.
- **Testing approach:** propose the test boundary from existing tests of similar behavior and confirm it with the user.
- **Approval:** show the draft and save it after the user approves it.

## Process

1. Establish the current behavior and relevant project terminology from available sources. Respect accepted decisions and link the authoritative task/specification.

2. Record the agreed acceptance criteria and testing approach, preferring existing behavioral interfaces. Keep unresolved test/design choices explicit. Obtain any confirmation required by the project rather than forcing a new seam-design exercise or a fixed number of seams.

3. Write the specification in the project's required format. The template below is a starting point where no format is prescribed; include only relevant sections. Save or publish through the authorized writer and location. With read-only access, return the proposed content and owner action. Apply readiness/status changes only after project criteria and approvals are satisfied; a ready spec does not authorize implementation.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A numbered list of relevant user stories where that form fits the project. For example:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

Cover the agreed behavior and significant edge cases. Preserve open questions and scope exclusions; length is not a completeness criterion.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Prefer stable concepts and source pointers over copied implementation detail. Include exact paths or contracts where needed to identify a requirement or source, making their role clear.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- The agreed behavioral test boundary and any focused internal invariants that also require protection
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Acceptance Criteria

Observable outcomes, failure cases and boundaries that establish whether the agreed behavior is delivered.

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>

**Done when:** the agreed requirements, acceptance criteria and unresolved questions are accounted for, and the result is saved in its authorized location or clearly presented as an unpublished proposal with its delivery blocker.
