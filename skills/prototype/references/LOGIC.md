# Logic Prototype

Use this pattern when the approved surface is an interactive HTML demo of **business logic, state transitions or data shape**. A single self-contained file can let non-developers exercise cases directly, but other project-approved surfaces remain valid under the [prototype procedure](../SKILL.md).

Use the reader's domain language and state the experiment's limitations. Portability is useful only if the chosen surface can actually answer the question.

## When this is the right shape

- "I'm not sure if this state machine handles the edge case where X then Y."
- "Does this data model actually let me represent the case where..."
- "I want to feel out what the API should look like before writing it."
- Anything where someone wants to **press buttons and watch state change**.

If the question is "what should this look like," this is the wrong branch. Use [UI.md](UI.md).

## Process

### 1. State the question

Before writing code, write down what state model and what question you're prototyping. One paragraph, at the top of the demo (in a visible intro, not just a comment). A logic prototype that answers the wrong question is pure waste, so make the question explicit so it can be checked later, whether the user is watching now or returning to it AFK.

### 2. Isolate the logic in a portable module

Separate the logic answering the question from presentation. For this HTML pattern, a small inline module is often sufficient; use project conventions where the experiment requires them. Potentially reusable logic still needs separate implementation approval and verification before production use.

The right shape depends on the question:

- **A pure reducer**: `(state, action) => state`. Good when actions are discrete events and state is a single value.
- **A state machine**: explicit states and transitions. Good when "which actions are even legal right now" is part of the question.
- **A small set of pure functions** over a plain data type. Good when there's no implicit current state, just transformations.
- **A class or module with a clear method surface** when the logic genuinely owns ongoing internal state.

Pick the form that fits the question and existing contracts. Keep state transitions inspectable and presentation effects distinct where practical. A portable module can preserve the experiment's evidence; portability is not proof that it is production-ready.

### 3. Build the shareable HTML file

When standalone HTML is the agreed surface, prefer inline HTML/CSS/JS so the recipient can open it without a toolchain. If the question needs a framework or server, use the authorized surface and document its real prerequisites rather than claiming a single file is sufficient.

Write it for a non-developer. Every label is in **domain language**, not code: buttons and state read like the business, not the reducer. Explain in plain words what's happening.

Lay it out with a clean hierarchy, top to bottom:

1. **Title and one-line explanation** of what this demo lets you explore (the question from step 1).
2. **Current state**: the full relevant state, rendered as a readable panel (labelled fields, not a raw JSON dump), re-rendered after every click so the change is visible. Where it helps a non-developer follow, call out what just changed.
3. **Free-play buttons**: one button per action, always available, so anyone can poke at the model in any order. Each click dispatches its action and re-renders the state.
4. **Guided walkthroughs**: a set of **scenarios**, one per tab. Each tab holds a short plain-language description of the scenario (the situation it sets up and what to watch for) and underneath it, the ordered **buttons to press** for that scenario. Each step is a real button: clicking it performs that action and moves to the next step. Starting a walkthrough resets to a known initial state so the scenario runs the same way every time.

Choose scenarios that demonstrate the awkward cases, the ones hard to reason about on paper: the happy path, a tricky edge case, an attempt at something that should be illegal.

Keep it beautiful but restrained: clean typography, generous spacing, one accent colour. No animations, no gimmicks: nothing that competes with the state and the buttons.

### 4. Hand it over

Provide the verified file or viewing method. Open a browser only under the applicable environment permissions. Invite the reader to exercise the guided and free-play cases and capture observations separately from assumptions; new actions or scenarios should stay within the agreed question.

### 5. Capture the answer and the prototype

Capture the answer, evidence and limitations under the [prototype procedure](../SKILL.md). Preserve the experiment in its agreed location or archive. Reusing the logic, changing production modules or performing Git operations is a separate authorized action, not an automatic consequence of confirming the model.

## Anti-patterns

- **Omitting verification needed to trust the answer.** Use focused checks for the question and project-required safety checks; production-level completeness is not the goal.
- **Don't wire it to the real database.** Use in-memory state unless the question is specifically about persistence.
- **Don't generalise.** No "what if we wanted to support X later." The prototype answers one question.
- **Don't blur the logic and the page together.** If the pure module references the DOM, `document`, or button handlers, it's no longer liftable. Keep the page as a thin shell over a pure module.
- **Adding a toolchain without a reason.** Use the agreed simplest workable surface; a framework/server is justified only when it helps answer the actual question within project permissions.
- **Shipping experimental code as a finished feature.** Treat production implementation and its verification as separate work.
