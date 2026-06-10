# Shaping Sessions Implementation

Status: active
Created: 2026-05-26
Updated: 2026-06-10

Legacy note: Risk — high - architecturally novel feature; new backend service, new interaction model, tight coupling between agent reasoning and UI rendering

## Summary

Implements `.loom/specs/mill-shaping-sessions.md`. The shaping session is a new Design Room
mode where the operator dumps raw thoughts, deep agents explore the codebase and
context, and records progressively materialize in a staging area through an
interactive block-based timeline—all before touching `.loom/`.

This is the highest-leverage feature in Loom Mill. It brings the Loom outer loop
into a visual, interactive workspace that didn't exist before.

## Related Records

- `.loom/specs/mill-shaping-sessions.md` - full behavioral contract (active)
- `.loom/tickets/20260526-mill-next-gen.md` - parent plan
- `loom-mill/src/loom_mill/chat/harness.py` - existing harness subprocess pattern
- `loom-mill/src/loom_mill/workstation/engine.py` - existing process lifecycle pattern
- `loom-mill/src/loom_mill/state/store.py` - event pub/sub for WebSocket streaming
- `loom-mill/src/loom_mill/chat/session.py` - existing session persistence pattern
- `loom-mill/src/loom_mill/api/design.py` - existing record creation/update flow

## Strategy

Build bottom-up in 5 tickets. Each is independently testable:

1. **Session foundation** — the shell: state model, persistence, context document,
   WebSocket events, API surface. After this, you can create sessions, append to
   the context doc, and stream events to the frontend. No intelligence yet.

2. **Harness orchestration** — the muscles: launch bounded agent invocations
   (opencode, claude, etc.) within a session, stream output, merge results into
   the context document, support parallelism and cancellation. After this, the
   engine can explore the codebase and accumulate context.

3. **Interaction block engine** — the brain: reads operator input + context doc,
   decides what to ask/observe/propose, produces typed interaction blocks through
   harness invocations. This is the core novelty. After this, the engine drives
   an actual shaping conversation.

4. **Staging area + commit flow** — the hands: draft record CRUD, branch
   management, cross-reference tracking, atomic commit to `.loom/`, durable
   session record. After this, records can be proposed, edited, branched, and
   materialized.

5. **Frontend shaping UI** — the face: timeline block renderer, staging sidebar,
   operator input, exploration indicators, proposal cards, branch tabs, commit
   flow. After this, the full experience works end-to-end.

**Dependency order:** 1 → 2 → 3 → 4 → 5 (sequential, each builds on prior).
However, ticket 5 (frontend) can start with mock/stub data before tickets 2-4 are
complete, using the session foundation events from ticket 1.

**Worker split:** Tickets 1-4 go to generalist (backend correctness, subprocess
management, agent orchestration). Ticket 5 goes to frontend-expert (visual design,
interaction quality, novel UI patterns).

**Recovery:** Each ticket adds independent value. After ticket 1+2, we have a
context-accumulating exploration engine. After 3, we have interactive shaping logic.
After 4, we have commit capability. Ticket 5 can ship progressively (timeline
first, then staging panel, then proposals, then branches).

**Coherence risk:** The interaction block engine (ticket 3) is the hardest to get
right. If the agent's reasoning quality is poor, the whole experience fails. The
mitigation is that the context document and harness orchestration give it good raw
material to work with. The prompt engineering for the "shaping agent" personality
happens inside ticket 3 and can be iterated independently.

## Execution Units

### Unit: Session Foundation + Context Document

Ticket: .loom/tickets/20260526-mill-shaping-foundation.md

The stateless shell that everything else builds on. Creates the session lifecycle,
persistence, context document management, API surface, and WebSocket event types.

Closure claim: A shaping session can be created, its context document appended to,
its state read and persisted, and structured events streamed to the frontend via
WebSocket.

### Unit: Bounded Harness Orchestration

Ticket: .loom/tickets/20260526-mill-shaping-harness.md

The subprocess engine that launches bounded agent invocations within a session.
Reuses patterns from the workstation engine and chat harness but adapted for
parallel bounded exploration with result merging.

