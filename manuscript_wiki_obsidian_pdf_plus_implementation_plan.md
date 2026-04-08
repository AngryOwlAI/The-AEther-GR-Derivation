# Manuscript Wiki Implementation Plan

Date: 2026-04-08

## Purpose

This document records a detailed implementation plan for a local Manuscripts Wiki for `The Æther-Flow Interpretation of Relativity`, built around:

- Obsidian as the local knowledge workspace
- the PDF++ community plugin for PDF-native linking and annotation workflows
- the active manuscript `.tex` and `.pdf` corpus already maintained in this repository
- `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv` as the routing control layer
- agent-facing scripts and skills that allow Codex to use the wiki as a disciplined reference surface rather than a second source of truth

The goal is not to replace the active LaTeX manuscripts as the scientific record. The goal is to create a searchable, navigable, agent-usable local wiki that helps connect:

- manuscript PDFs
- manuscript routing metadata
- benchmark-facing status
- concept notes
- line-of-development notes
- selected future reference literature

## Governing Principles

### Source-of-truth hierarchy

The wiki must preserve this order of authority:

1. active `.tex` under `manuscripts/active/tex/`
2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv` plus its guide for routing and classification
3. built PDFs under `manuscripts/active/pdf/`
4. wiki summaries, indexes, backlinks, and concept pages

The wiki is a compiled navigation and retrieval layer. It is not the canonical scientific record.

### Routing discipline

The wiki must respect the repository routing taxonomy:

- `front_door`
- `active_primary`
- `active_supporting`
- `historical_but_kept_active`
- `screened_out`
- `side_work`

It must not flatten all manuscripts into one undifferentiated library. Any index or agent query flow that ignores the file map will become misleading.

### Claim discipline

The wiki must encode the same benchmark boundary already enforced in the repository:

- GR is adopted exactly in the benchmark exact-closure package
- a first-principles substrate derivation remains open
- side continuations and screened branches must not be surfaced as the default next step

### Local-first design

The Manuscripts Wiki should be fully usable locally even if external services are unavailable. Obsidian vault content, copied PDFs, generated notes, and sync scripts should all run from the local filesystem.

## Current Repository Findings

The implementation plan should start from the actual repository state, not from an idealized blank setup.

### Existing build and validation seams

The repo already contains:

- `scripts/build_aether_pdf.sh`
- `scripts/validate_active_manuscript_file_map.py`
- `.codex/skills/aether-flow-manuscript-map/SKILL.md`

This is the correct seam for integrating the wiki sync workflow.

### Existing corpus counts

Current local counts observed in the repository:

- `239` active `.tex` manuscripts
- `237` active manuscript PDFs
- `9` retired `.tex` manuscripts
- `9` retired PDFs
- `8` curated public PDF bundle files under `docs/assets/pdfs/`

### Current integrity issues

Before the wiki is treated as healthy, the repo itself should be brought to a coherent baseline:

- `scripts/validate_active_manuscript_file_map.py` currently fails because two active `.tex` files are missing from `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
- two active `.pdf` files are currently missing from `manuscripts/active/pdf/`

The missing active PDFs observed at planning time are:

- `aether_flow_primitive_reservoir_observer_reduction_pre_pre_proto_kernel_dynamics_generating_substrate_pre_selector_pre_pre_pre_proto_kernel_dynamics_next_benchmark_criterion.tex`
- `aether_flow_primitive_reservoir_observer_reduction_pre_proto_kernel_dynamics_generating_substrate_pre_selector_pre_pre_proto_kernel_dynamics_from_pre_pre_proto_kernel_dynamics_generating_substrate_pre_selector_pre_pre_pre_proto_kernel_dynamics_theorem.tex`

The Manuscripts Wiki bootstrap should include a baseline repair pass so the vault starts from a consistent corpus.

### Routing drift warning

Some narrative docs no longer perfectly match the current file map. Therefore:

