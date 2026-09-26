#!/usr/bin/env bash
#
# setup.sh / apple-reminders-mcp / KRI
# Idempotent local setup: dependencies, Keychain token, LaunchAgent auto-start.
# Run from the tools/apple-reminders-mcp directory of your kri checkout.
# Copyright (c) 2026 Kitsune Kits. All rights reserved.
#
set -euo pipefail

DIR="$PWD"
SERVICE="com.kitsunekits.reminders-mcp"

# --- 1. Dependencies ---------------------------------------------------------
if ! command -v node >/dev/null 2>&1; then
  echo "node is required (brew install node)" >&2; exit 1
fi
NODE_BIN=$(command -v node)
npm install

# --- 2. Non-secret config ----------------------------------------------------
if [ ! -f .env ]; then
  cat > .env <<EOF
# Non-secret config only. The bearer token lives in the macOS Keychain.
DEFAULT_ACCOUNT=
PORT=3000
EOF
  chmod 600 .env
  echo "Created .env — set DEFAULT_ACCOUNT to your managed account after running list_accounts."
fi

# --- 3. Bearer token -> Keychain (idempotent replace) -------------------------
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

echo ""
echo "Done. The server auto-starts on login at http://127.0.0.1:3000/mcp"
echo "Next: see launchd/CLOUDFLARED.md for the tunnel + Cloudflare Access steps,"
echo "then register the URL + Keychain token in Mistral as a custom MCP connector."
