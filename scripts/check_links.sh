#!/usr/bin/env bash
set -Eeuo pipefail
DIR=${1:-.}
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/lib.sh"

info "Link checks in $DIR"
STATUS=0

if have lychee; then
  files_md=$(find_files "$DIR" "**/*.md")
  files_tex=$(find_files "$DIR" "**/*.tex")
  if [[ -n "$files_md$files_tex" ]]; then
    info "Running lychee (Markdown + LaTeX)"
    lychee --no-progress --max-redirects 4 --retry-wait-time 2 --retry-count 2 \
      $files_md $files_tex || STATUS=$?
  else
    warn "No Markdown/LaTeX files found"
  fi
else
  warn "lychee not installed — skipping"
fi

exit_nonzero_if_any_failed "$STATUS"

