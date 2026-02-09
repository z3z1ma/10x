---
"id": "al-29bf"
"status": "closed"
"deps": []
"links": []
"created": "2026-02-09T19:29:22Z"
"type": "feature"
"priority": 2
"assignee": "z3z1ma"
"tags": []
"external": {}
---
# Add pack --diff to show drifted file diffs

Expose a CLI flag on loom pack status that prints unified diffs for drifted files. The pack module already has a diff implementation; wire it into the command surface so users can inspect drift without manually opening files.

## Acceptance Criteria

- loom pack status gains a --diff flag
- When drift exists, prints a stable unified diff per drifted file
- Does not print diffs when there is no drift (or prints a clear message)
- Exit code remains consistent with existing drift behavior
- Covered by CLI UX test(s)

## Notes

**2026-02-09T19:35:01Z**

Implemented loom pack status --diff to print unified diffs for drifted managed files via agent_loom.pack.diff.diff_pack_file (truncated at 400 lines). Non-JSON output now prints a hint when drift exists; JSON output supports --json --diff via a diffs field. Added CLI UX regression tests.
