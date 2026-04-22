---
id: ticket:lj6g3e1y
kind: ticket
status: proposed
created_at: 2026-04-22T09:10:31Z
updated_at: 2026-04-22T09:10:31Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  critique:
    - critique:protocol-hardening-review
external_refs: {}
depends_on: []
---

# Summary

Reconcile legacy dogfood `.loom` directories that still use retired vocabulary.

# Context

The protocol source now teaches `wiki`, `packets`, and `evidence`, but the
dogfood tree still contains `.loom/docs`, `.loom/runs`, and
`.loom/verification`.

# Why Now

The protocol hardening pass added conformance guidance and clearer tree
expectations. The repository should not teach two competing runtime trees.

# Scope

- inventory `.loom/docs`, `.loom/runs`, and `.loom/verification`
- decide whether each artifact should move, be marked stale, or be retired
- reconcile references before moving or retiring records

# Non-goals

- do not rewrite unrelated historical records
- do not delete records without reference reconciliation

# Acceptance Criteria

- legacy directories are empty, removed, or explicitly documented as retired
- useful artifacts are moved to current owner paths
- references are reconciled

# Coverage

Covers:
- critique:protocol-hardening-review#FIND-001

# Critique Disposition

Risk class: medium

Required critique profiles:
- protocol-change
- operator-clarity

Findings:
- critique:protocol-hardening-review#FIND-001 — open

Status: required

# Wiki Disposition

Not required unless the reconciliation changes operator-facing guidance.

# Journal

- 2026-04-22T09:10:31Z: Created from critique follow-up.
