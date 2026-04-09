# Active Manuscript File Map Guide

## Purpose

This guide defines the taxonomy and update rules for `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`.

The file map is a routing layer for `The Æther-Flow Interpretation of Relativity`. It helps agents and reviewers distinguish:

- the benchmark exact-closure front door
- the benchmark-gatekeeping layer
- the current primitive-reservoir main line
- preserved but non-front-line chain history
- screened historical branches
- side continuations that remain active without counting as default front-line progress

The scientific source of truth remains the active `.tex` manuscripts under `manuscripts/active/tex/`. The file map exists so repository routing is disciplined before anyone proposes new work or summarizes project state.

## Use Order

When routing or classification is at issue, read in this order:

1. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`
3. the front-door benchmark package if the question touches public claim status
4. the specific active `.tex` manuscript being edited or discussed

The local routing skill at `.codex/skills/aether-flow-manuscript-map/SKILL.md` follows the same order.

## CSV Columns

The CSV uses the following columns.

| Column | Meaning |
| --- | --- |
| `file_name` | Active manuscript filename. |
| `relative_path` | Repository path to the active `.tex` file. |
| `pdf_path` | Matching built PDF path under `manuscripts/active/pdf/`. |
| `title` | Normalized descriptive title for routing and review. |
| `family` | Lineage family of the manuscript. |
| `document_type` | Manuscript form such as `overview`, `theorem`, `note`, or `test`. |
| `project_role` | Repository role such as `flagship_package`, `benchmark_gate`, or `side_continuation`. |
| `line_name` | Named manuscript line used for routing. |
| `frontline_status` | Whether the file is default front door, current frontier, direct support, preserved history, screened branch, or side work. |
| `status_reason` | One-sentence explanation of why that status was assigned. |
| `reading_priority` | Practical read order for agents. |
| `sequence_stage` | Stage label inside the named line. For long chains this is an inventory-stage label, not a claim of formal proof order unless the label says otherwise. |
| `upstream_dependency` | What must already be in hand to use the manuscript honestly. |
| `downstream_target` | Where the manuscript routes future reading or work. |
| `benchmark_effect` | Whether and how the manuscript changes benchmark-facing status. |
| `short_description` | Single-sentence summary answering what the file does and whether it changes benchmark-facing status. |
| `current_use_rule` | How to use the file today when answering repository questions. |
| `last_known_relevance` | Date stamp for the last routing audit. |

## Taxonomy

### Family

`family` tracks lineage rather than present-day importance.

| Value | Meaning |
| --- | --- |
| `exact_closure` | Core benchmark exact-closure package files. |
| `benchmark_gatekeeping` | Routing notes or criteria that control benchmark-facing status. |
| `primitive_reservoir` | Primitive-reservoir handoff and observer-reduction line. |
| `charge_polarization_exact_preservation` | Same-package exact-preservation observer-equation and deeper-origin line. |
| `higher_derivative` | Higher-derivative screened branches and side continuations. |
| `general_substrate` | Early substrate bridge setup and background bridge tests. |
| `public_facing` | Public-facing packaging artifact for the benchmark package. |

### Project Role

`project_role` answers what the file is for in the repository.

| Value | Meaning |
| --- | --- |
| `flagship_package` | Core benchmark package and public front door. |
| `benchmark_routing` | Routing note or criterion that still affects honest next-step decisions. |
| `benchmark_gate` | File that fixes or settles a benchmark-facing gate. |
| `current_primary_chain` | File on the current primitive-reservoir main line. |
| `supporting_main_chain` | Supporting file for the current main line or handoff into it. |
| `screened_historical_branch` | Preserved branch that is screened, negative, or superseded. |
| `side_continuation` | Active side continuation that is not default front-line progress. |
| `background_support` | Early bridge background still worth retaining but not routing the current frontier. |

### Front-Line Status

`frontline_status` answers whether the file should count as default progress today.

| Value | Meaning |
| --- | --- |
| `front_door` | Read first. Defines the benchmark package. |
| `active_primary` | Current deepest benchmark-facing main-line gain. |
| `active_supporting` | Direct support or still-live routing/gate file for the current frontier. |
| `historical_but_kept_active` | Preserved chain history or closure history, not default next-step progress. |
| `screened_out` | Screened, superseded, or negative branch record. |
| `side_work` | Side continuation that remains active but is not default main-line progress. |

### Reading Priority

`reading_priority` is the practical order for agents.

| Value | Meaning |
| --- | --- |
| `front_door` | Read before any derivational routing discussion. |
| `routing` | Read before naming the main line or next benchmark-facing step. |
| `frontier` | Read when working at the current deepest frontier. |
| `supporting` | Read when directly supporting the current frontier. |
| `historical` | Read only when immediate chain history matters. |
| `screened_reference` | Reference only; not a default next step. |
| `side_reference` | Reference only for side continuations. |

## Front-Line Decision Rule

A manuscript should no longer count as front-line progress if it:

- preserves the same one operative metric
- preserves the same observer-equation closure verdict
- preserves the same benchmark-facing output
- and only relocates the unexplained substrate layer deeper without proving a new gate, compression, necessity, or uniqueness result that changes project status

This is the repository safeguard against recursive depth drift.

## Classification Rules

Apply the fields in this order:

1. `family`: what lineage the manuscript belongs to
2. `project_role`: what repository job it performs now
3. `frontline_status`: whether it counts as default progress now
4. `benchmark_effect`: whether it changes benchmark-facing status
5. `current_use_rule`: how an agent should use it today

Important consequences:

- `front_door` files fix the benchmark package and come before derivational routing.
- `benchmark_gate` and `benchmark_routing` files must be consulted before claiming what the current main line is.
- `active_primary` should be unique or nearly unique at any given time.
- `active_supporting` is reserved for direct support or still-live routing/gate files, not for every preserved theorem on the chain.
- `historical_but_kept_active` means the file still matters, but it is not the default answer to “what is the next step?”
- `screened_out` means preserved branch record, not default candidate for reactivation.
- `side_work` means active continuation, but not main-line progress unless later promoted by routing docs or a genuinely benchmark-facing result.

## Short Description Rule

Every `short_description` should answer two questions in one sentence:

1. What does the file do?
2. Does it change benchmark-facing status?

Preferred style:

- “Proves the benchmark derivation gates that any honest substrate derivation must satisfy.”
- “Records that the same-package observer-side remainder gate is settled on the active branch and shifts the open burden upstream.”
- “Introduces a deeper substrate layer while preserving the same one-metric observer package; does not by itself change benchmark-facing status.”

## Maintenance Rules

When updating the file map:

1. Include every active `.tex` manuscript under `manuscripts/active/tex/`.
2. Keep `pdf_path` aligned with the built file under `manuscripts/active/pdf/`.
3. Update `last_known_relevance` to the date of the routing audit.
4. Re-check the benchmark package rows first.
5. Re-check the benchmark-gatekeeping rows second.
6. Re-check the current primitive-reservoir frontier and its direct support rows third.
7. Do not promote a file from `historical_but_kept_active`, `screened_out`, or `side_work` without a benchmark-facing reason stated in `status_reason` and `benchmark_effect`.
8. Run `python3 scripts/validate_active_manuscript_file_map.py` before closing the task.

The tracked validator script is:

- `scripts/validate_active_manuscript_file_map.py`

The active-manuscript PDF build flow also runs this validator automatically after builds from `manuscripts/active/tex/`.

## Default Routing Summary

At the current audit:

- the benchmark exact-closure package is the front door
- the benchmark-gatekeeping layer must be consulted before any main-line claim
- the current file map carries a single `active_primary` row at `primitive_reduction_current_pre_selector_pre_pre_pre_proto_kernel_frontier`
- benchmark-facing status after the post-bridge routing correction is governed by the continuity-Hessian compressed core and the bridge-entry derivations that force it; later same-output relays should be treated conservatively unless they derive, uniquely force, or further compress that bridge object
- the same-package exact-preservation line is preserved as supporting or historical routing context
- screened higher-derivative branches remain screened
- nonlocal self-response / orbit-shape continuations remain side work unless explicitly promoted
