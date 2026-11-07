# AGENTS.md — pocket-forge subproject standard

Subproject rules for AI coding agents working in `pocket-forge/` (a
subproject of the KRI hub repo, per the Architect's word, 2026-11-07).
The org-wide standard lives in this same repo's root — read both before
working: [AGENTS.md (org standard)](../AGENTS.md).

## What this subproject is

The KRI ensemble as Managed Agents (`mistralai-agents` SDK, public preview):
Coco Sensei as the root agent, Zaku / Piko / Nui as subagents, typed GitHub
REST tools with writes gated behind approvals. It is *both* a conversation
partner and a working agent for the `Kitsune-Kits` organization.

## Grounding order

1. [PROJECT-STATUS.md](PROJECT-STATUS.md) — source of truth.
2. [README.md](README.md) — what it is, how it runs.
3. This file.

## Repo map

| Path | Role |
| --- | --- |
| `main.py` | Entry point; interactive session with the approval stepper. Defines `agent` for `agents chat`. |
| `forge/canon.py` | Shared law every spirit carries (doctrine, Architect's word, grounding, attribution, voice). |
| `forge/personas.py` | The four identity blocks (CANON) and `build_forge_agent()`. |
| `forge/github_tools.py` | Typed GitHub REST tools; `READ_TOOL_IDS` / `WRITE_TOOL_IDS` feed the permission policy. |

## Conventions

- Apple-style documentation comments (file banners, doc blocks, section
  dividers) — the org standard.
- KRI persona attribution on every commit and PR — the ratified standard:
  [PERSONA-ATTRIBUTION.md](https://github.com/Kitsune-Kits/KRI/blob/main/PERSONA-ATTRIBUTION.md).
- Conventional commits; branches use persona prefixes.

## Watch-outs

- **Canon is not style.** The persona text in `forge/personas.py` and
  `forge/canon.py` (colors, tail counts, ages, voice, laws) is locked.
  "Tidying" it is a canon violation — changes are ADR-grade, pending the
  Architect's word.
- The SDK is **public preview**: its API and the pinned version
  (`mistralai-agents==1.1.0`) can change; an upgrade is a deliberate
  two-line change, tested on the bench first.
- Permission rules match **tool IDs** (`client.gh_write_file`), not the
  names the model calls. New tools must be added to `READ_TOOL_IDS` or
  `WRITE_TOOL_IDS` — an unlisted write falls to `default="ask"`, which is
  the safe direction.
- `.env` never leaves the machine: it holds the forge's keys.
- Deployed, a write tool can be retried after a crash — keep tools
  idempotent where the GitHub API allows (check-before-write, expected
  sha on updates).

## Do-not-touch list

- The `.env.example` scopes wording (matches the org token posture).
- Nothing vendored; the SDK comes from PyPI.