Closure claim: The shaping engine can launch multiple bounded harness invocations
in parallel, stream their output, merge results into the session context document,
and cancel in-flight work.

### Unit: Interaction Block Engine

Ticket: .loom/tickets/20260526-mill-shaping-blocks.md

The core agent reasoning that drives the shaping conversation. Reads operator input
and the accumulated context document, then produces typed interaction blocks
(questions, observations, proposals, branch points) through harness invocations.

Closure claim: Given operator input and context, the engine produces meaningful
structured interaction blocks that advance the shaping conversation toward
materialized records.

### Unit: Staging Area + Commit Flow

Ticket: .loom/tickets/20260526-mill-shaping-staging.md

Draft record management, branch support, cross-reference tracking, and the atomic
commit flow that materializes the staged subgraph to `.loom/`.

Closure claim: Records can be proposed into a staging area, edited, branched, and
atomically committed to `.loom/` with correct cross-references and a durable
session record.

### Unit: Frontend Shaping Session UI

Ticket: .loom/tickets/20260526-mill-shaping-frontend.md

The full interactive frontend experience: timeline block renderer, staging sidebar,
operator input, exploration indicators, proposal cards, branch tabs, and commit
flow.

Closure claim: The operator can start a shaping session via "New", see the
interactive timeline of blocks building up, view the staging area, answer questions,
edit proposals, switch branches, and commit the result.

## Milestones

### Milestone: Engine Can Explore

Child tickets: .loom/tickets/20260526-mill-shaping-foundation.md, .loom/tickets/20260526-mill-shaping-harness.md

True when: A session can be created, bounded harness invocations can explore the
codebase, and results accumulate in the context document with events streaming to
any WebSocket client.

### Milestone: Engine Can Shape

Child tickets: .loom/tickets/20260526-mill-shaping-blocks.md, .loom/tickets/20260526-mill-shaping-staging.md

True when: The engine produces meaningful interaction blocks, the operator can
respond, records can be proposed and committed. The shaping conversation works
end-to-end (even if only testable via API/WebSocket, not yet via UI).

### Milestone: Full Experience

Child tickets: .loom/tickets/20260526-mill-shaping-frontend.md

True when: The entire experience works in the browser—from "New" button through
interactive shaping to commit.

## Current State

The branch contains implementation for all original child units: foundation,
harness orchestration, interaction block engine, staging/commit flow, frontend UI,
and backend audit fixes. This plan is not closed: the branch remains in review
after earlier follow-up issues across record staging, engine fail-closed behavior,
parser safety, frontend continuation/disablement state, staging refetch behavior,
and Loom ledger staleness. A newer designer adversarial frontend pass found
additional blockers: record-node resurrection on deterministic temp IDs, canvas
origin flicker from the Svelvet positioning workaround, missing immediate
advancing feedback, option/question race gaps, and repeated multiple-choice
selections creating duplicate branches. The current follow-up pass on
`feature/design-room-redesign` is addressing those frontend interaction issues;
frontend build, relevant backend shaping tests, and final adversarial-review
confirmation passed, and acceptance remains with the ticket review/acceptance gate.

## Journal

- 2026-06-10: Reconciled plan state for the designer adversarial frontend
  follow-up. The branch is addressing deterministic-temp-id resurrection, Svelvet
  origin flicker, immediate advancing feedback, option/question race gaps, and
  duplicate multiple-choice branches. Frontend build, relevant backend shaping
  tests, and final adversarial-review confirmation passed, so the plan stays active.
- 2026-06-09: Reconciled plan state with branch reality. The original five
  shaping units plus backend audit fixes exist on the branch. The nine-finding
  follow-up fixes have been implemented, adversarially reviewed, and covered by
  focused backend/frontend verification. Only intentional source, record, and test
  changes are part of the branch state.
- 2026-05-26: Marked active after implementation began on `.loom/tickets/20260526-mill-shaping-foundation.md`.
- 2026-05-26: Created plan. All design questions resolved. Infrastructure mapped.
  Ready to decompose into detailed child tickets.
