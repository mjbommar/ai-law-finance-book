#!/usr/bin/env bash
set -Eeuo pipefail
DIR=${1:-chapters/agentic-primer}
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
. "$HERE/lib.sh"

info "LaTeX checks in $DIR"
STATUS=0
STRICT=${STRICT:-0}  # set to 1 to fail on lacheck/chktex warnings

tex_files=$(find_files "$DIR" "**/*.tex")
if [[ -z "$tex_files" ]]; then
  warn "No .tex files under $DIR"
else
  if have chktex; then
    info "Running chktex"
    # Typical ignores can be configured later via .chktexrc
    if ! chktex -q -n1 -n8 -n46 $tex_files; then
      [[ "$STRICT" = 1 ]] && STATUS=1 || warn "chktex reported issues (non-strict mode)"
    fi
  else
    warn "chktex not installed — skipping"
  fi

  if have lacheck; then
    info "Running lacheck"
    if [[ -f "$DIR/main.tex" ]]; then
      # run from chapter dir to resolve relative \input paths
      (cd "$DIR" && lacheck main.tex) || { [[ "$STRICT" = 1 ]] && STATUS=1 || warn "lacheck reported issues (non-strict mode)"; }
    else
      while IFS= read -r f; do
        (cd "$(dirname "$f")" && lacheck "$(basename "$f")") || { [[ "$STRICT" = 1 ]] && STATUS=1 || warn "lacheck issues in $f (non-strict)"; }
      done <<< "$tex_files"
    fi
  else
    warn "lacheck not installed — skipping"
  fi
fi

# If chapter has a Makefile, try lightweight validation
if [[ -f "$DIR/Makefile" ]]; then
  if have make; then
    info "Attempting chapter validation via make validate (non-fatal if toolchain missing)"
    make -C "$DIR" validate || STATUS=$?
  fi
fi

exit_nonzero_if_any_failed "$STATUS"
