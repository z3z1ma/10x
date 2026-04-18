---
name: loom-review
description: "Run adversarial critique against a ticket, packet, spec, wiki page, or other review target, then leave a durable critique record with prioritized follow-up."
arguments: "<ticket id | record id | change target>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-critique
  - loom-tickets
  - loom-specs
  - loom-wiki
---

# /loom-review

You are running **Loom Review**.

Review target:
`$ARGUMENTS`

This command is the explicit critique surface.
It exists so review has the same durability and rigor as implementation.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-critique`
- `loom-tickets`
- `loom-specs`
- `loom-wiki`

## Goals

- pressure-test claims against evidence
- surface correctness, scope, evidence, and operator-risk issues
- leave behind a durable critique record
- update the ticket or create follow-up work without hiding the review trail

## Procedure

1. **Anchor the target.**
   - Identify the ticket, spec, packet, wiki page, or other record being reviewed.
   - If a ticket is the main owner, read it first.

2. **Gather the minimum governing context.**
   - Read the linked plan, spec, evidence, and any recent packet outputs.
   - Inspect the relevant changed files or artifact diffs.

3. **Create critique scaffolding.**
   - Create or update a critique record under `.loom/critique/`.
   - If a fresh-context review is warranted, compile a critique packet under `.loom/packets/critique/`.

4. **Review through adversarial lenses.**
   - correctness
   - scope discipline
   - evidence sufficiency
   - hidden assumptions
   - failure modes
   - maintenance burden
   - operator clarity
   - security or performance if relevant

5. **Use multiple passes when helpful.**
   - If the harness supports subagents or multiple fresh reviewers, split the review into complementary passes.
   - A useful default split is:
     - correctness and scope
     - risk, security, and failure modes
     - operator clarity, docs, and wiki follow-through
   - If that transport is not available, do one disciplined single-agent critique.

6. **Write findings durably.**
   - Give each material finding a short title, severity, confidence, observation, why it matters, and follow-up.
   - Record a verdict and residual risks.

7. **Reconcile review back into Loom.**
   - Update the ticket status or journal if the critique changes what must happen next.
   - Create follow-up tickets for substantial issues.
   - Do not quietly “fix and forget” major review findings.

## Native tools to prefer

- `git status --short`
- `git diff --stat`
- `git diff`
- `rg -n '^(id|status|review_target):' .loom/{tickets,critique,specs,wiki,evidence} --glob '*.md'`
- `find .loom/packets/critique -type f -name '*.md' | sort | tail`

## Guardrails

- Do not overstate certainty.
- Do not collapse critique into casual inline comments.
- Do not silently rewrite ticket truth without leaving the review record.
- Fairness matters: be skeptical, not performatively harsh.

## Required output

- critique summary
- critique record and packet paths or IDs
- prioritized findings
- ticket or follow-up updates performed
- recommended next command
