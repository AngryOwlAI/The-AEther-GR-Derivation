# Implementation Plan for the Research AI Agent
## The Æther-Flow Interpretation of Relativity

## 1. Mission

Implement a project-wide reframing that makes the repository scientifically cleaner, more defensible, and more publishable **without changing the benchmark claim boundary**.

### Recommended primary goal
Keep the project centered on:

> **The Æther-Flow Interpretation of Relativity as an exact-GR benchmark package at observable scales, plus a separate foundational research program testing whether that benchmark can be derived from deeper substrate structure on a genuinely new line.**

### Recommended non-goal
Do **not** change the project’s main goal to:
- a low-energy modification of GR,
- a replacement for GR,
- or a claim that the current substrate line already derives GR.

### Optional future branch
If non-GR modifications are ever explored, treat them as a **separate project/branch with a separate claim boundary**, not as the continuation of the current benchmark package.

---

## 2. Executive diagnosis to implement

The repo already contains the right core scientific stance, but it is not yet fully harmonized across all public-facing surfaces.

### What is already correct and should be preserved
- The benchmark package is the public flagship.
- GR is adopted exactly at benchmark level.
- Observable low-energy content is exactly GR.
- The current frozen line now carries the verdict `Not Derived On Current Line`.
- Any resumed derivational work must begin with a genuinely new observer-localizing law, new primitive variable, or new symmetry principle.

### What must be fixed
- Some docs still speak as if **the present line might still derive GR**, instead of recognizing that the current line has already failed on its own frozen assumptions.
- At least one public research-routing page still promotes the older deeper-relay frontier as the “current primary burden,” which is no longer consistent with the no-go / obstruction framing.
- The repository title/subtitle still leans too hard on “GR Derivation,” which risks overstating the status.
- The literature-positioning layer is too weak.
- The benchmark package and the negative-result line should be separated more cleanly into distinct publishable outputs.
- The research-control documents need pruning and harmonization.

---

## 3. Non-negotiable working rules for the agent

The agent must obey these rules in every edit.

1. **Do not move the benchmark claim boundary.**
   - The benchmark package remains exact GR at observer level.
   - Do not introduce a second operative metric.
   - Do not enlarge the low-energy matter law.
   - Do not imply a distinct low-energy signature unless a separate project is intentionally opened.

2. **Do not present adoption as derivation.**
   - “Adoption” = exact GR benchmark package.
   - “Derivation” = first-principles recovery from explicit substrate structure.

3. **Do not reopen the frozen line as if more depth alone could save it.**
   - Another deeper same-output relay below the same frozen object is not progress.
   - The old line is either historical/supporting context or a bounded no-go record.

4. **Do not claim a new theory of gravity unless the project intentionally leaves the benchmark package and is renamed/re-scoped accordingly.**

5. **Use active `.tex` manuscripts as scientific authority.**
   - Use the file map and routing docs before broad searching.
   - Rebuild PDFs after `.tex` edits.
   - Update and validate the active manuscript file map after active-manuscript changes.

---

## 4. Immediate contradictions and cleanup targets

These are the first things to fix because they create project-level confusion.

### A. README/title mismatch
The README already says the benchmark package is the flagship and the current frozen line is `Not Derived On Current Line`, but the repo title still contains `GR Derivation`. That should be softened or qualified.

### B. “Present line can derive” wording is stale in multiple docs
Update any wording that says the active question is whether the **present line** can derive the benchmark. That is no longer accurate once the current line has been frozen with a scoped no-go verdict.

Priority files to inspect and likely edit:
- `docs/start-here.md`
- `docs/theory-package.md`
- `docs/how-to-review.md`
- `EXECUTION_CHECKLIST.md`

### C. `docs/research-archive.md` appears stale
This page still routes readers to the older pre-proto-section frontier as if that were the live current burden. That is incompatible with the newer “current-line obstruction / no-go” framing and must be rewritten.

### D. `RESEARCH_PLAN.md` needs pruning
It says it is “intentionally short,” but it also contains a very long historical checked-task ledger. Split current-control content from archival history.

---

## 5. Target end state

After implementation, the repository should read as follows:

### Publicly
- The project’s flagship result is an exact-GR interpretive/benchmark package.
- The current derivation attempt has ended in a scoped no-go on the frozen line.
- Any resumed derivation work must start on a genuinely new line with new localizing structure.
- The project is **not** currently a modification or replacement of GR.

