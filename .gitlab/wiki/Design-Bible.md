# Design Bible

The KRI Design Bible is the org's design doctrine — principles, patterns, and non-negotiables, expressed entirely in our own language. It is self-contained: if a passage reads like it came from somewhere else, that passage was written wrong. Knowledge is tested in conversation; what proves out is canonized here.

**Companion canon:** `BRAND.md` (palette, typography), `BRAND-TYPOGRAPHY.md`, `BRAND-AESTHETIC.md`, ADRs 0001–0003 in `docs/decisions/`, and [Operating Principles](Operating-Principles). The bible defers to all of them.

## How to use this bible

Route any design question in this order: Doctrine → Foundations → Patterns → Components → Inputs → Accessibility.

| KRI surface | Primary section |
|---|---|
| Vessel UI (Tufty 2350, 320×240 IPS) | Foundations (Layout, Type, Color) + Doctrine §Screen |
| GitLab Pages sites / docs | Foundations + Patterns (navigation, hierarchy) |
| Brand docs, READMEs, wikis | Doctrine (one seal per surface, Ma) |
| Print/finish specs, paint docs | Foundations (Color, Materials) + Doctrine §Print & finish |
| LED behavior, breathing glow | Foundations (Motion, Color) + Doctrine §Light |
| Interaction / prop behavior | Patterns (Feedback, Modality) + Inputs |

## KRI Design Doctrine (the synthesis)

The bible's operative core: how design *method* becomes KRI *practice*. Start here.

### The six commitments

