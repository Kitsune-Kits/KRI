# ADR-0019: Conformity decision rules: ISO 14253-1 guard bands at the tolerance edge

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** 🔨 Zaku (lead), ⚡ Piko (instrument uncertainty)
- **Scope:** org-wide

## Context

ADR-0012 made the instruments trustworthy and ADR-0010 declared the
tolerances, but the pack left one seam open: what happens when a
measured value sits near a tolerance edge. Today that verdict is bench
instinct. The Kogane gear sheet's plus-or-minus 0.06 acceptance already
courts the question; every future class check will too.

ISO 14253-1:2017 supplies the international answer: decision rules for
verifying conformity or nonconformity by measurement. Its core move is
the guard band: measurement uncertainty carves an inconclusive zone at
each tolerance edge, so a result is proven conforming, proven
nonconforming, or neither.

## Decision

1. Every KRI acceptance sheet declares its **decision rule**. The
   default is the ISO 14253-1 structure: the acceptance zone is reduced
   by the measurement uncertainty of the checking instrument, so a
   measurement only proves conformity when its uncertainty zone fits
   inside the tolerance.
2. Three verdicts are legal in the bench log: **Accepted**,
   **Rejected**, and **Inconclusive**, the reduced-zone cases.
   Inconclusive triggers re-measurement with a better instrument or a
   documented engineering judgment; it never silently becomes a pass.
3. The uncertainty figure for each instrument comes from the ADR-0012
   check record; an instrument without a fitness statement produces no
   guarded verdicts at all.
4. A purchased text comes before quoting 14253-1 requirements verbatim,
   per ADR-0008 point 5; the Proposed text adapts the published
   decision-rule structure.

## Consequences

- Verdicts on dimensional acceptance become traceable and rule-governed
  instead of mood-governed; borderline parts cost bench time instead of
  arguments.
- Cost: honest inconclusives will occasionally delay a build.
- Blast radius: feeds ADR-0010 class checks, ADR-0011 gear acceptance,
  and ADR-0018 fit declarations; all repos with acceptance sheets.
