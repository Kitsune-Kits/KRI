# vscodium-brand — Kitsune Modern Theme Installer

One-command VSCodium branding for KRI. Applies the locked brand palette
(`BRAND.md` / ADR-0001) and typography canon (`BRAND-TYPOGRAPHY.md` / ADR-0002)
to VSCodium:

- **Kitsune Modern (Foxfire)** — canonical light theme (“black is the ink,
  not the paper”): Foxfire White `#F4F7F8` surfaces, Sumi Ink `#0E1113` text.
- **Kitsune Modern (Sumi)** — dark variant for deep-night sessions.
- Accent discipline: Gold-Leaf `#C9A227` = types/headings/focus,
  Torii Crimson `#D0342C` = keywords/errors (the stamp),
  Imperial Jade `#0FA898` = strings/functions/git-added (the living).
  Never crimson + jade in one component. No neon green, ever.

## Usage

```bash
git clone https://github.com/Kitsune-Kits/KRI.git
bash KRI/tools/vscodium-brand/setup.sh        # full forge (v0.4.0)
bash KRI/tools/vscodium-brand/install.sh      # brand themes + prefs only
```

## Installing (private repo — read this first)

The Kitsune-Kits organization on GitHub is **private**, so clone with
your GitHub credentials — the `gh` CLI, or a personal access token with
`repo` scope. The supported flow is clone-first:

```bash
git clone https://github.com/Kitsune-Kits/KRI.git
./KRI/tools/vscodium-brand/setup.sh
```

The clone path is preferred — you can read the script before trusting it.
Connector commits may not carry the executable bit, so invoke through
`bash` — the door, not the lock.
(The GitLab group stays a read-only mirror until the post-AWA review.)

## Behavior

- Installs a local extension to `~/.vscode-oss/extensions/kri-kitsune-modern/`
  (override with `VSCODIUM_EXTENSIONS_DIR`).
- Merges brand settings (JetBrains Mono 13px/1.6, Inter UI, brand ANSI
  terminal palette, Ma rulers) into user `settings.json` via `jq`,
  **backing up** the existing file to `settings.json.backup-kri` first.
  Without `jq`, themes still install; the merge is skipped with a note.
- Env override: `VSCODIUM_USER_SETTINGS` for portable/Flatpak installs.

After install: restart VSCodium, `⌘K ⌘T`, pick a Kitsune Modern theme.

## Color themes (v0.5.0)

The workbench color themes live in the repo itself, at the root `themes/`
folder — exactly where `install.sh` copies them from into the local
extension:

- `themes/kitsune-modern.json` — **Kitsune Modern (Foxfire)**, the canonical
  light paper: Foxfire White surfaces, Sumi Ink text, jade interactive
  surfaces, a Gold-Leaf Kintsugi hairline on the active tab, and an
  ink-black status margin.
- `themes/kitsune-modern-dark.json` — **Kitsune Modern (Sumi)**, the
  deep-night variant: the same architecture reversed — ink surfaces,
  Foxfire text.

Legibility shifts are permitted and recorded: jade is sunk (`#0B8A7E`) on
paper and full (`#0FA898`) on sumi; crimson is raised (`#E0554C`) on sumi
for thin squiggles. Accent discipline holds everywhere — never crimson
and jade in one component, and no neon green, ever.

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
bash tools/vscodium-brand/setup.sh
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
