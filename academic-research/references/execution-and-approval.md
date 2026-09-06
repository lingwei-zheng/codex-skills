# Execution and Approval Scope

Use this Codex adaptation when interpreting internal phase boundaries,
checkpoint rules, or workflow routing. It clarifies scope and approval reuse;
it does not remove explicit approval requirements or scientific integrity gates.

## Phase completion and task completion

A phase role produces only its assigned deliverables and returns control to
the main agent. In Codex, roles may be executed inline: returning control does
not end the user's task. The main agent resumes orchestration and executes the
next authorized role, observing applicable checkpoints. It does not ask the user
to invoke each role manually. If only one phase was requested, finish at that
deliverable; do not expand it into a full pipeline.

Keep role-specific write boundaries, reviewer read-only rules, independent
verification requirements, and scientific specifications intact. A role must
not imitate an independent reviewer to satisfy its own gate. Use the available
authorized execution mechanism; do not require a Claude runtime or subagent
merely because an upstream file calls a phase an agent.

## Applicable checkpoints and approval reuse

- Select the requested mode first. Full-pipeline checkpoints govern the stages
  actually entered; standalone modes do not inherit unrelated stages or intake
  fields. Keep approval requirements belonging to the selected mode, including
  configuration, outline, revision-roadmap, integrity, and finalization gates.
- At each applicable checkpoint, identify the decision, artifact or configuration,
  version, and scope. Reuse an explicit approval only for that same decision on
  the same unchanged object/version and scope. A material change requires renewed
  approval. Approval of an outline is not approval of the later manuscript.
- The inner and outer workflows must not ask twice for the same approval. Record
  the user's decision in existing conversation/state notes; no extra manifest is
  required. Do not count reused approval as another user response.
- Silence, elapsed time, repeated previous approvals, and a general request to
  finish the task are not approval of a new gated decision. A failed integrity
  check remains failed even when some other object has been approved.
- Prepare the concrete reviewable result and other authorized independent work
  before asking. Pending approval blocks dependent actions only. Do not execute
  dependent future stages before their approval or verification prerequisites.

## Checkpoint presentation

MANDATORY takes precedence at integrity boundaries, review decisions, and
finalization. Otherwise the first checkpoint is FULL; later non-critical
checkpoints may use SLIM after two consecutive continue responses or an explicit
request for concise prompts. After four consecutive continue responses, use FULL
for a non-critical checkpoint. An awareness prompt never downgrades MANDATORY.

SLIM is a shorter presentation, not automatic approval. Both FULL and SLIM still
require explicit approval unless the identical decision was already approved.
"Just continue" or "fully automatic" does not waive subsequent approval gates.

## Completion

Report the requested deliverable as complete only when it is delivered and the
applicable verification is done. Distinguish delivered work, pending approval,
and blocked work. A phase report, alternative file format, or instructions for
the user to finish are not a substitute for the requested final artifact.

## Routine faults and recovery

Within the authorized task and execution permissions, diagnose and repair routine
implementation faults such as a wrong local path, a missing output directory,
or a conversion-script error, then validate the repair. Retry only an inexpensive,
local operation whose earlier outcome is known and whose effects will not be
duplicated. Do not loop on an unchanged failure; stop the affected operation when
a remedy needs new permission, changes scope, or has no supported next step.

This does not authorize restarting a crashed experiment, killing a running
process, changing scientific parameters, repeating paid or external mutations,
installing software, or bypassing integrity gates. Keep those existing approvals.
While a restart decision is pending, analyze logs and prepare the repair or other
independent work already authorized.

## Preparation for requested output formats

Use the requested formats and existing configuration; do not ask again for known
format or citation-style choices. Prepare source cleanup within the authorized
formatting scope, dependency and asset checks, and layout checks before requesting
the applicable final approval. Ask about LaTeX only if requested or needed for the
chosen build and a material choice remains unresolved. An internal LaTeX build
does not require a separate preference question when the user requested PDF and
the existing workflow already specifies that build route.

Keep final content approval, provenance refusal rules, and applicable verification
prerequisites. Do not emit a gated final artifact early, silently rewrite scientific
content, or relabel an artifact as a draft to bypass its final-output gate. A new
draft-export exception has not been authorized. Preparation may continue while
approval is pending only where it does not depend on that approval.
