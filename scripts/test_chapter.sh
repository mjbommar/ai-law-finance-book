#!/usr/bin/env bash
set -Eeuo pipefail
CHAPTER=${1:-chapters/agentic-primer}
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/lib.sh"

info "Testing chapter: $CHAPTER"

if [[ ! -d "$CHAPTER" ]]; then
  err "Chapter directory not found: $CHAPTER"
  exit 1
fi

"$HERE/check_markdown.sh" "$CHAPTER"
"$HERE/check_spelling.sh" "$CHAPTER"
"$HERE/check_latex.sh" "$CHAPTER"
"$HERE/check_bib.sh" "$CHAPTER"
"$HERE/check_links.sh" "$CHAPTER"

ok "Chapter checks complete"

