# HTML Report Format

Read this only when the project selects an HTML architecture report. Use its agreed language, destination and diagram conventions; opening a browser is a separate permission. Prefer an offline document with inline CSS and static diagrams. Add scripts or external assets only when the project authorizes those dependencies; a CDN-backed file is not self-contained.

## Scaffold

```html
<!doctype html>
<html lang="{{report language}}">
  <head>
    <meta charset="utf-8" />
    <title>Architecture review for {{repo name}}</title>
    <style>
      body { font: 1rem/1.5 system-ui, sans-serif; margin: 0; padding: 2rem; }
      main { max-width: 65rem; margin: auto; }
      article { border: 1px solid currentColor; padding: 1rem; margin-block: 1rem; }
      .diagram { overflow: auto; }
      .seam { stroke-dasharray: 4 4; }
    </style>
  </head>
  <body>
    <main>
      <header>...</header>
      <section id="candidates">...</section>
      <section id="top-recommendation">...</section>
    </main>
  </body>
</html>
```

## Header

Repository, investigation date, scope and the legend actually used in the diagrams. Distinguish current observations from proposed states and link relevant source evidence.

## Candidate card

Use diagrams where they communicate the architectural relationship, with enough prose to preserve constraints, evidence and uncertainty. Use the project's terminology and report language.

Each candidate is one `<article>`:

- **Title**: the affected responsibility and proposed direction.
- **Confidence**: supported, worth investigating or speculative, with the basis for that assessment.
- **Sources**: relevant files/modules and evidence links.
- **Before / After**: observed structure and explicitly proposed structure where a diagram helps.
- **Problem and proposal**: the actual friction and possible change.
- **Trade-offs**: expected benefits, migration/test costs, limitations and risks.
- **Decision conflict**: any accepted decision that would need reconsideration.

Keep enough explanation to support the recommendation; shorter labels must not replace necessary reasoning or imply measured benefits.

## Diagram patterns

Choose the pattern that explains the relationship. Reuse it for comparable candidates; diagram variety is not a goal.

### Mermaid graph (the workhorse for dependencies / call flow)

Use Mermaid for call/dependency graphs only when the report has an approved working renderer. Otherwise render an equivalent static diagram with an available tool. The following markup illustrates the graph input; it does not load or authorize a renderer:

```html
<div class="diagram">
  <pre class="mermaid">
    flowchart LR
      A[OrderHandler] --> B[OrderValidator]
      B --> C[OrderRepo]
      C -.leak.-> D[PricingClient]
      classDef leak stroke:#dc2626,stroke-width:2px;
      class C,D leak
  </pre>
</div>
```

### Hand-built boxes-and-arrows (when Mermaid's layout fights you)

Modules as `<div>`s with borders and labels. Arrows as inline SVG `<line>` or `<path>` elements positioned absolutely over a relative container. Reach for this when you want the "after" diagram to feel like one thick-bordered deep module with greyed-out internals, since Mermaid won't render that with the right weight.

### Cross-section (good for layered shallowness)

Stack horizontal bands (`h-12 border-l-4`) to show layers a call passes through. Before: 6 thin layers each doing nothing. After: 1 thick band labelled with the consolidated responsibility.

### Mass diagram (good for "interface as wide as implementation")

Two rectangles per module: one for interface surface area, one for implementation. Before: interface rectangle is nearly as tall as the implementation rectangle (shallow). After: interface rectangle is short, implementation rectangle is tall (deep).

### Call-graph collapse

Before: a tree of function calls rendered as nested boxes. After: the same tree collapsed into one box, with the now-internal calls shown faded inside it.

## Style guidance

- Use readable type, whitespace and a hierarchy suited to the report's audience.
- Use color sparingly and explain its meaning without relying on color alone.
- Size diagrams for their actual labels and relationships; keep before/after comparisons legible.
- Use ordinary inline CSS or the project's approved styling mechanism, not an assumed utility framework.
- Keep report scripts and external resources within the approved dependency policy; prefer a static offline result when no renderer is configured.

## Top recommendation section

When a candidate is supported, give its name, the reason to prefer it and a link to its card. When none is supported, state that result and any evidence gaps rather than inventing a recommendation.

## Tone

Use the project's language and established domain/architecture terms. The `codebase-design` vocabulary is available where it clarifies the proposal, not a replacement for every service, API or domain boundary.

Prefer specific, evidenced statements about behavior, ownership, complexity and testability. Distinguish observed facts, estimated benefits and unresolved questions. Preserve caveats and trade-offs instead of removing them for brevity or visual uniformity.
