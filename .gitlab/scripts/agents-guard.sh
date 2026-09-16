#!/bin/sh
# agents-guard.sh — context-rot guard, part of the KRI agent standard.
# Standard: https://gitlab.com/kitsune-kits/kri/-/blob/main/AGENTS.md
# Verifies the agent-guidance contract for this repo:
#   1. AGENTS.md, CLAUDE.md, PROJECT-STATUS.md exist
#   2. CLAUDE.md imports AGENTS.md
#   3. AGENTS.md links to the KRI org repo (except in the KRI repo itself)
#   4. PROJECT-STATUS.md is not stale (>30 days = warning)
# Non-blocking by design (allow_failure: true) — failures are signals, not gates.

set -u

FAIL=0

for f in AGENTS.md CLAUDE.md PROJECT-STATUS.md; do
  if [ -f "$f" ]; then
    echo "OK: $f present"
  else
    echo "FAIL: $f is missing"
    FAIL=1
  fi
done

if [ -f CLAUDE.md ] && ! grep -q '@AGENTS.md' CLAUDE.md; then
  echo "FAIL: CLAUDE.md does not import AGENTS.md (@AGENTS.md)"
  FAIL=1
fi

if [ "\${KRI_LINK_REQUIRED:-true}" = "true" ] && [ -f AGENTS.md ]; then
  if grep -q 'kitsune-kits/kri' AGENTS.md; then
    echo "OK: AGENTS.md links to the KRI org repo"
  else
    echo "FAIL: AGENTS.md does not link to kitsune-kits/kri"
    FAIL=1
  fi
fi

if [ -f PROJECT-STATUS.md ]; then
  updated=$(grep -m1 -o '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]' PROJECT-STATUS.md || true)
  if [ -z "$updated" ]; then
    echo "WARN: no date found in PROJECT-STATUS.md"
  else
    then=$(date -u -d "$updated" +%s 2>/dev/null || echo 0)
    if [ "$then" -gt 0 ]; then
      now=$(date +%s)
      age=$(( (now - then) / 86400 ))
      if [ "$age" -gt 30 ]; then
        echo "WARN: PROJECT-STATUS.md is \${age} days old (>30) — refresh it"
      else
        echo "OK: PROJECT-STATUS.md updated \${age} days ago"
      fi
    else
      echo "WARN: could not parse PROJECT-STATUS.md date ($updated)"
    fi
  fi
fi

exit $FAIL