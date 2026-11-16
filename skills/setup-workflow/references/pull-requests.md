# Project PR/MR procedure interview

Read this when configuring or revising PR/MR preparation, creation or updates. Establish the project's format, delivery checkpoints, targets and permissions. Setup records this procedure; it does not publish a PR/MR.

Project rules determine whether the agent prepares content or carries out authorized publication; configuration does not grant Git or external-write permissions.

## Explore before asking

Inspect applicable contribution guides, PR/MR templates, naming conventions, ownership/reviewer rules, hook configurations and CI requirements. Show what already exists and ask about missing decisions. Inspecting a hook does not authorize executing it or installing tooling.

## Interview topics

### Template and location

Ask: "Which existing PR/MR template should I use? Does the choice depend on repository, subsystem or change type? Where is the authoritative source, and what should I do when no template fits?"

Reuse the project source rather than maintaining a second template in agent instructions. If none exists, offer the upstream Summary/Evidence/Merge Danger format for agreement. A short inline format can suffice; a separate template file is not mandatory. Creating or editing a shared platform template is a separate proposed file change, not an implicit consequence of configuring its consumer.

### Title, description and language

Ask: "What title rules, task identifiers and required description sections apply? What language should I use? Which task references are plain links, and are closing keywords permitted?"

Capture required prefixes, naming rules and fields without inventing product facts. PR/MR titles and commit messages have separate conventions; do not derive one automatically from the other. Use the project's domain vocabulary and preserve mandatory template sections. A task-closing keyword may cause a later tracker transition; use it only under project policy, not because every linked task should close.

### Evidence and project checks

Ask: "What evidence should the description contain? Which hooks or checks must run before a PR is prepared or published, which run afterward in CI, and where are those requirements defined? How should failed, unavailable or pending checks appear in the description?"

Link to the existing quality/delivery rules and their gate order; ask there for any missing decisions. Record real results and their scope, not fabricated before/after evidence. Establish which hooks run through Git operations and which checks need a separate command. Content-only preparation does not imply those effects. A failed hook does not authorize bypassing it. Define whether a draft may be published with pending checks and how post-publication CI is followed.

### Assignees, reviewers and labels

Ask: "Who should be assigned, who should review, and which labels or tags belong on this kind of PR? Are they selected by subsystem, existing ownership rules, automation or manually? May I only recommend them, or also apply them when publication is separately authorized?"

Distinguish the authenticated author, responsible assignee and requested reviewers. Reuse CODEOWNERS and automatic assignment where applicable. Establish the rule for multiple affected subsystems or unclear ownership. Do not invent people or labels, create missing labels, or override automation without authority.

### Targets, publication and handoff

Ask: "When should PR/MR preparation start: on request, after acceptance, or earlier as a draft? Who may commit, push, create or update the request and apply metadata? Which actions require approval each time, and what should I hand over when publication is human-owned?"

Resolve source repository/remote/branch separately from destination repository/base branch, including forks and release targets. Record how the agent selects them and when confirmation is required. Establish the supported CLI, API, MCP or automation, existing-PR lookup/update rules and draft-to-ready checkpoint. Inspect available configuration before asking; leave task-specific branches to be resolved at execution time.

A ready task is not publication permission. Record the permitted route and approval boundaries in the instruction owner. Keep merge, deployment, history rewriting and branch cleanup separately authorized. Check the selected skill's invocation mode before promising a manual-only or automatic route.

## Capture the result

Reference the authoritative format and metadata rules from the existing contribution or delivery documentation. If a separate policy document is needed, propose `.docs/agents/pull-requests.md` and agree its location and Git visibility through setup. Define ownership if a new template is approved; avoid independent copies of the same format.

The canonical instruction owner must require reading the project PR/MR procedure before preparing content, pushing for delivery or creating/updating a request. Keep publication permission limits visible there; point to quality/delivery rules for checks and hooks instead of duplicating their procedure.

Check the selected PR skill for incompatible formats or unconditional actions. Explain any required adaptation rather than claiming a pointer alone changes its prompt. Preserve useful evidence and risk information in the shape the project requires.

**Done when:** the format source, title/body requirements, evidence, metadata, trigger, targets, gates and publication permissions are agreed or have an explicit escalation path. The agent can distinguish content-only handoff, blocked delivery and authorized publication.
