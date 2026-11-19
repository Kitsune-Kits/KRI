# ADR-0011: Gear acceptance grammar: declare an ISO 1328-1 flank tolerance class

- **Status:** Proposed
- **Date:** 2026-11-19
- **Persona:** 🔨 Zaku (lead)
- **Scope:** org-wide

## Context

The Kogane gear line already computes real inspection numbers: center
distance, tooth thinning, span over teeth, measurement over pins, with
an acceptance proposal of plus or minus 0.06 pending the Architect's
word. What the sheets lack is a grade the outside world can read.
ISO 1328-1:2013 is the international system of flank tolerance
classification for cylindrical gears: eleven classes, lower numbers
tighter, covering pitch, profile, helix, and runout deviations, with
inspection practice codified in the ISO/TR 10064 line, exactly the
span-over-teeth and pin-measurement methods the bench already performs.

## Decision

1. Every gear acceptance sheet declares a **target flank tolerance
   class per ISO 1328-1:2013**, alongside the existing numeric
   acceptance values. The class grades the numbers; it does not
   replace them.
2. The class target for printed-nylon gears is **declared from bench
   measurement** (capability rounds per ADR-0012 applied to the gear
   inspection values), not assumed; printed polymer realistically
   lands in coarse classes, and we will name ours honestly.
3. Inspection methods remain the forge's proven span and pin
   techniques, described where useful in ISO/TR 10064 vocabulary for
   outside legibility.
4. A change of material, process, or tower re-opens the declaration;
   the class travels with the process, not with the drawing ego.

## Consequences

- Third parties reading a KRI gear sheet see an international grade,
  not a naked number; vendor/machinist conversations shorten.
- Cost: the first declaration cycle requires measured gear capability
  data, so it lands in a bench sitting, not at a desk.
- Blast radius: Project-Kogane first (gears, carrier, cam); any future
  gear work inherits the grammar.
