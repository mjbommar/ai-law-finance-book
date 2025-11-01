# Build System Guide

**Last Updated**: November 1, 2025

This guide explains the dual-compilation LaTeX build system that allows generating both standalone chapter PDFs and a complete unified book PDF.

---

## Quick Start

### Build Everything
```bash
make all-pdfs     # Build all chapters + complete book
```

### Build Complete Book
```bash
make pdf          # or: make book
```

### Build Individual Chapters
```bash
make chapters                      # Build all chapters
cd chapters/agents-part-1 && make pdf  # Build one chapter
```

---

## Architecture Overview

The build system uses the **`subfiles` package** to enable dual compilation:

1. **Standalone Mode**: Each chapter compiles independently with its own title page, table of contents, and bibliography
2. **Book Mode**: All chapters compile together into a unified book with continuous page numbering, unified bibliography, and proper book structure

### Key Components

```
/
├── main.tex              # Root book document (book class)
├── preamble.tex          # Shared formatting for ALL documents
├── bib/refs.bib          # Consolidated bibliography (root level)
├── Makefile              # Root build system
└── chapters/
    └── chapter-name/
        ├── main.tex      # Chapter as subfile (references ../../main.tex)
        ├── sections/     # Chapter content sections
        ├── figures/      # Chapter-specific figures
        ├── bib/refs.bib  # Chapter bibliography (consolidated to root)
        └── Makefile      # Chapter-level build system
```

---

## How It Works

### 1. Shared Preamble (`preamble.tex`)

All formatting, colors, packages, and custom commands are defined in a single shared preamble:

- **Typography**: Libertinus fonts, microtype, spacing
- **Color System**: Complete 4-layer semantic color system (see [color-guide.md](color-guide.md))
- **Custom Environments**: definitionbox, highlightbox, keybox, questionbox
- **Section Styling**: Custom titlesec formatting
- **Bibliography**: BibLaTeX configuration with authoryear style
- **Cross-referencing**: Cleveref setup

**Both the root `main.tex` and chapter `main.tex` files load this same preamble**, ensuring identical formatting in both modes.

### 2. Root Book Document (`main.tex`)

The root document uses the `book` document class and:

```latex
\documentclass[11pt,oneside]{book}

% Load subfiles and path handling
\usepackage{import}
\usepackage{subfiles}

% Load shared preamble
\makeatletter
\def\input@path{{./}{../}{../../}}
\makeatother
\input{preamble.tex}

% ... metadata, title, etc ...

\begin{document}
\frontmatter
\maketitle
\tableofcontents

\mainmatter
\part{Agents and Agentic Systems}
\subfile{chapters/agents-part-1/main}  % Include chapter as subfile

\backmatter
\printbibliography
\end{document}
```

**Key Features**:
- Uses `book` class with frontmatter, mainmatter, backmatter structure
- Includes chapters via `\subfile{}`
- Unified bibliography at end
- Path handling via `\input@path` so preamble loads from any directory

### 3. Chapter Document (`chapters/*/main.tex`)

Each chapter references the parent book document:

```latex
\documentclass[../../main.tex]{subfiles}

\begin{document}

% Standalone mode: show title and TOC
\ifx\chapter\undefined
  \title{...}
  \maketitle
  \tableofcontents
  \newpage
\fi

% Book mode: show chapter heading
\ifx\chapter\undefined
\else
  \chapter{Chapter Title}
  \label{chap:chapter-name}
\fi

% Content (both modes)
\input{sections/intro}
\input{sections/content}
...

% Standalone mode: show bibliography
\ifx\chapter\undefined
  \newpage
  \printbibliography
\fi

\end{document}
```

**Key Features**:
- References parent document via `\documentclass[../../main.tex]{subfiles}`
- Uses `\ifx\chapter\undefined` to detect compilation mode
- In **standalone mode** (article class): shows title, TOC, and bibliography
- In **book mode** (book class): becomes a chapter with proper heading

### 4. Path Handling

The `\input@path` directive in the root `main.tex` allows the preamble to be found from any directory:

