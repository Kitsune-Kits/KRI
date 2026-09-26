# apple-reminders-mcp

A Node MCP server that exposes macOS **Apple Reminders** (via a JXA bridge) to
Mistral, over Streamable HTTP with **Keychain-backed bearer auth**. Runs on the
Architect's Mac as a hardened LaunchAgent behind a Cloudflare Tunnel guarded by
Cloudflare Access.

## Tools

| Tool | Purpose |
|---|---|
| `list_accounts` | List Reminders accounts (iCloud, On My Mac, managed) |
| `list_lists` | Lists, optionally scoped to one account |
| `list_reminders` | Filter by account / list / completion state |
| `create_reminder` | Create, with account + list targeting |
| `complete_reminder` | Complete by id |
| `delete_reminder` | Delete by id |

## Security model

Three independent walls (see `SECURITY.md` for the full threat model):

1. **Keychain** — the bearer token lives in the macOS Keychain, never in a file
   or the repo. Revocation is one `security delete-generic-password` command.
2. **DEFAULT_ACCOUNT policy** — when set in `.env`, the server force-scopes
   every call to the managed Apple Business account and rejects any request
   naming a different account. Personal iCloud lists are unreachable.
3. **Cloudflare Access** — an identity wall (Zero Trust policy on the tunnel
   hostname) in front of the bearer check. See `launchd/CLOUDFLARED.md`.

The server binds to `127.0.0.1` only — the tunnel is the single door.

## One-command install

With a GitLab personal access token (read_api scope) exported:

```bash
export GITLAB_TOKEN=glpat-...
bash <(curl -fsSL \
  -H "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "https://gitlab.com/api/v4/projects/86534918/repository/files/tools%2Fapple-reminders-mcp%2Finstall.sh/raw?ref=main")
```

It clones the repo into ~/kri, then runs `setup.sh --tunnel`: dependencies,
Keychain token, LaunchAgent auto-start, managed-account auto-detection, and a
guided Cloudflare Tunnel bootstrap. The token requirement is intentional —
the repo is private, so the bootstrap only runs for you. The Cloudflare
Access policy and the Mistral connector registration remain manual
(`launchd/CLOUDFLARED.md`).

## Quick start

```bash
cd tools/apple-reminders-mcp
./setup.sh          # deps + Keychain token + LaunchAgent (auto-start on login)
```

On the first tool call, macOS prompts to allow node to control Reminders —
approve it (System Settings → Privacy & Security → Automation to re-grant).

Then set `DEFAULT_ACCOUNT` in `.env` to the managed account's exact name
(run `list_accounts` first), and follow `launchd/CLOUDFLARED.md` for the
tunnel. Register `https://<tunnel-host>/mcp` + the Keychain token in Mistral
as a custom MCP connector.

## Layout

```text
tools/apple-reminders-mcp/
├── README.md
├── SECURITY.md
├── package.json
├── .env.example        # non-secret config only
├── server.mjs          # MCP server (HTTP transport, auth, account policy)
├── jxa.mjs             # Reminders bridge (serialized JXA, no shell quoting)
├── setup.sh            # idempotent local setup + LaunchAgent install
└── launchd/
    ├── com.kitsunekits.reminders-mcp.plist   # reference copy (setup.sh writes the real one)
    └── CLOUDFLARED.md                         # tunnel + Cloudflare Access steps
```

## Notes

- JXA `dueDate` handling is timezone-naive in places; pass ISO strings with
  explicit offsets for reliability.
- Managed accounts sync via Apple Business (iCloud infrastructure), so writes
  propagate across devices — with occasional sync lag if re-listed immediately.
- To return to a session-scoped posture: `launchctl unload` the agent and
  `cloudflared service uninstall`.
