# Security Policy — apple-reminders-mcp

## Threat model

The server accepts requests from the internet (via tunnel) and holds macOS
Automation access to Reminders on the Architect's Mac. It must never leak or
accept commands outside the managed Apple Business account.

## Controls

| Layer | Control |
|---|---|
| Secret storage | Bearer token in macOS Keychain (`com.kitsunekits.reminders-mcp`); no plaintext secret files, nothing in the repo or LaunchAgent |
| Transport auth | `Authorization: Bearer` required on every `POST /mcp`; constant-time comparison is a future hardening item |
| Network | Server binds `127.0.0.1` only; the Cloudflare Tunnel is the sole ingress |
| Identity wall | Cloudflare Access (Zero Trust) policy on the tunnel hostname requires an approved identity before requests reach the server |
| Blast radius | `DEFAULT_ACCOUNT` policy force-scopes all tools to the managed account; other accounts are rejected server-side |
| On disk | `.env` and the LaunchAgent plist are mode 0600; `server.log` must never be committed |
| CI | Secret detection over this path; any Keychain-formatted token or `.env` in a commit fails the pipeline |
| Revocation | `security delete-generic-password -s com.kitsunekits.reminders-mcp` + rotate in Mistral; also rotate the tunnel credential if the URL leaks |

## Never commit

`.env`, `server.log`, `~/.cloudflared/` credentials, Keychain dumps.

## Reporting

Report security issues via the org `SECURITY.md` contact. Do not open public
issues for suspected vulnerabilities.
