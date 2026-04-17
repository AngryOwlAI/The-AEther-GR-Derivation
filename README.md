# The Æther-Flow Interpretation of Relativity

## Exact-GR Benchmark and Substrate Research Program

This repository is the active LaTeX workspace for `The Æther-Flow Interpretation of Relativity`. The overview-first exact-closure package is the flagship scientific result already in hand: it adopts GR exactly as the operational relativistic sector with ordinary matter coupling, and it serves as the benchmark theory statement for the repository. The downstream substrate program is now separate in role: it asks whether a genuinely new line can derive that benchmark without changing the benchmark claim boundary prematurely.

Operationally, the benchmark package is ordinary GR at observable scale: Einstein-Hilbert dynamics, one operative metric, universal matter coupling, standard relativistic causal structure, and no extra preferred-frame, vector, or scalar graviton sector. Packet B is a separate scoped no-go on the frozen primitive-reservoir derivational line, not a revision of that benchmark package. The congruence layer belongs to standard GR observer kinematics, and any surviving novelty claim is methodological: benchmark-first package discipline and explicit no-go discipline inside the broader emergent / induced / reconstruction conversation.

Earlier ontology/background material is preserved in the predecessor repository [The Æther](https://github.com/AngryOwlAI/The-AEther).

## Status Snapshot

- Benchmark package: the overview-first exact-closure sequence is the flagship result and the public front door.
- Relation to GR: the repository currently presents an exact-GR benchmark and interpretive package, not a low-energy modification or replacement of GR.
- Current-line verdict: the frozen primitive-reservoir bounded line ends in the scoped verdict `Not Derived On Current Line`.
- Next admissible move: either stop with that scoped no-go and package the benchmark result already in hand, or open a genuinely new line with an explicit observer-localizing law, new primitive variable, or new symmetry principle.

## Project Intent

The project is not merely an ontology archive waiting for legitimacy from a future derivation. Its active intent is twofold:

- preserve the `Æther / Æther-flow` ontology in rigorous form
- state and maintain `The Æther-Flow Interpretation of Relativity` as an exact relativistic theory at the effective level

The benchmark package is therefore a positive scientific deliverable in its own right, while any resumed derivational line remains downstream foundational work answerable to that benchmark.

The explicit identity decision for the current repository is recorded in [docs/PROJECT_IDENTITY_DECISION_NOTE.md](docs/PROJECT_IDENTITY_DECISION_NOTE.md): keep exact GR as the public benchmark identity, treat derivation as a separate open burden, and do not treat low-energy GR modification or replacement as the current flagship project.

## Current State

- Public front door: [aether_flow_exact_closure_sequence_overview.tex](manuscripts/active/tex/aether_flow_exact_closure_sequence_overview.tex)
- Public orientation article: [aether_flow_exact_closure_flagship_article.tex](manuscripts/active/tex/aether_flow_exact_closure_flagship_article.tex)
- Fixed benchmark package: [aether_flow_exact_closure_note.tex](manuscripts/active/tex/aether_flow_exact_closure_note.tex), [aether_flow_foundations.tex](manuscripts/active/tex/aether_flow_foundations.tex), [aether_flow_dynamics.tex](manuscripts/active/tex/aether_flow_dynamics.tex), [aether_flow_consistency.tex](manuscripts/active/tex/aether_flow_consistency.tex), [aether_flow_relativistic_recovery.tex](manuscripts/active/tex/aether_flow_relativistic_recovery.tex), and [aether_flow_geometry.tex](manuscripts/active/tex/aether_flow_geometry.tex)
- Benchmark gatekeeping: [aether_flow_exact_closure_derivation_gates_note.tex](manuscripts/active/tex/aether_flow_exact_closure_derivation_gates_note.tex), [aether_flow_exact_closure_post_bridge_derivation_gate_status_note.tex](manuscripts/active/tex/aether_flow_exact_closure_post_bridge_derivation_gate_status_note.tex), and [aether_flow_benchmark_one_metric_observer_package_upstream_compression_theorem.tex](manuscripts/active/tex/aether_flow_benchmark_one_metric_observer_package_upstream_compression_theorem.tex)
- Live bounded verdict: [aether_flow_current_line_gr_derivation_obstruction_or_no_go.tex](manuscripts/active/tex/aether_flow_current_line_gr_derivation_obstruction_or_no_go.tex) holds `active_primary`; [aether_flow_bounded_gr_derivation_bridge_object_synthesis.tex](manuscripts/active/tex/aether_flow_bounded_gr_derivation_bridge_object_synthesis.tex) remains active supporting context; [aether_flow_bounded_gr_derivation_attempt_from_explicit_substrate_package_and_primitive_dynamics.tex](manuscripts/active/tex/aether_flow_bounded_gr_derivation_attempt_from_explicit_substrate_package_and_primitive_dynamics.tex) is preserved as the immediate suspension-stage handoff
- Historical same-output deeper-relay material remains preserved, but it no longer defines the default next move
- The deeper positive-pair / orbit-shape continuation remains recorded side work unless it changes the benchmark-facing burden

## Primary Goal

The primary goal is to keep the benchmark exact-closure theory statement scientifically stable and to present it clearly as the flagship result already achieved. If derivational work is resumed, it should proceed only as a disciplined new-line program testing whether the adopted GR benchmark can be derived from deeper substrate structure. The project goal is not to rebrand unfinished derivational work as success, and it is not to turn the current repository into a low-energy non-GR gravity project.

## Start Here

- [docs/start-here.md](docs/start-here.md)
- [docs/theory-package.md](docs/theory-package.md)
- [docs/research-archive.md](docs/research-archive.md)
- [docs/review_packets/README.md](docs/review_packets/README.md)
- [docs/AETHER_FLOW_CLAIM_BOUNDARY.md](docs/AETHER_FLOW_CLAIM_BOUNDARY.md)
- [docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md](docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md)

## Repository Layout

- `manuscripts/active/tex/`: active manuscript source of truth
- `manuscripts/active/pdf/`: built PDFs
- `docs/`: compact public and policy documentation
- `docs/review_packets/`: phase-8 review bundle with `ai/` LaTeX-first Markdown packets for AI review, `ai_pdfs/` PDF-first packet copies for AI PDF workflows, and `human/` PDF-first handoff copies for human review
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
- `scripts/build_aether_pdf.sh` runs the active manuscript file-map validation automatically after builds from `manuscripts/active/tex/`, and it can sync rebuilt PDFs into the local Manuscript Wiki.

## Manuscript Wiki

The local Obsidian Manuscript Wiki is part of the supported day-to-day workflow. Use [docs/manuscript-wiki-workflow.md](docs/manuscript-wiki-workflow.md) for the build, sync, lint, and authority-order commands. Use the wiki and the file map as the retrieval layer before broad repository search, and use the active `.tex` manuscripts as the scientific authority. Phase 6 also supports a separate supplemental external-reference library under the local vault without mixing that literature into the project-routing surfaces.

## Context Economy

The Markdown layer is intentionally compact. For scientific detail, read the relevant active `.tex` manuscript directly instead of treating repository documentation as a narrative archive.
