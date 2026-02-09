---
"id": "al-c09c"
"status": "open"
"deps": []
"links": []
"created": "2026-02-09T19:29:11Z"
"type": "feature"
"priority": 2
"assignee": "z3z1ma"
"tags": []
"external": {}
---
# Add pack --diff to show drifted file diffs

Expose a CLI flag on  that prints unified diffs for drifted files. The pack module already has a diff implementation; wire it into the command surface so users can inspect drift without manually opening files.

## Acceptance Criteria

-  (or equivalent) gains a  flag\n- When drift exists, prints a stable unified diff per drifted file\n- Does not print diffs when there is no drift (or prints a clear message)\n- Exit code remains consistent with existing drift behavior\n- Covered by CLI UX test(s)
