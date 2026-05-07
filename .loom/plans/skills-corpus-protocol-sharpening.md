---
id: plan:skills-corpus-protocol-sharpening
kind: plan
status: completed
created_at: 2026-05-02T07:58:42Z
updated_at: 2026-05-02T11:20:32Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  roadmap:
    - roadmap:bootstrap-the-markdown-first-protocol-corpus
  initiative:
    - initiative:skills-corpus-protocol-sharpening
  research:
    - research:skills-corpus-council-review
  evidence:
    - evidence:skills-corpus-council-review
    - evidence:skills-corpus-protocol-sharpening-validation
  critique:
    - critique:skills-corpus-protocol-sharpening-review
  ticket:
    - ticket:0a1106b6
    - ticket:4e8ebe92
    - ticket:0cd38381
    - ticket:50ded996
    - ticket:1a12d9ff
    - ticket:233cfdeb
    - ticket:795fa0f4
    - ticket:53cf2989
    - ticket:cdf664af
  superseded_ticket:
    - ticket:3uv5l5fh
---

# Purpose

Sequence the council-driven sharpening of Loom's `skills/` corpus so improvements
land in a safe order: first align obvious drift, then tighten shared grammar, then
improve operator routes, then consolidate duplicated doctrine, then validate and
critique before acceptance.

# Strategy

Treat the work as high-risk protocol-authority maintenance over a Markdown-native
product surface.

The route is:

1. preserve the council findings as evidence and research,
2. align public framing with existing shipped skills,
3. update shared grammar before downstream skills depend on it,
4. update workflow skills and references that teach operators what to do,
5. consolidate duplicated doctrine under the correct owner skill,
6. run structural validation queries and diff review,
7. run mandatory critique before ticket acceptance,
8. convert unresolved medium/high findings into follow-up tickets or accepted
   risks.

The plan deliberately avoids adding a runtime, command surface, database, or new
canonical layer. It sharpens visible Markdown instructions and templates.

# Strategy Snapshot

The upstream council consensus is that Loom is already strong. The immediate
failure risk is not missing architecture; it is cross-surface drift and
under-specified grammar that can make fresh agents infer behavior instead of
recovering it from owner records.

This plan serves `initiative:skills-corpus-protocol-sharpening`. The initial broad
ticket `ticket:3uv5l5fh` was cancelled before implementation and decomposed into
smaller Ralph-sized tickets. Live execution truth now belongs to the child tickets
listed in this plan; this plan owns high-level sequencing and execution strategy.

# Workstreams

Public framing alignment:

- Add `loom-drive` to skill maps and shipped-skill summaries where omitted.
- Reconcile README's outer-loop explanation with using-Loom doctrine.
- Replace misleading canonical-layer wording with owner-layer/support-surface
  wording where packet or memory would otherwise appear canonical.

Shared record grammar:

- Add or clarify `OBJ-*` objective coverage and its qualified reference shape.
- Enumerate valid or currently supported `kind:` values and canonical ID/path
  forms.
- Normalize packet family IDs, terminal statuses, critique/wiki packet guidance,
  and handoff terminology.
- Resolve ticket `change_class` and `risk_class` strictness.
- Clarify semantic links such as `superseded_by`, `promoted_to`, and follow-up
  relationships.
- Tighten external-reference provenance and lifecycle guidance.

Operator ergonomics:

- Add cold-start and post-compaction resume guidance to workspace entry and
  summarize it in using-Loom doctrine or README only where necessary.
- Teach pre-compaction checkpoints without making memory or handoff notes a
  second ledger.
- Ban generic scratchpads and route observations, hypotheses, execution state,
  and support recall to the correct owners.
- Add guidance for concurrent file-first edits, re-read-before-write discipline,
  stale records, and rejected or overscoped Ralph iterations.
- Clarify critique finding conversion into resolved, accepted risk, or linked
  follow-up ticket states.
- Clarify memory pruning cadence and frontmatter/status expectations.

Owner-surface consolidation:

- Make atlas page shape canonical in the wiki surface and have codemap point to
  it instead of duplicating the whole shape.
- Move or point retrospective mechanics to `loom-retrospective` rather than
  spreading them through shared records unnecessarily.
- Let research define spike/sketch as research variants while `loom-spike` owns
  procedural workflow detail.
- Tighten skill metadata conventions in `loom-skill-authoring`.

Validation and review:

- Run targeted grep/rg structural checks for skill maps, coverage IDs, packet
  grammar, frontmatter values, status values, risk/change class usage, metadata,
  empty directories, and source-repo leakage.
