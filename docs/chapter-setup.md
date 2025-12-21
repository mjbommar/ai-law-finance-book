# Chapter Setup Guide

> **Purpose**: Step-by-step instructions for creating new chapters following the established patterns from Chapters 06, 07, and 08.

**Last Updated**: December 2025

---

## Table of Contents

1. [Directory Structure](#directory-structure)
2. [Creating a New Chapter](#creating-a-new-chapter)
3. [main.tex Structure](#maintex-structure)
4. [Section Files](#section-files)
5. [Figures](#figures)
6. [Bibliography](#bibliography)
7. [Makefile](#makefile)
8. [Naming Conventions](#naming-conventions)
9. [Box Environments](#box-environments)
10. [Color System](#color-system)
11. [Cross-References](#cross-references)
12. [Build and Validation](#build-and-validation)
13. [Checklist](#checklist)

---

## Directory Structure

Each chapter follows a standardized four-directory layout:

```
chapters/XX-chapter-slug/
├── main.tex                    # Master document
├── Makefile                    # Build automation
├── sections/
│   ├── 00-how-to-read.tex      # Optional: reading guide
│   ├── 01-introduction.tex     # Introduction
│   ├── 02-first-topic.tex      # Main content sections
│   ├── 03-second-topic.tex
│   ├── ...
│   └── NN-conclusion.tex       # Conclusion/further learning
├── figures/
│   ├── fig-slug-name.tex       # TikZ figures (preferred)
│   └── fig-slug-image.png      # Raster images (when needed)
└── bib/
    └── refs.bib                # Chapter bibliography
```

### Directory Naming

Chapter directories use the format: `XX-descriptive-slug`

| Pattern | Example |
|---------|---------|
| `01-topic-name` | `01-foundations-llm-primer-mechanics` |
| `06-agents-part-1` | `06-agents-part-1` |
| `08-agents-part-3` | `08-agents-part-3` |

- Two-digit prefix for ordering
- Lowercase with hyphens
- Descriptive but concise

---

## Creating a New Chapter

### Step 1: Create Directory Structure

```bash
# From repository root
CHAPTER="XX-chapter-name"
mkdir -p chapters/$CHAPTER/{sections,figures,bib}
```

### Step 2: Copy Makefile

Copy from an existing chapter and update if needed:

```bash
cp chapters/07-agents-part-2/Makefile chapters/$CHAPTER/
```

### Step 3: Create main.tex

Use the template in [main.tex Structure](#maintex-structure) below.

### Step 4: Create Initial Section Files

```bash
touch chapters/$CHAPTER/sections/{01-introduction,02-topic,03-conclusion}.tex
```

### Step 5: Create Bibliography File

```bash
touch chapters/$CHAPTER/bib/refs.bib
```

### Step 6: Test Build

```bash
cd chapters/$CHAPTER
make pdf
```

---

## main.tex Structure

The `main.tex` file serves as the master document for standalone chapter compilation. It contains the full preamble (currently ~350 lines) to enable independent PDF generation.

### Template Structure

```latex
\documentclass[11pt]{article}

% ============================================================
% GEOMETRY
% ============================================================
\usepackage[
  left=1.2in,
  right=1.2in,
  top=1.3in,
  bottom=1.3in
]{geometry}

% ============================================================
% FONTS AND TYPOGRAPHY
% ============================================================
\usepackage{libertinus}
\usepackage{libertinust1math}
\usepackage[T1]{fontenc}
\usepackage{microtype}
\usepackage{setspace}
\setstretch{1.15}

% Paragraph spacing (no indent, space between)
\usepackage{parskip}
\setlength{\parskip}{0.5em}
\setlength{\parindent}{0pt}

% ============================================================
% PACKAGES
% ============================================================
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{cleveref}

% TikZ for figures
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta, shapes, calc, decorations, shadows}

% tcolorbox for styled boxes
\usepackage[most]{tcolorbox}
\tcbuselibrary{breakable, skins, theorems}

% ============================================================
% 4-LAYER COLOR SYSTEM
% ============================================================
% Copy the full color definitions from an existing chapter
% (~100 lines covering primitives, semantics, components, legacy)

% Layer 1: Primitives (slate, green, amber, red, teal, indigo, gray)
% Layer 2: Semantic mappings (definition, example, key, caution, note)
% Layer 3: Component aliases (bg-*, border-*, text-*)
% Layer 4: Legacy compatibility

% ============================================================
% TCOLORBOX ENVIRONMENTS
% ============================================================
% Copy box definitions from existing chapter:
% - definitionbox (blue, formal definitions)
% - keybox (amber, key takeaways)
% - highlightbox (neutral, notes/asides)
% - questionbox (gray, evaluation questions)
% - theorembox (indigo, formal statements)
% - listingbox (gray, code examples)

% ============================================================
% CUSTOM COMMANDS
% ============================================================
\newcommand{\keyterm}[1]{\textbf{\textcolor{primary}{#1}}}

% ============================================================
% BIBLIOGRAPHY
% ============================================================
\usepackage[
  backend=biber,
  style=authoryear,
  maxcitenames=2,
  maxbibnames=99,
  uniquename=false,
  uniquelist=false,
  sorting=nyt,
  dashed=false,
  giveninits=true
]{biblatex}
\addbibresource{bib/refs.bib}

% ============================================================
% HYPERREF & METADATA
% ============================================================
\hypersetup{
  colorlinks=true,
  linkcolor=primary,
  citecolor=accent,
  urlcolor=primary,
  pdftitle={Chapter Title Here},
  pdfauthor={Michael J Bommarito II, Jillian Bommarito, Daniel Martin Katz},
  pdfsubject={AI Agents, Law, Finance},
  pdfkeywords={agentic AI, legal AI, financial AI},
  pdfcreator={LaTeX with hyperref}
}

% ============================================================
% CROSS-REFERENCES
% ============================================================
\crefname{section}{Section}{Sections}
\crefname{figure}{Figure}{Figures}
\crefname{table}{Table}{Tables}

% ============================================================
% DOCUMENT
% ============================================================
\begin{document}

% ------------------------------------------------------------
% TITLE BLOCK
% ------------------------------------------------------------
\title{
  \vspace{-0.5em}
  {\Huge\bfseries\color{primary} Part Title}\\[0.6em]
  {\LARGE\color{primary} Chapter Subtitle}\\[0.4em]
  {\large\itshape\color{text-secondary} Descriptive Tagline}
  \vspace{0.5em}
}

\author{
  \vspace{-0.5em}
  {\large\color{text-muted}
    Michael J Bommarito II \enspace $\cdot$ \enspace
    Jillian Bommarito \enspace $\cdot$ \enspace
    Daniel Martin Katz
  }
  \vspace{-0.5em}
}

\date{{\normalsize\color{text-muted}\today}}

\maketitle

% Divider line
\vspace{-1em}
\noindent{\color{border-neutral}\rule{\textwidth}{0.5pt}}
\vspace{1.0em}

% ------------------------------------------------------------
% DRAFT NOTICE (remove for final)
% ------------------------------------------------------------
\begin{center}
  \begin{tcolorbox}[
      enhanced,
      width=0.80\textwidth,
      colback=bg-note,
      colframe=border-note,
      fonttitle=\bfseries\large\color{note-dark},
      boxrule=1.5pt,
      arc=4pt,
      left=16pt,
      right=16pt,
      top=12pt,
      bottom=12pt,
      drop shadow={opacity=0.15}
    ]
    \centering
    {\large\bfseries\color{note-dark} Working Draft}\\[0.5em]
    {\normalsize\color{text-secondary}
      Version X.XX \enspace$\cdot$\enspace \today\\[0.3em]
      This is a working draft. Content may change.
    }
  \end{tcolorbox}
\end{center}

\vspace{1em}

% ------------------------------------------------------------
% TABLE OF CONTENTS
% ------------------------------------------------------------
\tableofcontents
\newpage

% ------------------------------------------------------------
% CONTENT SECTIONS
% ------------------------------------------------------------
\input{sections/01-introduction}
\input{sections/02-topic}
\input{sections/03-another-topic}
\input{sections/04-conclusion}

% ------------------------------------------------------------
% BIBLIOGRAPHY
% ------------------------------------------------------------
\newpage
\printbibliography

\end{document}
```

---

## Section Files

### File Naming Convention

Section files use zero-padded numeric prefixes for ordering:

```
sections/
├── 00-how-to-read.tex      # Optional navigation guide
├── 01-introduction.tex     # Always starts with 01
├── 02-first-topic.tex      # Main content
├── 03-second-topic.tex
├── 04-third-topic.tex
├── ...
└── NN-conclusion.tex       # Final section
```

### Section File Template

```latex
% ============================================================
% Section: Topic Name
% Chapter: XX - Chapter Name
% ============================================================

\section{Section Title}
\label{sec:chapterslug-topic}

Opening paragraph that introduces the section content...

\subsection{First Subsection}
\label{sec:chapterslug-topic-sub1}

Content here with \keyterm{important terms} highlighted on first use.

\begin{definitionbox}[title={Term Being Defined}]
  Formal definition of the term...
\end{definitionbox}

Cross-reference other sections with \Cref{sec:chapterslug-other}.

\subsection{Second Subsection}

More content with citations \parencite{author2024}.

\begin{keybox}[title={Key Insight}]
  Critical takeaway that readers must understand...
\end{keybox}

% Include a figure
\begin{figure}[htbp]
  \centering
  \input{figures/fig-topic-diagram}
  \caption{Descriptive caption explaining the figure.}
  \label{fig:chapterslug-diagram}
\end{figure}

Reference figures with \Cref{fig:chapterslug-diagram}.
```

### Section Hierarchy

Use consistent heading levels:

| Level | Command | Use For |
|-------|---------|---------|
| 1 | `\section{}` | Major topics (one per file typically) |
| 2 | `\subsection{}` | Subtopics within a section |
| 3 | `\subsubsection{}` | Detailed breakdowns |
| 4 | `\paragraph{}` | Inline headers (run-in style) |

---

## Figures

### Preferred Format: TikZ

TikZ figures are preferred because they:
- Use semantic colors from the preamble
- Scale perfectly at any size
- Are easy to update and maintain
- Compile directly with the document

### Figure File Template

```latex
% figures/fig-topic-diagram.tex
% Description: Diagram showing X relationship to Y

\begin{tikzpicture}[
  node distance=2cm,
  box/.style={
    rectangle,
    draw=border-definition,
    fill=bg-definition,
    rounded corners=4pt,
    minimum width=3cm,
    minimum height=1cm,
    font=\small
  },
  arrow/.style={
    ->,
    >=stealth,
    thick,
    draw=text-secondary
  }
]

% Nodes
\node[box] (a) {First Element};
\node[box, right=of a] (b) {Second Element};

% Arrows
\draw[arrow] (a) -- (b);

\end{tikzpicture}
```

### Including Figures

```latex
\begin{figure}[htbp]
  \centering
  \resizebox{0.9\textwidth}{!}{\input{figures/fig-topic-diagram}}
  \caption{Clear, descriptive caption that explains what the figure shows.}
  \label{fig:chapterslug-diagram}
\end{figure}
```

### Raster Images

When TikZ isn't practical (research paper clippings, screenshots):

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/fig-paper-clipping.png}
  \caption{Caption with source attribution.}
  \label{fig:chapterslug-clipping}
\end{figure}
```

### Figure Naming

| Type | Pattern | Example |
|------|---------|---------|
| TikZ diagrams | `fig-slug-name.tex` | `fig-react-cycle.tex` |
| PNG images | `fig-slug-name.png` | `fig-paper-clipping.png` |
| PDF vectors | `fig-slug-name.pdf` | `fig-architecture.pdf` |

---

## Bibliography

### File Location

Each chapter maintains its own bibliography at `bib/refs.bib`.

### Entry Format

```bibtex
@article{author2024keyword,
  author    = {Last, First and Other, Author},
  title     = {Full Title of the Article},
  journal   = {Journal Name},
  year      = {2024},
  volume    = {10},
  number    = {2},
  pages     = {123--145},
  doi       = {10.1000/example},
  url       = {https://example.com/article},
  urldate   = {2025-12-20},
  note      = {Relevance: Establishes framework for...}
}

@online{org2024title,
  author    = {{Organization Name}},
  title     = {Document Title},
  year      = {2024},
  url       = {https://example.com/doc},
  urldate   = {2025-12-20},
  note      = {Official specification for...}
}
```

### Required Fields

| Entry Type | Required Fields |
|------------|-----------------|
| `@article` | author, title, journal, year |
| `@book` | author, title, publisher, year |
| `@inproceedings` | author, title, booktitle, year |
| `@online` | author/organization, title, url, urldate |
| `@techreport` | author, title, institution, year |

### Best Practices

1. **Always include `urldate`** for web sources
2. **Include DOI** when available
3. **Add relevance notes** explaining why the source matters
4. **Use consistent key format**: `author2024keyword`
5. **Escape special characters**: Use `{LaTeX}` for proper casing

### Citation Commands

```latex
\parencite{author2024}           % (Author 2024)
\textcite{author2024}            % Author (2024)
\parencite[p.~42]{author2024}    % (Author 2024, p. 42)
\parencite{a2024,b2024,c2024}    % Multiple citations
```

---

## Makefile

### Standard Makefile Template

Copy from an existing chapter. Key targets:

| Target | Description |
|--------|-------------|
| `make pdf` | Full compilation (latexmk or 4-pass manual) |
| `make quick` | Single-pass pdflatex for rapid iteration |
| `make watch` | Continuous recompilation on file changes |
| `make validate` | Check for undefined references/citations |
| `make clean` | Remove auxiliary files (keep PDF) |
| `make cleanall` | Remove everything including PDF |
| `make view` | Open PDF in system viewer |
| `make png` | Convert PDF pages to 300dpi PNG |
| `make wordcount` | Approximate word count |

### Compilation Pipeline

The manual 4-pass compilation:

1. `pdflatex main.tex` — Generate .aux, .bcf
2. `biber main` — Process bibliography
3. `pdflatex main.tex` — Resolve citations
4. `pdflatex main.tex` — Resolve cross-references

---

## Naming Conventions

### Labels

| Element | Pattern | Example |
|---------|---------|---------|
| Section | `sec:chapterslug-topic` | `sec:agents2-triggers` |
| Subsection | `sec:chapterslug-topic-sub` | `sec:agents2-triggers-channels` |
| Figure | `fig:chapterslug-name` | `fig:agents2-react-cycle` |
| Table | `tab:chapterslug-name` | `tab:agents2-comparison` |
| Equation | `eq:chapterslug-name` | `eq:agents2-utility` |

### Chapter Slugs by Number

| Chapter | Title | Slug | Section Prefix | Notes |
|---------|-------|------|----------------|-------|
| 01 | LLM Primer: Mechanics | `llmA` | `sec:llmA-*` | Foundations Part I |
| 02 | Conversations & Reasoning | `llmB` | `sec:llmB-*` | Foundations Part I |
| 03 | Structured Outputs & Tools | `llmC` | `sec:llmC-*` | Foundations Part I |
| 04 | Retrieval & Knowledge | `llmD` | `sec:llmD-*` | Foundations Part I |
| 05 | Evaluation & Testing | `llmE` | `sec:llmE-*` | Foundations Part I |
| 06 | Agents Part 1 | `agents1` | `sec:agents1-*` | Agents Part II |
| 07 | Agents Part 2 | `agents2` | `sec:agents2-*` | Agents Part II |
| 08 | Agents Part 3 | `agents3` | `sec:agents3-*` | Agents Part II |

**Slug Naming Rules:**
- Use consistent prefix within each chapter (all labels start with same slug)
- Use lowercase with hyphens for topic portions
- Keep labels descriptive but concise: `sec:llmB-cot` not `sec:llmB-chain-of-thought-reasoning-pattern`

---

## Cross-Chapter References

### The Challenge

When chapters are compiled standalone, references to other chapters using `\Cref{}` will fail because those labels don't exist in the current compilation unit. This section provides patterns for handling cross-chapter references gracefully.

### Pattern 1: Textual Chapter References

For references to content in other chapters, use textual references instead of `\Cref{}`:

**DON'T (fails in standalone mode):**
```latex
See \Cref{sec:llmA-intro} for background on tokenization.
```

**DO (works in all modes):**
```latex
See Chapter~1 (The LLM Primer) for background on tokenization.
```

**Format:** `Chapter~N (Chapter Title)` with non-breaking space

### Pattern 2: Signpost Paragraphs

When content is covered in detail elsewhere, use a signpost paragraph to direct readers:

```latex
\paragraph{Signpost to Chapter~1.} Prompt injection is not only a
conversational concern but also a core LLM failure mode with security
implications. Chapter~1 provides a detailed taxonomy of prompt injection
attacks and defense-in-depth mitigations.
```

**Signpost structure:**
1. `\paragraph{Signpost to Chapter~N.}` — Clear visual marker
2. Brief context — Why this matters here
3. What the other chapter covers — Specific content available there

**When to use signposts:**
- When a topic deserves more coverage than you can give in current context
- When readers might expect coverage here but it's elsewhere
- When two chapters have related but distinct treatments of a topic

### Pattern 3: Part References

For references to entire parts of the book:

```latex
These governance considerations are explored in depth in Part~III (Governance).
```

### Pattern 4: Forward References Within Chapter

For content later in the same chapter, use `\Cref{}` normally:

```latex
We address strategy selection in \Cref{sec:llmB-strategy}.
See \Cref{fig:llmB-react-loop} for a visualization of this cycle.
```

### Pattern 5: Conditional Compilation (Advanced)

For the eventual book compilation where all chapters are combined:

```latex
% In preamble (or shared definitions):
\newcommand{\chapterref}[2]{%
  \ifdefined\compilingbook
    \Cref{#1}%
  \else
    Chapter~#2%
  \fi
}

% Usage:
\chapterref{sec:llmA-intro}{1 (The LLM Primer)}
```

This allows automatic switching between standalone and book modes.

### Cross-Reference Checklist

Before finalizing a chapter, verify:
- [ ] No `\Cref{}` or `\ref{}` to labels outside current chapter
- [ ] All cross-chapter refs use `Chapter~N (Title)` format
- [ ] Signposts added where detailed treatment exists elsewhere
- [ ] Part references use `Part~N (Title)` format
- [ ] `make validate` shows no undefined reference warnings

---

## Standard Section Templates

### "How to Read This Chapter" Template

Every chapter should begin with a navigation section. This helps readers with different goals find the most efficient path through the material.

**File location:** `sections/howtoread.tex` (unnumbered section)

**Complete template:**

```latex
% =============================================================================
% How to Read This Chapter — [Chapter Topic]
% Purpose: Audience paths, scope, and navigation
% =============================================================================

\section*{How to Read This Chapter}
\addcontentsline{toc}{section}{How to Read This Chapter}

% Opening hook (1-2 sentences connecting to book context)
This chapter extends [previous concepts] into [new territory]. Whether you are
a [audience 1], [audience 2], or [audience 3], this chapter provides [value proposition].

\subsection*{Reading Paths}

\begin{highlightbox}[colback=bg-definition, colframe=definition-base,
    title={Path 1: Practitioner Quick Start (20--30 minutes)}]
If you are already [context] and want immediately applicable techniques:
\begin{itemize}
  \item \textbf{\Cref{sec:slug-topic1}}: [What they'll learn]
  \item \textbf{\Cref{sec:slug-topic2}}: [What they'll learn]
  \item \textbf{\Cref{sec:slug-topic3}}: [What they'll learn]
\end{itemize}
This path gives you [outcome] while building the foundation for [future topics].
\end{highlightbox}

\begin{highlightbox}[colback=bg-example, colframe=example-base,
    title={Path 2: Full Technical Understanding (60--90 minutes)}]
If you need to understand the underlying mechanics for system design:
\begin{itemize}
  \item Read all sections in order, paying particular attention to [key areas]
  \item Study [specific subsections] for [specific knowledge]
  \item Examine [advanced topics] for [advanced use cases]
\end{itemize}
This path prepares you to [advanced outcome].
\end{highlightbox}

\begin{highlightbox}[colback=bg-note, colframe=border-note,
    title={Path 3: Governance and Risk Focus (30--45 minutes)}]
If your primary concern is risk management, compliance, or audit:
\begin{itemize}
  \item \textbf{\Cref{sec:slug-safety}}: [Governance content]
  \item \textbf{\Cref{sec:slug-audit}}: [Compliance content]
  \item \textbf{\Cref{sec:slug-risk}}: [Risk content]
\end{itemize}
This path emphasizes governance dimensions that Part~III expands upon.
\end{highlightbox}

\subsection*{Prerequisites}

This chapter assumes familiarity with concepts from Chapter~N (Title):
\begin{itemize}
  \item [Prerequisite concept 1]
  \item [Prerequisite concept 2]
  \item [Prerequisite concept 3]
\end{itemize}

If these concepts are unfamiliar, we recommend reviewing [specific chapter] first.

\subsection*{What This Chapter Covers}

\begin{keybox}[title={Key Objectives}]
By the end of this chapter, you will be able to:
\begin{enumerate}
  \item \textbf{[Verb] [outcome 1]} with [context]
  \item \textbf{[Verb] [outcome 2]} based on [criteria]
  \item \textbf{[Verb] [outcome 3]} using [methods]
  \item \textbf{[Verb] [outcome 4]} while understanding [constraints]
  \item \textbf{[Verb] [outcome 5]} for [applications]
\end{enumerate}
\end{keybox}

\begin{highlightbox}[title={Visual Cues (Boxes)}]
Throughout the chapter, colored boxes signal intent:
\begin{itemize}
  \item \textbf{Key takeaways (\texttt{keybox}):} objectives, frameworks, decision rules
  \item \textbf{Definitions (\texttt{definitionbox}):} formal terms and concepts
  \item \textbf{Notes (\texttt{highlightbox}):} context, intuition, quick-start tips
  \item \textbf{Warnings (\texttt{cautionbox}):} risk and governance pitfalls
  \item \textbf{Code (\texttt{listingbox}):} reproducible snippets and examples
\end{itemize}
\end{highlightbox}

\subsection*{What This Chapter Does Not Cover}

To maintain focus, we defer several related topics:
\begin{itemize}
  \item \textbf{[Topic 1]}: Covered in Chapter~N (Title)
  \item \textbf{[Topic 2]}: Implementation details appear in Chapter~M
  \item \textbf{[Topic 3]}: Full treatment in Part~X (Part Name)
\end{itemize}

\subsection*{Bridge from Previous Chapter}

% 2 paragraphs connecting to prior content
In the previous chapter, we examined [prior concepts]. We saw that [key insight].
We explored [methods] and [outcomes].

This chapter extends those foundations in two critical directions:

\paragraph{From [Old] to [New].} [Explanation of first extension, ~3-4 sentences]

\paragraph{From [Old] to [New].} [Explanation of second extension, ~3-4 sentences]

Together, these extensions [overall value statement]. The techniques we introduce
here form the foundation for [subsequent chapters].
```

### "Further Learning" Section Template

Every chapter should end with an annotated bibliography and learning resources.

**File location:** `sections/furtherlearning.tex`

**Structure:**

```latex
\section{Further Learning}
\label{sec:slug-further}

This section provides an annotated guide to foundational literature...

\subsection{Foundational Papers on [Topic]}

\paragraph{[Subtopic Name].}
\textcite{author2024} introduced [concept], demonstrating that [key finding].
This paper is essential for understanding [why it matters for practitioners].

% Repeat for 3-5 key papers per subsection

\subsection{[Second Topic Category]}
% More annotated entries

\subsection{Implementation Resources}

\paragraph{[Resource Type].}
[Description of practical resources]:
\begin{itemize}
  \item \textbf{[Resource 1]}: [Description]
  \item \textbf{[Resource 2]}: [Description]
\end{itemize}

\subsection{Recommended Reading Sequence}

For readers who want to develop deep expertise:

\paragraph{Foundation Level (Week 1--2).}
Begin with the foundational papers:
\begin{enumerate}
  \item \textcite{paper1} to understand [concept]
  \item \textcite{paper2} to grasp [concept]
\end{enumerate}

\paragraph{Intermediate Level (Week 3--4).}
Progress to [next level topics]...

\paragraph{Advanced Level (Week 5--6).}
Explore sophisticated [advanced topics]...

\subsection{Common Misconceptions}

\paragraph{Misconception: [Statement].}
[Explanation of why this is wrong and what's actually true. 3-4 sentences.]

% Repeat for 3-5 common misconceptions

\subsection{Exercises for Practitioners}

\paragraph{Exercise 1: [Title].}
[Description of exercise with clear steps]:
\begin{enumerate}
  \item [Step 1]
  \item [Step 2]
  \item [Step 3]
\end{enumerate}
[Expected outcome or evaluation criteria]

% 4-6 exercises total
```

---

## TikZ Figures: Patterns and Common Errors

### File Structure

TikZ figures should be self-contained `.tex` files in the `figures/` directory:

```latex
% figures/fig-slug-name.tex
% Description: [What this figure shows]
% Used in: sections/XX-topic.tex

\begin{tikzpicture}[
  % Style definitions here
]

% Figure content

\end{tikzpicture}
```

### Common Error 1: Line Breaks in Nodes

**Problem:** `Not allowed in LR mode` error

**Wrong:**
```latex
\node[box] (a) {First Line\\Second Line};
```

**Right (Option A — add align style):**
```latex
\node[box, align=center] (a) {First Line\\Second Line};
```

**Right (Option B — use single line):**
```latex
\node[box] (a) {Combined Text};
```

**Right (Option C — use text width):**
```latex
\node[box, text width=3cm, align=center] (a) {First Line\\Second Line};
```

### Common Error 2: Missing Arrow Libraries

**Problem:** Arrow tips don't render correctly

**Fix:** Ensure usetikzlibrary includes arrows.meta:
```latex
\usetikzlibrary{positioning, arrows.meta, shapes, calc}
```

### Common Error 3: Color References

**Wrong (hardcoded colors):**
```latex
\node[fill=blue!20, draw=blue] {...};
```

**Right (semantic colors):**
```latex
\node[fill=bg-definition, draw=border-definition] {...};
```

### Common Error 4: Positioning Without Library

**Problem:** `of=` syntax doesn't work

**Fix:** Ensure positioning library is loaded:
```latex
\usetikzlibrary{positioning}

% Then use:
\node[box, right=of nodeA] (nodeB) {...};
```

### Common Error 5: Shadow Without Library

**Problem:** Shadow effects don't render

**Fix:** Load shadows library:
```latex
\usetikzlibrary{shadows.blur}
% or
\usetikzlibrary{shadows}
```

### Standard TikZ Style Template

```latex
\begin{tikzpicture}[
  % Node distance for positioning
  node distance=1.5cm and 2cm,

  % Standard box style
  box/.style={
    rectangle,
    draw=border-definition,
    fill=bg-definition,
    rounded corners=4pt,
    minimum width=2.5cm,
    minimum height=1cm,
    font=\small,
    text=text-primary,
    align=center
  },

  % Emphasized box style
  emphbox/.style={
    box,
    draw=border-key,
    fill=bg-key,
    line width=1.5pt
  },

  % Arrow style
  arrow/.style={
    ->,
    >=stealth,
    thick,
    draw=text-secondary
  },

  % Label style for annotations
  label/.style={
    font=\footnotesize,
    text=text-muted
  }
]

% Content here

\end{tikzpicture}
```

### Including TikZ Figures

```latex
\begin{figure}[htbp]
  \centering
  \input{figures/fig-slug-name}
  \caption{Descriptive caption explaining what the figure shows and why it matters.}
  \label{fig:slug-name}
\end{figure}
```

For scaling:
```latex
\resizebox{0.9\textwidth}{!}{\input{figures/fig-slug-name}}
```

---

## Box Environments

### Available Box Types

| Environment | Color | Use For |
|-------------|-------|---------|
| `definitionbox` | Blue | Formal definitions, technical terms |
| `keybox` | Amber/Orange | Key takeaways, critical insights |
| `highlightbox` | Neutral/Cream | Notes, context, asides |
| `questionbox` | Gray/Slate | Evaluation questions, prompts |
| `theorembox` | Indigo | Formal statements, proofs |
| `listingbox` | Gray | Code examples, API signatures |

### Usage Examples

```latex
\begin{definitionbox}[title={Agent}]
  An \keyterm{agent} is an entity that perceives its environment
  and takes actions to achieve goals.
\end{definitionbox}

\begin{keybox}[title={Core Insight}]
  The distinction between tools and agents lies in autonomous
  decision-making capability.
\end{keybox}

\begin{highlightbox}
  This section assumes familiarity with concepts from Chapter 1.
  See \Cref{sec:primer-tokens} for background.
\end{highlightbox}
```

### Box Options

All boxes support an optional `importance` parameter:

```latex
\begin{keybox}[title={Critical Point}, importance=high]
  This is extremely important...
\end{keybox}
```

| Importance | Effect |
|------------|--------|
| `high` | Thicker border (2pt), stronger shadow |
| `medium` | Default appearance |
| `low` | Thin border (0.8pt), reduced emphasis |

---

## Color System

### 4-Layer Architecture

1. **Layer 1 — Primitives**: Raw RGB colors (slate, green, amber, red, teal, indigo, gray)
2. **Layer 2 — Semantics**: Educational content types (definition, example, key, caution, note, theorem, practice)
3. **Layer 3 — Components**: Usage aliases (bg-definition, border-example, text-primary)
4. **Layer 4 — Legacy**: Backward compatibility (agentblue, accentorange)

### Semantic Color Usage

| Content Type | Color Family | Use For |
|--------------|--------------|---------|
| definition | Blue (slate) | Formal definitions, concepts |
| example | Green | Concrete examples, demonstrations |
| key | Amber/Orange | Important takeaways |
| caution | Red | Warnings, pitfalls |
| note | Neutral | Supplementary info |
| theorem | Indigo | Formal statements |
| practice | Teal | Exercises |

### Using Colors

```latex
% Text colors
\textcolor{primary}{Primary text}
\textcolor{text-secondary}{Secondary text}

% In TikZ
\node[fill=bg-definition, draw=border-definition] {...};

% Background colors
\colorbox{bg-key}{Highlighted text}
```

---

## Cross-References

### Using cleveref

Always use `\Cref{}` for automatic formatting:

```latex
\Cref{sec:agents2-triggers}     % "Section 2"
\Cref{fig:agents2-diagram}      % "Figure 3"
\Cref{tab:agents2-comparison}   % "Table 1"
```

### Multiple References

```latex
\Cref{sec:a,sec:b,sec:c}        % "Sections 1, 2, and 3"
```

### Cross-Chapter References

For references to other chapters:

```latex
See \textit{What is an Agent?} (Part I) for foundational concepts.
```

---

## Build and Validation

### Standard Build Workflow

```bash
cd chapters/XX-chapter-name

# Full build
make pdf

# Quick iteration (single pass)
make quick

# Continuous watch mode
make watch
```

### Validation Checks

```bash
# Check for undefined references and citation warnings
make validate

# Manual check for common issues
grep -rn "TODO\|FIXME" sections/
grep -rn "\\\\ref{" sections/ | grep -v "Cref"  # Should use \Cref
```

### Common Build Errors

| Error | Cause | Solution |
|-------|-------|----------|
| Undefined reference | Missing `\label{}` | Add label to target |
| Citation undefined | Missing bib entry | Add to refs.bib |
| Missing file | Wrong path | Check `\input{}` paths |
| Font not found | Missing package | Install texlive-fonts-extra |

---

## Checklist

### Before Starting

- [ ] Directory structure created
- [ ] Makefile copied and tested
- [ ] main.tex template in place
- [ ] Empty refs.bib created

### During Writing

- [ ] All sections have `\label{sec:...}`
- [ ] All figures have `\label{fig:...}`
- [ ] Key terms use `\keyterm{}`
- [ ] Citations use `\parencite{}` or `\textcite{}`
- [ ] Cross-references use `\Cref{}`
- [ ] Boxes used appropriately for content type

### Before Commit

- [ ] `make pdf` compiles without errors
- [ ] `make validate` shows no warnings
- [ ] All citations exist in refs.bib
- [ ] No TODO/FIXME markers remain
- [ ] Figures render correctly
- [ ] Table of contents is accurate

### Quality Standards

- [ ] Follows style guide (docs/style-guide.md)
- [ ] Uses semantic colors (docs/color-guide.md)
- [ ] Voice: "we" for analysis, "you" for guidance
- [ ] No "I" usage
- [ ] Citations include urldate for web sources
- [ ] No confidential/privileged content

---

## Related Documentation

- **[build-guide.md](build-guide.md)** — Dual-compilation system details
- **[style-guide.md](style-guide.md)** — Writing standards and voice
- **[color-guide.md](color-guide.md)** — Color system reference
- **[../CLAUDE.md](../CLAUDE.md)** — AI assistant workflow guide
- **[../AGENTS.md](../AGENTS.md)** — Evidence standards and file conventions
