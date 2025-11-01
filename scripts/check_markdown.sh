#!/usr/bin/env bash
set -Eeuo pipefail
DIR=${1:-.}
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/lib.sh"

info "Markdown checks in $DIR"

STATUS=0

# markdownlint (Node) if present
if have markdownlint || have markdownlint-cli2; then
  files=$(find_files "$DIR" "**/*.md")
  if [[ -n "$files" ]]; then
    info "Running markdownlint"
    if have markdownlint-cli2; then
      markdownlint-cli2 $files || STATUS=$?
    else
      markdownlint -c .markdownlint.jsonc $files || STATUS=$?
    fi
  else
    warn "No Markdown files found"
  fi
else
  warn "markdownlint not installed — skipping"
fi

# Vale (prose style)
if have vale; then
  files=$(find_files "$DIR" "**/*.md")
  if [[ -n "$files" ]]; then
    info "Running Vale"
    vale --no-exit $files || STATUS=$?
  fi
else
  warn "Vale not installed — skipping"
fi

# alex (inclusive language)
if have alex; then
  files=$(find_files "$DIR" "**/*.md")
  if [[ -n "$files" ]]; then
    info "Running alex"
    alex $files || STATUS=$?
  fi
else
  warn "alex not installed — skipping"
fi

exit_nonzero_if_any_failed "$STATUS"

