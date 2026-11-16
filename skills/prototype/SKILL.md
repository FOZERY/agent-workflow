---
name: prototype
description: Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like.
user-invocable: false
---

# Prototype

A prototype is a **disposable experiment that answers a question**, not a production change. Read root `AGENTS.md` and its prototype, artifact, environment and data-access rules. Establish the question, observable result needed to answer it, approved surface and retention before changing files or systems. Permission to prototype does not authorize production integration, commit, push or publication.

## Defaults

Use these when the project instructions settle nothing for prototypes, and mention once that `setup-agents-workflow` can configure the project. Confirm with the user before the first file write.

- **Logic question:** one self-contained HTML file following [LOGIC.md](references/LOGIC.md), saved as `.docs/prototypes/<slug>/index.html`.
- **UI question:** variants on the existing page, switched by a `?variant=` parameter, following [UI.md](references/UI.md). Build 3 variants, at most 5.
- **Data:** in-memory fixtures.
- **Retention:** once the user has the answer, record it and propose removing the prototype files; keep them only when the user asks.

## Pick a branch

Identify which question is being answered, using the user's prompt, the surrounding code, or by asking if the user is around:

- **"Does this logic / state model feel right?"**: use an approved executable experiment, simulation or visual model. If the agreed surface is an interactive HTML state demo, read [LOGIC.md](references/LOGIC.md).
- **"What should this look like?"**: explore distinct UI alternatives on the project's approved surface, such as an isolated route, existing component playground or mockup. For a runnable UI experiment, read [UI.md](references/UI.md) and adapt its presentation patterns.

Choose from the stated question and surrounding context. Clarify ambiguity that changes what the experiment proves or its safety; otherwise state the bounded assumption. The project determines the artifact format, not the branch name.

## Rules that apply to both

1. **Mark it as experimental.** Use the agreed sandbox or project location and distinguish it from production. Preserve existing routing and working-copy ownership.
2. **Make it easy to inspect.** Provide the actual command, URL or opening method for the selected surface, along with prerequisites. Verify that surface within the allowed environment; do not claim it runs from merely writing files.
3. **Isolate data and side effects.** Prefer in-memory state or explicitly approved disposable data. Use no production credentials or live writes without separate authorization; persistence experiments need a bounded recovery plan.
4. **Validate the question, not a product.** Use the minimum checks needed to trust the experiment's answer, plus project-required safety checks. Label simplifications and untested behavior; neither a blanket ban on tests nor production-level polish is required.
5. **Expose the relevant state.** Make the conditions, actions and outcomes visible enough to judge the stated question. Separate observed results from hypotheses.
6. **Capture the answer.** Record what was learned, remaining limitations and any accepted decision in the project's authoritative location. Retain or retire the prototype under the agreed lifecycle, with a usable source pointer. Implementation of a chosen solution is a separate authorized task; no throwaway branch or automatic Git operation is required.