- Record validation evidence after product-surface edits.
- Run mandatory critique using protocol-change, operator-clarity, and
  records-grammar/routing-safety lenses before acceptance.

# Milestones

1. Planning records created and linked: initiative, research, evidence, plan, and
   tickets.
2. Low-risk drift corrected: `loom-drive` surfaced and README/public diagrams
   aligned with using-Loom doctrine.
3. Shared grammar hardened: coverage, kinds, IDs, packets, risk/change,
   semantic links, and external refs made coherent.
4. Operator routes strengthened: resume, compaction, scratchpads, concurrency,
   rejected Ralph, follow-up conversion, memory pruning, and evidence freshness
   taught without creating new ledgers.
5. Duplicated doctrine consolidated under owner skills with pointers from related
   skills.
6. Structural evidence recorded from targeted queries and diff review.
7. Mandatory critique completed, with findings resolved, accepted as risk, or
   converted into linked follow-up tickets.

# Sequencing

Start with low-risk alignment because it removes obvious user-facing drift and
does not depend on deeper grammar changes. Then update shared grammar so later
skill edits can cite the right owner surface instead of inventing local variants.
After grammar is clear, update operator workflows. Consolidate duplication only
after the owner surface is explicit, so deletes and pointer edits do not remove
needed instructions. Validate and critique after the full diff is inspectable.

Loop back to research if implementation reveals that a council finding is wrong
or obsolete. Loop back to constitution only if a proposed improvement conflicts
with the no-runtime, skills-only, or owner-layer authority boundaries. Loop back
to tickets if the work becomes too broad for one acceptance dossier.

# Execution Waves

Wave 1:

- `ticket:0a1106b6` low-risk public and routing alignment. Expected write scope:
  `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md` if needed,
  `skills/using-loom/**`, and skill-map/routing references that enumerate
  workflow skills. The pass should avoid record grammar changes except where
  necessary to keep references truthful.

Wave 2:

- `ticket:4e8ebe92` shared record and objective grammar. Expected write scope:
  `skills/loom-records/**`, `skills/loom-initiatives/**`, and small pointers from
  affected skills. This wave is high risk because it affects claim coverage and
  shared record grammar.

Wave 3:

- `ticket:0cd38381` packet and handoff grammar. Expected write scope:
  `skills/loom-ralph/**`, `skills/loom-records/**`, `skills/loom-critique/**`,
  `skills/loom-wiki/**`, and `skills/loom-drive/**`.
- `ticket:50ded996` ticket risk, critique, acceptance, and follow-up grammar.
  Expected write scope: `skills/loom-tickets/**`,
  `skills/loom-records/references/change-class.md`, and targeted
  `skills/loom-critique/**` pointers.
- These tickets may run in parallel only if their child write scopes are narrowed
  to avoid overlapping `skills/loom-records/**` edits.

Wave 4:

- `ticket:1a12d9ff` workspace resume and compaction guidance. Expected write
  scope: `skills/loom-workspace/**`, `skills/using-loom/**`,
  `skills/loom-drive/**`, `skills/loom-tickets/**`, and `skills/loom-memory/**`.
- `ticket:233cfdeb` scratchpad, external reference, and concurrency guardrails.
  Expected write scope: `skills/loom-records/**`, `skills/loom-workspace/**`,
  `skills/loom-git/**`, `skills/loom-evidence/**`, `skills/loom-research/**`,
  `skills/loom-tickets/**`, and `skills/loom-memory/**`.
- `ticket:795fa0f4` memory pruning and frontmatter expectations. Expected write
  scope: `skills/loom-memory/**` plus narrow pointers to `skills/loom-records/**`
  or `skills/loom-retrospective/**` if needed.

Wave 5:

- `ticket:53cf2989` owner-surface consolidation. Expected write scope:
  `skills/loom-wiki/**`, `skills/loom-codemap/**`, `skills/loom-retrospective/**`,
  `skills/loom-records/**`, `skills/loom-research/**`, `skills/loom-spike/**`, and
  `skills/loom-skill-authoring/**`.

Wave 6:

- `ticket:cdf664af` validation, evidence, critique, and reconciliation. Expected
  write scope: `.loom/evidence/**`, `.loom/critique/**`, `.loom/tickets/**`, and
  any follow-up ticket records needed for unresolved findings. Product-surface
  edits should be frozen except for critique fixes.

# Risks

- Even the child tickets may be too broad if a surface proves more tangled than
  expected. Mitigation: split explicit follow-up tickets rather than expanding a
  Ralph packet beyond one bounded iteration.