```latex
\makeatletter
\def\input@path{{./}{../}{../../}}
\makeatother
```

This means:
- When compiling from root: `\input{preamble.tex}` → finds `./preamble.tex`
- When compiling from chapter: `\input{preamble.tex}` → finds `../../preamble.tex`

---

## Build Targets

### Root-Level Targets (from repository root)

| Target | Description | Output |
|--------|-------------|--------|
| `make pdf` | Build complete book (default) | `main.pdf` (~720KB, 54 pages) |
| `make book` | Same as `make pdf` | `main.pdf` |
| `make chapters` | Build all individual chapter PDFs | Each `chapters/*/main.pdf` |
| `make all-pdfs` | Build chapters + book | All PDFs |
| `make clean` | Remove auxiliary files | |
| `make cleanall` | Remove auxiliary files + PDFs | |
| `make view` | Open book PDF in viewer | |
| `make validate` | Check for undefined refs/citations | |
| `make wordcount` | Count words in document | |

### Chapter-Level Targets (from `chapters/chapter-name/`)

| Target | Description | Output |
|--------|-------------|--------|
| `make pdf` | Build standalone chapter PDF | `main.pdf` (~670KB, 47 pages) |
| `make quick` | Single-pass build (fast) | `main.pdf` |
| `make clean` | Remove auxiliary files | |
| `make cleanall` | Remove auxiliary files + PDF | |
| `make view` | Open chapter PDF in viewer | |
| `make validate` | Check for undefined refs/citations | |
| `make wordcount` | Count words in chapter | |

---

## Compilation Process

### Standalone Chapter Compilation

1. `pdflatex` reads `chapters/agents-part-1/main.tex`
2. Sees `\documentclass[../../main.tex]{subfiles}`
3. Loads parent preamble from `../../main.tex` → finds `preamble.tex`
4. `\ifx\chapter\undefined` is TRUE (article class) → shows title, TOC
5. Inputs sections via `\input{sections/...}`
6. Shows bibliography at end
7. Output: Standalone chapter PDF with own title page

### Book Compilation

1. `pdflatex` reads `main.tex` (book class)
2. Loads `preamble.tex` directly
3. In mainmatter, encounters `\subfile{chapters/agents-part-1/main}`
4. Subfiles package processes chapter:
   - `\ifx\chapter\undefined` is FALSE (book class defined) → skips title/TOC
   - Executes `\chapter{...}` → creates chapter heading
   - Inputs sections via `\input{sections/...}`
   - Skips chapter bibliography (book has unified one at end)
5. Continues with more chapters
6. Prints unified bibliography in backmatter
7. Output: Complete book PDF with all chapters

---

## Adding a New Chapter

### 1. Create Chapter Directory

```bash
mkdir -p chapters/new-chapter/{sections,figures,bib}
```

### 2. Create Chapter Main File

`chapters/new-chapter/main.tex`:

```latex
\documentclass[../../main.tex]{subfiles}

\begin{document}

\ifx\chapter\undefined
  \title{
    {\Huge\bfseries\color{primary} Chapter Title}\\[0.5em]
    {\large\itshape\color{text-secondary} Subtitle}
  }
  \author{\large\color{text-muted} Draft Version}
  \date{}
  \maketitle
  \tableofcontents
  \newpage
\fi

\ifx\chapter\undefined
\else
  \chapter{Chapter Title}
  \label{chap:new-chapter}
\fi

\input{sections/intro}
% ... more sections ...

\ifx\chapter\undefined
  \newpage
  \printbibliography
\fi

\end{document}
```

### 3. Copy Chapter Makefile

```bash
cp chapters/agents-part-1/Makefile chapters/new-chapter/Makefile
```

### 4. Add to Root Book

Edit `main.tex`:

```latex
\mainmatter

\part{Part Title}
\subfile{chapters/agents-part-1/main}
\subfile{chapters/new-chapter/main}  % Add this line
```

### 5. Create Chapter Bibliography

