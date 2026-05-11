---
id: research:agentsys-command-practices-synthesis
kind: research
status: concluded
created_at: 2026-05-07T08:24:29Z
updated_at: 2026-05-07T08:40:29Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:agntsys7
  research:
    - research:external-peer-skill-practices-synthesis
external_refs:
  agentsys_github: https://github.com/agent-sh/agentsys/tree/main#command-details
  agentsys_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/agentsys
  mattpocock_skills_github: https://github.com/mattpocock/skills
  mattpocock_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/mattpocock-skills
  addyosmani_agent_skills_github: https://github.com/addyosmani/agent-skills
  addyosmani_agent_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/addyosmani-agent-skills
  superpowers_github: https://github.com/obra/superpowers
  superpowers_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/superpowers
---

# Question

Which peer skill practices from AgentSys, Matt Pocock's skills, Addy Osmani's
agent skills, and Superpowers should Loom assimilate more boldly into existing
skills, without importing command/plugin/runtime models or letting external
systems own Loom truth?

# Why This Matters

The prior peer-practice tranche was too conservative. The peer sources contain
strong workflow practices around delivery gates, problem grilling, divergent and
convergent option shaping, tracer-bullet execution, deterministic collection,
source-driven implementation, specialist review, performance investigation, docs
drift, external consultation, release packaging, verification discipline, and
workflow-pattern learning. Loom should harvest those practices into its
Markdown-native owner graph instead of dismissing them because some source repos
are command-, hook-, or runtime-heavy.

# Scope

This pass covers direct inspection of local peer clones under
`/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/`:

- `README.md` command details and design philosophy
- `docs/workflows/NEXT-TASK.md`
- `docs/workflows/SHIP.md`
- selected `.kiro/skills/*/SKILL.md` files for review, slop cleanup, drift,
  delivery validation, docs sync, learning, debate, repo intel, and performance
  baseline/experiment practice
- selected Matt Pocock skill files for grilling, glossary/ADR alignment,
  tracer-bullet TDD, throwaway prototypes, issue triage, architecture deepening,
  and diagnosis
- selected Addy Osmani agent skill files for idea refinement, source-driven
  development, incremental implementation, code simplification, five-axis review,
  performance optimization, context engineering, and launch discipline
- selected Superpowers skill files for brainstorming gates, zero-context plans,
  executing plans, TDD pressure, systematic debugging, code review request and
  reception, verification-before-completion, and branch-finishing choices

It excludes adopting peer slash commands, npm installers, plugin marketplaces,
hook enforcement, JSON runtime state, generated state directories, external
CI/PR/deployment control, model routing, or tool-specific directory conventions as
Loom core.

# Method

- Fetched the AgentSys GitHub command-details page for overview.
- Cloned peer repositories into the benchmark repository area.
- Read selected workflow/skill files directly from local clones.
- Compared observed patterns against Loom's owner-layer model and existing skill
  surfaces.
- Routed transferable practices to the existing Loom skills that own the durable
  truth or workflow discipline.

# Sources

- Source: `agentsys/README.md` lines 120-168, 210-379
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: command and skill taxonomy evidence; not Loom authority

- Source: `agentsys/README.md` lines 380-639
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: shipping, slop cleanup, performance, drift, review, and enhancement pattern evidence; not Loom authority

- Source: `agentsys/README.md` lines 640-939
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: repo-intel, docs sync, learn, consult/debate, web, release, and skillers pattern evidence; not Loom authority

- Source: `agentsys/README.md` lines 940-1164
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: onboard/can-i-help and design philosophy evidence; not Loom authority

- Source: `agentsys/docs/workflows/NEXT-TASK.md` lines 1-220
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: end-to-end delivery pipeline and review-loop evidence; not Loom authority

- Source: `agentsys/docs/workflows/SHIP.md` lines 1-220
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: ship handoff and external review-comment handling evidence; not Loom authority

- Source: `agentsys/.kiro/skills/orchestrate-review/SKILL.md` lines 1-220
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: specialist review, aggregation, iteration, and stall discipline evidence; not Loom authority

- Source: `agentsys/.kiro/skills/deslop/SKILL.md` lines 1-204
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: certainty-graded cleanup and AI artifact detection evidence; not Loom authority

- Source: `agentsys/.kiro/skills/drift-analysis/SKILL.md` lines 1-324
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: plan/docs/issue/code drift analysis evidence; not Loom authority

- Source: `agentsys/.kiro/skills/validate-delivery/SKILL.md` lines 1-186
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: delivery validation checklist evidence; not Loom authority

