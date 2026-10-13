# AGENTS.md — Kitsune Kits org-wide agent standard

Operating standard for AI coding agents working anywhere in the kitsune-kits
GitLab group. Each repo carries its own repo-specific `AGENTS.md`; this file
holds what is shared. **Read both before working.**

## Grounding order (any repo)

1. The repo's `PROJECT-STATUS.md` — single source of truth for where things are.
2. The repo's `README.md`.
3. The repo's `AGENTS.md` — repo-specific rules, repo map, watch-outs.
4. This file, plus the repo's `.gitlab/DEV-WORKFLOW.md`.
5. [ORGANIZATION-SYSTEM.md](ORGANIZATION-SYSTEM.md) — how KRI files, tags,
   tools, and media are organized. Consult before creating, naming, moving,
   or tagging any KRI file or asset.
6. The brand canon — [BRAND.md](BRAND.md) (color),
   [BRAND-TYPOGRAPHY.md](BRAND-TYPOGRAPHY.md) (lettering),
   [BRAND-AESTHETIC.md](BRAND-AESTHETIC.md) (design language),
   [BRAND-WORDMARK.md](BRAND-WORDMARK.md) (the mark). Apply to any
   user-facing surface: docs, badges, web, UI, Vessel finishes, media.

## Context rot mitigation — mandatory for big operations

Long agentic sessions degrade: earlier instructions fade, details blur, and
confidence outgrows accuracy. These rules are mandatory for any operation
spanning more than a handful of steps:

- **Verify, don't assume.** Never trust memory — from a previous session or
  from earlier in the current one — for file contents, repo state, or past
  decisions. Re-read the file, re-list the tree, re-check the pipeline.
- **Checkpoint to disk, not memory.** Commit after every coherent step. When a
  milestone completes, update the repo's `PROJECT-STATUS.md`. Anything not
  written to the repo must be assumed lost between sessions.
- **Small, resumable steps.** Break large operations into steps that are each
  independently correct. Each step must leave the branch in a valid state so
  an interrupted operation can be resumed or safely rolled back.
- **Idempotence before redoing.** If unsure whether a step already happened,
  check the repo (file tree, commit history, pipeline history) before doing it
  again. Never redo work just in case.
- **Read narrowly.** Prefer targeted reads (one file, a line window, a search)
  over loading whole directories into context. Big context invites rot.
- **Write decisions down.** Record mid-operation choices (naming, structure,
  scope) in the commit message, MR description, issue, or `PROJECT-STATUS.md` —
  never only in the conversation.
- **Summarize at handoff.** When finishing or pausing an operation, leave a
  short note of what changed and what is next, so the next session re-grounds
  in one read.
- **Treat connector errors as unverified.** The GitLab connector has reported
  false commit failures (the commits actually landed). On any error: verify
  actual state (file tree, file contents) before retrying — blind retries can
  duplicate work.

## Cross-repo operation protocol

- **One repo at a time.** Never hold uncommitted changes in two repos
  simultaneously. Checkpoint (commit + status update) in one repo before
  moving to the next.
- **Know the blast radius.** kitsuneOS is pulled at build time by
  Project-Kogane (CMake FetchContent) and used by Project-Saffron-Blossom and
  Project-Lazy-Comet — breaking kitsuneOS `main` breaks three repos.
- **Nothing vendored.** Upstream code (kernel, LVGL, musl, BusyBox, U-Boot)
  is fetched at build time; never commit upstream code into our repos.
  Exception: kitsuneOS vendors `lua-5.5.1/` deliberately.

## Git & attribution

- Default branch: `main`. Org namespace: `kitsune-kits` on gitlab.com.
- Lifecycle (each repo's `.gitlab/DEV-WORKFLOW.md`):
  Plan → Branch → Code → Commit → Review → Merge → CI/CD → Deploy.
- KRI persona attribution — branch prefixes (`coco/`, `zaku/`, `piko/`,
  `nui/`), `KRI-Persona:` and `Co-authored-by:` trailers:
  [PERSONA-ATTRIBUTION.md](PERSONA-ATTRIBUTION.md).
- Architectural decisions are recorded as ADRs in
  [docs/decisions/](docs/decisions/) — accepted ADRs are immutable;
  supersede rather than edit.
- Shared CI templates live in
  [.gitlab/templates/](.gitlab/templates/) — repos include them from
  this repo instead of carrying per-repo copies (ADR-0006).

## Lessons learned

- Post-incident lessons live in [docs/lessons/](docs/lessons/) —
  read them before any first hardware bring-up, and append to them
  when a new one teaches something. Current:
  [Hardware bring-up (ST7789/Tufty)](docs/lessons/hardware-bringup.md).

## Tooling via Vibe (gitlab_4be8 connector)

**Can do:** file read/write, commits, branches, merge requests
(create/review/approve/merge), issues/work items, pipelines
(run/retry/cancel/check), search (code/issues/MRs/commits), labels (read),
wiki (list/read).

**Cannot do (manual GitLab UI required):** create projects, create labels,
create milestones, create issue boards, set protected branches, configure MR
approval rules, write wiki pages, archive repos.

## Do-not-touch list (org-wide)

- `.github/scripts/` directories — intentionally retained; referenced by
  `.gitlab-ci.yml`.
- Historical references in `CHANGELOG.md`, `LICENSE`, `SECURITY.md`, and older
  docs (brand names, historical fix notes).
- Known-failing non-blocking CI jobs — intentional on the free tier; don't
  fix them by making them blocking.
- kitsunebios locked key decisions (see that repo's `AGENTS.md`).
- This repo is the org standard — propose changes via MR rather than
  rewriting unilaterally.