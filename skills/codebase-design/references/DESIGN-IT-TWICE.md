# Design It Twice

When materially different interfaces could address a chosen design problem, compare independent alternatives where the project's delegation policy permits. The current design remains a candidate; deepening is one possible outcome, not the required answer.

Uses the vocabulary in [SKILL.md](../SKILL.md): **module**, **interface**, **seam**, **adapter**, **leverage**.

## Process

### 1. Frame the problem space

Before spawning sub-agents, write a user-facing explanation of the problem space for the chosen candidate:

- The constraints any new interface would need to satisfy
- The dependencies it would rely on, and which category they fall into (see [DEEPENING.md](DEEPENING.md))
- A rough illustrative code sketch to ground the constraints, not a proposal, just a way to make the constraints concrete

Explain the problem and proposed comparison. Obtain any required approval for delegation, roles, agent count and resource use before dispatching; presenting a brief is not consent.

### 2. Explore alternatives

Use the approved number of fresh-context design agents through the harness's configured roles/models. If delegation is unavailable or not approved, explore alternatives in the main agent and state that they were not independently produced. Do not force a fixed agent count.

Give each worker a bounded brief with the real constraints, relevant source pointers and a distinct design emphasis. The following emphases are examples, not a required set:

- Agent 1: "Minimize the interface: aim for 1–3 entry points max. Maximise leverage per entry point."
- Agent 2: "Maximise flexibility: support many use cases and extension."
- Agent 3: "Optimise for the most common caller: make the default case trivial."
- Agent 4 (if applicable): "Design around ports & adapters for cross-seam dependencies."

Include the relevant project terminology and accepted decisions from their actual sources, plus the useful vocabulary from [SKILL.md](../SKILL.md). Preserve established architectural names instead of requiring a root `GLOSSARY.md` or renaming concepts.

Each sub-agent outputs:

1. Interface (types, methods, params, plus invariants, ordering, error modes)
2. Usage example showing how callers use it
3. What the implementation hides behind the seam
4. Dependency strategy and adapters (see [DEEPENING.md](DEEPENING.md))
5. Trade-offs: where leverage is high, where it's thin

### 3. Present and compare

Present the actual alternatives and compare contract compatibility, complexity, locality, testability, migration cost and risks. Use depth and seam placement where those concepts clarify the trade-off.

Recommend the best-supported direction, including retaining the current design if appropriate. Explain evidence and uncertainties; a recommendation or hybrid sketch does not authorize implementation or recording an accepted ADR.
