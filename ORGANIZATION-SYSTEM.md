# KRI Organization System

> The canonical reference for how Kitsune Research Industries organizes its files, tags, tools, and media.
> Established September 2026. When doing *anything* with KRI files, consult this document first.

---

## 1. The Pillar Structure (iCloud Drive)

All KRI work lives in the **business iCloud Drive** under five numbered pillars:

```
iCloud Drive/
├── 00-KRI/           # Org hub: decisions, templates, standards
├── 01-Internal/      # Internal projects (one folder per project)
├── 02-Client/        # Client projects (one folder per client)
├── 03-Resources/     # Shared reusable library
├── 04-Operations/    # Business operations
└── 05-Archive/       # Completed projects, by year
```

### 00-KRI — Org Hub
- `Decisions/` — decision records
- `Templates/` — README-template.md, POSTMORTEM-template.md, project folder templates

### 01-Internal / 02-Client — Project Folders
Per-project template structure:

```
[Project]/
├── README.md
├── Design/
├── Engineering/
├── Media/
│   ├── Audio/
│   ├── Video/
│   └── Photos/
└── Business/
```

Client deliverables: `02-Client/[Client]/Deliveries/[YYYY-MM-DD]-[Type]/`

### 03-Resources — Shared Library
```
03-Resources/
└── Media/
    ├── Audio/
    │   ├── Logic-Pro/Templates/      # Mechanical, Electronic, Ambient sound templates
    │   ├── MainStage/                # KRI Demo Rig concerts
    │   └── Sound-Effects/Libraries/  # Reusable prop sounds (by type)
    ├── Video/
    │   ├── Final-Cut/                # Shared FCP libraries
    │   └── Motion/                   # Motion graphics working files
    ├── LUTs/                         # KRI look library (.cube) — applied in the edit, never baked into export presets
    └── *.app                         # Compressor droplets (see §4)
```

### 05-Archive
`05-Archive/[YYYY]/[Project]-Completed/` — includes `POSTMORTEM.md`.

---

## 2. Finder Tag Vocabulary

Order: `Context · Project · Department · Content · Status · Format`

| Tag class | Values |
|---|---|
| Context | `Internal`, `Client`, `Resource`, `Reference` |
| Project | Project/client name (e.g. `Saffron-Blossom`, `Kogane`) |
| Department | `Design`, `Engineering`, `Media`, `Business` |
| Content | `Sound-Effect`, `Video`, `Photo`, `CAD`, `Firmware`, `Logic-Pro`, `Final-Cut`, `Motion`, `MainStage`, `Compressor` |
| Status | `Draft`, `Final`, `Client-Review`, `Urgent` |
| Format | `WAV`, `MP3`, `MOV`, `STL`, etc. |

Examples:
- Work file: `Internal · Saffron-Blossom · Engineering · CAD · Draft · STL`
- Tool/template: `Resource · Media · Logic-Pro · Final · Reference`

**Rules:** pick one vocabulary and stay consistent; tools and templates always get `Resource ... Final · Reference`.

---

## 3. GitLab ↔ iCloud Sync

- Local repos live in `~/GitLab/`; the GitLab group is `kitsune-kits` on gitlab.com.
- `~/GitLab/sync-to-icloud.sh` mirrors repos into the matching pillar folders (rsync, runs every 30 min via cron: `*/30 * * * * /bin/bash ~/GitLab/sync-to-icloud.sh`).
- Log: `~/GitLab/sync.log`.
- ⚠️ The business iCloud root is the Daemon Containers path on the synced volume — copy the path from Finder's "Copy as Pathname," never hand-type it (a single wrong character silently breaks the sync).

---

## 4. Media Toolchain (Apple Creator Studio)

### Compressor presets & droplets (in `03-Resources/Media/`)

| Droplet | Format | Use |
|---|---|---|
| `KRI-Client-Delivery` | 1080p H.264, 12 Mbps, AAC 256 | Everything sent to a client |
| `KRI-Web-Demo` | 720p H.264, 6 Mbps, AAC 192, fast-start | Web embeds & quick shares |
| `KRI-Archive` | ProRes 422, source resolution, PCM 24-bit | Archival masters |
| `KRI-Social-Vertical` | 1080×1920 H.264, 8 Mbps | Instagram/TikTok |
| `KRI-Review-Proxy` | 540p H.264, 3 Mbps | Internal review copies |