- README edits could make README appear more authoritative than using-Loom.
  Mitigation: frame README as product overview and keep using-Loom doctrine as the
  operating authority.
- Grammar edits could silently break existing records. Mitigation: use structural
  queries and explicit transition language for any changed reference shape.
- Resume and scratchpad guidance could become a new ledger. Mitigation: route live
  state to tickets, observations to evidence, synthesis to research/wiki, and
  recall to memory only when support-only.
- Consolidation deletes could remove useful domain nuance. Mitigation: replace
  duplicate detail with pointers only after the owner surface contains the needed
  instruction.

# Evidence Strategy

Use structural and review evidence rather than runtime tests, because this is a
Markdown protocol corpus.

Minimum evidence after implementation:

- `git diff --check`.
- `git diff --stat` and manual diff review of touched product surfaces.
- Targeted `rg` queries for `loom-drive` visibility in public maps.
- Targeted `rg` queries for `OBJ-*`, `REQ-*`, `ACC-*`, and `CLAIM-*` coverage
  grammar.
- Targeted `rg` queries for packet family fields and `write_scope` drift.
- Targeted `rg` queries for `kind:`, `status:`, `skill_kind:`, `compatibility:`,
  `change_class`, and `risk_class` values.
- Empty-directory check for `skills/` directories.
- Source-repo leakage check for `agent-loom`, absolute paths, `.opencode`,
  `examples/`, and `optional-utilities` inside shipped skills.
- Manual comparison against this plan and child-ticket acceptance criteria.

# Plan Readiness Review

Spec / acceptance coverage:

No separate spec exists yet. `initiative:skills-corpus-protocol-sharpening` owns
strategic objective criteria; child tickets own ticket-local acceptance for their
bounded slices. If behavior contracts become reusable or disputed, promote them
into a spec before relying on them across multiple tickets.

Placeholder scan:

This plan intentionally contains no unresolved placeholder acceptance. Open
questions are recorded in `research:skills-corpus-council-review` and routed as
loopback conditions.

Ticket-sized slices:

The first broad ticket has been replaced by smaller tickets. If any child ticket
cannot be reviewed in one acceptance dossier, create follow-up tickets and update
this plan rather than expanding scope silently.

Likely write scopes:

- Public framing: `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, possibly
  `INSTALL.md` or `AGENTS.md` only if direct drift is found.
- Product surface: `skills/**`.
- Loom execution records: `.loom/evidence/**`, `.loom/critique/**`,
  `.loom/tickets/**`, and follow-up records only as needed.

Likely verification posture:

Observation-first structural validation plus mandatory critique. No code runtime
tests are expected because the changed product is Markdown protocol guidance.

Evidence and critique route:

Evidence must be recorded after the product-surface diff exists. Critique is
mandatory before acceptance because the work changes protocol authority,
operator routing, record grammar, packet contracts, and closure behavior.

Stop / loopback conditions:

- Stop and ask the user if an edit would add a runtime, CLI, database, daemon,
  hidden helper, or new canonical owner layer.
- Loop back to research if a council finding cannot be verified in the current
  corpus.
- Loop back to ticket refinement if implementation needs multiple independently
  reviewable follow-up tickets.
- Loop back to constitution if a proposed change contradicts the anti-runtime,
  skills-only, owner-layer, or ticket-ledger boundaries.

# Exit Criteria

- The child tickets have been accepted, cancelled with rationale, or have
  explicitly spawned follow-up tickets for residual work.
- The linked evidence records fresh structural validation from the final diff.
- Mandatory critique exists and all medium/high findings are resolved, accepted as
  risk, superseded by evidence, or converted into linked follow-up tickets.
- The initiative success metrics have a truthful status summary.
- Any wiki or retrospective promotion decision is recorded in the relevant ticket.

# Completion Basis

Completed at 2026-05-02T11:20:32Z.

All child tickets are closed: `ticket:0a1106b6`, `ticket:4e8ebe92`,
`ticket:0cd38381`, `ticket:50ded996`, `ticket:1a12d9ff`, `ticket:233cfdeb`,
`ticket:795fa0f4`, `ticket:53cf2989`, and `ticket:cdf664af`.

Final validation is recorded in
`evidence:skills-corpus-protocol-sharpening-validation`. Mandatory critique is
recorded in `critique:skills-corpus-protocol-sharpening-review`; its two medium
findings were resolved by targeted product-surface fixes and the final oracle
re-check passed.

No follow-up tickets or accepted risks were required for this plan. The plan can
stop because the scoped protocol-sharpening route landed through child tickets,
structural validation, mandatory critique, and ticket-owned acceptance.
