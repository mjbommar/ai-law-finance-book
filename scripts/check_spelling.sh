#!/usr/bin/env bash
set -Eeuo pipefail
DIR=${1:-.}
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/lib.sh"

info "Spelling checks in $DIR"
STATUS=0

# codespell for common typos
if have codespell; then
  info "Running codespell"
  codespell -q 3 -S ".git,node_modules,auto,dist,build,.venv" "$DIR" || STATUS=$?
else
  warn "codespell not installed — skipping"
fi

# cspell for code-aware spell checking
if have cspell; then
  files=$(find_files "$DIR" "**/*.{md,tex,texi,bib,py,js,ts,json,yml,yaml}")
  if [[ -n "$files" ]]; then
    info "Running cspell"
    cspell --no-progress --show-suggestions $files || STATUS=$?
  fi
else
  warn "cspell not installed — skipping"
fi

exit_nonzero_if_any_failed "$STATUS"

