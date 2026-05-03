---
id: plan:skills-corpus-context-integrity-hardening-pass
kind: plan
status: active
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T04:09:51Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-context-integrity-hardening-review
  ticket:
    - ticket:bootinv1
    - ticket:trustbd2
    - ticket:vocabx08
    - ticket:tplsave3
    - ticket:pktfam04
    - ticket:evhard05
    - ticket:reconchk
    - ticket:localed7
    - ticket:queryrc9
    - ticket:drives10
    - ticket:shipacc1
external_refs: {}
---

# Purpose

Sequence the council-driven skills-corpus hardening work into eleven bounded
tickets that improve fresh-agent operability without adding runtime machinery or a
new owner layer.

# Strategy

Work from doctrine and vocabulary toward operational surfaces:

1. Put only minimal orientation in bootstrap.
2. Add trust boundaries before expanding evidence and query surfaces.
3. Stabilize route/status vocabulary before templates and workflow references copy
   more examples.
4. Tighten templates, packets, evidence, and parent reconciliation.
5. Finish with ergonomics and workflow boundary tickets.

For each ticket:

- compile a Ralph packet;
- launch a `fixer` child worker;
- inspect and reconcile output;
- record structural evidence;
- run critique with required profiles;
- feed critique back through fixes or Ralph if necessary;
- record retrospective / promotion disposition;
- commit and push before continuing.

# Strategy Snapshot

The corpus is strong and runtime-safe. The improvement frontier is clarity,
copy-safety, anti-overclaiming, and preventing support surfaces from becoming a
second ledger.

# Workstreams

- Core worldview and trust: `ticket:bootinv1`, `ticket:trustbd2`.
- Vocabulary and templates: `ticket:vocabx08`, `ticket:tplsave3`.
- Execution and verification mechanics: `ticket:pktfam04`, `ticket:evhard05`,
  `ticket:reconchk`.
- Ergonomics and workflow boundaries: `ticket:localed7`, `ticket:queryrc9`,
  `ticket:drives10`, `ticket:shipacc1`.

# Milestones

- M1: Initiative, research, plan, and tickets created.
- M2: Bootstrap, trust, and vocabulary foundations closed.
- M3: Template, packet, evidence, and Ralph reconciliation surfaces closed.
- M4: Local edit, query, drive/support, and ship/acceptance boundaries closed.
- M5: Parent initiative accepted.

# Sequencing

`ticket:bootinv1` comes first because bootstrap is the first doctrine a cold model
sees. Keep it minimal: no internal framing, no marketing, no product strategy.

`ticket:trustbd2` follows because trust boundaries constrain evidence, research,
memory, and command snippets.

`ticket:vocabx08` precedes template and workflow edits so copied examples cite
canonical vocabulary rather than duplicating drift.

`ticket:tplsave3` then reduces template-retained ceremony. `ticket:pktfam04`,
`ticket:evhard05`, and `ticket:reconchk` tighten packet, evidence, and parent
execution mechanics.

`ticket:localed7` and `ticket:queryrc9` improve ergonomics without adding a new
skill or hidden runtime. `ticket:drives10` and `ticket:shipacc1` finish by
protecting workflow boundaries.

# Claim / Acceptance Coverage

