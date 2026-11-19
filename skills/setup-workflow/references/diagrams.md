# Optional diagram configuration

Read this file when the user selects `excalidraw-diagram` or changes its settings. It guides setup; it is not the project's runtime policy.
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
| `codebase-design` | Where are the interfaces and responsibilities? |
| `to-spec`, `to-plan` | How do the components interact, and which architecture supports the agreed behavior? |
| `prototype` | Which sketch explains the experiment? The sketch does not replace the runnable prototype. |

Get a bounded installation approval through [deployment](skills.md#install-plan-and-approval).

Consent rules:

- Selection or installation of the skill is not consent to draw a diagram.
- For each suggested diagram, offer two options: draw it, or continue in text.
- An explicit request for a diagram is consent to draw that diagram. It does not give a missing tool, download or publication permission.

## Check readiness without drawing

1. Read the skill's short entry point, its provenance notice and its renderer requirements from the selected source.
2. Leave the generation references and library JSON to the worker. Keep them out of the setup conversation.
3. Run the [source and same-name checks](skills.md#check-same-name-copies). Keep an existing upstream global copy unless the user approved its replacement.
4. Check these prerequisites without launching a test agent:
   - The selected tool can run a separate subagent with the approved authority. A worker in the same context is not a substitute.
   - The worker can read, in its own environment, the installed entry point, the generation references, the renderer, the approved library assets and the design sources.
   - The worker can write the editable `.excalidraw` file and the PNG preview next to the parent artifact, under the configured paths. Access from the coordinator does not prove access from the worker.
   - The renderer's runtime, dependencies and browser are available or covered by an approved installation. Needed network access is allowed. A local input file does not prove offline rendering.
   - The worker can inspect the rendered preview.
5. Report each prerequisite as known available or not tested.
6. Report a missing capability, source, asset, destination or rendering permission as a blocker of diagrams only. Continue the other setup and design work.
7. Keep the complete skill and its notices. Some upstream parts have no stated license; selection of the skill gives no redistribution rights.

## Write one project policy

1. Use the `excalidraw-diagram` section of the [AGENTS.md outline](AGENTS.md#outline) as the only diagram policy in the project.
2. Fill its skill pointer, delegation tool, artifact rules, allowed libraries and rendering permissions from the agreed facts.
3. Add a diagram pointer only to the sections of selected skills that use diagrams. Keep one copy of the policy.
4. Keep upstream skill files unchanged, including the exact copy of `grill-with-docs`. Connect diagrams through project instructions.
5. If a setting is open, record its blocked action. Save no unfilled template field.
6. Add no trigger or execution flags for diagrams.

In the setup report, keep apart: the approved configuration, the installed and discoverable skill, the known worker prerequisites and the untested behavior.
Check these cases: a declined offer, an explicit request, unavailable delegation, worker assets that the worker cannot read, and forbidden rendering access.
The setup interview authorizes no diagram and no helper probe.
