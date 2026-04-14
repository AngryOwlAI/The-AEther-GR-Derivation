# The Æther-Flow Interpretation of Relativity - GR Derivation

This repository is the active LaTeX workspace for `The Æther-Flow Interpretation of Relativity`. The overview-first exact-closure package is the benchmark theory statement, and GR is adopted there exactly as the operational relativistic sector with ordinary matter coupling. The current line has not yet derived that benchmark from explicit `Æther / Æther-flow` structure. The active research question is whether the present line can derive the adopted benchmark under the five benchmark derivation gates.

Earlier ontology/background material is preserved in the predecessor repository [The Æther](https://github.com/AngryOwlAI/The-AEther).

## Project Intent

The project is not merely an ontology archive waiting for its first disciplined theory statement. Its intent is twofold:

- to preserve the `Æther / Æther-flow` ontology in rigorous form
- to state and maintain `The Æther-Flow Interpretation of Relativity` as an exact relativistic theory at the effective level

The exact-closure package is therefore a positive scientific deliverable in its own right, while the deeper derivational line remains active foundational work downstream of that benchmark.

## Current State

- Public front door: [aether_flow_exact_closure_sequence_overview.tex](manuscripts/active/tex/aether_flow_exact_closure_sequence_overview.tex)
- Fixed benchmark package: [aether_flow_exact_closure_note.tex](manuscripts/active/tex/aether_flow_exact_closure_note.tex), [aether_flow_foundations.tex](manuscripts/active/tex/aether_flow_foundations.tex), [aether_flow_dynamics.tex](manuscripts/active/tex/aether_flow_dynamics.tex), [aether_flow_consistency.tex](manuscripts/active/tex/aether_flow_consistency.tex), [aether_flow_relativistic_recovery.tex](manuscripts/active/tex/aether_flow_relativistic_recovery.tex), and [aether_flow_geometry.tex](manuscripts/active/tex/aether_flow_geometry.tex)
- Claim boundary: GR is adopted exactly in the benchmark package; the current line has not yet derived that benchmark from explicit substrate structure
- The benchmark package is a completed exact-closure theory statement at the operational level, not a temporary placeholder
- Active research question: determine whether the present line can derive the adopted benchmark under the five benchmark derivation gates
- Post-bridge routing: the same-package observer-side closure burden is no longer the live bottleneck on the active one-metric line; the remaining honest burden is upstream substrate derivation of the benchmark package rather than another package-preserving same-output relay
- Active file-map state: no manuscript currently holds `active_primary`; that slot is reserved for a bounded bridge-object synthesis manuscript, bounded derivation attempt, or obstruction/no-go manuscript
- Former relay endpoint: use [docs/manuscript-wiki-workflow.md](docs/manuscript-wiki-workflow.md), [docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv](docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv), [docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md](docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md), and the local Manuscript Wiki to locate the preserved pre-reset source-penalty-kernel relay endpoint when reconstructing old chain history; it no longer defines the default next move
- Current derivational outcome framing: valid answers are `Derived`, `Not Derived On Current Line`, or `Suspended Pending New Law`; depth alone is not a research verdict
- The deeper positive-pair / orbit-shape continuation remains recorded side work unless it changes that primary burden

## Primary Goal

The primary goal is to keep the benchmark exact-closure theory statement scientifically stable while pursuing a disciplined derivational program that determines whether the current line can derive that adopted GR benchmark from deeper substrate structure. The project goal is not to replace GR by a separate low-energy deformation, and it is not to present unfinished derivational work as already complete.

## Start Here

- [docs/start-here.md](docs/start-here.md)
- [docs/theory-package.md](docs/theory-package.md)
- [docs/research-archive.md](docs/research-archive.md)
- [docs/AETHER_FLOW_CLAIM_BOUNDARY.md](docs/AETHER_FLOW_CLAIM_BOUNDARY.md)
- [docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md](docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md)

## Repository Layout

- `manuscripts/active/tex/`: active manuscript source of truth
- `manuscripts/active/pdf/`: built PDFs
- `docs/`: compact public and policy documentation
- `RESEARCH_PLAN.md`: current live research board
- `EXECUTION_CHECKLIST.md`: operational checklist for manuscript work
- `docs/manuscript-wiki-workflow.md`: local Obsidian Manuscript Wiki workflow

## Working Rules

- New manuscript content is written in `.tex`.
- Keep ontology, adopted GR benchmark, and derivational ambitions clearly separated.
- Preserve the fixed benchmark reading order before surfacing downstream derivational notes.
- Rebuild the matching PDF after each `.tex` change.
- Keep [RESEARCH_PLAN.md](RESEARCH_PLAN.md) active and tracked as a live control document.
- Retire completed one-off implementation-planning Markdown into the local ignored archive at `docs/_archived_plans/` instead of leaving it in the active tracked docs surface.
- After adding, removing, or renaming an active manuscript, keep [docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv](docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv) in sync and run `python3 scripts/validate_active_manuscript_file_map.py`.
- `scripts/build_aether_pdf.sh` now runs the active manuscript file-map validation automatically after builds from `manuscripts/active/tex/`, and it can sync rebuilt PDFs into the local Manuscript Wiki.

## Manuscript Wiki

The local Obsidian Manuscript Wiki is now part of the supported day-to-day workflow. Use [docs/manuscript-wiki-workflow.md](docs/manuscript-wiki-workflow.md) for the build, sync, lint, and authority-order commands. Use the wiki and file map as the retrieval layer before broad repository search, and use the active `.tex` manuscripts as the scientific authority.
Phase 6 also supports a separate supplemental external-reference library under the local vault without mixing that literature into the project-routing surfaces.

## Context Economy

The Markdown layer is now intentionally short. For scientific detail, read the relevant active `.tex` manuscript directly instead of treating repository documentation as a narrative archive.
