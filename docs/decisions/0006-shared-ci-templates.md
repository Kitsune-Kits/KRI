# 6. Shared CI templates (included from the kri hub)

**Date:** 2026-10-13 · **Status:** Accepted · **Lead:** ⚡ Piko (CI / build environments)

## Context

Every repo in the group carries its own copy of the CI scaffolding: the
`agents-guard` job, `.gitlab/scripts/agents-guard.sh`, and its
security-stage includes. Six copies of the guard script drifted once
already — a `\${…}` shell-escaping bug silently disabled the
KRI-link check in every repo — proving copy-pasted standards rot. The
GitLab free-tier compute-minute budget is also a live constraint:
toolchains install per pipeline with no pinning, and stray branch
pushes trigger pipelines nobody asked for.

## Decision

1. CI scaffolding is defined **once** in this repo and consumed by
   every repo via `include: project:`:
   - `.gitlab/templates/agents-guard.yml` — the context-rot guard job
     (inline script, `KRI_LINK_REQUIRED` toggle, `lint` stage,
     non-blocking, MR + `main` rules).
   - `.gitlab/templates/security-minimal.yml` — SAST + secret
     detection re-staged into a `security` stage. Dependency scanning
     remains opt-in per repo.
2. Per-repo copies of the guard job and script are deleted as repos
   adopt the templates. The template is the single source of truth.
3. Reproducibility posture: toolchains are pinned (Rust CI image and
   `rust-toolchain.toml` channel pinned to the same stable release);
   caches are keyed against the pinned versions.
4. Compute-minute defense: every repo adds `workflow: rules` so
   pipelines run only for merge requests, `main`, and tags.

## Consequences

- A template change on kri `main` reaches every repo at its next
  pipeline creation — the blast radius of kri `main` grows. Keep the
  templates minimal and additive; breaking template changes require
  coordinated MRs across repos.
- Templates carry jobs only. A `stages:` block in an included
  file does **not** union-merge into the consuming repo's stage list —
  each consuming repo must list `lint` and `security` in its own
  `stages:` (learned 2026-10-13: template-declared stages break
  pipeline creation with "chosen stage does not exist").
- The escaping fix restores the KRI-link check across all repos.
- Pinning the Rust toolchain makes upgrades a deliberate two-line
  change (image tag + `rust-toolchain.toml` channel) instead of a
  surprise from `rust:latest`.
