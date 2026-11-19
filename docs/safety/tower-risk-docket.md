# Standing Tower Risk Docket

- **Status:** Living standing docket; first installment (laser hazards) filed 2026-11-19
- **Method:** ADR-0014 (ISO 12100: identify hazards, estimate and evaluate risk, reduce in the order inherently safe design, safeguards, information; document residuals honestly)
- **Scope:** the tower fleet and its integrations (Tatara, Silo, Engine, Surgeon, Photon, the BaBo line, the mobile Armory, the AMS 2 Pro pair)
- **Record class:** ADR-0015; docket closures are permanent; this standing document is open and accumulates. Risk decisions that wait on judgment are recorded "pending the Architect's word".

## L. Laser hazards (first installment, per the Architect's word, 2026-11-19)

### L.1 Hazard identification

- The 40 W cutting-class module (mono 90 drawer): per IEC 60825-1 its output exceeds any Class 3B accessible-emission limit; the module is treated as **Class 4** until its datasheet is read and rules otherwise (consult live source; do not estimate).
- The 10 W engraving-class module (mono 60 drawer): likewise treated as Class 4 pending a datasheet read.
- Hazard modes: direct beam exposure, specular and diffuse reflections, fire ignition of nearby materials, cutting/engraving byproducts (fume exposure), enclosure failure exposing the beam path, module supply electrical hazards.

### L.2 Risk reduction, in the ISO 12100 order

1. **Inherently safe design:** beam paths fully enclosed or interlocked wherever geometry permits; Photon's rebuilt cutting bay is the first named enclosure.
2. **Safeguards:** interlocks on enclosure openings, following the IEC 60825-1 interlock discipline: any override gives a distinct visible or audible warning whenever the laser is energized; class labels at each bay door.
3. **Information:** eyewear rated for the module wavelength (OD to be read from the datasheet, consult live source) worn whenever an enclosure is open and the module can energize; operating checklists name the module and its treated class each session; no unattended energized modules.

### L.3 Residual risk, recorded honestly

- Beam alignment and focal work happen with enclosures open and modules in restricted states. This residual is accepted for bench work under ADR-0014's craft-sense clause and controlled by the checklist discipline above; it is never zero and never unwritten.

### L.4 Open items (scheduled, not erased)

1. Per-module class declarations transcribed from datasheets (bench sitting; live source only).
2. Eyewear rating recorded per module wavelength into the Silo drawer trail.
3. Remaining hazard sections of this docket: electrical, thermal and mechanical, solvent and resin handling (pending bench sittings, per ADR-0014).
