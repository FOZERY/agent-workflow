# Project triage interview

Read this when triage is part of the workflow being configured or revised. Establish the project's decision procedure, not just its labels. This is a setup reference: discuss and document the procedure; do not triage live incidents or mutate the tracker during configuration.

## Explore before asking

Read existing runbooks, tracker conventions, ownership maps and relevant release/incident documentation within the authorized scope. Show what is already established. Ask only about missing facts, permissions or decisions; preserve an authoritative procedure rather than copying it into a parallel document.

## Interview topics

Discuss these as a conversation, adapting the questions to the project.

### Sources and evidence

Ask: "Where is the incident recorded? Which sources explain related work, deployed versions, releases and the current system state? Which environment, time range and version does the report concern? What may I access?"

Identify authoritative records, access methods and limits. A ticket's status, code on the main branch and a deployed fix are different facts. Define what to do when a source is unavailable, stale or contradictory.

### Routing and ownership

Ask: "How do we identify the affected subsystem and responsible team? In this monorepo, which package, service or ownership map should guide routing? What happens when several teams or repositories are involved, or ownership is unclear?"

Record the routing method and escalation owner. Repository location is a clue, not proof of root cause or responsibility. Do not require a monorepo map for a project that does not need one.

### Current relevance and resolution

Ask: "What evidence lets us call this incident active, mitigated or resolved? Who confirms the outcome? If it cannot be reproduced, what remains to investigate or ask?"

Define criteria against the affected environment/version and available evidence. Failure to reproduce is inconclusive unless the project supplies additional grounds. An existing fix ticket is not proof of resolution; even merged code may not have reached the affected deployment. Distinguish unknown, mitigated and resolved outcomes where the project uses them. Any reproduction or system access must stay within agreed safety and permissions.

### Related and overlapping work

Ask: "How should I search active and linked tasks for the same subsystem and symptoms? What makes a duplicate, and what makes a related but distinct problem? How do I confirm the scope of an in-progress fix?"

Agree the search scope, statuses and matching criteria, including which recent closed work matters. Require the eventual triage procedure to check existing work before recommending a new implementation. When work overlaps, point to it and identify any missing coverage instead of silently creating parallel work. A suspected duplicate remains a recommendation until the project's evidence and approval requirements are met.

### Outcomes, permissions and uncertainty

Ask: "Should I only present findings, or may I link tasks, comment, route, label, transition or close them? Which decisions require a responsible person? What evidence is sufficient, and when should I stop and ask?"

Separate recommendation from execution for every mutation. Record who accepts closure, conflict resolution and uncertain routing. Agree an output containing the relevant records, affected scope, evidence and its limits, related work, recommended disposition and the decision or information still needed from a human.

### Vocabulary and request surfaces

After establishing the procedure, map the original roles `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human` and `wontfix` to existing project states or labels where meaningful. Reuse category names such as bug, enhancement or incident when applicable. Do not force every incident into the upstream GitHub state machine.

If incoming PRs/MRs are triage inputs, agree which ones and how their review differs from issue triage. This is distinct from creating a delivery PR for the agent's own changes. A vocabulary mapping grants neither classification authority nor permission to create labels.

## Capture the result

Reference the established runbook. If none exists, draft the agreed procedure in a suitable existing policy section or an approved supporting document; propose `.docs/agents/triage.md` only when a separate document is useful. Its location and Git visibility go through the normal setup approval.

The canonical instruction owner must contain an explicit pointer to read this procedure before triaging incidents or other enabled request types. Keep always-applicable permission limits visible there. The procedure must cover sources, routing, evidence/relevance, overlapping work, outcomes, permissions and escalation; link to the vocabulary mapping instead of duplicating it.

Check selected triage instructions for incompatible behavior, especially unconditional comments, state changes, closure, local rejection files or reproduction requirements. Surface the conflict and the necessary skill adaptation. Recording policy does not mean an unchanged upstream prompt already honors it.

**Done when:** each applicable topic has an agreed rule or authoritative source, the instruction owner has a mandatory reading trigger, and missing evidence or authority has an explicit escalation path rather than an invented disposition.
