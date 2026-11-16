---
name: wayfinder
description: Explore a large uncertain effort through a shared map of decisions, resolving its frontier until the route is clear. Use the project's approved artifact and task procedures.
disable-model-invocation: true
---

A loose idea has arrived, too big for one agent session, and wrapped in fog: the way from here to the **destination** isn't visible yet. Wayfinding finds that way rather than charging at the destination. Chart a **shared map** and work its **decision tickets** (questions to resolve, not implementation slices) until the route is clear.

The destination varies per effort, and naming it is the first act of charting: it shapes every ticket. It might be a spec to hand off and iterate on, a decision to lock before planning starts, or a change made in place like a data-structure migration. The map is domain-agnostic: engineering work, course content, whatever fits the shape.

## Plan, don't do

Wayfinder is **planning**: each ticket resolves a decision, and the map is done when the way is clear. The pull to implement usually means it is time to hand off. Any operational work needed to answer a question follows separate project authorization; the map's Notes do not grant permission to implement or publish.

## Refer by name

Every map and ticket has a **name**: its title. A ticket can be a tracker record or a section/file in the agreed project artifact. Refer to names with links in human-facing discussion, not bare ids. Preserve identifiers where the project needs them.

## The Map

The map is the canonical index in the project's agreed location. Its decision tickets use the project's representation: linked tracker records, local documents or sections of the map. Labels and parent/child relationships apply only when configured.

The map is an **index**, not a store. It gives a short gist of each resolved decision and links to its authoritative answer. That answer may live in the decision ticket, an accepted ADR or another project-owned source. When it lives elsewhere, the ticket links to it rather than keeping a second full account.

Read root `AGENTS.md` and its artifact, tracker and wayfinding pointers for locations, formats, dependencies, ownership and allowed operations. Use the current client's mechanism to load skills named below. If the map location or procedure is missing, use the [defaults](#defaults). A read-only tracker supports inspection and proposed changes for its owner, not unauthorized publication or a competing local tracker.

### The map body

The whole map at low resolution, loaded once per session. Where supported, query open tickets rather than duplicating their bodies in the index; otherwise maintain their project-defined references in the map.

```markdown
## Destination

<what reaching the end of this map looks like: the spec, decision, or change this effort is finding its way to. One or two lines; every session orients to it before choosing a ticket.>

## Notes

<domain; skills every session should consult; standing preferences for this effort>

## Decisions so far

<!-- the index: one line per closed ticket, enough to judge relevance, then zoom the link for the detail the ticket holds -->

- [<closed ticket title>](link): <one-line gist of the answer>

## Not yet specified

<!-- see "Fog of war": in-scope fog you can't ticket yet; graduates as the frontier advances -->

## Out of scope

<!-- see "Out of scope": work ruled beyond the destination; closed, never graduates -->
```

### Tickets

Each ticket is one bounded decision or investigation that fits the available session context. Use stable project identifiers and the project's required fields; the following body is a starting point when no format is prescribed.

```markdown
## Question

<the decision or investigation this ticket resolves>
```

