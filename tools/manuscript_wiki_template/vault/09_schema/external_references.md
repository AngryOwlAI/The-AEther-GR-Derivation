# External References

Phase 6 keeps supplemental literature clearly separate from project-authored manuscripts.

Use these locations:

- `01_raw/references/external/` for copied external PDFs
- `02_sources/references/` for external-reference notes and the library page
- `07_logs/external_references_manifest.json` for machine-readable ingest state

Supported literature classes:

- `reference_paper`
- `benchmark_gr_reference`
- `methodological_paper`
- `project_adjacent_literature`

Operational rules:

1. External references are supplemental context only.
2. They must not appear in the generated routing indexes that are rebuilt from `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`.
3. They must not be used to overrule active `.tex` language or file-map routing.
4. Their notes should explain project relevance without pretending that the reference is part of the project-authored benchmark package.
5. Their copied PDFs should remain inside `01_raw/references/external/`, never inside `01_raw/project_pdfs/`.

Recommended command:

```bash
python3 scripts/add_manuscript_wiki_reference.py \
  --pdf /path/to/paper.pdf \
  --title "Reference Title" \
  --authors "A. Author; B. Author" \
  --year 2024 \
  --kind benchmark_gr_reference \
  --project-relevance "Why this paper matters here."
```
