# ADR-0015: Records declaration: naming the Tail Ledger's record classes

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** 🦊 Coco (lead)
- **Scope:** org-wide

## Context

The forge has run a records system for weeks without naming it one:
the Tail Ledger and Forge Diary are append-only, supersede-don't-edit,
with metadata and retrieval by index. ISO 15489-1:2016 is the
international concepts standard for exactly this: the creation,
capture, and management of records in any format. What is missing is
the declaration: which artifacts are official records, what each is
for, and how long each is kept. ISO 30401 (knowledge management) is
noted and deliberately deferred: it is mid-revision, so its vocabulary
enters later at principles level.

## Decision

1. The forge declares its **official record classes**, as follows
   (each with a stated retention):
   - **Ratified ADRs** (all repos): life of the organization, immutable.
   - **Forge Diary ratified entries**: permanent; a changed conclusion
     becomes a later superseding entry; the machine zone laws stand
     untouched.
   - **PROJECT-STATUS.md snapshots at merge points**: retained by git
     history; the tag itself is the snapshot mechanism.
   - **Named release baselines** (per the configuration management
     grammar, when adopted): permanent, as tags.
   - **Print-job acceptance records** (ADR-0009): life of the part
     plus debut + one year.
   - **Risk docket closures** (ADR-0014): permanent.
2. Anything not in a declared class is a working note: useful, but
  it makes no claim to authority.
3. Retention rules are stated per class; none of them authorize
  editing history.

## Consequences

- What counts as the record becomes explicit; retrieval and audit
  become reader-proof rather than narrator-dependent.
- Cost: the declaration is a page; discipline is a habit we mostly
  have.
- Blast radius: the hub plus every repo's decisions folder; diary and
  Ledger laws unchanged in every particular.
