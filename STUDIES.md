# STUDIES — the Study tier ledger

> Canonical index of KRI Studies. Tier definition: ADR-0005
> (docs/decisions/0005-study-tier.md). A Study is a focused work of craft,
> smaller than a Project, whose deliverable includes written principles.
> One repo per Study, full craft standards.

## Numbering

- Studies are numbered `NNNa`, `NNNb`, … — one number per Study,
  letters advancing in the alphabet.
- Subset Studies nest inside their parent number: Study 001a →
  subset Study 001ab (its own letters continue from there). The parent
  passes doctrine to the child.

## Index

| Study | Title | Soul | Status | Repo |
|---|---|---|---|---|
| 001a | First Light | kitsuneOS + blade KMOD | Active — soul-mapped, doctrine set | [Study-First-Light](https://gitlab.com/kitsune-kits/Study-First-Light) *(repo creation pending)* |
| 001ab | *(reserved)* First Light subset — Yoda's lightsaber | — | Not started | — |

## Study 001a: First Light — founding doctrine

A buildable, in-universe modular lightsaber hilt (the First Blade: an ancient
chassis the builder completes), running kitsuneOS to save development time.
The kit **is** the product: assembly ritual mirrors the myth.

- **Kyber crystal doctrine:** NFC tag (e.g. ST25DV64KC) in a hand-poured
  resin crystal. Factory UID = guaranteed uniqueness. Soul-data (color, sound
  font, hum character, name) lives on the crystal; UID salts a per-crystal
  voice hash so no two crystals sound identical. Hilt reads crystal at
  ignition; without a crystal the hilt is inert.
- **Crystal chamber:** a keyed seat inside the chassis, contact at the socket
  base, NFC antenna in the chamber wall — seating the crystal is an assembly
  step and the moment the Vessel receives its soul.
- **Diatium cell:** removable 18650 in a knurled canister, loaded through the
  pommel — in-universe power maintenance, real-world battery swapping.
- **Chassis:** threaded modular segments, no glue, Obsidian Protocol
  throughout; component names mirror in-universe lightsaber parts.
