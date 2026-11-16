# Domain Glossary Format

Preserve the project's accepted vocabulary source and format. The examples below are defaults for a source with no established format; they do not prescribe filenames or storage locations.

## Structure

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A one or two sentence description of the term}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account
```

## Rules

- **Be opinionated.** When multiple words exist for the same concept, pick the best one and list the others under `_Avoid_`.
- **Keep definitions tight.** One or two sentences max. Define what it IS, not what it does.
- **Only include terms specific to this project's context.** General programming concepts (timeouts, error types, utility patterns) don't belong even if the project uses them extensively. Before adding a term, ask: is this a concept unique to this context, or a general programming concept? Only the former belongs.
- **Group terms under subheadings** when natural clusters emerge. If all terms belong to a single cohesive area, a flat list is fine.

## Single vs multi-context repos

**Single context (most repos):** Use the project's designated vocabulary source.

**Multiple contexts:** Follow the project's existing map of contexts, sources and relationships. Introduce one only when distinct vocabularies justify it. In the example below, substitute the agreed source paths or URLs:

```md
# Glossary Map

## Contexts

- [Ordering](<ordering-glossary-path-or-url>): receives and tracks customer orders
- [Billing](<billing-glossary-path-or-url>): generates invoices and processes payments
- [Fulfillment](<fulfillment-glossary-path-or-url>): manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

Resolve the structure from project instructions and their pointers, not from a required root filename. Read only the relevant mapped context; if its ownership or applicability is unclear, ask. When no layout exists, agree one under the skill's project-domain contract before creating a source.
