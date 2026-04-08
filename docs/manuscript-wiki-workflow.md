# Manuscript Wiki Workflow

This document is the compact user-facing workflow for the local Obsidian Manuscript Wiki.

The wiki is a retrieval and navigation layer, not the scientific source of truth. Authority remains:

1. active `.tex` under `manuscripts/active/tex/`
2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv` and its guide
3. built repository PDFs
4. generated wiki notes and indexes

## Default Vault

The default local vault path is:

- `.local/obsidian/aether-manuscripts-wiki/`

Override it when needed with either:

- `MANUSCRIPT_WIKI_VAULT=/abs/path/to/vault`
- `scripts/build_aether_pdf.sh --wiki-vault /abs/path/to/vault ...`
- `scripts/check_manuscript_wiki.sh --vault /abs/path/to/vault`

## Day-To-Day Commands

Build one active manuscript and refresh the local wiki automatically if the vault exists:

```bash
scripts/build_aether_pdf.sh manuscripts/active/tex/aether_flow_exact_closure_note.tex
```

Force wiki sync after a build:

```bash
scripts/build_aether_pdf.sh --sync-wiki manuscripts/active/tex/aether_flow_exact_closure_note.tex
```

Skip wiki sync for one build:

```bash
scripts/build_aether_pdf.sh --no-sync-wiki manuscripts/active/tex/aether_flow_exact_closure_note.tex
```

Build and lint in one pass:

```bash
scripts/build_aether_pdf.sh --sync-wiki --lint-wiki manuscripts/active/tex/aether_flow_exact_closure_note.tex
```

Run the standalone wiki lint command:

```bash
scripts/check_manuscript_wiki.sh
```

Refresh the full wiki manually after wider repo changes:

```bash
python3 scripts/sync_manuscript_wiki_pdfs.py --changed
python3 scripts/generate_manuscript_wiki_notes.py
scripts/check_manuscript_wiki.sh
```

Add one supplemental external reference PDF:

```bash
python3 scripts/add_manuscript_wiki_reference.py \
  --pdf /path/to/paper.pdf \
  --title "Reference Title" \
  --authors "A. Author; B. Author" \
  --year 2024 \
  --kind benchmark_gr_reference \
  --project-relevance "Why this paper matters here."
```

## Integrated Build Behavior

After a successful active-manuscript build, the integrated workflow now does the following:

1. rebuild the PDF
2. validate `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
3. sync the built PDF into the vault
4. refresh the matching manuscript note if exactly one active manuscript was built, or regenerate the full navigation layer if multiple active manuscripts were built
5. optionally lint the wiki if `--lint-wiki` was requested
6. append a local run record to `07_logs/build_sync_events.tsv` inside the vault

Retired and public-bundle PDF builds also sync their rebuilt PDFs into the vault, but note generation remains driven by the active manuscript file map.

## External Literature Expansion

Phase 6 keeps outside literature separate from project-authored manuscripts.

- External PDFs belong under `01_raw/references/external/`.
- External reference notes belong under `02_sources/references/`.
- The generated library page is `02_sources/references/external_reference_library.md`.
- External references are supplemental context only; they must not be used to set manuscript routing, benchmark status, or the current primary burden.

Use this command to refresh the external-reference library page without ingesting a new PDF:

```bash
python3 scripts/add_manuscript_wiki_reference.py --rebuild-index-only
```

## Agent Use

Agents should use the local wiki only as a compiled retrieval surface.

- Use `.codex/skills/manuscript-wiki/SKILL.md` for routing and verification order.
- Prefer `scripts/build_aether_pdf.sh --sync-wiki path/to/file.tex` after active manuscript edits.
- Use `scripts/check_manuscript_wiki.sh` before trusting the wiki after larger changes.
- Keep external-reference notes clearly separate from manuscript-routing answers.
