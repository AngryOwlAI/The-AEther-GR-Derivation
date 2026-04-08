# Aether Manuscripts Wiki

This local vault is a retrieval and navigation layer for the manuscript corpus of `The Æther-Flow Interpretation of Relativity`.

Authority order:

1. active `.tex` manuscripts under `manuscripts/active/tex/`
2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv` plus its guide
3. built repository PDFs
4. generated vault notes and indexes

Use the tracked scripts from the repository root:

- `python3 scripts/init_manuscript_wiki.py --vault /path/to/this/vault`
- `python3 scripts/install_obsidian_pdf_plus.py --vault /path/to/this/vault --enable`
- `python3 scripts/sync_manuscript_wiki_pdfs.py --all --vault /path/to/this/vault`
- `python3 scripts/generate_manuscript_wiki_notes.py --vault /path/to/this/vault`
- `python3 scripts/add_manuscript_wiki_reference.py --rebuild-index-only --vault /path/to/this/vault`
- `python3 scripts/lint_manuscript_wiki.py --vault /path/to/this/vault`

This vault should remain local and ignored by git.
