# ADR-0010: GPS default tolerances: ISO 8015 principles, forge-computed classes

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** 🔨 Zaku (lead)
- **Scope:** org-wide

## Context

Every drawing that is silent about a tolerance currently relitigates
the question per conversation. The wider world solved this decades ago:
ISO 8015 (GPS fundamentals: the responsibility and independency
principles) plus ISO 2768 general tolerances, whose tolerance classes
(f/m/c/v) give unstated dimensions a declared default.

The trap: ISO 2768's class values are calibrated for machining and
molding. Our towers are FDM and nylon; importing those numbers would
violate the Deterministic Numbers Law and the Geometry Gate alike. Note
also that ISO 2768's 2026 edition was in final production during
research; its publication status must be confirmed before the edition
is cited.

## Decision

1. Every KRI drawing (or CAD note block) carries a **general
   tolerance class**, named in KRI's own table, overridable per feature:
   the structure of ISO 2768 adapted, not its machining values.
2. **Class values are computed per tower and material** from the
   capability rounds of ADR-0012, recorded in a KRI tolerance table
   document, and revised when towers or materials change.
3. ISO 8015's principles (independency, the drawing as contract,
   responsibility split between design and production) are adopted as
   the reading rules of the Geometry Gate; the Gate's law that
   a scale drawing outranks numbers stands unchanged.
4. Full-class ISO 2768 naming (e.g. class m) may be referenced for
   outside legibility, mapped to the nearest KRI-computed class, with
   the mapping stated, never implied.

## Consequences

- Dimensioning defaults stop being a conversation and become a line
  on the drawing; vendors and collaborators read us natively.
- Cost: capability rounds must actually run before any class value is
  declared; until then the table carries empty entries, marked
  "consult live source", never estimates.
- Blast radius: all repos with CAD; the Geometry Gate skill gains a
  standards-anchored reading section.
