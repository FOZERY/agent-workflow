---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing the project's domain/glossary document, or recording or editing an ADR.
user-invocable: false
---

# Domain Modeling

Actively build and sharpen the project's domain model as you design. This is the *active* discipline: challenging terms, inventing edge-case scenarios, and writing the glossary and decisions down the moment they crystallise. (Merely *reading* the project's glossary for vocabulary is not this skill: that's a one-line habit any skill can do. This skill is for when you're changing the model, not just consuming it.)

## Project domain contract

Before modeling or writing, read repository-root `AGENTS.md` and the applicable project instructions, then follow their domain/ADR pointers. Resolve the vocabulary source, ADR location, owners, allowed operations and approval rules from that contract.

Preserve the project's chosen names, locations, formats and context map. Existing `GLOSSARY.md`, `DOMAIN.md`, documentation pages and external sources are valid; reuse them rather than renaming, migrating or creating parallel records. For multiple domain contexts, follow the project map into only the relevant contexts.

Read access does not authorize writing. If the source is read-only or a required approval is missing, present the proposed definition or decision to its owner instead of publishing it or creating a local substitute.

If no layout is configured, use `.docs/GLOSSARY.md` and `.docs/adr/<NNNN>-<slug>.md`, and mention once that `setup-agents-workflow` can configure the project. Ask once per session before the first write; after that, update the records inline as terms resolve. Introduce a context map only when distinct domain vocabularies require it.

Create records lazily: only when a term is resolved or an agreed decision merits an ADR. Vocabulary, specifications, implementation decisions and conversation memory retain their separate project-owned locations.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in the project's glossary, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"

### Update the domain vocabulary inline

When a term is resolved, update the agreed vocabulary source right there, subject to its write and approval rules. Don't batch these up: capture them as they happen. Preserve the project's format; [GLOSSARY-FORMAT.md](references/GLOSSARY-FORMAT.md) provides a default when none is established.

Keep glossary entries focused on vocabulary, not implementation details, specifications or scratch notes. Preserve unrelated existing content; record other outcomes in their configured sources.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Follow the project's decision approval, location and format rules; [ADR-FORMAT.md](references/ADR-FORMAT.md) provides a minimal default.
