# KRI Typography

> The canonical Kitsune Research Industries type system. Established September 2026.
> Decided in [ADR-0002](docs/decisions/0002-typography-system.md) — immutable once merged; changes require a superseding ADR.
> Companion to [BRAND.md](BRAND.md) — color and lettering are one voice.

## Principle

**Modern and futuristic, grounded in tradition.** The system pairs the working
voice of the present (a crisp geometric sans) with the formal voice of the past
(a Mincho serif — letterforms born of woodblock printing, whose sharp ink-cut
terminals are the shape a carving knife makes in cherry wood). Rendered in
Gold-Leaf on Foxfire White, the tradition is the structure and the resolution
is the future.

Apple-native first (the no-third-party-dependency rule extends to type): on Apple
platforms and anything rendered by our toolchain, use the native families. Wherever
Apple fonts cannot travel (GitLab wikis, open web, embedded/UI on Vessels), the
listed open equivalents are canon — not fallbacks of lesser honor, but the same
voice licensed for that surface.

## The Families

| Stack | Canon (Apple-native) | Canon (open equivalent) | Role |
|---|---|---|---|
| **KRI Sans** | SF Pro | Inter | Body, UI, structure — the working voice |
| **KRI Mincho** | New York / Songti SC | Noto Serif JP | Display & formal lettering — titles, wordmarks, ceremony; pairs with Gold-Leaf. Woodblock-cut letterforms: the tradition is the structure, the crispness is the future |
| **KRI Mono** | SF Mono | JetBrains Mono | Code, firmware, terminal, technical readouts, prop engravings |

**Rules:**
1. **Sans is the default.** Mincho is earned (titles, wordmarks, ceremony). Mono is truthful (anything a machine reads).
2. **Mincho always pairs with Gold-Leaf** when used as formal lettering; on ink grounds it may also read in Foxfire White.
3. **Never mix serif and mono in one component.** Sans bridges between them.
4. **One family per block of text.** Weights carry hierarchy, not family switches.
5. **No italic in Mono** — code is never emphasized, it is read.
6. Font stacks (write them exactly):
   - Sans: `font-family: "SF Pro", "Inter", -apple-system, system-ui, sans-serif`
   - Mincho: `font-family: "Noto Serif JP", "New York", "Songti SC", "Hiragino Mincho ProN", serif`
   - Mono: `font-family: "SF Mono", "JetBrains Mono", "SF Mono", ui-monospace, monospace`

## The Size Scale

Modular scale, ratio **1.250 (major third)**, base **16px**. Sizes are canon;
line-heights are part of the size, not a suggestion.

| Token | Size | Line height | Weight | Family | Use |
|---|---|---|---|---|---|
| `display-xl` | 48px / 3rem | 1.10 (53px) | 700 | Mincho | Wordmarks, hero titles — Gold-Leaf |
| `display` | 40px / 2.5rem | 1.15 (46px) | 700 | Mincho | Page-level ceremony |
| `title-1` | 32px / 2rem | 1.20 (38px) | 700 | Sans | H1 |
| `title-2` | 24px / 1.5rem | 1.25 (30px) | 600 | Sans | H2 |
| `title-3` | 20px / 1.25rem | 1.30 (26px) | 600 | Sans | H3 |
| `title-4` | 16px / 1rem | 1.40 (22px) | 600 | Sans | H4, sidebar headings |
| `body-lg` | 18px / 1.125rem | 1.55 (28px) | 400 | Sans | Lead paragraphs, intros |
| `body` | 16px / 1rem | 1.55 (25px) | 400 | Sans | Default body text |
| `body-strong` | 16px / 1rem | 1.55 (25px) | 600 | Sans | Emphasis within body |
| `small` | 14px / 0.875rem | 1.45 (20px) | 400 | Sans | Secondary text, captions |
| `caption` | 12px / 0.75rem | 1.40 (17px) | 400 | Sans | Labels, timestamps, tags |
| `overline` | 12px / 0.75rem | 1.20 (14px) | 600 | Sans | ALL-CAPS eyebrows above titles, letterspaced +5% |
| `code` | 14px / 0.875rem | 1.60 (22px) | 400 | Mono | Inline & block code |
| `code-sm` | 12px / 0.75rem | 1.60 (19px) | 400 | Mono | Terminal readouts, dense logs |
| `data` | 20px / 1.25rem | 1.20 (24px) | 500 | Mono (tabular) | Numbers that matter — readouts, BOM counts |

**Size rules:**
1. **Nothing below 12px. Ever.** The forge respects eyes.
2. **Skip no more than one step** moving between adjacent hierarchy levels (mirrors the sanding schedule — progressive, never jumping).
3. `display` sizes are Mincho-only; `title` and below are Sans-only. Mono never scales above `data`.
4. **Line length:** 60–75 characters for body text. `body-lg` max ~55.
5. **Weights are three:** 400 (working), 600 (structure), 700 (ceremony). No 300, no 800 — thin weights break on physical prints, and 800 shouts louder than Zaku.
6. **Letterspacing:** negative on `display` (-1%), zero on body, positive on `overline` (+5%). Mincho's ink-cut terminals already carry visual weight — its display sizes need the least correction of any family we have tried.
7. **If Noto Serif JP cannot be installed:** fetch it from Google Fonts (one CSS line, zero dependencies) — or fall to **New York** (Apple-native, best Latin display) or **Songti SC** (Apple-bundled; the Chinese Song face of the same woodblock tradition — genuine Mincho lineage, though its Latin capitals are wider and flatter than Shippori's; prefer New York for Latin-only display). The stack order encodes this: never is a system left without a correct-tradition face.

## Pairing with the Palette

| Text situation | Color | Token |
|---|---|---|
| Wordmark / hero title | Gold-Leaf `#C9A227` | `display-xl` Mincho 700 |
| Section ceremony | Gold-Leaf or Sumi Ink | `display` Mincho 700 |
| Working headings & body | Sumi Ink `#0E1113` on Foxfire White | `title-*` / `body` Sans |
| Alerts, seals | Torii Crimson `#D0342C` | `title-3` max, never body |
| Success, living states | Imperial Jade `#0FA898` | `small`–`title-3`, per BRAND.md role |
| Code | Sumi Ink; jade for strings, crimson for errors | `code` Mono |

## Embedded / Vessel Contexts

- **LVGL/e-paper props:** closest available family to SF Pro at the needed size; `data` uses tabular figures always.
- **Engraving & vinyl cutting:** Mincho at `display` scale or larger only — below that, the ink-cut terminals collapse.
- **Badges (countdown/shields):** Sans `caption`/`small` with Inter — renders identically on GitLab Pages.
- **Print (cards, plaques):** sizes hold; line-height may open to 1.6 for ink on uncoated stock.
