---
id: research:peer-engineering-discipline-deep-dive
kind: research
status: concluded
created_at: 2026-05-07T14:25:12Z
updated_at: 2026-05-07T14:42:26Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:engdisc7
  research:
    - research:agentsys-command-practices-synthesis
external_refs:
  mattpocock_skills_github: https://github.com/mattpocock/skills
  mattpocock_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/mattpocock-skills
  addyosmani_agent_skills_github: https://github.com/addyosmani/agent-skills
  addyosmani_agent_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/addyosmani-agent-skills
  superpowers_github: https://github.com/obra/superpowers
  superpowers_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/superpowers
---

# Question

What deeper engineering-discipline primitives from Matt Pocock skills, Addy
Osmani agent skills, and Superpowers should Loom bake into its skill corpus, and
which peer mechanics should Loom reject because they would create hidden runtime,
command, or non-owner truth drift?

# Why This Matters

The previous peer-practice passes added useful practices, but they still risk
being too shallow if they only name patterns. The user wants Loom to absorb the
engineering discipline itself: how agents should shape problems, slice work,
write tests, debug, verify, review, simplify, package, and learn without relying
on transcript habits or external command systems.

# Scope

This research focuses on deeper direct reads from local peer clones:

- Matt Pocock skills: engineering, productivity, handoff, TDD references,
  architecture, triage, prototype, diagnosis, glossary/ADR, and setup docs.
- Addy Osmani agent skills: engineering workflow skills, references, agents, and
  command examples where they reveal discipline rather than runtime requirements.
- Superpowers: brainstorming, plans, execution, TDD, debugging, review, finishing,
  parallel agents, subagent-driven development, writing-skills, and test fixtures
  that pressure-test skill behavior.

It excludes adopting peer command systems, hooks, installers, MCP requirements,
generated state directories, or tool-specific truth surfaces as Loom core.

# Method

- Read peer source files directly from local clones.
- Extract engineering-discipline primitives, not command names.
- Compare each primitive against Loom's owner-layer model and existing skill
  surfaces.
- Promote accepted primitives into the existing skill that owns the behavior.
- Record rejected mechanics and null results so future agents do not rediscover
  the same boundary.

# Sources

Peer source paths are cited relative to the local clones named in `external_refs`.

Observed peer source state on 2026-05-07:

- `mattpocock-skills` local clone HEAD:
  `70141119e9fe47430b62b93bcf166a73e6580048`
- `addyosmani-agent-skills` local clone HEAD:
  `742dca58ae557bc67afec9ea8e6de59c085f0534`
- `superpowers` local clone HEAD:
  `f2cbfbefebbfef77321e4c9abc9e949826bea9d7`

Matt Pocock skills direct reads:

- `mattpocock-skills:skills/engineering/tdd/SKILL.md:18-30,62-99` - rejects horizontal all-tests-then-all-code TDD and teaches one-test/one-implementation tracer bullets with refactor only after green.
- `mattpocock-skills:skills/engineering/tdd/tests.md:5-24,38-61` - defines behavior-first tests through public interfaces and flags implementation-detail tests.
- `mattpocock-skills:skills/engineering/diagnose/SKILL.md:12-51,65-117` - makes the feedback loop the core of debugging, requires ranked falsifiable hypotheses, correct regression seam, cleanup, and architecture handoff after the fix.
- `mattpocock-skills:skills/engineering/improve-codebase-architecture/SKILL.md:23-60` and `DEEPENING.md:27-37` - teaches module/interface/seam/adapter vocabulary, deletion tests, two-adapter seam discipline, and interface-as-test-surface.
- `mattpocock-skills:skills/engineering/grill-with-docs/SKILL.md:8-13,56-86` - asks one question at a time, inspects code before asking when possible, surfaces terminology conflicts, and records ADRs only for hard-to-reverse, surprising, tradeoff-backed decisions.
- `mattpocock-skills:skills/engineering/prototype/SKILL.md:8-30` - treats prototypes as throwaway question-answering artifacts whose durable output is the answer, not the prototype code.
- `mattpocock-skills:skills/engineering/to-issues/SKILL.md:22-83` - decomposes plans into tracer-bullet vertical slices, shows AFK/HITL readiness, and forbids parent issue mutation during child issue creation.
- `mattpocock-skills:skills/engineering/triage/OUT-OF-SCOPE.md:3-7,70-101` - preserves durable rejected enhancement reasoning for deduplication and reconsideration.
- `mattpocock-skills:docs/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md:3-10` - distinguishes hard dependencies that make output wrong without setup from soft dependencies that merely sharpen output.

