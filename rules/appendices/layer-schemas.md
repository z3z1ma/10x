# Appendix B — Layer Schemas

## Constitution

### Main constitution

Required sections:

- Vision
- Principles
- Constraints
- Strategic Direction
- Current Focus
- Open Constitutional Questions
- Change History

Section intent:

- `Vision`: the durable statement of what the project is trying to become
- `Principles`: the rules of judgment that should still hold across implementation changes
- `Constraints`: the important limitations or non-negotiable boundaries
- `Strategic Direction`: the current architectural or strategic path
- `Current Focus`: what the project is concentrating on right now
- `Open Constitutional Questions`: unresolved questions that affect the long-term operating model
- `Change History`: durable record of major constitutional changes

### Decision records

Required sections:

- Decision
- Why This Decision Exists
- Alternatives Considered
- Consequences
- Supersession

Section intent:

- `Decision`: the durable policy or architectural choice in plain language
- `Why This Decision Exists`: why this choice matters now and what pressure led to it
- `Alternatives Considered`: the rejected or deferred options that should remain visible later
- `Consequences`: what downstream records, workflows, or design choices are constrained by this decision
- `Supersession`: whether the decision replaces, narrows, or leaves open earlier assumptions

### Roadmap records

Required sections:

- Strategic Theme
- Why Now
- Focus Areas
- Milestones
- Sequencing Assumptions
- Downstream Work
- Status Summary

Section intent:

- `Strategic Theme`: the durable direction the roadmap is organizing
- `Why Now`: why the roadmap matters in the current stage of the repository
- `Focus Areas`: the main surfaces or workstreams the roadmap is steering
- `Milestones`: meaningful checkpoints that show the direction becoming real
- `Sequencing Assumptions`: the ordering logic and strategic dependencies behind the roadmap
- `Downstream Work`: what initiatives, specs, plans, tickets, or research should exist beneath it
- `Status Summary`: the current truthful state of the roadmap without becoming a live execution log

## Research

Required sections:

- Question
- Objective
- Scope
- Non-goals
- Methodology
- Hypotheses
- Evidence
- Experiments
- Rejected Paths
- Conclusions
- Recommendations
- Open Questions
- Linked Downstream Artifacts

Section intent:

- `Question`: the specific question the research set out to answer
- `Objective`: what useful outcome the research was supposed to produce
- `Scope`: what the research did cover
- `Non-goals`: what the research intentionally left out
- `Methodology`: how the investigation was performed
- `Hypotheses`: what ideas were tested or compared
- `Evidence`: what facts, observations, or source material were gathered
- `Experiments`: what concrete tests were run
- `Rejected Paths`: what approaches were considered and dropped
- `Conclusions`: what the evidence supports now
- `Recommendations`: what downstream work should do with the findings
- `Open Questions`: what still remains unresolved
- `Linked Downstream Artifacts`: which specs, plans, or tickets depend on this research

## Initiatives

Required sections:

- Objective
- Why Now
- In Scope
- Out of Scope
- Success Metrics
- Milestones
- Dependencies
- Risks
- Linked Specs, Plans, and Tickets
- Status Summary

Section intent:

- `Objective`: the strategic outcome being pursued
- `Why Now`: why the initiative matters in the current sequence of work
- `In Scope`: what strategic surface this initiative owns
- `Out of Scope`: what it intentionally does not own
- `Success Metrics`: how success should be judged
- `Milestones`: meaningful checkpoints toward the outcome
- `Dependencies`: the major prerequisites or related workstreams
- `Risks`: strategic threats to success
- `Linked Specs, Plans, and Tickets`: the downstream execution graph
- `Status Summary`: concise current state of the initiative

## Specs

Required sections:

- Summary
- Problem Framing
- Desired Behavior
- Constraints
- Capabilities
- Requirements
- Scenarios
- Acceptance
- Design Notes
- Open Questions

Section intent:

- `Summary`: one durable statement of the behavior being specified
- `Problem Framing`: why the spec exists and what problem it addresses
- `Desired Behavior`: the user-visible or system-visible behavior the spec wants
- `Constraints`: limits the implementation must respect
- `Capabilities`: what the system should be able to do
- `Requirements`: explicit, testable requirements
- `Scenarios`: representative situations that exercise the requirements
- `Acceptance`: what evidence or observed behavior will count as success
- `Design Notes`: informative implementation or architectural notes that help interpretation
- `Open Questions`: unresolved design questions that still affect the behavior contract

## Plans

Required sections:

- Purpose / Big Picture
- Progress
- Surprises & Discoveries
- Decision Log
- Outcomes & Retrospective
- Context and Orientation
- Milestones
- Plan of Work
- Concrete Steps
- Validation and Acceptance
- Idempotence and Recovery
- Artifacts and Notes
- Interfaces and Dependencies
- Linked Tickets
- Risks and Open Questions
- Revision Notes

Section intent:

