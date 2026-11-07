# PROJECT-STATUS — KRI (org context hub)

> **Last updated:** 2026-10-26 (P4 face-wing display doctrine, ADR-0007) · **Maintained by:** KRI (Kitsune Research Industries)
> **Last updated:** 2026-11-02 (GitHub homecoming — ADR-0007 + hub/repo link pass; previous: 2026-10-13 shared CI templates, ADR-0006) · **Maintained by:** KRI (Kitsune Research Industries)
> **Read this first when starting a new chat** — org-wide state lives here.

## Overview

| Field | Value |
|---|---|
| **Project** | KRI — org-wide context hub for the Kitsune-Kits organization |
| **Role** | Agent standards, org context, persona attribution, repo index, decisions |
| **CI pipeline** | GitHub Actions: `agents-guard` (reusable workflow, ADR-0006/0007) + `repo-link-check` (both non-blocking) |
| **GitHub URL** | https://github.com/Kitsune-Kits/KRI · mirror (read-only until post-AWA): https://gitlab.com/kitsune-kits/kri |

## Repo states (at a glance)

Live per-repo state lives in each repo's `PROJECT-STATUS.md` — read it there,
not from memory of this table.

| Repo | Role | Phase |
|---|---|---|
| [kitsunebiOS](https://github.com/Kitsune-Kits/kitsunebiOS) | Shell | v0.4 — boot-to-CLI in progress |
| [kitsuneOS](https://github.com/Kitsune-Kits/kitsuneOS) | Soul | **Rust-only main** — C estate retired to `legacy/c-reference` (PR #23, 2026-11-02) |
| [Project-Kogane](https://github.com/Kitsune-Kits/Project-Kogane) | Vessel | Tasogane rust-era — pico-firmware retired (PR #2) |
| [Project-Saffron-Blossom](https://github.com/Kitsune-Kits/Project-Saffron-Blossom) | Cosplay Vessel | M1 — electronics design (deadline 2027-10-31); Rust-primary rebase merged (PR #15) |
| [Project-Lazy-Comet](https://github.com/Kitsune-Kits/Project-Lazy-Comet) | Cosplay Vessel | Debuted May 2026; Lua estate retirement deferred — prop code converts to kitsuneOS-compatible Rhai first |
| [Study-First-Light](https://github.com/Kitsune-Kits/Study-First-Light) | Study 001a | S1 foundation done; S2 KMOD outline merged |

## Current initiatives

- **GitHub homecoming (Nov 1–2, ADR-0007):** all seven repos mirrored to the
  Kitsune-Kits org (every branch and tag); CI translated to GitHub Actions
  (seven PRs merged, all blocking gates green); the hub's reusable
  agents-guard now runs from every sibling. The C/Lua retirement landed:
  kitsuneOS #23 (C estate) + #36, Kogane #2/#3, Saffron #15. **Open:** Pages
  enablement (Settings → Pages → Source: GitHub Actions) on kitsuneOS and
  Saffron; Lazy-Comet's Lua
  estate awaits the Rhai conversion; a vault-backup committed cargo's
  `target/` tree to kitsuneOS main (now gitignored — bulk removal pending
  the Architect's word; one `git rm -r target/` from the bench clone is the
  clean single-commit cure).
- **Fall break push (week of Sept 21, 2026):** Architect creates labels +
  milestones in the GitLab UI (see SETUP-UI-CHECKLIST.md), then heavy project
  work across repos.
- **Agent guidance (done, Sept 16):** repo-specific `AGENTS.md` + `CLAUDE.md`
  on every repo; org standard here.
- **Anti-rot guard (done, Sept 16):** `agents-guard` CI job on every repo
  (non-blocking) — verifies guidance files exist, KRI link resolves, and
  warns when `PROJECT-STATUS.md` is >30 days stale.
- **Decision log (done, Sept 16):** ADR convention in `docs/decisions/`.
- **Rust-primary switchover (Sept 23, kitsuneOS ADR-0004):** Rust is canonical; rust-check blocking; C-only CI jobs retired; C tree frozen as the R2 golden-harness reference. Kogane rewired (build.sh --firmware → cargo). **Manual step pending:** create the `legacy/c-reference` tag in the kitsuneOS UI (connector cannot create tags). Commits: kitsuneOS `2fe60c15`, Kogane `90274f4a`.
- **Study tier + Study 001a: First Light (Sept 23):** ADR-0005 defines the
  Study tier and numbering; STUDIES.md is the canonical index. First Light is
  a buildable in-universe lightsaber on kitsuneOS with the NFC kyber-crystal
  doctrine. Repo created 2026-09-23; foundation seeded, KMOD crystal-handshake outline merged (MR !1).

- **Shared CI templates (Oct 13, ADR-0006):** the agents-guard job and the minimal security stage now live in `.gitlab/templates/` here; sibling repos include them instead of carrying copies. Fixes the escaped-variable bug that silently disabled the KRI-link check. Sibling repos adopt via their own `piko/ci-streamline` MRs.
- **P4 face-wing display doctrine (Oct 26, ADR-0007):** any KRI prop requiring a display uses an ESP32-P4 face wing on the principles of Project-Kogane ADR-0002 — kami stays on the RP2350 Soul, LVGL over MIPI-DSI with capacitive touch, Rust-on-ESP-IDF, face wing doubles as bench instrument and at-con authoring surface. kitsunebiOS stays retired. First application: Kogane (gated G1–G3); Saffron Blossom and Lazy Comet adopt next.
- **Shared CI templates (Oct 13, ADR-0006):** the agents-guard job and the minimal security stage now live in `.gitlab/templates/` here; sibling repos include them instead of carrying copies. Fixes the escaped-variable bug that silently disabled the KRI-link check. Sibling repos adopt via their own `piko/ci-streamline` MRs. **GitHub realization (Nov 2026, ADR-0007):** the live form is now `.github/workflows/agents-guard.yml`, called via `uses:`; the GitLab templates stay dormant until the post-AWA archive decision.

## Manual setup remaining (GitLab-era — superseded by ADR-0007)

The checklist below reflects the September 2026 GitLab setup era; the
GitLab group is now the read-only mirror (ADR-0007). Kept for history —
the equivalent GitHub org settings (branch protection, labels, boards)
are the open manual setup.

See [SETUP-UI-CHECKLIST.md](SETUP-UI-CHECKLIST.md) — labels, milestones,
issue boards, MR approval rules, protected branches, archiving.
**Wiki population is now scripted:** every repo (2026-09-23) carries
`.gitlab/wiki/*.md` content plus `.gitlab/scripts/populate-wiki.sh` — one
command clones the wiki repo and pushes all pages. kitsunebios and kri got
wiki content for the first time; the four older repos were restyled
(front-matter titles, breadcrumb nav, brand footer). Commits: Saffron
`210812d9`, kitsuneOS `1174a7a7`, Lazy Comet `76f36b4a`, Kogane `06f87b9f`,
kitsunebios `063ac953`, kri `496007b2`.
