#!/usr/bin/env bash
#
# install.sh / apple-reminders-mcp / KRI
# One-command bootstrap: clone the kri repo (private), then run setup.sh
# with account auto-detection and optional tunnel bootstrap.
# Requires: GITLAB_TOKEN env var (a personal access token with read_api).
# Copyright (c) 2026 Kitsune Kits. All rights reserved.
#
set -euo pipefail

: "${GITLAB_TOKEN:?Set GITLAB_TOKEN first — the repo is private:
  export GITLAB_TOKEN=glpat-...   (read_api scope is enough)}"

DEST="$HOME/kri"
REPO="https://oauth2:${GITLAB_TOKEN}@gitlab.com/kitsune-kits/kri.git"

if ! command -v git >/dev/null 2>&1; then
  echo "git is required (xcode-select --install)" >&2; exit 1
fi

# --- 1. Clone or update the repo --------------------------------------------
if [ -d "$DEST/.git" ]; then
  echo "Updating existing checkout at $DEST..."
  git -C "$DEST" fetch origin main --quiet
  git -C "$DEST" checkout main --quiet
  git -C "$DEST" reset --hard origin/main --quiet
else
  echo "Cloning kitsune-kits/kri into $DEST..."
  git clone --depth 1 "$REPO" "$DEST"
fi
# Never leave the token in .git config or the working tree.
git -C "$DEST" remote set-url origin "https://gitlab.com/kitsune-kits/kri.git" 2>/dev/null || true

# --- 2. Run the full setup ----------------------------------------------------
cd "$DEST/tools/apple-reminders-mcp"
./setup.sh --tunnel

echo ""
echo "Binding complete. Register in Mistral:"
echo "  URL:   https://reminders.<your-domain>/mcp"
echo "  Token: security find-generic-password -w -s com.kitsunekits.reminders-mcp"
