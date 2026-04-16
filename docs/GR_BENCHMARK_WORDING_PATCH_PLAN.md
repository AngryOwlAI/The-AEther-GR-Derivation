# GR Benchmark Wording Patch Plan

Updated: April 16, 2026

Status: Execution checklist for the public-doc and public-bundle repair. This note now tracks the concrete cleanup needed to bring the public navigation surface, the curated `docs/assets/` bundle, and the routing-language control docs back into sync with the current bounded no-go state.

## Current Baseline

The current authoritative status is already fixed elsewhere in the repo:

- the benchmark exact-closure package remains the public front door
- the current frozen primitive-reservoir line now carries the scoped verdict `Not Derived On Current Line`
- any resumed derivational work must begin on a genuinely new line with an explicit observer-localizing law, new primitive variable, or new symmetry principle

Authority for that status comes from:

- [README.md](../README.md)
- [AETHER_FLOW_CLAIM_BOUNDARY.md](AETHER_FLOW_CLAIM_BOUNDARY.md)
- [AETHER_FLOW_NAMING_AND_VOCABULARY.md](AETHER_FLOW_NAMING_AND_VOCABULARY.md)
- [ACTIVE_MANUSCRIPT_FILE_MAP.csv](ACTIVE_MANUSCRIPT_FILE_MAP.csv)
- [RESEARCH_PLAN.md](../RESEARCH_PLAN.md)
- [EXECUTION_CHECKLIST.md](../EXECUTION_CHECKLIST.md)

## Repair Goal

Bring all public-entry docs and the curated public asset bundle into alignment with that bounded no-go routing state without changing the benchmark scientific claim.

## Canonical Public Formula

Use this structure on public-facing repo pages:

- GR is adopted exactly in the benchmark exact-closure package.
- The current frozen primitive-reservoir line now ends in the scoped verdict `Not Derived On Current Line`.
- If derivational work is resumed, the live question becomes whether a genuinely new line can derive the adopted benchmark under the five benchmark derivation gates once it states an explicit observer-localizing law.

## Execution Checklist

### Phase 1: Lock source of truth

- [x] Confirm the current routing state from the file map, claim-boundary note, naming note, README, research plan, and execution checklist.
- [x] Treat the current dirty benchmark `.tex` files in `manuscripts/active/tex/` as the intended worktree source unless explicitly overridden.
- [x] Keep the public cleanup answerable to those sources rather than to stale public prose.

### Phase 2: Repair public navigation docs

- [x] Update [index.md](index.md) so its research-status block no longer advertises the old zepto-section frontier.
- [x] Update [research-archive.md](research-archive.md) so it no longer advertises the old proto-section / pre-proto-section frontier as current.
- [x] Update [start-here.md](start-here.md), [theory-package.md](theory-package.md), and [how-to-review.md](how-to-review.md) so they use the current bounded no-go wording rather than the earlier “current line has not yet derived” wording by itself.
- [x] Update [front-facing-article.md](front-facing-article.md) and [ai-collaboration-and-method.md](ai-collaboration-and-method.md) where needed so they reflect the current bounded verdict and the new-line restart rule.

### Phase 3: Repair public asset bundle

- [x] Compare the curated public `docs/assets/tex/` files against the intended current benchmark-package sources under `manuscripts/active/tex/`.
- [x] Sync any drifted public `.tex` copies to the intended current benchmark-package source state.
- [x] Rebuild the matching public PDFs under `docs/assets/pdfs/` using the tracked build flow rather than manual PDF copying.
- [x] Keep the flagship article, overview, and six benchmark-package modules mutually synchronized in both `.tex` and `.pdf` form.

### Phase 4: Repair related wording-control docs

- [x] Refresh this checklist note so it reflects the current no-go state rather than the pre-no-go “current line can derive” framing.
- [x] Update [GR_RESEARCH_QUESTION_RESET.md](GR_RESEARCH_QUESTION_RESET.md) so it records that the frozen current line has already landed on `Not Derived On Current Line` and that the open question now applies to any resumed genuinely new line.
- [x] Patch any other directly related routing/wording control note only where its current prose still conflicts with the bounded no-go status.

### Phase 5: Validation and hardening

- [x] Re-run a local Markdown link audit across the public docs and key repo-facing summaries.
- [x] Re-check that the curated public bundle exists and is synchronized with the intended source state.
- [x] Run `python3 scripts/validate_active_manuscript_file_map.py` if any active-manuscript routing surface is touched.
- [x] Add a lightweight scripted guardrail so public-bundle drift is easier to catch on later edits.

## Done Condition

This cleanup is complete when:

- no public navigation page advertises the old zepto-section or proto-section frontier as the current live line
- the public docs use the bounded no-go wording consistently
- `docs/assets/tex/` and `docs/assets/pdfs/` are intentionally current
- the public links resolve locally
- the file map and public docs no longer disagree about the current benchmark-facing state
