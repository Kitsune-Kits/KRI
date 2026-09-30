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

## Forge setup (v0.4.0)

`setup.sh` is the one-command forge bootstrap beyond branding:

1. **Extension rack** — installs every extension in `extensions.txt`
   (clangd, CMake, Lua, GitLab workflow, GitLens, Git Graph, Todo Tree,
   Error Lens, Markdown/Mermaid/PDF, Prettier, spell checker, EditorConfig).
   Open VSX gaps are skipped with a warning, never fatal.
2. **Forge settings merge** — clangd args (background index, clang-tidy),
   Lua KMOD globals, Error Lens, KRI file associations (`.kmod`/`.kmacro`
   → Lua, `.kspec` → YAML), build/target excludes, git discipline.
   Merged via `jq` with a `settings.json.backup-kri` backup.
3. **Keybindings** — `Alt+E` Error Lens toggle, `Alt+G` Git Graph,
   `Alt+O` clangd source↔header, `Alt+Shift+P` quick-open profile.
4. Hands off to `install.sh` for the brand color themes + icon theme.

```bash
./tools/vscodium-brand/setup.sh
```

Env overrides: `VSCODIUM_BIN`, `VSCODIUM_USER_SETTINGS`,
`VSCODIUM_USER_KEYBINDINGS`, `VSCODIUM_EXTENSIONS_DIR`.

### Mascot callbacks (v0.3.1 of the icon set)

Language icons now carry their official mascot, held to the brand
accents (one accent per icon — never crimson + jade together):

- **Rust** — Ferris the crab holding the page (crimson, the stamp)
- **Python** — snake coiled around the page edge (jade, the living)
- **C / C++** — badge ring / hexagon with `++` (crimson)
- **CMake** — gold triangle at the fold (`.cmake`, `CMakeLists.txt`)
- **Lua KMOD** — the crescent wearing fox ears (`.kmod`, `.kmacro`) —
  the one allowed KRI deviation; plain `.lua` keeps the bare crescent

Contact rule: every mascot touches its document.

## Snippets (v0.4.1)

`install.sh` now registers two org snippets in the local extension:

- **`kribanner`** — the Apple-style file banner (`FileName / Project /
  Abstract / Copyright`) for Rust, Lua, C, and Markdown
- **`krito`** — a TODO with a persona picker (`piko`/`zaku`/`nui`/`coco`)

The commenting standard becomes one keystroke instead of a copy-paste
ritual.

## Git identity per repo

Git deliberately ignores identity from repo-committed files, so it's a
per-clone setting. Helper in `tools/git-identity.sh`:

```bash
./tools/git-identity.sh architect   # your identity
./tools/git-identity.sh piko        # a persona (see PERSONA-ATTRIBUTION.md)
```

## Apple / MDM deployment

`apple/make-pkg.sh` builds a deployable macOS package: VSCodium.app +
this entire forge, with a postinstall that runs `setup.sh` as the
console user. Apple Business Manager cannot host custom pkgs itself —
it goes through your MDM (Jamf, Kandji, Mosyle...). Full flow, signing,
and scope notes: [`apple/README.md`](apple/README.md).
