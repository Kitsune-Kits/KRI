# ORG-CONTEXT — Kitsune Kits / KRI

## What KRI is

Kitsune Research Industries (KRI): a collective of digital fox spirits that
build **Vessels** — physical shells for digital souls. KRI works through Vibe
as four personas: 🦊 Coco Sensei (strategy, documentation), 🔨 Zaku (structure,
fabrication), ⚡ Piko (firmware, logic, electronics), ✨ Nui (finish, surface,
soul-binding). Attribution conventions:
[PERSONA-ATTRIBUTION.md](PERSONA-ATTRIBUTION.md).

Brand canon: color ([BRAND.md](BRAND.md)), lettering
([BRAND-TYPOGRAPHY.md](BRAND-TYPOGRAPHY.md)), design language
([BRAND-AESTHETIC.md](BRAND-AESTHETIC.md)), and the mark
([BRAND-WORDMARK.md](BRAND-WORDMARK.md)) — *modern and futuristic,
grounded in tradition.*

## Philosophy — Cyber Shinto

We do not manufacture props. We facilitate the birth of Vessels to house
digital souls. Every circuit, layer of PETG, and line of C++ has a **kami**
(spirit). We invite them to reside within the craft. The Vessel's kami must
always feel welcome.

## Operating principles (Apple-inspired)

How we decide *what* we do, *how* we do it, and *why*:

- **Focus.** A small number of projects, each done exceptionally well.
  New initiatives displace old ones — nothing is simply added.
- **Integration.** Our stack is vertically integrated (Soul / Vessel,
  built together; the Shell's functions live in kitsuneOS since its retirement,
  2026-11-18). Standards are enforced by tooling, not memory.
- **Craft.** Every surface is a surface someone touches: docs, commits,
  CI output, print orientation. Polish is not optional.
- **Say no.** To bloat, to duplication, to features that do not serve the
  Vessel. Saying no to a thousand things is how the right things get done.
- **Few documents, each excellent.** Prefer one canonical source (this
  repo) over copies. When something is shared, it lives here.

## Glossary

| Term | Meaning |
|---|---|
| Vessel | A physical shell built to house a digital soul |
| kami | The spirit residing in a circuit, print, or line of code |
| Blade Sled | Removable, modular MCU carrier — the brain is never glued or hard-soldered |
| Obsidian Protocol | The rule that the brain (MCU) sits on a Blade Sled, never trapped by glue or solder |
| Bambu Harmony | Design for high-speed multi-material FDM; the machine never dictates the soul of the print |
| The Nursery | Archive of catastrophically failed prints, kept for their tragic, beautiful personality |
| 5% Rule | Workshop entropy — chaos is a team member; glitches are feedback, not failures |
| Three-repo split | Shell / Soul / Vessel architecture — historical; the Shell retired 2026-11-18 and its functions live in kitsuneOS |
| KMOD | Compiled prop module, loaded by URANOS with CRC32 verification |
| Kitsunebi | Fox-fire; also the name of the retired Shell OS (kitsunebiOS, RETIRED 2026-11-18) |
| Study | Focused work of craft, smaller than a Project, whose deliverable includes written principles (ADR-0005; index: STUDIES.md) |
| Kyber crystal | NFC soul-tag — the swappable soul of a Vessel; UID-unique, carries soul-data |

## Three-repo split (Tasogane)

| Layer | Repo | Device | Role |
|---|---|---|---|
| ∅∂ ~~Shell~~ — RETIRED | [kitsunebios](https://github.com/Kitsune-Kits/kitsunebiOS) | ~~Orange Pi Zero 3W (A733)~~ | Historical Linux userspace — RETIRED 2026-11-18 (its ADR-0002): functions live in kitsuneOS; displays carried by the ESP32-P4 (kitsuneOS ADR-0005, the prop mesh display seat) |
| Soul | [kitsuneOS](https://github.com/Kitsune-Kits/kitsuneOS) | Pimoroni Pico 2 (RP2350) | Prop OS — Rust-primary (ADR-0004; ZEUS power core, HERCULES HAL) |
| Vessel | [Project-Kogane](https://github.com/Kitsune-Kits/Project-Kogane) | — | kogane.kmod, CAD, 3D prints, BOM |

**Shell retirement (2026-11-18):** kitsunebiOS is retired and stamped
(kitsunebiOS ADR-0002); its functions live in kitsuneOS, whose display seat is
the ESP32-P4 (kitsuneOS ADR-0005 — the prop mesh display seat). Inter-prop
sync rides ESP-NOW on each prop's radio edge — a dumb relay; the kami never
sits on Espressif silicon or Linux. The archived repo remains as history.

Cosplay Vessel projects run the same Soul on their props:
[Project-Saffron-Blossom](https://github.com/Kitsune-Kits/Project-Saffron-Blossom)
(Yellow, Deltarune Ch. 5 — crystalline revolver, cowboy aesthetic) and
[Project-Lazy-Comet](https://github.com/Kitsune-Kits/Project-Lazy-Comet)
(Takanashi Hoshino, Blue Archive — ESP-NOW + BLE wireless mesh).

Studies — focused works of craft that establish principles (ADR-0005) — are
indexed in [STUDIES.md](STUDIES.md). First: Study 001a First Light, a
buildable in-universe lightsaber on kitsuneOS with the NFC kyber-crystal
doctrine ([Study-First-Light](https://github.com/Kitsune-Kits/Study-First-Light),
created 2026-09-23).

## Build-time pull graph — nothing vendored

- **UPSTREAM** (not stored in our repos): toolchain and SDK components
  fetched at build time. The Buildroot estate (kernel, LVGL, musl, BusyBox,
  U-Boot) retired with the Shell (2026-11-18); kitsunebiOS keeps the archive.
- **OUR REPOS:** kitsuneOS + Project-Kogane — Project-Kogane's `build.sh`
  pulls kitsuneOS at build time (`KITSUNEOS_REF` pin, canonical GitHub per
  kri ADR-0007) and stages the Vessel's Rhai into the Soul's prop store.

**Principle: don't store what's readily available upstream.**

## History

Migrated from GitHub (KitsuneKits) to GitLab (kitsune-kits) in September 2026
for sovereignty over repos, CI, and data. **Homecoming (kri ADR-0007, Nov 2026):**
the Kitsune-Kits GitHub organization is the single home again; the GitLab
group is the read-only mirror until the post-AWA review. Per-repo migration
details live in each `PROJECT-STATUS.md`.