#!/usr/bin/env bash
# new-day.sh — create today's inbox + daily-brief files in your PRIVATE instance.
#
# Your instance lives under ./instance (gitignored). This script never writes
# anything tracked by the public repo.
#
#   ./scripts/new-day.sh            # uses today's date
#   ./scripts/new-day.sh 2026-06-25 # explicit date
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

date_str="${1:-$(date +%F)}"
inst="instance"

mkdir -p "$inst/inbox" "$inst/today" "$inst/decisions"

inbox="$inst/inbox/$date_str.md"
brief="$inst/today/$date_str.md"

if [ ! -f "$inbox" ]; then
  sed "s/<YYYY-MM-DD>/$date_str/" templates/inbox.template.md > "$inbox"
  echo "created $inbox"
else
  echo "exists  $inbox"
fi

if [ ! -f "$brief" ]; then
  sed "s/<YYYY-MM-DD>/$date_str/" templates/daily-brief.template.md > "$brief"
  echo "created $brief"
else
  echo "exists  $brief"
fi

echo "Ready. Capture into $inbox, then run the Chief of Staff prompt over it."
