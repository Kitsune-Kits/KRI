# vscodium-brand — Kitsune Modern Theme Installer

One-command VSCodium branding for KRI. Applies the locked brand palette
(`BRAND.md` / ADR-0001) and typography canon (`BRAND-TYPOGRAPHY.md` / ADR-0002)
to VSCodium:

- **Kitsune Modern (Foxfire)** — canonical light theme ("black is the ink,
  not the paper"): Foxfire White `#F4F7F8` surfaces, Sumi Ink `#0E1113` text.
- **Kitsune Modern (Sumi)** — dark variant for deep-night sessions.
- Accent discipline: Gold-Leaf `#C9A227` = types/headings/focus,
  Torii Crimson `#D0342C` = keywords/errors (the stamp),
  Imperial Jade `#0FA898` = strings/functions/git-added (the living).
  Never crimson + jade in one component. No neon green, ever.

## Usage

```bash
bash <(curl -fsSL https://gitlab.com/kitsune-kits/kri/-/raw/main/tools/vscodium-brand/install.sh)
```

Or from a checkout:

```bash
./tools/vscodium-brand/install.sh
```

## Behavior

- Installs a local extension to `~/.vscode-oss/extensions/kri-kitsune-modern/`
  (override with `VSCODIUM_EXTENSIONS_DIR`).
- Merges brand settings (JetBrains Mono 13px/1.6, Inter UI, brand ANSI
  terminal palette, Ma rulers) into user `settings.json` via `jq`,
  **backing up** the existing file to `settings.json.backup-kri` first.
  Without `jq`, themes still install; the merge is skipped with a note.
- Env override: `VSCODIUM_USER_SETTINGS` for portable/Flatpak installs.

After install: restart VSCodium, `⌘K ⌘T`, pick a Kitsune Modern theme.
