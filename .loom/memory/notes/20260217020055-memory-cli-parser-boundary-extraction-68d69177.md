---
id: 20260217020055-memory-cli-parser-boundary-extraction-68d69177
title: Memory CLI parser boundary extraction
tags:
- architecture
- memory
visibility: shared
status: active
created_at: "2026-02-17T02:00:55Z"
updated_at: "2026-02-17T02:00:55Z"
---

Established a cleaner module boundary for [[20260217015632-memory-cli-52a58d8c|memory-cli]] by extracting all parser and argv normalization concerns into a dedicated parser module. Runtime command execution now imports parser helpers instead of mixing parser construction, argument normalization, and command dispatch in one file. This boundary keeps behavior stable while making future command-group extraction lower risk. Related concepts: [[20260217020055-parser-hotspots-9afdcc53|parser-hotspots]], [[20260217015632-shim-boundaries-7b53ab6a|shim-boundaries]], [[20260216233522-behavior-stable-refactor-ff3ee4c3|behavior-stable-refactor]].