### Internally
- Routing docs, control docs, and manuscript metadata all agree on the same status.
- Historical deeper-relay material is retained but not misrepresented as the live frontier.
- The benchmark package is publishable as one coherent exact-GR interpretive statement.
- The no-go result is publishable as a separate bounded negative result.
- Any new derivation line must pass a pre-registered design charter before being promoted.

---

## 6. Phase-by-phase implementation plan

## Phase 0 — Establish the baseline and freeze the scientific status

### Objective
Create a single authoritative internal status memo before editing anything.

### Tasks
- Read, in order:
  1. `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`
  2. `docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md`
  3. `README.md`
  4. `docs/AETHER_FLOW_CLAIM_BOUNDARY.md`
  5. `docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md`
  6. `RESEARCH_PLAN.md`
  7. `EXECUTION_CHECKLIST.md`
  8. `docs/start-here.md`
  9. `docs/theory-package.md`
  10. `docs/front-facing-article.md`
  11. `docs/research-archive.md`
  12. `docs/how-to-review.md`
  13. `manuscripts/active/tex/aether_flow_exact_closure_sequence_overview.tex`
  14. `manuscripts/active/tex/aether_flow_exact_closure_derivation_gates_note.tex`
  15. `manuscripts/active/tex/aether_flow_current_line_gr_derivation_obstruction_or_no_go.tex`

- Produce an internal memo named something like:
  - `docs/_archived_plans/2026-04-status-baseline.md`
  - or another archived planning location consistent with repo rules.

### Memo contents
- Current benchmark claim boundary.
- Current derivational verdict.
- Exact wording of the recommended primary goal.
- Explicit list of stale or contradictory files.
- Which files are authoritative vs routing-only vs historical.
- Which old chain/frontier descriptions must no longer be treated as live.

### Deliverable
A one-document “status baseline” that the rest of the implementation follows.

### Acceptance test
No work proceeds until the baseline memo answers these five questions unambiguously:
1. What is the flagship result?
2. Is the current line a derivation success?
3. What remains open?
4. What would count as a legitimate new main line?
5. What does **not** count as progress anymore?

---

## Phase 1 — Reframe the public-facing mission without changing the benchmark

### Objective
Make every high-visibility public surface say the same thing.

### Core message to implement
Use this or a very close variant everywhere:

> The flagship result of the repository is the exact-GR benchmark package, `The Æther-Flow Interpretation of Relativity`, which adopts GR exactly at observable scales. The current frozen substrate line does **not** derive that benchmark and is now scoped as `Not Derived On Current Line`. Any resumed derivational work must begin on a genuinely new line with an explicit observer-localizing law, new primitive variable, or new symmetry principle.

### Files to edit
- `README.md`
- `docs/start-here.md`
- `docs/theory-package.md`
- `docs/front-facing-article.md`
- `docs/research-archive.md`
- `docs/how-to-review.md`
- `docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md`
- `EXECUTION_CHECKLIST.md`
- `RESEARCH_PLAN.md` (current-control portion)

### Specific edit instructions
#### `README.md`
- Change the top-level presentation so it does not imply a completed GR derivation.
- Preferred options:
  - Rename heading to `The Æther-Flow Interpretation of Relativity`
  - Or use a subtitle such as `Exact-GR Benchmark and Substrate Research Program`
- Keep the current positive benchmark language.
- Add a compact status box with:
  - benchmark status,
  - current-line status,
  - next admissible research move.

#### `docs/start-here.md`
- Replace “whether the present line can derive…” with “whether a genuinely new line can derive…”
- Add a one-sentence statement that the current frozen line has already been answered negatively.

#### `docs/theory-package.md`
- Same cleanup as above.
- Make clear that downstream derivational work is no longer about testing the same frozen line.

#### `docs/front-facing-article.md`
- Keep it as accessibility layer.
- Replace any language that sounds like an active, ongoing, same-line GR derivation with:
  - “open foundational derivation program,”
  - or “open substrate-derivation program,”
  - or “future new-line derivation program.”

#### `docs/research-archive.md`
- Rewrite heavily.
- Remove the stale routing that still promotes the old deeper pre-proto-section frontier as the live next move.
- Replace with a compact three-part structure:
  1. what was achieved on the frozen line,
  2. why that line is now scoped as `Not Derived On Current Line`,
  3. what a genuinely new line would have to add before promotion.

