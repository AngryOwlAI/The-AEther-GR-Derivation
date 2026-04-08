# Workflow

Recommended workflow:

1. Build or refresh repository PDFs.
2. Sync copied PDFs into the local vault.
3. Regenerate manuscript notes, indexes, line pages, and concept seeds.
4. Run the wiki lint pass.
5. Use the wiki for retrieval, then verify substantive claims in the active `.tex`.

When the local vault already exists, the supported day-to-day shortcut is:

- `scripts/build_aether_pdf.sh --sync-wiki path/to/file.tex`
- `scripts/check_manuscript_wiki.sh`

For supplemental literature expansion:

- `python3 scripts/add_manuscript_wiki_reference.py --pdf /path/to/paper.pdf --title "Reference Title" ...`
- keep those PDFs and notes under the dedicated external-reference locations
- do not treat external-reference notes as routing authority

Do not treat the vault as authoritative when sync metadata is stale or missing.
