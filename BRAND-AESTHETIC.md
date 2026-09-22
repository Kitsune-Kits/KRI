# KRI Design Language — Kitsune Modern

> The canonical KRI aesthetic: modern and futuristic, grounded in tradition. Established September 2026.
> Decided in [ADR-0003](docs/decisions/0003-design-language-kitsune-modern.md) — immutable once merged; changes require a superseding ADR.
> Companion to [BRAND.md](BRAND.md) (color) and [BRAND-TYPOGRAPHY.md](BRAND-TYPOGRAPHY.md) (lettering).

## The One Sentence

**Tradition is the structure; the future is the light.** Every surface, layout,
and Vessel is built from traditional Japanese form — and lit from within by
modern technology, the way a torii gate glows against a neon skyline.

## Principles

1. **Ma (間) — negative space is sacred.** Foxfire White fields carry the design.
   Content breathes in generous whitespace; the page is a room, not a shelf.
2. **Structure honors the old.** Grids, keylines, and enclosures follow
   traditional proportion — centered, symmetrical, axial. The torii gate is a
   structural diagram: two pillars, one lintel, perfect repetition.
3. **The light is new.** LEDs, screens, and glow sit *inside* the traditional
   form — never bolted on. Technology must appear discovered within the
   artifact, not attached to it.
4. **One seal per surface.** Restraint: a single Torii Crimson accent
   per composition. Red is stamped, never painted large.
5. **Gold is earned at the joints.** Gold-Leaf appears where two things meet —
   hairline borders, title lettering, kintsugi-style seams. It marks craft,
   never decoration.
6. **Circuitry is pattern, not clutter.** Traces echo traditional motifs —
   sakura branches, river curves, shoji grids. A PCB in a KRI Vessel should
   read like a woodblock print from across the room.

## Motifs (the canon vocabulary)

| Motif | Form | Use |
|---|---|---|
| **The Gate** | Torii-inspired frame: two pillars + lintel | Page headers, UI frames, enclosure openings |
| **The Seal (hanko)** | Small square stamp in Torii Crimson | Logos, section marks, "approved" states, firmware splash |
| **Kintsugi Line** | Gold hairline where surfaces join | Section dividers, physical seams, repairs as feature |
| **Circuit-Kami** | PCB traces drawn as branch/river/shoji patterns | Board art, backplates, lighting layers |
| **Foxfire Bloom** | Soft breathing glow with no visible emitter | All lighting, on-screen and physical |
| **The Ledger Grid** | Symmetrical axial grid, generous gutters | All page and document layout |

## Materials (physical canon)

| Surface | Material | Finish |
|---|---|---|
| Primary body | PLA/PETG in Foxfire White, or painted to match | Matte, satin — never gloss |
| Structure/trim | Brass or gold-anodized aluminum | Brushed, hairline grain |
| Light surfaces | Frosted acrylic, heat-molded white PLA | Diffusion per BRAND.md rule 7 |
| Ceremonial parts | Lacquer-black resin or Sumi-painted | High polish, minimal area |
| Accents | Torii Crimson and Imperial Jade paint | Sealed, matte, small area |

## Motion & Light

- **Breathing, not blinking.** All glow follows slow sine curves (4–6 s period),
  corrected in firmware. Strobe is forbidden outside alarms.
- **Jade is the living color of motion** — active states, success, data flow.
  Crimson is reserved and sudden; it should feel like a stamp landing.
- **On screen:** transitions are crossfades and soft slides (200–400 ms), never
  bounces or spins. The interface moves like sliding a shoji panel.

## Photography & Imagery

- Cool white light, single accent of crimson or jade per frame.
- Physical builds shot on light gray or ink grounds; never busy backdrops.
- Glow always slightly overexposed — foxfire must feel like weather, not LEDs.

## What This Is Not

- Not cyberpunk: no neon clutter, no rain-soaked grime. The future is clean.
- Not pastiche: no kanji wallpaper, no geisha motifs. We borrow structure,
  not costume.
- Not minimal-for-minimal's-sake: every empty field frames something sacred.
