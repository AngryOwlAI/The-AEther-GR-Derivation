# AI Collaboration and Method

[Home](index.md) | [Start Here](start-here.md) | [Theory Package](theory-package.md) | [Active Research](research-archive.md) | [How to Review](how-to-review.md) | [AI Collaboration and Method](ai-collaboration-and-method.md) | [Front-Facing Article](front-facing-article.md)

This repository should be read as an administratively supervised AI research workflow built on Alexander Samuel Ricciardi's originating `Æther / Æther-flow` ontology.

## Provenance

- The original conceptual basis is Ricciardi's `Æther / Æther-flow` ontology.
- The work was developed using the Codex App with GPT-5.4 at Ultra High reasoning effort as the primary researcher and drafter.
- GPT-5.4 carried out the formalization, extension, organization, mathematical exploration, and stress-testing of the manuscript line.
- The human role was administrative and supervisory: managing the prompting pipeline, reusing the same prompt set, and ensuring file generation rather than independently validating the physics content.
- The resulting repository is therefore not a conventional human-authored draft sequence, even though the originating ontology is Ricciardi's.

## What The Collaboration Did

- translated the originating conceptual aims into manuscript structure
- tested candidate formulations and screened weaker branches
- carried out equation-level presentation, prose revision, and package organization
- separated established results, interpretive proposals, and open burdens more explicitly

## What This Collaboration Does Not Mean

- It does not make AI an accountable scientific author.
- It does not remove the need for human expert scrutiny.
- It does not convert speculative steps into established physics merely by volume of drafting or analysis.

## Review Standard

Readers should evaluate the manuscripts by their stated assumptions, explicit equations, logical scope, and honesty about what remains open. The right standard is not whether AI carried out the drafting and research work. The right standard is whether the documents distinguish clearly between adoption, interpretation, derivation, and conjectural continuation.

## Repository Method

- keep the overview-first exact-closure package fixed as the benchmark deliverable
- keep the derivational manuscripts downstream of that benchmark in public presentation even while they become the active research workstream
- treat bounded obstruction / no-go results as valid research outcomes and require any resumed derivational line to state genuinely new observer-localizing structure explicitly
- record negative results and boundary statements rather than smoothing them away
- preserve explicit provenance so collaborators and reviewers can see how the project has been developed
- treat LaTeX/PDF build hygiene as part of the documented workflow: every new or modified `.tex` file should have a regenerated `.pdf` in the matching PDF folder, new `.tex` files should be followed immediately by `scripts/build_aether_pdf.sh path/to/file.tex` or `scripts/build_aether_pdf.sh --missing`, and successful builds should delete the temporary `.aux`, `.log`, and `.out` files

## Related Repository Notes

- [Claim boundary note](AETHER_FLOW_CLAIM_BOUNDARY.md)
- [Naming and vocabulary note](AETHER_FLOW_NAMING_AND_VOCABULARY.md)

If you want the technical audit path next, continue to [How to Review](how-to-review.md).
