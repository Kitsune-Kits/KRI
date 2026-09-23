# ADR-0005: The Study tier

- **Status:** Accepted
- **Date:** 2026-09-23
- **Persona:** 🦊 Coco (lead), with 🔨 Zaku, ⚡ Piko, ✨ Nui
- **Scope:** org-wide

## Context

KRI needed a tier between "one-off tinkering" and a full Project/Initiative.
Some works are too small to displace an Initiative yet still deserve full
craft — and their true product is not the object but the **principles the
object teaches**. The first such work (a buildable, in-universe lightsaber
running kitsuneOS) forced us to name the tier before building.

Alternatives considered: Mini Project (rejected — implies shrunken ceremony,
no doctrine), Tempering / Fieldwork (rejected as tier names; kept as
candidates earlier), no tier (rejected — unbounded scope creep).

## Decision

We adopt the **Study** tier: a focused work of craft, smaller than a Project,
whose deliverable includes written principles the org keeps after the object
is done. One repo per Study. Full craft standards (Apple-style comments,
persona attribution, agents-guard, ADR convention) apply — ceremony does not
shrink, only scope.

**Numbering:** Studies are numbered `NNNa`, `NNNb`, … per Study. When a
Study spawns a **subset Study** (a close variant, e.g. a second saber sharing
the first's chassis doctrine), it nests inside the parent number:
Study 001a → subset Study 001ab → 001ab**c** continues the alphabet within it.
The parent passes doctrine to the child.

**Study 001a: First Light** — a buildable, in-universe modular lightsaber
hilt (the First Blade: ancient chassis completed by its builder), Soul =
kitsuneOS + a blade KMOD, hardware-swappable per the Obsidian Protocol.
Founding doctrine:

- **Kyber crystal = NFC soul-tag.** Factory UID guarantees each crystal is
  unique; soul-data (blade color, sound font, hum character, name) lives on
  the crystal, never the hilt. Hilt without a crystal is an inert heirloom.
- **Crystal chamber is an assembly step** — keyed seat, contact at the socket
  base; seating the crystal seats the soul.
- **Energy core = removable "diatium cell" canister** (18650, pommel-loaded),
  per the lore's own removable power cells.
- Component naming follows the in-universe parts (emitter, energizers,
  insulator, pommel cap) so assembly instructions read like the myth.

## Consequences

- Studies get their own repos; the KRI hub keeps the canonical Study index
  ([STUDIES.md](../../STUDIES.md)) so tier rules live in one place.
- A Study may graduate to a Project; it does not inherit Initiative
  displacement rights while a Study.
- Blast radius: org-wide naming/filing only; no build changes to existing
  repos. kitsuneOS gains a blade KMOD later, developed under Study 001a.
