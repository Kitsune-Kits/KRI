# ADR-0012: Measurement management: instrument fitness and capability rounds

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** 🔨 Zaku (lead), ⚡ Piko (bench instruments)
- **Scope:** org-wide

## Context

Round one declared what drawings mean (ADR-0010); this decision makes
the instruments and processes that prove them trustworthy. ISO 10012
was republished in 2026 as a second edition, restructured to align with
the ISO 9001 harmonized structure, with one objective: measurements
used in design, production, testing, and monitoring must be fit for
purpose. Its companions: ISO 22514-2:2026 (process capability,
time-dependent models) and the ISO 7870 control charts series, which
turn repeated measurement into defensible capability statements.
ISO/IEC 17025 governs lab accreditation and is deliberately not
adopted; we use its vocabulary when judging outside calibration
vendors.

## Decision

1. The bench adopts **instrument check records**: every measuring
   instrument in forge service (calipers, pin gauges, feeler gauges)
   has a check record and a current fitness statement; measurements
   from unchecked instruments do not gate designs. The instrument set
   is inventoried alongside the Silo materials.
2. **Capability rounds** per ISO 22514-2 discipline: a controlled
   artifact per tower and material, measured repeatedly, producing
   capability numbers and control limits that feed ADR-0010's class
   values and ADR-0011's gear-class declaration.
3. Where the forge cannot trace a check internally, outside services
   are judged using ISO/IEC 17025 vocabulary; no adoption of the lab
   standard itself.
4. All of this records to the bench log; a failed or drifting
   instrument leaves its field empty until restored, per the
   Deterministic Numbers Law.

## Consequences

- The numbers that gate designs become traceable to fit instruments;
  capability claims become repeatable evidence.
- Cost: initial check of the instrument set, then a light periodic
  discipline; capability rounds cost bench time per tower/material.
- Blast radius: all repos whose parts are measured; the bench
  contract's capture rounds gain an instrument line.
