---
{
  "created_at": "2026-04-01T17:44:00Z",
  "id": "decision:0002",
  "kind": "decision",
  "links": {
    "roadmap": [
      "roadmap:bootstrap-the-markdown-first-protocol-corpus"
    ]
  },
  "repository_scope": {
    "kind": "repository",
    "repository_id": "repo:root"
  },
  "schema_version": 1,
  "status": "active",
  "updated_at": "2026-04-01T17:44:00Z"
}
---

# Decision

Bounded execution in Loom should happen through packetized fresh-context child runs, while tickets remain the sole canonical ledger of live execution state.

Packets, run artifacts, and verification records support bounded work and replayability, but they must not become shadow truth that replaces the canonical record graph.

# Why This Decision Exists

`CONSTITUTION.md` locks in packetized fresh-context execution, explicit provenance, direct harness invocation, and tickets as the sole execution ledger.

The current repository already encodes that posture in the rules corpus, the Ralph/critique/docs skills, the packet compiler, and the acceptance doctrine.

# Alternatives Considered

- allowing long-lived transcripts to act as the primary execution context instead of curated packets
- treating run artifacts or plan documents as the live execution ledger
- allowing child runs to infer write scope or completion without explicit packet and parent reconciliation contracts

# Consequences

- parent contexts own workflow judgment, scope resolution, packet compilation, and reconciliation
- child contexts own only bounded work inside the packet contract
- Ralph, critique, and docs-update flows should prefer fresh harness contexts
- no outcome should be treated as complete until canonical records and verification evidence reflect the result truthfully
- ticket, critique, docs, and verification records must stay aligned so no second ledger emerges

# Supersession

This supersedes any assumption that long-lived transcripts, run artifacts, or plan notes can act as the live execution ledger in place of ticket truth.
