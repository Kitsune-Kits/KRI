# PROJECT-STATUS — KRI (org context hub)

> **Last updated:** 2026-09-23 · **Maintained by:** KRI (Kitsune Research Industries)
> **Read this first when starting a new chat** — org-wide state lives here.

## Overview

| Field | Value |
|---|---|
| **Project** | KRI — org-wide context hub for the kitsune-kits group |
| **Role** | Agent standards, org context, persona attribution, repo index, decisions |
| **CI pipeline** | `agents-guard` + `repo-link-check` (both non-blocking) |
| **GitLab URL** | https://gitlab.com/kitsune-kits/kri |

## Repo states (at a glance)

Live per-repo state lives in each repo's `PROJECT-STATUS.md` — read it there,
not from memory of this table.

| Repo | Role | Phase |
|---|---|---|
| [kitsunebios](https://gitlab.com/kitsune-kits/kitsunebios) | Shell | v0.4 — boot-to-CLI in progress |
| [kitsuneOS](https://gitlab.com/kitsune-kits/kitsuneOS) | Soul | Stable core; all modules complete |
| [Project-Kogane](https://gitlab.com/kitsune-kits/Project-Kogane) | Vessel | Tasogane build + testbench |
| [Project-Saffron-Blossom](https://gitlab.com/kitsune-kits/Project-Saffron-Blossom) | Cosplay Vessel | M1 — electronics design (deadline 2027-10-31) |
| [Project-Lazy-Comet](https://gitlab.com/kitsune-kits/Project-Lazy-Comet) | Cosplay Vessel | Debuted May 2026 |
| [Study-First-Light](https://gitlab.com/kitsune-kits/Study-First-Light) | Study 001a | Soul-mapped; repo creation pending (see STUDIES.md) |

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
- **Study tier + Study 001a: First Light (Sept 23):** ADR-0004 defines the
  Study tier and numbering; STUDIES.md is the canonical index. First Light is
  a buildable in-universe lightsaber on kitsuneOS with the NFC kyber-crystal
  doctrine. Repo to be created by the Architect in the GitLab UI.

## Manual setup remaining (GitLab UI)

See [SETUP-UI-CHECKLIST.md](SETUP-UI-CHECKLIST.md) — labels, milestones,
issue boards, MR approval rules, protected branches, wiki population,
GitHub archiving.