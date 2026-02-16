---
id: 20260216152320-workspace-cli-composition-boundary-3e6096d6
title: Workspace CLI composition boundary
tags:
- cli
- workspace
visibility: shared
status: active
created_at: "2026-02-16T15:23:20Z"
updated_at: "2026-02-16T15:23:39Z"
---

Established a clearer [[20260216083521-workspace-boundaries-8c6a6cb1|workspace boundaries]] pattern: keep workspace/cli.py as a thin entrypoint (global flags + error handling), move repo-mode parser wiring to workspace/cli_repo.py, and harness-mode wiring to workspace/cli_harness.py. This preserves UX while reducing cross-responsibility coupling and makes future mode-specific refactors safer.
