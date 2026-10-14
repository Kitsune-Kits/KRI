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
