#!/usr/bin/env bash
#
# setup.sh / apple-reminders-mcp / KRI
# Idempotent local setup: dependencies, Keychain token, LaunchAgent auto-start,
# managed-account auto-detection, and (with --tunnel) a guided Cloudflare
# Tunnel bootstrap. Run from the tools/apple-reminders-mcp directory.
# Copyright (c) 2026 Kitsune Kits. All rights reserved.
#
set -euo pipefail

DIR="$PWD"
SERVICE="com.kitsunekits.reminders-mcp"
WANT_TUNNEL=""

for arg in "$@"; do
  case "$arg" in
    --tunnel) WANT_TUNNEL=1 ;;
    *) echo "unknown flag: $arg" >&2; exit 1 ;;
  esac
done

# --- 1. Dependencies ---------------------------------------------------------
if ! command -v node >/dev/null 2>&1; then
  echo "node is required (brew install node)" >&2; exit 1
fi
NODE_BIN=$(command -v node)
npm install

# --- 2. Non-secret config + managed-account auto-detection --------------------
# Ask Reminders itself what accounts exist (triggers the Automation prompt —
# approve it; this is the same permission the server needs).
ACCOUNTS_JSON=$(osascript -l JavaScript -e \
  'const Rem = Application("Reminders");
   JSON.stringify(Rem.accounts().map(function (a) { return a.name(); }))')
ACCOUNTS=$(echo "$ACCOUNTS_JSON" | tr -d '[]"' | tr ',' '\n' | sed 's/^ *//')

if [ ! -f .env ]; then
  DEFAULT_ACCOUNT=""
  NON_PERSONAL=$(echo "$ACCOUNTS" | grep -viE '^(iCloud|On My Mac|此 Mac.*)$' || true)
  NON_PERSONAL_COUNT=$(echo "$NON_PERSONAL" | grep -c . || true)
  if [ "$NON_PERSONAL_COUNT" -eq 1 ]; then
    DEFAULT_ACCOUNT="$NON_PERSONAL"
    echo "Detected managed account: $DEFAULT_ACCOUNT"
  elif [ "$NON_PERSONAL_COUNT" -gt 1 ]; then
    echo "Multiple non-personal accounts found:"
    echo "$NON_PERSONAL" | nl
    read -r -p "Enter the exact account name for DEFAULT_ACCOUNT (blank = all accounts): " DEFAULT_ACCOUNT
  else
    echo "No managed account detected — DEFAULT_ACCOUNT left blank (all accounts)."
  fi
  cat > .env <<EOF
# Non-secret config only. The bearer token lives in the macOS Keychain.
DEFAULT_ACCOUNT=${DEFAULT_ACCOUNT}
PORT=3000
EOF
  chmod 600 .env
  echo "Created .env (DEFAULT_ACCOUNT set)."
else
  echo ".env exists — leaving it alone."
fi

# --- 3. Bearer token -> Keychain (idempotent) --------------------------------
if security find-generic-password -s "$SERVICE" >/dev/null 2>&1; then
  echo "Keychain entry exists — keeping the existing token."
else
  TOKEN=$(openssl rand -hex 32)
  security add-generic-password -a "$USER" -s "$SERVICE" -w "$TOKEN"
  echo "Token stored in Keychain (shown once): $TOKEN"
fi

# --- 4. LaunchAgent (auto-start on login, localhost only) ---------------------
PLIST="$HOME/Library/LaunchAgents/$SERVICE.plist"
mkdir -p "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$SERVICE</string>
  <key>ProgramArguments</key>
  <array>
    <string>$NODE_BIN</string>
    <string>$DIR/server.mjs</string>
  </array>
  <key>WorkingDirectory</key><string>$DIR</string>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>$DIR/server.log</string>
  <key>StandardErrorPath</key><string>$DIR/server.log</string>
</dict>
</plist>
EOF
chmod 600 "$PLIST"
launchctl unload "$PLIST" >/dev/null 2>&1 || true
launchctl load "$PLIST"
echo "LaunchAgent installed — the server auto-starts on login."

# --- 5. Optional: tunnel bootstrap ---------------------------------------------
if [ -n "$WANT_TUNNEL" ]; then
  echo ""
  if ! command -v cloudflared >/dev/null 2>&1; then
    echo "Installing cloudflared via Homebrew..."
    brew install cloudflared
  fi
  if [ ! -f "$HOME/.cloudflared/cert.pem" ]; then
    echo "cloudflared needs a one-time browser login."
    cloudflared tunnel login
  fi
  if cloudflared tunnel info reminders-mcp >/dev/null 2>&1; then
    echo "Tunnel 'reminders-mcp' already exists — reusing it."
  else
    cloudflared tunnel create reminders-mcp
  fi
  TUNNEL_UUID=$(cloudflared tunnel list -o json | /usr/bin/python3 -c \
    'import json,sys; print([t["id"] for t in json.load(sys.stdin) if t["name"]=="reminders-mcp"][0])')
  CFG="$HOME/.cloudflared/config.yml"
  if [ ! -f "$CFG" ]; then
    read -r -p "Hostname for the tunnel (e.g. reminders.example.com): " HOSTNAME
    cat > "$CFG" <<EOF
tunnel: $TUNNEL_UUID
credentials-file: $HOME/.cloudflared/$TUNNEL_UUID.json
ingress:
  - hostname: $HOSTNAME
    service: http://127.0.0.1:3000
  - service: http_status:404
EOF
    chmod 600 "$CFG"
    cloudflared tunnel route dns reminders-mcp "$HOSTNAME"
    echo "Tunnel config written and DNS routed."
  else
    echo "config.yml exists — leaving it alone."
  fi
  echo ""
  echo "Remaining manual steps (cannot be automated from this shell):"
  echo "  1. Cloudflare Zero Trust dashboard -> Access -> Applications:"
  echo "     add a policy for your hostname (Service Token for Mistral)."
  echo "  2. sudo cloudflared service install   (tunnel auto-starts on boot)"
  echo "  3. Register the connector in Mistral (URL + Keychain token)."
  echo "     Full guide: launchd/CLOUDFLARED.md"
fi

echo ""
echo "Done. The server is at http://127.0.0.1:3000/mcp"