Addy Osmani agent skills direct reads:

- `addyosmani-agent-skills:skills/spec-driven-development/SKILL.md:22-50,51-80,117-163,165-200` - gates spec/plan/task/implementation, surfaces assumptions first, defines boundary tiers, reframes vague goals as testable success criteria, and keeps specs alive.
- `addyosmani-agent-skills:skills/source-driven-development/SKILL.md:38-120,122-160` - detects dependency versions, fetches authoritative docs, surfaces doc/code conflicts, and cites unverified patterns honestly.
- `addyosmani-agent-skills:skills/planning-and-task-breakdown/SKILL.md:24-33,57-77,106-142,188-195` - plans read-only, slices vertically, orders by dependency and risk, and marks safe parallelism only when contracts are clear.
- `addyosmani-agent-skills:skills/incremental-implementation/SKILL.md:21-43,91-145,199-222` - builds thin increments, prefers simplicity, enforces scope discipline, one logical change, working state, and no repeated reassurance runs.
- `addyosmani-agent-skills:skills/test-driven-development/SKILL.md:35-80,82-103,174-232,298-325,329-383` - requires red/green/refactor, prove-it bug tests, state-not-interaction tests, browser runtime evidence, optional independent test-writing subagents, and no repeated test commands without source changes.
- `addyosmani-agent-skills:skills/debugging-and-error-recovery/SKILL.md:21-36,40-152,243-280` - stops feature work on failure, preserves evidence, reproduces/localizes/reduces, adds and removes instrumentation, and treats error output as untrusted data.
- `addyosmani-agent-skills:skills/code-review-and-quality/SKILL.md:22-84,118-180,207-267,318-347` - reviews correctness, simplicity, architecture, security, and performance; reviews tests first; categorizes feedback by severity; checks dependency risk.
- `addyosmani-agent-skills:skills/performance-optimization/SKILL.md:30-38,40-120,292-350` - requires baseline measurement, bottleneck identification, after measurement, budgets, and CI/monitoring guards.
- `addyosmani-agent-skills:skills/security-and-hardening/SKILL.md:21-53,216-241,263-349` - defines always/ask-first/never security boundaries, vulnerability triage, secret hygiene, and security verification.
- `addyosmani-agent-skills:skills/shipping-and-launch/SKILL.md:20-76,77-161,225-265` - packages pre-launch checks, staged rollout, feature flags, monitoring, rollback triggers, and post-launch verification.
- `addyosmani-agent-skills:skills/documentation-and-adrs/SKILL.md:23-91,92-140,190-248` - writes ADRs for significant decisions, comments the why, maintains README/changelog/API docs, and treats agent docs as future context.
- `addyosmani-agent-skills:skills/git-workflow-and-versioning/SKILL.md:34-119,147-209` - uses commits as save points, keeps concerns separate, sizes changes, isolates parallel work with worktrees, and reports intentional non-touches.
- `addyosmani-agent-skills:skills/deprecation-and-migration/SKILL.md:37-118,164-206` - requires replacement before deprecation, incremental migration, zero-usage verification, and zombie-code disposition.
- `addyosmani-agent-skills:skills/api-and-interface-design/SKILL.md:20-39,61-125` - applies Hyrum's Law, contract-first design, consistent errors, boundary validation, and additive compatibility.
- `addyosmani-agent-skills:skills/context-engineering/SKILL.md:20-36,88-104,196-251` - structures persistent/spec/source/error/conversation context, reads target files/tests/examples before editing, treats loaded context by trust level, and surfaces conflicts.

Superpowers direct reads:

- `superpowers:skills/test-driven-development/SKILL.md:31-45,113-183,206-240` - states the strongest form of test-first discipline, mandatory verify-red/verify-green, and rationalization handling.
- `superpowers:skills/systematic-debugging/SKILL.md:16-23,50-121,145-213,215-240` - forbids fixes without root cause, requires evidence gathering across component boundaries, one-variable hypothesis tests, and architecture escalation after repeated failed fixes.
- `superpowers:skills/verification-before-completion/SKILL.md:16-38,40-74,84-106,117-139` - defines evidence-before-claims as a gate: identify, run, read, verify, then claim.
- `superpowers:skills/requesting-code-review/SKILL.md:12-47,75-103` - requests review at checkpoints, fixes important findings before continuation, and pushes back with evidence when reviewers are wrong.
- `superpowers:skills/receiving-code-review/SKILL.md:14-25,40-84,100-129,164-174` - reads, understands, verifies, evaluates, then implements feedback one item at a time; unclear feedback blocks partial implementation.
- `superpowers:skills/executing-plans/SKILL.md:18-47` - critically reviews a written plan before execution and stops on blockers instead of guessing.
- `superpowers:skills/finishing-a-development-branch/SKILL.md:18-39,40-94,95-193,203-251` - verifies tests before options, detects environment, presents merge/PR/keep/discard choices, and protects worktree cleanup by provenance.
- `superpowers:skills/subagent-driven-development/SKILL.md:8-14,42-87,104-120,223-261` - uses fresh implementers plus spec-compliance then code-quality review, handles blocked subagents, and forbids skipping review loops.
- `superpowers:skills/writing-plans/SKILL.md:21-34,36-44,106-132` - maps file responsibilities, writes bite-sized TDD steps, forbids placeholders, and self-reviews plan/spec coverage.
- `superpowers:skills/writing-skills/SKILL.md:10-18,30-45,140-180` - treats skill writing as process TDD, emphasizes pressure scenarios, and warns that descriptions must not summarize workflows or agents may skip the body.

# Variant / Experiment Matrix

| Variant / hypothesis | Artifact or probe | Strength | Weakness | Decision |
| --- | --- | --- | --- | --- |
| Make small incremental wording edits only | Prior ticket outcomes and user feedback | Low risk | Fails the user's explicit request for deeper ownership | Rejected |
| Import peer skills as new Loom skills wholesale | Peer skill directories | Captures detail quickly | Duplicates owner layers and imports command/runtime assumptions | Rejected |
| Extract discipline primitives into existing Loom owners | Direct reads plus current Loom skills | Preserves Loom truth model while improving engineering rigor | Requires broad coordinated skill edits and critique | Chosen |
| Add a new engineering-discipline omnibus skill | Cross-cutting source practices | Easy activation story | Risks shadowing tickets, Ralph, debugging, critique, evidence, and ship | Rejected unless later critique proves a narrow missing boundary |

# Evidence Synthesis

The transferable primitives fit Loom best when each is routed to the owner layer
that already owns the relevant truth.

## Problem shaping, specs, and plans

- Adopt problem pressure before execution: Matt's `grill-with-docs`, Addy's
  spec-driven assumptions, and Superpowers planning all penalize silent invention.
  Loom should keep this in workspace/spec/plan guidance, not in chat rituals.
- Adopt divergent/convergent shaping: candidate approaches, not-doing lists,
  boundary tiers, and decision capture thresholds reduce premature solution
  attachment. Loom should route intended behavior to specs, sequencing to plans,
  durable policy to constitution, and reusable explanation to wiki.
- Adapt human gates: peer skills often require explicit human approval before each
  phase. Loom should instead ask only when authority, risk, or ambiguity requires
  operator judgment; low-risk reversible assumptions can proceed when recorded in
  the owner layer.
- Adopt vertical/tracer-bullet slicing: each plan ticket should cut through the
  real interface/behavior/evidence path when possible, be independently
  verifiable, and stay small enough for local execution or Ralph.

## Execution and TDD

- Adopt one-test/one-implementation discipline: Matt and Superpowers both reject
  all-tests-then-all-code. Loom's `test-first` posture should keep red/green
  evidence at packet/iteration level and encourage behavior tests through public
  interfaces.
