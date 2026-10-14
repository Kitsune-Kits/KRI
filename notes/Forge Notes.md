# Forge Notes

> The one-glance digest of everything Kitsune Research Industries has in flight.
> **Verified against** each repo's PROJECT-STATUS.md at HEAD on **2026-10-14**.
> When this note and a repo disagree, the repo wins — then this note gets fixed.

---

## 🦊 The One-Glance Map

KRI builds **Vessels** — physical shells for digital souls. Every Vessel follows the **three-repo split**:

| Layer | Repo | What it is |
|---|---|---|
| **Shell** | kitsunebios | Linux userspace host (retired from the Vessel — bench template only) |
| **Soul** | kitsuneOS | The prop OS — Rust, runs on every Vessel's RP2350 |
| **Vessel** | Project-Kogane | The Tasogane gunblade: prop scripts, CAD, BOM, docs |

Plus two cosplay Vessels (Saffron Blossom, Lazy Comet), one Study (First Light), and the **kri** org hub.

| Repo | Role | Phase (2026-10) |
|---|---|---|
| [[kri/PROJECT-STATUS|kri]] | Org context hub | Shared CI templates live (ADR-0006) |
| [[kitsuneOS/PROJECT-STATUS|kitsuneOS]] | Soul | **Rust-primary** — workspace compiles, rust-check blocking |
| [[Project-Kogane/PROJECT-STATUS|Project-Kogane]] | Vessel | CAD **frozen Oct 12**; countdown to AWA debut |
| [[Project-Saffron-Blossom/PROJECT-STATUS|Project-Saffron-Blossom]] | Cosplay Vessel | M1 — electronics design |
| [[Project-Lazy-Comet/PROJECT-STATUS|Project-Lazy-Comet]] | Cosplay Vessel | **Debuted May 2026** — the only completed Vessel |
| [[kitsunebios/PROJECT-STATUS|kitsunebios]] | Shell | v0.4 boot-to-CLI; deprecation gate open |
| [[Study-First-Light/PROJECT-STATUS|Study-First-Light]] | Study 001a | Foundation+; S3 CAD in progress |

All repos live under the kitsune-kits GitLab group (migrated from GitHub, Sept 2026). All on main, all pipelines ✅ passing.

---

## ⏳ Key Dates (live countdown)

| Date | Event |
|---|---|
| **Oct 12, 2026** | ✅ CAD freeze (Kogane) — passed; geometry changes now need a superseding plan |
| **Oct 13, 2026** | Parts-delivery verification gate (Oct 5/7 carts) |
| **Nov 1, 2026** | ST60 cutoff — if the 60 GHz pair is not in hand, docking is **demo-only** at AWA |
| **Nov 6, 2026** | Full integration test (Tasogane) |
| **Nov 19–22, 2026** | **AWA 2026 — Kogane debut** (build *and* business debut, DEBUT-PLAN.md) |
| **Oct 31, 2027** | Saffron Blossom deadline (Yellow, Deltarune Ch.5) |

---

## 🧠 kitsuneOS — The Soul

**What it is:** Prop OS for the RP2350, being **fully rewritten from C to Rust** (ADR-0001). Rust is now canonical (ADR-0004, 2026-09-23); the C tree is frozen on main as the R2 golden-harness reference — not deleted, not built.

**Hardware target (interim):** Adafruit **Feather RP2350 HSTX** — bench and Vessel silicon are now identical. Console/status-bar canon is USB CDC until the DVI face lands.

### The Pantheon (named systems)

| System | Responsibility | Rust status |
|---|---|---|
| JANUS | A/B dual-bank bootloader with rollback | Stub (C reference exists) |
| THESEUS | Maintained independently | Stub |
| CHARON | Security (AES-256-GCM, ECDSA) | Trait faces done; RustCrypto in R4 |
| HERMES | Messaging/event bus | Traits + topics done; embassy impl pending |
| ZEUS | Power + thermal core (PYTHIA prediction, NYX sleep) | Zones + predict + sleep states |
| KRONOS | Time discipline (DS3231 RTC) | Codec ported |
| URANOS | KMOD loader (CRC32 verify, ATHENA gate) | Ported |
| HERCULES | HAL (GPIO, PWM, LED, Audio, MIDI) | Trait faces only |
| HEPHAESTUS | KMOD compiler — Rhai target | Stub |
| HESTIA | Persistent storage / flash regions | Stub |
| HERA | Config/manifest validation | Stub |
| IRIS | Display pipeline (three lanes: host link / radio / mesh — ADR-0007) | Stub |
| METIS | Kitsune Kommand app protocol | Stub |
| POSEIDON | Water/short management | Classify + ladder done |
| ATHENA | Electronics component registry | Registry done |
| ARGUS | Watchdog / anomaly detection | Heartbeats + budgets done |
| HADES | Process-killing core | Warden done |
| MNEMOSYNE | Event history / black box | Ring done |
| KPE | Prop manifest format | Stub |
| THALIA | Rhai performing layer, with LACHESIS stage manager inside (ADR-0006) | New crate |

