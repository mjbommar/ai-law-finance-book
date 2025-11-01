#!/usr/bin/env bash
set -Eeuo pipefail

# Colors
if [[ -t 1 ]]; then
  RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[0;33m'; BLUE='\033[0;34m'; CYAN='\033[0;36m'; BOLD='\033[1m'; RESET='\033[0m'
else
  RED=''; GREEN=''; YELLOW=''; BLUE=''; CYAN=''; BOLD=''; RESET=''
fi

log() { printf "%b\n" "$*"; }
info() { log "${CYAN}${BOLD}➜${RESET} $*"; }
ok()   { log "${GREEN}✓${RESET} $*"; }
warn() { log "${YELLOW}!${RESET} $*"; }
err()  { log "${RED}✗${RESET} $*"; }

have() { command -v "$1" >/dev/null 2>&1; }

# find files by glob while excluding common dirs
find_files() {
  local root="$1"; shift
  local pattern="$1"; shift || true
  rg -uu --glob "${pattern}" \
     --hidden --no-messages \
     --glob '!**/.git/**' \
     --glob '!**/node_modules/**' \
     --glob '!**/auto/**' \
     --glob '!**/build/**' \
     --glob '!**/dist/**' \
     --glob '!**/.venv/**' \
     --files "$root" || true
}

exit_nonzero_if_any_failed() {
  local status="$1"
  if [[ "$status" -ne 0 ]]; then
    err "One or more checks failed"
    exit "$status"
  else
    ok "All checks passed or were skipped"
  fi
}