- routing decisions must come from `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
- wiki front-line pages must be generated from the CSV rather than hand-maintained prose summaries

## Recommended Architecture

## Vault strategy

Start with one primary project-local vault, not multiple vaults.

Recommended local path:

- `.local/obsidian/aether-manuscripts-wiki/`

This path should remain inside the repository tree for discoverability, but it should stay ignored by git.

Rationale:

- the repo already wants implementation-planning and local workflow surfaces to remain out of the tracked scientific docs layer
- the agent can still read and write the vault locally
- the vault can evolve without cluttering versioned manuscript content

### Tracked vs untracked split

Tracked in repo:

- templates
- scripts
- schema docs
- agent skills
- optional sample config fragments

Untracked local content:

- the live Obsidian vault
- copied manuscript PDFs inside the vault
- local plugin state
- local workspace layout
- local-generated query scratchpads

## Karpathy-style layer model adapted to this repo

The wiki should use three practical layers:

### Layer 1: raw sources

Immutable or minimally edited source artifacts:

- project manuscript PDFs copied from `manuscripts/active/pdf/`
- retired manuscript PDFs copied from `manuscripts/retired/pdf/`
- curated public PDF copies from `docs/assets/pdfs/`
- future external reference PDFs

### Layer 2: generated source notes and indexes

LLM-maintained or script-generated markdown notes:

- one note per manuscript PDF
- routing indexes
- line-of-development pages
- concept pages
- query notebooks
- review and triage pages

### Layer 3: schema and operational rules

Machine-readable and human-readable rules for the agent:

- folder conventions
- note frontmatter schema
- sync rules
- conflict policy
- routing read order
- lint rules
- refresh workflow

## Obsidian and PDF++ design choices

## Obsidian

Use a normal local Obsidian vault folder. A vault is just a folder with a `.obsidian/` config directory.

Recommended core features to enable:

- Backlinks
- Outline
- Search
- Page Preview
- Graph View
- Templates

Recommended `Files & Links` behavior:

- use Wikilinks
- auto-update internal links
- fixed attachment location
- show all file extensions when useful

## PDF++

Use PDF++ for:

- copying links to pages and text selections
- backlink highlighting inside PDFs
- viewing note backlinks in context
- embedding rectangular or selection-based PDF references when useful

Do not depend on PDF++ direct PDF editing for canonical repository-owned manuscript copies.

Canonical manuscript PDFs in the vault should be plain copied binaries, not dummy placeholders and not external-link surrogates, because:

- the project wants durable local copies
- copied local files reduce ambiguity
- PDF++ external/dummy workflows are more useful for web-hosted PDFs than for a repo-owned manuscript corpus

## Proposed Vault Layout

```text
aether-manuscripts-wiki/
  .obsidian/
  01_raw/
    project_pdfs/
      active/
      retired/
      public_bundle/
    references/
      external/
    attachments/
  02_sources/
    manuscripts/
    references/
  03_indexes/
    routing/
    families/
    priorities/
  04_lines/
  05_concepts/
  06_queries/
  07_logs/
  08_templates/
  09_schema/
```

### Folder roles

`01_raw/project_pdfs/active/`
- copied current PDFs from `manuscripts/active/pdf/`

`01_raw/project_pdfs/retired/`
- copied retired PDFs from `manuscripts/retired/pdf/`

`01_raw/project_pdfs/public_bundle/`
- copied public-facing package PDFs from `docs/assets/pdfs/`

`01_raw/references/external/`
- curated external PDFs for future literature support

`02_sources/manuscripts/`
- one markdown source note per manuscript PDF

`03_indexes/`
- generated routing views

`04_lines/`
- generated line-of-development pages keyed by `line_name`

`05_concepts/`
- concept pages for recurring framework terms and technical motifs

`06_queries/`
- agent-generated transient or semi-persistent research query notes

`07_logs/`
- sync logs, lint results, and ingestion status records

`08_templates/`
- note templates used by scripts or by manual curation

`09_schema/`
- machine-readable and human-readable schema definitions and workflow docs

## Metadata Model

Each manuscript source note should include frontmatter like:

```yaml
file_name:
title:
family:
document_type:
project_role:
line_name:
frontline_status:
reading_priority:
sequence_stage:
status_reason:
benchmark_effect:
short_description:
current_use_rule:
upstream_dependency:
downstream_target:
relative_tex_path:
relative_repo_pdf_path:
relative_vault_pdf_path:
sha256:
repo_last_modified:
vault_last_synced:
map_last_known_relevance:
```

This metadata should be generated from:

- `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
- the repo filesystem
- file hashing of copied PDFs

