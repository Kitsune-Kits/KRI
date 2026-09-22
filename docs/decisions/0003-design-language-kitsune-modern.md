# ADR-0003: Design language locked — Kitsune Modern

- **Status:** Accepted
- **Date:** 2026-09-22
- **Persona:** ✨ Nui (lead), 🔨 Zaku (materials/structure)
- **Scope:** org-wide

## Context

ADR-0001 (color) and ADR-0002 (type) define the ingredients but not the
cuisine. The Architect set the direction: **modern and futuristic, but
grounded in tradition**. Without a written aesthetic, each doc, UI, and
Vessel interprets that phrase anew — and interpretation drifts.

Alternatives considered:

- **Cyberpunk neon** — rejected: cluttered, dark, and costume-futurist; the
  org direction is Apple-inspired craft, and the palette is white-first.
- **Pure zen minimalism** — rejected: tradition without the future; loses the
  foxfire glow that is the heart of the forge.
- **Pastiche traditionalism** (kanji decoration, woodblock costume) — rejected:
  borrows costume, not structure; reads as tourism, not identity.
- **No written aesthetic, decide per-project** — rejected: same erosion
  ADR-0001 exists to prevent.

## Decision

The KRI design language — **Kitsune Modern** — is locked, canonically defined
in [BRAND-AESTHETIC.md](../../BRAND-AESTHETIC.md):

1. **Tradition is the structure; the future is the light.** Traditional form
   (the gate, the seal, kintsugi, the axial grid) built modern and lit from
   within (breathing glow, circuit-kami patterns).
2. Six principles: Ma negative space, traditional structural proportion,
   technology discovered-within, one seal per surface, gold at the joints,
   circuitry as pattern.
3. Six motifs (Gate, Seal, Kintsugi Line, Circuit-Kami, Foxfire Bloom, Ledger
   Grid) and a materials canon (Foxfire-matte bodies, brushed brass, frosted
   acrylic diffusion).
4. Motion doctrine: breathing light, jade = living motion, crimson = sudden
   stamp; on-screen motion like shoji panels.

## Consequences

- **Easier:** every future doc, badge, UI, Vessel, and photo has a decision
  framework instead of per-project debate; firmware glow behavior and PCB art
  now have canon; physical builds have a materials spec.
- **Harder:** existing assets that read cyberpunk-dark or decoration-heavy
  drift from canon until touched; breathing-glow requirement adds firmware
  work to every lit Vessel; one-seal-per-surface demands real restraint.
- **Blast radius:** org-wide (docs, web, media, Vessel CAD/firmware finish
  specs). Glow canon touches future firmware (Piko's LED handlers) and PCB
  art conventions.
