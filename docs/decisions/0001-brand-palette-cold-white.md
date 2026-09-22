# ADR-0001: Brand palette locked — cold white primary, five-color canon

- **Status:** Accepted
- **Date:** 2026-09-22
- **Persona:** ✨ Nui (lead)
- **Scope:** org-wide

## Context

KRI has never had a written brand palette; color decisions lived in conversation
and eroded between sessions. The org's visual identity was implicitly black-primary,
and the September 2026 direction (Apple-inspired craft on every surface) makes a
locked, explicit palette a prerequisite for consistent docs, UI, packaging,
Vessel finishes, and media.

The Architect directed a switch: **the main color moves from black to cold white**,
with exact values delegated for proposal and approval. During MR review the
palette evolved before merge: a **crimson** accent rooted in Eastern tradition
(torii-gate vermillion) and a **turquoise-leaning imperial jade** highlight were
added; then **Kimono Teal and Kitsunebi Ember were removed** (teal collided with
jade; ember was decorative without a role), **Gold-Leaf was re-roled as the formal
lettering color**, and the contrast black was branded **Sumi Ink** — the soot-black
of calligraphy sticks, the ink the vermillion seals are stamped upon. Finally,
**persona sub-palettes** for all four spirits were codified as character canon,
exempt from the closed-set rule. This ADR records the final decision at acceptance.

Alternatives considered:

- Pure `#FFFFFF` primary — rejected: reads sterile on screen and impossible to
  maintain as a physical finish; a slightly cold tint (`#F4F7F8`) carries warmth
  and hides handling.
- Keeping black primary with white accents — rejected by direction.
- An open-ended palette — rejected: open palettes drift; a closed five-color set
  enforced by document beats an unlimited set enforced by memory.
- Adding further core colors beyond five — rejected: five covers paper, ink,
  formal lettering, the sacred, and the living; more would be decoration, and
  decoration is what subtraction just removed.
- Pure torii vermillion (`#E34234`) — rejected: reads alarm-orange next to the
  cold white; pulled toward crimson (`#D0342C`) to read sacred instead.
- True jade green (`#00A86B`) — rejected: too mossy; shifted bluer toward
  turquoise (`#0FA898`) per the Architect's "slightly bluer" direction.
- Keeping Kimono Teal `#008080` alongside jade — rejected: two neighboring
  blue-greens with no separating role; teal removed so jade owns "living" alone.
  Teal survives only as Coco's character color in her sub-palette.
- Keeping Kitsunebi Ember `#E8853D` — rejected: decorative, no role the
  crimson/gold pair does not already fulfill.
- Names for the ink other than Sumi Ink — rejected: "Ink Black" described, did
  not brand; Sumi binds it to the same tradition as the torii crimson.
- Persona colors inside the brand palette — rejected: the ensemble's colors
  describe the spirits, not the org; codified as separate character-canon
  sub-palettes instead.

## Decision

The KRI brand palette is locked to five colors, canonically defined in
[BRAND.md](../../BRAND.md):

1. **Foxfire White `#F4F7F8`** — primary (cold white; backgrounds, primary surfaces)
2. **Sumi Ink `#0E1113`** — contrast (body text, keylines, structure)
3. **Gold-Leaf `#C9A227`** — formal lettering (titles, wordmarks, ceremonial text)
4. **Torii Crimson `#D0342C`** — sacred accent (alerts, seals, ceremony)
5. **Imperial Jade `#0FA898`** — highlight (success, glow, forward motion)

Additionally, **persona sub-palettes** (Coco, Zaku, Piko, Nui — five colors each)
are codified in BRAND.md as character canon: they describe the ensemble for
Vessels, artwork, and persona-attributed work; they are exempt from the
closed-set rule and may never be used as brand or product colors.

Black is no longer the primary color; it is the ink, not the paper. Tints and
shades of the five core colors are permitted; new core colors require a
superseding ADR.

## Consequences

- **Easier:** consistent theming across docs, wikis, web, and Vessel finishes;
  a single source of truth for agents and humans; a tight text hierarchy
  (Sumi working ink → Gold-Leaf formal voice → Crimson headline); crimson/jade
  give the brand a sacred/living accent pair that photographs well under stage
  lighting; physical finishes have a calibration target under cool white LED;
  persona artwork now has reference values instead of guesswork.
- **Harder:** existing teal/ember usage must be migrated (docs, badges, any UI
  experiments); Gold-Leaf is display-only and fails contrast for small text —
  pair formal lettering with Sumi Ink body text; crimson must never be fill;
  sub-palette hexes are observational canon and may be refined only via ADR
  supersession like the core.
- **Blast radius:** org-wide (KRI hub, all repo docs/badges, future Vessel
  finish specs, media/LUT look library). No build or firmware impact; purely
  identity and finish canon.
