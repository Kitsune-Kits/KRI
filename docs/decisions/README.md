# Decisions — Architecture Decision Records

Architecturally significant decisions for Kitsune Kits are recorded here as
ADRs: numbered, immutable, one decision per file.

## Why

Decisions recorded in prose inside status files erode across edits. An ADR
records the **context** and **consequences** at the moment of the decision,
so future sessions (human or agent) can understand *why*, not just *what*.

## Rules

1. **One decision per file**, named `NNNN-short-title.md` (NNNN = zero-padded
   sequence, starting 0001).
2. **ADRs are immutable.** To change a decision, write a new ADR that
   supersedes the old one and update the old one's Status line to
   `Superseded by ADR-NNNN` — nothing else.
3. **Propose via MR.** Decisions land through review, never direct edits to
   `main`.
4. **Link from the repo.** A repo affected by a decision should reference it
   from its `AGENTS.md` or `PROJECT-STATUS.md`.

## Where

- Org-wide decisions live in this repo: `docs/decisions/`
- Repo-specific decisions live in that repo: `docs/decisions/`

Use [TEMPLATE.md](TEMPLATE.md) to start a new ADR.