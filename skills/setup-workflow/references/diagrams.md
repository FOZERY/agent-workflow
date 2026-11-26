# Optional diagram configuration

Read this file when the user selects `draw-diagram` or changes its settings. It guides setup; it is not the project's runtime policy.
Setup works without this skill. If the user declines it, the other selected routes stay as they are.

## Agree the open choices

Reuse the existing delegation, artifact and environment rules. Ask only about choices that they do not settle:

1. **Routes.** Select the routes from the table below. A diagram becomes an option for a relevant design question, not a step after every task.
2. **Worker.** Offer the tools that can run a separate worker, for example Orca when selected. If none fits, leave the diagram route unavailable. Prescribe no fixed model.
3. **Output.** Use the rules of the parent artifact, or agree a destination, naming, visibility and who can revise the diagram.
4. **Libraries.** If the routes need library assets, offer the allowed subset of `post-it`, `drwnio`, `system-design` and `software-architecture`, or no libraries. The skill's library index describes them.
5. **Rendering.** Ask about a renderer dependency, browser execution, a download or network access only if the route needs it and existing rules do not settle it. Ask for approval of that exact operation, or leave it unavailable. Sending data outside is a separate permission.

| Selected route | Visual question that helps |
| --- | --- |
| `grilling`, `grill-with-docs`, `domain-modeling`, `wayfinder` | Which relationships or alternatives does the discussion compare? |
| `to-spec`, `to-plan` | How do the components interact, and which architecture supports the agreed behavior? |
| `prototype` | Which sketch explains the experiment? The sketch does not replace the runnable prototype. |

Get a bounded installation approval through [deployment](skills.md#install-plan-and-approval).

The consent rules live in the `draw-diagram` section of the [outline](AGENTS.md#outline) and in the skill itself. Setup draws no diagram and launches no helper probe.

## Check readiness without drawing

1. Read the skill's short entry point, its provenance notice and its renderer requirements from the selected source.
2. Leave the generation references and library JSON to the worker. Keep them out of the setup conversation.
3. Run the [source and same-name checks](skills.md#check-same-name-copies).
4. Check these prerequisites without launching a test agent:
   - The selected tool can run a separate subagent with the approved authority. A worker in the same context is not a substitute.
   - The worker can read, in its own environment, the installed entry point, the generation references, the renderer, the approved library assets and the design sources.
   - The worker can write the editable `.excalidraw` file and the PNG preview next to the parent artifact, under the configured paths. Access from the coordinator does not prove access from the worker.
   - The renderer's runtime, dependencies and browser are available or covered by an approved installation. Needed network access is allowed. A local input file does not prove offline rendering.
   - The worker can inspect the rendered preview.
5. Report each prerequisite as known available or not tested.
6. Report a missing capability, source, asset, destination or rendering permission as a blocker of diagrams only. Continue the other setup and design work.

## Write one project policy

1. Use the `draw-diagram` section of the [AGENTS.md outline](AGENTS.md#outline) as the only diagram policy in the project.
2. Fill its skill pointer, delegation tool, artifact rules, allowed libraries and rendering permissions from the agreed facts.
3. Add a diagram pointer only to the sections of selected skills that use diagrams.
4. Keep the exact copy of `grill-with-docs` unchanged. Connect diagrams through project instructions.
5. If a setting is open, record its blocked action. Save no unfilled template field.
6. Add no trigger or execution flags for diagrams.

In the setup report, keep apart: the approved configuration, the installed and discoverable skill, the known worker prerequisites and the untested behavior.
Check these cases: a declined offer, an explicit request, unavailable delegation, worker assets that the worker cannot read, and forbidden rendering access.
