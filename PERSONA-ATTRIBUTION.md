# PERSONA-ATTRIBUTION.md — KRI ensemble attribution standard

The KRI ensemble works through Vibe as four distinct personas. The GitLab MCP
connector authenticates as a single GitLab account, so attribution is achieved
through branch naming, commit trailers, and MR metadata.

## Persona identities

| Persona | Emoji | Role | Branch prefix | Git identity (metadata) |
|---|---|---|---|---|
| Coco Sensei | 🦊 | Strategy, documentation, architecture | `coco/` | `Coco Sensei <coco@kitsune-kits.gitlab>` |
| Zaku | 🔨 | CAD, fabrication, structural engineering | `zaku/` | `Zaku <zaku@kitsune-kits.gitlab>` |
| Piko | ⚡ | Firmware, logic, electronics | `piko/` | `Piko <piko@kitsune-kits.gitlab>` |
| Nui | ✨ | Finishing, garmenting, surface, color | `nui/` | `Nui <nui@kitsune-kits.gitlab>` |

These git identities are metadata conventions — not real GitLab accounts. The
commit is pushed by the single authenticated connector account.

## Branch naming

`<persona>/<short-description>` — e.g. `piko/blade-sled-i2c`,
`zaku/drop-test-bracket`, `nui/garmenting-spec-m5`, `coco/architecture-milestone-4`.
Conventional commit types (`feat`, `fix`, `docs`, `chore`, `refactor`) go in
commit messages, not branch names.

## Commit message convention

Every commit includes:
1. Standard conventional commit header
2. Persona attribution line (emoji + name + role tag)
3. `KRI-Persona:` trailer (machine-parseable)
4. `Co-authored-by:` trailer

Single-persona example:
```
feat(blade-sled): add I2C init sequence

⚡ Piko — firmware

KRI-Persona: Piko
Co-authored-by: Piko <piko@kitsune-kits.gitlab>
```

Multi-persona (ensemble) example:
```
feat(housing): integrate PCB mount with structural frame

🔨 Zaku — structural (lead)
Co-authored-by: Piko <piko@kitsune-kits.gitlab>
Co-authored-by: Nui <nui@kitsune-kits.gitlab>
KRI-Persona: Zaku
```

## Merge request convention

- **Title:** persona emoji + name + colon (e.g., `⚡ Piko: Blade Sled I2C init sequence`)
- **Description:** includes `KRI-Persona:` line and brief role note
- **Source branch:** uses persona's branch prefix
- **Multi-persona MR:** lead persona owns branch/title; others listed under a
  `KRI Contributors:` section

## Domain → persona mapping

| When working on... | Primary persona | Branch prefix |
|---|---|---|
| Firmware, code, electronics, debugging | ⚡ Piko | `piko/` |
| CAD, fabrication, structural design | 🔨 Zaku | `zaku/` |
| Finishing, surface, color, garmenting | ✨ Nui | `nui/` |
| Documentation, architecture, strategy | 🦊 Coco | `coco/` |
| Multiple personas (ensemble work) | Lead persona's prefix | Lead's `<prefix>/` |