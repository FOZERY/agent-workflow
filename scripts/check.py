#!/usr/bin/env python3
"""Check the contracts between the skills of this kit.

Run from the repository root: python3 scripts/check.py
Exit code 1 if any check fails.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
errors = []


def err(msg):
    errors.append(msg)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_code(text):
    """Remove fenced code blocks, so that template text is not checked as links."""
    return re.sub(r"```.*?```", "", text, flags=re.S)


def heading_slugs(text):
    slugs = []
    for h in re.findall(r"^#+\s+(.+)$", strip_code(text), re.M):
        h = re.sub(r"`", "", h.strip().lower())
        slugs.append(re.sub(r"[^\w\- ]", "", h).replace(" ", "-"))
    return slugs


# 1. Frontmatter and invocation flags.
skills = {}
for d in sorted(os.listdir("skills")):
    p = f"skills/{d}/SKILL.md"
    if not os.path.isfile(p):
        continue
    text = read(p)
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{p}: no frontmatter")
        continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    if not name or name.group(1) != d:
        err(f"{p}: name must be '{d}'")
    if not re.search(r"^description:\s*\S", fm, re.M):
        err(f"{p}: no description")
    user_only = re.search(r"^disable-model-invocation:\s*true", fm, re.M) is not None
    skills[d] = {"user_only": user_only, "text": text}
    oy = f"skills/{d}/agents/openai.yaml"
    if os.path.isfile(oy):
        pol = re.search(r"allow_implicit_invocation:\s*(\w+)", read(oy))
        if user_only and (not pol or pol.group(1) != "false"):
            err(f"{oy}: user-only skill needs allow_implicit_invocation: false")
        if not user_only and pol and pol.group(1) == "false":
            err(f"{oy}: agent-started skill has allow_implicit_invocation: false")
    elif user_only:
        err(f"{p}: user-only skill has no agents/openai.yaml")

# 2. Every skill is listed in the docs, with the right starter.
for readme, you in (("README.md", "Human"), ("docs/README.ru.md", "Человек")):
    text = read(readme)
    for s, info in skills.items():
        m = re.search(rf"\[`/?{re.escape(s)}`\]\([^)]*\) \| (\S+) \|", text)
        if not m:
            err(f"{readme}: skill '{s}' is not in the table")
        elif (m.group(1) == you) != info["user_only"]:
            err(f"{readme}: '{s}' starter column does not match disable-model-invocation")
for doc in ("docs/GUIDE.md", "docs/GUIDE.ru.md", "skills/ask-workflow/SKILL.md", "skills/setup-workflow/references/catalog.md"):
    text = read(doc)
    for s in skills:
        if s in ("ask-workflow",) and doc.endswith("ask-workflow/SKILL.md"):
            continue
        if f"`{s}`" not in text and f"`/{s}`" not in text:
            err(f"{doc}: skill '{s}' is not mentioned")
ask = read("skills/ask-workflow/SKILL.md")
for row in re.findall(r"^\|.*\|.*\|$", ask, re.M):
    for s in re.findall(r"`([a-z-]+)`", row.split("|")[-2]):
        if s in skills and skills[s]["user_only"] and "(manual)" not in row:
            err(f"ask-workflow: '{s}' is user-only, mark it (manual)")

# 3. Relative links and anchors.
import subprocess
md_files = ["./" + f for f in subprocess.run(["git", "ls-files", "*.md"], capture_output=True, text=True, check=True).stdout.split()]
for p in md_files:
    text = strip_code(read(p))
    text = re.sub(r"`[^`]*`", "", text)
    for u in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"(https?:|mailto:)", u) or "<" in u:
            continue
        path, _, anchor = u.partition("#")
        target = os.path.normpath(os.path.join(os.path.dirname(p), path)) if path else p
        if not os.path.exists(target):
            if path in ("link",) or "/src/" in path:
                continue
            err(f"{p}: broken link {u}")
        elif anchor and target.endswith(".md") and anchor not in heading_slugs(read(target)):
            err(f"{p}: broken anchor {u}")

# 4. Settings: every key in a template skill section is defined in the core block.
core = read("skills/setup-workflow/references/core-rules.md")
block = re.search(r"<!-- agent-workflow:core v(\d+) -->(.*?)<!-- /agent-workflow:core -->", core, re.S)
if not block:
    err("core-rules.md: no versioned core block")
    defined = set()
else:
    glossary = re.search(r"^## Skill settings\n(.*?)\n## ", core, re.S | re.M)
    if not glossary:
        err("core-rules.md: no '## Skill settings' section")
    defined = set(re.findall(r"^- `([a-z-]+)`(?:, `([a-z-]+)`)?:", glossary.group(1) if glossary else "", re.M))
    defined = {k for pair in defined for k in pair if k}
template = read("skills/setup-workflow/references/AGENTS.md")
outline = re.search(r"## Skills\n(.*?)\n## Git and delivery", template, re.S).group(1)
section_keys = {}
for sec in re.split(r"^### ", outline, flags=re.M)[1:]:
    name, body = sec.split("\n", 1)
    keys = re.findall(r"^([a-z-]+): <", body, re.M)
    section_keys[name.strip()] = set(keys)
    for k in keys:
        if k not in defined:
            err(f"AGENTS.md template: setting '{k}' in '{name.strip()}' is not defined in core-rules.md#skill-settings")
table = re.search(r"## Automation settings.*?\n(\|.*?)\n\n", template, re.S).group(1)
for row in table.splitlines()[2:]:
    cells = [c.strip() for c in row.strip("|").split("|")]
    sec = cells[0].strip("`")
    if sec not in section_keys:
        continue
    listed = set(re.findall(r"`([a-z-]+)`", cells[1]))
    if listed != section_keys[sec]:
        err(f"AGENTS.md template: automation table for '{sec}' lists {sorted(listed)}, section has {sorted(section_keys[sec])}")
for s, keys in section_keys.items():
    if s not in skills:
        err(f"AGENTS.md template: section '{s}' has no skill")

# 5. Step references: "step N of `skill`" and "WORKER.md step N" point to real steps.
def steps(text):
    return set(re.findall(r"^## (\d+)\.", text, re.M))

worker = read("skills/implement/WORKER.md")
for p in md_files:
    if not p.startswith("./skills/"):
        continue
    text = read(p)
    for n, s in re.findall(r"step (\d+) of `([a-z-]+)`", text):
        if s in skills and n not in steps(skills[s]["text"]):
            err(f"{p}: 'step {n} of `{s}`' does not exist")
    for n in re.findall(r"\[WORKER\.md\]\(WORKER\.md\) step (\d+)", text):
        if n not in steps(worker):
            err(f"{p}: 'WORKER.md step {n}' does not exist")

if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} problems")
    sys.exit(1)
print(f"OK: {len(skills)} skills, {len(md_files)} Markdown files")