#### `docs/how-to-review.md`
- Update reviewer prompts so they ask:
  - whether the benchmark package is coherent and honest,
  - whether the no-go framing is justified,
  - whether any proposed new line actually adds new localizing structure.

#### `EXECUTION_CHECKLIST.md`
- Replace “determine whether the present line can derive…” with wording consistent with the frozen-line verdict and new-line requirement.

#### `RESEARCH_PLAN.md`
- Leave only genuinely current control items in the active file.
- Move the giant completed-task ledger into an archive file.
- Keep `RESEARCH_PLAN.md` truly short and live.

### Deliverables
- Harmonized public docs.
- Short status box template reused across surfaces.
- Archived historical plan file(s).

### Acceptance test
A reader who lands on **any** public entry document should get the same answers to:
- What the project is.
- Whether GR is adopted or derived.
- Whether the current line succeeded.
- Whether the project is a modification/replacement of GR.
- What the next legitimate step is.

---

## Phase 2 — Consolidate the benchmark package as the flagship scientific product

### Objective
Treat the exact-GR package as a standalone scientific deliverable.

### Files in scope
- `aether_flow_exact_closure_sequence_overview.tex`
- `aether_flow_exact_closure_note.tex`
- `aether_flow_foundations.tex`
- `aether_flow_dynamics.tex`
- `aether_flow_consistency.tex`
- `aether_flow_relativistic_recovery.tex`
- `aether_flow_geometry.tex`
- `aether_flow_exact_closure_flagship_article.tex`

### Tasks
- Audit all flagship-package intros and conclusions for identical claim discipline.
- Ensure each manuscript states:
  - what it establishes,
  - what it does not establish,
  - how it fits the benchmark package.
- Add or standardize a “nonclaims” paragraph where needed.
- Add a compact benchmark-claim matrix (internal doc or appendix) listing:
  - manuscript,
  - role,
  - positive claim,
  - explicit nonclaim,
  - benchmark relevance.

### Benchmark consistency checks
The agent must verify that every flagship manuscript preserves:
- one operative metric,
- universal matter coupling,
- exact GR observer-level dynamics,
- no independent low-energy non-GR sector,
- interpretation not deformation,
- adoption/derivation distinction.

### Editorial improvements
- Make the flow-geometry manuscript visibly an interpretive/congruence dictionary, not a second dynamics paper.
- Use consistent language for:
  - Æther,
  - Æther-flow,
  - observed three-dimensional space,
  - S-time,
  - exact closure,
  - adoption,
  - derivation.

### Deliverables
- Clean benchmark package.
- Benchmark claim matrix.
- Rebuilt PDFs for all touched manuscripts.

### Acceptance test
A technically literate reader should be able to read the benchmark package **without reading the derivational archive** and correctly conclude:
- the package is exact GR at observable level,
- the ontology is interpretive at that level,
- no completed substrate derivation is being claimed.

---

## Phase 3 — Package the negative result cleanly and stop recursive depth drift

### Objective
Turn the failed current line into a rigorous, bounded, reusable result rather than a muddled research frontier.

### Core rule
The frozen line must now function as a **documented obstruction/no-go**, not as an invitation to continue descending by same-output relay.

### Files in scope
- `aether_flow_current_line_gr_derivation_obstruction_or_no_go.tex`
- `aether_flow_exact_closure_derivation_gates_note.tex`
- `aether_flow_bounded_gr_derivation_bridge_object_synthesis.tex`
- supporting bridge-entry / continuity-Hessian files
- file map / routing docs

### Tasks
- Make the no-go note the canonical downstream status document.
- Add a short plain-language summary section if one is missing.
- Create an internal or public-facing “current-line audit summary” document that answers:
  - what the frozen bridge object contains,
  - what it does **not** contain,
  - which derivation gates remain unmet,
  - why same-output deeper relays no longer count as progress.

### Required argument to make explicit
The current line fails not merely because it is incomplete, but because it lacks:
- an observer-localization law,
- a local map from substrate variables to observer spacetime fields,
- a derived operative metric law,
- derived local curvature/null/proper-time/redshift structure.

### Reclassification tasks
- Reclassify older same-output deeper-relay manuscripts as:
  - historical,
  - supporting context,
  - or side work,
  not as the live frontier.
- Ensure the file map reflects this.

