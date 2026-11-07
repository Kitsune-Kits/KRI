# ADR-0007: P4 Face-Wing Display Doctrine

- **Status:** Proposed
- **Date:** 2026-10-26
- **Persona:** 🦊 Coco (lead)
- **Scope:** org-wide

## Context

KRI props increasingly need displays — a face, a bench instrument, an
at-con authoring surface. Until now the display tier was decided
per-prop, with three recurring options:

- **Soul MCU drives the display** (HSTX DVI, SPI TFTs): proven, but an
  RTOS-class UI co-resident with sandboxed prop code and prop monitoring
  hits the documented compute ceiling of the RP2350 Soul. Project-Kogane
  ADR-0001 named this ceiling when rejecting single-chip candidates;
  Kogane's face debate (2026-10-26) hit it in practice.
- **SBC owns the display (Linux):** provisionally inked for Kogane
  (Project-Kogane MR !53), then superseded in open debate — ~1–2 W
  always-on, boot posture, and two-OS maintenance lost to a shape that
  puts the UI on display-native silicon without Linux.
- **No display:** at-con authoring and monitoring then require a laptop,
  which violates the Architect's standing requirement: prop code must be
  changeable at the con with no computer.

The resolution in Project-Kogane (ADR-0002, 2026-10-26) was the
**four-brain face wing**: an ESP32-P4 drives the display via MIPI-DSI
with capacitive touch, while the kami stays on the RP2350 Soul. The
Architect then ruled the pattern general: *any KRI prop requiring a
display uses a P4 face wing.* This ADR inks that ruling as org doctrine.

## Decision

**Any KRI prop that requires a display uses an ESP32-P4 face wing**,
built on the principles proven out in Project-Kogane ADR-0002:

1. **Presentation, not soul.** The kami and prop code stay on the RP2350
   Soul. The kami never sits on Espressif silicon, and Linux never
   boards the Vessel.
2. **The Vessel degrades, never dies.** P4 down → face dark, prop alive.
   Soul down → spine (TASOGANE) runs its resident KMOD.
3. **Connectivity: MIPI-DSI panel with capacitive touch**, UI in LVGL,
   touch latency under 50 ms (Nui's law).
4. **P4 organ firmware is Rust-on-ESP-IDF** — Rust application code on
   the proven ESP-IDF display stack (esp_lvgl_port, esp_lcd panel +
   GT911-class touch drivers). Arduino-P4 is beta and is not the path.
5. **The face wing is also the bench instrument and prop-code courier** —
   telemetry/monitoring on the bench, and the at-con authoring surface
   (presets, tweaker, cue composer, script editor) pushing Tier 2 source
   to the Soul for on-chip Rhai interpretation.
6. **Flashing stays on the resident UART updater** (Tier 3); BOOTSEL is
   the bench fallback. Rust USB-host on the P4 is too young to lean on.
7. **A display need alone never justifies an SBC.** kitsunebiOS stays
   retired from Vessels; it remains a bench template only.

**Scope boundary:** the doctrine covers *interactive on-Vessel screens*.
Dumb video-out to an external sink (HSTX DVI via kitsuneOS T1.6 /
kri-iris) remains a platform capability and is not a display wing; nor
are fixed indicators (single LEDs, bargraphs), which never need a wing.

**First application:** Project-Kogane ADR-0002 (activation gated on
G1–G3, sled CAD gate G4 follows). Project-Saffron-Blossom (M1,
electronics) and Project-Lazy-Comet adopt this doctrine for their
display needs.

## Consequences

- **Easier:** one proven display stack to reuse across props; G1
  bring-up becomes a template; full-face draw is ~0.6–0.8 W class
  (≈3× under an SBC); at-con authoring needs no laptop.
- **Harder:** BOM grows a P4 module + panel; each display loom adds
  P4↔Soul UART, power, and RUN lines; benches carry the ESP-IDF
  toolchain alongside cargo; panel driver-IC support must be confirmed
  at cart time (esp_lcd driver present, silicon rev 3.0).
- **Blast radius:** org-wide. Project-Kogane (live, gated);
  Project-Saffron-Blossom (M1 — can adopt cleanly before the 2027-10-31
  electronics deadline); Project-Lazy-Comet (debuted; retrofit optional
  and opportunistic). kitsuneOS and kitsunebios are unaffected — no
  displays. This ADR references Project-Kogane ADR-0002 and does not
  modify it; the two stand together.
