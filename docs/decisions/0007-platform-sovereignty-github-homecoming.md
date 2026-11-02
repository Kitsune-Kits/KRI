# ADR-0007: Platform sovereignty — the GitHub homecoming

- **Status:** Accepted
- **Date:** 2026-11-02
- **Persona:** 🦊 Coco (lead)
- **Scope:** org-wide

## Context

The September 2026 migration moved all seven repos to
gitlab.com/kitsune-kits — driven by free-tier CI minutes, group
tooling, and wiki features. That posture was recorded in each repo's
`PROJECT-STATUS.md` ("Migration History"), never as an ADR; it made
GitLab the canonical home and GitHub the archive-bound past.

The forces changed by November 2026:

- The Architect's GitHub presence is the org home now: the
  **Kitsune-Kits** organization holds all seven repos (mirrored
  2026-11-01 — every branch and tag), with Vibe's GitHub App
  connector installed at org level.
- GitHub Actions was proven against the full org CI translation
  (2026-11-01 → 11-02): all seven repos translated, every blocking
  gate green on the runners, the kri hub's reusable workflow called
  from every sibling (ADR-0006 pattern carried over).
- The AWA 2026 debut (Nov 19–22; bench integration test Nov 6)
  makes platform risk-reduction urgent: one canonical home, one CI
  system, before the world watches.
- The C/Lua estate retirement (the Architect's ruling, 2026-11-01)
  landed on GitHub main branches only; the estates are archive-bound
  either way.

## Decision

1. The GitHub organization **Kitsune-Kits** is the canonical home for
   all Kitsune Kits repos. gitlab.com/kitsune-kits remains as a
   read-only safety mirror — un-archived until after the AWA 2026
   debut — and is archived after a post-AWA review.
2. CI runs on **GitHub Actions**. The translated
   `.github/workflows/` pipelines are live; per-repo
   `.gitlab-ci.yml` files stay dormant in-tree until the post-AWA
   archive decision.
3. The kri shared-template hub pattern (ADR-0006) continues on
   GitHub: `.github/workflows/agents-guard.yml` is the live
   reusable workflow (`uses: Kitsune-Kits/KRI/...`); the
   `.gitlab/templates/` equivalents stay dormant alongside it. The
   hub's org Access setting grants sibling repos the right to call
   the private reusable workflow.
4. This supersedes the September 2026 GitLab-canonical posture as
   recorded in every repo's `PROJECT-STATUS.md`. Canonical URLs in
   operational docs point at github.com/Kitsune-Kits; GitLab URLs in
   historical records are intentionally left as history.

## Consequences

- A link/reference pass across all repos moves operational links to
  github.com/Kitsune-Kits (in flight 2026-11-02).
- Pages deployments need one-time enablement (Settings → Pages →
  Source: GitHub Actions) on every repo with a Pages job.
- The GitLab group becomes archive-bound after AWA 2026; the GitLab
  connector retires from live workflows once the archive decision
  is taken.
- Blast radius: all seven repos plus the kri hub. A breaking change
  to the hub's reusable workflow reaches every sibling at its next
  pipeline — keep the hub minimal and additive (the ADR-0006
  discipline carries over unchanged).
