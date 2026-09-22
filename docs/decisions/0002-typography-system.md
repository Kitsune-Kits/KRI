# ADR-0002: Typography system locked — three families, fifteen tokens

- **Status:** Accepted
- **Date:** 2026-09-22
- **Persona:** ✨ Nui (lead)
- **Scope:** org-wide

## Context

ADR-0001 locked the color canon but lettering had no voice: no families, no
sizes, no rules. Docs, wikis, badges, web, and Vessel UI were each improvising
typography, and improvisation drifts. The org's Apple-inspired direction and its
no-third-party-dependency principle constrain the choice: native fonts first.

Alternatives considered:

- Third-party brand fonts (purchased/licensed display faces) — rejected: violates
  the no-third-party rule and adds licensing surface for zero craft.
- SF Pro everywhere, no serif — rejected: formal lettering (Gold-Leaf's role in
  ADR-0001) demands a serif voice.
- A Western serif (New York / Source Serif 4) as the formal voice — rejected
  during review: beautiful, but traditional without futurism. Replaced by a
  Mincho: letterforms born of woodblock printing — ink-cut terminals shaped
  by the carving knife — matching the Eastern tradition of the torii crimson
  and sumi ink. *Modern and futuristic, grounded in tradition*, per the
  Architect's direction.
- **Shippori Mincho** — selected first, then replaced during MR review: the
  Architect could not install it (web-distributed, not packaged as normal
  macOS font files). A canon font must install when its Architect asks.
- **Noto Serif JP** — selected second, then replaced: it is a Japanese font —
  the download arrives as a large CJK glyph set with Latin as a second-class
  passenger, while KRI's canon lettering is Latin-first. **Hahmlet** takes its
  place: a Mincho-style Latin typeface (same woodblock-cut tradition, built
  for the script KRI actually sets), ordinary downloadable font files, canon
  weights 400/700 available.
- Open fonts only (Inter + Noto Serif JP + JetBrains Mono) — rejected as primary:
  the Apple-native families are canon; the open faces are the licensed-for-web
  voice of the same families, not lesser fallbacks.
- A fluid/viewport-based scale — rejected: fixed tokens survive across GitLab
  markdown, print, and embedded UI; fluid scales break in exactly two of those.
- A 1.333 or 1.414 ratio — rejected: too aggressive by `title-2`; 1.250 (major
  third) yields a scale that survives from hero to caption without stepping
  outside 12–48px.

## Decision

The KRI type system is locked, canonically defined in
[BRAND-TYPOGRAPHY.md](../../BRAND-TYPOGRAPHY.md):

1. **Three families:** KRI Sans (SF Pro / Inter), KRI Mincho (New York /
   Noto Serif JP), KRI Mono (SF Mono / JetBrains Mono).
2. **Fifteen size tokens** on a 1.250 modular scale from 16px base
   (`display-xl` 48px down to `caption` 12px), each with canon line-height,
   weight, and family.
3. **Three weights only:** 400, 600, 700.
4. **Mincho is earned** (display/formal lettering, paired with Gold-Leaf);
   Sans is default; Mono is truthful and never italic.
5. **Nothing below 12px**; hierarchy steps skip at most one size token.

## Consequences

- **Easier:** one voice across docs, wikis, web, badges, print, and Vessel UI;
  hierarchy decided once instead of per-document; palette-token pairings are
  explicit, so color and type stop being separate decisions.
- **Harder:** existing docs with improvised heading sizes drift from canon
  until touched (no mass rewrite mandated — canon applies on edit); Mincho is
  display-only, so long-form documents must lean on Sans hierarchy discipline.
- **Blast radius:** org-wide (all repo docs/wikis, GitLab Pages, badges, media
  graphics, Vessel embedded UI). No build or firmware impact; embedded contexts
  approximate with nearest available family per BRAND-TYPOGRAPHY.md.
