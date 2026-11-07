# PROJECT-STATUS.md — pocket-forge (KRI hub subproject)

Single source of truth for where this subproject is. Updated at every milestone.

| Field | Value |
| --- | --- |
| Home | `Kitsune-Kits/KRI` → `pocket-forge/` (per the Architect's word, 2026-11-07) |
| Phase | v0.1 — scaffold, first live run pending |
| Date | 2026-11-07 |

## Build overview

The KRI ensemble as Managed Agents (`mistralai-agents==1.1.0`, public
preview): 🦊 Coco Sensei as the root agent at the front door, 🔨 Zaku /
⚡ Piko / ✨ Nui as subagents cast by craft. Talk and work in one agent:
typed GitHub REST tools (reads allowed, writes gated behind the
Architect's word), persona attribution per the ratified org standard,
interactive approval stepper in `main.py`.

## Current state

- ✅ Ensemble architecture: root + three subagents, `Builtins(subagents=False)` on the cubs.
- ✅ GitHub tools: 10 read (allowed), 8 write (ask); permission policy `default="ask"`.
- ✅ Persona canon embedded: locked identities, voices, forge law, attribution.
- ✅ Interactive session loop with terminal approvals (`python main.py`).
- ⏳ First live session on the bench (needs `MISTRAL_API_KEY` + `GITHUB_TOKEN`).

## Open dependencies (all pending the Architect's word)

- LICENSE: org repos converted to proprietary — this repo needs its license
  decision recorded.
- First live run + approvals exercised against a scratch branch.
- `agents deploy` decision (Mistral-managed vs self-hosted).
- `MistralSandbox` + secrets posture for deployed sessions.
- Ledger tools (forge diary) and KRI skills as follow-ups.
- Org manual setup for this repo (branch protection, labels) — connector cannot.

## Cross-repo context

- Org namespace: `Kitsune-Kits` on GitHub (ADR-0007); GitLab mirrors read-only.
- This subproject consumes nothing at build time; its agents *operate on* the org
  repos (kitsuneOS, Project-Kogane, etc.), so a misbehaving write gate is a
  blast-radius concern for all seven.
- The hub's own status board lives at the KRI repo root `PROJECT-STATUS.md`;
  this file tracks the subproject only.
- Org standards: [AGENTS.md](https://github.com/Kitsune-Kits/KRI/blob/main/AGENTS.md),
  [PERSONA-ATTRIBUTION.md](https://github.com/Kitsune-Kits/KRI/blob/main/PERSONA-ATTRIBUTION.md).

## Session log

- **2026-11-07** — v0.1 scaffold committed (ensemble architecture, canon,
  GitHub tools, approval stepper, docs). First live run pending.
