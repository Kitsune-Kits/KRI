# Documentation Map — the KRI hub

> *Few documents, each excellent.* The hub holds no product code; it holds
> the org's shared paper. This page maps every shelf, so nothing has to be
> found twice.

Living page — maintained with the hub (org principle: one canonical source,
never copies). Dates are written in plain text on every surface.

---

## Reading paths

| Where you land | Start with |
|---|---|
| A new chat or session, anywhere in the org | [PROJECT-STATUS.md](../PROJECT-STATUS.md) — org-wide state; then the sibling repo's own `PROJECT-STATUS.md` |
| An agent (Vibe, Claude Code, VS Codium) about to work | [AGENTS.md](../AGENTS.md) — the org operating standard; each repo carries its own rules |
| New to KRI entirely | [ORG-CONTEXT.md](../ORG-CONTEXT.md) — what the forge is, Cyber Shinto, glossary, pull graph |
| Touching any KRI file, asset, or note | [ORGANIZATION-SYSTEM.md](../ORGANIZATION-SYSTEM.md) — organization canon; consult before creating, naming, moving, or tagging |

---

## Root canon

| File | Purpose |
|---|---|
| `README.md` | The front door — org intro, contents, repo index |
| `AGENTS.md` | Org-wide AI agent operating standard |
| `CLAUDE.md` | Claude Code entrypoint (imports AGENTS.md) |
| `ORG-CONTEXT.md` | What KRI is: philosophy, glossary, repo split, pull graph, history |
| `ORGANIZATION-SYSTEM.md` | How KRI organizes files — pillars, tags, sync, media toolchain |
| `PERSONA-ATTRIBUTION.md` | Ensemble attribution standard — branch prefixes, commit trailers, PR titles |
| `BRAND.md` | Brand palette canon — five-color core + persona sub-palettes (ADR-0001) |
| `BRAND-TYPOGRAPHY.md` | Typography canon — KRI Sans / Mincho / Mono, size scale (ADR-0002) |
| `BRAND-AESTHETIC.md` | Design language — Kitsune Modern (ADR-0003) |
| `BRAND-WORDMARK.md` | Wordmark & seal spec — the hanko (ADR-0004) |
| `STUDIES.md` | Index of Studies — the tier canon (ADR-0005) |
| `Forge Tasks.md` | The task layer (Now / Next / Someday) — Task Hub is a reading pane, never the source |
| `PROJECT-STATUS.md` | The status ledger — read live, never from memory |
| `SETUP-UI-CHECKLIST.md` | GitLab-era UI setup checklist — historical |
| `LICENSE` | Proprietary license — © 2026 KRI / Kitsune Kits |
| `.editorconfig`, `CODEOWNERS` | Housekeeping — formatting and review ownership |

---

## The docs tree

| Path | What lives there |
|---|---|
| [`decisions/`](decisions) | The decision log — ADRs (convention below) |
| [`infra/`](infra) | [CI-RUNNERS.md](infra/CI-RUNNERS.md) — the self-hosted GitLab group runner runbook (mirror era; the archive review decides its successor posture) |
| [`lessons/`](lessons) | [hardware-bringup.md](lessons/hardware-bringup.md) — bench lessons that generalize across repos |
| `WORKSPACE-INFRA-PROPOSAL.md` | Piko's GitLab Workspaces proposal — draft, awaiting the Architect's word; GitLab-era posture |

### ADR convention

Numbered, immutable, and merged by PR. Acceptance is final: a changed
decision gets a new ADR that supersedes the old — never an edit. The live
index is [decisions/README.md](decisions/README.md) (do not duplicate it
here); `TEMPLATE.md` is the blank.

Accepted on main today: ADR-0001 brand, 0002 typography, 0003 Kitsune
Modern, 0004 wordmark, 0005 Study tier, 0006 shared CI templates, 0007
platform sovereignty (the GitHub homecoming).

In flight: the ISO standards alignment rail — ADR-0008 through 0017, all
Proposed (PR #15).

Known seam (still open): **two files carry the number 0007** — the
platform-sovereignty homecoming ADR and the earlier P4 face-wing display
doctrine (Oct 26). ADRs are immutable, so the seam is flagged here rather
than silently renumbered; a convention ruling is pending the Architect's
word.

---

## The other wings

| Path | What lives there |
|---|---|
| [`notes/`](../notes) | The Obsidian vault layer over the repos: three laws in [VAULT.md](../notes/VAULT.md) (repos are the truth · one vault over all clones · removable, no glue), front door [Home.md](../notes/Home.md), org digest [Forge Notes.md](../notes/Forge%20Notes.md), task canon [TASKS-DOCTRINE.md](../notes/TASKS-DOCTRINE.md), Kitsune Modern theme in [`theme/`](../notes/theme) |
| [`pocket-forge/`](../pocket-forge) | The ensemble as Managed Agents — the deployable scaffold; keeps its own `README.md` + `PROJECT-STATUS.md` (first live run pending the bench) |
| [`bench-triage/`](../bench-triage) | Bench session triage tool (own README) |
| [`tools/`](../tools) | Forge tooling: `git-identity.sh`, `persona-router`, `apple-reminders-mcp`, `vscodium-brand` |
| [`.github/`](../.github) | CI: the reusable `agents-guard` workflow (every sibling repo calls it) + `repo-link-check` |
| [`.gitlab/`](../.gitlab) | GitLab-era templates + wiki content — dormant until the post-AWA archive decision |
| [`.vscode/`](../.vscode) | Bench workspace settings |

---

## Where state lives

- **State:** `PROJECT-STATUS.md` — here and in each repo; the source of truth, read live.
- **Tasks:** [Forge Tasks.md](../Forge%20Tasks.md) — Git-canonical; status prose stays in PROJECT-STATUS.md.
- **Decisions:** `decisions/` — immutable ADRs, superseded, never edited.
- **Vault notes:** link and digest; they never fork repo state.

---

*Built by Kitsune Research Industries (KRI).*
