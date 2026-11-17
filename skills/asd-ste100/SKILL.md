---
name: asd-ste100
description: "Write or edit technical artifacts in ASD-STE100 style: documentation, ADRs, specifications, tickets, reports, CONTEXT.md and LESSONS.md. Use for artifact prose for people or agents, including drafts returned in chat."
---

# ASD-STE100 artifact writing

Write technical artifacts so that the reader can identify the fact, action and condition without guessing.
Keep the project's document format, language, technical meaning and approval rules.

## Scope

Use this skill for documentation, ADRs, specifications, tickets, reports, descriptions, `CONTEXT.md` and `LESSONS.md`.
It applies whether a person or an agent reads the artifact, including an artifact draft returned in chat.
This package works on its own. The task and project instructions determine where this style applies.

ASD-STE100 is controlled English. This skill uses an **STE-based project profile**, not a claim of full conformance.
For a required non-English artifact, keep its language and adapt the clarity principles.
For full conformance, check the official Issue 9 rules, dictionary and applicable technical terms.
Report a missing source or review instead of claiming compliance. See [research and sources](references/sources.md).

## Principles

- **One term, one concept.** Use the project's accepted terms. Define an unfamiliar term at first use.
  A glossary does not make every word STE-approved. The official dictionary restricts meanings and parts of speech.
- **One idea per sentence.** Keep descriptions to 25 words per sentence.
  Keep each paragraph on one topic, with no more than six sentences.
- **One sequential action per step.** Keep procedural sentences to 20 words.
  Give direct instructions in the imperative. Keep simultaneous actions together when separating them would change the operation.
- **Condition before action.** Put a prerequisite before the command that depends on it.
- **Actor and verb.** Prefer active voice and simple present, past or future.
  In descriptions, passive voice is an exception for an unknown actor. Do not invent the actor.
- **Complete, simple sentences.** Keep necessary subjects, articles and connecting words.
  Expand contractions. Use periods instead of semicolons in prose.
- **Clear word relations.** Break ambiguous noun chains into explicit relations.
  The normal limit is three words. Preserve an established longer technical name and explain it where needed.
- **Literal language.** Replace figurative expressions and noun-heavy actions with the actual operation.
  Check an `-ing` form by its function: technical nouns and approved entries can be valid.
- **Visible requirements and risks.** Keep required actions and limits out of informational notes.
  Put a risk notice before the hazardous action and state the consequence. Preserve the project's risk labels.
- **Meaning before brevity.** Preserve negation, quantifiers, exceptions, order, uncertainty, decision status and mandatory modal words.
  Keep code, commands, identifiers, paths, quotations, units and numbers intact. Rewrite the surrounding prose instead.

Use American spelling unless a project directive requires another spelling.
The official word count has exceptions for identifiers, numbers with units, quoted text, parentheses and other elements.
A space-only counter can flag a sentence for review. It cannot establish conformance.

## Replace ambiguity with an observable fact

These original examples illustrate the project profile. They are not dictionary-verified conformance examples.
Example thresholds and decisions do not supply requirements for the current project.

| Instead of | Write | What changed |
| --- | --- | --- |
| After checking the config, restart the service and verify the response. | 1. Check the configuration.<br>2. Restart the service.<br>3. Check the response. | Three sequential actions become three steps. |
| Delete the backup if the restore check passed. | If the restore check passed, delete the backup. | The reader sees the prerequisite first. |
| If a job fails three times, the worker must perform a transition of its state to `failed`. | If a job fails three times, the worker must set the job state to `failed`. | The verb names the required action. |
| The migration has been completed on `abc123`, although the row-count check has not been run. | The migration completed on `abc123`. The row-count check was not run. | The event and verification gap have separate sentences. |
| Our proposed decision is to leverage Redis as the cache, but no performance measurement is available. | Status: Proposed. Redis is an option for the cache. No performance measurement is available. | The proposal and evidence limit remain explicit. |
| If configuration validation fails, make an error notification. | If the configuration is not valid, show the error. | The condition and action replace noun-heavy wording. |

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
State any requested but unverified conformance in the conversational handoff.
Add a compliance label or separate review report only when the project requires one.

**Done when:** the complete artifact preserves the agreed content, follows this profile and has a clear delivery and verification state.
