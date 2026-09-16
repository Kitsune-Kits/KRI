# Development Workflow — KRI Org Hub

This document describes the development lifecycle for this repo — the
Kitsune Kits org context hub — through Vibe Work using the GitLab MCP
connector. This repo contains standards and documentation only: changes here
affect every repo in the group, so they deserve extra care.

## Overview

```
Plan → Branch → Edit → Commit → Review → Merge → CI
```

## 1. Plan: Issues

Ask Vibe to create an issue on this repo describing the standards change.
Use the issue templates (Bug report for something broken, Feature request
for a new standard or document).

## 2. Branch

Create a branch from `main` with the persona prefix of the lead persona
(see [PERSONA-ATTRIBUTION.md](PERSONA-ATTRIBUTION.md)):

```
<persona>/<short-description>
```

Examples: `coco/org-principles`, `piko/agents-guard-job`.

## 3. Edit: Read & Write Files

Through the connector, Vibe can read any file, list the tree, search
contents, and commit create/update/delete actions — multiple file changes
in a single commit.

**Special care in this repo:**

- `AGENTS.md` is the org-wide agent standard — changes to it propagate
  conceptually to every repo. Propose via MR, never rewrite unilaterally.
- Accepted ADRs in `docs/decisions/` are immutable — supersede them with a
  new ADR rather than editing history.

## 4. Commit

Conventional Commits (`docs:`, `feat:`, `fix:`, `chore:`) plus KRI persona
attribution (attribution line, `KRI-Persona:` and `Co-authored-by:`
trailers). Full convention: [PERSONA-ATTRIBUTION.md](PERSONA-ATTRIBUTION.md).

## 5. Review: Merge Requests

Every change to this repo goes through an MR — even small ones. Vibe can
create the MR, read the diff, comment, approve, and merge. Use the default
MR template.

## 6. CI

This repo's pipeline (all non-blocking):

| Job | What it does |
|---|---|
| `agents-guard` | Verifies AGENTS.md / CLAUDE.md / PROJECT-STATUS.md exist and are fresh |
| `repo-link-check` | Verifies all sibling repo URLs resolve |

## After merging

If a change here alters what repos should do (e.g., a new standard), follow
up on the affected repos — one repo at a time, checkpointed — and update
their repo-specific `AGENTS.md` files to match.