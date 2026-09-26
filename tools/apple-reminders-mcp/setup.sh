#!/usr/bin/env bash
#
# setup.sh / apple-reminders-mcp / KRI
# Idempotent local setup: dependencies, Keychain token, LaunchAgent auto-start,
# managed-account auto-detection, and (with --tunnel) a Tailscale Funnel
# bootstrap. Run from the tools/apple-reminders-mcp directory.
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

# --- 5. Optional: Tailscale Funnel bootstrap ------------------------------------
if [ -n "$WANT_TUNNEL" ]; then
  echo ""
  if ! command -v tailscale >/dev/null 2>&1; then
    echo "Installing Tailscale via Homebrew..."
    brew install --cask tailscale
    echo "Tailscale installed. Open the Tailscale app (or menu bar icon) and log in,"
    echo "then re-run: ./setup.sh --tunnel"
    exit 0
  fi
  if ! tailscale status >/dev/null 2>&1; then
    echo "Tailscale is not logged in. Open the Tailscale app and log in,"
    echo "then re-run: ./setup.sh --tunnel"
    exit 0
  fi
  tailscale funnel --bg 3000 || true
  echo ""
  echo "Funnel status:"
  tailscale funnel status || true
  echo ""
  echo "Remaining manual steps:"
  echo "  1. If Funnel needs enabling on the tailnet (one-time): admin console"
  echo "     -> Access Controls -> add the funnel attribute. See launchd/TAILSCALE.md"
  echo "  2. Register the connector in Mistral:"
  echo "     URL:   https://<your-host>.<tailnet>.ts.net/mcp   (from funnel status above)"
  echo "     Token: security find-generic-password -w -s com.kitsunekits.reminders-mcp"
fi

echo ""
echo "Done. The server is at http://127.0.0.1:3000/mcp"
