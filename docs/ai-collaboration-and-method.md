# AI Collaboration and Method

[Home](index.md) | [Start Here](start-here.md) | [Theory Package](theory-package.md) | [Active Research](research-archive.md) | [How to Review](how-to-review.md) | [AI Collaboration and Method](ai-collaboration-and-method.md) | [Front-Facing Article](front-facing-article.md)

This repository should be read as AI-assisted theoretical research carried out under sustained human direction.

## Provenance

- The research is led by Alexander Samuel Ricciardi.
- The original conceptual basis is Ricciardi's `Æther / Æther-flow` ontology.
- The work was developed using the Codex App with GPT-5.4 at Ultra High reasoning effort.
- GPT-5.4 assisted with drafting, mathematical exploration, branch screening, organization, and revision under Ricciardi's direction.
- The resulting repository is therefore neither purely solo-human drafting nor an autonomous AI product.

## What The Collaboration Did

- translated conceptual aims into manuscript structure
- helped test candidate formulations and screen weaker branches
- assisted with equation-level presentation, prose revision, and package organization
- helped separate established results, interpretive proposals, and open burdens more explicitly

## What This Collaboration Does Not Mean

- It does not make AI an accountable scientific author.
- It does not remove the need for human expert scrutiny.
- It does not convert speculative steps into established physics merely by volume of drafting or analysis.

## Review Standard

Readers should evaluate the manuscripts by their stated assumptions, explicit equations, logical scope, and honesty about what remains open. The right standard is not whether AI participated. The right standard is whether the documents distinguish clearly between adoption, interpretation, derivation, and conjectural continuation.

## Repository Method

- keep the overview-first exact-closure package fixed as the benchmark deliverable
- keep the derivational manuscripts downstream of that benchmark in public presentation even while they become the active research workstream
- record negative results and boundary statements rather than smoothing them away
- preserve explicit provenance so collaborators and reviewers can see how the project has been developed
- treat LaTeX/PDF build hygiene as part of the documented workflow: every new or modified `.tex` file should have a regenerated `.pdf` in the matching PDF folder, new `.tex` files should be followed immediately by `scripts/build_aether_pdf.sh path/to/file.tex` or `scripts/build_aether_pdf.sh --missing`, and successful builds should delete the temporary `.aux`, `.log`, and `.out` files

## Related Repository Notes

- [Claim boundary note](AETHER_FLOW_CLAIM_BOUNDARY.md)
- [Naming and vocabulary note](AETHER_FLOW_NAMING_AND_VOCABULARY.md)

If you want the technical audit path next, continue to [How to Review](how-to-review.md).
