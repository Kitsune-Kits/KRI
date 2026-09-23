#!/usr/bin/env bash
# populate-wiki.sh — populate this project GitLab wiki from .gitlab/wiki/
#
# The GitLab API/connector cannot write wiki pages, so run this once from a
# machine with push access to gitlab.com (SSH key or HTTPS + token):
#
#   bash .gitlab/scripts/populate-wiki.sh
#
# Safe to re-run — it overwrites wiki pages with the committed content.
set -euo pipefail

PROJECT="kitsune-kits/kri"
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../wiki"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

[ -d "$SRC" ] || { echo "No .gitlab/wiki/ directory found." >&2; exit 1; }
[ -n "$(ls "$SRC"/*.md 2>/dev/null)" ] || { echo "No wiki .md files found." >&2; exit 1; }

echo "Cloning wiki for $PROJECT ..."
git clone -q "git@gitlab.com:${PROJECT}.wiki.git" "$TMP/wiki"
# HTTPS alternative: git clone "https://gitlab.com/${PROJECT}.wiki.git" "$TMP/wiki"

cp "$SRC"/*.md "$TMP/wiki/"
git -C "$TMP/wiki" add -A
git -C "$TMP/wiki" commit -q -m "docs(wiki): populate wiki from .gitlab/wiki/" || true
# Newer wikis default to main; older ones to master. Push whichever takes.
git -C "$TMP/wiki" push -q origin HEAD:main 2>/dev/null || git -C "$TMP/wiki" push -q origin HEAD:master

echo "Wiki populated: https://gitlab.com/${PROJECT}/-/wikis"
