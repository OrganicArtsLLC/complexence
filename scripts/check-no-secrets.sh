#!/usr/bin/env bash
# check-no-secrets.sh — pre-commit guard for a PUBLIC repo.
#
# Scans staged changes for (a) common personal-data / secret patterns and
# (b) any terms listed in a local, gitignored `.private-denylist`.
# Exits non-zero if anything matches, so it can be wired as a pre-commit hook:
#
#   ln -s ../../scripts/check-no-secrets.sh .git/hooks/pre-commit
#
# Or run it manually before committing. Portable to the bash 3.2 that ships
# with macOS (no mapfile, no associative arrays).
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

staged="$(git diff --cached --name-only --diff-filter=ACM || true)"
if [ -z "$staged" ]; then
  echo "check-no-secrets: nothing staged."
  exit 0
fi

# Generic high-signal patterns, one per line as "label|regex".
# Conservative on purpose, to limit false positives.
patterns='email|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
phone|(\+?[0-9]{1,2}[ .-]?)?\(?[0-9]{3}\)?[ .-][0-9]{3}[ .-][0-9]{4}
aws-key|AKIA[0-9A-Z]{16}
private-key|-----BEGIN [A-Z ]*PRIVATE KEY-----
secret-assign|(authorization|bearer|api[_-]?key|secret|token)["'"'"' :=]+[A-Za-z0-9._-]{16,}
private-marker|(CONFIDENTIAL|DO[ _-]?NOT[ _-]?COMMIT|PRIVATE[ _-]ONLY|@private)'

findings="$(mktemp)"
trap 'rm -f "$findings"' EXIT

printf '%s\n' "$staged" | while IFS= read -r f; do
  [ -n "$f" ] || continue
  [ -f "$f" ] || continue
  added="$(git diff --cached -U0 -- "$f" | grep '^+' | grep -v '^+++' || true)"
  [ -n "$added" ] || continue

  printf '%s\n' "$patterns" | while IFS='|' read -r label regex; do
    [ -n "$label" ] || continue
    printf '%s\n' "$added" \
      | grep -niE "$regex" 2>/dev/null \
      | sed "s|^|  [$label] $f: |" >> "$findings" || true
  done

  if [ -f .private-denylist ]; then
    while IFS= read -r term; do
      [ -n "$term" ] || continue
      case "$term" in \#*) continue ;; esac
      printf '%s\n' "$added" \
        | grep -niF "$term" 2>/dev/null \
        | sed "s|^|  [denylist:$term] $f: |" >> "$findings" || true
    done < .private-denylist
  fi
done

count="$(grep -c . "$findings" 2>/dev/null || true)"
count="${count:-0}"
if [ "$count" -gt 0 ]; then
  echo "check-no-secrets: $count potential issue(s) in staged changes:"
  cut -c1-140 "$findings"
  echo ""
  echo "Review GUARDRAILS.md. If a hit is a false positive, edit/unstage it, or"
  echo "commit with --no-verify only after confirming it is safe."
  exit 1
fi

echo "check-no-secrets: clean."
