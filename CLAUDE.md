# CLAUDE.md — AI Assistant Guide for "Artificial Intelligence for Law and Finance"

> **⚠️ Note on File Naming**: This file is named `CLAUDE.md` because Claude Code requires this exact filename. It contains **AI assistant workflow and quick start guide**, not content about AI agents or Claude (which is the book's subject matter found in `chapters/`).

**Last Updated**: November 1, 2025
**Purpose**: Primary entry point for AI assistants (like Claude Code) working on this textbook project
**Scope**: Entire repository

---

## Quick Start

This repository is a **LaTeX-based textbook project** targeting legal and financial professionals, regulators, and researchers. You are assisting with:

- **Academic rigor** meets **practitioner accessibility**
- **Vendor-neutral** and **citable** content
- **Reproducible** builds with strict quality gates

### Essential Reading Order

1. **THIS FILE (CLAUDE.md)** — Overview and quick reference
2. **[AGENTS.md](AGENTS.md)** — Detailed workflow, evidence standards, and file conventions
3. **[docs/build-guide.md](docs/build-guide.md)** — **Build system guide (dual-compilation)**
4. **[docs/style-guide.md](docs/style-guide.md)** — Writing and presentation standards
5. **[docs/color-guide.md](docs/color-guide.md)** — Visual design system and color usage
6. **[README.md](README.md)** — Project overview for human readers

---

## Core Principles

### 1. Evidence & Source Hierarchy

**Always prefer primary, dated, link-stable sources:**

- **Legal**: Statutes, regulations, official reporters (USC/CFR, EUR-Lex, court websites)
- **Finance**: SEC (EDGAR), FRB, OCC, FDIC, CFTC, FINRA, BIS, FSB, IOSCO
- **Research**: Peer-reviewed venues, reputable arXiv papers, official vendor docs

**For facts after June 2024**: Verify before inclusion. State effective dates explicitly.

See [AGENTS.md](AGENTS.md) for complete evidence hierarchy.

### 2. Writing Standards

**Tone**: Accessible, direct, professional. Blend scholarly rigor with practitioner accessibility.

**Voice patterns**:
- **"we"** for analysis and synthesis (collaborative)
- **"you"** for direct guidance and reader navigation
- **Avoid "I"** entirely (this is collaborative scholarship)
- **Avoid "one"** (archaic and stuffy)

**Citations**: BibLaTeX with `authoryear` style. Always include `urldate` for web sources.

See [docs/style-guide.md](docs/style-guide.md) for comprehensive writing guidelines.

### 3. File & Naming Conventions

**Repository structure**:
```
/
├── CLAUDE.md          # This file — AI assistant entry point
├── AGENTS.md          # Detailed workflow and evidence standards
├── README.md          # Project overview (for humans)
├── docs/
│   ├── style-guide.md # Writing and presentation guide
│   └── color-guide.md # Visual design system
├── main.tex           # Top-level LaTeX document
├── Makefile           # Build system
├── chapters/
│   ├── agentic-primer/
│   │   ├── main.tex
│   │   ├── sections/*.tex
│   │   ├── bib/refs.bib
│   │   ├── figures/
│   │   └── Makefile
│   ├── agents-part-01/
│   └── prompting-and-meta-prompting/
└── scripts/           # Validation scripts
```

**Labels**:
- Sections: `sec:<slug>-<topic>`
- Figures: `fig:<slug>-<name>`
- Tables: `tab:<slug>-<name>`

**Figures**: Vector first (PDF/SVG). Names: `fig-<slug>-<name>.pdf`

See [AGENTS.md](AGENTS.md) for complete file and naming conventions.

---

## LaTeX & Build System

**IMPORTANT**: This project uses a **dual-compilation system** that allows:
- Building individual chapters as standalone PDFs
- Building the complete book with all chapters integrated

**See [docs/build-guide.md](docs/build-guide.md) for comprehensive documentation**

### Toolchain

- **Primary**: `latexmk` + `biber` + `subfiles` package
- **Shared Preamble**: `preamble.tex` contains all formatting, colors, packages
- **4-Layer Color System**: Educational semantic color palette (see [docs/color-guide.md](docs/color-guide.md))
- **Citations**: BibLaTeX with `backend=biber`, style `authoryear`

### Build Commands

**From Root Directory** (build book):
```bash
# Build complete book with all chapters
make book             # or: make pdf

# Build all individual chapter PDFs
make chapters

# Build everything (chapters + book)
make all-pdfs

# Validate references and citations
make validate

# Clean auxiliary files
make clean

# Clean everything including PDFs
make cleanall
```

**From Chapter Directory** (build standalone chapter):
```bash
cd chapters/06-agents-part-1

# Build standalone chapter PDF
make pdf

# Quick single-pass
make quick

# Validate references
make validate

# Clean
make clean
```

### Quality Gates

Before any PR or commit:
- [ ] Compiles without error (`make pdf`)
- [ ] No undefined refs (`make validate`)
- [ ] Conforms to [docs/style-guide.md](docs/style-guide.md)
- [ ] Citations present with dates
- [ ] Figures/tables labeled and referenced
- [ ] No client-confidential or privileged data

See [AGENTS.md](AGENTS.md) for complete quality checklist.

---

## Visual Design System

### Educational Semantic Color Palette

The textbook uses a **4-layer color architecture** for modularity and clarity:

| Type | Color | Use For |
|------|-------|---------|
| **definition** | Blue | Formal definitions, theoretical concepts |
| **example** | Green | Concrete examples, demonstrations |
| **key** | Amber/Orange | Important takeaways, essential points |
| **caution** | Red | Warnings, pitfalls, mistakes |
| **note** | Neutral | Supplementary info, asides |
| **theorem** | Indigo | Formal statements, proofs |
| **practice** | Teal | Exercises, hands-on activities |

**Pattern**: Each type has three variants:
- `[type]-dark` — Text and strong borders
- `[type]-base` — Medium emphasis (accents)
- `[type]-light` — Backgrounds

**Component aliases** for self-documenting code:
- Backgrounds: `bg-definition`, `bg-example`, `bg-key`, etc.
- Borders: `border-definition`, `border-example`, `border-key`, etc.
- Text: `text-primary`, `text-secondary`, `text-muted`

See [docs/color-guide.md](docs/color-guide.md) for complete color system guide and validation checklist.

---

## AI-Assisted Workflows

### Your Role

You are an **AI contributor** helping with:
- Drafting and refining LaTeX content
- Research and citation management
- Code examples and demonstrations
- Quality assurance and validation

### Critical Requirements

1. **Verify time-sensitive facts** via search before asserting them
2. **Preserve hedges/limitations** from sources — highlight uncertainties
3. **Keep drafts LaTeX-ready** — write section stubs with labels, not placeholders
4. **No client-confidential or privileged data** in examples
5. **Always check** [AGENTS.md](AGENTS.md) for evidence hierarchy

### When Drafting Content

**Section structure**:
```latex
\section{Section Title}
\label{sec:slug-topic}

Content here with \keyterm{important terms} highlighted on first use.

Cross-reference with Section~\ref{sec:other} or \Cref{sec:other}.

\parencite{author2020} for citations.
```

**Boxes**:
```latex
% Definition box
\begin{definitionbox}[title={Term}]
  Formal definition here...
\end{definitionbox}

% Key takeaway box
\begin{keybox}[title={Key Point}]
  Essential concept here...
\end{keybox}

% Highlight box (notes, context)
\begin{highlightbox}
  Supplementary information...
\end{highlightbox}
```

### When Researching

**Search strategy**:
1. Identify if topic is law, finance, or research
2. Check evidence hierarchy in [AGENTS.md](AGENTS.md)
3. Prefer official domains and primary sources
4. For web sources: capture title, authors, date, stable URL/DOI, `urldate`
5. Add 1-2 line relevance note for bibliography

**Citation capture**:
```bibtex
@article{author2020,
  author = {Author, First and Author, Second},
  title = {Article Title},
  journal = {Journal Name},
  year = {2020},
  volume = {10},
  number = {2},
  pages = {123--145},
  doi = {10.1000/example},
  url = {https://example.com/article},
  urldate = {2025-10-31},
  note = {Relevance: Establishes key framework for...}
}
```

---

## Common Tasks

### Adding a New Section

1. Create `sections/newsection.tex`
2. Add label: `\label{sec:slug-topic}`
3. Update `main.tex` with `\input{sections/newsection}`
4. Add any new citations to `bib/refs.bib`
5. Run `make validate` to check references
6. Run `make pdf` to verify compilation

### Adding a Figure

1. Create vector graphic (PDF/SVG)
2. Save to `figures/fig-slug-name.pdf`
3. Add to LaTeX:
```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/fig-slug-name.pdf}
  \caption{Descriptive caption with alt text for accessibility}
  \label{fig:slug-name}
\end{figure}
```
4. Reference with: `Figure~\ref{fig:slug-name}` or `\Cref{fig:slug-name}`

### Adding Citations

1. Add BibLaTeX entry to `bib/refs.bib`
2. Include full metadata (authors, year, venue, DOI/URL, `urldate`)
3. Use in text:
   - Parenthetical: `\parencite{author2020}`
   - Narrative: `\textcite{author2020}`
   - With page: `\parencite[p.~42]{author2020}`
4. Run `make pdf` to process with biber

### Validating Your Work

```bash
# Full validation sequence
make clean           # Remove old artifacts
make pdf             # Full compilation
make validate        # Check for undefined refs and citations

# Check for common issues
grep -rn "TODO\|FIXME" sections/    # Find incomplete work
grep -rn "\\cite" sections/          # Verify citations exist in bib
```

---

## Cross-References Between Guidance Files

### When to Consult Each File

**[AGENTS.md](AGENTS.md)** — Read when:
- Starting work on the repository
- Adding research or citations
- Creating new files or chapters
- Need evidence source hierarchy
- Preparing PRs or commits
- Working with legal or financial content

**[docs/build-guide.md](docs/build-guide.md)** — Read when:
- **Setting up or troubleshooting builds**
- **Adding a new chapter**
- Understanding dual-compilation system
- Need to build standalone chapters or complete book
- Debugging LaTeX compilation errors
- Want to understand subfiles package usage
- Need bibliography management guidance

**[docs/style-guide.md](docs/style-guide.md)** — Read when:
- Writing or editing prose
- Choosing tone and voice
- Structuring sections
- Formatting citations
- Creating cross-references
- Using boxes and callouts
- Need writing revision checklist

**[docs/color-guide.md](docs/color-guide.md)** — Read when:
- Creating new tcolorbox definitions
- Choosing colors for visual elements
- Migrating from legacy color names
- Validating color system compliance
- Need color usage examples

**[README.md](README.md)** — Read when:
- Need project overview
- Setting up build environment
- Understanding repository goals
- Contributing guidelines

---

## Commit and PR Guidelines

### Commit Messages

Format: `area: summary (refs #issue)`

Examples:
- `agents-ch01: add historical timeline section (refs #12)`
- `style: update color system to semantic palette`
- `bib: add SEC and FINRA citations for Chapter 3`

### Before Committing

- [ ] Run `make validate` — no undefined references
- [ ] Run `make pdf` — compiles without errors
- [ ] Check [docs/style-guide.md](docs/style-guide.md) compliance
- [ ] Verify citations in `bib/refs.bib`
- [ ] No large binaries (prefer vector graphics)
- [ ] No problematic data or licenses

### Small, Focused Commits

- One logical change per commit
- Don't mix content changes with style/formatting changes
- Document dependencies or build step changes in README.md

---

## Prohibited Content

**NEVER include**:
- Client-confidential information
- Privileged attorney-client material
- Material non-public information (MNPI) or inside information
- Proprietary third-party content without license
- Personal identifying information (PII)
- Large binary files (use scripted generation or external links)

**If you encounter such data**: Redact immediately and notify in commit message.

---

## Quality Standards Summary

### Evidence
✅ Primary sources with dates and stable URLs
✅ Time-sensitive facts verified
✅ Citations include full metadata and `urldate`

### Writing
✅ Tone: accessible yet rigorous
✅ Voice: "we" for analysis, "you" for guidance
✅ Cross-references use `\Cref{}` with labels
✅ Key terms use `\keyterm{}` on first use

### LaTeX
✅ Compiles without errors (`make pdf`)
✅ No undefined references (`make validate`)
✅ No HIGH severity margin violations (`scripts/check_margins.py`)
✅ Semantic color names (not legacy)
✅ Figures labeled, captioned, referenced

### Process
✅ Small, focused commits
✅ Quality gates pass before PR
✅ Build steps documented if changed
✅ No prohibited content

---

## Troubleshooting

### Build Fails

```bash
# Check LaTeX errors
cat main.log | grep -i error

# Common issues
# - Missing biber: install texlive-bibtex-extra biber
# - Undefined refs: run make pdf twice (or use make pdf which runs latexmk)
# - Missing packages: install texlive-latex-extra
```

### Citations Not Appearing

```bash
# Verify bibliography file exists
ls -la bib/refs.bib

# Check for biber errors
biber main 2>&1 | grep -i error

# Ensure citation keys match
grep "cite{" sections/*.tex
grep "@" bib/refs.bib
```

### Color Issues

```bash
# Check for legacy color names
grep -rn "agentblue\|primary-slate\|secondary-sage" .

# See docs/color-guide.md for migration guide
```

---

## Additional Resources

### LaTeX Content Analysis Tools

Python tools for analyzing prose quality, repetition, and structure in LaTeX documents.
Requires `rich` and `typer` — run with `uv run --with rich,typer`.

**`scripts/tex_paragraphs.py`** — Find short/long paragraphs:
```bash
# Find short paragraphs (< 30 words) that may need expansion
uv run --with rich,typer python scripts/tex_paragraphs.py chapters/07-agents-part-2/

# Find long paragraphs (> 150 words) that may need breaking up
uv run --with rich,typer python scripts/tex_paragraphs.py chapters/07-agents-part-2/ --long

# Output as JSON for processing
uv run --with rich,typer python scripts/tex_paragraphs.py chapters/07-agents-part-2/ -f json
```

**`scripts/tex_frequency.py`** — Analyze word/phrase frequencies:
```bash
# Find overused words and phrases
uv run --with rich,typer python scripts/tex_frequency.py chapters/07-agents-part-2/

# Per-file breakdown
uv run --with rich,typer python scripts/tex_frequency.py chapters/07-agents-part-2/ --show-files
```

**`scripts/tex_chunks.py`** — Create sliding-window chunks for LLM review:
```bash
# Create 3-paragraph chunks with 1-paragraph overlap
uv run --with rich,typer python scripts/tex_chunks.py chapters/07-agents-part-2/

# Export as JSONL for processing
uv run --with rich,typer python scripts/tex_chunks.py chapters/07-agents-part-2/ -f jsonl > chunks.jsonl
```

All tools output clickable `file:line` locations and support multiple formats: `table` (default), `json`, `jsonl`, `csv`.

### PDF Margin Checker

**`scripts/check_margins.py`** — Detect content bleeding into PDF margins (overfull hboxes, oversized images):

Requires `pillow`, `pypdfium2`, `numpy`, `rich`, `typer` — run with `uv run --with pillow,pypdfium2,numpy,rich,typer`.

```bash
# Check margins (skip first/last pages as covers, skip top margin for headers)
uv run --with pillow,pypdfium2,numpy,rich,typer python scripts/check_margins.py check main.pdf --no-top

# Generate annotated debug images for specific pages
uv run --with pillow,pypdfium2,numpy,rich,typer python scripts/check_margins.py check main.pdf --debug-pages 38,205 --no-top

# Check with custom margins (inches) - matches LaTeX geometry settings
uv run --with pillow,pypdfium2,numpy,rich,typer python scripts/check_margins.py check main.pdf \
  --inner 0.75 --outer 0.625 --top 0.7 --bottom 0.8 --no-top
```

**Features**:
- Renders PDF pages at configurable DPI and analyzes margin regions for non-white pixels
- Supports twoside documents (inner/outer margins swap on odd/even pages)
- Skip zones for headers, footers, and page numbers
- Severity levels: LOW (<0.5% coverage), MEDIUM (0.5-3%), HIGH (>3%)
- Debug mode generates annotated PNGs with colored boxes showing violations

**Default settings** (US Trade 6"×9" format):
- Page size: 6.0" × 9.0"
- Inner margin: 0.75", Outer margin: 0.625"
- Top margin: 0.7", Bottom margin: 0.8"
- Twoside document: enabled

### Validation Scripts

Located in `scripts/`:
- `check_markdown.sh` — Markdown linting
- `check_latex.sh` — LaTeX validation
- `check_bib.sh` — Bibliography validation
- `check_spelling.sh` — Spell checking
- `check_links.sh` — Link verification
- `run_all.sh` — Run all checks

Usage:
```bash
# Check entire repository
./scripts/run_all.sh .

# Check specific chapter
./scripts/test_chapter.sh chapters/agentic-primer
```

### Docker Builds

For reproducible builds:
```bash
# Using Docker (pulls latex image)
make docker
```

---

## Document Hierarchy

```
CLAUDE.md (THIS FILE)
    ├─→ Quick start and overview
    ├─→ Points to all other guidance files
    └─→ Primary entry point for AI assistants

AGENTS.md
    ├─→ Evidence and source hierarchy
    ├─→ File and naming conventions
    ├─→ LaTeX build expectations
    ├─→ Legal/financial citation guidance
    └─→ Quality gates and PR checklist

docs/build-guide.md ⭐
    ├─→ Dual-compilation architecture (subfiles package)
    ├─→ Build commands and targets
    ├─→ Adding new chapters
    ├─→ Troubleshooting builds
    └─→ Bibliography management

docs/style-guide.md
    ├─→ Tone, voice, and tense
    ├─→ Cross-referencing standards
    ├─→ Terminology and key terms
    ├─→ Section-specific guidelines
    └─→ Revision checklist

docs/color-guide.md
    ├─→ Educational semantic color system
    ├─→ 4-layer architecture
    ├─→ Usage guidelines by content type
    └─→ Validation checklist

README.md
    ├─→ Project goals and audience
    ├─→ Repository layout
    ├─→ Build instructions
    └─→ Contributing guidelines
```

**⭐ Essential reading for build/compilation tasks**

---

## Questions or Issues?

1. **Check the relevant guidance file** using the hierarchy above
2. **Search existing issues** in the repository
3. **Consult validation scripts** in `scripts/`
4. **Run quality checks**: `make validate` and `./scripts/run_all.sh .`

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2025-10-31 | Initial creation, consolidation of guidance files | Claude Code |
| 2025-10-31 | Moved detailed guides to docs/, updated all references | Claude Code |

---

**Remember**: This is scholarly work for practitioners and regulators. Maintain high standards for evidence, citations, and accessibility. When in doubt, consult [AGENTS.md](AGENTS.md) or [docs/style-guide.md](docs/style-guide.md).
