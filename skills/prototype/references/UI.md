# UI Prototype

Explore meaningfully different UI alternatives on the project-approved surface. An existing page, isolated route, component playground or mockup can be suitable. Use the patterns below only where they fit the agreed question, permissions and routing; they do not require changing production pages.

If the question is about logic/state rather than what something looks like, this is the wrong branch. Use [LOGIC.md](LOGIC.md).

## When this is the right shape

- "What should this page look like?"
- "I want to see a few options for this dashboard before committing."
- "Try a different layout for the settings screen."
- Any time the user would otherwise spend a day picking between three vague mockups in their head.

## Choose the approved surface

Realistic surrounding layout and data density help judge a design. Use safe fixtures or authorized read-only data. Prefer the project's existing prototype/component-preview mechanism; changing a live application route needs explicit scope and appropriate isolation.

### Sub-shape A: an approved existing-page experiment

Where the project allows it, variants can share a route and use a `?variant=` parameter. Preserve existing behavior outside the explicitly experimental surface; production authentication/data access is not automatically authorized by this pattern.

When an approved experiment belongs inside an existing page, embed it there only within the agreed isolated environment and edit scope. Otherwise choose a preview/story surface with representative context.

### Sub-shape B: an isolated experiment

Use an isolated route, component story or mockup when the project selects that surface. Follow its naming and routing rather than requiring `/prototype/<name>`. Mark it as experimental and show enough surrounding context to evaluate the question.

A floating switcher is optional; native playground controls or separate preview links may serve the same purpose.

## Process

### 1. State the question and pick N

Choose enough alternatives to expose the actual design trade-off, without a fixed required count. State the question, intended comparisons and chosen surface in a short visible description or project-appropriate note. Use variants that differ meaningfully, not merely cosmetically.

### 2. Generate radically different variants

Draft each variant. Hold each one to:

- The page's purpose and the data it has access to.
- The project's component library / styling system (TailwindCSS, shadcn, MUI, plain CSS, whatever).
- A clear exported component name, e.g. `VariantA`, `VariantB`, `VariantC`.

Variants must be **structurally different**: different layout, different information hierarchy, different primary affordance, not just different colours. Three slightly-tweaked card grids isn't a UI prototype, it's wallpaper. If two drafts come out too similar, redo one with explicit "do not use a card grid" guidance.

### 3. Wire them together

For an approved route-based experiment, a switcher can look like this; adapt it or use the preview surface's existing controls:

```tsx
// pseudo-code, adapt to the project's framework
const variant = searchParams.get('variant') ?? 'A';
return (
  <>
    {variant === 'A' && <VariantA {...data} />}
    {variant === 'B' && <VariantB {...data} />}
    {variant === 'C' && <VariantC {...data} />}
    <PrototypeSwitcher variants={['A','B','C']} current={variant} />
  </>
);
```

Preserve the approved data-access boundary whichever surface is used. A new experiment uses the project's location, not an assumed route.

### 4. Make comparison usable

If a floating switcher suits the selected surface, it can provide:

- **Left arrow**: cycles to the previous variant (wraps around).
- **Variant label**: shows the current variant key and, if the variant exports a name, that name too. e.g. `B (Sidebar layout)`.
- **Right arrow**: cycles forward (wraps around).

Behaviour:

- Clicking an arrow updates the URL search param (use the framework's router, e.g. `router.replace` on Next, `navigate` on React Router, etc) so the variant is shareable and reload-stable.
- Keyboard: `←` and `→` arrow keys also cycle. Don't intercept arrow keys when an `<input>`, `<textarea>`, or `[contenteditable]` is focused.
- Visually distinct from the page (e.g. high-contrast pill, subtle shadow) so it's obviously not part of the design being evaluated.
- Isolate the experiment from production exposure using the project's actual mechanism. A UI build flag alone is not permission to merge experimental code.

Keep any comparison-only component scoped to the experiment unless a shared location was explicitly agreed.

### 5. Hand it over

Provide the verified preview URL, story, file or viewing method. Invite comparison of the actual alternatives; opening a browser or changing its state follows the applicable environment permissions.

### 6. Capture the answer and clean up

Record the selected direction, reasons and remaining uncertainty, then retain or retire the experiment under the [prototype procedure](../SKILL.md). Preserve useful source pointers without prescribing a throwaway branch.

Moving the design into production, promoting routes, deleting variants or changing shared components are separate implementation/lifecycle actions with their own authorization. Selection of a variant alone does not authorize them.

## Anti-patterns

- **Variants that differ only in colour or copy.** That's a tweak, not a prototype. Real variants disagree about structure.
- **Sharing too much code between variants.** A shared `<Header>` is fine; a shared `<Layout>` defeats the point. Each variant should be free to throw out the layout.
- **Wiring variants to real mutations.** Read-only prototypes are fine. If a variant needs to mutate, point it at a stub: the question is "what should this look like", not "does the backend work".
- **Treating an experimental result as production-ready.** Review its shortcuts and run project-required verification in the separately authorized implementation; preserve relevant evidence rather than assuming a prototype needs no tests.
