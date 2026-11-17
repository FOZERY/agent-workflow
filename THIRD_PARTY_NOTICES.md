# Third-party notices

Original contributions to this repository are covered by [LICENSE](LICENSE). The following notices apply to retained third-party material, including local adaptations.

## Scope and attribution

| Copyright holder | Covered material and source |
| --- | --- |
| Matt Pocock | Adapted setup; `grilling`, `grill-with-docs`, `research`, `wayfinder`, `to-spec`, `to-tickets`, `implement`, `implement-spec`, `tdd`, `code-review`, `retro`, `writing-for-agents`, `domain-modeling`, `prototype` and `codebase-design`, with their retained supporting files. [Setup license](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/LICENSE); [import baseline license](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/LICENSE). |
| Kirill Sachkov | Retained project-aware setup/adaptation material and the `human-text` package (originally `plain-writing`), including its Russian reference. [Adaptation license](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/LICENSE); [communication license](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/provenance/communication-LICENSE). |
| HumanLayer | Historical attribution for PR-format visual examples previously distributed in this kit, credited to Dex Horthy's `show-me` via Matt's PR skill. [HumanLayer license](https://github.com/humanlayer/skills/blob/bba9d13ab34f0a87f1cc33df4dd196372393ddfc/LICENSE). |

The HumanLayer revision above is a verified license/source reference, not the proven revision copied by Matt; that copied revision is not stated in the available provenance. This kit is an independent adaptation and does not imply endorsement by the upstream authors.

## ASD-STE100 source references

The `asd-ste100` package contains original instructions and software examples informed by [official ASD-STE100 sources](skills/asd-ste100/references/sources.md).
ASD owns the standard and its registered trademark. This repository does not bundle the official PDF or dictionary.
The MIT terms for this repository do not license the standard itself.
This skill is not endorsed, certified or approved by ASD or the STEMG.

## Excalidraw diagrams and component libraries

The `excalidraw-diagram` package retains generation guidance and renderer files from [coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill/tree/8646fcc9f74f38539c6cdb4c969723336a96ddcd).
The pinned revision has no declared license. These files are not covered by this repository's MIT grant.
Obtain redistribution permission from the rights holder before publishing them or a distribution that includes them.
The [package notice](skills/excalidraw-diagram/NOTICE.md) identifies the imported files and the separately licensed original integration material.

Four owner-supplied component collections byte-match [Excalidraw Libraries](https://github.com/excalidraw/excalidraw-libraries/tree/297a349eaff859e678f78d4dbc8e68df5fce42e5):
Sticky Notes by ferminrp, Software Logos by drwnio.polyrand.net, System Design Components by Rohan Pithadiya, and Software Architecture by Youri Tjang.
Their [source map](skills/excalidraw-diagram/references/libraries.md#provenance) and [Excalidraw MIT notice](skills/excalidraw-diagram/assets/libraries/LICENSE) ship with the package.
Keep those credits and terms with the files. Software logos remain subject to their owners' trademark rights.


## MIT notices and terms

The Matt Pocock, Kirill Sachkov and HumanLayer notices use the shared MIT terms below. Other material retains the separate terms identified above.

```text
MIT License

Copyright (c) 2026 Matt Pocock
Copyright (c) 2026 Kirill Sachkov
Copyright (c) 2026 HumanLayer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Distribution

Keep `LICENSE` and this document with every distribution of the repository. When you export or install single skills, include the applicable copyright notices, full license terms and inherited credits with the copied files. One shared notice can cover several packages when its scope is clear, but it must actually ship with them.

Packages with bundled license notices must retain them. For Matt Pocock's imported packages without a package-local notice, include this notice alongside their installs and exports to preserve Matt's MIT terms. Root legal files remain required for whole-repository distribution.

Including notices does not grant missing permissions. The unlicensed Excalidraw generation material requires a separate rights decision before redistribution.
