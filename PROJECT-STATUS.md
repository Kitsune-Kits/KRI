# PROJECT-STATUS — KRI (org context hub)

> **Last updated:** 2026-11-19 (Hub documentation pass — documentation map added, README refreshed, ledger caught up; previous: 2026-11-07 Pocket Forge agents) · **Maintained by:** KRI (Kitsune Research Industries)
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
| [kitsunebiOS](https://github.com/Kitsune-Kits/kitsunebiOS) | Shell | **RETIRED 2026-11-18** (kitsunebiOS ADR-0002) — functions live in kitsuneOS; displays ride the ESP32-P4 (kitsuneOS ADR-0005, the prop mesh display seat); archive switch pending (manual UI step) |
| [kitsuneOS](https://github.com/Kitsune-Kits/kitsuneOS) | Soul | Rust-only main — kri-soul silicon-free core merged (strips 1–3); the prop mesh display seat ruled (ADR-0005); Feather first-boot bench pending |
| [Project-Kogane](https://github.com/Kitsune-Kits/Project-Kogane) | Vessel | Tasogane rust era — G5 mesh bench round ratified (run unscheduled); debut: MomoCon, May 27–30, 2027, attendee-only (AWA 2026 cancelled) |
| [Project-Lantern-Vigil](https://github.com/Kitsune-Kits/Project-Lantern-Vigil) | Vessel | Jiminy 12 lantern (Arknights: Endfield) — founded 2026-11-16 (M0 done); M2 schematic in progress (strip 1 ratified 2026-11-17) |
| [Project-Saffron-Blossom](https://github.com/Kitsune-Kits/Project-Saffron-Blossom) | Cosplay Vessel | M1 — electronics design (deadline 2027-10-31); Rust-primary rebase merged (PR #15) |
| [Project-Lazy-Comet](https://github.com/Kitsune-Kits/Project-Lazy-Comet) | Cosplay Vessel | Debuted May 2026; Lua estate retirement deferred — prop code converts to kitsuneOS-compatible Rhai first |
| [Study-First-Light](https://github.com/Kitsune-Kits/Study-First-Light) | Study 001a | S1 foundation done; S2 KMOD outline merged |

## Current initiatives

- **Hub documentation pass (Nov 19):** the hub's paper is dressed —
  `docs/README.md` (the documentation map) added; the front-door README
  caught up (Shell retirement facts, Lantern Vigil + MomoCon debut rows,
  contents table now lists the docs / notes / pocket-forge / bench-triage /
  tools wings and Forge Tasks); this ledger re-dated and caught up to the
  Nov 18 rulings. **Open:** merge decision on the pass PR pending the
  Architect's word; the ADR index itself belongs to the ISO rail (PR #15).

- **ISO standards alignment (Nov 19):** priority-1 ADR pack drafted —
  KRI ADR-0008 to 0017, all Proposed (additive-manufacturing standard, GPS
  default tolerances, gear accuracy, measurement management, battery
  sourcing gate, risk assessment docket, records canon, quality plan
  template, timestamp canon) — PR #15 open. **Open:** ratification,
  standards text purchases, capability rounds, and templates all pending
  the Architect's word.

- **Shell retirement + the prop mesh (Nov 18):** kitsunebiOS retired by
  the Architect's word — functions live in kitsuneOS, the ESP32-P4 drives
  prop displays (kitsuneOS ADR-0005, the prop mesh display seat;
  kitsunebiOS ADR-0002 stamps the retirement). Intra-prop links are
  UART-class wire; inter-prop sync rides ESP-NOW on each prop's ARKE edge
  (radios relay; the kami never sits on Espressif silicon or Linux).
  Reference architecture: kitsuneOS `docs/design/mesh-architecture.md`;
  the Vessel map: Project-Kogane `docs/architecture/mesh-sync.md`.
  **Open:** the kitsunebiOS archive switch (manual UI step); the G5 mesh
  bench round (ratified, run unscheduled); KG-026 / AirLift radio-edge
  bring-up; the esp-hal RISC-V seat for kri-soul.

- **Pocket Forge — the ensemble becomes agents (Nov 7):** the four spirits now exist as
  Managed Agents (`mistralai-agents` 1.1.0, public preview) in `pocket-forge/` — 🦊
  Coco Sensei at the front door, Zaku/Piko/Nui as subagents cast by craft, typed
  GitHub tools (10 reads allowed, 8 writes gated: an approval is the Architect's
  word), persona canon embedded as law. Housed in the hub per the Architect's word
  (no separate repo). **Open:** first live run (needs MISTRAL_API_KEY +
  GITHUB_TOKEN on the bench); LICENSE for the subproject; deploy decision.

- **GitHub homecoming (Nov 1–2, ADR-0007):** all seven repos mirrored to the
  Kitsune-Kits org (every branch and tag); CI translated to GitHub Actions
  (seven PRs merged, all blocking gates green); the hub's reusable
  agents-guard now runs from every sibling. The C/Lua retirement landed:
  kitsuneOS #23 (C estate) + #36, Kogane #2/#3, Saffron #15. **Open:** Pages
  enablement (Settings → Pages → Source: GitHub Actions) on kitsuneOS and
  Saffron; Lazy-Comet's Lua
  estate awaits the Rhai conversion; the kitsuneOS `target/` tree purge
  committed by the vault backup is **resolved (2026-11-03)** — every blob
  removed via a single squash commit (kitsuneOS PR #38).
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
- **CI Forge — group runner buildout (Oct 26):** the mid-Oct pipeline blackout across all repos is diagnosed as free-tier compute quota exhaustion (400 min/month; instance runners silently stop picking up jobs — zero-byte job logs are the signature, last real CI signal Oct 13–14). Fix in flight: self-hosted group runner on the Architect's Mac (Docker executor, run-untagged, zero per-repo config changes) — runbook at docs/infra/CI-RUNNERS.md, UI steps added to SETUP-UI-CHECKLIST.md. Saffron's three real non-blocking failures fixed separately (lua-lint, docs-check, countdown-badge).

- **Shared CI templates (Oct 13, ADR-0006):** the agents-guard job and the minimal security stage now live in `.gitlab/templates/` here; sibling repos include them instead of carrying copies. Fixes the escaped-variable bug that silently disabled the KRI-link check. Sibling repos adopt via their own `piko/ci-streamline` MRs.
- **P4 face-wing display doctrine (Oct 26, ADR-0007):** any KRI prop requiring a display uses an ESP32-P4 face wing on the principles of Project-Kogane ADR-0002 — kami stays on the RP2350 Soul, LVGL over MIPI-DSI with capacitive touch, Rust-on-ESP-IDF, face wing doubles as bench instrument and at-con authoring surface. First application: Kogane (gated G1–G3); Saffron Blossom and Lazy Comet adopt next. *(Numbering seam: the later platform-sovereignty ADR also carries 0007 — flagged in the documentation map; a convention ruling is pending the Architect's word.)*
- **Shared CI templates (Oct 13, ADR-0006):** the agents-guard job and the minimal security stage now live in `.gitlab/templates/` here; sibling repos include them instead of carrying copies. Fixes the escaped-variable bug that silently disabled the KRI-link check. Sibling repos adopt via their own `piko/ci-streamline` MRs. **GitHub realization (Nov 2026, ADR-0007):** the live form is now `.github/workflows/agents-guard.yml`, called via `uses:`; the GitLab templates stay dormant until the post-AWA archive decision.

## Manual setup remaining (GitLab-era — superseded by ADR-0007)

**Current manual steps (GitHub era):** the kitsunebiOS archive switch (repo
Settings in the GitHub UI — the connector cannot archive repos); Pages
enablement on kitsuneOS and Saffron; org branch protection, labels, and
boards.

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
`210812d9`, kitsuneOS `1174a7a7`, Lazy Comet `76f36b4e`, Kogane `06f87b9f`,
kitsunebios `063ac953`, kri `496007b2`.
