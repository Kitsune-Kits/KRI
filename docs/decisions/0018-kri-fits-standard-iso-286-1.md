# ADR-0018: KRI fits standard: ISO 286-1 grammar, forge-computed interference

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** 🔨 Zaku (lead)
- **Scope:** org-wide

## Context

ADR-0010 declared what an unstated tolerance means. It was silent on
the other half of the question: what a mating pair means. The forge
already lives in that half daily: carrier pins in plates, the sun
collar's heat-set pockets, the pin-journal carrier, every shaft-in-bore
and press the Geometry Gate rules on, with the nylon tier's pin press
re-engineered for creep. The wider world writes this as ISO 286-1, the
system of limits and fits: hole-basis and shaft-basis fits, tolerance
zone designations, and the named fit types (running clearance,
location, transition, press/interference). The research brief's third
round grounded it as the true companion of ADR-0010.

The same trap as ADR-0010 applies, doubled: ISO 286-1's numbers are
calibrated for metal-on-metal, and polymer interference fits creep.

## Decision

1. Every mating pair on a KRI drawing declares its fit in ISO 286-1
   grammar: basis feature, tolerance-zone designation, and fit type,
   resolved against the KRI tolerance table of ADR-0010.
2. **Interference values are forge-computed** per material and process
   from ADR-0012 capability rounds, exactly like the tolerance classes;
   ISO 286-1 tables are never quoted for polymer fits. Machined or
   purchased metal parts may cite 286-1 directly.
3. **Creep rider:** fits in creeping materials (the nylon tier) carry
   an explicit rider naming the time-dependent behavior, the assembly
   method, and any retention means, matching the ratified nylon
   pin-press doctrine. A polymer press fit is declared with its seat
   and its lifespan, not just its interference.
4. Fit declarations appear on the acceptance sheet and are judged under
   the decision rules of ADR-0019.

## Consequences

- Pin presses, bearing seats, and enclosure registers get one grammar
  across CAD, the bench, and outside vendors.
- Cost: capability rounds must run before any fit value is declared;
  until then the table row stays empty rather than estimated, per the
  Deterministic Numbers Law.
- Blast radius: all repos with CAD; Kogane's carrier, cam, and
  enclosure first.
