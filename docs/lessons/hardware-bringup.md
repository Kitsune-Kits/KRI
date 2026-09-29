# Hardware Bring-Up Lessons — ST7789 / Tufty 2350 (Sept 2026)

> Org-wide lessons from the first kitsuneOS panel bring-up. The panel
> stayed dark for three bench sessions while the firmware wrote happily
> into RAM nobody could see. These rules exist so no persona spends
> three sessions on a one-command ghost again.

## The incident

kitsuneOS sandbox bench, first hardware boot (Sept 2026): backlight
lit, prop LED (the heartbeat) flashing, panel completely dark. Pin map
verified correct. Bus timing hardened (rail settle, WR pulse width).
Still dark. Root cause: the ST7789 init sequence ended at NORON
(0x13, "normal display mode") — the panel's output stage never turns on
without **DISPON (0x29)**. Pimoroni's own driver
(pimoroni-pico drivers/st7789/st7789.cpp, common_init) sends
INVON → SLPOUT → DISPON; our slice stopped one command short.
Fixed in kitsuneOS !51.

## Rules

0. **Docs first — always.** Before forming any hypothesis about a
   fault, read the documentation and the known-good baked-in code:
   vendor driver, upstream example, crate docs, board file. Most
   "mysteries" are simple misuse of code that already works. The
   three-session dark panel was one missing command in a sequence
   Pimoroni's driver already contained.
1. **Verify peripheral init against a known-good upstream driver,
   not just the datasheet.** Datasheets enumerate commands; a working
   driver shows the order and the minimum set. Read the vendor's
   driver before writing your own.
2. **Ship a bring-up tell.** First boot draws something unmistakable
   (full-screen color flash) before the application takes over. One
   observation splits "bus dead" from "app bug". A dark tell is
   bus-level; a visible tell means everything after is software.
3. **The host spike is not the device.** A fix that compiles and runs
   on the host can fail on-target (no_std prelude lacks trait imports
   the host has — e.g. ToString for to_string()). Compile for the
   real target before claiming a fix works.
4. **Bit-banged buses need explicit timing margins.** Settle power
   rails before reset; pad strobes on both edges.
5. **Verify pin transcriptions against the vendor's board file**
   (pins.csv / board header) before suspecting wiring.
6. **Triage three separate questions:** MCU alive (heartbeat LED)?
   Panel alive (tell)? Content correct (console)? Never conflate them.
7. **Embedded interpreter contracts fault silently.** Rhai's print
   overload must return the string; a unit return faults every printed
   line, and panic_halt freezes without a word. Sandboxes need their
   fault path visible on-device, not just in theory.

## Applies to

Any first-bring-up of a peripheral in any KRI repo: displays, sensors,
audio, radios. When a new bring-up lands, append its lessons here.
