---
id: research:skills-corpus-context-integrity-hardening-review
kind: research
status: concluded
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T04:09:51Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
external_refs: {}
---

# Question

Which council findings should drive the next corpus-hardening pass over `skills/`
after the residual protocol sharpening pass closed?

# Why This Matters

The user delegated a complete follow-through pass to make the `skills/` corpus
more precise, agent-operable, and future-proof without adding runtime machinery or
new owner layers.

# Scope

Covered:

- Council review of `README.md` and `skills/` from task
  `ses_2140f74d6ffeNXzzTi38MDzqc7`.
- The user's additional framing around model-shaped agentic coding: finite visible
  context, bounded chunks, externalized state, progressive disclosure, fresh
  workers, observed verification, agent-computer interface, and human judgment.
- Product constraints from `AGENTS.md`: `skills/` is the product surface;
  Markdown and ordinary file tools remain the API; no runtime, CLI, schema engine,
  daemon, DB, MCP, hidden helper, or new canonical owner layer should become
  protocol truth.

Excluded:

- Marketing copy or internal positioning in bootstrap.
- Tool-dependent validation systems.
- Broad rewrites of the full corpus for style alone.

# Method

Synthesized the council report into bounded workstreams and ordered them by
upstream dependency: bootstrap worldview, trust boundaries, vocabulary, templates,
packet families, evidence, reconciliation, local edit ergonomics, query recipes,
drive/support boundaries, and acceptance/ship separation.

# Sources

- `README.md`
- `skills/`
- Council report from task `ses_2140f74d6ffeNXzzTi38MDzqc7`
- User instruction in the current conversation to plan, ticket, execute with
  Ralph, critique, commit, push, and continue until complete

# Evidence

Council consensus:

- Loom already strongly embodies repo-local context integrity, owner records,
  bounded packets, ticket-owned closure, evidence, critique, and Markdown-native
  portability.
- Highest-leverage improvements should sharpen doctrine and ergonomics rather
  than add machinery.
- Bootstrap should carry only the minimal worldview a never-seen-Loom model needs
  to orient itself: placement, ownership, disposable sessions, and graph recovery.
- Trust boundaries, evidence anti-theater, parent reconciliation, route/status
  vocabulary, local-edit ergonomics, query recipes, drive/support limits, and
  ship/acceptance separation remain the main corpus-hardening opportunities.

# Rejected Options

- Do not add validators, schema engines, command routers, CLIs, daemons, DBs, MCP
  dependencies, hidden helpers, or new canonical owner layers.
- Do not put product marketing or internal strategic framing into bootstrap.
- Do not create a new `drive` or `local_edit` owner layer.

# Null Results

None.

# Conclusions

The next pass should be a bounded skills-corpus hardening pass with eleven tickets:

1. minimal bootstrap invariant;
2. trust-boundary doctrine;
3. route/status vocabulary consolidation;
4. save-ready template pruning rules;
5. packet-family requirement separation;
6. evidence anti-theater hardening;
7. Ralph parent reconciliation and stale packet recovery;
8. low-friction `local_edit` guidance;
9. Markdown-native query recipes;
10. drive/support boundary tightening;
11. acceptance-review versus ship boundary.

# Recommendations

Execute each ticket sequentially through Ralph, structural evidence, mandatory
critique, retrospective disposition, semantic commit, and push. Stop only if a
ticket would require new product direction or violate the Markdown-native product
boundary.

# Open Questions

None for planning. Each ticket may loop back if Ralph or critique finds the slice
too broad.

# Linked Work

- `initiative:skills-corpus-context-integrity-hardening-pass`
- `plan:skills-corpus-context-integrity-hardening-pass`