## Source Note Template

Each manuscript note should follow a stable structure:

1. Title
2. Routing Status
3. Short Summary
4. Benchmark Effect
5. Current Use Rule
6. Upstream Dependency
7. Downstream Target
8. Open Burden
9. Related Manuscripts
10. Related Concepts
11. PDF Deep Links
12. Build and Sync Metadata

The note should embed or link the copied local PDF so PDF++ features work natively.

## Generated Index Pages

The wiki should generate at least the following index pages automatically.

### Routing indexes

- `03_indexes/routing/front_door.md`
- `03_indexes/routing/active_primary.md`
- `03_indexes/routing/active_supporting.md`
- `03_indexes/routing/historical_but_kept_active.md`
- `03_indexes/routing/screened_out.md`
- `03_indexes/routing/side_work.md`

### Project-role indexes

- `03_indexes/priorities/flagship_package.md`
- `03_indexes/priorities/benchmark_gate.md`
- `03_indexes/priorities/benchmark_routing.md`
- `03_indexes/priorities/current_primary_chain.md`
- `03_indexes/priorities/supporting_main_chain.md`

### Family indexes

- `03_indexes/families/exact_closure.md`
- `03_indexes/families/benchmark_gatekeeping.md`
- `03_indexes/families/primitive_reservoir.md`
- `03_indexes/families/charge_polarization_exact_preservation.md`
- `03_indexes/families/higher_derivative.md`
- `03_indexes/families/general_substrate.md`
- `03_indexes/families/public_facing.md`

### Line indexes

Generate one page per `line_name` under `04_lines/`.

## Concept Pages

The first wave of concept pages should cover recurring repo language rather than trying to summarize all physics immediately.

Mandatory initial concepts:

- `Æther`
- `Æther-flow`
- `S-time`
- observed three-dimensional space
- local experiential slice
- exact closure
- adoption
- derivation
- benchmark exact-closure package
- benchmark gatekeeping
- current primary burden

These concept pages should quote or summarize the approved terminology in:

- `docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md`
- `docs/AETHER_FLOW_CLAIM_BOUNDARY.md`

## Agent Workflow Design

## New skill

Add a new skill:

- `.codex/skills/manuscript-wiki/SKILL.md`

Purpose:

- teach the agent how to use the Obsidian Manuscripts Wiki without treating it as scientific authority over the active `.tex`
- define search and verification order
- define when to consult routing pages, concept pages, source notes, PDFs, and `.tex`

### Skill read order

The skill should tell the agent to use this order:

1. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`
3. the relevant wiki routing index
4. the relevant manuscript source note
5. the copied local PDF if page-specific or selection-specific detail is needed
6. the active `.tex` manuscript for scientific authority

### Skill rules

The skill should explicitly forbid:

- naming the current main line from stale prose summaries
- promoting side work or screened work from wiki backlinks alone
- using wiki summaries to overrule `.tex` language
- using obsolete vault notes after a PDF hash mismatch without re-sync

## Required Scripts

The wiki system should be implemented with repo-local scripts so the workflow remains reproducible.

### `scripts/init_manuscript_wiki.py`

Responsibilities:

- create the vault folder if missing
- scaffold the folder layout
- write initial templates
- write baseline schema files
- optionally write recommended `.obsidian/` config stubs
- optionally print next-step instructions for enabling PDF++

### `scripts/sync_manuscript_wiki_pdfs.py`

Responsibilities:

- copy active manuscript PDFs into the vault
- copy retired manuscript PDFs into the vault
- copy curated public package PDFs into the vault
- detect changed files by hash or modified time
- remove or quarantine stale copies if a repo PDF disappears
- write a sync manifest to `07_logs/`

Important behavior:

- use copy, not symlink
- preserve deterministic destination paths
- support `--all`, `--changed`, and `--one path/to/file.pdf`

### `scripts/generate_manuscript_wiki_notes.py`

Responsibilities:

- read `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
- generate or refresh manuscript source notes
- generate routing indexes
- generate family indexes
- generate line pages
- refresh concept seed pages where appropriate

