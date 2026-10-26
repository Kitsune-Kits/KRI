# PROJECT-STATUS — KRI (org context hub)

> **Last updated:** 2026-10-26 (P4 face-wing display doctrine, ADR-0007) · **Maintained by:** KRI (Kitsune Research Industries)
> **Read this first when starting a new chat** — org-wide state lives here.

## Overview

| Field | Value |
|---|---|
| **Project** | KRI — org-wide context hub for the kitsune-kits group |
| **Role** | Agent standards, org context, persona attribution, repo index, decisions |
| **CI pipeline** | `agents-guard` (shared template, ADR-0006) + `repo-link-check` (both non-blocking) |
| **GitLab URL** | https://gitlab.com/kitsune-kits/kri |

## Repo states (at a glance)

Live per-repo state lives in each repo's `PROJECT-STATUS.md` — read it there,
not from memory of this table.

| Repo | Role | Phase |
|---|---|---|
| [kitsunebios](https://gitlab.com/kitsune-kits/kitsunebios) | Shell | v0.4 — boot-to-CLI in progress |
| [kitsuneOS](https://gitlab.com/kitsune-kits/kitsuneOS) | Soul | **Rust-primary** (ADR-0004, 2026-09-23) — workspace compiles, rust-check blocking, C reference frozen |
| [Project-Kogane](https://gitlab.com/kitsune-kits/Project-Kogane) | Vessel | Tasogane build + testbench — rewired to cargo firmware build (ADR-0004) |
| [Project-Saffron-Blossom](https://gitlab.com/kitsune-kits/Project-Saffron-Blossom) | Cosplay Vessel | M1 — electronics design (deadline 2027-10-31) |
| [Project-Lazy-Comet](https://gitlab.com/kitsune-kits/Project-Lazy-Comet) | Cosplay Vessel | Debuted May 2026 |
| [Study-First-Light](https://gitlab.com/kitsune-kits/Study-First-Light) | Study 001a | S1 foundation done; S2 KMOD outline merged |

## Current initiatives

- **Fall break push (week of Sept 21, 2026):** Architect creates labels +
  milestones in the GitLab UI (see SETUP-UI-CHECKLIST.md), then heavy project
  work across repos.
- **Agent guidance (done, Sept 16):** repo-specific `AGENTS.md` + `CLAUDE.md`
  on every repo; org standard here.
- **Anti-rot guard (done, Sept 16):** `agents-guard` CI job on every repo
  (non-blocking) — verifies guidance files exist, KRI link resolves, and
  warns when `PROJECT-STATUS.md` is >30 days stale.
- **Decision log (done, Sept 16):** ADR convention in `docs/decisions/`.
- **Rust-primary switchover (Sept 23, kitsuneOS ADR-0004):** Rust is canonical; rust-check blocking; C-only CI jobs retired; C tree frozen as the R2 golden-harness reference. Kogane rewired (build.sh --firmware → cargo). **Manual step pending:** create the `legacy/c-reference` tag in the kitsuneOS GitLab UI (connector cannot create tags). Commits: kitsuneOS `2fe60c15`, Kogane `90274f4a`.
- **Study tier + Study 001a: First Light (Sept 23):** ADR-0005 defines the
  Study tier and numbering; STUDIES.md is the canonical index. First Light is
  a buildable in-universe lightsaber on kitsuneOS with the NFC kyber-crystal
  doctrine. Repo created 2026-09-23; foundation seeded, KMOD crystal-handshake outline merged (MR !1).

- **Shared CI templates (Oct 13, ADR-0006):** the agents-guard job and the minimal security stage now live in `.gitlab/templates/` here; sibling repos include them instead of carrying copies. Fixes the escaped-variable bug that silently disabled the KRI-link check. Sibling repos adopt via their own `piko/ci-streamline` MRs.
- **P4 face-wing display doctrine (Oct 26, ADR-0007):** any KRI prop requiring a display uses an ESP32-P4 face wing on the principles of Project-Kogane ADR-0002 — kami stays on the RP2350 Soul, LVGL over MIPI-DSI with capacitive touch, Rust-on-ESP-IDF, face wing doubles as bench instrument and at-con authoring surface. kitsunebiOS stays retired. First application: Kogane (gated G1–G3); Saffron Blossom and Lazy Comet adopt next.

## Manual setup remaining (GitLab UI)

See [SETUP-UI-CHECKLIST.md](SETUP-UI-CHECKLIST.md) — labels, milestones,
issue boards, MR approval rules, protected branches, GitHub archiving.
**Wiki population is now scripted:** every repo (2026-09-23) carries
`.gitlab/wiki/*.md` content plus `.gitlab/scripts/populate-wiki.sh` — one
command clones the wiki repo and pushes all pages. kitsunebios and kri got
wiki content for the first time; the four older repos were restyled
(front-matter titles, breadcrumb nav, brand footer). Commits: Saffron
`210812d9`, kitsuneOS `1174a7a7`, Lazy Comet `76f36b4a`, Kogane `06f87b9f`,
kitsunebios `063ac953`, kri `496007b2`.