# Tunnel + Cloudflare Access — apple-reminders-mcp

The server binds to `127.0.0.1:3000`. The tunnel is the only door, and it has
two locks: a Cloudflare Access identity policy, then the server's Keychain
bearer token.

## 1. Named tunnel

```bash
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create reminders-mcp
```

`~/.cloudflared/config.yml` (mode 0600):

```yaml
tunnel: <TUNNEL-UUID>
credentials-file: /Users/<you>/.cloudflared/<TUNNEL-UUID>.json
ingress:
  - hostname: reminders.<your-domain>.com
    service: http://127.0.0.1:3000
  - service: http_status:404
```

DNS route (one time): `cloudflared tunnel route dns reminders-mcp reminders.<your-domain>.com`

## 2. Cloudflare Access (the identity wall)

In the Cloudflare Zero Trust dashboard:

1. Add an **Access > Applications** entry for `reminders.<your-domain>.com`.
2. Policy: allow only your managed Apple Business email (via Google, Apple, or
   GitLab IdP login — pick one and keep it narrow).
3. Session duration: keep short (e.g. 24h) — Mistral's requests carry the
   bearer token, but Access still gates the *first* reachability.

Note: for programmatic (non-interactive) clients like Mistral's connector, use
a **Service Token** in the Access policy instead of interactive IdP login, and
store those credentials in Mistral's connector config — never in the repo.

## 3. Run as a service (auto-start on boot)

```bash
sudo cloudflared service install
```

`launchctl unload ~/Library/LaunchAgents/com.kitsunekits.reminders-mcp.plist`
and `sudo cloudflared service uninstall` return you to the session-scoped
posture at any time.

## 4. Register in Mistral

Custom MCP connector: URL `https://reminders.<your-domain>.com/mcp`, auth
Bearer = the Keychain token from `setup.sh` (retrieve once:
`security find-generic-password -w -s com.kitsunekits.reminders-mcp`).
