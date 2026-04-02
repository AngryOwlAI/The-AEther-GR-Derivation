# Active Manuscript File Map Plan

## Purpose

This plan defines how the repository should create and use a clean file map for the active manuscript tree of `The Æther-Flow Interpretation of Relativity`.

The goal is not to replace the manuscripts or to downgrade existing work. The goal is to give future agents and reviewers a reliable routing system for answering:

- what the flagship package is
- what the current benchmark-facing derivation chain is
- what counts as screened historical branch work
- what counts as side continuation
- which files no longer count as front-line progress unless they change benchmark-facing status

## Background

The repository now contains two very different kinds of active material in the same manuscript tree:

- a stable exact-closure flagship package that already serves as the benchmark public theory statement
- a much larger derivational manuscript line that includes primary work, supporting work, screened branches, and side continuations

The audit of the active tree showed that the derivational line can keep moving one layer deeper even when a new manuscript does not materially change the benchmark-facing status of the project. In practice, some files produce genuine front-line progress, while others preserve the same one-metric observer result and mainly relocate the unexplained substrate layer farther upstream.

Without a formal map, an agent can easily confuse those two cases.

This plan therefore creates a machine-sortable inventory plus a small policy layer so future agents can classify manuscripts consistently before proposing new work, summarizing project state, or deciding what the next front-line step is.

## Why This Is Needed

- The benchmark theory statement already exists and should not be repeatedly treated as unresolved.
- The active manuscript tree is large enough that informal memory is no longer reliable.
- Some derivational manuscripts are benchmark-facing primary work, while others are better treated as screened, supporting, or side-line material.
- The repository needs a stable way to distinguish primary progress from preserved-output deeper-origin continuation.
- Future agents need one source of truth before classifying branches or recommending the next step.

## Core Idea

Create two new documentation artifacts and one enforcement layer:

1. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`
3. a repo-local agent rule in `AGENTS.md`, supported by a small local skill

The CSV will be the machine-sortable inventory.

The guide will define the taxonomy and the classification rules.

The `AGENTS.md` rule will make use of the map mandatory whenever routing or front-line status is at issue.

The local skill will provide a reusable workflow so agents can apply the taxonomy consistently.

## Deliverables

### 1. CSV Inventory

Create:

- `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`

This CSV should include all active `.tex` manuscripts under `manuscripts/active/tex/`.

### 2. Guide

Create:

- `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`

This guide should define the categories, explain the front-line decision rules, and document how descriptions are written consistently.

### 3. Agent Enforcement

Update:

- `AGENTS.md`

Add a repo-local rule requiring agents to consult the file map before:

- proposing a new active manuscript
- summarizing project state
- identifying the current main line
- classifying a branch as front-line
- recommending the next benchmark-facing step

### 4. Local Skill

Create a small local skill for manuscript-map maintenance and routing.

The skill should help agents:

- read the CSV first
- apply the taxonomy
- classify files consistently
- distinguish front-door, active-primary, active-supporting, screened-out, and side-work status
- avoid treating same-output deeper-origin relays as front-line without a benchmark-facing reason

## Proposed CSV Columns

The CSV should include at least the following columns:

- `file_name`
- `relative_path`
- `pdf_path`
- `title`
- `family`
- `document_type`
- `project_role`
- `line_name`
- `frontline_status`
- `status_reason`
- `reading_priority`
- `sequence_stage`
- `upstream_dependency`
- `downstream_target`
- `benchmark_effect`
- `short_description`
- `current_use_rule`
- `last_known_relevance`

## Taxonomy

Classification should be separated into multiple fields so one column does not carry too much meaning.

### Family

Recommended values:

- `exact_closure`
- `benchmark_gatekeeping`
- `higher_derivative`
- `charge_polarization_exact_preservation`
- `primitive_reservoir`
- `general_substrate`
- `public_facing`

### Document Type

Recommended values:

- `overview`
- `article`
- `foundations`
- `dynamics`
- `consistency`
- `recovery`
- `geometry`
- `note`
- `theorem`
- `test`
- `verdict`
- `criterion`
- `obstruction`
- `requirements`
- `setup`

### Project Role

Recommended values:

- `flagship_package`
- `benchmark_routing`
- `benchmark_gate`
- `current_primary_chain`
- `supporting_main_chain`
- `screened_historical_branch`
- `side_continuation`
- `background_support`

### Front-Line Status

Recommended values:

- `front_door`
- `active_primary`
- `active_supporting`
- `screened_out`
- `side_work`
- `historical_but_kept_active`

## Front-Line Decision Rule

A manuscript should no longer count as front-line progress if it:

- preserves the same one operative metric
- preserves the same observer-equation closure verdict
- preserves the same benchmark-facing output
- and only relocates the unexplained substrate layer deeper without proving a new gate, compression, necessity, or uniqueness result that changes project status

That rule is the main safeguard against recursive depth drift.

## Short Description Rule

Each `short_description` entry should answer two questions:

1. What does the file do?
2. Does it change benchmark-facing status?

Preferred style:

- "Proves the benchmark derivation gates that any honest substrate derivation must satisfy."
- "Records that the same-package observer-side remainder gate is settled on the active branch and shifts the open burden upstream."
- "Introduces a deeper substrate layer while preserving the same one-metric observer package; does not by itself change benchmark-facing status."

## Implementation Sequence

### Phase 1. Freeze the Taxonomy

- Finalize the CSV columns.
- Finalize the category definitions in the guide.
- Define the front-line decision rule in exact wording.

### Phase 2. Seed the Benchmark Package

Populate the benchmark exact-closure package first:

- overview
- exact-closure note
- foundations
- dynamics
- consistency
- relativistic recovery
- geometry
- flagship public article

Mark these as `front_door` or `flagship_package`.

### Phase 3. Seed the Benchmark-Routing Layer

Populate the benchmark-routing and benchmark-facing control files:

- benchmark derivation-gates note
- post-bridge derivation-gate status note
- upstream compression theorem
- continuity-Hessian necessity / uniqueness theorem
- continuity-Hessian derivation theorem

### Phase 4. Map the Current Primary Derivation Chain

Populate the current primitive-reservoir observer-reduction line in order.

Mark only the live frontier and directly supporting files as `active_primary` or `active_supporting`.

### Phase 5. Classify Screened Historical Branches

Classify higher-derivative screened, negative, or superseded branch files as `screened_historical_branch` unless a specific file still controls an active gate or benchmark-facing routing decision.

### Phase 6. Classify Side Continuations

Classify orbit-shape, primitive-class, midpoint-selector, and related continuations as `side_work` unless current routing docs explicitly promote them.

### Phase 7. Add Descriptions

Write one-sentence descriptions for all files using the short-description rule.

### Phase 8. Add Enforcement

Update `AGENTS.md` so file-map consultation is mandatory whenever routing or front-line status is discussed.

### Phase 9. Add Skill Support

Create the local skill that teaches agents how to consult and update the map.

### Phase 10. Validate

Add a validation pass that checks:

- every active `.tex` file appears in the CSV
- every CSV row points to an existing file
- front-line files remain consistent with `RESEARCH_PLAN.md`
- benchmark package labels remain fixed

### Phase 11. Produce Human-Facing Summary

Use the finished map to produce a clean high-level summary of:

- flagship package
- current benchmark-facing derivation chain
- screened historical branches
- files that no longer count as front-line progress

## AGENTS.md Enforcement Rule

The plan should add a rule to `AGENTS.md` stating that agents must consult the file map before:

- proposing a new active manuscript
- describing the project's current main line
- classifying a file as front-line progress
- recommending the next benchmark-facing step

The plan should also add a maintenance rule:

- if an agent creates a new active `.tex` manuscript, reclassifies an active manuscript, or changes front-line status, it must update the CSV in the same task

The plan should add a conflict rule:

- if `AGENTS.md`, the CSV, `RESEARCH_PLAN.md`, and the routing docs disagree, the agent must note the conflict explicitly and avoid silently inventing a new front-line status

## Skill Support

The local skill should be treated as a convenience workflow, not as the only enforcement mechanism.

The intended interaction is:

- `AGENTS.md` is the mandatory guardrail
- the skill is the reusable procedure for carrying the rule out efficiently

This avoids relying on skill triggering alone.

## Validation Rule

The map should be considered valid only if:

- all active `.tex` manuscripts are represented
- all paths are correct
- benchmark package labels remain stable
- current primary-chain labels agree with the current research plan
- screened and side-work labels are backed by the files' own verdict or routing language

## Success Condition

This plan succeeds when a future agent can consult one authoritative file map and determine, without guesswork:

- the fixed public reading package
- the benchmark-routing manuscripts
- the current deepest benchmark-facing derivation step
- which branches are screened historical work
- which continuations are side work
- whether a proposed new manuscript would actually change project status or merely go deeper without changing the benchmark-facing result

## Final Note

The purpose of this plan is clarity, not demotion. The repository can preserve the full derivational archive while still making it clear which files are:

- benchmark-defining
- benchmark-routing
- actively front-line
- screened but historically informative
- or side continuations that should not be mistaken for the current primary task
