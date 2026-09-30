#!/usr/bin/env bash
set -euo pipefail

# setup.sh / KRI VSCodium Forge Setup / Abstract: one-command forge
# bootstrap for VSCodium — installs the KRI extension rack, merges forge
# settings (clangd, Lua, error lens, KRI file associations) and keybindings,
# then hands off to install.sh for brand themes + icon theme. Idempotent;
# every merge is backed up first. Palette per BRAND.md / ADR-0001 (locked).
# v0.4.0

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SETTINGS="${VSCODIUM_USER_SETTINGS:-$HOME/.vscode-oss/User/settings.json}"
KEYBINDINGS="${VSCODIUM_USER_KEYBINDINGS:-$HOME/.vscode-oss/User/keybindings.json}"
BIN="${VSCODIUM_BIN:-codium}"

# --- 1. extension rack ---
if command -v "$BIN" >/dev/null 2>&1; then
  echo "→ installing extension rack"
  grep -vE '^\s*#' "$SCRIPT_DIR/extensions.txt" | grep -vE '^\s*$' | while read -r ext; do
    if "$BIN" --install-extension "$ext" >/dev/null 2>&1; then
      echo "   ✓ $ext"
    else
      echo "   ⚠ $ext unavailable on Open VSX — skipped"
    fi
  done
else
  echo "⚠ codium not found — install VSCodium or set VSCODIUM_BIN; extensions skipped."
fi

# --- 2. forge settings merge ---
FORGE_SETTINGS='{
  "clangd.arguments": ["--background-index", "--clang-tidy", "--header-insertion=iwyu"],
  "Lua.diagnostics.globals": ["kitnode", "kmod"],
  "Lua.runtime.version": "LuaJIT",
  "errorLens.enabled": true,
  "errorLens.exclude": ["info"],
  "editor.bracketPairColorization.enabled": true,
  "editor.stickyScroll.enabled": true,
  "editor.formatOnPaste": true,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "files.autoSave": "onFocusChange",
  "files.associations": {"*.kmod": "lua", "*.kmacro": "lua", "*.kspec": "yaml"},
  "search.exclude": {"**/build": true, "**/target": true, "**/.pio": true, "**/node_modules": true},
  "files.watcherExclude": {"**/build/**": true, "**/target/**": true, "**/.pio/**": true},
  "git.autofetch": true,
  "git.confirmSync": false,
  "gitlens.currentLine.enabled": true,
  "diffEditor.ignoreTrimWhitespace": false,
  "terminal.integrated.copyOnSelection": true
}'

if command -v jq >/dev/null 2>&1; then
  echo "→ merging forge settings into $SETTINGS"
  mkdir -p "$(dirname "$SETTINGS")"
  if [ -f "$SETTINGS" ]; then
    cp "$SETTINGS" "$SETTINGS.backup-kri"
    jq -s '.[0] * .[1]' "$SETTINGS" <(echo "$FORGE_SETTINGS") > "$SETTINGS.tmp" && mv "$SETTINGS.tmp" "$SETTINGS" || echo "⚠ merge failed — backup at $SETTINGS.backup-kri"
  else
    echo "$FORGE_SETTINGS" | jq '.' > "$SETTINGS"
  fi
else
  echo "⚠ jq not found — install it (brew install jq) and re-run for settings merge."
fi

# --- 3. keybindings ---
echo "→ writing keybindings ($KEYBINDINGS)"
mkdir -p "$(dirname "$KEYBINDINGS")"
if [ -f "$KEYBINDINGS" ]; then cp "$KEYBINDINGS" "$KEYBINDINGS.backup-kri"; fi
cp "$SCRIPT_DIR/keybindings.json" "$KEYBINDINGS"

# --- 4. brand themes + icons (the Ledger finish) ---
echo "→ running install.sh (brand themes + Kitsune Modern icons)"
bash "$SCRIPT_DIR/install.sh"

echo ""
echo "✅ forge ready. restart VSCodium: crab for Rust, moon-ears for KMODs, tea optional."
