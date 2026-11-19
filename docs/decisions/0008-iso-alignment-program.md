# ADR-0008: The ISO alignment program: adaptation, not certification

- **Status:** Proposed
- **Date:** 2026-11-19
- **Persona:** 🦊 Coco (lead)
- **Scope:** org-wide

## Context

KRI standards today are house-written and house-perfect: the all-PETG
prototyping standard, the torx fastener rail, the Geometry Gate, the
append-only Tail Ledger. They work, but they speak only our dialect.
A two-round research sweep (November 2026, archived in the research
brief) mapped the international standards landscape against the forge's
actual surfaces: printing, metrology, electronics, garmenting,
documentation, planning. Strong matches exist, led by the ISO/ASTM
52900 additive series, the ISO GPS tolerancing line, ISO 1328-1 gears,
ISO 10012:2026 measurement management, and ISO 15489 records.

Constraints in play:

- ISO full texts are paywalled; drafts must not quote requirements we
  have not purchased and read.
- Several families are mid-revision in 2026 (ISO 30401, ISO 21502,
  ISO 10007, ISO 45001), so clause-precise adoption would strand us on
  old editions.
- The forge's Deterministic Numbers Law forbids importing tolerance or
  capability values from tables calibrated to other processes; values
  must come from our own bench measurement.

## Decision

1. KRI adapts external standards at the **structure level**, and
   certifies nothing. Formal certification is out of scope until the
   business side of a debut justifies otherwise, and even then it is a
   separate ADR.
2. The adoption vehicle is this ADR convention: **one ADR per standards
   family**, status Proposed at merge, flipped to Accepted only by the
   Architect's word.
3. **Values are measured, not imported.** Tolerance classes, gear
   grades, and capability claims in KRI doctrine come from
   forge-measured capability rounds (the ISO 22514 discipline), never
   copied from machining-calibrated tables.
4. Families mid-revision are adopted at **principles level**, crosswalked
   light, and re-visited when the new edition lands.
5. Full texts are purchased before requirements are quoted verbatim in
   any doctrine document; Proposed ADRs may rely on official catalogue
   scope text and honest paraphrase.
6. Existing doctrine is expressed in the new grammar where it applies;
   nothing ratified is edited. Supersede, don't edit, per the decisions
   README.

## Consequences

- Forge documents become legible to outside engineers, vendors, and
  venues; less translation, fewer blank stares.
- Cost: text purchases and slightly more ceremony per standard.
- Blast radius: all repos. Adopted ADRs should be referenced from each
  affected repo's AGENTS.md or PROJECT-STATUS (decisions README rule 4);
  that link pass is scheduled, not silent.
- Study of each new edition becomes a small standing chore; the
  principles-level rule (point 4) keeps each re-read an update, not a
  rewrite.
