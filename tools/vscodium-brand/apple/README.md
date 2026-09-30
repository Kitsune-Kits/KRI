# Apple deployment — ABM / MDM packaging

Goal: any KRI Mac gets VSCodium + the full forge (brand themes, mascot
icons, snippets, extension rack, settings) with zero manual steps.

## The honest constraint

**Apple Business Manager cannot distribute this package by itself.**
ABM only handles (a) App Store apps and (b) custom apps published by
developers through App Store Connect. VSCodium is neither. The
supported path for a custom .pkg on ABM-enrolled Macs is through your
**MDM** (Jamf, Kandji, Mosyle, Addigy...) — ABM enrolls the devices,
the MDM installs the package.

## Build the package

On any Mac (with Xcode command line tools installed):

```bash
./make-pkg.sh 1.96.2.24356        # universal build
```

This produces `KRI-VSCodium-<version>.pkg` containing:

- `/Applications/VSCodium.app` — official VSCodium release
- `/usr/local/kri/vscodium-brand/` — the whole forge (setup.sh,
  extensions.txt, snippets, icons, themes)
- a `postinstall` that runs `setup.sh` **as the console user** —
  never root, because VSCodium user settings live in $HOME

## Sign it (required for silent MDM install)

Unsigned pkgs trigger user-visible Gatekeeper prompts. With a Developer
ID Installer certificate:

```bash
productbuild --package KRI-VSCodium-*.pkg \
  --sign "Developer ID Installer: YOUR COMPANY NAME" \
  KRI-VSCodium-signed.pkg
```

(No Apple Developer Program membership yet? That's the one KRI-side
purchase this path needs. Unsigned pkgs also deploy fine via MDM if
the MDM is configured to allow them — Mosyle and Addigy both can.)

## Deploy

1. Upload the signed pkg to the MDM as a custom package.
2. Scope it to the KRI device group (ABM-assigned devices).
3. Set it to install on enrollment + auto-update on new versions.

Re-running an upgraded package is safe: `setup.sh` is idempotent and
backs up `settings.json` before every merge (`*.backup-kri`).

## What the fleet gets

- Kitsune Modern (Foxfire) theme + mascot icon set, applied
- Extension rack pre-installed (clangd, rust-analyzer, Lua, GitLab...)
- clangd/Lua/Error Lens settings + KRI file associations
- Keybindings (Alt+E/G/O)
- `kribanner` / `krito` snippets
