# Project domain documents

Use the glossary, context map and ADR locations declared by the project's canonical instructions. Existing `GLOSSARY.md`, `DOMAIN.md`, documentation-site pages and external knowledge bases are valid sources; a different name or location is not a reason to migrate them.

## Reading rules

Before domain design, exploration, implementation, tests or review, read the vocabulary and ADRs relevant to the area being changed. Follow a context map only into relevant contexts. Use the project's canonical terms instead of synonyms its glossary rejects.

If optional domain records do not exist yet, continue without creating empty files. If a required source is inaccessible or conflicts with the task, report the specific gap and ask the responsible owner; do not invent definitions or silently override a decision.

## Layout

Preserve the accepted layout. If none exists and domain documentation is needed, agree one glossary and an ADR location. Multiple packages alone do not require multiple domain contexts; introduce a map only when distinct vocabularies justify it. External sources need declared access rights just as local files do.

## Writing rules

Record agreed vocabulary and consequential decisions when the project permits the action; otherwise propose the record to its owner. The ability to read a source does not authorize editing it.

Keep definitions free of implementation plans. A spec records behavior and acceptance; an ADR records a consequential decision, alternatives and trade-offs; the glossary defines the language used by both. Conversation context remains a separate artifact.

Offer an ADR when a decision is costly to reverse, surprising without context and based on a real trade-off. Record resolved terms and accepted decisions as they arise, not empty scaffolds or every small implementation choice.

Use the project's approved diagram tools and storage. Link a relevant editable diagram or agreed export from its spec or ADR; the visual does not replace the textual decision and reasons. External publication requires authorization.

Preserve established sources until their owner accepts a migration and updates to their consumers. Surface conflicts with relevant ADRs explicitly; proposing a reconsideration is not permission to supersede the decision.
