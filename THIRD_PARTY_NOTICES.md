# Third-party notices

Original contributions to this repository are covered by [LICENSE](LICENSE). The following notices apply to retained third-party material, including local adaptations.

## Scope and attribution

| Copyright holder | Covered material and source |
| --- | --- |
| Matt Pocock | Adapted setup; `grilling`, `grill-with-docs`, `research`, `wayfinder`, `to-spec`, `to-tickets`, `implement` (its worker mode adapted from `implement-spec`), `tdd`, `code-review`, `retro`, `writing-for-agents`, `domain-modeling`, `prototype` and `refactor-codebase` (adapted from `improve-codebase-architecture`, with the vocabulary and references of `codebase-design`), with their retained supporting files. [Setup license](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/LICENSE); [import baseline license](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/LICENSE). |
| Kirill Sachkov | Retained project-aware setup/adaptation material and the `writing-for-people` package (originally `plain-writing`), including its Russian reference. [Adaptation license](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/LICENSE); [communication license](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/provenance/communication-LICENSE). |
| Lauren Tan | `investigate`, adapted from the `why`, `how` and `teach` skills, `rephrase`, adapted from `bro`, `recall`, adapted from `recall`, the evidence rules in `verify`, adapted from `create-verification-skill`, the fit, bug-fix and evidence rules in `tdd`, adapted from `tdd` and `principle-test-behavior-not-implementation`, the evidence and root-cause rules in `implement/WORKER.md`, from the pstack principles, and the multi-session review in `retro`, from `reflect`; all from pstack in [cursor/plugins](https://github.com/cursor/plugins/tree/main/harness/pstack), licensed under MIT. |
| Anthropic | `simplify-codebase`, written from the approach of the `code-simplifier` agent in [claude-plugins-official](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier), licensed under Apache 2.0. The full [license text](skills/simplify-codebase/LICENSE) ships with the skill. |
| HumanLayer | Historical attribution for PR-format visual examples previously distributed in this kit, credited to Dex Horthy's `show-me` via Matt's PR skill. [HumanLayer license](https://github.com/humanlayer/skills/blob/bba9d13ab34f0a87f1cc33df4dd196372393ddfc/LICENSE). |

The `simplify-codebase` skill also draws on MIT-licensed projects. The simplification signals in `simplify-codebase` are adapted from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/main/skills/code-simplification) (`code-simplification`, Copyright (c) 2025 Addy Osmani). The `tdd` skill adapts `audit-tests` from [dzhng/skills](https://github.com/dzhng/skills/tree/main/skills/review/audit-tests) (Copyright (c) 2026 David Zhang) in `audit.md` and in its anti-patterns. The other sources contribute ideas only, and no text is copied: [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) (`test-driven-development`: name the break before the test, change detectors), Kent Beck's test list, Kent C. Dodds' "mostly integration" and Martin Fowler's sociable tests (the test levels in `tdd`), [dzhng/skills](https://github.com/dzhng/skills/tree/main/skills/review/find-overengineering) (`find-overengineering`: roll back protective code, keep checks on input we do not control), [Smirnov-Labs/claude-skills](https://github.com/Smirnov-Labs/claude-skills/tree/main/skills/detect-overengineering) (a catalog of patterns with paired examples) and [TNTcraftHIM/Piik](https://github.com/TNTcraftHIM/Piik/tree/main/.agents/skills/ponytail) (`ponytail`: fix the boundary, not each symptom).

The HumanLayer revision above is a verified license/source reference, not the proven revision copied by Matt; that copied revision is not stated in the available provenance. This kit is an independent adaptation and does not imply endorsement by the upstream authors.

## ASD-STE100 source references

The `writing-technical` package contains original instructions and software examples informed by the [official ASD-STE100 site](https://www.asd-ste100.org/).
ASD owns the standard and its registered trademark. This repository does not bundle the official PDF or dictionary.
The MIT terms for this repository do not license the standard itself.
This skill is not endorsed, certified or approved by ASD or the STEMG.

## Excalidraw diagrams and component libraries

The `draw-diagram` package retains generation guidance and renderer files from [coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill/tree/8646fcc9f74f38539c6cdb4c969723336a96ddcd).
The pinned revision has no declared license. These files are not covered by this repository's MIT grant.
Obtain redistribution permission from the rights holder before publishing them or a distribution that includes them.
The [package notice](skills/draw-diagram/NOTICE.md) identifies the imported files and the separately licensed original integration material.

Four owner-supplied component collections byte-match [Excalidraw Libraries](https://github.com/excalidraw/excalidraw-libraries/tree/297a349eaff859e678f78d4dbc8e68df5fce42e5):
Sticky Notes by ferminrp, Software Logos by drwnio.polyrand.net, System Design Components by Rohan Pithadiya, and Software Architecture by Youri Tjang.
Their [source map](skills/draw-diagram/references/libraries.md#provenance) and [Excalidraw MIT notice](skills/draw-diagram/assets/libraries/LICENSE) ship with the package.
Keep those credits and terms with the files. Software logos remain subject to their owners' trademark rights.


## MIT notices and terms

The Matt Pocock, Kirill Sachkov, Lauren Tan, HumanLayer, Addy Osmani and David Zhang notices use the shared MIT terms below. The Anthropic notice uses the Apache 2.0 text in `skills/simplify-codebase/LICENSE`. Other material retains the separate terms identified above.

```text
MIT License

Copyright (c) 2026 Matt Pocock
Copyright (c) 2026 Kirill Sachkov
Copyright (c) 2026 Lauren Tan
Copyright (c) 2026 HumanLayer
Copyright (c) 2025 Addy Osmani
Copyright (c) 2026 David Zhang

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
