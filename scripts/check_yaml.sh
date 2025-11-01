#!/usr/bin/env bash
set -Eeuo pipefail
DIR=${1:-.}
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/lib.sh"

info "YAML checks in $DIR"
STATUS=0

if have yamllint; then
  files=$(find_files "$DIR" "**/*.{yml,yaml}")
  if [[ -n "$files" ]]; then
    info "Running yamllint"
    yamllint -s $files || STATUS=$?
  else
    warn "No YAML files found"
  fi
else
  warn "yamllint not installed — skipping"
fi

exit_nonzero_if_any_failed "$STATUS"

