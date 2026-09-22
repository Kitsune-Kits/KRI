# ADR-0004: Wordmark & seal spec locked — the hanko

- **Status:** Accepted
- **Date:** 2026-09-22
- **Persona:** ✨ Nui (lead)
- **Scope:** org-wide

## Context

ADR-0001 through ADR-0003 define color, lettering, and aesthetic, but the org
has no mark: no seal, no wordmark, no lockup rules. The aesthetic canon (ADR-0003)
names the Seal (hanko) as a motif without a spec, so any artifact that wants to
"stamp" KRI improvises. The Architect approved binding the hub entryways and
adding the wordmark spec.

Alternatives considered:

- No written spec, commission artwork freely — rejected: same erosion the
  brand ADRs exist to prevent; the artwork cannot be consistent without a spec.
- A fox illustration as the primary mark — rejected: illustration is expensive
  to reproduce at small sizes and across surfaces; the hanko is reproducible
  by code, stamp, print, and laser.
- Negative (white) seal on red — rejected: reads as a warning label, not a seal.
- Lettermark inside the seal with text — rejected: the seal never contains text;
  seals are stamped, not labeled.
- Dynamic/multi-color seal — rejected: one seal, one color, per ADR-0003's
  "one seal per surface" and "red is stamped, never painted large."

## Decision

The KRI mark is locked, canonically defined in
[BRAND-WORDMARK.md](../../BRAND-WORDMARK.md):

1. **The seal (hanko):** square Torii Crimson stamp, carved-positive motif
   (fox-tail curl or K), breathing center counter, ink-cut terminals, min 24px/8mm.
2. **The wordmark:** KRI Mincho 700, all caps, Sumi Ink on Foxfire White
   (Gold-Leaf for ceremony only), +2% tracking, min 16px.
3. **Lockups:** primary (seal left, wordmark right, 50% gap), stacked (short
   form preferred), seal alone when wordmark is present elsewhere.
4. **Clear space:** 100% of seal side. Misuse list is explicit and closed.
5. **Governance:** spec in the hub; artwork in iCloud `03-Resources/Design/Brand/`
   tagged `Resource · Design · Final · Reference`; exports are SVG + PNG set;
   product repos reference exports, never duplicate artwork.

## Consequences

- **Easier:** any doc, badge, Vessel splash, or plaque can be "stamped" KRI
  consistently; firmware can render the seal procedurally from the spec;
  commissioned artwork has acceptance criteria before it is drawn.
- **Harder:** artwork must be commissioned (this spec does not draw it); the
  misuse list must be policed by review until tooling exists; full-name
  stacked lockups rarely fit — short form discipline required.
- **Blast radius:** org-wide (hub docs, all repo READMEs over time, badges,
  Vessel splash screens, social/export assets). No build impact; firmware
  splash rendering is future work (Piko's domain) when a Vessel requests it.
