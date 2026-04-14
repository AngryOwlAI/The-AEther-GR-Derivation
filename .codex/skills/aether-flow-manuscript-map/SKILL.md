# Aether-Flow Manuscript Map

Use this skill whenever the task involves manuscript routing rather than manuscript science alone.

Typical triggers:

- summarizing repository state
- identifying the current main line
- deciding whether a manuscript is front-line
- proposing a new active manuscript
- recommending the next benchmark-facing step
- updating the active manuscript file map

## Read Order

Read these first and in this order:

1. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`
3. the specific active `.tex` file being discussed

If public claim status is involved, also read the benchmark front door first:

- `manuscripts/active/tex/aether_flow_exact_closure_sequence_overview.tex`
- `manuscripts/active/tex/aether_flow_exact_closure_note.tex`

## Core Rules

- Treat the file map as the routing control layer and the active `.tex` manuscripts as the scientific source of truth.
- Use `frontline_status`, `project_role`, `benchmark_effect`, and `current_use_rule` before making routing claims.
- Do not treat a same-output deeper-origin relay as front-line progress unless it changes benchmark-facing status through a new gate, compression, necessity, or uniqueness result.
- After the GR-derivation reset, do not assume there is always an `active_primary` row; the file map may intentionally carry none until a bounded synthesis, derivation-attempt, or obstruction manuscript exists.
- Do not present `screened_out` or `side_work` files as the default next main-line step.
- Do not skip the benchmark-gatekeeping rows when naming the current main line or the next honest burden.

## Working Procedure

1. Locate the row for the file in `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`.
2. Read `frontline_status` and `project_role`.
3. Read `status_reason`, `benchmark_effect`, and `current_use_rule`.
4. Check whether the map points to a front-door file, benchmark gate, current bounded frontier, strongest bridge-entry / bridge-object support file, historical record, screened branch, or side continuation.
5. If no `active_primary` row exists, treat that absence as deliberate reset state and use benchmark-gatekeeping rows plus the bridge-entry / bridge-object anchors to explain the current main-line burden.
6. Only then open the manuscript itself for scientific detail.

## Output Rules

When answering a routing question:

- name the file’s `frontline_status`
- say whether it changes benchmark-facing status
- state whether it is front door, current bounded frontier, direct bounded-program support, historical support, screened branch, or side work
- if recommending a next step, tie it to the `active_primary` row when one exists, otherwise tie it to the benchmark-gatekeeping rows and bridge-object anchors that define the bounded program

When updating the CSV:

- include every active `.tex` file under `manuscripts/active/tex/`
- keep `pdf_path` aligned with `manuscripts/active/pdf/`
- update `last_known_relevance`
- keep `short_description` to one sentence answering what the file does and whether it changes benchmark-facing status
- prefer conservative status assignments; promotion requires a benchmark-facing reason
- run `python3 scripts/validate_active_manuscript_file_map.py` before closing the task
