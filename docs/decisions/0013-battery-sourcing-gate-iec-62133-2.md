# ADR-0013: Battery sourcing gate: IEC 62133-2 qualification for worn cells

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** ⚡ Piko (lead)
- **Scope:** org-wide

## Context

Vessels and worn props carry lithium polymer cells next to the
Architect's body, in crowds, for ten-hour convention days. IEC
62133-2 (safety requirements for portable sealed secondary lithium
cells, 2017 edition consolidated with Amendment 1:2021) is the
international standard the battery industry, venues, and insurers
recognize for exactly this class of cell. The current gate on battery
choice is datasheet vibes and house caution; that is not a document
that survives a hallway conversation with a fire marshal.

## Decision

1. Any cell or pack in a **worn or carried** Vessel or prop BOM must
   carry **IEC 62133-2 qualification evidence from its vendor**,
   recorded in the BOM row (standard-grade cells, protection circuits,
   vendor test evidence link).
2. Pre-debut LiPos already in bench service are recorded in an amnesty
   list: legal on the bench, never worn at a convention.
3. The gate is a row in the BOM template; a build whose battery row
   cannot show evidence does not ship to a convention, no exceptions
   before MomoCon 2027, the first affected debut.
4. Charging practice (receipt, bench charging posture, storage state)
   is folded into the risk docket of ADR-0014 rather than duplicated.

## Consequences

- Worn power is sourced from qualified cells; venue and insurance
  conversations become short.
- Cost: slightly narrower sourcing (qualified cells only for wearable
  builds) and a homework column in every Vessel BOM.
- Blast radius: all wearable builds: Kogane, Lantern Vigil, Saffron,
  Lazy Comet refits.