### Stop rules to write down explicitly
A manuscript does **not** count as new main-line progress if it:
- preserves the same benchmark outputs,
- preserves the same continuity-Hessian compressed core,
- only moves the unexplained substrate layer deeper,
- does not discharge a benchmark gate,
- does not add a genuinely new observer-localizing ingredient,
- does not produce a bounded yes/no/conditional verdict.

### Deliverables
- Canonical no-go/downstream status page.
- Current-line audit summary.
- Updated file map and routing metadata.

### Acceptance test
No active document should imply that “the next honest move” is merely another deeper same-output relay inside the old frozen line.

---

## Phase 4 — Repair the literature and novelty positioning

### Objective
Place the project in existing gravitational/emergent-gravity literature so the novelty claim becomes precise and defensible.

### Why this phase matters
Without direct positioning, the benchmark package risks reading like a private relabeling of standard GR, and the derivation program risks reading like it is rediscovering known emergent-gravity ambitions without comparison.

### Required comparison targets
At minimum, compare against:
1. **Standard GR with interpretive language**
2. **Einstein-æther theory**
3. **Emergent/thermodynamic derivations of Einstein gravity**
4. **Induced gravity / Sakharov-style emergence**
5. Any other directly relevant emergent-spacetime or preferred-frame literature the agent identifies

### Required comparison questions
For each comparison target, answer:
- What does that framework actually claim?
- Does it modify low-energy gravity or not?
- Does it introduce additional observer-level fields or modes?
- Is the present project doing the same thing, a weaker thing, or a different thing?
- What is genuinely novel here:
  - ontology?
  - benchmark packaging?
  - derivational architecture?
  - negative-result discipline?
  - or nothing beyond reframing?

### Output artifact
Create a literature-positioning matrix with columns:
- framework,
- low-energy content,
- extra fields/modes,
- relation to GR,
- relation to the Æther-Flow benchmark,
- key overlap,
- key difference,
- implication for project claims.

### Editing tasks
- Add a Related Work / Literature Positioning section to:
  - `aether_flow_exact_closure_flagship_article.tex`
  - optionally `aether_flow_exact_closure_sequence_overview.tex`
  - optionally a dedicated new note such as `aether_flow_literature_positioning_note.tex`

### Minimum comparison conclusions the agent should be prepared to write
- This project is **not** Einstein-æther theory if it does not claim a surviving low-energy dynamical preferred-frame field.
- This project is closer to an **exact-GR interpretive package plus an emergent-gravity research program** than to a completed alternative theory of gravity.
- Any derivational ambition should be framed in relation to established emergent-gravity programs, not as if the conceptual category were unprecedented.

### Deliverables
- Literature matrix.
- Added citations and related-work sections.
- Revised novelty statement.

### Acceptance test
A skeptical reviewer should be able to tell, quickly and accurately:
- what the project is not,
- what it is trying to do,
- where it overlaps with known frameworks,
- and where its actual novelty, if any, resides.

---

## Phase 5 — Split the project into clean publishable outputs

### Objective
Separate the stable result from the failed derivation attempt.

### Recommended publication architecture

#### Paper/Product A — Benchmark package paper
**Purpose:** Present the exact-GR interpretive package as the flagship result.

**Core claim:**
The Æther-Flow framework provides an exact-GR benchmark interpretation with ontology/flow/congruence language, while making no claim of completed substrate derivation or low-energy deviation from GR.

**Suggested ingredients:**
- overview
- exact-closure note
- core package condensation
- claim boundary
- related-work section
- nonclaims section

#### Paper/Product B — Current-line no-go paper
**Purpose:** Present the bounded obstruction result on the frozen line.

**Core claim:**
The current primitive-reservoir/frozen-bridge line does not derive the benchmark because it lacks the observer-localizing structure needed to discharge the relevant derivation gates.

**Suggested ingredients:**
- derivation gates recap
- frozen bridge object summary
- exact missing ingredient
- no-go statement
- what remains open
- what would count as a new line

#### Optional Paper/Product C — New-line derivation charter / literature position note
Only if needed.

### Tasks
- Write abstracts for A and B.
- Produce one-paragraph “claim boundary” statements for each.
- Remove cross-talk that causes Product A to look like Product B in disguise.
- Ensure Product B does not demote Product A.

### Deliverables
- Two explicit product outlines.
- Abstracts and section structures.
- File mapping from current manuscripts to product bundles.

