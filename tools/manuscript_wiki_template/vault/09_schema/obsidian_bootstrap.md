# Obsidian Bootstrap

Phase 2 bootstrap order:

1. Run `python3 scripts/init_manuscript_wiki.py --vault /path/to/vault`.
2. Run `python3 scripts/install_obsidian_pdf_plus.py --vault /path/to/vault --enable`.
3. Open the vault in Obsidian.
4. Confirm the seeded core plugins are enabled:
   - Backlinks
   - Outline
   - Search
   - Page Preview
   - Graph View
   - Templates
5. Confirm the seeded `Files & Links` behavior:
   - Wikilinks enabled
   - internal links auto-update
   - attachments stored under `01_raw/attachments`
   - unsupported file extensions visible when useful

`PDF++` is the required community plugin for page-level links, backlink highlighting, and PDF-native deep-link workflows. The plugin runtime files stay local under `.obsidian/plugins/pdf-plus/` and should remain ignored by git.

If the plugin install is refreshed later, rerun the installer helper with `--force`.
