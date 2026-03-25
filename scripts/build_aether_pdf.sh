#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  build_aether_pdf.sh [--all] [path/to/file.tex ...]

Builds repository LaTeX sources into the matching PDF folders:
  manuscripts/active/tex   -> manuscripts/active/pdf
  manuscripts/retired/tex  -> manuscripts/retired/pdf
  docs/assets/tex          -> docs/assets/pdfs

Options:
  --all       Build every .tex file in the supported source trees
  --help, -h  Show this help message

Notes:
  - Runs pdflatex twice for each target.
  - Deletes the matching .aux, .log, and .out files after a successful build.
  - Leaves temporary files in place if pdflatex fails, so the failure can be inspected.
EOF
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"

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

pdf_dir_for_tex() {
  local tex_path="$1"

  case "$tex_path" in
    "$repo_root"/manuscripts/active/tex/*)
      printf '%s\n' "$repo_root/manuscripts/active/pdf"
      ;;
    "$repo_root"/manuscripts/retired/tex/*)
      printf '%s\n' "$repo_root/manuscripts/retired/pdf"
      ;;
    "$repo_root"/docs/assets/tex/*)
      printf '%s\n' "$repo_root/docs/assets/pdfs"
      ;;
    *)
      return 1
      ;;
  esac
}

build_one() {
  local tex_path="$1"
  local pdf_dir base_name

  if [[ ! -f "$tex_path" ]]; then
    printf 'Missing .tex file: %s\n' "$tex_path" >&2
    exit 1
  fi

  if [[ "${tex_path##*.}" != "tex" ]]; then
    printf 'Expected a .tex file, got: %s\n' "$tex_path" >&2
    exit 1
  fi

  if ! pdf_dir="$(pdf_dir_for_tex "$tex_path")"; then
    cat >&2 <<EOF
Unsupported source location: $tex_path

Supported source trees:
  $repo_root/manuscripts/active/tex
  $repo_root/manuscripts/retired/tex
  $repo_root/docs/assets/tex
EOF
    exit 1
  fi

  mkdir -p "$pdf_dir"
  base_name="$(basename "${tex_path%.tex}")"

  printf 'Building %s\n' "$tex_path"
  printf '  -> %s/%s.pdf\n' "$pdf_dir" "$base_name"

  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="$pdf_dir" "$tex_path"
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="$pdf_dir" "$tex_path"

  rm -f \
    "$pdf_dir/$base_name.aux" \
    "$pdf_dir/$base_name.log" \
    "$pdf_dir/$base_name.out"

  printf 'Finished %s\n' "$pdf_dir/$base_name.pdf"
}

build_all=0
targets_file="$(mktemp)"
trap 'rm -f "$targets_file"' EXIT

while (($# > 0)); do
  case "$1" in
    --all)
      build_all=1
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    -*)
      printf 'Unknown option: %s\n\n' "$1" >&2
      usage >&2
      exit 1
      ;;
    *)
      printf '%s\n' "$(resolve_path "$1")" >> "$targets_file"
      shift
      ;;
  esac
done

if ((build_all)); then
  find \
    "$repo_root/manuscripts/active/tex" \
    "$repo_root/manuscripts/retired/tex" \
    "$repo_root/docs/assets/tex" \
    -type f -name '*.tex' -print >> "$targets_file"
fi

if [[ ! -s "$targets_file" ]]; then
  usage >&2
  exit 1
fi

while IFS= read -r tex_path; do
  [[ -n "$tex_path" ]] || continue
  build_one "$tex_path"
done < <(sort -u "$targets_file")
