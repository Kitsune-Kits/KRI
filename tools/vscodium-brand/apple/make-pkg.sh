#!/usr/bin/env bash
set -euo pipefail

# make-pkg.sh / KRI VSCodium macOS Package / Abstract: builds a
# distribution-style .pkg for MDM deployment: VSCodium.app + the whole
# vscodium-brand forge (setup.sh, extensions, snippets, icons, themes)
# at /usr/local/kri/vscodium-brand, plus a postinstall that runs the
# forge setup as the console user. Build on macOS (pkgbuild required).
# v0.1.0

VSCODIUM_VERSION="${1:?usage: make-pkg.sh <vscodium-release-tag> e.g. 1.96.2.24356>"
ARCH="${2:-universal}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BRAND_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORK="$(mktemp -d)"
PKGROOT="$WORK/root"
trap 'rm -rf "$WORK"' EXIT

echo "→ fetching VSCodium $VSCODIUM_VERSION ($ARCH)"
case "$ARCH" in
  universal) ZIP="VSCodium-darwin-universal.zip" ;;
  arm64)     ZIP="VSCodium-darwin-arm64.zip" ;;
  x64)       ZIP="VSCodium-darwin-x64.zip" ;;
  *) echo "⚠ arch must be universal|arm64|x64"; exit 1 ;;
esac
curl -fsSL -o "$WORK/vsc.zip" \
  "https://github.com/VSCodium/vscodium/releases/download/$VSCODIUM_VERSION/$ZIP"

echo "→ assembling payload"
mkdir -p "$PKGROOT/Applications" "$PKGROOT/usr/local/kri"
ditto -x -k "$WORK/vsc.zip" "$WORK/extracted"
APP="$(find "$WORK/extracted" -maxdepth 1 -name '*.app')"
ditto "$APP" "$PKGROOT/Applications/VSCodium.app"
cp -R "$BRAND_DIR" "$PKGROOT/usr/local/kri/vscodium-brand"

echo "→ staging postinstall"
mkdir -p "$WORK/scripts"
cp "$SCRIPT_DIR/postinstall" "$WORK/scripts/postinstall"
chmod +x "$WORK/scripts/postinstall"

OUT="KRI-VSCodium-$VSCODIUM_VERSION.pkg"
echo "→ building $OUT"
pkgbuild \
  --identifier com.kitsunekits.kri.vscodium \
  --version "${VSCODIUM_VERSION//./}" \
  --root "$PKGROOT" \
  --scripts "$WORK/scripts" \
  "$OUT"

echo ""
echo "✅ $OUT built (unsigned). For MDM deployment, sign with your"
echo "   Developer ID Installer certificate via productbuild, e.g.:"
echo "   productbuild --package $OUT --sign \"Developer ID Installer: KITSUNE KITS\" KRI-VSCodium-signed.pkg"
