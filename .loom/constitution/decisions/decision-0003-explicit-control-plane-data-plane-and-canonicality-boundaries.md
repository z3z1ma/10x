---
{
  "created_at": "2026-04-01T18:06:00Z",
  "id": "decision:0003",
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
  "updated_at": "2026-04-01T18:06:00Z"
}
---

# Decision

Loom in this repository keeps an explicit boundary between the control plane and the data plane, and it keeps an explicit distinction between canonical and merely durable artifacts.

Rules, skill activation guidance, scope and packet doctrine, and parent workflow judgment form the visible control plane. Canonical records, packets, run artifacts, verification artifacts, and derived reports live in the data plane, but not all data-plane artifacts are canonical truth.

# Why This Decision Exists

`CONSTITUTION.md` treats this distinction as necessary to prevent hidden behavior, authority inversion, and shadow ledgers.

The current codebase already reflects that architecture through the rules corpus, the workspace and Ralph skills, the packet compiler, canonical `.loom/` subtrees, and the explicit non-canonical status of `.loom/runs/` and `.loom/verification/`.

# Alternatives Considered

- letting packets or run artifacts silently outrank canonical records because they are newer or more detailed
- treating everything under `.loom/` as equally canonical
- hiding workflow judgment inside helper scripts or runtime behavior instead of preserving it in the visible control surfaces

# Consequences

- canonical records remain the top project-truth layer beneath the active rules and operator constraints
- `.loom/runs/` and `.loom/verification/` persist for replayability and evidence, but they do not silently mutate canonical truth
- helpers must continue to mechanize published doctrine instead of becoming a shadow control plane
- future docs, specs, plans, and tickets should explain which artifact owns the next durable truth change instead of blending layers together

# Supersession

This supersedes any assumption that durable artifact persistence alone makes an artifact canonical, or that helper behavior may quietly redefine authority boundaries.