`chapters/new-chapter/bib/refs.bib`:

```bibtex
@article{key,
  author = {...},
  title = {...},
  ...
}
```

Then consolidate to root:

```bash
cat chapters/new-chapter/bib/refs.bib >> bib/refs.bib
```

### 6. Test Both Modes

```bash
# Test standalone
cd chapters/new-chapter && make pdf

# Test book
cd ../.. && make book
```

---

## Common Issues & Solutions

### Issue: `preamble.tex` not found

**Symptom**: `File 'preamble.tex' not found`

**Solution**: Ensure `\input@path` is set in root `main.tex`:

```latex
\makeatletter
\def\input@path{{./}{../}{../../}}
\makeatother
```

### Issue: Colors undefined

**Symptom**: `Undefined color 'text-key'` or similar

**Solution**: Check that `preamble.tex` contains all color definitions from the 4-layer system. Missing colors should be added to Layer 3 (Component Aliases).

### Issue: Environment undefined

**Symptom**: `Environment questionbox undefined`

**Solution**: Add the environment definition to `preamble.tex`:

```latex
\newtcolorbox{questionbox}[1][]{
  enhanced,
  colback=bg-practice,
  colframe=border-practice,
  ...
}
```

### Issue: Bibliography not appearing in standalone chapter

**Symptom**: Empty bibliography section in chapter PDF

**Solution**:
1. Ensure chapter has `bib/refs.bib` file
2. Chapter must use `\addbibresource{bib/refs.bib}` in standalone mode
3. Run full compilation: `make clean && make pdf` (runs biber)

### Issue: Cross-references to other chapters fail

**Symptom**: `Reference 'chap:other-chapter' undefined` when compiling standalone chapter

**Solution**: This is expected. Standalone chapters can only reference content within themselves. Cross-chapter references only work in book mode.

**Workaround**: Use conditional compilation:

```latex
\ifx\chapter\undefined
  % Standalone mode - describe the concept instead
  As discussed in another chapter...
\else
  % Book mode - use actual reference
  As discussed in \Cref{chap:other-chapter}...
\fi
```

---

## Bibliography Management

### Strategy

1. **Development**: Each chapter maintains its own `chapters/*/bib/refs.bib`
2. **Book Build**: Root has consolidated `bib/refs.bib` with all entries
3. **Maintenance**: Periodically sync chapter bibliographies to root:

```bash
# Consolidate all chapter bibliographies
cat chapters/*/bib/refs.bib | sort -u > bib/refs.bib

# Or manually merge new entries as chapters are added
```

### Best Practices

1. **Unique Keys**: Use descriptive, unique citation keys (e.g., `author2020topic`)
2. **Full Metadata**: Include all BibLaTeX fields (author, title, year, venue, DOI/URL, urldate)
3. **Primary Sources**: Follow evidence hierarchy from [AGENTS.md](../AGENTS.md)
4. **Time-Sensitive**: Include `date` and `urldate` fields for web sources
5. **Consistency**: Use same formatting style across all entries

---

## Advanced Features

### Conditional Compilation

Use `\ifx\chapter\undefined` to detect mode:

```latex
\ifx\chapter\undefined
  % Standalone mode code
  This is a standalone chapter.
\else
  % Book mode code
  This is \Cref{chap:my-chapter}.
\fi
```

### Cross-Chapter References (Book Mode Only)

```latex
% In chapters/chapter-2/main.tex
\ifx\chapter\undefined
  % Standalone: don't reference other chapters
  Building on earlier concepts...
\else
  % Book mode: reference other chapters
  Building on \Cref{chap:agents-part-1}...
\fi
```

### Multiple Bibliography Sections

For book with per-chapter bibliographies (advanced):

```latex
% In root main.tex
\usepackage[refsection=chapter]{biblatex}

% Each \subfile{} automatically creates a new refsection
\subfile{chapters/chapter-1/main}  % Has own bibliography
\subfile{chapters/chapter-2/main}  % Has own bibliography
```

---

## Performance Tips