### Acceptance test
A reader can reject the derivation program while still understanding exactly what the benchmark package claims and does not claim.

---

## Phase 6 — Design the only acceptable kind of resumed derivation program

### Objective
Create a hard gate that prevents the project from re-entering recursive depth drift.

### Rule
Do **not** open a new derivation line unless the agent can write a **New-Line Design Charter** first.

### Required charter fields
Create a document such as:
- `docs/new_line_derivation_charter.md`
- or `manuscripts/active/tex/aether_flow_new_line_derivation_charter.tex`

It must include:

1. **New ingredient**
   - explicit observer-localizing law, or
   - new primitive variable, or
   - new symmetry principle.

2. **Local observer map**
   - How do substrate variables generate local observer spacetime fields?
   - What is the mathematical map?
   - What counts as locality?

3. **Operative metric generation**
   - How does the single operative metric arise?
   - Is it derived or merely posited?

4. **Observer dynamics**
   - How do Einsteinian dynamics arise?
   - If an Einstein-Hilbert term is inserted by hand, the line is an ansatz, not a derivation.

5. **Gauge/mode control**
   - Why are only GR-compatible low-energy observer modes left?
   - What happens to extra scalar/vector sectors?

6. **Relativistic recovery**
   - How do null cones, proper time, and redshift arise from the same metric?

7. **Remainder audit**
   - What prevents a genuine observer-side remainder?

8. **Failure conditions**
   - What result would count as:
     - `Derived`
     - `Not Derived On Current Line`
     - `Suspended Pending New Law`

### Mandatory pre-screen questions
The new line may proceed only if all of the following can be answered concretely:
- What is the new localizing structure?
- What exact mathematical object maps substrate data to spacetime fields?
- How is the metric generated, not merely inherited?
- What prevents extra unsuppressed low-energy sectors?
- Why is this not just another same-output relay?

### Additional technical rule
A new line must **not** rely on any of the following while calling itself a derivation:
- direct insertion of an Einstein-Hilbert term without a derivational account,
- use of a preserved observer metric as if that were generated output,
- exact closure only on a tuned/degenerate locus,
- unresolved extra low-energy observer sectors,
- a missing local curvature-generating law.

### Deliverables
- New-Line Design Charter.
- Gate-by-gate success/failure checklist.
- Short go/no-go recommendation at the end of the charter.

### Acceptance test
If the charter cannot be written concretely, do **not** open a new derivation line.

---

## Phase 7 — Decide explicitly whether to keep exact GR, modify GR, or replace GR

### Recommended answer
Keep **exact GR** as the project’s main benchmark and public scientific identity.

### Decision rule
#### Default path
- **Keep exact GR.**
- Treat the framework as an exact-GR interpretive package + open derivation program.

#### Deferred path
- **Do not modify GR within the current flagship project.**

#### Separate-project path
Open a GR-modification or GR-replacement branch **only if** all of the following are true:
- the benchmark package is intentionally abandoned or demoted,
- the new project states explicit low-energy deviations,
- it identifies observable consequences,
- it accepts the burden of current observational/theoretical constraints,
- it is renamed/re-scoped as a different project.

### Tasks
- Write a short “project identity decision note” answering:
  - Why exact GR remains the correct benchmark.
  - Why low-energy modification/replacement is not the current goal.
  - Under what conditions a separate non-GR project could be opened later.

### Deliverable
A one-page decision note.

### Acceptance test
There is no ambiguity left about whether the project is:
- an exact-GR interpretation,
- a new low-energy gravity theory,
- or a separate future speculative branch.

---

## Phase 8 — Expert review and red-team pass

### Objective
Subject the cleaned project to external technical pressure.

### Why this is mandatory
Because the repo’s own provenance note says the work was primarily AI-developed with human supervision, external expert scrutiny is essential before scientific confidence is increased.

### Reviewer packets to assemble
#### Packet A — Benchmark package review
Ask reviewers:
- Is the benchmark package internally coherent?
- Is it scientifically honest?
- Is it anything more than GR plus ontology?
- Where is the novelty real vs verbal?

#### Packet B — No-go review
Ask reviewers:
- Is the no-go theorem actually scoped correctly?
- Does it really justify `Not Derived On Current Line`?
- Are any hidden escape routes still inside the same frozen line?

#### Packet C — Literature review
Ask reviewers:
- What prior work must be cited directly?
- Is the Einstein-æther / emergent-gravity positioning accurate?
- Is any claimed novelty overstated?