- Adopt source-driven implementation: Addy's source-driven and context-engineering
  skills strengthen Loom's packet/local execution guidance by requiring dependency
  versions, official docs or project examples for framework-specific patterns, and
  explicit conflict handling when docs and code disagree.
- Adapt commit-per-slice: commits are valuable save points, but Loom must not
  require commits because commits are a Git transport choice and the operator may
  not request them. The Loom-native equivalent is one logical mutation plus fresh
  evidence and ticket reconciliation.
- Adopt scope discipline: adjacent cleanup, refactors, feature work, dependency
  changes, and formatting should stay separate unless the ticket explicitly owns
  the bundle.

## Debugging and performance

- Adopt feedback-loop-first debugging: all three peer corpora converge on
  reproduce/observe before fix. Loom already has `loom-debugging`; deepen it with
  explicit instrumentation hygiene, correct-seam findings, and architecture
  escalation after repeated failed fixes.
- Adopt ranked falsifiable hypotheses and one variable per probe: this belongs in
  debugging and research, with observations preserved as evidence when acceptance
  or critique will rely on them.
- Adopt performance-as-measurement: no performance claim without baseline, target,
  bottleneck, changed variable, after measurement, and limitations.

## Critique and review feedback

- Adopt multi-axis review: Addy's five-axis review and Superpowers' two-stage
  spec-then-quality review map directly onto Loom critique profiles and pass
  splitting.
- Adopt review of verification before implementation detail: tests, evidence,
  screenshots, performance numbers, and before/after artifacts show what the
  author thinks changed; critique should inspect them before implementation shape.
- Adopt review feedback reception discipline: review comments are claims to read,
  understand, verify, classify, implement one item at a time, push back on with
  evidence when wrong, and disposition through the ticket when they affect closure.
- Adopt AI-artifact cleanup: temporary logs, no-op variables, speculative helpers,
  stale comments, TODOs, debug prefixes, and over-engineering need explicit review
  because AI-generated code tends to leave plausible debris.

## Evidence, tickets, and acceptance

- Adopt evidence-before-claims as a gate: identify what proves the claim, run or
  inspect it fresh enough for the current source state, read the output/exit code,
  compare expected and actual, then state only the supported claim.
- Adopt no repeated reassurance runs: rerunning an unchanged successful command is
  not fresher evidence. Re-run after source, records, dependencies, environment,
  or procedure change, or when the original observation was incomplete.
- Keep ticket-owned evidence sufficiency: peer skills sometimes let commands or
  reviewers decide completion. Loom must keep closure in the ticket acceptance
  gate with evidence/critique disposition.

## Codemap, research, wiki, and shared language

- Adopt deterministic orientation before editing: inspect target files, related
  tests, source examples, contracts, dependency files, and prior owner records
  before implementing patterns from memory.
- Adopt shared language conflict handling: Matt's glossary/ADR approach and Addy's
  context conflict handling map to Loom wiki/shared-language, spec, research, and
  ticket blockers, depending on which truth changed.
- Adapt out-of-scope knowledge bases as research/wiki patterns: rejected options
  and null results should live in research, constitution decisions, wiki, or
  tickets; Loom should not add a separate `.out-of-scope/` canonical layer.

## Ship, retrospective, and lifecycle

- Adopt optionized finishing: verify first, inspect Git/worktree state, then offer
  safe merge/PR/keep/abandon options. Loom already routes this through `loom-ship`
  and `loom-git`; deepen launch/rollback packaging and cleanup provenance.
- Adopt feature flag and staged rollout metadata as shipping facts, not closure:
  flag owner, expiry, rollout thresholds, monitoring, rollback triggers, and docs
  sync belong in ship/evidence/ticket/plan records as appropriate.
- Adopt deprecation/migration as lifecycle discipline: replacement, usage evidence,
  migration guide, zero-usage verification, and zombie-code disposition should
  route through plans, tickets, evidence, ship, and retrospective.

# Rejected Options

- Copy peer command systems, hooks, installers, or hard-coded folder conventions:
  rejected because Loom behavior belongs in Markdown-native skills and owner
  records, not hidden runtimes or command adapters.
