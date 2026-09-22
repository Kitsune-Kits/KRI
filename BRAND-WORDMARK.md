# KRI Wordmark & Seal Spec

> The canonical spec for the KRI mark: the hanko seal and the wordmark lockup. Established September 2026.
> Decided in [ADR-0004](docs/decisions/0004-wordmark-seal-spec.md) — immutable once merged; changes require a superseding ADR.
> Companion to [BRAND.md](BRAND.md), [BRAND-TYPOGRAPHY.md](BRAND-TYPOGRAPHY.md), and [BRAND-AESTHETIC.md](BRAND-AESTHETIC.md).
> **This file is the spec, not the artwork** — artwork is commissioned from this spec and lives in iCloud `03-Resources` (see Asset governance below).

## The Seal (hanko)

The primary mark: a **square stamp** in the tradition of the hanko.

| Property | Canon |
|---|---|
| Shape | Square, equal weight on all sides; corners may soften by max 4% (hand-cut feel, never rounded-rectangle) |
| Color | **Torii Crimson `#D0342C`**, solid fill — always |
| Content | The character motif: a stylized fox-tail curl or the letterform **K**, carved positive (red on ground) — never negative |
| Counter | A breathing counter (enclosed negative space) at the center, reading as a fox-eye or a torii gap — never fully solid |
| Stroke | Carved, not drawn: terminals end in ink-cut bevels echoing Mincho terminals |
| Minimum size | 24px digital / 8mm physical; below this, use the wordmark alone |
| Backgrounds | Foxfire White or Sumi Ink only. Never placed on photography, gradients, or other colors |

**The seal never contains text.** It is stamped, not labeled.

## The Wordmark

| Property | Canon |
|---|---|
| Type | **KRI Mincho** (Shippori Mincho), weight 700 |
| Case | All caps, `KITSUNE RESEARCH INDUSTRIES` — or the short form `KRI` |
| Color | **Sumi Ink `#0E1113`** on Foxfire White; **Foxfire White** on Sumi Ink; **Gold-Leaf `#C9A227`** for ceremonial contexts only |
| Letterspacing | +2% at display scale — Mincho's ink-cut terminals need air between them |
| Minimum size | 16px digital / 6mm physical |

## Lockups

### Primary lockup (seal + wordmark)
```
[seal]  KITSUNE RESEARCH INDUSTRIES
```
- Seal left, wordmark right, vertically centered to the seal's midline
- Gap between seal and wordmark: **50% of the seal's side length**
- Seal size: cap-height of the wordmark × 1.2

### Stacked lockup (ceremony)
```
        [seal]
KITUNE RESEARCH INDUSTRIES   ← no: see rule below
```
- Wordmark centered beneath the seal; gap = 40% of seal side
- Short form `KRI` preferred when stacked — full name only when space allows all of it comfortably

### Seal alone
Permitted when the wordmark appears elsewhere in the same document or product.

## Clear space & misuse

- **Clear space:** minimum 100% of the seal's side on all sides — Ma (間) applies to the mark as much as the page.
- **Forbidden:** placing the seal on busy surfaces; stretching or rotating either element; recoloring the seal; adding outlines; mixing lockup directions in one artifact; placing crimson seal and jade highlight in the same lockup zone.

## Asset governance

- **Spec lives here** (GitLab, `kitsune-kits/kri`); **artwork lives in iCloud** `03-Resources/Design/Brand/`, tagged `Resource · Design · Final · Reference` per [ORGANIZATION-SYSTEM.md](ORGANIZATION-SYSTEM.md).
- Export set (from commissioned artwork): SVG (master), PNG @2x transparent, dark-mode PNG, favicon, and a 512px social square.
- Repo docs and badges reference exported PNGs/SVGs — never commit duplicate artwork into product repos.
- The seal may be stamped (Torii Crimson) into Vessel firmware splash screens as a **shape**, rendered by code, at the `code-sm` scale or larger.
