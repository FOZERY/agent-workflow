---
name: research
description: Conduct an in-depth investigation against primary sources and preserve a sourced research report. Use when the user needs a durable investigation, comparison or evidence review, rather than a quick lookup or routine file reading.
---

Research produces a reusable report. Routine file reading, repository searches and quick web lookups follow the project's read-only exploration policy; they can return findings to the parent agent without creating files.

Read project instructions for the research scope, permitted sources, delegation profile, artifact location and write authority. Reuse settled choices; clarify only gaps that affect this investigation. If no report location is configured, use the folder where the repository already keeps research notes, or `.docs/research/<topic>.md` when there is none. Confirm before the first write and mention once that `setup-agents-workflow` can configure the project.

Use the project's approved research role or harness preset rather than prescribing a model. Delegate bounded questions with fresh context when authorized and supported; use background execution where available. Without a project policy, run independent lines of inquiry as read-only background subagents where the client supports them. If delegation is unavailable or forbidden, investigate in the main agent within its authority. A read-only researcher returns findings and sources to the coordinating agent; an authorized writer saves the report. In OMP (the oh-my-pi coding agent), a `scout` does not receive write duties.

1. Establish the question, relevant scope and what the report needs to resolve. Break the investigation into the necessary lines of inquiry.
2. Investigate against **primary sources**: official documentation, source code, specifications and first-party APIs. Follow material claims back to the source that owns them. Compare relevant alternatives, examine conflicting evidence and pursue gaps that affect the answer. Distinguish verified facts, inference and unresolved questions; state version/date limits where they matter.
3. Synthesize the evidence into one Markdown report containing the question and scope, findings with source links, supported conclusions, limitations and open questions. Record the investigation date and relevant versions. Keep only sections useful to this question; depth comes from evidence, not report length.
4. Save the report at the agreed project location through the authorized writer. Check its references and report the destination and remaining uncertainty. If writing is blocked, return the findings and identify the missing permission or destination; do not claim the artifact was saved or silently create a competing local copy.

**Done when:** the investigation's material questions have sourced answers or explicit evidence gaps, and the report is saved at the agreed location or its blocked delivery is clearly reported.