**ARKE** (ADR-0007) is the ESP companion edge — ESP-NOW + BLE, companion/arke/. *Family, not pantheon — never the kami.*

### Scripting doctrine

- **Rhai replaces Lua 5.5.1** (ADR-0002 → superseded by ADR-0003): ZEUS owns power/thermal, the Rhai interpreter lives in HERCULES→THALIA, HEPHAESTUS retargets to Rhai.
- **Stage-Play model** (ADR-0005): plays declare cast/timeline/improv; the stage manager fires cues with canonical fallback. The bench UP button injects improv.
- **R5 hard gate (locked):** Rhai performance spike ≥ **1000 iters/s on-target**. kogane.lua keeps loading over UART until then.

### Milestones

R0 ✅ toolchain CI · R1 ✅ workspace (MR !28) · **R2 planned** (golden parity harness — capture-not-port, issue #5) · R3 in progress (organs landing) · R4–R18 queued.

### What's left to first Rust release (honest list)

1. Embassy executor + Feather BSP; PIO bus slice for IRIS
2. HERMES embassy-backed implementation
3. Rhai integration + perf spike (R5 gate)
4. CHARON primitives (RustCrypto), JANUS/THESEUS port, HESTIA flash regions
5. KPE manifest format + HEPHAESTUS Rhai target
6. Golden tests vs the frozen C reference

### CI (compute-minute defense)

- **Blocking:** rust-check (build+clippy+fmt), commit-lint, docs, pages.
- **Manual by default:** build-firmware, test-coverage, code-quality, docker-build — don't flip back without reason.
- Toolchain pinned to **Rust 1.99.0**; pipelines run only for MRs, main, and tags; scaffolding included from the kri hub.
- Docs site: https://kitsune-kits.gitlab.io/kitsuneOS

**Known battle scars:** the stale-cache incident (Oct 5, MR !84) — CARGO_HOME pointed at the committed .cargo dir, so a Sept 19 cache kept breaking every CI link while local builds stayed green. Fixed for good; the same footgun was preemptively patched in Kogane's CI.

---

## ⚔️ Project-Kogane — The Tasogane Vessel (黄昏)

**What it is:** A smart gunblade prop + mobile hardware testbench. The AWA 2026 headliner.

### Architecture (ADR-0001)

| Component | Device | Role |
|---|---|---|
| **MARI** (Soul sled) | Feather RP2350 HSTX (PSRAM) | kitsuneOS Rust; Rhai/HERCULES, ZEUS thermal, sensors, radio via AirLift breakout #4201 |
| **TASOGANE** (prop spine) | Pimoroni Pico LiPo 2 (RP2350) | 123× WS2812 via PIO, 4 actuators, 10 Hall sensors, 4-point haptics, KMOD loader stub |
| **kogane.kmod** | Pushed MARI → TASOGANE | Prop events + tests over UART, CRC32 |

The Orange Pi Zero 3W host is **RETIRED from the Vessel** (ADR-0001) — kitsunebios remains a bench template. UART: MARI is protocol master, both 3.3 V, no level shifter.

### Blade doctrine (2026-10-07 rulings)

- The Kopis blade deploys **LINEARLY** — no 180° hinge flip. Channel + rail geometry; the collar is stationary.
- KG-081 = **L16-P feedback actuator + LAC-1 driver (I2C)** — live position readback feeds the blade LED cascade + stall detection. KG-080 sled stays L16-R.
- **Two-stage trigger** (green-lit): printed lever + staged Hall mounts (KG-078/079 + KG-039). Fire is semi-auto, one round per cycle; **magazine = 12 rounds** (remap is firmware-only).
- **Haptics:** four-point travel wave — 8 mm LRA cradles at blade mid + ~80% station, TPU-isolated, 2× DRV2625 (one per motor — auto-resonance tracking is per-motor).

### Procurement watch (Oct 7 pass)

| Item | Status / decision |
|---|---|
| **ST60 60 GHz pair** | ⚠️ **Highest risk.** Order via ST eStore; if not in hand by Nov 1, docking is demo-only at AWA (Hall docked-detect + mechanical seat carry the moment). Order regardless — completes post-AWA. |
| LiPos + add-on order | Reconcile at the Oct 13 gate — the Adafruit cart was reported unplaced on Oct 7 |
| DRV2625 ×3 | TI sample limits — order today; fallbacks: BOOSTXL EVM, then DRV2605L breakout |
| Actuonix L16-R + L16-P + LAC-1 | In stock direct — order today, 50 mm stroke, confirm 5 V/6 V |
| Qi2 receiver, N52 magnets, trigger parts, LRA pair | All fast-ship vendors; mux (TCA9548A) deferred to the bring-up address check |

Cart placement is the Architect's click — the connector cannot pay.

### Firmware path

kogane.lua loads over UART (LOAD_PROP) until HEPHAESTUS retargets to Rhai (R5). rhai/kogane.rhai is the drafted **contract** for the retarget — Stage-Play, three-lane doctrine. rhai/improv.rhai is reserved for cross-prop improv over ESP-NOW.

**CI:** prop-validate (blocking) + firmware-rust (manual) + kri shared security templates.

---

## 🌸 Project-Saffron-Blossom — Yellow (Deltarune Ch.5)

**What it is:** Yellow cosplay — crystalline 7-chamber revolver, cowboy aesthetic. Deadline **Oct 31, 2027**. v0.7.0, phase **M1 — electronics design**.

**Props:** revolver (in progress, M1/M2) · yellow hat, spurs, belt (M3 CAD) · butterfly wings (optional, M8).
**Garments:** suit with wing mounts, boots, wig, makeup — all M5.

**Milestones (M1→M8, issues #5–#12, all open):** electronics → firmware → CAD → fabrication → garments → assembly → quality review → wings. Dependency chain: M1→M2, M1→M3, M3→M4, M4→M6, M5→M6, M6→M7, M4→M8.

**CI:** config-validate + pages blocking ✅; docs-check, sast, countdown-badge fail non-blocking (intentional, free tier).

**Key docs:** ARCHITECTURE, DESIGN-SPEC, STYLE-GUIDE, FABRICATION-PLAN, BLADE-SLEDS, MESH-PROTOCOL, ROADMAP, PROP-LUA — all under docs/.

---

## 🌠 Project-Lazy-Comet — Hoshino (Blue Archive)

**What it is:** Takanashi Hoshino multi-node prop system — **debuted May 2026**, the org's only completed Vessel.

- **Architecture:** wireless mesh — **ESP-NOW + BLE**, kitsuneOS v9.6 / KPE v2.0.
- **Nodes:** Crown of Horus · Eye of Horus · Iron Horus · Yume Relic.
- **CI:** structure-validate (**blocking**, ported from retired GHA), lua-lint (recipe fixed Oct 13 — it had failed silently for weeks), agents-guard + security via kri templates. All green.

---

## 🐚 kitsunebios — The Shell (bench template)

**What it is:** Linux userspace CLI for the Orange Pi Zero 3W (Allwinner A733). **Retired from the Vessel**; kept as a bench-template repo. v0.4 — boot-to-CLI in progress (Buildroot image built; first hardware boot pending).

**Deprecation gate (Architect, 2026-10-14):** regarded as a relic of the C era — deprecate once it's verified a UI can run under Rust kitsuneOS **purely through Rhai** (THALIA/IRIS territory). Verification gate only, not yet an R-milestone.

**Seven locked decisions (Sept 14):** AIOT SDK kernel (5.15) · BusyBox init · LVGL + DRM/KMS · Buildroot first, Yocto later · static musl · straight to A733 · GPLv2 kernel doesn't infect the proprietary userspace.

**Nothing vendored:** kernel, LVGL, musl, BusyBox, U-Boot all fetched at build time; only proprietary code lives in our repos.

---

## ⚡ Study-First-Light — Study 001a

**What it is:** A buildable in-universe **lightsaber** — the SWTOR First Blade hilt as canonical reference. Study tier per ADR-0005: a standalone custom Vessel, *not* a Kogane prototype. The product is the assembly ritual — the wielder completes the Vessel.

**Stack (locked):** Pimoroni Pico 2 (RP2350) Blade Sled · 18650 cell (10 A, protected) · MAX98357A I2S amp + 28 mm speaker · 2× DRV2605L (hilt + blade LRA) · ST25DV64KC NFC · dual TDK IIM-42352 IMUs (hilt SPI + tip I2C).

**Doctrine highlights (all locked):**

- **Quarter-turn law:** "maintained by its keeper, alone, in the dark, with no tools" — one clock, no full threads anywhere.
- **Crystal:** hand-poured resin with NFC tag + micro-LED pogo disc cast in — glows from within; pogo seat contact.
- **Clash exchange:** UWB (DW3110) bearing/ranging is primary — each blade pre-computes clash geometry and renders the *opponent's* color at the triangulated zone; TCS3471 optical is the fallback.
- **Charging:** 3-pin pogo trio in the pommel on the KRI stand (full rate, ~1.5–2 h); Apple Watch puck fallback (~5 W). USB-C is wired-jobs only, never charging.
- **Palette:** ice-silver #C2D9F0 body, warm aged bronze #8A6B45 ritual rings — two-tone doctrine: gunmetal is the chassis, bronze is the ceremony.
- **Dims:** hilt 280 mm × Ø36 mm; blade 36″ × 1″ OD × 2 mm wall; ~750 g total; balance 45–55 mm behind emitter.

**Milestones:** S1 ✅ foundation · S2 🔄 Blade KMOD crystal-handshake (outline merged; code after S4) · S3 🔄 chassis CAD (MR !3, coupon-first) · S4 🔒 stack locked · S5 crystal fabrication (Nui) · S6 print/finish/ritual write-up.

---

## 🏛️ kri — The Org Hub

- **Standards:** AGENTS.md (org agent protocol — grounding order: PROJECT-STATUS → README → AGENTS → DEV-WORKFLOW), ORG-CONTEXT.md (Cyber Shinto, glossary, three-repo split), PERSONA-ATTRIBUTION.md (canonical persona standard).
- **Shared CI templates** (ADR-0006, Oct 13): agents-guard.yml + security-minimal.yml in .gitlab/templates/ — all seven repos include them from the kri hub. Fixes the escaped-variable bug that silently disabled the KRI-link check everywhere.
- **Decisions:** ADR convention in docs/decisions/ — numbered, immutable, supersede-don't-edit. **STUDIES.md** indexes the Study tier.
- **Brand canon lives here:** BRAND.md + brand ADRs (palette, typography, aesthetics).
- **Vault layer (this folder):** notes/ — Obsidian as the pretty UI over the repos. Doctrine in [[kri/notes/VAULT|VAULT.md]].

### Brand quick canon (locked Sept 2026)

**Kitsune Modern** — *tradition is the structure, the future is the light.* Five colors: Foxfire White #F4F7F8 (primary) · Sumi Ink #0E1113 (body) · Gold-Leaf #C9A227 (formal) · Torii Crimson #D0342C (sacred — never with jade) · Imperial Jade #0FA898 (living). Neon green is forbidden in all palettes. Typography: KRI Sans / KRI Mincho (Shippori Mincho — earned, formal, gold-leaf pairing) / KRI Mono. Motifs: Gate, Seal, Kintsugi Line, Circuit-Kami, Foxfire Bloom, Ledger Grid.

---

## 🛠️ Cross-Org Rules of the Road

- **Persona attribution:** branch prefixes coco/, zaku/, piko/, nui/ + KRI-Persona: / Co-authored-by: trailers on every branch, commit, MR.
- **Connector caution:** GitLab connector has reported false commit failures — on any error, verify actual state before retrying.
- **One repo at a time** — never hold uncommitted changes in two repos. Breaking kitsuneOS main breaks three repos (Kogane pulls it at build time; Saffron and Lazy Comet run it).
- **Manual GitLab UI remaining:** create labels + milestones (Saffron M1–M8), issue board, protected branches, MR approval rules, the legacy/c-reference tag in kitsuneOS, GitHub archiving. Wiki population is now **scripted** (populate-wiki.sh) — not manual anymore.

## 📖 Glossary (quick)

| Term | Meaning |
|---|---|
| **Vessel** | The physical shell that houses a digital soul |
| **kami** | The spirit residing in a crafted thing — every circuit and layer has one |
| **Blade Sled** | Removable, modular MCU carrier — the Vessel's brain sits on it |
| **Obsidian Protocol** | The brain is never trapped by glue or permanent solder |
| **KMOD** | Prop module loaded over UART/flash — CRC32-verified |
| **Stage-Play** | Rhai prop model: cast / timeline / improv with canonical fallback |
| **Pantheon** | The named system architecture of kitsuneOS |
| **The Nursery** | Coco's folder of catastrophically failed prints — kept, loved, never recycled |
