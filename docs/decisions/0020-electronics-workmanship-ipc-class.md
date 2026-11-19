# ADR-0020: Electronics workmanship: the IPC class declaration for KRI boards

- **Status:** Accepted
- **Date:** 2026-11-19
- **Persona:** ⚡ Piko (lead)
- **Scope:** org-wide

## Context

The Lantern Vigil custom board is ruled (RP2350A Soul plus ESP32-C6
edge, all chips soldered down), the bench hand-solders every sled, and
the crimp-first connector doctrine is already law. ISO covers
management and EMC; for design and workmanship the electronics
industry's own house governs, and the industry's house is IPC:
IPC-2221 (generic PCB design), J-STD-001 (soldered assembly
requirements), IPC-A-610 (assembly acceptability, Classes 1/2/3),
IPC-A-600 (bare-board acceptability) with IPC-9252 (bare-board
electrical test), IPC-7351 (land patterns and footprint naming),
IPC/WHMA-A-620 (cable and wire harness assemblies, including crimped
interconnections), and IPC-7711/7721 (rework, modification, repair).
The research brief's electronics round grounded each member.

Round 4 of the brief added the radio law: in the United States,
intentional radiators are governed by FCC Part 15, and the practical
host path is modular approval under 47 CFR 15.212, where a
pre-certified module carries its own grant and the host product
references it.

## Decision

1. **Class declaration:** every KRI built board declares
   **IPC-A-610 Class 2** (dedicated-service electronics) as its
   acceptance class, cited with revision, e.g. "IPC-A-610J Class 2".
   Class 3 is a deliberate per-project upgrade, never a default.
2. **Design principles:** custom boards follow IPC-2221 at principles
   level; footprint libraries follow IPC-7351 naming where the EDA
   permits.
3. **Bare boards:** first articles from a fab are accepted against
   IPC-A-600 character and IPC-9252 electrical-test language; follow-on
   boards are spot-checked, not re-articles.
4. **Assembly and harnessing:** bench hand-soldering is accepted
   against J-STD-001 / IPC-A-610 Class 2 criteria; harnessing follows
   IPC/WHMA-A-620, where the crimp-first doctrine already lives.
5. **Rework:** rework and repair on a functional assembly are performed
   with IPC-7711/7721 methods in mind, and every rework is recorded in
   the bench log.
6. IPC texts are paywalled like ISO texts: structure adapts now,
   requirements are quoted only after purchase, per ADR-0008 point 5.
7. **Radio modules:** any intentional radiator in a KRI build ships
   only as a pre-certified module carrying its own grant (47 CFR
   15.212 modular approval). The module's FCC ID is recorded in its
   BOM row alongside the ADR-0013 battery evidence, and the host
   follows the module grant's integration conditions (antenna,
   separation, shielding). Full host certification is re-opened as
   a separate decision before any commercial sale.

## Consequences

- The first Vessel board (Lantern Vigil) carries an industry-legible
  workmanship class; vendor and fab conversations shorten to a few
  words.
- Cost: class discipline on hand-soldering acceptance, and a purchase
  list that now includes IPC documents alongside ISO ones.
- Blast radius: Lantern Vigil first, then every Vessel board, sled,
  and harness; feeds the risk docket's electrical-hazard section.
