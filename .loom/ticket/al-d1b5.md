---
"id": "al-d1b5"
"status": "review"
"deps": []
"links": []
"created": "2026-02-07T16:03:28Z"
"type": "task"
"priority": 2
"assignee": "z3z1ma"
"parent": "al-1f81"
"tags":
- "workspace"
- "leases"
- "ux"
- "docs"
"external": {}
---
# Workspace: clarify harness leases

## Notes

**2026-02-07T16:03:33Z**

Add repo-mode leases and worktree GC so orchestrators (Team) can claim/skip worktrees during automated cleanup. Clarify leases as coordination locks (not a limitation on parallel branches).

**2026-02-07T16:09:25Z**

Direction change: leases remain harness-only. This ticket is about clarifying semantics + tightening the story, not tying leases to tickets or duplicating ticket claims.
