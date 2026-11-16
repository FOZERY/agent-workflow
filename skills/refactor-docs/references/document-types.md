# Preserve each document's role

Read the applicable sections when editing ADRs, specifications or READMEs. The project's existing format and ownership remain authoritative.

## ADRs

Preserve status, decision date, context, considered alternatives, the chosen decision, reasons, consequences and replacement links. An accepted or superseded ADR is a historical record, not a fresh design proposal. Follow the project's immutability/correction procedure; where a section cannot be edited, propose the editorial correction separately. Keep the distinction between what was known at decision time and later evidence.

## Specifications and task documents

Preserve required behavior, acceptance criteria, scope exclusions, edge cases, dependencies and unresolved decisions. Keep examples distinguishable from requirements. Changing MUST to SHOULD, dropping a failure case or presenting an open question as settled changes the contract. Report conflicting requirements instead of resolving them through wording. For read-only external specifications, propose corrections in the approved channel rather than creating a competing local specification.

## READMEs and technical guides

Organize around the intended reader's task and the project's required sections. Preserve prerequisites, working commands, compatibility constraints, warnings, limitations and documentation links. Separate an example value from a required setting. Remove repeated marketing language without replacing it with invented performance or reliability claims. Keep existing installation and operational facts unless a separately authorized technical update has evidence.