- Source: `agentsys/.kiro/skills/sync-docs/SKILL.md` lines 1-220
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: docs/code sync pattern evidence; not Loom authority

- Source: `agentsys/.kiro/skills/learn/SKILL.md` lines 1-220
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: progressive research and source quality scoring evidence; not Loom authority

- Source: `agentsys/.kiro/skills/debate/SKILL.md` lines 1-220
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: structured adversarial consultation evidence; not Loom authority

- Source: `agentsys/.kiro/skills/repo-intel/SKILL.md` lines 1-63
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: repo intelligence staleness and deterministic analysis evidence; not Loom authority

- Source: `agentsys/.kiro/skills/perf-baseline-manager/SKILL.md` lines 1-30 and `perf-theory-tester/SKILL.md` lines 1-36
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:24:29Z
  - Freshness risk / recheck trigger: recheck if AgentSys clone changes
  - Trust rationale: performance baseline and controlled experiment evidence; not Loom authority

- Source: `mattpocock-skills/skills/productivity/grill-me/SKILL.md` lines 1-10 and `skills/engineering/grill-with-docs/SKILL.md` lines 1-88
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:29:07Z
  - Freshness risk / recheck trigger: recheck if Matt Pocock skills clone changes
  - Trust rationale: one-question grilling, codebase-first clarification, glossary conflict, scenario probing, and ADR threshold evidence; not Loom authority

- Source: `mattpocock-skills/skills/engineering/tdd/SKILL.md` lines 1-109, `prototype/SKILL.md` lines 1-30, `triage/SKILL.md` lines 1-103, `improve-codebase-architecture/SKILL.md` lines 1-71, and `diagnose/SKILL.md` lines 1-117
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:29:07Z
  - Freshness risk / recheck trigger: recheck if Matt Pocock skills clone changes
  - Trust rationale: tracer-bullet TDD, throwaway prototype, issue triage, architecture deepening, and feedback-loop diagnosis evidence; not Loom authority

- Source: `addyosmani-agent-skills/skills/idea-refine/SKILL.md` lines 1-178 and `source-driven-development/SKILL.md` lines 1-194
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:29:07Z
  - Freshness risk / recheck trigger: recheck if Addy Osmani agent skills clone changes
  - Trust rationale: divergent/convergent shaping, hidden assumptions, not-doing lists, official-source hierarchy, and version-aware citation evidence; not Loom authority

- Source: `addyosmani-agent-skills/skills/incremental-implementation/SKILL.md` lines 1-245, `code-simplification/SKILL.md` lines 1-331, `code-review-and-quality/SKILL.md` lines 1-347, `performance-optimization/SKILL.md` lines 1-350, `context-engineering/SKILL.md` lines 1-289, and `shipping-and-launch/SKILL.md` lines 1-309
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:29:07Z
  - Freshness risk / recheck trigger: recheck if Addy Osmani agent skills clone changes
  - Trust rationale: incremental slicing, simplification, five-axis review, measured performance, context hierarchy, and launch/rollback evidence; not Loom authority

- Source: `superpowers/skills/brainstorming/SKILL.md` lines 1-164, `writing-plans/SKILL.md` lines 1-152, `executing-plans/SKILL.md` lines 1-70, and `finishing-a-development-branch/SKILL.md` lines 1-220
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:29:07Z
  - Freshness risk / recheck trigger: recheck if Superpowers clone changes
  - Trust rationale: hard pre-implementation shaping, zero-context plan detail, critical plan review, and finishing-option discipline evidence; not Loom authority

- Source: `superpowers/skills/test-driven-development/SKILL.md` lines 1-371, `systematic-debugging/SKILL.md` lines 1-296, `requesting-code-review/SKILL.md` lines 1-103, `receiving-code-review/SKILL.md` lines 1-213, and `verification-before-completion/SKILL.md` lines 1-139
  - Type / provenance: external repository clone, direct file read
  - Observed at / version: 2026-05-07T08:29:07Z
  - Freshness risk / recheck trigger: recheck if Superpowers clone changes
  - Trust rationale: TDD pressure, root-cause investigation, precise review packets, review-feedback verification, and evidence-before-claims evidence; not Loom authority

# Variant / Experiment Matrix

