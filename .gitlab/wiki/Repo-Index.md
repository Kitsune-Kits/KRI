---
title: Repo Index
---

---
title: Repo Index
---
# Repo Index

> 🦊 **kri Wiki** · [Home](Home) · [Operating Principles](Operating-Principles) · [Glossary](Glossary) · [Decisions](Decisions)


Every repository in the kitsune-kits group.

| Repo | Layer | Role |
|---|---|---|
| [kitsunebios](https://gitlab.com/kitsune-kits/kitsunebios) | Shell | Linux userspace (Orange Pi Zero 3W, A733) |
| [kitsuneOS](https://gitlab.com/kitsune-kits/kitsuneOS) | Soul | Pure C prop OS (RP2350) |
| [Project-Kogane](https://gitlab.com/kitsune-kits/Project-Kogane) | Vessel | Tasogane gunblade + testbench |
| [Project-Saffron-Blossom](https://gitlab.com/kitsune-kits/Project-Saffron-Blossom) | Cosplay Vessel | Yellow (Deltarune Ch. 5) build — deadline 2027-10-31 |
| [Project-Lazy-Comet](https://gitlab.com/kitsune-kits/Project-Lazy-Comet) | Cosplay Vessel | Hoshino (Blue Archive) mesh prop system — debuted May 2026 |

Each repo carries its own repo-specific `AGENTS.md`, a living `PROJECT-STATUS.md` (read it there, not from memory), GitLab-native templates, and a `populate-wiki.sh` script for its wiki.

## Cross-Repo Rules

- **One repo at a time.** Never hold uncommitted changes in two repos.
- **Know the blast radius.** kitsuneOS is pulled at build time by Project-Kogane — breaking kitsuneOS `main` breaks three repos.
- **Nothing vendored.** Upstream code is fetched at build time; never commit it. (Exception: kitsuneOS vendors `lua-5.5.1/` deliberately.)

---

> 🦊 **Kitsune Research Industries** — *Tradition is the structure; the future is the light.*
> This page mirrors `.gitlab/wiki/Repo-Index.md` in the [kri repository](https://gitlab.com/kitsune-kits/kri) — edit it there, then re-run `.gitlab/scripts/populate-wiki.sh` to update the wiki.
