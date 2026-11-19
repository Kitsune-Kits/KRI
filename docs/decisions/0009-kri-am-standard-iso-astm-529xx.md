# ADR-0009: KRI-AM standard: the ISO/ASTM 52900 line as base layer

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** 🔨 Zaku (lead)
- **Scope:** org-wide

## Context

The print floor is the forge's largest daily surface, and it runs on
house vocabulary: spaghetti, blobs, tower first-layer rituals, material
tiering. The rest of the additive world runs on ISO/ASTM 52900:2021
(fundamentals and vocabulary, Edition 2, confirmed 2025), written jointly
by ISO/TC 261 and ASTM F42. Its companion ISO/ASTM 52901:2017 defines
the information exchanged when AM parts are ordered: order information,
part definition data, feedstock requirements, final part
characteristics, inspection requirements, acceptance methods. We are
both customer and provider of our own prints, so we owe ourselves both
halves of that ledger.

ISO/ASTM 52902:2023 (test artifacts for geometric capability
assessment) exists for scoring what each tower can hold; ISO/ASTM 52915
(AMF) is noted and rejected for workflow: the slicer chain is 3MF/STL.

## Decision

1. ISO/ASTM 52900:2021 terminology is the **base layer** of a KRI-AM
   standard. House terms stay as colloquial nicknames; where a 52900
   term exists, it wins in records and acceptance sheets.
2. Every completed print job for a functional part carries a
   **print-job acceptance record** shaped on ISO/ASTM 52901: order
   intent, part definition (file and revision), feedstock (material,
   batch, Silo drawer trail), final characteristics, inspection
   performed, acceptance verdict. Bench-only drafts may skip the
   record; functional parts may not.
3. Tower capability scoring adopts the **52902-style artifact** idea:
   a defined test piece, measured per the measurement ADR (ADR-0012),
   producing per-tower, per-material capability numbers.
4. AMF is watch-only. The file chain remains 3MF and STL.
5. Existing sub-standards (all-PETG prototyping, the nylon tier,
   color doctrine) are re-expressed in this vocabulary, not rewritten.

## Consequences

- One language across all towers and repos; acceptance records become
  evidence, not memory.
- Cost: a new template and a little more paperwork per functional
  print. The Nursery's exemptions are unaffected and unexamined.
- Blast radius: every repo with printed parts; the template lands in
  the hub and is referenced per repo.
