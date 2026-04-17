#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  build_aether_pdf.sh [--all] [--missing] [--stale] [--sync-wiki|--no-sync-wiki] [--wiki-vault /abs/path] [path/to/file.tex ...]

Builds repository LaTeX sources into the matching PDF folders:
  manuscripts/active/tex   -> manuscripts/active/pdf
  manuscripts/retired/tex  -> manuscripts/retired/pdf
  docs/assets/tex          -> docs/assets/pdfs

Options:
  --all            Build every .tex file in the supported source trees
  --missing        Build every supported .tex file whose matching .pdf does not exist
  --stale          Build every supported .tex file whose matching .pdf is missing or older
  --sync-wiki      Force wiki sync after successful builds
  --no-sync-wiki   Skip wiki sync even if the local vault exists
  --wiki-vault     Override the vault path used for wiki sync and lint
  --lint-wiki      Run the Manuscript Wiki lint pass after a successful wiki sync
  --help, -h       Show this help message

Notes:
  - Runs pdflatex three times for each target to settle cross-references from a clean build.
  - Deletes the matching .aux, .log, and .out files after a successful build.
  - Leaves temporary files in place if pdflatex fails, so the failure can be inspected.
  - After building any file under manuscripts/active/tex, validates docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv.
  - If a local vault exists at .local/obsidian/aether-manuscripts-wiki, active-build sync runs automatically unless --no-sync-wiki is passed.
  - MANUSCRIPT_WIKI_VAULT can override the default vault path.
EOF
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
default_wiki_vault="$repo_root/.local/obsidian/aether-manuscripts-wiki"
wiki_vault="${MANUSCRIPT_WIKI_VAULT:-$default_wiki_vault}"

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

pdf_path_for_tex() {
  local tex_path="$1"
  local pdf_dir base_name

  pdf_dir="$(pdf_dir_for_tex "$tex_path")"
  base_name="$(basename "${tex_path%.tex}")"
  printf '%s/%s.pdf\n' "$pdf_dir" "$base_name"
}

validate_active_file_map() {
  local validator="$script_dir/validate_active_manuscript_file_map.py"

  if [[ ! -f "$validator" ]]; then
    printf 'Missing validator script: %s\n' "$validator" >&2
    exit 1
  fi

  printf 'Validating active manuscript file map\n'
  python3 "$validator"
}

ensure_wiki_script() {
  local script_path="$1"

  if [[ ! -f "$script_path" ]]; then
    printf 'Missing Manuscript Wiki helper: %s\n' "$script_path" >&2
    exit 1
  fi
}

append_wiki_log() {
  local built_count="$1"
  local active_count="$2"
  local note_refresh="$3"
  local lint_result="$4"
  local target_list="$5"
  local log_dir="$wiki_vault/07_logs"
  local log_file="$log_dir/build_sync_events.tsv"

  mkdir -p "$log_dir"
  if [[ ! -f "$log_file" ]]; then
    printf 'timestamp_utc\tbuilt_targets\tactive_targets\tnote_refresh\tlint_result\ttargets\n' > "$log_file"
  fi

  printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    "$built_count" \
    "$active_count" \
    "$note_refresh" \
    "$lint_result" \
    "$target_list" >> "$log_file"
}

should_sync_wiki() {
  case "$wiki_sync_mode" in
    force)
      return 0
      ;;
    skip)
      return 1
      ;;
    auto)
      [[ -d "$wiki_vault" ]]
      ;;
    *)
      return 1
      ;;
  esac
}

