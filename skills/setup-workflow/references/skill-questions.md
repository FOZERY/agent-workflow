# Questions for optional skills

Read the part for a skill only when the user selects that skill or changes its settings.
Record each answer in the skill's section of the project's `AGENTS.md`.

## to-plan

1. Agree the plan location and naming. Keep the plan with the other artifacts of its task where the project permits.
2. Ask about visibility. Offer only the allowed options: tracked in Git, ignored in the repository, or an approved private location.
3. Ask about approval. Options: the agent saves a draft for review, or the user approves the plan before the agent saves it. Use the project's procedure for other checkpoints.
4. Ask who can change an approved plan. Options: the agent within agreed limits, the agent with approval for each change, or the plan owner only.
5. Agree the executor that receives the plan. Check that it can take the plan and the source task without a new spec or tickets.
6. Record that approval of a plan does not start implementation. The user starts implementation separately.

Configure the handoff in `AGENTS.md`. Keep the installed skill files unchanged.

## Trackers: to-spec, to-tickets, wayfinder

1. Ask which sources own the requirements and the tickets.
2. If `wayfinder` is selected, ask where its decision map belongs.
3. List the tracker operations that the selected skills need: read, create, edit, comment, label, assign, link, change state, close.
4. For each operation, ask for one option: allowed within a named scope, needs separate approval, or human only. Ask only about operations that the selected skills need.
5. Record that a readiness label does not authorize starting work or publishing.
6. If the project has no adequate tracker procedure, use the seed for the selected tracker:
   - [GitHub](issue-tracker-github.md)
   - [GitLab](issue-tracker-gitlab.md)
   - [Local Markdown](issue-tracker-local.md)
7. For another tracker, write the procedure from its agreed sources and access method.

Keep the readiness labels that the selected skills need. Setup does not configure incident triage.
Read [domain documents](domain.md) only when glossary or ADR conventions need configuration.

## excalidraw-diagram

1. Offer the bundled `excalidraw-diagram` skill as an option for visual design support.
2. If the user selects it or changes its settings, read [diagram configuration](diagrams.md).
3. Agree one diagram policy for the project. Link it from the sections of the skills that use diagrams.

Selection of the skill does not give consent to draw a diagram.
