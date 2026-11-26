# Excalidraw diagram workflow

This package offers optional design diagrams and delegates approved generation to a separate subagent.
It includes a renderer and four component libraries. It can install independently of `agent-workflow`.

The coordinator reads `SKILL.md`. Only the assigned worker reads the generation reference, selected component data and render output.
Project instructions select the sources, output directory, delegation tool and permitted operations.
An Orca Excalidraw plugin is useful for editing the result, but is not a rendering dependency.

## Renderer setup

Requirements: Python 3.11 or later, `uv`, Playwright and its Chromium installation.
From this installed package's `references/` directory, with permission to install dependencies:

```bash
uv sync
uv run playwright install chromium
```

Render with absolute input and output paths:

```bash
uv run python render_excalidraw.py /absolute/path/design.excalidraw --output /absolute/path/design.png
```

The renderer loads Excalidraw JavaScript from `esm.sh` in headless Chromium. It is not an offline renderer.
Follow applicable browser and network rules. Do not pass private diagrams to external code without the required permission.
A missing dependency or forbidden render leaves the diagram unverified; it does not authorize installation or an alternative service.

## Components

Use [the library index](references/libraries.md) to choose components without loading every JSON file.
The four `.excalidrawlib` files remain unchanged and can also be imported into Excalidraw's library panel.
Their presence on disk does not automatically register them in Orca or any editor profile.

## Source and distribution

Read [NOTICE.md](NOTICE.md) before redistribution. The imported generation prompt and renderer have no declared upstream license at the pinned revision.
The component collections have their own bundled MIT notice. This repository's MIT license does not grant rights to the unlicensed upstream material.