| Source claim / acceptance ID | Downstream ticket | Coverage expectation | Evidence / critique route | Notes |
| --- | --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-001` | `ticket:bootinv1` | Minimal bootstrap orientation | Structural evidence plus critique | Do not leak internal framing |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-002` | `ticket:trustbd2` | Trust-boundary doctrine | Structural evidence plus critique | Doctrine-only, no tooling |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-003` | `ticket:vocabx08` | Vocabulary consolidation | Structural evidence plus critique | No runtime enum |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-004` | `ticket:tplsave3` | Save-ready template rules | Structural evidence plus critique | Avoid over-pruning gates |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-005` | `ticket:pktfam04` | Packet-family boundaries | Structural evidence plus critique | Ralph remains strict |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-006` | `ticket:evhard05` | Evidence anti-theater | Structural evidence plus critique | Evidence does not accept |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-007` | `ticket:reconchk` | Parent reconciliation and stale packet recovery | Structural evidence plus critique | No new reconciliation record |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-008` | `ticket:localed7` | Cheap local edit route | Structural evidence plus critique | No bypass mode |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-009` | `ticket:queryrc9` | Markdown-native query recipes | Structural evidence plus critique | No generated index or CLI |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-010` | `ticket:drives10` | Drive/support boundary tightening | Structural evidence plus critique | No `.loom/drive/` |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-011` | `ticket:shipacc1` | Acceptance-review versus ship separation | Structural evidence plus critique | Ship does not close tickets |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-012` | all tickets | Each child closes with evidence, critique, retrospective, commit, and push | Ticket-owned acceptance | Parent plan verifies at closure |

# Execution Waves

Sequential only. The tickets touch overlapping doctrine, templates, and workflow
references, so parallel Ralph would create unnecessary write-scope risk.

Wave readiness table:

| Wave | Tickets | Independent because | Expected `child_write_scope` / write scope overlap check | Dependency / shared-state check | Parent reconciliation |
| --- | --- | --- | --- | --- | --- |
| No wave | Sequential tickets | Dependencies and overlapping guidance favor order | Child write scopes may overlap across tickets; run one at a time | No generated files, lockfiles, migrations, or stateful resources | Ticket-owned update plus evidence/critique route |

# Risks

- Bootstrap can become over-explanatory; restrict to orientation needed before any
  other Loom token.
- Trust guidance can sound like a scanner requirement; keep it as agent behavior.
- Template pruning can create under-specified tickets if acceptance and critique
  gates disappear.
- Packet-family separation can make critique/wiki packets too vague if shared
  support metadata is under-specified.
- Query recipes can appear normative for every harness; frame as ordinary-tool
  examples.

# Evidence Strategy

Each ticket should record:

- `git diff --check` including new files with intent-to-add when needed;
- targeted `rg` queries for the ticket-specific wording;
- manual comparison against owner skill references/templates;
- confirmation that no runtime/CLI/schema/new-owner layer was introduced.

# Plan Readiness Review

Claim coverage: all initiative objectives are mapped to downstream tickets.

Spec / acceptance coverage: no separate spec is needed. The pass changes
protocol/operator guidance and uses initiative objectives plus ticket-local
acceptance criteria.

Placeholder scan: each ticket should include targeted placeholder/search evidence
when templates are touched.

Ticket-sized slices: eleven bounded tickets map directly to council improvement
opportunities.

Likely write scopes: each ticket is limited to the relevant skill references,
templates, and its Loom reconciliation records.

Parallel / wave independence: none; run sequentially.

Expected packet `child_write_scope` / write scope overlap check: each Ralph packet
must name exact files for that ticket. Do not launch overlapping packets.

Likely verification posture: observation-first structural validation for every
ticket.

Evidence and critique route: mandatory critique for every ticket by user
instruction; required profiles are named in each ticket.

Stop / loopback conditions: stop and ask only if a ticket would add runtime/new
owner-layer mechanics, leak internal product framing into bootstrap, or accept
material unresolved critique risk.

# Exit Criteria

- All eleven tickets are closed with evidence, critique, and retrospective
  disposition.
- All medium/high critique findings are resolved, accepted as risk with ticket
  provenance, superseded, or converted into follow-up tickets before closure.
- No runtime, hidden helper, CLI, schema engine, DB, daemon, MCP dependency, or new
  canonical owner layer is introduced.
- Final commit for each ticket is pushed.

# Completion Basis

When `status: completed`, cite child tickets, evidence records, critique records,
semantic commits, pushes, retrospective dispositions, residual risks, and any
follow-up tickets.