Important behavior:

- preserve manual annotation blocks where safe
- regenerate machine-owned sections deterministically
- clearly separate generated sections from user-authored notes

### `scripts/lint_manuscript_wiki.py`

Responsibilities:

- detect missing vault PDF copies
- detect missing source notes
- detect stale hashes
- detect notes whose routing metadata disagrees with the CSV
- detect duplicate manuscript notes
- detect broken internal wiki links
- detect missing concept references for required benchmark terminology

### Optional future script: `scripts/query_manuscript_wiki.py`

Responsibilities:

- provide a CLI query interface for agent use
- search metadata, note bodies, and selected headings
- optionally print ranked note paths and manuscript matches

This is optional for phase one because Obsidian search plus filesystem search may be enough initially.

## Integration with Existing Build Flow

The cleanest integration point is `scripts/build_aether_pdf.sh`.

Recommended behavior after a successful build of any active manuscript:

1. build the PDF
2. validate `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
3. sync the corresponding PDF into the vault
4. refresh the manuscript note for that file
5. refresh affected routing or line indexes if needed
6. append a log entry

This should be configurable so the user can skip vault sync if desired.

Suggested flags:

- `--sync-wiki`
- `--no-sync-wiki`
- `MANUSCRIPT_WIKI_VAULT=/abs/path/...`

## Initial Setup Workflow

The initial rollout should be phased.

## Phase 0: baseline repair

Before the wiki is treated as authoritative as a retrieval surface:

1. build the two missing active PDFs
2. add the two missing active `.tex` rows to `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
3. run `python3 scripts/validate_active_manuscript_file_map.py`
4. confirm that the active manuscript set and active PDF set are coherent

Deliverable:

- a healthy active corpus baseline

## Phase 1: tracked scaffolding

Create tracked repo assets:

- `.codex/skills/manuscript-wiki/SKILL.md`
- `scripts/init_manuscript_wiki.py`
- `scripts/sync_manuscript_wiki_pdfs.py`
- `scripts/generate_manuscript_wiki_notes.py`
- `scripts/lint_manuscript_wiki.py`
- `tools/manuscript_wiki_template/` or equivalent tracked template folder

Deliverable:

- reproducible repo-owned wiki tooling

## Phase 2: local vault bootstrap

Steps:

1. create the local vault folder
2. initialize it with the template script
3. open it in Obsidian
4. install PDF++
5. enable recommended core plugins
6. configure file and link behavior

Deliverable:

- working local vault shell with plugin support

## Phase 3: corpus sync

Steps:

1. copy active manuscript PDFs into the vault
2. copy retired manuscript PDFs
3. copy curated public bundle PDFs
4. generate sync manifest
5. verify that copied files open correctly in Obsidian

Deliverable:

- complete local PDF corpus

## Phase 4: note generation

Steps:

1. generate manuscript source notes
2. generate routing indexes
3. generate family and line pages
4. seed concept pages

Deliverable:

- usable wiki navigation layer

## Phase 5: workflow integration

Steps:

1. hook sync into the PDF build flow
2. add lint command
3. add usage docs for the agent and user
4. test incremental update behavior on one edited manuscript

Deliverable:

- sustainable day-to-day workflow

## Phase 6: external literature expansion

