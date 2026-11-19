# ADR-0016: Quality plan template: the bench round's published shape

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** 🦊 Coco (lead), 🔨 Zaku (bench acceptance)
- **Scope:** org-wide

## Context

Bench rounds already have a de facto shape: a goal, a pass/fail line,
capture artifacts, and a verdict recorded in the bench log. Debut
readiness will need the same shape at higher stakes. ISO 10005:2018
(quality plans) is the small, focused international standard for a
per-project plan of controls, inspections, and acceptance criteria:
which check, applied to what, judged how, by whom. Of everything in
the second research round, it is the closest match to paper we already
write by hand.

## Decision

1. A KRI **quality plan template** is drafted into the hub
   (docs/standards/quality-plan.md), structured on ISO 10005:
   scope, referenced documents, controls and acceptance criteria per
   deliverable, measurement and inspection steps, responsibilities,
   and the record each check leaves behind.
2. Every bench round runs as a filled quality plan instance: the
   paste-ready bench prompts gain a one-page plan header rather than
   a new bureaucracy.
3. Debut readiness (starting with MomoCon 2027) runs on the same
   template at project scale; the word "prototype" on a sheet does not
   exempt the debuting artifact.
4. Configuration management (ISO 10007) is noted and deferred to the
   pending release-baseline ruling; naming a Vessel revision to an
   exact commit belongs to that decision.

## Consequences

- Bench verdicts become comparable across rounds and repos; the
  debut gate becomes a filled template, not a mood.
- Cost: one template, one page per round, and Zaku's acceptance sheets
  migrate once.
- Blast radius: bench workflow org-wide; Kogane and Lantern Vigil
  first at project scale.
