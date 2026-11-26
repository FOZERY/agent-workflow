# Component libraries

Read in the diagram worker after receiving an approved assignment. Load only the collections and items needed for that diagram.
All four files use Excalidraw library format version 1: `library` is an array of item arrays, each containing scene elements.
They are not scene files and cannot be passed directly to the PNG renderer.

| Collection | Use | Items | File |
| --- | --- | --- | --- |
| Sticky Notes | Group questions, proposals or alternatives in a discussion | 13 | [post-it.excalidrawlib](../assets/libraries/post-it.excalidrawlib) |
| Software Logos | Recognizable software and infrastructure symbols | 18 | [drwnio.excalidrawlib](../assets/libraries/drwnio.excalidrawlib) |
| System Design Components | System-level components and interactions | 24 | [system-design.excalidrawlib](../assets/libraries/system-design.excalidrawlib) |
| Software Architecture | Services, storage, messaging and clients | 7 | [software-architecture.excalidrawlib](../assets/libraries/software-architecture.excalidrawlib) |

## Use selected items

Inspect item types and labels programmatically before loading detailed coordinates. An item can contain several grouped elements; preserve the complete item.
Choose symbols that explain a role. A logo does not establish which technology the design uses; take that fact from the brief.
Use plain shapes when no library item fits. Do not fetch another collection unless it is authorized.

Copy selected items into the scene's `elements` array. Assign fresh element and group IDs to every inserted instance.
Remap internal text/container, frame, arrow and bound-element references, including legacy `boundElementIds` where present.
Preserve references within the copied item; remove references to elements that were not copied. Repeated instances must not bind to one another accidentally.
Translate each item's elements together. Preserve line/arrow points relative to their element origin.
Carry required image data into the scene's `files` map if an item uses images. Report absent image data instead of inserting a broken symbol.

Keep the source libraries unchanged. Validate unique IDs and resolvable bindings, then use the generation skill's render-and-view check.
Render the diagram, not every collection, and return only the requested preview to the coordinator.

## Provenance

The supplied files byte-match the [Excalidraw Libraries repository at `297a349eaff859e678f78d4dbc8e68df5fce42e5`](https://github.com/excalidraw/excalidraw-libraries/tree/297a349eaff859e678f78d4dbc8e68df5fce42e5).

| Local file | Author credited by the catalog | Upstream path |
| --- | --- | --- |
| `post-it.excalidrawlib` | ferminrp | `libraries/ferminrp/post-it.excalidrawlib` |
| `drwnio.excalidrawlib` | drwnio.polyrand.net | `libraries/drwnio/drwnio.excalidrawlib` |
| `system-design.excalidrawlib` | Rohan Pithadiya | `libraries/rohanp/system-design.excalidrawlib` |
| `software-architecture.excalidrawlib` | Youri Tjang | `libraries/youritjang/software-architecture.excalidrawlib` |

Keep their [MIT notice](../assets/libraries/LICENSE) and these credits with the assets. Logos do not imply endorsement or grant trademark rights.
