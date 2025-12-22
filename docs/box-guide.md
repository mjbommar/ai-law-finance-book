# Box and Callout Guide

This project uses **semantic boxes**: the *color family* and the *box environment name* carry meaning. Treat boxes as **reader navigation**, not decoration.

## Core Principle: Color = Meaning

- Use the pre-defined environments when possible (`definitionbox`, `keybox`, etc.).
- If you must use raw `tcolorbox` (layout constraints), still use **semantic component colors** (`bg-*`, `border-*`, `text-*`) and keep the same meaning as the corresponding box family.
- Do not “borrow” a color because it looks good; if the color’s semantics do not match, readers get trained wrong.

## Quick Selection (What Each Box Means)

| Box / Color Family | Use For | Avoid Using For |
|---|---|---|
| `definitionbox` (blue) | Formal definitions; crisp criteria; boundary conditions | General explanations; “tips”; long narrative |
| `keybox` (amber/orange) | Must-remember takeaways; decision rules; checklists; “stop here” summaries | Minor points; background; anything you’d be okay with readers skipping |
| `highlightbox` (neutral) | Context; historical notes; optional nuance; “why this matters” asides | Warnings; mandatory requirements; key takeaways |
| `cautionbox` (red) | Pitfalls; failure modes; compliance risks; “don’t do this” patterns | Speculative fears; anything without mitigation; overuse (alarm fatigue) |
| `examplebox` (green) | Worked examples; concrete scenarios; sample artifacts (clauses, workflows) | Abstract claims; “advantages” lists that are not examples |
| `theorembox` (indigo/purple) | Formal propositions; invariants; “if X then Y” claims with assumptions | Informal intuition; purely rhetorical claims |
| `practicebox` (teal) | Exercises; “try it yourself”; implementation tasks with deliverables | Background explanations; warnings without tasks |
| `technicalbox` (indigo) | Optional deep dives; protocol/mechanics detail; implementation caveats | Key takeaways (use `keybox`); exercises (use `practicebox`) |
| `questionbox` (gray/slate) | Self-check questions; review prompts; evaluation rubrics | Answers/solutions as the main content; key takeaways |
| `listingbox` (gray) | Code; configs; prompt templates; policy snippets | Prose paragraphs; “pseudo-code” that is really narrative |

## Box-Writing Rules (Applies to All Boxes)

- **Title is mandatory** for any non-trivial box; use titles that state purpose (e.g., “Key Takeaway”, “Pitfall”, “Example”, “Exercise”).
- **One job per box**: if the box mixes definition + warning + example, split it or convert to prose.
- **Make it skimmable**: short paragraphs, bullets, bolded lead terms, and explicit “So what?” lines.
- **Control density**: target ≤ 1–2 boxes per subsection; avoid 3+ boxes in sequence.
- **Avoid nesting** boxes inside boxes (use headings instead).
- **Don’t fight page breaks**: boxes are `breakable` by default; only set `breakable=false` when the box is short enough to fit.

## Do / Don’t by Color Family

### Blue (`definitionbox`): “This term means…”

**Do**
- Provide a single-sentence definition, then *criteria* or *scope notes*.
- State boundary cases explicitly (“This excludes …”).

**Don’t**
- Turn the box into a mini-essay.
- Put advice or normative claims in the definition (move to `keybox` / prose).

### Amber (`keybox`): “If you remember one thing…”

**Do**
- Use for decision rules, checklists, and executive summaries.
- Make the takeaway falsifiable or testable when possible (“Ask Q1–Q3…”).

**Don’t**
- Use for “nice to know” context.
- Use repeatedly for every numbered point (it dilutes the signal).

### Neutral (`highlightbox`): “Optional context”

**Do**
- Use for historical notes, framing, and “why this matters” nuance.
- Use for brief “Implementation note” / “Further reading” callouts.

**Don’t**
- Hide requirements or warnings here.
- Use to avoid writing transitions in the main prose.

### Red (`cautionbox`): “Risk / Pitfall”

**Do**
- State the risk, then the mitigation (or an escalation rule).
- Prefer concrete triggers (“If X happens, stop and escalate”) over vague fear.

**Don’t**
- Use red for ordinary disagreement or “controversy”.
- Use without an action the reader can take.

### Green (`examplebox`): “Concrete instance”

**Do**
- Use realistic scenarios with enough detail to be instructive (roles, constraints, artifacts).
- Label the example with what it illustrates (“Example: HITL Legal Research”).

**Don’t**
- Use green for generic benefits/marketing language.
- Use green for purely abstract “toy” examples unless you say they are toy.

### Teal (`practicebox`): "Hands-on exercises"

**Do**
- Include "Task", "Deliverable", and (optionally) "Check" criteria.

**Don't**
- Use teal as a catch-all for anything "technical" (pick `definitionbox`, `keybox`, etc., when appropriate).

### Indigo (`theorembox` / `technicalbox`): "Formal or deep dive"

**Do (`theorembox`)**
- State assumptions; define terms; keep the statement tight.
- If giving a proof or justification, separate it clearly (or keep it brief).

**Do (`technicalbox`)**
- Keep it explicitly optional; use for internal mechanics readers can skip safely.

**Don't**
- Use for claims that are really editorial.
- Put key takeaways here (use `keybox`).

### Gray (`questionbox` / `listingbox`): “Utility / tooling”

**Do**
- Use `questionbox` for prompts that force the reader to apply the section.
- Use `listingbox` for code/config/prompt templates and keep line widths reasonable.

**Don’t**
- Put the main argument in gray; it will visually de-emphasize core content.

## When Raw `tcolorbox` Is Acceptable (And How To Do It)

Use raw `tcolorbox` only when you need layout that the standard environments don’t cover:

- Side-by-side comparisons (`minipage`, equal heights)
- Tight “micro-callouts” inside a section opener
- Custom figure-like callouts

Rules:
- Use semantic colors: `colback=bg-*`, `colframe=border-*` (avoid raw primitives like `green-600` in prose boxes).
- Keep border + background in the same family (don’t mix `bg-example` with a slate border unless you have a strong reason).
- If you repeat the same raw `tcolorbox` pattern 3+ times, promote it into a named environment in `preamble.tex`.

