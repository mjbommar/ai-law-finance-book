# LLM Essentials for Law and Finance

**A Practitioner's Guide from Mechanics to Mastery**

*Michael J. Bommarito II, Daniel Martin Katz, Jillian Bommarito*

---

## Overview

This minibook provides a comprehensive guide to understanding and deploying large language models in legal and financial contexts. It covers the foundational knowledge practitioners need before building more sophisticated agentic systems.

**ISBN:** 979-8-9943457-1-9 (Paperback)

## The Practitioner Journey

The book follows a progressive arc from understanding to mastery:

| Chapter | Title | Focus |
|---------|-------|-------|
| 1 | **What Am I Working With?** | Tokens, probabilities, and failure modes |
| 2 | **How Do I Get It to Reason?** | Conversations, context, chain-of-thought |
| 3 | **How Do I Get Reliable Output?** | Structured results, tool calls, audit trails |
| 4 | **How Do I Handle Real Documents?** | Contracts, financials, images, audio |
| 5 | **How Do I Improve Systematically?** | Evaluation, versioning, optimization |

## Build Instructions

### Prerequisites

- TeX Live 2024 or later (with XeLaTeX)
- Biber for bibliography processing
- GNU Make

### Building the PDF

```bash
# Full build (recommended)
make pdf

# Quick single-pass build (for minor edits)
make quick

# Validate references and citations
make validate

# Watch mode (continuous compilation)
make watch

# Clean auxiliary files
make clean

# Clean everything including PDF
make cleanall
```

### Building for Lulu Print-on-Demand

```bash
# Generate interior PDF (strips cover pages)
make interior

# Build cover PDFs
xelatex -output-directory=covers covers/cover-front.tex
xelatex -output-directory=covers covers/cover-back.tex

# Build wrap cover (requires cover PDFs)
xelatex lulu-cover.tex
```

## Directory Structure

```
llm-foundations-law-finance/
├── main.tex                    # Book entry point
├── Makefile                    # Build automation
├── TODO.md                     # Implementation tracking
├── README.md                   # This file
├── lulu-cover.tex              # Wrap cover for print
├── preamble/                   # LaTeX preamble files
│   ├── main.tex
│   ├── packages.tex
│   ├── colors.tex
│   └── ...
├── front-matter/
│   ├── cover/
│   │   ├── cover.tex           # Interior cover page
│   │   ├── front-cover-art.tex # Cover artwork
│   │   └── cover-vars.tex      # Print cover dimensions
│   ├── title-page.tex
│   ├── copyright.tex
│   ├── preface.tex
│   ├── how-to-read.tex
│   └── glossary-entries.tex
├── chapters/
│   ├── 01-llm-mechanics/
│   │   ├── chapter.tex
│   │   └── sections/*.tex
│   ├── 02-conversations-reasoning/
│   │   ├── chapter.tex
│   │   ├── sections/*.tex
│   │   └── figures/*.tex
│   ├── 03-structured-outputs-tools/
│   ├── 04-multimodal/
│   └── 05-prompt-engineering/
├── back-matter/
│   └── back-cover.tex
├── bib/
│   └── refs.bib                # 118 bibliography entries
├── covers/
│   ├── cover-front.tex
│   └── cover-back.tex
├── figures/
│   └── icons/                  # CC license icons
└── scripts/
    └── update_cover_vars.py    # Cover dimension calculator
```

## Relationship to Other Books

This book is the **first volume** in a two-book series:

1. **LLM Essentials for Law and Finance** (this book) — Foundational knowledge for understanding and using LLMs
2. **Agentic AI in Law and Finance** — Advanced patterns for autonomous AI systems

The foundations established here—structured outputs, evidence records, security patterns—scale directly to the agentic architectures covered in the companion volume.

## Content Sources

This minibook extracts and adapts chapters 1-5 from the larger *Artificial Intelligence for Law and Finance* textbook project. The content has been refined for standalone use with:

- Forward references to agentic chapters rewritten to point to the companion volume
- Self-contained glossary of 40+ key LLM terms
- Merged bibliography with 118 unique entries
- Consistent blue/teal visual theme differentiating from the agents book

## Print Specifications

- **Format:** US Trade 6" × 9"
- **Pages:** ~420
- **Binding:** Paperback (perfect bound)
- **Interior:** Black & white with color cover
- **Printer:** Lulu

## License

Content is released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Contact

For questions or feedback, visit [ai4lf.com](https://ai4lf.com).
