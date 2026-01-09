# Agentic AI in Law and Finance

A standalone book on understanding, designing, and governing AI agents for legal and financial applications.

## About This Book

This minibook is a polished, print-ready extraction of Part II (Agents) from the main textbook *Artificial Intelligence for Law and Finance*. It covers the complete agent lifecycle in three chapters:

| Chapter | Title | Main Book Equivalent |
|---------|-------|---------------------|
| 1 | What is an Agent? | Chapter 06 |
| 2 | How to Design an Agent | Chapter 07 |
| 3 | How to Govern an Agent | Chapter 08 |

## Relationship to Main Book

This minibook and the main book's chapters 06-08 share common ancestry but have diverged:

- **This minibook** includes glossary integration, updated statistics (e.g., ABA Opinion 512), and print-ready formatting
- **Main book chapters** are integrated with the broader textbook structure

**Canonical source**: For agent content, this minibook represents the most current version. Changes should be made here first, then synced to the main book as needed.

## Building

### Prerequisites

- TeX Live or equivalent LaTeX distribution
- XeLaTeX (for font support)
- Biber (for bibliography)

### Build Commands

```bash
# Build the interior PDF
make pdf

# Build for Lulu print (with bleed)
make lulu

# Build cover
make cover

# Clean auxiliary files
make clean
```

### Output Files

| File | Description |
|------|-------------|
| `main.pdf` | Interior PDF for reading/review |
| `lulu-interior.pdf` | Print-ready interior (US Trade 6"x9") |
| `lulu-cover.pdf` | Print-ready cover |

## Print Editions

This book is being prepared for publication through Lulu in:
- Paperback (perfect bound)
- Hardcover (case laminate)

## Structure

```
agents-in-law-finance/
├── main.tex              # Book entry point
├── Makefile              # Build automation
├── preamble/             # Shared LaTeX configuration
├── front-matter/         # Title, copyright, preface, TOC
│   ├── cover/
│   ├── title-page.tex
│   ├── copyright.tex
│   ├── preface.tex
│   └── how-to-read.tex
├── chapters/
│   ├── 01-what-is-agent/
│   ├── 02-how-to-design/
│   └── 03-how-to-govern/
├── back-matter/          # Glossary, bibliography, back cover
├── bib/                  # Bibliography database
│   └── refs.bib
├── figures/              # Shared figures and icons
└── covers/               # Cover design options
```

## License

This work is licensed under Creative Commons Attribution 4.0 International License (CC BY 4.0).
