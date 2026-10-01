# Apple deployment — ABM / MDM packaging

Goal: any KRI Mac gets VSCodium + the full forge (brand themes, mascot
icons, snippets, extension rack, settings) with zero manual steps.

## The honest constraint — and why ABE changes it

**Apple Business Manager alone cannot distribute a custom package** —
ABM only handles App Store apps and developer-published custom apps.
VSCodium is neither.

**But KRI runs Apple Business Essentials, which includes its own MDM.**
ABE *can* deploy custom packages directly — no Jamf, Kandji, or Mosyle
middleman. The flow is:

    Apple Business Essentials → Collections → deploy the .pkg to devices

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

## Deploy — Apple Business Essentials

ABE deploys custom packages through **Collections** (Settings → your
plan; or Devices → Collections):

1. In Apple Business Essentials (business.apple.com), open
   **Collections** and create one named *KRI Forge* (or add to an
   existing collection).
2. In the collection, under **Apps and books**, choose
   **Custom App / Add Package** and upload the signed
   `KRI-VSCodium-*.pkg`.
3. Assign the collection to the KRI users/devices — collections sync
   to every Mac in them automatically.
4. The package installs silently on assignment. Upgrades: build a new
   pkg with a bumped version and re-upload — `setup.sh` is idempotent
   and re-merges settings safely.

Notes:
- ABE installs as the device channel; our postinstall detects the
  console user and runs the forge setup in *their* $HOME at install
  time. If a Mac installs while logged out, the setup defers — it
  re-runs cleanly on the next package push, or the user can run
  `/usr/local/kri/vscodium-brand/setup.sh` once manually.
- ABE requires the pkg to be **signed** for silent install (see the
  signing section above).

Re-running an upgraded package is safe: `setup.sh` is idempotent and
backs up `settings.json` before every merge (`*.backup-kri`).

## What the fleet gets

- Kitsune Modern (Foxfire) theme + mascot icon set, applied
- Extension rack pre-installed (clangd, rust-analyzer, Lua, GitLab...)
- clangd/Lua/Error Lens settings + KRI file associations
- Keybindings (Alt+E/G/O)
- `kribanner` / `krito` snippets
