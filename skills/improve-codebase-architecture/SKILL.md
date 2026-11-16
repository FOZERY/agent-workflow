---
name: improve-codebase-architecture
description: Investigate architectural friction, compare evidence-based improvement candidates and explore a selected design within project constraints.
disable-model-invocation: true
---

# Improve Codebase Architecture

Surface architectural friction and compare improvements. Deepening shallow modules is one useful approach, not the required outcome of every review. This skill diagnoses and proposes; implementation requires a separate authorized task.

Read root `AGENTS.md` and its architecture/domain pointers for accepted decisions, terminology, scope, permissions and report/diagram conventions. Use `codebase-design` as a design lens through the current client's skill mechanism, while retaining project vocabulary and intentional architectural roles.

## Process

### 1. Explore

**Scope before you scan: YAGNI.** Deepening a module pays off by making future changes to it easier, so put extra weight on the parts of the codebase that have recently changed. Decide *where* to look before you look:

- If the user named a direction (a module, a subsystem, a pain point), take it, and skip the inference below.
- Otherwise, walk back a good stretch of the commit history (`git log --oneline`) to find the codebase's hot spots, the files and areas that keep coming up, and let those paths pull your attention first. If the changes are scattered with no clear hot spot, widen the net.

Read the relevant project terminology and accepted architectural decisions from their authoritative locations; a glossary or ADR directory is not required if the project uses other sources.

Explore within the agreed scope, using the project's read-only delegation policy where helpful and permitted. Give any helper a bounded question and fresh context. Note observed friction and its source:

- Where does understanding one concept require bouncing between many small modules?
- Where are modules **shallow**, with an interface nearly as complex as the implementation?
- Where have pure functions been extracted just for testability, but the real bugs hide in how they're called (no **locality**)?
- Where do tightly-coupled modules leak across their seams?
- Which parts of the codebase are untested, or hard to test through their current interface?

Use the **deletion test** as a diagnostic question, not proof that an abstraction should be removed. Check whether an apparently shallow layer enforces a real contract, safety property or ownership boundary. Separate observed friction from speculative future benefits.

### 2. Present evidence and candidates

Use the project's report language, format and location. A conversational or Markdown report is valid; HTML, diagrams or external boards are optional surfaces, not mandatory publication. Agree any missing storage/write choice before creating an artifact. Preserve existing sources and report write blockers instead of silently publishing elsewhere.

For each candidate show the affected modules/files, observed problem and evidence, a proposed direction, expected benefits and costs, constraints and test/migration implications, and confidence. Use before/after diagrams when they clarify a relationship; label the after state as proposed and any unmeasured benefit as an expectation. Link editable diagram sources according to project rules.

Use [HTML-REPORT.md](references/HTML-REPORT.md) only when an HTML report is selected. Remote renderers, CDN dependencies, browser opening and external-board writes require the relevant project/user authorization; an architectural investigation does not grant it.

Rank candidates by the demonstrated problem, cost and project priorities. If a proposal conflicts with an accepted decision, identify the exact conflict and evidence for reconsideration rather than treating it as already approved. No finding is also a valid outcome.

Ask which candidate, if any, the user wants to explore, unless the selection is already explicit. Present direction and trade-offs here, leaving detailed alternative interfaces for that focused discussion.

### 3. Grilling loop

Once a candidate is selected, use `grilling` to examine constraints, dependencies, interface alternatives, relevant tests and migration costs. Keep the framing open to retaining the current architecture.

Use `domain-modeling` when terminology or a consequential decision needs clarification. Propose document updates in their authoritative locations and apply only approved writes through its project procedure; do not automatically edit domain records as conversation unfolds. A consequential rejection may merit an ADR, but not every preference or temporary deferral does.

For materially different interface alternatives, use `codebase-design`'s design-it-twice reference under the project's delegation and approval rules. Capture the selected direction and remaining questions in the agreed place. This discussion does not implement it.

**Done when:** the scoped findings and evidence are presented in the agreed form, and any selected design has an explicit decision or unresolved questions. Report permission/access limits; never present a proposed architecture as delivered code.
