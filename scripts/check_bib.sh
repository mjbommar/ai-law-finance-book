#!/usr/bin/env bash
set -Eeuo pipefail
DIR=${1:-.}
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/lib.sh"

info "BibTeX/BibLaTeX checks in $DIR"
STATUS=0

bibs=$(find_files "$DIR" "**/*.bib")
if [[ -z "$bibs" ]]; then
  warn "No .bib files found"
else
  if have biber; then
    info "Running biber --tool (validation)"
    while IFS= read -r f; do
      biber --tool --validate-datamodel "$f" >/dev/null || STATUS=$?
    done <<< "$bibs"
  else
    warn "biber not installed — skipping validation"
  fi

  if have bibtex-tidy; then
    info "Running bibtex-tidy --dry"
    while IFS= read -r f; do
      bibtex-tidy --quiet --dry "$f" || STATUS=$?
    done <<< "$bibs"
  else
    warn "bibtex-tidy not installed — skipping formatting check"
  fi
fi

exit_nonzero_if_any_failed "$STATUS"