### Deliverables
- Reviewer question lists.
- Review packet bundle.
- Response-to-review note.

### Acceptance test
Feedback is incorporated into:
- claim boundary,
- literature positioning,
- naming,
- no-go framing,
- and any decision to open or not open a new line.

---

## 7. File-by-file change list

Use this as the actual execution checklist.

## Top-priority files
- [ ] `README.md`
- [ ] `docs/start-here.md`
- [ ] `docs/theory-package.md`
- [ ] `docs/research-archive.md`
- [ ] `docs/how-to-review.md`
- [ ] `docs/front-facing-article.md`
- [ ] `docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md`
- [ ] `RESEARCH_PLAN.md`
- [ ] `EXECUTION_CHECKLIST.md`
- [ ] `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`

## Benchmark manuscripts
- [ ] `aether_flow_exact_closure_sequence_overview.tex`
- [ ] `aether_flow_exact_closure_note.tex`
- [ ] `aether_flow_foundations.tex`
- [ ] `aether_flow_dynamics.tex`
- [ ] `aether_flow_consistency.tex`
- [ ] `aether_flow_relativistic_recovery.tex`
- [ ] `aether_flow_geometry.tex`
- [ ] `aether_flow_exact_closure_flagship_article.tex`

## Downstream/no-go manuscripts
- [ ] `aether_flow_exact_closure_derivation_gates_note.tex`
- [ ] `aether_flow_current_line_gr_derivation_obstruction_or_no_go.tex`
- [ ] `aether_flow_bounded_gr_derivation_bridge_object_synthesis.tex`

## Historical/supporting candidate-derivation manuscripts to reclassify and annotate
- [ ] `aether_flow_substrate_kinematics.tex`
- [ ] `aether_flow_substrate_linearized_consistency.tex`
- [ ] `aether_flow_substrate_minimal_stable_sign_no_go.tex`
- [ ] direct bridge-entry / continuity-Hessian support files as needed

---

## 8. Research-agent reporting format

After each phase, the agent should report back in this exact structure:

### Phase report
- **Phase completed:**  
- **Files changed:**  
- **Build status:**  
- **File-map validation status:**  
- **What is now clearer than before:**  
- **Any remaining contradiction:**  
- **Did the benchmark claim boundary change?** (must be `No`)  
- **Did any task accidentally imply GR modification/replacement?**  
- **What is the next admissible task?**  

---

## 9. Hard stop conditions

The agent must stop and report rather than keep descending if any of the following occurs:
- It cannot state a new observer-localizing law concretely.
- It finds itself only pushing the same unexplained structure deeper.
- It relies on a preserved observer metric instead of deriving one.
- It inserts Einsteinian dynamics by hand and starts calling that a derivation.
- It obtains closure only on a degenerate/tuned locus.
- It identifies a possible low-energy deviation from GR but cannot cleanly separate that into a new project.

---

## 10. Final recommended project identity statement

Use this as the final destination wording unless a deliberate later decision changes it:

> **The Æther-Flow Interpretation of Relativity** is an exact-GR benchmark package built on the Æther / Æther-flow ontology. At observable scales it adopts GR exactly and does not currently claim an independent low-energy non-GR sector. The current frozen substrate line does not derive that benchmark and is now scoped as `Not Derived On Current Line`. Any resumed derivational work must begin on a genuinely new line with an explicit observer-localizing law, new primitive variable, or new symmetry principle. Modification or replacement of GR is not the current project goal.

---

## 11. Most important implementation priorities in plain language

If the agent does nothing else, it must do these five things first:

1. Harmonize all public docs to the same current status.
2. Stop treating the old deeper-relay line as the live frontier.
3. Present the exact-GR benchmark package as the flagship result.
4. Package the current line as a bounded no-go / obstruction result.
5. Add serious literature positioning before making stronger novelty claims.

---

## 12. Bottom-line recommendation to the research AI agent

Do **not** steer the project toward “modify GR” or “replace GR” as the current main line.

Instead:
- **stabilize the benchmark exact-GR interpretation,**
- **publish the negative result honestly,**
- **repair the literature positioning,**
- and **only then** decide whether a genuinely new derivational line can even be stated.

If no concrete new observer-localizing law can be written, the correct scientific action is not to keep digging. It is to stop with the benchmark package and the bounded no-go.