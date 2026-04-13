# GR Benchmark Wording Patch Plan

Updated: April 13, 2026

Status: Plan only. This document does not apply the wording patches. It defines a small repo-facing patch set that makes the benchmark/derivation distinction explicit everywhere it matters without changing the scientific benchmark.

## Goal

Standardize the repo’s wording so the following three statements always travel together:

1. GR is adopted exactly in the benchmark exact-closure package.
2. GR is not yet derived from explicit substrate structure on the current line.
3. The active derivational question is whether the current line can derive that adopted benchmark under the five benchmark derivation gates.

This patch plan does **not** change the scientific benchmark.

It does **not** replace:

- exact GR adoption in the benchmark package
- the five-gate derivation standard
- the benchmark/package split already established in the front-door manuscripts

It only tightens wording so adoption, derivation, and the active open question are not allowed to drift apart in repo-facing prose.

## Why This Patch Is Needed

The current repo wording is already close to the right position, but the distinction is not always stated in the same compact form across all public-facing and operational surfaces.

The main risk is not explicit overclaiming.

The main risk is partial phrasing such as:

- “GR is adopted exactly” without the matching “not yet derived”
- “the derivation remains open” without the matching benchmark reminder
- “the active frontier is X” without the matching statement that X is not itself a completed derivation

This patch should make the default repo language mechanically clear.

## Canonical Wording To Standardize

### Primary three-part formula

Use this exact structure whenever a repo-facing page summarizes project status:

- The benchmark exact-closure package adopts GR exactly as the operational relativistic sector with ordinary matter coupling.
- The current line has not yet derived that benchmark package from explicit substrate structure.
- The active derivational question is whether the present line can derive the adopted benchmark under the five benchmark derivation gates.

### Short public formula

When only one short status sentence fits, use:

- `GR is adopted exactly in the benchmark package; first-principles substrate derivation remains open on the current line.`

### Short research formula

When naming the active research burden, use:

- `The active task is not to restate the benchmark package, but to determine whether the current line can derive that adopted GR benchmark under the recorded derivation gates.`

### Disallowed shortened formulas

Avoid repo-facing summaries that use only one side of the distinction, for example:

- `GR is adopted exactly.` if it is not immediately paired with the open derivation status
- `GR has not been derived.` if it is not immediately paired with the fact that the benchmark package is still scientifically in hand
- `The frontier is X.` if it is not immediately paired with the warning that X is not itself a completed GR derivation

## Small Patch Set

The patch should stay small and target the highest-leverage wording surfaces first.

### Group A: Claim and benchmark control

Patch these files first:

- [docs/AETHER_FLOW_CLAIM_BOUNDARY.md](AETHER_FLOW_CLAIM_BOUNDARY.md)
- [README.md](../README.md)

Planned change:

- add the three-part formula near the top of each file
- make “GR adopted exactly” and “derivation remains open” appear in the same block
- add one sentence clarifying that the active derivational question is whether the current line can derive the adopted benchmark, not whether the benchmark package exists

Expected outcome:

- the repo’s claim boundary and repo root say the same thing in the same order

### Group B: Public-facing docs pages

Patch these files second:

- [docs/start-here.md](start-here.md)
- [docs/theory-package.md](theory-package.md)
- [docs/how-to-review.md](how-to-review.md)

Planned change:

- insert one compact status paragraph on each page using the short public formula
- add a sentence that the active research line is testing whether the current line can derive the adopted benchmark
- avoid new technical detail; this is wording alignment only

Expected outcome:

- a new reader sees the same benchmark/derivation distinction on every public entry page

### Group C: Operational planning surfaces

Patch these files third:

- [RESEARCH_PLAN.md](../RESEARCH_PLAN.md)
- [EXECUTION_CHECKLIST.md](../EXECUTION_CHECKLIST.md)
- [docs/GR_DERIVATION_RESET_PLAN.md](GR_DERIVATION_RESET_PLAN.md)

Planned change:

- add one compact “status line” near the top of each file
- make the current task sentence use “derive the adopted benchmark” language rather than only “go below the current frontier”
- where the file mentions the current `active_primary` frontier, add explicit wording that it is not itself a completed derivation

Expected outcome:

- operational docs stop sounding as if the repo’s identity is the latest frontier label

### Group D: Audit package consistency

Patch this file last if needed:

- [docs/GR_DERIVATION_AUDIT_PACKAGE.md](GR_DERIVATION_AUDIT_PACKAGE.md)

Planned change:

- only make wording conform to the same canonical three-part formula
- do not change audit substance

Expected outcome:

- the audit package, reset plan, and claim-boundary doc use the same short status language

## File-By-File Patch Notes

### `docs/AETHER_FLOW_CLAIM_BOUNDARY.md`

Patch scope:

- add a short `Current Status Formula` section after the canonical claim set

Suggested wording:

- `The benchmark package adopts GR exactly as the operational relativistic sector.`
- `The current line has not yet derived that benchmark from explicit substrate structure.`
- `The live question is whether the current line can derive that adopted benchmark under the five recorded derivation gates.`

### `README.md`

Patch scope:

- strengthen the top summary paragraph
- add one sentence under the current bullet list

Suggested wording:

- keep the existing “GR is adopted exactly” line
- add: `The current derivational line is not yet a derivation of GR; it is the active attempt to determine whether the adopted benchmark can be derived from explicit Æther / Æther-flow structure under the repo’s five-gate standard.`

### `docs/start-here.md`

Patch scope:

- expand the “What You Should Understand First” section by one bullet

Suggested wording:

- `The benchmark package is already the active exact-relativistic theory statement.`
- `The open question is whether the current line can derive that adopted benchmark, not whether the benchmark exists.`

### `docs/theory-package.md`

Patch scope:

- add one sentence below the opening paragraph

Suggested wording:

- `This package is the benchmark in hand; the downstream research line is the active test of whether that adopted benchmark can be derived from explicit substrate structure under the recorded derivation gates.`

### `docs/how-to-review.md`

Patch scope:

- refine the “Core Audits Requested” bullets

Suggested wording:

- replace generic “derivation-program audit” phrasing with:
  - `Derivation-program audit: does the active line stay clear that GR is already adopted in the benchmark package while the open question is whether that adopted benchmark can be derived on the current line?`

### `RESEARCH_PLAN.md`

Patch scope:

- add one short status block immediately under `## Current Objective`

Suggested wording:

- `Benchmark status: GR is adopted exactly in the benchmark package.`
- `Derivational status: the current line has not yet derived that benchmark from explicit substrate structure.`
- `Current question: can the present line derive the adopted benchmark under the five benchmark derivation gates?`

### `EXECUTION_CHECKLIST.md`

Patch scope:

- add one short status block under `## Benchmark Package`
- add one short guard under `## Validation Gate`

Suggested wording:

- `Do not describe the current frontier as if it were already a completed derivation of GR; the active task is to test whether the present line can derive the adopted benchmark.`

### `docs/GR_DERIVATION_RESET_PLAN.md`

Patch scope:

- add one sentence in the `Purpose` or `Reset Principle` section tying the stop-rule directly to the adopted-benchmark language

Suggested wording:

- `The reset assumes a fixed benchmark in hand and asks only whether the current line can derive that adopted benchmark, not whether the benchmark package should be replaced.`

## Patch Rules

The wording patch should follow these limits.

### Keep unchanged

Do not change:

- any Einstein-equation or action-level benchmark statement
- any of the five derivation gates
- the exact-closure package reading order
- the underlying scientific claim that GR is adopted exactly at benchmark scope

### Prefer insertion over rewrite

Where possible:

- add one compact clarifying paragraph or bullet
- do not rewrite whole sections
- do not restyle the documents

### Keep active `.tex` changes optional

This is primarily a repo-facing Markdown patch set.

The front-door `.tex` manuscripts already state the distinction well enough for current purposes. Only patch them later if a second pass shows a real inconsistency.

## Validation Checklist

After applying the wording patch, each target file should answer all three questions clearly.

1. Does it say that GR is adopted exactly in the benchmark package?
2. Does it say that the current line has not yet derived that benchmark?
3. Does it say that the active question is whether the current line can derive the adopted benchmark under the recorded derivation standard?

If a file answers only one or two of those, the wording patch is incomplete.

## Success Condition

The patch is successful if a reader can open any high-level repo-facing page and quickly understand:

- the benchmark package is already scientifically in hand
- the current line is not yet a completed derivation of GR
- the live research question is whether the adopted benchmark can be derived on the current line

That is the full purpose of this wording patch.
