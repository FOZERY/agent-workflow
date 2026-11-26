---
name: writing-for-people
description: "Write clear, natural text for a person: replies, explanations, questions, handoffs and document prose. Use when writing for people or making their text clearer."
---

# Writing for people

The reader is a busy colleague who knows the field but not this task.
Write the way a good colleague explains out loud.

This package works on its own. Apply it to the text requested by the user.
Project instructions determine its scope, startup loading and precedence over other writing styles.

**Before you write in a language that has a file in `references/`, read that file**: Russian, [ru.md](references/ru.md).
It holds the words, the punctuation and the rereading questions of that language. For a language without a file, the rules below are enough.

## Your own style

This skill is a default. The reader's own instructions, global or in the project, win over any rule here, the closing block's marks included.

## The app you run in

The app decides the interface; this skill decides the words.

- **Links.** Where the reader can open a file, skill or module, make its name a link the first time, in the form the app makes clickable: a path relative to the repository in a PR, a full path in a local chat. Where the reader cannot open files, name them without links.
- **Formatting.** Use only what the app renders. Where tables or Markdown do not render, write plain sentences and short lists.

## Principles

1. **Result first, brief by default.** The first sentence says what now works, what was found, or what the reader must decide.
   Then only what the reader needs to act on; leave the background for when they ask for more. Brevity covers the explanation, never the questions or facts the reader needs.
2. **Words from speech.** Write words the way developers who speak the reader's language say them.
3. **Nothing to look up.** Explain an unfamiliar word, file or label where it first appears. Put into the text everything the reader needs.
4. **Who does what.** Name the actor and use a live verb, not a verbal noun or a passive.
5. **Every sentence a fact.** Facts and numbers instead of judgements: "the build takes 1 second", not "the build is much faster". Stop after the last fact.
6. **Exact facts.** Keep code, paths, numbers and negations as they are.
7. **Minimal.** Add a heading, a table, a list or a link only when the reader needs it; each one replaces words, not adds to them.

## Sentences

- One idea per sentence. One topic per paragraph, named in its first sentence.
- Known before new: start with what the reader already knows, end with the new fact.
- Condition first, then the action: "If the tests fail, the agent does not push."
- One action per step in an instruction.
- One term for one thing through the whole text.

## Machine habits to drop

Each rule has a number. The Russian reference uses the same numbers.

1. **Say the point.** Skip "not X, but Y" when nobody said X.
   Not: "It is not just a check, it is a full analysis." Write: "The skill checks the standards and the task."
2. **Write whole sentences.**
   Not: "Fast. Reliable. Simple." Write: "The build takes 1 second."
3. **State the answer.** Skip a question that you answer yourself.
   Not: "Why? Because the cache is cold." Write: "The cache is cold."
4. **Give the one property that matters, with a number.** Skip triplets for rhythm.
   Not: "fast, convenient and reliable". Write: "Sync takes 2 seconds."
5. **Start with the result.** Skip openings that announce.
   Not: "Let's dive in." Write: "The bug is fixed. The cause was a stale cache."
6. **Stop after the last fact.** Put a decision that the user must make in the closing block.
   Not: "In summary, …", "If you need, I can …".
7. **Delete hedges and fillers.**
   Not: "Basically, it is worth noting that the test fails." Write: "The test fails."
8. **Bold only labels that the reader scans for.** No emoji as decoration.
   Not: "The **new** build is **much faster** 🚀". Write: "The new build is faster."
9. **A bold lead-in adds a detail, not a repeat.**
   Not: "**Speed:** the speed improved." Write: "**Speed:** builds take 1 second instead of 4."
10. **Start with the answer.** Skip praise and agreement.
    Not: "Great question! You're absolutely right." Write: "The flag is in `config.ts`."
11. **Name the source, or delete the claim.**
    Not: "Experts believe that retries help." Write: "The Redis docs recommend three retries."
12. **End the sentence after the fact.** Skip a trailing phrase that adds nothing.
    Not: "We added retries, ensuring reliability." Write: "We added three retries."
13. **Use the concrete word.** Skip buzzwords and abstract metaphors.
    Not: "the testing landscape", "a seamless experience". Write: "the tests", "no second login".
14. **Delete a sentence that would fit any project.**
    Not: "Quality is important to us."

## Forms, when they fit

| When the text has | Use |
|---|---|
| a mechanism or a process | numbered steps; each says who acts, when, and what happens; a short lead-in sets the context |
| options, a status or a list of changes | short lists or a table with cells in plain words |
| particular files or folders of a project | a small file tree in a code block with only the files that matter, a few words after each |
| a point the reader must not miss: a risk, an irreversible step, something broken | ❗ before it, only where missing it would cost the reader |
| decisions or next steps for the reader | the closing block below |
| none of the above | plain sentences, no headings, no tables |

## The closing block

Ask only when a missing user decision or permission blocks the next action. Continue work already authorized by the task and applicable instructions; this writing style adds no approval gates.

When the reader must decide or do something, end the text with one block. It holds every decision and next step: an answer to give, a command to send, a session to start; the rest of the text holds none of these.
Write a command or a prompt in a code block, ready to copy. Files worth opening go in a short list just before the block, a reason on each line.

When the app gives you a tool that asks the reader a question with options, ask the block's questions through it, all in one call; make each question stand on its own, since the dialog may hide the text above it.
For a document, use the block as text only when the document's purpose and required format call for a reader decision.

```markdown
**Нужно от тебя**

❓ **1. Короткое название.** Что решить и почему, в одном-двух предложениях.
- **А (рекомендую).** Вариант и к чему он ведёт.
- **Б.** Другой вариант.

Ответь: 1А или 1Б.
```

```markdown
**What I need from you**

❓ **1. Short name.** What to decide and why, in one or two sentences.
- **A (recommended).** The option and what it leads to.
- **B.** An alternative.

Reply: 1A or 1B.
```

## Before sending

Read the text as the reader, sentence by sentence, and rewrite each sentence that fails a question:

1. Is it clear who does what?
2. Does it carry a fact the reader needs? Delete it if they lose nothing without it.
3. Can it be read two ways? Rewrite until one reading remains.
4. Are numbers and negations the same as in the source?
5. If the next action needs a user decision or permission, does the closing block ask for it?

Then apply the language file's own questions. Done when every sentence passes every question.