| Variant / hypothesis | Artifact or probe | Strength | Weakness | Decision |
| --- | --- | --- | --- | --- |
| Copy AgentSys commands and runtime | README command details, workflow docs | Very operational and comprehensive | Violates Loom's Markdown-native, no-runtime, skills-only product boundary | Rejected |
| Ignore runtime-heavy AgentSys because Loom is superior | Prior conservative tranche plus user feedback | Avoids ontology drift | Misses many high-quality practices the user explicitly wants considered | Rejected |
| Assimilate command practices into existing Loom routes | Current Loom skills plus AgentSys direct reads | Preserves owner graph while improving operator discipline | Requires more substantial cross-surface edits and critique | Chosen |
| Add a new omnibus delivery command skill | AgentSys `/next-task` and `/prepare-delivery` | Familiar end-to-end shape | Risks creating a shadow command surface and second ledger | Rejected |
| Treat Superpowers hard gates as literal Loom runtime law | Superpowers brainstorming and TDD skills | Strong anti-rationalization force | Too broad for Loom's proportional owner-layer model and would overrule operator/harness autonomy | Rejected |
| Assimilate peer pressure patterns as Loom-native gates and loopbacks | Direct reads across all four source sets | Preserves Loom ownership while strengthening discipline | Requires careful wording to avoid command/runtime drift | Chosen |

# Evidence Synthesis

- AgentSys's strongest transferable idea is not the command system; it is a
  delivery-chain mindset: discovery, exploration, planning, implementation,
  cleanup, review, validation, docs sync, and ship packaging as explicit gates.
- Loom already has owner layers and workflows that can carry those gates more
  durably than JSON runtime state. The gap is making the gates more visible in
  `loom-drive`, `loom-tickets`, `loom-ship`, `loom-critique`, and related skills.
- AgentSys review guidance is useful because it separates core review passes from
  conditional specialists, aggregates findings by severity/confidence, repeats
  review after fixes, and escalates when the loop stalls. Loom should express that
  as critique profiles, ticket-owned finding disposition, and parent reconciliation.
- AgentSys `deslop` is useful as a named cleanup lens: debug statements,
  placeholders, empty catches, excessive comments, stubs, dead code,
  over-engineering, buzzword inflation, and hardcoded secrets. Loom should treat
  this as critique/evidence cleanup discipline, not an auto-fix runtime.
- Performance work needs its own disciplined branch inside debugging/evidence:
  baseline, breaking point, constraints, hypotheses, code paths, profiling, one
  change per experiment, repeated validation, and final consolidation.
- Drift detection maps cleanly to Loom's truth-boundary doctrine: compare plans,
  docs/wiki, issues/tickets, and implementation reality; route each discrepancy to
  the owner layer rather than letting the report own truth.
- Repo intel and onboarding reinforce deterministic collection before synthesis:
  gather manifests, CI, git history, AST/symbols, hotspots, ownership, and bus
  factor when relevant, then preserve accepted structure in codemap/wiki and
  observations in evidence.
- Learn/source research practices strengthen `loom-research`: progressive source
  discovery, quality scoring, just-in-time extraction, and source indexes are
  transferable as optional research discipline.
- Consultation and debate are useful when bounded by evidence-cited claims,
  challenger roles, concessions, unresolved questions, and a parent verdict. They
  must remain support/critique/research inputs, not external-model truth owners.
- Ship/release/docs-sync practices strengthen `loom-ship`: external review comments
  need classification and disposition; release packaging needs ecosystem and
  changelog awareness; docs sync needs stale examples, broken refs, and missing
  docs routed to wiki/docs owners or follow-up tickets.
- Skillers/workflow-pattern learning maps to retrospective and memory: transcripts
  may reveal repeated pain or wishes, but durable lessons must be promoted into
  owner records, wiki, research, specs, or project-local skills.
- Matt Pocock's strongest transferable pattern is ruthless clarification without
  lazy questions: ask one question at a time, explore the codebase when the answer
  is inspectable, challenge fuzzy terms against glossary/ADR context, and update
  durable language or decisions only when the threshold is met.
- Matt's tracer-bullet TDD and prototype guidance fit Loom as spec/plan/Ralph/spike
  discipline: one behavior at a time through public interfaces, prototypes answer
  one question, surface state, avoid persistence by default, and delete or absorb
  throwaway scaffolding after the answer is preserved.
- Matt's architecture guidance gives Loom useful code-structure vocabulary without
  becoming ontology: look for shallow modules, seams, locality, leverage, test
  surfaces, and the deletion test, then route durable findings to codemap,
  research, spec, plan, or tickets.
- Addy's idea-refine practice strengthens Loom's outer loop: divergent options,
  convergent clustering, hidden assumptions, explicit not-doing lists, target user,
  success criteria, and codebase-grounded constraints should shape specs and plans
  before implementation.
- Addy's source-driven development and context-engineering practices strengthen
  research/codemap/Ralph: exact dependency versions, official source hierarchy,
  precise citations, conflict surfacing, focused context packing, trust levels, and
  ambiguity options are transferable. Hooks, MCP assumptions, and command files are
  not required Loom runtime surfaces.