1. **Clarity — the kami must be understood.** Any interface — screen, garment, prop, doc — must be graspable in seconds. If a design needs a manual to be read, it fails.
2. **Deference — Ma.** Negative space leads; the content (the kami's behavior) is the star; chrome recedes. One seal per surface.
3. **Depth — technology discovered-within.** Layers, materials, and motion *explain* structure (what's above, what's alive, what's sacred). Never decoration for its own sake.
4. **Consistency — the Ledger.** Standards are enforced by tooling and canon (ADRs, BRAND.md, this bible), not by memory. Components are vocabulary; the vocabulary stays small and shared.
5. **Closed vocabulary — don't rebuild the Seal.** Shared, pre-built patterns before custom ones; custom is earned through an ADR.
6. **Accessibility as foundation — the Vessel's kami must always feel welcome.** No color-only meaning, no hidden-gesture-only behavior, requests for stillness honored. (This commitment is the whole ethic in one line.)

### Per-surface decision framework

**§Screen (Vessel UI, Tufty 320×240 and beyond)**
- Design at 320×240 first; tokens not px; 12px type floor; 2–3 components visible max; every state has a visible exit; foxfire bloom = working, Ledger fill = progress, breathing glow = alive (jade), stamp = sacred (crimson). Perceived input→feedback latency < 100 ms.

**§Web (GitLab Pages, docs, READMEs)**
- Semantic HTML; token-based CSS from the brand ADRs; keyboard + focus + reduced-motion honored; one callout class per meaning; images compressed and alt-texted; dark mode is native mode, light is designed deliberately.

**§Print & finish (Vessel surfaces, paint specs)**
- Colors specified in the prop spec from the five-color palette with finish notes (matte Foxfire body, brushed brass, frosted acrylic = our materials system); light diffusion is sacred — LEDs never visible as dots; nothing below 12px equivalent at intended viewing distance.

**§Behavior (props, firmware UX)**
- Feedback comes first, nearest the cause, in calm language; destructive actions named and confirmed; safe defaults everywhere — a Vessel boots alive without configuration; hidden gestures always have a visible twin.

## Foundations

The bedrock elements every KRI surface is built from. Foundations are decided once, written down, and then simply *used*.

### Core principles

Four qualities every interface must have, in descending order of importance:

1. **Clarity** — understood in seconds, without a manual. If a design needs explaining before it can be read, it has already failed.
2. **Deference** — the UI recedes; the content leads. Chrome is a frame, never the picture.
3. **Depth** — layers, materials, and motion exist to *explain* structure: what is above, what is beneath, what is alive, what is sacred.
4. **Consistency** — the same pattern means the same thing on every surface. Familiarity is a gift to the person, not a constraint on the maker.

**KRI reading:** These map onto "Kitsune Modern" — deference is *Ma* (negative space leads), depth is *technology discovered-within*, consistency is the Ledger and its ADRs.

### Layout

- Design for adaptivity first: one layout system that reflows across sizes and orientations — never fixed canvases.
- Respect margins and safe areas; align to a consistent grid; let content define density, not the other way around.
- Hierarchy through grouping, alignment, and relative emphasis — never through decoration.

**KRI mapping:** For the Tufty 2350 (320×240), design at the smallest target first — if it survives 320×240 with breathing room, larger surfaces are free. No fixed-position chrome that fights reflow on Pages sites.

### Typography

- One neutral default typeface family, with a *scale of named tokens* rather than ad-hoc sizes; text must be able to grow (someone always needs it larger) without breaking layout.
- Weight and size carry hierarchy; nothing below legible minimums, ever.

**KRI mapping:** Our canon already embodies this — KRI Sans (default), KRI Mincho/Shippori (earned, formal), KRI Mono (code), 15 tokens on a 1.250 scale, base 16px, weights 400/600/700, nothing below 12px (ADR-0002). **Use tokens, never raw px.** On the Tufty, compute sizes from the same scale, stepped down — 12px minimum holds even at 320px wide. Never hard-code container heights around text; let type grow.

### Color

- Colors in an interface are **meaning-carried tokens** (text, fills, separators, backgrounds, accents) that adapt to their appearance mode — never raw hard-coded values.
- Any custom color must pass contrast in *both* light and dark appearances; a dark appearance is not an inversion — it desaturates, lifts grays, and cools.
- Increased-contrast and reduced-transparency preferences must remain honored.

**KRI mapping:** Extend the locked brand palette with semantic tokens per surface: `--kri-primary`, `--kri-ink`, `--kri-accent-sacred` (Crimson), `--kri-accent-living` (Jade) — never both accents in one component. Dark mode is our *native* mode ("black is the ink, not the paper" — Foxfire White on Sumi Ink); light mode is designed deliberately, never derived by inversion. Crimson/jade are checked for contrast in both modes.

### Materials

- Material is how a surface *implies depth without stealing focus*: translucency layered thin-to-thick, foreground content pulled forward, background receding.
- Prefer a drawn glyph or symbol over a full-color image whenever the surface is translucent or layered.

**KRI mapping:** Materials canon (ADR-0003) is the physical analog: Foxfire matte bodies, brushed brass, frosted acrylic. On screen, "material" = *breathing glow layers* — LEDs never visible as dots, only as diffuse foxfire. Frosted acrylic over an LED is our vibrancy.

### Iconography

- Icon vocabulary must be a consistent, self-integrated set that scales with text, adapts to appearance mode, and *accurately represents its function* — an icon is a promise, not a decoration.
- One clear focal concept per mark; no wordy detail at small sizes.

**KRI mapping:** KRI-native iconography draws from the six motifs (Gate, Seal, Kintsugi Line, Circuit-Kami, Foxfire Bloom, Ledger Grid). One seal per surface — an icon is a hanko stamp, not a photo. A new mark is added to the vocabulary deliberately, not sketched ad hoc.

### Motion

- Motion exists to clarify cause-and-effect and spatial relationships — purposeful, brief, interruptible. Never decoration-only.
- Touch feedback should be meaningful and sparing; a pattern used for everything means nothing.

**KRI mapping:** Motion doctrine (ADR-0003) already aligns: breathing glow 4–6s sine for *living* (jade) state, sudden stamp for *sacred* (crimson) alerts. Any Vessel animation must answer "what does this clarify?" — foxfire drift that explains state is canon; drift that is merely pretty goes to the Nursery of ideas.

## Patterns

Recurring *behavioral* structures — how people move through, get information from, and give information to a system. Read after Foundations; apply per surface.

### Navigation

- People must always know **where they are and how to get back**. Prefer standard, predictable structures over custom exploration.
- One clear path to content beats clever branching. Navigation elements are for *destinations*, not actions — never mix movement with commands in the same control.

**KRI mapping:** Pages sites and docs — persistent header, breadcrumb-style hierarchy, predictable "back to index." Vessel UI on the Tufty: every reachable screen state must have an obvious way home; button = destination, long-press = action, never the reverse.

### Modality

- An interrupt (sheet, alert, seal) must be rare, self-contained, and used only when the flow *must* stop. Always offer an obvious escape; never stack interrupts.
- Destructive confirmations: name the consequence, offer the safe default.

**KRI mapping:** Crimson is the sacred interrupt — an alert/seal. A modal alert on a Vessel should be rare, stamp-like, and always escapable. Jade states (living, success) are never modal.

### Onboarding & first-run

- Get people to value fast; teach in context, not with walls of text. Launch quickly, defer any setup or permission until the moment it's needed, make skip obvious.
- No marketing screens inside the tool.

**KRI mapping:** A Vessel's first boot should *do its kami's thing* within seconds — foxfire breathing — not show a boot logo carousel. Docs/wiki home pages put the build guide within one click of the front door.

### Loading, progress & waiting

- Distinguish busy/indeterminate from determinate progress; keep progress honest; never block interaction unnecessarily; preserve state across waits.

**KRI mapping:** On the Tufty, a breathing foxfire bloom = working (indeterminate); a Ledger Grid fill = determinate. Never freeze a Vessel display silent — silence reads as death.

### Feedback & error handling

- Surface what happened at the moment it matters, in plain language; tell people how to fix it; no jargon, no blame ("that didn't work" + remedy, not "error 0x…").
- Interruptive alerts are a last resort; inline or ambient feedback comes first.

**KRI mapping:** Vessel error states use Crimson sparingly and always pair with a suggested gesture ("reseat the Blade Sled"). Firmware log lines are written to be read aloud calmly, not debugged mid-panic.

### Search, data entry & settings

- Reduce entry cost: sensible defaults, incremental search, completion, input scoped to what's expected.
- Settings are discoverable but invisible in daily flow; no core task should require visiting settings first.

**KRI mapping:** Prop config (KMOD/prop scripts) has safe defaults so a Vessel works unconfigured. Deep options live in the Ledger, out of the ceremony.

### Managing content

- Treat user data as sacred: predictable undo, clear confirmation before destructive bulk actions, no surprise reordering.

**KRI mapping:** The Ledger is sacred — Coco's book. Any tooling that reorders, rewrites, or deletes canon files must confirm with a named scope first.

## Components

### The closed-vocabulary doctrine

The strongest structural rule in this bible: **a small set of shared, pre-built components is used by default.** A standard control ships with correct behavior, accessibility, appearance adaptation, and familiarity already *built in*. Every custom control invented inherits the job of rebuilding all of that correctly — state, focus, gesture, contrast, motion. Customize *within* an existing component (tint, size, content) before replacing it; go custom only when the standard genuinely cannot express the experience.

**KRI mapping:** This is the org principle already codified ("integration — standards enforced by tooling not memory"):

- **Web/docs:** standard HTML elements + semantic classes over bespoke widgets. A `<button>` is a button; a link is a link.
- **Vessel UI:** a small closed set of Vessel widgets — Seal (toggle), Gate (screen transition), Ledger row (list item), Bloom (status glow) — defined once in kitsuneOS UI code and reused everywhere. If a screen needs a widget the set doesn't have, that's a Coco-scope decision, not a per-screen improvisation.
- **Naming:** components are vocabulary, not one-off art. New components enter the set through an ADR-style addition; the set stays small.

### Inventory (by cluster)

- **Navigation & containers:** navigation bars/sidebars, tab bars, toolbars, split views, sheets, popovers. Use for *destinations and containment*, never as action surfaces.
- **Commands:** buttons, menus, toggles, sliders, pickers. One unambiguous action per control; a consistent glyph vocabulary for common actions; generous hit targets, thumb-tested.
- **Content organization:** lists/tables, collections, grids, groupings. Grouping carries comprehension — align, don't decorate.
- **Status & feedback:** progress indicators, badges, labels, alerts, transient notices. Feedback belongs nearest the content it describes.
- **Text & selection:** text fields, search fields, text views, selection handles. Scope entry to the expected input.
- **Presentation:** tooltips, context menus, drag-and-drop. Let people peek at content before committing to it.

### Annotated usage (per surface)

- **Vessel screens (320×240):** components must be readable at arm's length in daylight. Minimum interactive hit area ≈ 24px on Tufty, scaled from the generous-hit-area principle for the display's physical size — verify by thumb test. Only 2–3 components visible at once; the rest behind a Gate.
- **Pages sites:** navigation bar, list, badge, callouts — implemented with plain semantic HTML/CSS tokens from Foundations. No JS component libraries unless a real behavior needs it.
- **Docs/markdown:** callouts and tables are components too — one callout class per semantic meaning (sacred/crimson = warning, living/jade = tip, ink = default note).

### When custom is justified

Custom components are *earned*, like the Mincho: only when (1) the shared set cannot express it, (2) you can commit to matching accessibility + appearance + motion behavior of the standard it replaces, and (3) the deviation is written down. Everything else is a Seal waiting for its surface.

## Inputs

Inputs = how a person *physically* talks to the system. The stance: honor the input methods people already know; never shadow or hijack standard behaviors; support the full set relevant to your surface.

### Gestures & touch

- Standard gestures (tap, swipe, drag, long-press) keep their standard meanings. Custom gestures must be *additive*, discoverable, and never the only path to an action.
- Gestures are invisible UI — every gesture-based behavior needs a visible affordance or fallback.

**KRI mapping:** Vessel interactions (prop behavior, touch zones, IMU triggers) are custom gestures by nature — so each one needs a visible/audible fallback. Rule: a behavior that only a hidden gesture can reach doesn't ship.

### Pointing devices & keyboards

- Full keyboard navigation and focus states are table stakes; visible focus, logical tab order, shortcuts that don't collide with the system's.
- Context menus *accelerate* existing actions; they never hide exclusive ones.

**KRI mapping:** Pages sites must be fully keyboard-navigable with visible focus states. Firmware console/Shell commands are our "keyboard shortcuts" — document them in the wiki, and every command-line power has a UI/LED-state counterpart where feasible.

### Voice, camera & sensors

- Defer permission/setup requests to the moment of need; explain why; provide the service in degraded form even when declined.

**KRI mapping:** A Vessel that needs calibration (IMU, audio) must boot and *breathe* without it — degraded-but-alive beats a permission wall before the kami settles.

### Physical controls (KRI extension)

Physical controls are *first-class components with expectations*: consistent mapping, predictable response, no surprise latency.

**KRI mapping:** Every physical control on a Vessel — dial, switch, haptic pad — is a component in the same sense as a screen widget: named, consistent, documented in the prop spec, with instant (<100ms perceived) response. A control with lag reads as a broken kami.

## Accessibility

### The stance

Accessibility is a foundation, not a feature. The bible assumes assistive technologies (screen readers, larger text, reduced motion, increased contrast, color-blindness settings) are part of the audience *by default*. Two rules are absolute:

1. **Never convey meaning with color alone** — pair color with symbol, text, position, or motion.
2. **Honor the request for stillness** — when someone asks for less motion or less translucency, decorative motion and materials step aside.

### Key guidance

- Text must scale without breaking layout; maintain contrast in both appearance modes; don't hard-code heights around text.
- Every interactive element needs: a name, a role, and a value/state (labels are content, not decoration).
- Generous hit targets with spacing between them prevent mis-taps.
- Honor system preferences: bold text, reduced transparency, differentiation without color, captions for audio/video.
- Test with the tools on: screen readers (semantic HTML gives this for free on web), keyboard-only navigation, and a grayscale pass to catch color dependence.

### KRI mapping

- **Web/docs:** semantic HTML + alt text + visible focus + reduced-motion honored for the breathing glow (the glow *slows to stillness*, never simply removed — a stopped foxfire is a dead one).
- **Vessel UI:** **no state is color-only.** Jade living-state always pairs with motion or symbol; crimson sacred-state always pairs with a stamp pattern. On a 320×240 screen, contrast ≥ 4.5:1 for body text is checked in the prop spec.
- **Physical builds:** accessibility extends to wearables — a Vessel garment must be donnable and operable by the wearer alone, controls reachable without assistance (garmenting comfort engineering shares this goal).
- **Audio/feedback states:** any audible alert has a visible twin; any glow-only state has a tactile twin where hardware allows.

## Governing canon (do not contradict)

- Brand palette & typography ADRs (BRAND.md, ADR-0001/0002/0003). This bible defers to them.
- "Kitsune Modern": tradition is the structure, the future is the light.
- The bible is method, never a style transplant. We never make things look like anyone else's system — we adopt the discipline: small shared component vocabularies, meaning-carried tokens, deference to content, accessibility as foundation.
- This wiki page is a living doctrine, self-contained by design — no external citations in the text. Bible content that proves out repeatedly graduates into `docs/decisions/` as an ADR (immutable, MR-only) — knowledge is tested in conversation, canonized here.
