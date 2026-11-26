---
name: refactor-docs
description: Rewrite existing documentation and project memory for clarity and structure without changing what it says.
disable-model-invocation: true
---

# Refactor docs

Rewrite the wording and the structure of existing documents, `CONTEXT.md` and `LESSONS.md`. Keep every decision, requirement and fact.

Other work goes elsewhere:
- a change to a decision, a requirement or a rule in `AGENTS.md` or a skill needs its own approved change;
- removing files is `cleanup-artifacts`;
- code is `refactor-codebase`.

## 1. Find the writing rules

1. Read the project instructions for language, style, document format and required sources.
2. If the project names a writing skill, use it. Otherwise use `writing-technical` if it is installed, or the rules in step 3.

**Done when:** you know the writing rules, and every required source is readable.

## 2. Find what must stay

1. Read the documents. Find the reader, the purpose, the sources, the format, the language and what you may edit.
2. For an ADR, a spec, a README or project memory, read [the document-type rules](references/document-types.md).
3. Keep a copy of the original for comparison.
4. List each claim, requirement, decision, reason, alternative, limit, example and open question, with its scope and source link.

Keep these exactly: commands, code, paths, identifiers, API names, error text, dates, numbers and units. Keep negations, conditions, exceptions, defaults, order, approval gates and the strength of each rule, for example MUST versus SHOULD.

If content is ambiguous or contradicts itself, check the source. If the source does not settle it, leave the text and ask the owner.

A request to edit named documents is permission to edit those documents.

**Done when:** you have the files, their required structure and the list of what must stay, and each ambiguity is settled or left out of the edit.

## 3. Rewrite

- Start with the fact. Name who acts. Put one idea in each sentence. Group related facts.
- Remove filler and repeats only when no fact, condition or reason goes with them. Keep caveats, counterexamples and trade-offs.
- Mark a claim without evidence. Do not add precision that the source does not have.
- Keep deliberate terms and the existing structure.
- Prefer small, targeted edits. Leave unrelated files and other people's edits.
- Before you move text between files, split a file, change a heading or anchor, or change who owns a document, show the change with its affected links and get approval.
- Keep questions to the user in the chat, not in the document.

**Done when:** each edit makes the text clearer, and everything from the step 2 list is still in its proper place.

## 4. Check and report

1. Compare the original and the new text by meaning, not by length. Check the step 2 list item by item.
2. Restore anything that you weakened, strengthened or dropped. A proposal stays a proposal. A past fact stays a past fact.
3. Check changed headings, anchors, links, images and generated tables of contents. Run the project's documentation check if it has one.
4. Report the edited files, structural changes, checks, and the claims or links that you could not verify.

If the text already meets the standard, say so and make no edits.