sync_manuscript_wiki() {
  local sync_script="$script_dir/sync_manuscript_wiki_pdfs.py"
  local generate_script="$script_dir/generate_manuscript_wiki_notes.py"
  local check_script="$script_dir/check_manuscript_wiki.sh"
  local built_count active_count note_refresh lint_result targets_csv tex_path pdf_path

  if [[ ! -s "$built_tex_targets_file" ]]; then
    return 0
  fi

  if ! should_sync_wiki; then
    if [[ "$wiki_sync_mode" == "skip" ]]; then
      printf 'Skipping Manuscript Wiki sync by request\n'
    else
      printf 'Skipping Manuscript Wiki sync: vault not found at %s\n' "$wiki_vault"
    fi
    return 0
  fi

  if [[ ! -d "$wiki_vault" ]]; then
    printf 'Manuscript Wiki vault does not exist: %s\n' "$wiki_vault" >&2
    exit 1
  fi

  ensure_wiki_script "$sync_script"
  ensure_wiki_script "$generate_script"

  printf 'Syncing built PDFs into Manuscript Wiki at %s\n' "$wiki_vault"
  while IFS= read -r tex_path; do
    [[ -n "$tex_path" ]] || continue
    pdf_path="$(pdf_path_for_tex "$tex_path")"
    python3 "$sync_script" --one "$pdf_path" --vault "$wiki_vault"
  done < <(sort -u "$built_tex_targets_file")

  active_count=0
  if [[ -s "$built_active_targets_file" ]]; then
    active_count="$(sort -u "$built_active_targets_file" | wc -l | tr -d ' ')"
  fi

  note_refresh="none"
  if (( active_count == 1 )); then
    tex_path="$(sort -u "$built_active_targets_file")"
    printf 'Refreshing Manuscript Wiki note for %s\n' "$tex_path"
    python3 "$generate_script" --one "$tex_path" --vault "$wiki_vault"
    note_refresh="single"
  elif (( active_count > 1 )); then
    printf 'Refreshing full Manuscript Wiki navigation layer\n'
    python3 "$generate_script" --vault "$wiki_vault"
    note_refresh="full"
  fi

  lint_result="skipped"
  if (( wiki_lint_after_sync )); then
    if [[ -f "$check_script" ]]; then
      printf 'Running Manuscript Wiki lint\n'
      MANUSCRIPT_WIKI_VAULT="$wiki_vault" "$check_script"
    else
      ensure_wiki_script "$script_dir/lint_manuscript_wiki.py"
      printf 'Running Manuscript Wiki lint\n'
      python3 "$script_dir/lint_manuscript_wiki.py" --vault "$wiki_vault"
    fi
    lint_result="passed"
  fi

  built_count="$(sort -u "$built_tex_targets_file" | wc -l | tr -d ' ')"
  targets_csv="$(sort -u "$built_tex_targets_file" | sed "s#^$repo_root/##" | paste -sd';' -)"
  append_wiki_log "$built_count" "$active_count" "$note_refresh" "$lint_result" "$targets_csv"
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

  TEXINPUTS="$repo_root:${TEXINPUTS:-}" \
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="$pdf_dir" "$tex_path"
  TEXINPUTS="$repo_root:${TEXINPUTS:-}" \
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="$pdf_dir" "$tex_path"
  TEXINPUTS="$repo_root:${TEXINPUTS:-}" \
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="$pdf_dir" "$tex_path"

  rm -f \
    "$pdf_dir/$base_name.aux" \
    "$pdf_dir/$base_name.log" \
    "$pdf_dir/$base_name.out"

  printf '%s\n' "$tex_path" >> "$built_tex_targets_file"
  if [[ "$tex_path" == "$repo_root"/manuscripts/active/tex/* ]]; then
    built_active_manuscript=1
    printf '%s\n' "$tex_path" >> "$built_active_targets_file"
  fi

  printf 'Finished %s\n' "$pdf_dir/$base_name.pdf"
}

build_all=0
build_missing=0
build_stale=0
built_active_manuscript=0
wiki_sync_mode="auto"
wiki_lint_after_sync=0
targets_file="$(mktemp)"
built_tex_targets_file="$(mktemp)"
built_active_targets_file="$(mktemp)"
trap 'rm -f "$targets_file" "$built_tex_targets_file" "$built_active_targets_file"' EXIT

append_supported_tree_targets() {
  find \
    "$repo_root/manuscripts/active/tex" \
    "$repo_root/manuscripts/retired/tex" \
    "$repo_root/docs/assets/tex" \
    -type f -name '*.tex' -print
}

append_missing_targets() {
  local tex_path pdf_path

  while IFS= read -r tex_path; do
    [[ -n "$tex_path" ]] || continue
    pdf_path="$(pdf_path_for_tex "$tex_path")"
    if [[ ! -f "$pdf_path" ]]; then
      printf '%s\n' "$tex_path"
    fi
  done < <(append_supported_tree_targets)
}

append_stale_targets() {
  local tex_path pdf_path

  while IFS= read -r tex_path; do
    [[ -n "$tex_path" ]] || continue
    pdf_path="$(pdf_path_for_tex "$tex_path")"
    if [[ ! -f "$pdf_path" || "$tex_path" -nt "$pdf_path" ]]; then
      printf '%s\n' "$tex_path"
    fi
  done < <(append_supported_tree_targets)
}

while (($# > 0)); do
  case "$1" in
    --all)
      build_all=1
      shift
      ;;
    --missing)
      build_missing=1
      shift
      ;;
    --stale)
      build_stale=1
      shift
      ;;
    --sync-wiki)
      wiki_sync_mode="force"
      shift
      ;;
    --no-sync-wiki)
      wiki_sync_mode="skip"
      shift
      ;;
    --wiki-vault)
      if (($# < 2)); then
        printf 'Missing argument for --wiki-vault\n' >&2
        exit 1
      fi
      wiki_vault="$(resolve_path "$2")"
      shift 2
      ;;
    --lint-wiki)
      wiki_lint_after_sync=1
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
  append_supported_tree_targets >> "$targets_file"
fi

if ((build_missing)); then
  append_missing_targets >> "$targets_file"
fi

if ((build_stale)); then
  append_stale_targets >> "$targets_file"
fi

if [[ ! -s "$targets_file" ]]; then
  usage >&2
  exit 1
fi

while IFS= read -r tex_path; do
  [[ -n "$tex_path" ]] || continue
  build_one "$tex_path"
done < <(sort -u "$targets_file")

if ((built_active_manuscript)); then
  validate_active_file_map
fi

sync_manuscript_wiki
