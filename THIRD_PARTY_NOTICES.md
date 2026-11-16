# Third-party notices

Original contributions to this repository are covered by [LICENSE](LICENSE). The following notices apply to retained third-party material, including local adaptations. Source revisions and modification history are maintained separately in [docs/UPSTREAM.md](docs/UPSTREAM.md).

## Scope and attribution

| Copyright holder | Covered material and source |
| --- | --- |
| Matt Pocock | Adapted setup; `grilling`, `grill-with-docs`, `research`, `wayfinder`, `to-spec`, `to-tickets`, `implement`, `implement-spec`, `tdd`, `code-review`, `retro` and `writing-for-agents`, with their retained supporting files. [Setup license](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/LICENSE); [import baseline license](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/LICENSE). |
| Kirill Sachkov | Retained project-aware setup/adaptation material and the `human-text` package (originally `plain-writing`), including its Russian reference. [Adaptation license](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/LICENSE); [communication license](https://github.com/KirillSachkov/agent-kit/blob/3b5e37249118aff3d3dfb547977939145524d525/provenance/communication-LICENSE). |
| HumanLayer | Historical attribution for PR-format visual examples previously distributed in this kit, credited to Dex Horthy's `show-me` via Matt's PR skill. [HumanLayer license](https://github.com/humanlayer/skills/blob/bba9d13ab34f0a87f1cc33df4dd196372393ddfc/LICENSE). |

The HumanLayer revision above is a verified license/source reference, not the proven revision copied by Matt; that copied revision is not stated in the available provenance. This kit is an independent adaptation and does not imply endorsement by the upstream authors.

## MIT notices and terms

The applicable notices are combined below with the full shared MIT terms. Each notice applies to the material identified above.

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

The skill installer does not copy the root license files into packages, so copy them to the installation or export destination yourself. A `SKILL.md` copied without its references and notices is not a complete distribution. This source tree does not need license files inside each package.
