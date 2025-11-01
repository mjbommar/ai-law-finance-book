# AGENTS.md — Working Guide for "Artificial Intelligence for Law and Finance"

> **⚠️ Note on File Naming**: This file is named `AGENTS.md` because tools like Codex and Gemini require this exact filename for AI assistant guidance. It contains **contribution workflow and standards**, not content about AI agents (which is the book's subject matter found in `chapters/`).

This file directs human and AI assistants contributing to the textbook. It consolidates workflow, evidence standards, file conventions, and LaTeX/build expectations, drawing on the chapter guides under `chapters/`.

## Scope & Intent
- Applies to the entire repository unless a deeper `AGENTS.md` overrides it.
- Objective: a vendor‑neutral, citable, reproducible textbook spanning law and finance.
- Audience: practitioners (law, risk, compliance, markets), regulators, researchers, graduate students.

## Evidence & Source Hierarchy
Prefer primary, dated, link‑stable sources. For time‑sensitive facts (especially after June 2024), verify before inclusion.
- Law/regulation (by authority order):
  - Statutes, regulations, and official reporters (USC/CFR; state codes; EUR‑Lex; court websites).
  - Judicial opinions and orders from official or recognized reporters.
  - Bar/ethics rules and court administrative policies.
  - Regulator guidance and releases (ABA, AOUSC; UK Judiciary; national/state bars).
- Finance/regulators:
  - US: SEC (EDGAR, rule releases), FRB, OCC, FDIC, CFPB, CFTC/FINRA; Treasury/OFAC.
  - International: BIS, FSB, IOSCO, ESMA/EBA/EIOPA, IMF/World Bank, OECD.
  - Accounting: FASB (ASC), IASB/IFRS; auditing: PCAOB; risk: BCBS.
- Research/industry:
  - Peer‑reviewed venues; arXiv from reputable groups; official vendor docs/pressrooms.
  - Avoid tertiary blogs when primary sources exist.

Capture for each citation: title, authors, venue/body, date, stable URL/DOI, and 1–2 line relevance note.

## Writing Rules (musts)
- Follow [`docs/style-guide.md`](docs/style-guide.md) for tone, person/voice, cross‑references (use `\Cref{}`), and terminology.
- Use BibLaTeX with `biber`; include full metadata and `urldate` for web sources.
- Treat rates, thresholds, rules, and release notes as volatile. State effective dates explicitly.
- Paraphrase with citations; use quotes sparingly and only when necessary.
- No client‑confidential, privileged, or regulated (MNPI/inside) data. Redact any accidental inclusion immediately.

## File & Naming Conventions
- Chapters: `chapters/<slug>/` with `main.tex`, `sections/*.tex`, `bib/refs.bib`, `figures/`, `Makefile`.
- Labels: `sec:<slug>-<topic>`, `fig:<slug>-<name>`, `tab:<slug>-<name>`.
- Figures: vector first (PDF/SVG). Names: `fig-<slug>-<name>.pdf`.
- Generated assets: write to `assets/figures/` or `assets/tables/` (planned) with deterministic names.
- Notebooks: place in `notebooks/` and render outputs during builds; do not commit large binary outputs.

## LaTeX & Build Expectations
- Default toolchain: `latexmk` + `biber`. Each chapter must compile with `make pdf`.
- Packages in common preamble: `babel`, `csquotes`, `microtype`, `graphicx`, `booktabs`, `xcolor`, `tcolorbox`, `hyperref`, `cleveref`.
- Cross‑refs: always “Section~`\ref{}`” or `\Cref{}`; never “see above”.
- Before opening a PR: run `make validate`; fix undefined references and citation warnings.

## Legal and Financial Citation Guidance
- Default style: BibLaTeX `authoryear` for academic/industry works.
- Legal sources: include Bluebook elements in BibLaTeX fields (`shorttitle`, `note`, `institution`, `jurisdiction`, `date`, `howpublished`). Prefer footnotes where Bluebook clarity matters. A book appendix will document our field mapping.
- Finance/regulatory: cite the issuing authority, document type (rule/proposal/FAQ), release number, and effective/measurement dates. Provide exhibit/page when applicable.

## AI‑Assisted Workflows (you are reading this as an AI too)
- Verify time‑sensitive facts via search before asserting them. Prefer official domains.
- When summarizing, preserve hedges/limitations from sources. Highlight uncertainties.
- For code/data claims, add minimal runnable artifacts (script or notebook) or clearly mark as conceptual.
- Keep drafts LaTeX‑ready; write section stubs with labels and TODOs rather than leaving placeholders in prose.

## Quality Gates (PR checklist)
- [ ] Compiles without error (`make pdf`), no undefined refs (`make validate`).
- [ ] Conforms to [`docs/style-guide.md`](docs/style-guide.md); consistent person/voice and tense.
- [ ] Claims are cited; time‑sensitive items have dates.
- [ ] Figures/tables labeled, referenced, and captioned; alt text present.
- [ ] No problematic data or licenses; sources have clear reuse rights or are referenced, not embedded.

## Commit Hygiene
- Small, focused changes. Message format: `area: summary (refs #issue)`.
- Do not commit large binaries; prefer vector graphics or scripted generation.
- If adding dependencies or build steps, document them in `README.md` and chapter `Makefile`.

## Open Tasks (initial)
- Create `book/main.tex` and top‑level Makefile that includes compiled chapters.
- Consolidate citations into `book/bib/refs.bib`; add a Bluebook mapping appendix.
- Add CI to compile chapters and the book on PRs; surface `make validate` output.

## Related Guidance Files
- **[CLAUDE.md](CLAUDE.md)** — Quick start guide for AI assistants (Claude Code)
- **[docs/style-guide.md](docs/style-guide.md)** — Comprehensive writing and presentation standards
- **[docs/color-guide.md](docs/color-guide.md)** — Visual design system and semantic color palette
- **[README.md](README.md)** — Project overview and build instructions

_Last updated: October 31, 2025_

