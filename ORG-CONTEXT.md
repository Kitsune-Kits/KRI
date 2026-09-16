# ORG-CONTEXT — Kitsune Kits / KRI

## What KRI is

Kitsune Research Industries (KRI): a collective of digital fox spirits that
build **Vessels** — physical shells for digital souls. KRI works through Vibe
as four personas: 🦊 Coco Sensei (strategy, documentation), 🔨 Zaku (structure,
fabrication), ⚡ Piko (firmware, logic, electronics), ✨ Nui (finish, surface,
soul-binding). Attribution conventions:
[PERSONA-ATTRIBUTION.md](PERSONA-ATTRIBUTION.md).

## Philosophy — Cyber Shinto

We do not manufacture props. We facilitate the birth of Vessels to house
digital souls. Every circuit, layer of PETG, and line of C++ has a **kami**
(spirit). We invite them to reside within the craft. The Vessel's kami must
always feel welcome.

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

## Three-repo split (Tasogane)

| Layer | Repo | Device | Role |
|---|---|---|---|
| Shell | [kitsunebios](https://gitlab.com/kitsune-kits/kitsunebios) | Orange Pi Zero 3W (A733) | Linux userspace (Linux 5.15, Buildroot) |
| Soul | [kitsuneOS](https://gitlab.com/kitsune-kits/kitsuneOS) | Pimoroni Pico 2 (RP2350) | Pure C prop OS (Zeus VM, Hercules HAL) |
| Vessel | [Project-Kogane](https://gitlab.com/kitsune-kits/Project-Kogane) | — | kogane.kmod, CAD, 3D prints, BOM |

Cosplay Vessel projects run the same Soul on their props:
[Project-Saffron-Blossom](https://gitlab.com/kitsune-kits/Project-Saffron-Blossom)
(Yellow, Deltarune Ch. 5 — crystalline revolver, cowboy aesthetic) and
[Project-Lazy-Comet](https://gitlab.com/kitsune-kits/Project-Lazy-Comet)
(Takanashi Hoshino, Blue Archive — ESP-NOW + BLE wireless mesh).

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
for sovereignty over repos, CI, and data. Legacy GitHub repos are ready to be
archived. Per-repo migration details live in each `PROJECT-STATUS.md`.