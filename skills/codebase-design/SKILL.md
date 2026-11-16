---
name: codebase-design
description: Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary.
---

# Codebase Design

Use **deep modules** as one lens for evaluating interfaces: useful behavior behind a manageable surface, coherent seams, testability and locality. Read root `AGENTS.md` and its architecture/domain pointers first. Existing project terminology, constraints and accepted decisions govern the design; this vocabulary is a reference, not a required architecture or permission to refactor.

## Glossary

Use the following terms when they clarify the discussion, mapping them to the project's established vocabulary. Keep domain names and intentional architectural roles rather than renaming every service, component or API.

**Module**: a unit with an interface and an implementation, such as a function, class, package or tier-spanning slice.

**Interface**: what a caller must know to use the module correctly: signatures, invariants, ordering, error modes, configuration and relevant performance characteristics.

**Implementation**: what's inside a module, its body of code. Distinct from **Adapter**: a thing can be a small adapter with a large implementation (a Postgres repo) or a large adapter with a small implementation (an in-memory fake). Reach for "adapter" when the seam is the topic; "implementation" otherwise.

**Depth**: leverage at the interface. The amount of behaviour a caller (or test) can exercise per unit of interface they have to learn. A module is **deep** when a large amount of behaviour sits behind a small interface, **shallow** when the interface is nearly as complex as the implementation.

**Seam** _(Michael Feathers)_: a place where behavior can vary without changing the caller at that place. Distinguish it from a domain boundary when that distinction matters to the project.

**Adapter**: a concrete thing that satisfies an interface at a seam. Describes *role* (what slot it fills), not substance (what's inside).

**Leverage**: what callers get from depth. More capability per unit of interface they learn. One implementation pays back across N call sites and M tests.

**Locality**: what maintainers get from depth. Change, bugs, knowledge, and verification concentrate in one place rather than spreading across callers. Fix once, fixed everywhere.

## Deep vs shallow

**Deep module** = small interface + lots of implementation:

```
┌─────────────────────┐
│   Small Interface   │  ← Few methods, simple params
├─────────────────────┤
│                     │
│  Deep Implementation│  ← Complex logic hidden
│                     │
└─────────────────────┘
```

**Shallow module** = interface complexity close to implementation complexity. Investigate whether it adds a necessary role, such as adaptation, security, protocol compatibility or ownership, before recommending its removal:

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Many methods, complex params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Just passes through
└─────────────────────────────────┘
```

When designing an interface, ask:

- Can I reduce the number of methods?
- Can I simplify the parameters?
- Can I hide incidental complexity without obscuring behavior, constraints or failure modes?

## Principles

- **Depth is a property of the interface, not the implementation.** A deep module can be internally composed of small, mockable, swappable parts; they just aren't part of the interface. A module can have **internal seams** (private to its implementation, used by its own tests) as well as the **external seam** at its interface.
- **The deletion test.** Imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep.
- **The interface is a useful test surface.** Prefer observable behavior at the relevant boundary. Internal invariants or safety properties may justify focused internal tests; needing one does not by itself prove the architecture wrong.
- **Actual variation is evidence for a seam.** Multiple adapters can demonstrate a real need, but adapter count alone neither requires nor forbids an interface. Consider existing contracts, safety constraints and the concrete cost of change.

## Designing for testability

Good interfaces make testing natural:

1. **Accept dependencies, don't create them.**

   ```typescript
   // Testable
   function processOrder(order, paymentGateway) {}

   // Hard to test
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **Make side effects explicit.** Pure transformations are useful where appropriate; mutation and effects remain valid when the interface and tests make their behavior clear.

   ```typescript
   // Testable
   function calculateDiscount(cart): Discount {}

   // Effectful alternative: verify the documented input mutation
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **Manageable surface area.** Reduce unnecessary concepts without hiding distinct responsibilities or assuming fewer methods automatically require fewer tests.

## Relationships

- A **Module** exposes the interface or interfaces its callers need; the project determines their responsibilities and access boundaries.
- **Depth** is a property of a **Module**, measured against its **Interface**.
- A **Seam** is where a **Module**'s **Interface** lives.
- An **Adapter** sits at a **Seam** and satisfies the **Interface**.
- **Depth** produces **Leverage** for callers and **Locality** for maintainers.

## Rejected framings

- **Depth as ratio of implementation-lines to interface-lines** (Ousterhout): rewards padding the implementation. We use depth-as-leverage instead.
- **"Interface" as the TypeScript `interface` keyword or a class's public methods**: too narrow: interface here includes every fact a caller must know.
- **"Boundary" without a defined meaning**: distinguish a domain boundary, interface or variation point where needed, using the project's established terms.

## Going deeper

- **Considering consolidation given its dependencies**, see [DEEPENING.md](references/DEEPENING.md): dependency options, boundary trade-offs and preservation of useful test coverage.
- **Exploring alternative interfaces**, see [DESIGN-IT-TWICE.md](references/DESIGN-IT-TWICE.md): compare materially different interfaces, using independent design agents only under the project's delegation and approval rules.