- `Purpose / Big Picture`: why the plan exists and what larger goal it serves
- `Progress`: current state of execution against the plan
- `Surprises & Discoveries`: important learnings that changed planning assumptions
- `Decision Log`: planning decisions that should remain visible later
- `Outcomes & Retrospective`: what happened and what should be learned from it
- `Context and Orientation`: information a fresh agent needs to interpret the plan
- `Milestones`: major checkpoints in the execution path
- `Plan of Work`: overall execution strategy
- `Concrete Steps`: the current specific action sequence
- `Validation and Acceptance`: how the plan expects work to be verified and accepted
- `Idempotence and Recovery`: how the work can be safely resumed or retried
- `Artifacts and Notes`: supporting references and important operational notes
- `Interfaces and Dependencies`: major system boundaries or upstream/downstream constraints
- `Linked Tickets`: the execution ledger items that realize the plan
- `Risks and Open Questions`: current planning uncertainty and risk
- `Revision Notes`: durable notes about material plan edits

Writing standard:

- write plans as living, self-contained strategy documents
- assume the reader is a novice to the repository
- explain why the strategy is shaped this way, not just what the next step list is
- keep current execution technical details in linked tickets rather than duplicating it here

## Tickets

Required sections:

- Summary
- Context
- Why This Work Matters Now
- Scope
- Non-goals
- Acceptance Criteria
- Implementation Plan
- Dependencies
- Risks / Edge Cases
- Verification
- Documentation Disposition
- Journal

Section intent:

- `Summary`: the durable name of the execution work item
- `Context`: execution-relevant background
- `Why This Work Matters Now`: why the ticket should be worked now rather than later
- `Scope`: the current execution boundary
- `Non-goals`: nearby work the ticket should not quietly absorb
- `Acceptance Criteria`: the closure bar
- `Implementation Plan`: the current expected path through the work
- `Dependencies`: what must exist or finish first
- `Risks / Edge Cases`: known failure modes, complexity, or caution areas
- `Verification`: what evidence is required or already exists
- `Documentation Disposition`: whether explanation work is required and in what form
- `Journal`: a durable append-only-ish narrative of meaningful execution changes

Writing standard:

- write tickets as self-contained units of execution
- assume a novice should be able to pick up the ticket and continue the work safely
- include enough context, direction, constraints, and verification framing that the next actor does not have to guess the intended path
- keep tickets concrete, current, and truthful rather than terse or aspirational

## Critique

Required sections:

- Target Under Review
- Review Question
- Focus Areas
- Relevant Context
- Evidence Reviewed
- Verdict
- Residual Risks
- Follow-up Tickets
- Findings Summary

Section intent:

- `Target Under Review`: the exact object of review
- `Review Question`: the question the critique answers
- `Focus Areas`: the review dimensions the reader should keep in mind
- `Relevant Context`: only the context needed to interpret the findings
- `Evidence Reviewed`: what was actually examined
- `Verdict`: the concise top-line review outcome
- `Residual Risks`: what still remains risky or uncertain after review
- `Follow-up Tickets`: execution work created or affected by the critique
- `Findings Summary`: the concrete issues the reader should act on

## Docs

Required sections:

- Overview
- Audience
- Problem Framing
- Accepted System Shape
- Workflow / Operations Details
- Rationale
- Examples
- Verification Source
- Related Artifacts
- Supersession / History

Section intent:

- `Overview`: what this document is about
- `Audience`: who the document is for
- `Problem Framing`: why this explanation exists
- `Accepted System Shape`: the accepted behavior or architecture the document explains
- `Workflow / Operations Details`: how the reader should actually use or operate the system
- `Rationale`: why the accepted shape works this way
- `Examples`: make the explanation concrete
- `Verification Source`: what evidence supports the claims
- `Related Artifacts`: nearby specs, plans, tickets, or records the reader may need
- `Supersession / History`: how this document relates to earlier or later docs

## Verification

Required sections:

- Summary
- Command
- Evidence
- Outcome
- Related Artifacts

Section intent:

- `Summary`: what was verified
- `Command`: what was actually run or executed
- `Evidence`: the observed outputs, artifacts, or checks that justify the verification claim
- `Outcome`: the durable verdict of the verification effort
- `Related Artifacts`: records or packets that depend on this evidence

## Packet

Packets use frontmatter-heavy structure plus body sections for:

- Objective
- Completion Contract
- Constraints and Non-goals
- Trust Boundary
- Scope and Environment Notes
- Source Refs
- Embedded Source Material
- Current Execution State
- Verification Expectations
- Stop Rules and Escalation Guidance

Section intent:

- `Objective`: what the child should accomplish in this bounded run
- `Completion Contract`: what the child must return for the parent to evaluate success
- `Constraints and Non-goals`: the deliberate boundary of the run
- `Trust Boundary`: how the child should interpret authority and write limits
- `Scope and Environment Notes`: repository, worktree, and environment context
- `Source Refs`: the authoritative records or artifacts included in the packet contract
- `Embedded Source Material`: the actual embedded context for hermetic or excerpted packets
- `Current Execution State`: the relevant current-state summary for the child
- `Verification Expectations`: what evidence the child should produce or report
- `Stop Rules and Escalation Guidance`: when the child should stop, block, or escalate instead of improvising
