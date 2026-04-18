# AI Collaboration and Method

[Home](index.md) | [Start Here](start-here.md) | [Theory Package](theory-package.md) | [Active Research](research-archive.md) | [How to Review](how-to-review.md) | [AI Collaboration and Method](ai-collaboration-and-method.md) | [Front-Facing Article](front-facing-article.md)

This repository should be read as an AI-led, human-scaffolded research experiment built on Alexander Samuel Ricciardi's originating `Æther / Æther-flow` ontology. Its scientific front door remains the exact-GR benchmark package, but the repository also records an experiment in whether GPT-5.4 in Codex can carry out substantial theoretical physics and mathematics research when a human supplies process-level human guidance, tooling, routing, and workflow scaffolding rather than equation-level scientific steering.

## What The Experiment Is Testing

The experiment asks whether GPT-5.4 in Codex can take a human-supplied ontology and research goal and then carry out substantial theoretical physics / mathematics research from there. In this repository, that means formalizing the `Æther` / `Æther-flow` ontology into a disciplined exact-relativistic theory package, testing whether the resulting framework is a viable interpretation of relativity, and tracking the open question of whether GR can be derived from deeper substrate structure rather than merely adopted exactly at observable scale.

The point of the experiment is therefore not only to produce documents. It is also to test whether a model can sustain nontrivial mathematical and physical research over time when the human provides infrastructure, process discipline, and goal-tracking strong enough to keep the work coherent without directly supplying the substantive equation-level results.

## What The AI Did

- carried out most of the drafting, formalization, mathematical exploration, screening, and package-building
- translated the originating ontological aims into manuscript structure, equations, and explicit claim-boundary language
- developed candidate derivation lines, bounded no-go framing, and negative-result handling inside the same repository
- organized the manuscript sequence, package architecture, and supporting prose around the benchmark exact-closure deliverable
- separated established results, interpretive proposals, open burdens, and conjectural continuations more explicitly than a loose draft stream would have done

## What The Human Did

- maintained goal discipline so the repository stayed oriented toward the exact-relativistic package, the open derivation question, and the honest current-line verdict
- supplied process-level human guidance about how the research should be organized and kept on track rather than physics-content answers about what the equations should say
- intervened to prevent drift, recursive loops, and loss of the main project objective
- built and maintained the Manuscript Wiki, CSV routing/control layer, workflow surfaces, and documentation structure that let the agent retrieve, classify, and remember its own work across a large manuscript tree
- kept the repository operational and readable by maintaining the supporting processes, file structure, and routing surfaces needed for sustained research inside Codex

## What The Human Did Not Do

- did not independently validate the physics or mathematics as established results
- did not supply the substantive mathematical derivations as the main scientific drafter
- did not use the AI merely as a transcription layer for already-completed human research
- did not provide equation-level scientific steering as the primary source of the manuscript content

## Autonomy Boundary

This workflow should be described as AI-led and human-scaffolded, not as fully autonomous. GPT-5.4 had broad room to explore, draft, organize, and develop the line of work, but it was not left in unrestricted unsupervised freedom for the entire project.

The autonomy boundary matters because the human role was real but different from direct scientific authorship. The human supplied tooling, routing, workflow scaffolding, and project-level correction when the work risked drifting away from the main goal. In secondary explanatory language, the workflow may be described as semi-autonomous, but that is not the lead framing: the sharper description is that the research was AI-led under human scaffolding and goal-discipline.

## How Readers Should Evaluate The Project

Readers should evaluate the science and the AI methodology separately. The manuscripts should stand or fall on their stated assumptions, explicit equations, logical scope, claim discipline, and honesty about what remains open. The methodology question is different: whether this repository shows that an AI-led, human-scaffolded workflow can produce sustained, nontrivial theoretical physics / mathematics research worth taking seriously as research output.

Criticism of the AI process is therefore valid, but it should not be silently substituted for criticism of the physics itself, and vice versa. A reader may reject the scientific claims while still finding the workflow experiment informative, or may find the scientific package disciplined while remaining skeptical of the broader methodological lesson.

## What This Collaboration Does Not Mean

- It does not make AI an accountable scientific author.
- It does not remove the need for human expert scrutiny.
- It does not convert speculative steps into established physics merely by volume of drafting or analysis.
- It does not mean the human validated the science simply by supervising the workflow.

## Repository Method

- keep the overview-first exact-closure package fixed as the benchmark deliverable
- keep Product B and any future new-line derivational manuscripts downstream of that benchmark in public presentation rather than letting them replace Product A as the front door
- treat bounded obstruction / no-go results as valid research outcomes and require any resumed derivational line to state genuinely new observer-localizing structure explicitly
- record negative results and boundary statements rather than smoothing them away
- preserve explicit provenance so collaborators and reviewers can see both the scientific line and the AI-research experiment that produced the present repository
- treat LaTeX/PDF build hygiene as part of the documented workflow: every new or modified `.tex` file should have a regenerated `.pdf` in the matching PDF folder, new `.tex` files should be followed immediately by `scripts/build_aether_pdf.sh path/to/file.tex` or `scripts/build_aether_pdf.sh --missing`, and successful builds should delete the temporary `.aux`, `.log`, and `.out` files

## Related Repository Notes

- [Claim boundary note](AETHER_FLOW_CLAIM_BOUNDARY.md)
- [Naming and vocabulary note](AETHER_FLOW_NAMING_AND_VOCABULARY.md)
- [How to Review](how-to-review.md)

If you want the technical audit path next, continue to [How to Review](how-to-review.md).
