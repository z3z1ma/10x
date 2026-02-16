---
id: 20260216222207-ticket-claim-enforcement-pattern-3499ae58
title: Ticket claim enforcement pattern
tags:
- correctness
- ticket
visibility: shared
status: active
created_at: "2026-02-16T22:22:07Z"
updated_at: "2026-02-16T22:22:07Z"
---

When enforcing `TK_REQUIRE_CLAIM`, check for an active lease (`claim_expires` not stale), not only claimant identity. Expired self-claims must be denied until a fresh claim is taken. Also centralize shared CLI query arguments (`list`/`ls`/`ready`) in one helper to prevent alias drift.

Related: [[20260216222207-ticket-claims-bef7d050|ticket-claims]] [[20260216222207-lease-expiration-3d68cc43|lease-expiration]] [[20260216222207-cli-arg-dedup-5af4f6ca|cli-arg-dedup]]