- Addy's incremental implementation, simplification, five-axis review, performance,
  and launch guidance strengthen tickets, critique, evidence, and ship: thin
  vertical slices, scope discipline, behavior-preserving simplification,
  correctness/readability/architecture/security/performance review, baseline-first
  performance, rollback plans, monitoring, and post-launch verification are useful
  when routed through owner records.
- Superpowers contributes strong anti-rationalization language: present a design
  before broad creative implementation, write zero-context plans/packets, review a
  plan critically before executing, watch tests fail before behavior code when TDD
  applies, find root cause before fixes, verify review feedback before acting, and
  require fresh verification before success claims.
- Superpowers' hard-gate style should be translated into Loom's proportional gates:
  mandatory for high-risk or behavior-defining work, recommended for medium-risk
  work, and avoidable for tiny local edits when the ticket and evidence honestly
  justify that choice.

# Rejected Options

- Add AgentSys-like commands to Loom: rejected because command surfaces are
  invocation conveniences, not Loom product truth.
- Require static analyzers, agnix, repo-intel, Playwright, or CI tools as Loom core:
  rejected because optional tool outputs can be evidence, but Loom must stay
  Markdown-native and plain-tool operable.
- Import AgentSys JSON state files as resumable truth: rejected because Loom tickets
  own live execution state and packets/evidence/critique/wiki own their own layers.
- Auto-fix every review/slop finding: rejected because Loom requires ticket-owned
  disposition, evidence, and critique proportional to risk.

# Null Results

- No AgentSys command is a better truth owner than Loom's existing layers.
- The useful additions are review, validation, collection, and packaging discipline,
  not new ontology.
- Runtime state and hook enforcement are strong AgentSys implementation choices but
  non-transferable as Loom core.
- Exact peer folder conventions such as `CONTEXT.md`, `docs/ideas`,
  `docs/superpowers`, `.out-of-scope`, command files, and hooks are examples of
  local transport. Loom should instead route glossary, ideas, specs, plans,
  out-of-scope decisions, and reusable explanations to existing owner layers.

# Conclusions

Assimilate more substantially than the prior tranche:

- Strengthen `loom-drive` and tickets around end-to-end delivery gates and stop
  points.
- Strengthen `loom-critique` around specialist selection, confidence/severity,
  iterative review, stall limits, and AI-artifact cleanup.
- Strengthen `loom-debugging` and evidence around performance investigations.
- Strengthen `loom-codemap`, `loom-research`, and `loom-wiki` around deterministic
  collection, source quality, drift detection, and accepted explanation promotion.
- Strengthen `loom-ship` around docs sync, release packaging, review-comment
  classification, and external handoff truth mirroring.
- Strengthen `loom-retrospective` around recurring transcript/workflow patterns as
  support signals that must be promoted to owner truth before they matter.
- Strengthen `loom-critique`/`loom-research` around consultation/debate as bounded,
  evidence-cited adversarial support.
- Strengthen `loom-workspace`, `loom-specs`, and `loom-wiki` around one-question
  grilling, codebase-first clarification, divergent/convergent option shaping,
  hidden assumptions, not-doing lists, and shared-language conflict handling.
- Strengthen `loom-plans`, `loom-tickets`, `loom-ralph`, and `loom-spike` around
  tracer bullets, zero-context worker contracts, source-driven context, critical
  plan/packet review before execution, and throwaway prototype cleanup.
- Strengthen `loom-evidence` and `loom-ship` around fresh verification before
  completion claims, measured performance changes, rollout/rollback readiness, and
  post-launch observation when launches are in scope.

# Recommendations

- Make visibly broader edits than `ticket:peerpr07`, focused on skill behavior and
  references rather than adding new runtime surfaces.
- Add AgentSys-inspired named lenses and gate checklists where they fit existing
  Loom routes.
- Validate with structural scans, hidden-runtime lexical scans, marker scans, and
  mandatory critique because this changes protocol-authority guidance.

# Open Questions

- Whether a later pass should add optional project-local examples showing complete
  delivery chains. This pass should not add examples unless needed to validate the
  product-skill guidance.

# Linked Work

- `ticket:agntsys7`
- `ticket:peerpr07`
- `research:external-peer-skill-practices-synthesis`

# Conclusion Status

Concluded for `ticket:agntsys7` after direct-read synthesis across the four peer
source sets and promotion of accepted practices into existing Loom skill surfaces.
Future peer-source additions should reopen or supersede this research only if they
materially change the transfer/reject decisions recorded above.
