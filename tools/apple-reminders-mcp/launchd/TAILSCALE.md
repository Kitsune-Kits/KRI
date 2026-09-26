# Tailscale Funnel — apple-reminders-mcp

Replaces Cloudflare Tunnel as the public door (September 2026 — the Architect
has no Cloudflare zone; Funnel needs no domain). The server binds
`127.0.0.1:3000`; Funnel exposes it at a stable HTTPS URL.

## 1. Install & log in

```bash
brew install --cask tailscale
open -a Tailscale   # menu bar icon -> log in (Google/Apple/GitHub SSO)
```

Tailscale auto-starts on login, which is what makes the whole chain seamless
after reboot.

## 2. Enable Funnel on the tailnet (one-time)

Funnel is opt-in per tailnet. Run `tailscale funnel 3000` once — if the
client asks for tailnet approval, allow `funnel` for your user in the admin
console (https://login.tailscale.com/admin/acls):

```json
"nodeAttrs": [
  { "target": ["autogroup:member"], "attr": ["funnel"] }
]
```

## 3. Serve (stable, background, survives reboot)

```bash
tailscale funnel --bg 3000
```

You get a stable URL like `https://mac-name.tailnet-name.ts.net` — TLS is
handled by Tailscale (Let's Encrypt, auto-renewed). `--bg` makes it a
background service that restarts on login.

## 4. Register in Mistral

Custom MCP connector:

- **URL:** `https://<your-host>.<tailnet>.ts.net/mcp`
- **Auth:** Bearer = the Keychain token
  (`security find-generic-password -w -s com.kitsunekits.reminders-mcp`)

## Security model (updated)

The Cloudflare Access identity wall is gone; what remains:

1. **TLS** — Tailscale terminates HTTPS with auto-renewed certs.
2. **Bearer token** — Keychain-stored, required on every request.
3. **DEFAULT_ACCOUNT** — server-side scoping to the managed Apple Business account.
4. **Funnel is inbound-only** — Funnel routes internet traffic INTO the
   exposed port; it grants no tailnet or device access.

For a single-user setup with a 64-hex Keychain token, the bearer check does
the real work. To add an identity wall later, put any auth proxy in front of
the Funnel URL — the server does not care what precedes it.

## Tear-down

```bash
tailscale funnel off
launchctl unload ~/Library/LaunchAgents/com.kitsunekits.reminders-mcp.plist
```