After the project manuscript corpus is stable inside the vault, add selected external PDFs:

- reference papers
- benchmark GR references
- methodological papers
- project-adjacent literature

These should live under `01_raw/references/external/` and must be clearly separated from project-authored manuscript PDFs.

Deliverable:

- broader Article Wiki without corrupting project-routing discipline

## Operational Workflow Rules

## When a new manuscript is created

Required workflow:

1. create the `.tex`
2. build the PDF
3. update `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
4. run the CSV validator
5. sync the PDF into the vault
6. generate the manuscript note
7. refresh indexes
8. run wiki lint

## When an existing manuscript is modified

Required workflow:

1. modify the `.tex`
2. rebuild the PDF
3. detect PDF change
4. replace the copied vault PDF
5. update hash and sync metadata
6. refresh the corresponding manuscript note
7. refresh affected indexes if routing changed

## Agent query workflow

When the agent is trying to answer a project question, the wiki skill should encourage:

1. consult the file map first if routing is relevant
2. use the wiki to locate candidate manuscripts, lines, and concepts
3. use PDF++ deep links for page-level verification where useful
4. verify substantive claims against the source `.tex`

## PDF annotation rule

For project manuscripts:

- prefer markdown note annotations linked into PDFs
- avoid mutating the canonical manuscript PDF copies
- keep annotations attributable and local to the vault note layer

## Health Checks and Drift Control

The system should actively defend against drift.

### Lint targets

The lint script should catch:

- vault copies missing for active PDFs
- source notes missing for active files
- source notes whose frontmatter no longer matches the CSV
- hashes changed without note refresh
- broken links to PDFs
- stale routing indexes
- line pages missing current frontier entries
- concept pages with no backlinks from active manuscripts

### Routing drift safeguards

Because prose summaries can become stale, the generated routing pages should always be rebuilt from the CSV.

In particular:

- `active_primary` should be generated directly from the current CSV row
- README-style summaries should not drive the wiki frontier view

### Sync manifest

Maintain a machine-readable sync manifest, for example:

- `07_logs/pdf_sync_manifest.json`

Each entry should record:

- source repo path
- vault destination path
- file size
- hash
- sync timestamp

## Recommended Ignored Paths

The local vault and its generated runtime state should remain ignored.

Suggested additions to `.gitignore` later if desired:

```gitignore
.local/
```

If the repo owner prefers a narrower ignore:

```gitignore
.local/obsidian/
```

## Documentation Deliverables

The implementation should eventually include short tracked docs for:

- how to initialize the local vault
- how to install PDF++
- how the sync process works
- how the agent should use the wiki
- what is authoritative when the wiki and repo prose disagree

These docs should stay compact and should not replace the scientific manuscript sources.

## Immediate Next Steps

The best practical execution order is:

1. repair the current active PDF and file-map baseline
2. scaffold the tracked wiki tooling and new skill
3. create the local vault
4. install PDF++
5. sync the manuscript PDF corpus
6. generate source notes and routing pages
7. wire incremental sync into the PDF build workflow
8. test the workflow on one real manuscript edit

## Expected Outcome

When implemented, the Manuscripts Wiki should give the project:

- a local searchable manuscript knowledge base
- page-level PDF linking and backlinking via PDF++
- routing-aware manuscript retrieval grounded in the file map
- an agent-usable knowledge layer that collaborates with the active `.tex` line
- automatic inclusion of newly built or modified manuscript PDFs
- a disciplined way to add future reference literature without losing project structure

## Reference Sources Used for the Plan

- `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
- `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`
- `docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md`
- `docs/AETHER_FLOW_CLAIM_BOUNDARY.md`
- `README.md`
- `.codex/skills/aether-flow-manuscript-map/SKILL.md`
- `scripts/build_aether_pdf.sh`
- `scripts/validate_active_manuscript_file_map.py`
- Obsidian documentation
- PDF++ documentation
- Karpathy `llm-wiki` concept gist
