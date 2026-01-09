# Book Reorganization Plan

## Goals
1. Single LaTeX compiler (XeLaTeX) for entire book
2. Single Makefile - no separate cover compilation
3. Zero PDF includes - everything compiled together
4. Consistent, clean folder structure
5. Easy to understand and maintain

## Target Directory Structure

```
agents-in-law-finance/
├── Makefile                    # Single build system
├── main.tex                    # Master document
│
├── preamble/                   # Split preamble for clarity
│   ├── main.tex               # Includes all preamble components
│   ├── packages.tex           # Package loading
│   ├── geometry.tex           # Page geometry setup
│   ├── colors.tex             # ALL color definitions (book + cover)
│   ├── fonts.tex              # Font configuration
│   ├── boxes.tex              # tcolorbox environments
│   ├── commands.tex           # Custom commands
│   └── tikz.tex               # TikZ libraries and setup
│
├── front-matter/
│   ├── cover/                 # Cover components
│   │   ├── cover.tex          # Main cover page (inline TikZ)
│   │   ├── network-mlp.tex    # Background neural network
│   │   ├── network-graph.tex  # Foreground constellation
│   │   ├── diagram-radar.tex  # Radar chart
│   │   └── diagram-tree.tex   # Decision tree
│   ├── title-page.tex         # Title page
│   ├── copyright.tex          # Copyright page
│   ├── preface.tex            # Preface
│   ├── how-to-read.tex        # How to read this book
│   └── glossary-entries.tex   # Glossary definitions
│
├── chapters/
│   ├── 01-what-is-agent/
│   │   ├── chapter.tex        # Chapter main file
│   │   ├── sections/          # Section files
│   │   └── figures/           # Chapter figures
│   ├── 02-how-to-design/
│   │   ├── chapter.tex
│   │   ├── sections/
│   │   └── figures/
│   └── 03-how-to-govern/
│       ├── chapter.tex
│       ├── sections/
│       └── figures/
│
├── back-matter/               # Future expansion
│   └── .gitkeep
│
├── bib/
│   └── refs.bib               # Bibliography
│
└── .gitignore
```

## Execution Steps

### Phase 1: Create directory structure
- [x] Create preamble/
- [x] Create front-matter/cover/
- [x] Create back-matter/

### Phase 2: Split preamble
- [x] Extract packages.tex
- [x] Extract geometry.tex
- [x] Extract colors.tex (merge cover + book colors)
- [x] Extract fonts.tex
- [x] Extract boxes.tex
- [x] Extract commands.tex
- [x] Extract tikz.tex
- [x] Create preamble/main.tex

### Phase 3: Reorganize front-matter
- [x] Move cover graphics to front-matter/cover/
- [x] Create inline cover.tex (no standalone)
- [x] Keep existing front-matter files

### Phase 4: Rename chapter files
- [x] Rename chapters/*/main.tex to chapters/*/chapter.tex
- [x] Update any references

### Phase 5: Update main.tex
- [x] Use new preamble structure
- [x] Include cover inline (no \includepdf)
- [x] Use \newgeometry for cover page

### Phase 6: Clean up
- [x] Remove covers/ directory (all options)
- [x] Remove old preamble.tex
- [x] Update Makefile
- [x] Clean temporary files

### Phase 7: Verify
- [ ] Build with xelatex
- [ ] Check for warnings/errors
- [ ] Verify PDF output
