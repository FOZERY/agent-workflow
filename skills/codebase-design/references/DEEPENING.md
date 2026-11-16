# Deepening

Use this reference when considering consolidation of modules and their dependencies. Apply the lens from [SKILL.md](../SKILL.md) within accepted project architecture; these are proposal patterns, not permission to merge modules or change tests.

## Dependency categories

Classify dependencies to evaluate costs, isolation and verification options. The category informs a recommendation; it does not determine the project's architecture or test framework.

### 1. In-process

Pure computation or in-memory state may be consolidated where one responsibility and caller contract become clearer. Preserve useful boundaries and focused invariants; being in-process does not by itself justify merging modules.

### 2. Local-substitutable

A local substitute, such as an embedded database or in-memory filesystem, may support realistic tests. Check fidelity for the behavior under review; a substitute's existence does not prove equivalence or require hiding the dependency behind a particular interface.

### 3. Remote but owned (Ports & Adapters)

Owned services across a network boundary may benefit from explicit contracts and transport isolation. Ports and adapters are one option, not a universal requirement. Compare this with the project's existing service boundaries, ownership and contract/integration tests.

Where appropriate, propose an injected transport and a suitable test implementation, stating which real network/failure properties still need verification.

### 4. True external (Mock)

For third-party services, compare the project's approved SDK boundary, contract tests, sandbox access and test doubles. Injected ports and mock adapters can help isolate logic but do not prove the live integration or justify a new abstraction without a concrete need.

## Seam discipline

- **Evidence before indirection.** Actual variation, a stable contract or a safety/ownership constraint can justify a seam. Adapter count is a clue, not a mandatory threshold.
- **Internal seams vs external seams.** A deep module can have internal seams (private to its implementation, used by its own tests) as well as the external seam at its interface. Don't expose internal seams through the interface just because tests use them.

## Preserve useful test coverage

- Compare proposed boundary-level tests with existing coverage, including internal invariants and failure cases.
- Recommend retiring a test only when its consumer-relevant protection is demonstrably redundant or its contract is intentionally changed. Never prescribe blanket deletion merely because modules are consolidated.
- Prefer tests of observable behavior at the appropriate interface; focused internal tests can remain valuable.
- Record test migration and remaining verification needs as part of the proposal. Implementing that migration belongs to the separately authorized change.
