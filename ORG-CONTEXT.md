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
- **Integration.** Our stack is vertically integrated (Shell / Soul /
  Vessel, built together). Standards are enforced by tooling, not memory.
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
| Three-repo split | Shell / Soul / Vessel architecture |
| KMOD | Compiled prop module, loaded by URANOS with CRC32 verification |
| Kitsunebi | Fox-fire; also the name of the Shell OS (kitsunebiOS) |
| Study | Focused work of craft, smaller than a Project, whose deliverable includes written principles (ADR-0005; index: STUDIES.md) |
| Kyber crystal | NFC soul-tag — the swappable soul of a Vessel; UID-unique, carries soul-data |

## Three-repo split (Tasogane)

| Layer | Repo | Device | Role |
|---|---|---|---|
| Shell | [kitsunebios](https://github.com/Kitsune-Kits/kitsunebiOS) | Orange Pi Zero 3W (A733) | Linux userspace (Linux 5.15, Buildroot) |
| Soul | [kitsuneOS](https://github.com/Kitsune-Kits/kitsuneOS) | Pimoroni Pico 2 (RP2350) | Prop OS — Rust-primary (ADR-0004; ZEUS power core, HERCULES HAL) |
| Vessel | [Project-Kogane](https://github.com/Kitsune-Kits/Project-Kogane) | — | kogane.kmod, CAD, 3D prints, BOM |

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

Buildroot (network fetch at build time)
- UPSTREAM (not stored in our repos): Linux kernel (Allwinner AIOT SDK),
  LVGL, musl libc, BusyBox, U-Boot
- OUR REPOS (only proprietary code): kitsunebios → /usr/bin/kitsunebios,
  Project-Kogane → /sdcard/props/*.lua

kitsuneOS is fetched via CMake FetchContent by Project-Kogane at build time.

**Principle: don't store what's readily available upstream.**

## History

Migrated from GitHub (KitsuneKits) to GitLab (kitsune-kits) in September 2026
for sovereignty over repos, CI, and data. **Homecoming (kri ADR-0007, Nov 2026):**
the Kitsune-Kits GitHub organization is the single home again; the GitLab
group is the read-only mirror until the post-AWA review. Per-repo migration
details live in each `PROJECT-STATUS.md`.