- Add a new omnibus engineering-discipline skill: rejected for this tranche because
  it would shadow `loom-specs`, `loom-plans`, `loom-ralph`, `loom-debugging`,
  `loom-critique`, `loom-evidence`, `loom-ship`, and `loom-retrospective`.
- Import hard human approval gates: rejected as default protocol because Loom's
  authority model asks when material judgment is unsafe to infer, while allowing
  bounded autonomous progress when assumptions are low-risk, reversible, and
  recorded.
- Require commits after every increment: rejected because commits are valuable
  save points but not Loom truth, and operators may not have asked for commits.
- Require MCPs, DevTools, subagents, or model-specific worktree directories:
  rejected as protocol requirements. They can be useful transports or evidence
  mechanisms, but Loom must remain harness-neutral.
- Promote `.out-of-scope/`, PR descriptions, generated plans, command wrappers, or
  tracker labels into Loom owner layers: rejected because rejected options,
  shipping summaries, live execution, and acceptance already have owners.

# Null Results

- The direct reads did not justify a hidden validation runtime or new CLI layer for
  enforcing engineering discipline; the peer value is procedural guidance plus
  evidence/critique, not mandatory automation.
- The direct reads did not justify a fixed question cap for grilling/problem
  shaping; the shared pattern is one material question at a time, not a numeric
  limit.
- The direct reads did not justify making browser DevTools, Context7, or MCP setup
  a Loom prerequisite; they are optional evidence/context transports when present.
- The direct reads did not justify copying peer skill file layouts or plan storage
  paths; Loom's `skills/` layout, `.loom` records, and packet templates already own
  those shapes.

# Conclusions

- Loom should deepen existing owner/workflow skills rather than add another layer.
  The strongest peer practices all become clearer when routed through Loom's
  current owners: specs for intended behavior, plans for sequencing, tickets for
  live execution and acceptance, Ralph/local execution for bounded mutation,
  debugging for reproduce-first repair, evidence for observations, critique for
  review, wiki for accepted explanation, ship for packaging, and retrospective for
  prevention.
- The highest-value transfer is anti-rationalization discipline: no coding through
  ambiguity, no tests after implementation masquerading as TDD, no fixes without
  root cause, no completion claims without fresh evidence, no review feedback
  implemented blindly, no shipping package stronger than owner records.
- The main boundary to protect is command/runtime drift. Peer systems often encode
  useful discipline in commands, hooks, subagent routes, hard-coded folders, and
  issue tracker labels. Loom should absorb the discipline while rejecting those
  mechanics as canonical truth.

# Recommendations

Update existing skills and templates in this tranche:

- `loom-workspace` and `loom-specs`: strengthen problem pressure, options/not-doing,
  boundary tiers, interface contracts, one-question/codebase-first clarification,
  and ADR/decision thresholds.
- `loom-plans`, `loom-tickets`, and `loom-ralph`: strengthen vertical slices,
  one-logical-change discipline, source-driven context, behavior-first test shape,
  explicit write boundaries, and local/Ralph escalation triggers.
- `loom-debugging`: add instrumentation cleanup, untrusted error-output handling,
  correct-seam findings, architecture escalation after repeated failed fixes, and
  performance measurement discipline.
- `loom-critique`: deepen multi-axis review, tests/evidence-first review order,
  spec-compliance-before-quality pass splitting, dependency/security/performance
  lenses, AI-artifact cleanup, and review feedback disposition.
- `loom-evidence` and ticket acceptance guidance: make evidence-before-claims and
  no-reassurance-reruns explicit at the claim gate.
- `loom-codemap`, `loom-research`, and `loom-wiki`: strengthen deterministic
  source orientation, source quality/freshness hierarchy, conflict handling, and
  shared-language promotion.
- `loom-ship`, `loom-git`, and `loom-retrospective`: strengthen optionized
  finishing, launch/rollback packaging, docs sync, feature-flag lifecycle,
  deprecation/migration cleanup, and prevention-artifact promotion.

# Open Questions

- None blocking. Prefer reshaping existing references and templates. Add a new
  reference only if an owner skill lacks a coherent place for the discipline.

# Linked Work

- `ticket:engdisc7`
- `ticket:agntsys7`
