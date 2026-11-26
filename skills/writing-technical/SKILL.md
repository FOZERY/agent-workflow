---
name: writing-technical
description: "Write or edit technical artifacts in ASD-STE100 style: documentation, skills, AGENTS.md, READMEs, ADRs, specifications, tickets, reports, CONTEXT.md and LESSONS.md. Use for artifact prose for people or agents, including drafts returned in chat."
---

# Writing technical

Write technical artifacts so that the reader can identify the fact, action and condition without guessing.
Keep the project's document format, language, technical meaning and approval rules.

## Scope

This skill works on its own. The task and project instructions determine where it applies.

ASD-STE100 is controlled English. This skill is a writing profile based on it, not a claim of full conformance.
Before you write or edit an artifact in Russian, read [the Russian rules](references/ru.md).
For an artifact in another language, keep its language and adapt the clarity principles.
Use the principles and examples below. Do not look up the standard or its dictionary. Take the artifact's facts from its own sources.

## Principles

- **One term, one concept.** Use the project's accepted terms. Define an unfamiliar term at first use.
  Use the words that developers say. Do not invent a term when a common word exists.
- **Real names.** Write the actual command, file, flag, setting or symbol, not a description of it.
- **One idea per sentence.** Keep descriptions to 25 words per sentence.
  Keep each paragraph on one topic, with no more than six sentences.
- **One sequential action per step.** Keep procedural sentences to 20 words.
  Give direct instructions in the imperative. Keep simultaneous actions together when separating them would change the operation.
- **Condition before action.** Put a prerequisite before the command that depends on it.
- **Actor and verb.** Prefer active voice and simple present, past or future.
  In descriptions, passive voice is an exception for an unknown actor. Do not invent the actor.
- **Complete, simple sentences.** Keep necessary subjects, articles and connecting words.
  Expand contractions. Use periods instead of semicolons in prose.
  Write `and` or `or` instead of a slash. Write the plural instead of `(s)`.
- **Clear word relations.** Break ambiguous noun chains into explicit relations.
  The normal limit is three words. Preserve an established longer technical name and explain it where needed.
  Put `only` and `not` next to the word that they change.
  Make each `it`, `this`, `they` and `which` point to one obvious noun, not to a full sentence.
  If `and` and `or` are in one sentence, show which parts each word joins, or split the sentence.
- **Lists.** Use a numbered list for a sequence and a bulleted list for other items.
  Introduce each list with a complete sentence. Give all items the same grammatical form.
- **Literal language.** Replace figurative expressions and noun-heavy actions with the actual operation.
  Check an `-ing` form by its function: technical nouns and approved entries can be valid.
- **Visible requirements and risks.** Keep required actions and limits out of informational notes.
  Put a risk notice before the hazardous action and state the consequence. Preserve the project's risk labels.
- **No empty words.** Delete words that add no fact, condition or action.
- **Meaning before brevity.** Preserve negation, quantifiers, exceptions, order, uncertainty, decision status and mandatory modal words.
  Keep code, commands, identifiers, paths, quotations, units and numbers intact. Rewrite the surrounding prose instead.

If a rule makes a sentence worse, rewrite the sentence in a different way or keep it.

Use American spelling unless a project directive requires another spelling.
Do not count code, identifiers, numbers with units or quoted text toward the word limits.

## Replace ambiguity with an observable fact

The values and decisions in these examples do not set requirements for the current project.

| Instead of | Write | What changed |
| --- | --- | --- |
| After checking the config, restart the service and verify the response. | 1. Check the configuration.<br>2. Restart the service.<br>3. Check the response. | Three sequential actions become three steps. |
| Delete the backup if the restore check passed. | If the restore check passed, delete the backup. | The reader sees the prerequisite first. |
| If a job fails three times, the worker must perform a transition of its state to `failed`. | If a job fails three times, the worker must set the job state to `failed`. | The verb names the required action. |
| The migration has been completed on `abc123`, although the row-count check has not been run. | The migration completed on `abc123`. The row-count check was not run. | The event and verification gap have separate sentences. |
| Our proposed decision is to leverage Redis as the cache, but no performance measurement is available. | Status: Proposed. Use Redis as the cache. No performance measurement is available. | The proposal and evidence limit remain explicit. |
| If configuration validation fails, make an error notification. | If the configuration is not valid, show the error. | The condition and action replace noun-heavy wording. |
| Run the test command. | Run `pnpm test`. | The reader gets the real command. |
| Check the leading word of the pointer. | Check that the skill description says when to use the skill. | A common phrase replaces an invented term. |
| The worker only runs the tests after review. | The worker runs the tests only after review. | `only` limits the time, not the action. |
| The orchestrator sends the brief to the worker. This can fail. | The orchestrator sends the brief to the worker. The dispatch can fail. | The subject names the thing that fails. |
| Run lint and typecheck or tests. | Run lint. Then run typecheck or the tests. | Each sentence shows what `and` and `or` join. |
| Commit/push the file(s). | Commit the files. Push only with permission. | Two actions get two sentences. The plural replaces `(s)`. |
| Build the package, run the tests and then commit. | 1. Build the package.<br>2. Run the tests.<br>3. Commit. | A sequence becomes a numbered list. |
| It is important to make sure that you run the tests. | Run the tests. | The empty words are gone. |

## Preserve the artifact's role

- **ADRs:** preserve status, date, alternatives, decision, reasons and consequences. Follow the project's historical-record policy.
- **Specs and tickets:** preserve scope, failure behavior, dependencies and checkable acceptance criteria.
  Separate required behavior from implementation advice and test procedures.
- **Context:** record the dated event, source, observed result, uncertainty and remaining work.
- **Lessons:** record confirmed experience or preferences, their source and applicable conditions.
  Propose mandatory rules separately through their authoritative instruction source.
- **Reports and guides:** separate supported findings, expected output and observed output. Keep prerequisites and exact commands.

## Before delivery

Read the whole artifact against its authoritative sources.
Check meaning, sentence limits, consistent terms, required fields and local links.
Keep unresolved facts explicit instead of inventing precision.
Save only through the authorized writer and destination, or return an explicit unpublished proposal.

**Done when:** the complete artifact preserves the agreed content, follows this profile and has a clear delivery and verification state.
