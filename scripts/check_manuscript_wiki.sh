#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  check_manuscript_wiki.sh [--vault /abs/path]

Runs the Manuscript Wiki lint pass against the local vault.

Options:
  --vault      Override the vault path
  --help, -h   Show this help message

Notes:
  - Defaults to MANUSCRIPT_WIKI_VAULT if set.
  - Otherwise defaults to .local/obsidian/aether-manuscripts-wiki inside the repository.
EOF
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
vault="${MANUSCRIPT_WIKI_VAULT:-$repo_root/.local/obsidian/aether-manuscripts-wiki}"

resolve_path() {
  local input="$1"
  local path dir base

  if [[ "$input" = /* ]]; then
    path="$input"
  else
    path="$PWD/$input"
  fi

  dir="$(cd "$(dirname "$path")" && pwd)"
  base="$(basename "$path")"
  printf '%s/%s\n' "$dir" "$base"
}

while (($# > 0)); do
  case "$1" in
    --vault)
      if (($# < 2)); then
        printf 'Missing argument for --vault\n' >&2
        exit 1
      fi
      vault="$(resolve_path "$2")"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown option: %s\n\n' "$1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

python3 "$script_dir/lint_manuscript_wiki.py" --vault "$vault"
