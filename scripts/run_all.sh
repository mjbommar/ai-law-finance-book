#!/usr/bin/env bash
set -Eeuo pipefail
ROOT=${1:-.}
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/lib.sh"

info "Running repository checks in $ROOT"

"$HERE/check_markdown.sh" "$ROOT"
"$HERE/check_spelling.sh" "$ROOT"
"$HERE/check_yaml.sh" "$ROOT"
"$HERE/check_links.sh" "$ROOT"
"$HERE/check_bib.sh" "$ROOT"

ok "Repo checks complete"