### Fast Iteration During Writing

When working on a single chapter:

```bash
cd chapters/agents-part-1
make quick  # Single pass, no biber (fast)
```

### Full Rebuild

When colors, preamble, or bibliography change:

```bash
# From root
make cleanall && make all-pdfs

# Or from chapter
cd chapters/agents-part-1
make cleanall && make pdf
```

### Parallel Builds

Build all chapters in parallel (if you have multiple cores):

```bash
# From root
for chapter in chapters/*/; do
  (cd "$chapter" && make pdf) &
done
wait
```

---

## File Size Optimization

### Current Sizes

- **Standalone chapter**: ~670KB (47 pages)
- **Complete book**: ~720KB (54 pages)

### Optimization Options

1. **Compress PDFs** (lossless):
```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

2. **Reduce image resolution** (if adding figures):
   - Use vector formats (PDF, SVG) when possible
   - Rasterize at 300 DPI for print, 150 DPI for screen

3. **Font subsetting**: Automatically done by pdflatex

---

## Debugging

### View LaTeX Log

```bash
# From chapter directory
less main.log

# Or search for errors
grep -i "error\|warning" main.log
```

### Validate References

```bash
make validate
```

This checks for:
- Undefined references (`\ref{}` without corresponding `\label{}`)
- Undefined citations (`\cite{}` without corresponding bib entry)
- Multiple-defined labels

### Check File Dependencies

```bash
# See what files are read during compilation
grep "File:" main.log | grep -v "^("
```

---

## Integration with Version Control

### What to Commit

✅ **DO commit**:
- `*.tex` files (main.tex, preamble.tex, sections/)
- `*.bib` files (bibliography)
- `Makefile`
- Figure source files (`.tex` diagrams, vector `.pdf`/`.svg`)

❌ **DON'T commit** (use `.gitignore`):
- `*.aux`, `*.log`, `*.out`, `*.toc`, `*.bbl`, `*.bcf`, `*.run.xml`, `*.synctex.gz`, `*.fls`, `*.fdb_latexmk`
- Generated `*.pdf` (except release versions)

### Recommended `.gitignore`

Already set up in repository root. See [.gitignore](../.gitignore).

---

## Continuous Integration

### GitHub Actions Example

```yaml
name: Build LaTeX PDFs

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Install LaTeX
        run: |
          sudo apt-get update
          sudo apt-get install -y texlive-full biber

      - name: Build All PDFs
        run: make all-pdfs

      - name: Upload Artifacts
        uses: actions/upload-artifact@v2
        with:
          name: pdfs
          path: |
            main.pdf
            chapters/*/main.pdf
```

---

## Migration Guide

### From Old Single-File Structure

If you have an existing chapter with everything in one file:

1. **Backup**: `cp main.tex main.tex.backup`

2. **Split into sections**:
   - Create `sections/` directory
   - Move each `\section{}` block to separate file in `sections/`
   - Use logical names: `intro.tex`, `methodology.tex`, `results.tex`, etc.

3. **Update main.tex** to subfile format:
   - Change `\documentclass{article}` to `\documentclass[../../main.tex]{subfiles}`
   - Add conditional blocks for title/TOC/bibliography
   - Replace section content with `\input{sections/...}`

4. **Test**: `make pdf` should produce same output

5. **Verify book mode**: `cd ../.. && make book`

---

## Related Documentation

- [AGENTS.md](../AGENTS.md) - Contribution workflow and evidence standards
- [CLAUDE.md](../CLAUDE.md) - AI assistant quick start guide
- [style-guide.md](style-guide.md) - Writing and presentation standards
- [color-guide.md](color-guide.md) - Visual design system and semantic colors
- [README.md](../README.md) - Project overview and getting started

---

## Support

For build issues:
1. Check this guide for common issues
2. Review `.log` files for detailed error messages
3. Verify all dependencies installed: `pdflatex`, `biber`, `latexmk`
4. Try clean rebuild: `make cleanall && make pdf`

For questions about structure or design decisions, see related documentation above.