**Philosophy:** no LUTs or creative grading in export presets — grade in the timeline (Final Cut), export clean. Droplets are tagged `Resource · Media · Compressor · Final · Reference`.

### Logic Pro (sound design for props)

- Templates in `03-Resources/Media/Audio/Logic-Pro/Templates/`: `Mechanical-Sound-Template`, `Electronic-Sound-Template`, `Ambient-Sound-Template`. Modern instruments only (Alchemy, Retro Synth, ChromaVerb) — no legacy ES synths.
- Save via File → Save as Template (internal folder), then mirror to 03-Resources.
- Export presets: `KRI-High-Quality` (WAV 24-bit/48k stereo), `KRI-Embedded` (WAV 16-bit/44.1k **mono**, normalize off — firmware files), `KRI-Web` (MP3 320).
  - In Logic 12's bounce dialog, WAV lives under the **Uncompressed** family.
- Firmware audio filenames: lowercase, underscores, no spaces, no version numbers.

### Final Cut Pro
- Per-project libraries in `[Project]/Media/Video/[Project].fcpbundle`; shared assets in `03-Resources/Media/Video/Final-Cut/`.
- Keep active libraries local-first; let iCloud sync a copy (FCP bundles are sluggish mid-sync).

### Motion
- Working files in `03-Resources/Media/Video/Motion/`; publish templates to Final Cut under the `KRI` category.

### MainStage
- KRI Demo Rig concerts in `03-Resources/Media/Audio/MainStage/` — live prop-sound triggering from the shared sound library.

---

## 5. Shortcuts (macOS 27 "Describe a Shortcut")

Built with the AI shortcut builder; tag application uses a native **Run AppleScript** step (Finder has no native Shortcuts tag action — no third-party dependencies).

| Shortcut | Purpose |
|---|---|
| `KRI Media Ingest` | Ask project + category → save media to the right pillar folder → apply tags |
| `KRI Client Delivery` | Ask client (dynamic menu from 02-Client folders) + delivery type → create dated deliverables folder → copy, tag, zip, share |
| `KRI New Project` | Ask internal/client + name → scaffold project folder template + README.md → apply tags |
| `KRI Archive Project` | Move project to `05-Archive/[YYYY]/[Project]-Completed/` + add POSTMORTEM.md |

Tagging AppleScript pattern (additive):

```applescript
on run {input, parameters}
    tell application "Finder"
        repeat with f in input
            set f to (f as alias)
            set existingTags to tagNames of f
            set tagNames of f to existingTags & {"Project-Name", "Department", "Draft"}
        end repeat
    end tell
    return input
end run
```

Known limitation: batch-retagging entire archived folder trees is not native — do it via Terminal or accept legacy tags.

---

## 6. Guiding Principles

1. **Apple-inspired:** few things done exceptionally; standards enforced by tooling, not memory; craft on every surface; say no to bloat.
2. **No third-party dependencies** where macOS can do it natively (rsync, cron, AppleScript, afconvert, stock apps).
3. **The Obsidian Protocol spirit:** tools must be removable and modular — no glue, no lock-in.
4. **Decisions are written down** — this file, the decision records in `00-KRI/Decisions/`, and the ADRs in this repo's `docs/decisions/`.
5. **The Vessel's kami must always feel welcome.**

---

## 7. Obsidian Vault Layer (October 2026)

Obsidian is the reading room, not the archive: **the repos remain the source of truth.**

- **Vault root:** open ~/GitLab/ (the local repos folder, §3) as one vault spanning all clones. The .obsidian/ config then lives at ~/GitLab/.obsidian/ — *outside every repo*, so no repo is dirtied and no .gitignore is needed. Never open a single repo as its own vault.
- **The layer lives in kri/notes/** — Home (front-door MOC), Forge Notes (digest), VAULT (doctrine + setup). See notes/VAULT.md. Removable in one folder delete — Obsidian Protocol spirit, no glue, no lock-in.
- **Notes link and digest; they never fork state.** PROJECT-STATUS.md in each repo stays the single source of truth. When a note and a repo disagree, the repo wins and the note gets fixed.
- **Under the surface, nothing changes:** git, CI, MRs, persona attribution, VS Code. A note edit is a commit like any other; commits happen in VS Code or the terminal, not inside Obsidian.