Each ticket has a logical type: `research`, `prototype`, `grilling` or `task` (see [Ticket Types](#ticket-types)). Map these to the project's labels or document fields where configured. A decision ticket is not an implementation-ready task merely because it has a type or no blockers.

Use the project's ownership/claim procedure before concurrent work. Assignment is a claim only if the project defines it that way and permits the change. If no safe claim is available, coordinate with the owner rather than pretending to reserve work or writing to a read-only tracker.

Represent blocking through the project's supported dependency mechanism, with native edges when appropriate or explicit artifact references otherwise. A ticket is **unblocked** once its prerequisite decisions satisfy the project's acceptance criteria; the **frontier** is the open, unblocked and unclaimed work available under its ownership rules. Eligibility does not itself authorize starting or changing records.

Record each answer in the project's authoritative decision location and link it from the map. Supporting assets use source pointers rather than pasted copies; resolution need not be a tracker comment.

## Defaults

Use these when the project instructions settle nothing for wayfinding, and mention once that `setup-agents-workflow` can configure the project. Confirm with the user before the first file write.

- **Map:** `.docs/planning/<effort-slug>/map.md`, using the map body above.
- **Tickets:** one file per ticket beside the map, named `<NN>-<slug>.md` in creation order. Each holds `Type:` (`research`, `prototype`, `grilling` or `task`; `grilling` when unsure), `Status:` (`open`, `claimed by <session name>` or `resolved`), `Blocked by:` (ticket file names or `none`), the `## Question` and, once resolved, `## Answer`.
- **Unblocked:** every ticket listed in `Blocked by:` is `resolved`.
- **Frontier:** open, unblocked, unclaimed tickets in number order.
- **Claim:** take the first frontier ticket unless the user names one, then set `Status: claimed by <session name>` and save it before working.
- **Resolve:** write the answer under `## Answer`, set `Status: resolved` and add its one-line gist to the map's **Decisions so far**.

## Ticket Types

Every ticket is either **HITL** (human in the loop, worked _with_ a human who speaks for themselves) or **AFK**, driven by the agent alone. A HITL ticket only resolves through that live exchange; the agent never stands in for the human's side of it (a grilling agent that answers its own questions has broken this).

- **Research** (AFK): Resolve an evidence gap. Use the project's read-only exploration policy for quick facts; use `research` for an in-depth investigation with a reusable report. Delegation, sources and the report writer follow project permissions; a read-only helper returns findings to the authorized writer.
- **Prototype** (HITL): Raise the fidelity of discussion with a bounded experiment by using `prototype`. Link any approved artifact. Use when "how should it look" or "how should it behave" needs a concrete answer.
- **Grilling** (HITL): Conversation, using `grilling` and `domain-modeling` for questions and terminology within their project permissions.
- **Task** (HITL or AFK): Operational work that must happen before a decision can be made. Establish its scope and authorization separately, including changes to services, accounts or data. If a human must do it, provide the precise checklist. Record the observed result and safe source pointers, never credentials themselves.

## Fog of war

The map is _deliberately_ incomplete: don't chart what you can't yet see. Beyond the live tickets lies the **fog of war**: the dim view of decisions and investigations you can tell are coming but can't yet pin down, because they hang on questions still open. Resolving a ticket clears the fog ahead of it, graduating whatever's now specifiable into fresh tickets, one at a time, until the way to the destination is clear and no tickets remain.

The map's **Not yet specified** section is where that dim view is written down: the suspected question, the area to revisit later. It's the undiscovered frontier _toward_ the destination: everything here is in scope, just not sharp enough to ticket. Write as loosely or as fully as the view allows; it doubles as a signpost for collaborators reading where the effort is headed.

**Fog or ticket?** The test is whether you can state the question precisely now, _not_ whether you can answer it now.

- **Ticket when** the question is already sharp, even if it's blocked and you can't act on it yet.
- **Not yet specified when** you can't yet phrase it that sharply. Don't pre-slice the fog into ticket-sized pieces: it's coarser than a ticket, and one patch may graduate into several tickets, or none, once the frontier reaches it.

**Not yet specified** excludes what's already decided (Decisions so far), what's already a live ticket, and what's out of scope (the next section).

## Out of scope

Fog only ever gathers _toward_ the destination. The destination fixes the scope, so work beyond it is **out of scope**: it isn't fog, and it doesn't belong in **Not yet specified**. It gets its own **Out of scope** section on the map: work you've consciously ruled out of _this_ effort. Scope, not sharpness, lands it here.

Out-of-scope work never graduates (the frontier stops at the destination), so it returns only if the destination is redrawn, and then as a fresh effort, not a resumption.

When an existing ticket falls outside the destination, record the reason and link it under **Out of scope**, not Decisions so far. Close or transition a tracker record only through the authorized project procedure; otherwise propose that change to its owner and exclude it logically from this map's frontier.

## Invocation

Two modes. Either way, **never resolve more than one ticket per session**, with the exception of research tickets.

### Chart the map

User invokes with a loose idea.

1. **Name the destination.** Use `grilling` and `domain-modeling` to clarify what this map is finding its way to. The destination fixes the effort's scope.
2. **Map the frontier.** Grill breadth-first across the open decisions. If the route is already clear and fits one session, stop and ask how the user wants to proceed instead of manufacturing a map.
3. **Draft the map:** Destination, Notes and the known fog. Use the project's format, reusing an existing authoritative map where applicable.
4. **Draft the tickets you can specify now**, then their blocking edges and cross-references. Use real identifiers only after records exist; local drafts use explicit draft references, not invented issue numbers. Save or publish only through the approved project procedure. If writing is forbidden, present the proposal for the owner.
5. **Investigate the available evidence gaps** through the project's exploration/delegation policy. Use `research` only for questions needing its deeper report. Store any result in its approved location and link it from the map; no throwaway branch or push is required.
6. Stop: charting is one session's work; it hand-resolves nothing.

### Work through the map

User invokes with a map reference. A ticket is optional: use the named ticket, or take the first frontier ticket under project ownership and start rules.

1. Load the **map**: the low-resolution view, not every ticket body.
2. Select the ticket and follow the agreed claim/coordination procedure. Respect another worker's active ownership.
3. Resolve it using its logical type and the relevant skills. Fetch related records on demand. HITL decisions require the human's actual answer; evidence-gathering tasks require observed findings.
4. Record the answer in its authoritative location and link it from Decisions so far. Apply any resolution comment, acceptance or closure only where authorized; in read-only mode, return the proposed update and remaining owner action.
5. Propose newly surfaced tickets and dependency changes, graduating fog into specific questions without duplicating it. Apply only authorized edits; preserve decision history and handle retirement through the project's lifecycle rules rather than silently deleting invalidated tickets.

The user may run unblocked tickets in parallel, so expect other sessions to be editing the tracker concurrently.
