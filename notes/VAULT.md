# The KRI Vault — Doctrine & Setup

> Obsidian is the reading room. The repos are the archive.
> Everything in this folder is a pretty UI laid over the repos — the real work stays under the surface.

## The Three Laws of the Vault Layer

1. **The repos are the truth.** Every PROJECT-STATUS.md, ADR, design doc, and plan lives in its repo. Vault notes link and digest — they never fork state. If a note and a repo disagree, the repo wins and the note gets fixed.
2. **One vault, spanning all clones.** Open ~/GitLab/ (the existing local repos folder, per ORGANIZATION-SYSTEM §3) as a single Obsidian vault. The Obsidian config then lands in ~/GitLab/.obsidian/ — *outside every repo*, so no .gitignore is needed and no repo is dirtied. **Never open a single repo as its own vault** — that drops an .obsidian/ folder inside it.
3. **Removable, no glue — the Obsidian Protocol spirit.** The entire layer is kri/notes/ plus ~/GitLab/.obsidian/. Delete both and zero repo data is lost. Obsidian can be uninstalled tomorrow with nothing of value inside it.

## Under the Surface (what does NOT change)

- Git, CI, MRs, persona attribution — untouched. A note edit is a commit like any other, with branch prefix and trailers.
- VS Code edits these same files happily. Wiki-links and plugin blocks are inert text to every non-Obsidian tool.
- Commits are made in VS Code or the terminal — the org default. Obsidian stays the reading room. (The Obsidian Git plugin is allowed, but pick one owner per file state; never let both commit blindly.)

## Setup (once, ~2 minutes)

1. Obsidian → "Open folder as vault" → ~/GitLab
2. Core plugins on: Graph, Backlinks, Outline, Tags
3. Optional community plugins: Dataview (indexes and dashboards), Homepage (make Home the landing note)
4. Start walking from [[kri/notes/Home|Home]]
5. Link caveat: links assume clone folders are named exactly as the GitLab repos (kitsuneOS, Project-Kogane, ...) inside ~/GitLab/. Rename a clone → update Home.md.

## What Lives Where

- **Each repo** — the truth: PROJECT-STATUS.md, ADRs, design docs, plans, code
- **kri/notes/** — the layer: Home (front door MOC), Forge Notes (digest)
- **~/GitLab/.obsidian/** — app config; ignored by every repo, never committed
- **iPad** — Working Copy clones linked into an Obsidian vault (the ritual below)
- **Nowhere else** — no mirrored repo copies, ever; the repos are the single home (ORGANIZATION-SYSTEM §3)

## The iPad Ritual (Working Copy)

The iPad cannot open the Mac's folders — Working Copy is the bridge: a real git client that clones, pulls, commits, and pushes.

1. Install Working Copy; add each repo (https://gitlab.com/kitsune-kits/&lt;repo&gt;.git) with your GitLab username + personal access token. Clone and pull are free; pushing needs the one-time premium unlock.
2. In Obsidian on iPad: create an empty vault named kitsune-kits (stored On My iPad).
3. In each Working Copy repo: share menu → Link Repository to Folder → a subfolder inside the vault folder, named exactly as the repo (kri, kitsuneOS, ...). Home's wiki-links then resolve exactly like on the Mac.
4. Rhythm: pull in Working Copy before reading, edit in Obsidian, commit + push in Working Copy after.
5. The iPad vault's .obsidian config lives in the vault root, never inside a repo — the doctrine holds on both devices.

## The Theme — Kitsune Modern

*Tradition is the structure, the future is the light.* One snippet carries the brand into the vault: paper Foxfire White #F4F7F8, ink Sumi #0E1113, Gold-Leaf at the joints (titles, the breathing tab glow), jade for the living (links, active states), crimson for the sacred (errors and seals only — never beside jade in one component). Mincho for headings, Sans for body, Mono for code. Neon green does not exist in a polite universe.

- **Canonical source:** notes/theme/kri-theme.css in this repo. Presentation only — the repos stay the truth, and the theme never touches a repo's own files.
- **Mac ritual:** install the Mincho once (brew install --cask font-shippori-mincho), then copy the snippet into the vault and enable it:

      mkdir -p ~/GitLab/.obsidian/snippets
      cp ~/GitLab/kri/notes/theme/kri-theme.css ~/GitLab/.obsidian/snippets/

  then Obsidian → Settings → Appearance → CSS snippets → enable **kri-theme**.
- **iPad ritual:** the iPad vault has its own .obsidian — copy kri-theme.css from the Working Copy kri clone into the vault's .obsidian/snippets/ folder (Files app), then enable it under Settings → Appearance. On iPad the Mincho falls back gracefully (New York).
- **Removable:** delete the snippet and the theme is gone — no glue, no lock-in. The third law holds.

## Code in the Reading Room

Source files live in the repos, and the vault spans the repos — so code is viewable in Obsidian with two switches:

1. **Settings → Files & Links → Detect all file extensions — on.** Every file in every clone now appears in the file explorer and quick switcher (.rs, .lua, .c, .css, .sh, ...). Hidden folders (.git, .obsidian) stay hidden.
2. **Community plugin: Code Viewer.** Opens 50+ extensions (Rust, Lua, C, CSS, shell, ...) with syntax highlighting through Obsidian's own renderer — colors always follow the theme, so code wears Kitsune Modern too. Read-only by default: the reading room reads; edits stay deliberate.

- Wiki-links reach code directly: Home can link [[Project-Kogane/kogane.lua|kogane.lua]] or [[kri/notes/theme/kri-theme.css|the theme itself]].
- Trade-off: the file explorer grows dense — every repo file becomes visible. That is the point: the whole forge, readable from one room. Content search stays markdown-first; code is found by file name.
- The anvil stays the anvil: real editing sessions belong to VS Code / terminal. (If an in-vault editor is ever wanted, the VSCode Editor plugin brings Monaco in — not default doctrine.)
