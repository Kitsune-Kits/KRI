#!/usr/bin/env bash
set -euo pipefail

# install.sh / Kitsune Modern VSCodium Brand Theme / Abstract: installs the
# KRI brand themes (Foxfire light, Sumi dark), the Kitsune Modern file icon
# theme, and brand settings into VSCodium. Palette per BRAND.md / ADR-0001
# (locked). Neon green forbidden.
# v0.2.0 — icon theme added

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXT_DIR="${VSCODIUM_EXTENSIONS_DIR:-$HOME/.vscode-oss/extensions}/kri-kitsune-modern"
SETTINGS="${VSCODIUM_USER_SETTINGS:-$HOME/.vscode-oss/User/settings.json}"

mkdir -p "$EXT_DIR/themes" "$EXT_DIR/icons"
echo "→ installing to $EXT_DIR"

# --- manifest (color + icon themes) ---
cat > "$EXT_DIR/package.json" <<'EOF'
{
  "name": "kri-kitsune-modern",
  "displayName": "Kitsune Modern — KRI Brand Theme",
  "publisher": "kitsune-kits",
  "version": "0.2.0",
  "engines": { "vscode": "^1.70.0" },
  "categories": ["Themes"],
  "contributes": {
    "themes": [
      { "label": "Kitsune Modern (Foxfire)", "uiTheme": "vs", "path": "./themes/kitsune-modern.json" },
      { "label": "Kitsune Modern (Sumi)", "uiTheme": "vs-dark", "path": "./themes/kitsune-modern-dark.json" }
    ],
    "iconThemes": [
      { "id": "kri-kitsune-modern", "label": "Kitsune Modern Icons", "path": "./icon-theme.json" }
    ]
  }
}
EOF

# --- themes (from repo files, with embedded fallback) ---
if [ -f "$SCRIPT_DIR/../../themes/kitsune-modern.json" ]; then
  echo "→ copying theme JSONs from repo checkout"
  cp "$SCRIPT_DIR/../../themes/kitsune-modern.json" "$EXT_DIR/themes/"
  cp "$SCRIPT_DIR/../../themes/kitsune-modern-dark.json" "$EXT_DIR/themes/"
fi

# --- icon theme ---
cp "$SCRIPT_DIR/icon-theme.json" "$EXT_DIR/"
cp "$SCRIPT_DIR/icons/"*.svg "$EXT_DIR/icons/"
echo "→ icon theme installed"

# --- settings.json merge (typography + terminal + Ma + icon theme) ---
BRAND_SETTINGS='{
  "editor.fontFamily": "'\''JetBrains Mono'\'', '\''SF Mono'\'', Menlo, monospace",
  "editor.fontLigatures": true,
  "editor.fontSize": 13,
  "editor.lineHeight": 1.6,
  "workbench.fontFamily": "'\''Inter'\'', '\''SF Pro Text'\'', system-ui, sans-serif",
  "markdown.preview.fontFamily": "'\''Inter'\'', '\''SF Pro Text'\'', system-ui, sans-serif",
  "markdown.preview.fontSize": 16,
  "terminal.integrated.fontFamily": "'\''JetBrains Mono'\'', '\''SF Mono'\'', monospace",
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.cursorBlinking": true,
  "editor.rulers": [100],
  "editor.guides.bracketPairs": true,
  "editor.minimap.enabled": false,
  "workbench.editor.enablePreview": false,
  "editor.cursorSmoothCaretAnimation": "on",
  "editor.smoothScrolling": true,
  "workbench.tree.indent": 16,
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "editor.formatOnSave": true,
  "window.autoDetectColorScheme": false,
  "workbench.colorTheme": "Kitsune Modern (Foxfire)",
  "workbench.iconTheme": "kri-kitsune-modern",
  "workbench.colorCustomizations": {
    "terminal.ansiBlack": "#0E1113", "terminal.ansiRed": "#D0342C",
    "terminal.ansiGreen": "#0FA898", "terminal.ansiYellow": "#C9A227",
    "terminal.ansiBlue": "#0E1113", "terminal.ansiMagenta": "#C9A227",
    "terminal.ansiCyan": "#0FA898", "terminal.ansiWhite": "#F4F7F8",
    "terminal.ansiBrightBlack": "#0E1113", "terminal.ansiBrightRed": "#D0342C",
    "terminal.ansiBrightGreen": "#0FA898", "terminal.ansiBrightYellow": "#C9A227",
    "terminal.ansiBrightBlue": "#0E1113", "terminal.ansiBrightMagenta": "#C9A227",
    "terminal.ansiBrightCyan": "#0FA898", "terminal.ansiBrightWhite": "#F4F7F8"
  }
}'

if command -v jq >/dev/null 2>&1; then
  echo "→ merging brand settings into $SETTINGS"
  mkdir -p "$(dirname "$SETTINGS")"
  if [ -f "$SETTINGS" ]; then
    cp "$SETTINGS" "$SETTINGS.backup-kri"
    jq -s '.[0] * .[1]' "$SETTINGS" <(echo "$BRAND_SETTINGS") > "$SETTINGS.tmp" \
      && mv "$SETTINGS.tmp" "$SETTINGS" || { echo "⚠ merge failed — backup at $SETTINGS.backup-kri"; }
  else
    echo "$BRAND_SETTINGS" | jq '.' > "$SETTINGS"
  fi
else
  echo "⚠ jq not found — themes installed, but merge settings.json manually (backup untouched)."
  echo "  brew install jq && re-run to merge automatically."
fi

echo ""
echo "✅ done. restart VSCodium, then: ⌘K ⌘T → 'Kitsune Modern (Foxfire)' — icons: 'Kitsune Modern Icons'."
