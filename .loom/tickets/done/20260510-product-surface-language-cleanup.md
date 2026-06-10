# Product Surface Language Cleanup

Status: done
Created: 2026-05-10
Updated: 2026-05-11

Legacy note: Risk — medium - changes shipped instruction wording and public docs after review feedback.

## Summary

Clean up the shipped skill and public documentation prose so operational guidance references Loom surfaces and named skills instead of exposing package-layer distinctions. Remove eval-shaped slicing examples from shipped skills and keep implementation-specific dogfooding context out of the product-facing corpus.

Single closure claim: product-facing instruction and doc prose avoids package-boundary guidance and eval-specific examples while preserving the intended shaping, slicing, Ralph, evidence, and audit semantics.

## Related Records

- `.loom/tickets/20260510-core-loop-hardening.md` - prior completed hardening plan that this follow-up corrects.
- `.loom/reviews/20260510-loop-hardening-review.md` - prior fresh review that is superseded for language-leakage concerns by this follow-up.
- `.loom/evidence/20260510-product-surface-language-cleanup-checks.md` - command and search evidence for this ticket.
- `.loom/reviews/20260511-product-surface-language-cleanup-review.md` - final fresh-context review for this ticket.
- `former packet 20260511T070642Z-product-surface-language-review` - prior review packet that found two public-doc wording leaks.
- `former packet 20260511T071542Z-product-surface-language-final-review` - final review packet after those findings were fixed.

## Scope

May change:

- `loom-core/skills/**`
- `loom-playbooks/skills/**`
- public docs that restate the operating route, including `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `INSTALL.md`, and package READMEs
- this ticket, related evidence, audit, and Ralph packet records

Must not change:

- eval app implementation files
- adapter entrypoints or manifests unless verification reveals direct drift
- historical dogfood records solely to make product-facing grep cleaner

## Acceptance

- ACC-001: Shipped skill bodies no longer use package-boundary guidance such as `Core Dependency`, `Use loom-core first`, `Core routing`, or `Playbooks over Core` to explain workflow precedence.
  - Evidence: grep checks over `loom-core/skills` and `loom-playbooks/skills`.
  - Audit: fresh review should challenge whether remaining wording still leaks package boundaries to skill consumers.
  - Result: satisfied by `.loom/evidence/20260510-product-surface-language-cleanup-checks.md` and `.loom/reviews/20260511-product-surface-language-cleanup-review.md`.

- ACC-002: Shipped skill bodies no longer contain examples tied to the recent eval or implementation path.
  - Evidence: grep checks over shipped skill directories for eval-specific terms and source diff inspection.
  - Audit: fresh review should challenge whether generic examples still overfit the dogfood episode.
  - Result: satisfied by `.loom/evidence/20260510-product-surface-language-cleanup-checks.md` and `.loom/reviews/20260511-product-surface-language-cleanup-review.md`.

- ACC-003: Package smoke, package pack checks, and Markdown diff checks pass after the cleanup.
  - Evidence: command outputs recorded in evidence.
  - Audit: fresh review should inspect evidence sufficiency.
  - Result: satisfied by `.loom/evidence/20260510-product-surface-language-cleanup-checks.md` and `.loom/reviews/20260511-product-surface-language-cleanup-review.md`.

## Current State

Closed. Implementation changes are complete; package checks, diff checks, shipped skill searches, public-doc searches, and eval-term searches passed. The first fresh review found two public-doc wording leaks, both were patched, and the final fresh review returned `clear` with no material findings.

## Journal

- 2026-05-10: Created follow-up after operator feedback about package-boundary leakage and eval-shaped examples in product-facing prose.
- 2026-05-11: Consumed `former packet 20260511T070642Z-product-surface-language-review`; fresh review returned `changes-needed` for two public-doc wording leaks in `loom-playbooks/README.md` and `ARCHITECTURE.md`.
- 2026-05-11: Patched both public-doc findings to route wording through `Loom records` rather than `Core` or `Core records`.
- 2026-05-11: Reran final package smoke, pack checks, `git diff --check`, shipped skill searches, public-doc package-boundary searches, and eval-term searches; results recorded in `.loom/evidence/20260510-product-surface-language-cleanup-checks.md`.
- 2026-05-11: Consumed `former packet 20260511T071542Z-product-surface-language-final-review`; final fresh review returned `clear` with no material findings.
- 2026-05-11: Closed after acceptance criteria, evidence, prior finding disposition, and audit told one truthful story. Residual risk: targeted searches cannot prove every synonym absent, and live agent behavior was not verified.
