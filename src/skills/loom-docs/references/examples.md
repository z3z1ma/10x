# Docs Examples

## Example Intent

Good docs intent sounds like this:

```text
Explain the accepted repository workflow clearly enough that another agent can operate the workspace without rediscovering the protocol from raw records.
```

## Example Evidence Basis

A strong docs update cites:

- the relevant spec or constitution record
- the relevant ticket or plan
- the verification records that justify the claims

## Example Strong Documentation Excerpt

```text
Audience
Agents and operators who need to resume work in this repository without hidden local context.

Problem Framing
The repository contains rules, skills, canonical records, and packet artifacts, but a fresh operator needs one durable explanation of how those layers relate and where to start.

Accepted System Shape
Canonical project truth lives in designated `.loom/` subtrees. Tickets remain the sole live execution ledger. Packets are bounded handoff artifacts and do not outrank canonical records.

Workflow / Operations Details
Start from the workspace layer to establish health and scope, then switch into the owning artifact skill. Use packets only when a fresh bounded child run is actually needed.

Verification Source
This explanation is grounded in the current constitution, rules corpus, workspace helpers, and verification records that exercised the helper layer and proof workflows.
```

Why this is strong:

- the audience is explicit
- the accepted shape is described plainly
- the evidence basis is visible
- the workflow guidance is useful to a future operator

## Example Good Documentation Outcome

Good docs output usually includes:

- the changed document
- a concise summary of what changed
- the evidence basis supporting the change
- stale triggers or known explanatory gaps that remain

## Example Weak Documentation Outcome

This is weak:

```text
Updated docs to match the changes.
```

It is weak because it says nothing about audience, accepted system shape, evidence basis, or what future drift should look like.

## Better Documentation Outcome Summary

```text
Updated the operator guide to explain the accepted Loom layer model, the fresh-entry workflow, the helper command surface, and the evidence basis supporting those explanations. The guide should be revisited if packet compilation, ticket ownership rules, or workspace control-plane routing change materially.
```

## Why This Example Matters

It shows docs as accepted explanation grounded in evidence, not as a substitute for unfinished implementation.
