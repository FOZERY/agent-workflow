# Project domain documents

Use the glossary, context map and ADR locations that the project's instructions declare.
Existing `GLOSSARY.md`, `DOMAIN.md`, documentation-site pages and external knowledge bases are valid sources. Keep them where they are, whatever their name or location.

## Reading

1. Before domain design, exploration, implementation, tests or review, read the glossary terms and ADRs for the area that changes.
2. Follow a context map only into the relevant contexts.
3. Use the project's terms. Avoid the synonyms that its glossary rejects.
4. If optional domain records do not exist yet, continue. Create no empty files.
5. If a required source is not accessible or conflicts with the task, report the gap and ask its owner. Invent no definitions, and override no decision.

## Layout

1. Keep the accepted layout.
2. If there is no layout and the project needs domain documents, agree one glossary and one ADR location.
3. Several packages in the code do not need several domain contexts. Add a context map only when the vocabularies really differ.
4. External sources need declared access rights, the same as local files.

## Writing

1. Record agreed terms and important decisions when the project permits it. Otherwise, propose the record to its owner. Read access does not permit edits.
2. Keep each record type to its role:
   - A spec records behavior and acceptance.
   - An ADR records an important decision, its alternatives and trade-offs.
   - The glossary defines the terms that both use. It holds no implementation plans.
   - Conversation context stays in `CONTEXT.md`.
3. Offer an ADR when a decision is costly to reverse, surprising without context, and based on a real trade-off.
4. Record resolved terms and accepted decisions when they appear. Write no empty scaffolds and no record for each small implementation choice.
5. Use the project's approved diagram tools and storage. Link an editable diagram or an agreed export from its spec or ADR. The diagram does not replace the decision text and its reasons. External publication needs authorization.
6. Keep established sources until their owner accepts a migration and updates the documents that use them.
7. If a task conflicts with an ADR, say so explicitly. A proposal to reconsider the ADR does not supersede it.
