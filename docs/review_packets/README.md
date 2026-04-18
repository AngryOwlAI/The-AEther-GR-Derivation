# Phase 8 Review Packets

Last updated: April 17, 2026

This folder contains the phase-8 reviewer handoff bundle for `The Æther-Flow Interpretation of Relativity`.
The goal is to let outside reviewers pressure-test the cleaned repository in three distinct ways:

- Packet A: benchmark-package review
- Packet B: current-line no-go review
- Packet C: literature and novelty positioning review

These packets are intentionally separated so a reviewer can audit one layer without being forced to audit the whole repository at once.

## Folder Layout

- [ai/](ai/): Markdown source packets and template for AI-facing or editable documentation.
- [ai_pdfs/](ai_pdfs/): PDF packet copies intended for AI workflows that need PDF-first article links.
- [human/](human/): PDF renderings of the same reviewer packets for human handoff.
- [outgoing/](outgoing/): dated frozen handoff bundles with copied packet assets, authoritative product PDFs, a cover memo, and reviewer-targeted send notes.
- `_ai_pdf_sources/`: internal Markdown build sources used to generate the AI PDF packets with PDF-first article links.
- `_human_sources/`: internal Markdown build sources used to generate the human PDFs with human-specific format priorities.

## Format Priority

- AI Markdown review packets are `LaTeX -> Markdown -> PDF -> other`.
- AI PDF review packets are `PDF -> Markdown -> LaTeX -> other`.
- Human review packets are `PDF -> Markdown -> LaTeX -> other`.

## How To Use This Folder

Send the packet most relevant to the reviewer’s expertise from the `human/` folder, together with the matching AI-side Markdown source when editable text is useful.
Use [ai/response_to_review_template.md](ai/response_to_review_template.md) as the editable response form.

The current dated freeze bundle is:

- [outgoing/2026-04-17/README.md](outgoing/2026-04-17/README.md)

The current live circulation bundle is:

- [outgoing/2026-04-17-live/README.md](outgoing/2026-04-17-live/README.md)

The frozen bundle remains the archival same-day snapshot. The live circulation bundle is the repo-local handoff surface for real outside review:

- Packet A to a GR / foundations reader
- Packet B to a mathematical physicist
- Packet C to an emergence / reconstruction / literature reader

Use the one-page cover memo from that bundle to keep Product A, Product B, and Packet C separated under strict packet discipline.
Treat the simulated packet reviews under `docs/Reviews/` as internal routing evidence only, not as external peer review.

Recommended order if one reviewer is reading the whole project:

1. Product A benchmark package:
   [ai/packet_A_benchmark_package_review.md](ai/packet_A_benchmark_package_review.md),
   [ai_pdfs/packet_A_benchmark_package_review.pdf](ai_pdfs/packet_A_benchmark_package_review.pdf),
   [human/packet_A_benchmark_package_review.pdf](human/packet_A_benchmark_package_review.pdf)
2. Product B current-line no-go:
   [ai/packet_B_current_line_no_go_review.md](ai/packet_B_current_line_no_go_review.md),
   [ai_pdfs/packet_B_current_line_no_go_review.pdf](ai_pdfs/packet_B_current_line_no_go_review.pdf),
   [human/packet_B_current_line_no_go_review.pdf](human/packet_B_current_line_no_go_review.pdf)
3. Packet C literature positioning:
   [ai/packet_C_literature_positioning_review.md](ai/packet_C_literature_positioning_review.md),
   [ai_pdfs/packet_C_literature_positioning_review.pdf](ai_pdfs/packet_C_literature_positioning_review.pdf),
   [human/packet_C_literature_positioning_review.pdf](human/packet_C_literature_positioning_review.pdf)

## Packet List

- [ai/packet_A_benchmark_package_review.md](ai/packet_A_benchmark_package_review.md) and [human/packet_A_benchmark_package_review.pdf](human/packet_A_benchmark_package_review.pdf): review whether the overview-first exact-closure package is coherent, honest, and correctly scoped as the flagship exact-GR result.
- [ai/packet_B_current_line_no_go_review.md](ai/packet_B_current_line_no_go_review.md) and [human/packet_B_current_line_no_go_review.pdf](human/packet_B_current_line_no_go_review.pdf): review whether the frozen primitive-reservoir line is correctly scoped as `Not Derived On Current Line`.
- [ai/packet_C_literature_positioning_review.md](ai/packet_C_literature_positioning_review.md) and [human/packet_C_literature_positioning_review.pdf](human/packet_C_literature_positioning_review.pdf): review whether the project’s literature category and novelty claims are accurate and conservative.
- [ai_pdfs/packet_A_benchmark_package_review.pdf](ai_pdfs/packet_A_benchmark_package_review.pdf), [ai_pdfs/packet_B_current_line_no_go_review.pdf](ai_pdfs/packet_B_current_line_no_go_review.pdf), and [ai_pdfs/packet_C_literature_positioning_review.pdf](ai_pdfs/packet_C_literature_positioning_review.pdf): AI PDF packet copies with article links prioritized in PDF form.
- [ai/response_to_review_template.md](ai/response_to_review_template.md) and [human/response_to_review_template.pdf](human/response_to_review_template.pdf): reusable template for reviewers or internal responses to reviewer feedback.
- [outgoing/2026-04-17/README.md](outgoing/2026-04-17/README.md): frozen same-day archival snapshot retained for reference.
- [outgoing/2026-04-17-live/README.md](outgoing/2026-04-17-live/README.md): live same-day circulation bundle for real outside review.

## Current Repository Status

- Benchmark package: the overview-first exact-closure sequence is the flagship result already in hand.
- Relation to GR: the active project is an exact-GR benchmark and interpretive package, not a low-energy modification or replacement of GR.
- Current-line verdict: the frozen primitive-reservoir line ends in `Not Derived On Current Line`.
- Future derivational status: any reopened derivational ambition would have to be a separate new-line program rather than a continuation of Product B.
- Next admissible move: either stop with that scoped no-go and package the benchmark result already in hand, or open that genuinely new line only after `../NEW_LINE_DERIVATION_CHARTER.md` is completed concretely at equation level.

## Scope Discipline

Use these packets with the repository’s current control surfaces in mind:

- [../AETHER_FLOW_CLAIM_BOUNDARY.md](../AETHER_FLOW_CLAIM_BOUNDARY.md)
- [../PROJECT_IDENTITY_DECISION_NOTE.md](../PROJECT_IDENTITY_DECISION_NOTE.md)
- [../PUBLICATION_ARCHITECTURE.md](../PUBLICATION_ARCHITECTURE.md)
- [../NEW_LINE_DERIVATION_CHARTER.md](../NEW_LINE_DERIVATION_CHARTER.md)

The benchmark package is Product A.
The frozen-line no-go is Product B.
Packet C tests whether that split is being placed honestly in the literature.
Packet C is not a request to reopen the frozen line as if Product B were still a live positive derivation program.
