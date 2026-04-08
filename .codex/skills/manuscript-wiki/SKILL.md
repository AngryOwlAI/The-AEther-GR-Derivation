# Manuscript Wiki

Use this skill when a task benefits from the local Obsidian Manuscript Wiki as a retrieval and navigation layer.

Typical triggers:

- locating a manuscript quickly by routing status, family, or line
- checking the current frontier note against the generated routing pages
- using copied local PDFs for page-level verification or PDF++ links
- regenerating or linting the local wiki after manuscript builds

## Authority Order

The wiki is not a second scientific source of truth. Use this order:

1. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`
3. the relevant wiki routing index under `.local/obsidian/aether-manuscripts-wiki/03_indexes/`
4. the relevant manuscript source note under `.local/obsidian/aether-manuscripts-wiki/02_sources/manuscripts/`
5. the copied local PDF under `.local/obsidian/aether-manuscripts-wiki/01_raw/project_pdfs/` if page-specific detail or PDF++ context is needed
6. the active `.tex` manuscript for scientific authority

If the local vault does not exist yet, fall back to the repository files and the tracked scripts:

- `scripts/init_manuscript_wiki.py`
- `scripts/sync_manuscript_wiki_pdfs.py`
- `scripts/generate_manuscript_wiki_notes.py`
- `scripts/lint_manuscript_wiki.py`

## Core Rules

- Treat the wiki as a compiled retrieval surface, not as the canonical scientific record.
- Use the file map and the guide before naming the current main line, current frontier, or next honest benchmark-facing burden.
- Use generated routing pages rather than stale prose summaries when routing is at issue.
- Do not use a wiki source note or copied PDF as authoritative if its hash or sync metadata no longer matches the current sync manifest.
- Do not promote `historical_but_kept_active`, `screened_out`, or `side_work` material from backlinks alone.
- Do not let wiki summaries overrule the active `.tex` language.
- Verify substantive scientific claims in the active `.tex`, not only in the copied PDF or source note.

## Working Procedure

1. Read the relevant row in `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`.
2. Confirm the routing meaning in `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`.
3. Open the generated routing index for the target `frontline_status`, `project_role`, or `line_name`.
4. Open the manuscript source note to gather links, summary metadata, and local PDF paths.
5. Open the copied local PDF only when page-level verification or annotation context is needed.
6. Open the active `.tex` before making any scientific statement or repository-state claim.

## Output Rules

When the wiki is used in an answer:

- say whether the result came from routing metadata, a generated note, a copied PDF, or the active `.tex`
- keep routing claims anchored to the file map
- keep scientific claims anchored to the active `.tex`
- mention a sync mismatch or stale-note condition if one was detected

## Safety Checks

Before trusting the wiki after manuscript changes:

1. run `python3 scripts/sync_manuscript_wiki_pdfs.py --changed`
2. run `python3 scripts/generate_manuscript_wiki_notes.py`
3. run `python3 scripts/lint_manuscript_wiki.py`

If the lint step fails, use the repository files directly until the wiki is refreshed.
