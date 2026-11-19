# 🦊 Kitsune Research Industries (KRI)

> *The forge is the forge. The Ledger gives information its soul.*

Org-wide context hub for the [Kitsune-Kits](https://github.com/Kitsune-Kits)
GitHub organization (kri ADR-0007 — the GitHub homecoming); the
[kitsune-kits GitLab group](https://gitlab.com/kitsune-kits) is the read-only
mirror until the post-AWA archive review. This repo holds no product code —
it holds everything shared: the agent operating standard, persona
attribution, org context, the brand canon, and the repo index.

[![CI](https://github.com/Kitsune-Kits/KRI/actions/workflows/ci.yml/badge.svg)](https://github.com/Kitsune-Kits/KRI/actions/workflows/ci.yml)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-0E1113.svg?labelColor=C9A227)](LICENSE)
[![Kitsune Modern](https://img.shields.io/badge/KRI-Kitsune_Modern-C9A227.svg?labelColor=0E1113)](https://github.com/Kitsune-Kits/KRI/blob/main/BRAND-AESTHETIC.md)

---

## Contents

| File | Purpose |
|---|---|
| `AGENTS.md` | Org-wide AI agent operating standard — read before working in any repo |
| `CLAUDE.md` | Claude Code entrypoint (imports AGENTS.md) |
| `ORG-CONTEXT.md` | What KRI is: philosophy, glossary, repo split, pull graph, history |
| `ORGANIZATION-SYSTEM.md` | How KRI organizes files: pillars, tags, sync, media toolchain, shortcuts — consult before touching files |
| `PERSONA-ATTRIBUTION.md` | KRI ensemble attribution standard |
| `BRAND.md` | Brand palette canon — five-color core + persona sub-palettes (ADR-0001) |
| `BRAND-TYPOGRAPHY.md` | Typography canon — KRI Sans/Mincho/Mono, size scale (ADR-0002) |
| `BRAND-AESTHETIC.md` | Design language — Kitsune Modern: tradition is the structure, the future is the light (ADR-0003) |
| `BRAND-WORDMARK.md` | Wordmark & seal spec — the hanko (ADR-0004) |
| `STUDIES.md` | Index of Studies — the tier canon (ADR-0005) |
| `Forge Tasks.md` | The task layer — Git-canonical Now / Next / Someday; Task Hub reads it, never owns it |
| `docs/` | Documentation map ([docs/README.md](docs/README.md)) — the decision log (ADRs), infra runbooks, lessons, proposals |
| `notes/` | Obsidian vault layer over the repos — the three laws live in [VAULT.md](notes/VAULT.md); front door [Home.md](notes/Home.md), org digest [Forge Notes.md](notes/Forge%20Notes.md), Kitsune Modern theme |
| `pocket-forge/` | The ensemble as Managed Agents — the four spirits as a deployable scaffold; keeps its own `README.md` and `PROJECT-STATUS.md` |
| `bench-triage/` | Bench session triage tool |
| `tools/` | Forge tooling — git identity, persona router, Apple Reminders MCP, VSCodium branding |
| `SETUP-UI-CHECKLIST.md` | GitLab-era UI setup checklist (historical — kept for history) |
| `LICENSE` | Proprietary license — © 2026 KRI / Kitsune Kits |

Every page of the hub's paper is mapped in the
[documentation map](docs/README.md).

---

## Repos

| Repo | Role |
|---|---|
| [kitsuneOS](https://github.com/Kitsune-Kits/kitsuneOS) | Soul — the prop OS for RP2350 (Rust-primary, ADR-0004); in the prop mesh, displays ride the ESP32-P4 (ADR-0005) |
| [kitsunebiOS](https://github.com/Kitsune-Kits/kitsunebiOS) | Shell — **RETIRED 2026-11-18** (kitsunebiOS ADR-0002): functions live in kitsuneOS; kept as history until the archive review |
| [Project-Kogane](https://github.com/Kitsune-Kits/Project-Kogane) | Vessel — the Tasogane gunblade + testbench; debut: MomoCon, May 27–30, 2027 (attendee-only) |
| [Project-Lantern-Vigil](https://github.com/Kitsune-Kits/Project-Lantern-Vigil) | Vessel — the Jiminy 12 lantern (Arknights: Endfield); Standard Issue / Vigil Prime tiers |
| [Project-Saffron-Blossom](https://github.com/Kitsune-Kits/Project-Saffron-Blossom) | Yellow (Deltarune Ch. 5) cosplay Vessel |
| [Project-Lazy-Comet](https://github.com/Kitsune-Kits/Project-Lazy-Comet) | Hoshino (Blue Archive) mesh prop system |
| [Study-First-Light](https://github.com/Kitsune-Kits/Study-First-Light) | Study 001a — First Light (ADR-0005) |

Each repo carries its own repo-specific `AGENTS.md` and a living
`PROJECT-STATUS.md` — live state lives there, never in memory of this page.
The pull graph is one-way ([ORG-CONTEXT.md](ORG-CONTEXT.md)): the Vessels
pull kitsuneOS at build time; intra-prop links are UART-class wire and
inter-prop sync rides ESP-NOW on the ARKE radio edge — the kami never sits
on Espressif silicon or Linux.

---

## Cyber Shinto

We do not manufacture props. We facilitate the birth of Vessels to house
digital souls. Every circuit, layer of PETG, and line of code has a kami.
Full glossary: [ORG-CONTEXT.md](ORG-CONTEXT.md).

---

## License

Proprietary — © 2026 Kitsune Research Industries (KRI) / Kitsune Kits.
All rights reserved. See [LICENSE](LICENSE).

---

*Built by Kitsune Research Industries (KRI).*
*Coco Sensei · Zaku · Piko · Nui*
