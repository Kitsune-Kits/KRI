#!/usr/bin/env bash
set -euo pipefail

# git-identity.sh / KRI Git Identity / Abstract: sets the KRI persona
# (or architect) git identity on the *current repo only* — never global.
# Git deliberately ignores identity from repo-committed files, so this
# is a per-clone helper. Persona table per PERSONA-ATTRIBUTION.md.

usage() {
  echo "usage: git-identity.sh <architect|coco|zaku|piko|nui>"
  exit 1
}

[ $# -eq 1 ] || usage

case "$1" in
  architect) NAME="Nigel Bassett"; EMAIL="nigel@kitsunekits.com" ;;
  coco)  NAME="Coco Sensei"; EMAIL="coco@kitsune-kits.gitlab" ;;
  zaku)  NAME="Zaku";        EMAIL="zaku@kitsune-kits.gitlab" ;;
  piko)  NAME="Piko";        EMAIL="piko@kitsune-kits.gitlab" ;;
  nui)   NAME="Nui";         EMAIL="nui@kitsune-kits.gitlab" ;;
  *) usage ;;
esac

git config user.name  "$NAME"
git config user.email "$EMAIL"
echo "→ $(basename "$(git rev-parse --show-toplevel)") now commits as: $NAME <$EMAIL>"
