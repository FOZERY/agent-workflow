# Project planning procedures

Read when configuring or revising enabled `wayfinder`, `to-spec` or `to-tickets` routes. Discuss only applicable branches. Reuse existing procedures and ask about missing decisions, not facts already documented.

## Maps and decision work

For wayfinding, establish the authoritative map location and representation of decision items: tracker records, local files or sections. Ask how dependencies, unresolved questions, accepted answers and out-of-scope decisions are represented. Which acceptance criteria make a prerequisite settled? Who may select or claim the next question, and how is concurrent ownership visible?

Agree permitted operations separately: reading, drafting, creating records, assigning, linking, commenting, transitioning and retiring. A read-only tracker can supply context while proposed map changes go to its owner; creating a local substitute requires agreement. Preserve decision history. Ordinary fact finding uses the exploration policy; deep investigations can use `research` and its approved report destination.

## Specifications and task decomposition

Identify who owns requirements and whether an analyst's specification or existing task graph is already authoritative. Ask which fields and acceptance criteria the project requires, how unknowns are represented and who confirms completeness. Distinguish an editable specification from proposed corrections to a read-only source.

For decomposition, agree suitable ticket granularity, dependency and parent/child conventions, required acceptance fields and any migration constraints. Check existing work before proposing missing tickets. Decide who approves the breakdown and which records the agent may actually write. Format, initial states and local grouping follow project conventions; there is no required label or one-file-per-ticket layout.

Record the difference between dependency-ready, accepted, assigned and authorized to execute. Finishing a spec or ticket plan neither dispatches implementation nor closes its parent requirement. Unavailable writing access leaves a proposal and owner action, not an automatically created shadow tracker.

## Prototype experiments

Ask where experiments may run: an isolated workspace, preview/story surface, approved application route, standalone demo or another existing mechanism. Establish permitted datasets, read/write access, tools/runtime/network effects and how production exposure is prevented.

Agree what evidence is sufficient to answer the experiment's question, how the owner views it, and any required safety checks. Set the result/source location, retention or recovery rules and authority to retire artifacts. Selecting a prototype direction is not approval to integrate its code, promote routes, commit or publish. Preserve the distinction between demonstrated behavior and untested assumptions.

## Architecture investigation and decisions

Establish accepted architectural constraints and the authoritative terminology/decision sources. Ask whether comparison may challenge a previous decision and who accepts a replacement. Deep modules are one analysis lens; preserve intentional project service, component, security and ownership boundaries.

Agree report language, audience, format and location. Diagrams may be Markdown/Mermaid, local assets or an existing board; verify allowed renderers, external-resource use and read/write rights. Browser opening and external-board edits have their own permission requirements. HTML and a temporary file are options, not defaults for every project.

Confirm checkpoints for selecting a candidate, comparing interface alternatives and recording a decision. Reuse the delegation policy for roles/models, independent design work and its approval; do not prescribe an agent count. Diagnosis, recommendation, accepted ADR and implementation are separate outcomes.

## Capture the agreements

Put the applicable permissions and start/acceptance rules in root `AGENTS.md` or its existing workflow owner. Link established tracker, requirements, prototype and architecture procedures at the actions that need them. Create a focused supporting document under the agreed namespace only when detail warrants one; these interview notes are not themselves the project's runbook.

**Done when:** enabled routes have authoritative sources, output formats/locations, ownership, acceptance/start criteria and permitted operations, with missing access or decisions explicitly assigned to a human. Existing sources remain authoritative and setup has not executed planning tasks, experiments or tracker mutations.
