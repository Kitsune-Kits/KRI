# SETUP-UI-CHECKLIST — GitLab UI configuration

The GitLab connector cannot create labels, milestones, boards, approval
rules, or wikis. This is the manual setup guide — one pass per repo.
Check off as you go. (Companion to the per-repo setup issues.)

## Labels & milestones per repo

Create under **Manage → Labels** and **Plan → Milestones**. Priority labels
(`P0`–`P2`) and type labels (`feat`, `fix`, `docs`, `chore`, `hardware`) are
shared across all repos; component labels are repo-specific.

### Project-Saffron-Blossom
- Component: `revolver`, `yellow-hat`, `spurs`, `belt`, `butterfly-wings`,
  `garments`, `makeup`, `electronics`, `firmware`
- Milestones M1–M8: Electronics design · Firmware development · CAD design ·
  Physical fabrication · Garments · Assembly and integration · Quality
  review · Butterfly wings (optional)
- Assign milestones + labels to issues #5–#12; set up an issue board
  (Plan → Issue boards)

### kitsuneOS
- Component (modules): `janus`, `charon`, `hermes`, `zeus`, `kronos`,
  `uranos`, `hercules`, `hephaestus`
- Milestones (suggested — adjust freely): module API hardening · Tasogane
  integration · v1.0 first Vessel deployment

### Project-Lazy-Comet
- Component: `crown-of-horus`, `eye-of-horus`, `iron-horus`, `yume-relic`,
  `audio`, `events`, `hardware`, `software`

### Project-Kogane
- Component: `pico-firmware`, `companion`, `cad`, `3d-printing`, `bom`,
  `kogane-lua`
- Milestones (suggested): hardware bring-up · LED strips (123 × WS2812B) ·
  display + audio · 60 GHz docking · assembly

### kitsunebios
- Component: `buildroot`, `cli`, `display`, `protocol`, `flasher`
- Milestones (suggested, from the v0.4 plan): v0.4 boot-to-CLI · v0.5 epoll
  event loop · v0.6 LVGL display (DRM/KMS) · v0.7 GT911 touch · v1.0
  Tasogane Mode + prop flasher

### KRI (this repo)
- Type: `docs`, `standard`, `decision`, `chore`

## All repos

- [ ] Protected branches: `main` (maintainers only)
- [ ] MR approval rules: all threads resolved + pipelines must pass
- [ ] Issue board (at minimum on Saffron)

## Wikis

Each repo has pre-written wiki content in `.gitlab/wiki/`. The connector
cannot write wikis. To populate:

```bash
git clone git@gitlab.com:kitsune-kits/<repo>.wiki.git
cd <repo>.wiki
cp -r ../<repo>/.gitlab/wiki/*.md .
git add . && git commit -m "Populate wiki from templates" && git push
```

Or create pages manually in the GitLab web UI.

## Archive legacy GitHub repos

All repos migrated to GitLab in September 2026. Archive the old
`github.com/KitsuneKits/` repos (Settings → General → Advanced → Archive)
so GitLab is the single source of truth. Do not delete — archive.