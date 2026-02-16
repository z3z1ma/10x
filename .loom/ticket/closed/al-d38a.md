---
"id": "al-d38a"
"status": "closed"
"deps": []
"links": []
"created": "2026-02-15T23:22:28Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"tags":
- "sprint:YAML-Sprint-Foundations"
- "fanout"
"external": {}
---
# Sprint prep: YAML Sprint Foundations

Objective:
Improve code architecture, modularity, and organization by adding first-class sprint support in `ticket` and declarative YAML team composition in `team` (broadcasting, worktree mapping, always-on vs ephemeral members, communication and escalation boundaries, and BYO agent support with Loom-enforced operating instructions).

## Sprint Brief

### Objective restatement
Build a minimal-correct foundation where teams can be defined declaratively in YAML and executed reliably by Team runtime, while Ticket evolves from env-driven sprint tagging to explicit sprint-aware workflows.

### Sprint focus (2-5 words)
Declarative Team Composition

### Why this sprint focus is the best next step
The highest leverage is to establish a strict, testable YAML contract and integrate it into run, spawn, and send paths before adding UX sugar. Without that contract, broadcast semantics, escalation boundaries, worktree routing, and BYO agent wrapping will fragment across ad hoc flags and `core.py` branches. In parallel, ticket sprint context must become explicit so sprint behavior is not dependent on transient environment variables.

### Current state
- Existing tickets that matter:
  - `al-d38a` (this sprint prep ticket) was the only sprint-tagged ticket before this prep pass.
  - `al-c09c` is open but unrelated to this sprint objective.
- Codebase state that matters:
  - `git status`: clean.
  - `git log -n 20 --oneline`: recent work already introduced sprint metadata and prep-sprint flow.
  - `src/agent_loom/team/core.py` (about 6300 LOC) already persists sprint metadata and handles run/spawn/send, but has no YAML team-composition loader and no broadcast target model.
  - `src/agent_loom/team/targets.py` resolves only single targets (`manager`, `worker_id`, `worktree_key`, `window`, `ticket_id`).
  - `src/agent_loom/ticket/core.py` currently provides sprint behavior primarily via `TEAM_SPRINT_TAG` auto-tagging during `create`; there is no explicit ticket sprint context command surface.

### Risks + unknowns (and how we will resolve them)
1. YAML schema sprawl and ambiguous precedence between YAML and CLI flags.
   - Resolution: define a versioned schema plus deterministic precedence matrix in a dedicated ticket before integration.
2. Unsafe messaging expansion, including broadcast storms and invalid escalation paths.
   - Resolution: enforce explicit communication policy in validation and runtime checks; fail closed on unknown or forbidden routes.
3. Worktree pattern collisions where multiple members match the same ticket or worktree.
   - Resolution: deterministic matching order plus collision errors with actionable remediation.
4. BYO agent prompts bypass Loom protocol constraints.
   - Resolution: implement wrapper composition that prepends a non-negotiable Loom protocol block around user-specified agent prompts.
5. Ticket sprint context conflicts between env tags and explicit sprint selection.
   - Resolution: add explicit ticket sprint context commands and precedence tests: CLI/context first, env fallback second.

## Ticket Set

Created/updated ticket IDs:
- `al-aec3` — Define YAML team composition schema
- `al-89cc` — Integrate YAML composition into team start/run state
- `al-5e98` — Implement YAML-driven member lifecycle + BYO agent wrapping
- `al-f6e4` — Add broadcast messaging + communication and escalation boundaries
- `al-239b` — Add first-class ticket sprint context commands

Dependencies encoded:
- `al-89cc` depends on `al-aec3`
- `al-5e98` depends on `al-89cc`
- `al-f6e4` depends on `al-89cc`

Suggested ordering:
1. `al-aec3` (schema + validation baseline)
2. Parallel after `al-aec3`:
   - `al-89cc` (team start/run-state integration)
   - `al-239b` (ticket sprint context track, largely independent)
3. Parallel after `al-89cc`:
   - `al-5e98` (spawn/member mapping + BYO wrapper)
   - `al-f6e4` (broadcast + communication policy)
4. Reconcile and integrate both tracks, then run full gates.

Parallelization guidance:
- Safe parallel lane A (team config/runtime): `al-aec3` → `al-89cc` → (`al-5e98` + `al-f6e4`)
- Safe parallel lane B (ticket module): `al-239b`
- Avoid parallel edits to `team/core.py` between `al-5e98` and `al-f6e4` unless one worker is rebased after the other due high merge collision risk.

Sprint name: YAML Sprint Foundations
Sprint tag: sprint:YAML-Sprint-Foundations

## Notes

**2026-02-15T23:33:32Z**

Validation pass complete: confirmed all child tickets include objective alignment, scope/non-goals, implementation plan, verification commands, acceptance criteria, and risks. Commands run: loom ticket --json show <id> | jq checks for required sections and dep/tag/parent verification.

**2026-02-15T23:34:01Z**

Completion candidate: sprint prep deliverables done. Created backlog tickets [al-aec3, al-89cc, al-5e98, al-f6e4, al-239b], added dependencies, and wrote ordering/parallelization into ticket body. Verification commands run: loom ticket list -T sprint:YAML-Sprint-Foundations; loom ticket list --status open; git status --short --branch; git log -n 20 --oneline; loom ticket --json show <id> | jq (deps/parent/tags + rubric checks). Residual risks: high merge-collision probability in src/agent_loom/team/core.py between runtime tickets; schema precedence decisions must be locked before integration to avoid rework.
