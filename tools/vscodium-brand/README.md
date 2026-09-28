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

## Icon theme (v0.2.0)

The installer also ships **Kitsune Modern Icons** — a file/folder icon
theme on the same palette:

- Folders: Foxfire White with **Gold-Leaf** tab (gold at the joints);
  special folders by meaning — `docs`/`decisions` gold, `themes`/`crates`/`tests`
  jade (the living), `.gitlab`/`.git` crimson (the sacred seal), build-output
  folders dimmed sumi.
- Files: neutral Foxfire page with a gold corner fold; language accent stripe —
  **Crimson** for Rust/C and lockfiles (the stamp), **Jade** for Lua/Python/TS
  and media/CAD, **Gold-Leaf** for config (`json`/`toml`/`yaml`) and Markdown.
- No neon green. It does not exist in a polite universe.

Selected via `workbench.iconTheme: "kri-kitsune-modern"` (set by the installer).

### Language glyphs (v0.3.0)

Files now carry a **language glyph**, not just a color stripe — identity by
glyph, meaning by accent color:

- **Crimson** (the stamp): Rust gear, C braces, C++ braces-plus, lockfile seal
- **Jade** (the living): Lua crescent, Python mark, TS/JS blocks, CSS brush
- **Gold-Leaf** (the joints): shell prompt, JSON brace pair, TOML table band,
  YAML waves, Markdown mark, HTML brackets, Makefile hammer

All glyphs sit on the Foxfire page with the gold corner fold. 16×16 SVG,
readable at 13px sidebar size.
