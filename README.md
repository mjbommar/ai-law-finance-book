# Artificial Intelligence for Law and Finance

Status: Working Draft (October 30, 2025)

This repository hosts the evolving textbook “Artificial Intelligence for Law and Finance.” It unifies first‑draft chapters into a coherent, reproducible book with consistent style, citations, build tooling, and quality gates.

Goals
- Build a rigorous, vendor‑neutral, and readable textbook for legal and financial professionals, researchers, and regulators.
- Keep content LaTeX‑ready, well‑cited (BibLaTeX + biber), and reproducible for code/data examples.
- Enforce consistent tone, terminology, and cross‑referencing across chapters.

Audience
- Primary: practitioners (law, compliance, risk, finance), regulators, and graduate students.
- Secondary: industry builders, researchers in AI/ML, law & economics, and information systems.

Guidance Files
This repository uses multiple guidance files for different purposes. **Start with the right file for your role:**

**Root-level entry points:**
- **[CLAUDE.md](CLAUDE.md)** — **Primary entry point for AI assistants** (like Claude Code). Quick start guide with cross-references to all other guidance files, common tasks, and quality standards. *Note: Named CLAUDE.md per tool requirements.*
- **[AGENTS.md](AGENTS.md)** — Detailed workflow for human and AI contributors. Covers evidence hierarchy, source standards, file conventions, LaTeX build expectations, and quality gates. Essential for research and citation work. *Note: Named AGENTS.md per Codex/Gemini requirements.*
- **[README.md](README.md)** — This file. Project overview, build instructions, and getting started guide for human readers.

**Detailed guides in `docs/`:**
- **[docs/style-guide.md](docs/style-guide.md)** — Comprehensive writing and presentation standards. Covers tone, voice, tense, cross-referencing, terminology, section-specific guidelines, and revision checklist. Read before drafting or editing content.
- **[docs/color-guide.md](docs/color-guide.md)** — Visual design system. Educational semantic color palette with 4-layer architecture, usage guidelines, validation checklist, and migration guide from legacy colors.

**Quick guidance selection:**
- Contributing content? → Read [AGENTS.md](AGENTS.md) and [docs/style-guide.md](docs/style-guide.md)
- AI assistant starting work? → Start with [CLAUDE.md](CLAUDE.md)
- Adding visuals or colors? → Read [docs/color-guide.md](docs/color-guide.md)
- Setting up the build? → This file (README.md)

Repository Layout (current and planned)
- `chapters/` — chapter workspaces (drafts) with their own LaTeX and Makefile
  - Example: `chapters/agentic-primer/` with `main.tex`, `sections/`, `bib/refs.bib`, `Makefile`
  - Example: `chapters/prompting-and-meta-prompting/` with executive summaries and citations
- `CLAUDE.md` — AI assistant entry point and quick start guide (required filename for Claude Code)
- `AGENTS.md` — guidance for human and AI contributors (required filename for Codex/Gemini)
- `docs/` — detailed guidance documentation
  - `docs/style-guide.md` — comprehensive writing and presentation standards
  - `docs/color-guide.md` — visual design system and semantic color palette
- `scripts/` — validation scripts (markdown, LaTeX, spelling, links, bibliography)
- Planned top‑level scaffold (added as chapters converge):
  - `book/` — master LaTeX project (`book/main.tex`) that `\include`s chapter PDFs or sources
  - `book/bib/refs.bib` — consolidated bibliography (merged from chapter `bib/refs.bib` files)
  - `assets/` — shared figures (vector first: PDF/SVG); `assets/tables/` for generated tables
  - `code/` — example code used in chapters (language‑specific subfolders)
  - `data/` — small sample datasets; larger data via DataLad/LFS or external links
  - `notebooks/` — Jupyter notebooks that render figures/tables used by the text
  - `scripts/` — helper scripts for linting, builds, and bibliography checks

Build Instructions
- Per‑chapter (today):
  - `cd chapters/agentic-primer && make pdf` (uses `latexmk` if available, falls back to manual)
  - Other helpful targets: `make quick`, `make clean`, `make validate`, `make wordcount`
- Book‑level (planned):
  - `make book` → compiles `book/main.tex` and includes chapter PDFs/sources
  - `make docker` → reproducible build using a LaTeX container with `latexmk` and `biber`

Requirements
- Local: TeX Live with `latexmk`, `biber`, `biblatex`, `csquotes`, `cleveref`, `booktabs`, `tcolorbox`
- Or Docker: a LaTeX image that includes `latexmk` and `biber` (e.g., `ghcr.io/latex-action/latex:latest`)

Writing & Style
- Read `docs/style-guide.md` before drafting. It sets tone, person/voice, cross‑references (`\Cref{}`), labels, figures/tables, and terminology for a law‑finance audience.
- Each chapter keeps its own `bib/refs.bib` during drafting; maintain clean keys and full metadata (authors, year, venue, DOI/URL, `urldate`). Consolidation to `book/bib/refs.bib` happens before integration.

Legal and Financial Citations
- Default: BibLaTeX `authoryear` for academic/industry sources.
- Legal sources (cases, statutes, regulations): include Bluebook‑style information in BibLaTeX entries (`title`, `shorttitle`, `note`, `institution`, `jurisdiction`, `date`); use footnotes where clarity is improved. A harmonized appendix will document mapping from BibLaTeX fields to Bluebook forms.
- Finance/regulatory sources: prefer primary issuers (SEC, FRB, FDIC, OCC, CFTC/ESMA, BIS/FSB, IMF/WB) with stable URLs and release dates.

Reproducibility (code, data, figures)
- Place runnable code in `code/` or `notebooks/`; generate assets into `assets/figures/` or `assets/tables/` with deterministic file names referenced by LaTeX.
- Keep datasets small in‑repo; larger data via LFS or documented external sources with checksums.
- Notebooks should clear outputs in git; CI or `make` regenerates figures/tables.

Quality Gates (definition of done for a section/chapter)
- Compiles without errors; `make validate` shows no undefined references/citations.
- Conforms to `docs/style-guide.md` tone, structure, and cross‑referencing rules.
- Citations present for claims beyond general knowledge; time‑sensitive facts verified.
- Figures/tables labeled, referenced, and have meaningful captions and alt text.
- No client‑confidential, privileged, or proprietary third‑party content without license.

Contributing
- Small, focused commits; message format `area: summary (refs #issue)`.
- Discuss outlines and anchor citations before large drafts; open an issue for new chapters.
- Use `AGENTS.md` when involving AI assistants; always verify time‑sensitive facts and use primary sources.

Disclaimers
- Educational material only; not legal, financial, or investment advice.
- Examples are illustrative; verify local laws, court rules, and regulatory guidance.

Roadmap (near‑term)
- Create `book/main.tex` and top‑level Makefile that includes chapter PDFs/sources.
- Merge chapter bibliographies; add citation style appendix (Bluebook mapping).
- Add `assets/` policy and figure naming scheme; add CI to compile PDFs on PRs.

Local Checks (scripts)
- Run all repo checks: `scripts/run_all.sh .`
- Test a chapter (example): `scripts/test_chapter.sh chapters/agentic-primer`
  - Markdown: markdownlint, Vale, alex (skips if not installed)
  - Spelling: codespell, cspell (skips if not installed)
  - LaTeX: chktex + lacheck (non‑fatal by default) and `make validate`
  - BibTeX: `biber --tool` validation; `bibtex-tidy` if available
  - Links: lychee link checker (skips if not installed)

