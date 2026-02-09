---
"id": "al-cf19"
"status": "review"
"deps": []
"links": []
"created": "2026-02-09T06:30:25Z"
"type": "task"
"priority": 2
"assignee": "z3z1ma"
"tags":
- "memory"
- "ux"
"external": {}
---
# Add memory grep + link suggest

Add loom memory grep (regex search, no ranking) and loom memory link suggest <id> (non-mutating related-note suggestions). Ensure .loom/ticket and .loom/memory are gitignored by default and loom memory init does not mutate repo-root .gitignore.

## Notes

**2026-02-09T06:30:31Z**

Implemented: memory grep subcommand with filters; link suggest subcommand; init_vault now writes vault-local .gitignore only (no repo-root mutation). Updated repo .gitignore to ignore .loom/ticket/ and .loom/memory/ fully. Gates: ruff pass, basedpyright pass, pytest 198 passed.
