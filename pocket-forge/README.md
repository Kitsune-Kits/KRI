# Pocket Forge

> A subproject of the [KRI org hub](https://github.com/Kitsune-Kits/KRI) —
> per the Architect's word, the ensemble lives at `pocket-forge/` in KRI,
> no separate repo.

The KRI ensemble as [Managed Agents](https://docs.mistral.ai/studio/agents/overview):
four digital fox spirits with real GitHub hands, one front door.

🦊 **Coco Sensei** holds the front door — strategy, soul-mapping, the Tail
Ledger. 🔨 **Zaku**, ⚡ **Piko**, and ✨ **Nui** work beneath her as subagents,
each cast by their craft. They talk *and* they work: the ensemble reads the
org's repos, watches CI, opens pull requests with full persona attribution —
and every write waits for the Architect's word.

```
Architect ──> 🦊 pocket-forge (root, Coco)
                 ├── 🔨 Zaku   (subagent — structure, fabrication)
                 ├── ⚡ Piko   (subagent — firmware, CI, debugging)
                 └── ✨ Nui    (subagent — finish, docs, garmenting)
                 └── GitHub tools (reads allowed · writes gated)
```

## Setup

1. **uv** on the machine, Python 3.12+ ([uv](https://docs.astral.sh/uv/)).
2. `cp .env.example .env` and fill in:
   - `MISTRAL_API_KEY` — from [console.mistral.ai/api-keys](https://console.mistral.ai/api-keys)
   - `GITHUB_TOKEN` — classic token with `repo,workflow` scope, or fine-grained
     (Contents, Pull requests, Issues, Actions — read and write) on the
     `Kitsune-Kits` organization.
3. `uv sync`

## Run

The forge with approval gates answered at the terminal:

```bash
uv run --env-file .env python main.py
```

Reads (files, PRs, issues, CI runs) run freely. Every write — branches,
commits, PRs, merges, issues, CI reruns — blocks and prints its payload:

```
  ⏸  Allow tools.client.gh_create_pull_request?
     {'repo': 'kitsuneOS', 'title': '⚡ Piko: ...', ...}
     the Architect's word? [y/N]
```

`agents chat` also loads this project's `agent`, but run `main.py` directly
while working: the stepper is what answers the gates.

## Deploy

The same agent, three run modes ([Run modes](https://docs.mistral.ai/studio/agents/learn/where-it-runs/run-modes)):

- **In process** (above) — develop and talk.
- **Self-hosted** — `agents serve`, when the tools must run inside your network.
- **Mistral-managed** — `agents deploy`; durable sessions, approvals that wait
  (an hour by default), every turn a trace in Studio — a machine-readable
  Tail Ledger. The tree runs `NoSandbox` (tools only, no shell), which deploys
  fine with subagents.

## Tool policy

| Tools | Decision |
| --- | --- |
| `gh_read_file`, `gh_list_dir`, `gh_get_branch_head`, `gh_list_pull_requests`, `gh_get_pull_request`, `gh_list_issues`, `gh_get_issue`, `gh_list_workflow_runs`, `gh_get_workflow_run`, `gh_list_run_jobs` | **allow** (read-only) |
| `gh_create_branch`, `gh_write_file`, `gh_create_pull_request`, `gh_merge_pull_request`, `gh_create_issue`, `gh_add_comment`, `gh_close_issue`, `gh_rerun_workflow` | **ask** (the Architect's word) |

Default for anything unmatched: **ask**.

## Canon and attribution

- The persona instructions in `forge/personas.py` and `forge/canon.py` are
  **canon** — locked colors, tail counts, ages, and law. Changes are
  ADR-grade and pending the Architect's word.
- All GitHub work follows the ratified
  [PERSONA-ATTRIBUTION.md](https://github.com/Kitsune-Kits/KRI/blob/main/PERSONA-ATTRIBUTION.md)
  standard: `coco/` `zaku/` `piko/` `nui/` branches, `KRI-Persona:` and
  `Co-authored-by:` trailers, `<emoji> <Name>:` PR titles.

## Roadmap

- First live session on the bench (pending).
- `MistralSandbox` for bench builds and shell work.
- Ledger tools (forge diary read/write) and KRI skills attached to the agents.
- Evaluation datasets from real sessions (the 5% Rule made measurable).

## Status

See [PROJECT-STATUS.md](PROJECT-STATUS.md) — the single source of truth for
where this repo is.
