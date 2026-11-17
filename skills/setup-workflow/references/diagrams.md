# Optional diagram configuration

Read when `excalidraw-diagram` is selected or its project settings change. This is setup guidance, not the consumer project's runtime policy.
Setup works without this package. Declining it leaves the other selected routes intact.

## Discuss only missing choices

Once optional support is selected, settle the routes and the worker's operating boundaries separately. Reuse existing delegation, artifact and environment rules:

- **Routes.** Select the applicable routes from the table below. This makes diagrams an option for relevant design questions, not a diagram after each step.
- **Worker.** Offer compatible separate-worker tools (use Orca when selected) or leave the diagram route unavailable. Do not impose a fixed model.
- **Output.** Use the parent artifact's existing rules or agree a project-specific destination, naming, visibility and revision authority.
- **Libraries.** When the selected routes need library assets, offer the allowed subset of `post-it`, `drwnio`, `system-design` and `software-architecture`, or no additional libraries. Refer to the package's library index for descriptions.
- **Rendering.** Ask about a renderer dependency, browser execution, download or network access only if the selected route needs it and existing rules do not settle it. Present the specific unresolved operation for approval or leave it unavailable. External transfer is a separate permission.

| Selected route | Useful visual question |
| --- | --- |
| `grilling`, `grill-with-docs`, `domain-modeling`, `wayfinder` | Which relationships or alternatives does the discussion need to compare? |
| `codebase-design` | Where are the interfaces and responsibilities? |
| `to-spec`, `to-plan` | How do components interact, and what architecture supports the agreed behavior? |
| `prototype` | Which supporting sketch clarifies the experiment without replacing its runnable output? |

Obtain bounded installation approval through the [deployment reference](skills.md#obtain-installation-approval). Neither selection nor installation supplies consent for any diagram.
For each suggested diagram, offer to draw it or continue in text. An explicit diagram request supplies consent to draw that diagram, not missing tool, download or publication permissions.

## Establish readiness without drawing

Read the package's short entrypoint, provenance notice and renderer setup requirements from the selected source.
Keep generation references and library JSON out of the setup conversation; those belong in the assigned worker's context.
Apply the deployment reference's [source and same-name checks](skills.md#check-same-name-copies).
Preserve an existing upstream global copy unless replacement was separately approved.

Check these prerequisites without launching a test agent:

- The designated tool supports a separate subagent with the approved authority. A same-context fallback is not a compatible substitute.
- The worker can read the installed entrypoint, generation references, renderer, approved library assets and authoritative design sources in its own environment.
- The worker can write both editable `.excalidraw` and PNG preview files beside the parent artifact under configured paths. Coordinator-local access is not evidence of worker access.
- The renderer's runtime, dependencies and browser are available or covered by an approved installation. Required network access is allowed; a local input file does not prove offline rendering.
- The worker can inspect the rendered preview. Distinguish known availability from untested execution or visual inspection.

Report a missing capability, source, asset, destination or rendering permission as a diagram-only blocker. Continue unrelated setup and design work.
Preserve the complete package and its notices. Some upstream parts have no stated license; package selection does not supply redistribution rights.

## Draft one project policy

Use the `excalidraw-diagram` section in the [AGENTS.md outline](AGENTS.md#outline) as the single policy in the generated project contract.
Fill its package pointer, designated delegation tool, artifact rules, allowed libraries and rendering permissions from agreed facts.
Add only the applicable per-skill pointers. Leave upstream prompts unchanged, including exact-copy `grill-with-docs`; compose through project instructions.
If a setting is unresolved, report its blocked action rather than saving an unresolved template field.
Do not add generic trigger/execution flags or duplicate the policy in each calling section.

In the setup handoff, distinguish approved configuration, installed/discoverable package, known worker prerequisites and untested behavior.
A walkthrough covers a declined offer, an explicit request, unavailable delegation, inaccessible worker assets and forbidden rendering access.
No diagram generation or substantive helper probe is authorized merely by this setup interview.
