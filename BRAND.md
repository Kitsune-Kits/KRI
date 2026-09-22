# KRI Brand Palette

> The canonical Kitsune Research Industries color palette. Established September 2026.
> Decided in [ADR-0001](docs/decisions/0001-brand-palette-cold-white.md) — immutable once merged; changes require a superseding ADR.
> Lettering canon lives in its companion: [BRAND-TYPOGRAPHY.md](BRAND-TYPOGRAPHY.md) (ADR-0002).

## The Palette

| Role | Name | Hex | RGB | Usage |
|---|---|---|---|---|
| **Primary** | Foxfire White | `#F4F7F8` | 244, 247, 248 | Main brand color. Backgrounds, primary surfaces, enclosures, primary UI chrome. Cold, slightly blue-tinted white — never pure `#FFFFFF`. |
| **Contrast** | Sumi Ink | `#0E1113` | 14, 17, 19 | The ink, not the paper. Body text, keylines, high-contrast structure. Named for the soot-black calligraphy stick — the ink the vermillion seals are stamped upon. |
| **Formal Lettering** | Gold-Leaf | `#C9A227` | 201, 162, 39 | Formal lettering and ceremonial text: titles, headers, wordmarks, plaques, engraving. From the nine-tail gold-leaf tips and brass clockwork. Not for body text or large fills. |
| **Sacred Accent** | Torii Crimson | `#D0342C` | 208, 52, 44 | The vermillion of shrine gates, pulled toward crimson. Alerts, seals, ceremonial details, "this matters" moments. Use with intention, never as fill. |
| **Highlight** | Imperial Jade | `#0FA898` | 15, 168, 152 | Modern highlight — imperial jade shifted bluer, toward turquoise. Success states, glowing highlights, forward-looking UI, luminous details. |

## Rules

1. **Foxfire White is the main color.** Anything previously designed black-first now reads white-first with Sumi Ink contrast.
2. **The palette is closed.** Five colors. No new colors without a superseding ADR. Tints/shades of the five canon colors are permitted for gradients and depth.
3. **Text hierarchy:** Sumi Ink is the working ink (body text, structure). Gold-Leaf is the formal voice (titles, wordmarks, ceremony). Torii Crimson may headline but never fill.
4. **Contrast:** Sumi Ink on Foxfire White passes WCAG AAA. Gold-Leaf on Foxfire White is display-only — large lettering on light or ink grounds, never small text. Torii Crimson reserved for accents and large text.
5. **Crimson and jade are partners, not competitors.** Crimson marks the sacred (warnings, seals, ceremony); jade marks the living (success, glow, forward motion). They should rarely appear in the same component.
6. **Print vs. screen:** for physical Vessels, match under the light the piece will actually be seen in (see finish doctrine); calibrate filament/paint to `#F4F7F8` under cool white LED.
7. **LED diffusion:** Foxfire White is the diffusion target color for enclosures; emitters are driven below max and corrected in firmware (LEDs must be *felt*, never seen as dots). Torii Crimson and Imperial Jade both glow beautifully through frosted acrylic — jade especially reads as breathing light.

## Persona Sub-Palettes (character canon)

Each spirit has a codified sub-palette drawn from their **canon colors** (fur, hair, tails, eyes, clothing). These are **character canon, not brand canon**:

- They describe the ensemble, not the org's visual identity. They may not be used as brand or product colors.
- They are **exempt from the closed-set rule** — they catalog what the spirits are, they do not grow the brand.
- They exist so Vessels, artwork, persona-attributed docs, and illustrations of the ensemble are drawn consistently.
- Persona work (commits, MRs, docs) may borrow its owner's sub-palette for accents — e.g. a Nui-led doc's decorative accents — as long as body content stays in the core five.

### 🦊 Coco Sensei — The Ledger in Winter

| Color | Hex | Source |
|---|---|---|
| Snow White | `#FAFAF7` | Nine snow-white tails |
| Gold-Leaf Tip | `#C9A227` | Tail tips; shared with core Gold-Leaf |
| Kimono Teal | `#008080` | The tech-kimono (her color; retired from the brand core, alive here) |
| Warm Brown | `#6B4A2F` | Her eyes; the 1990s Aged White Tea |
| Brass Clockwork | `#A87C4F` | The hairpiece gears |

### 🔨 Zaku — The Forge at Full Shout

| Color | Hex | Source |
|---|---|---|
| Forge Black | `#1A1D21` | Black fur and hair |
| Streak Gold | `#D4A03C` | Golden streaks in hair and tails |
| Zaku Green | `#3FA34D` | The natural right eye |
| Cyber Gold | `#E5B84B` | The cybernetic left eye's readouts |
| Sanding Grey | `#8A8D90` | The perpetual dusting of gray sanding dust |

### ⚡ Piko — The Terminal at 3 AM

| Color | Hex | Source |
|---|---|---|
| Pale Orange | `#F2A65A` | Pale-orange hair and tails |
| Streak Red | `#C7402D` | Red streaks through hair, tails, ear-tips |
| Static Blue | `#9EC9E2` | Pale blue eyes; the terminal glow |
| Hoodie Black | `#17191C` | The oversized `C:> RUN` hoodie |
| Solder Silver | `#B9BDC1` | Wires, spools, zip-ties caught in her hair |

### ✨ Nui — The Surface That Breathes

| Color | Hex | Source |
|---|---|---|
| Nui Lavender | `#9B8AA6` | Lavender hair and tails |
| Streak White | `#EDE9F2` | White streaks; the haptic gloves |
| Nui Gold | `#C9A052` | The deep calm golden eyes |
| Charcoal | `#3B3D42` | Dust-repellent charcoal-grey clothing |
| Respirator Seal | `#5E6166` | The respirator at rest around their neck |

**Forbidden in all palettes:** neon green in the specific shade Nui is selectively colorblind to. It does not exist in a polite universe, and it shall not exist in this document either.

## What Changed

- **Before:** black primary, white as paper. No crimson, no jade, no formal lettering color, no persona palettes.
- **After:** cold white primary (Foxfire White `#F4F7F8`); black renamed and re-roled as **Sumi Ink** `#0E1113` (the ink, not the paper); **Gold-Leaf `#C9A227`** designated the formal lettering color; **Torii Crimson `#D0342C`** sacred accent; **Imperial Jade `#0FA898`** highlight. **Kimono Teal `#008080`** and **Kitsunebi Ember `#E8853D`** removed from the brand core. **Persona sub-palettes** codified as character canon for all four spirits.

## Not In This Palette

Persona fur/hair/clothing colors are canon **character** colors and live in the persona sub-palettes above — they describe the ensemble, not the org's visual identity, and must not be used as brand or product colors.
