---
"id": "al-a1ba"
"status": "open"
"deps": []
"links": []
"created": "2026-02-17T06:24:20Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"tags":
- "sprint:Pack-Module-Improvements"
- "fanout"
"external": {}
---
# Sprint prep: Pack Module Improvements

## Sprint Brief

### Objective restatement
Improve the pack module so pack operations are safer, more deterministic under edge cases, and easier for operators to trust.

### Sprint focus (2-5 words)
Pack Safety + Contracts

### Why this sprint focus is the best next step
Pack is now central to distributing agent assets, but its highest-risk failure modes are boundary issues (unsafe manifest/path input, lockfile ambiguity, and drift UX inconsistency). Hardening these contracts now gives us better reliability before adding new pack features.

### Current state
- Existing tickets that matter:
  - `al-a1ba` (this sprint prep parent)
  - `al-c09c` (existing open pack diff UX ticket; now pulled into this sprint)
- Codebase state that matters:
  - `git status --short` currently shows ticket metadata changes and this sprint prep ticket artifact (`.loom/ticket/*`).
  - Recent pack history includes `a6f5fe5 feat: first class pack diff cmd`, indicating drift diff behavior landed but needs completion/hardening.
  - Key pack modules:
    - `src/agent_loom/pack/core.py` (install/update/uninstall semantics)
    - `src/agent_loom/pack/lock.py` (lockfile parsing/persistence)
    - `src/agent_loom/pack/packs.py` (manifest loading + pack file discovery)
    - `src/agent_loom/pack/cli.py` (operator UX + JSON/text output contracts)
    - `tests/test_pack_*.py` (lifecycle and CLI regression coverage)

### Risks + unknowns (and how we’ll resolve them)
- **Ambiguity: strict vs permissive validation policy.**
  - Option A (strict fail-fast): safer, but may break messy repos/manifests immediately.
  - Option B (auto-repair/warn): smoother UX, but risks hiding invalid state.
  - **Plan:** adopt strict validation for unsafe/ambiguous states; allow deterministic normalization only where risk-free.
- **Ambiguity: lockfile corruption handling behavior.**
  - Option A: hard fail always (safe, less ergonomic).
  - Option B: deterministic repair where unambiguous + explicit warnings.
  - **Plan:** hybrid policy in ticket `al-d94d`.
- **Diff UX edge cases (binary/non-text/large files).**
  - **Plan:** preserve truncation and explicit “diff unavailable” messaging; add UX tests.

## Ticket Set

Created/updated ticket IDs:
- `al-4f2d` — Pack manifest contract hardening (path safety + root invariants)
- `al-d94d` — Pack lockfile resilience: strict validation + deterministic repair path
- `al-c09c` — Pack CLI drift diff contract completion (existing ticket updated; parent/tag/body hardened)
- `al-23a3` — Pack built-in coverage expansion + operator docs refresh

Dependencies encoded:
- `al-c09c` depends on `al-d94d`
- `al-23a3` depends on `al-4f2d`
- `al-23a3` depends on `al-d94d`
- `al-23a3` depends on `al-c09c`

Suggested ordering + what can run in parallel:
- **Wave 1 (parallel):**
  - `al-4f2d`
  - `al-d94d`
- **Wave 2 (after lockfile hardening):**
  - `al-c09c`
- **Wave 3 (fan-in stabilization/docs):**
  - `al-23a3`

Created/updated ticket IDs: [`al-4f2d`, `al-d94d`, `al-c09c`, `al-23a3`]
