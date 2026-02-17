---
id: 20260217010742-large-parser-surfaces-should-collapse-to-stable-shims-76a976cf
title: Large parser surfaces should collapse to stable shims
visibility: shared
status: active
created_at: "2026-02-17T01:07:42Z"
updated_at: "2026-02-17T01:07:42Z"
---

In [[20260216165029-loom-workspace-0994ef7a|Loom Workspace]], very large CLI parser files should be decomposed into domain builder modules, with the public parser module kept as a stable shim exporting the entrypoint. This keeps command UX stable while improving [[20260217010742-modular-parser-architecture-322fd202|modular parser architecture]] and limiting hotspot regrowth.

Related: [[[[20260217010742-parser-decomposition-d675a7e6|parser decomposition]]]] [[[[20260217010742-workspace-harness-06782006|workspace harness]]]] [[[[20260217010742-maintainability-2e0fe4c5|maintainability]]]]
