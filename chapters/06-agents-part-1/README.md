# Chapter: Agents - Part I: What is an Agent?

**Subtitle**: A Conceptual Primer and History

## Overview

This chapter is Part I of a three-part series from the textbook *Artificial Intelligence for Law and Finance*. It answers the deceptively simple question "What is an agent?" by synthesizing seven decades of scholarship from philosophy, psychology, law, economics, cognitive science, complex systems, computer science, and AI into practical frameworks for understanding and evaluating agency.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 1 | `sections/00-how-to-read.tex` | How to Read This Chapter |
| 2 | `sections/01-introduction.tex` | Introduction |
| 3 | `sections/02-recognize-agent.tex` | How to Recognize an Agent |
| 4 | `sections/03-historical-journey.tex` | A Historical Journey: Defining Agents Across Seven Decades |
| 5 | `sections/04-disciplinary-perspectives.tex` | Disciplinary Perspectives on Agency |
| 6 | `sections/05-analytical-dimensions.tex` | Analytical Dimensions of Agency |
| 7 | `sections/06-analytical-framework.tex` | Analytical Framework |
| 8 | `sections/07-conclusion.tex` | Conclusion |

## Files

```
06-agents-part-1/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
├── sections/             # Section content
│   ├── 00-how-to-read.tex
│   ├── 01-introduction.tex
│   ├── 02-recognize-agent.tex
│   ├── 03-historical-journey.tex
│   ├── 04-disciplinary-perspectives.tex
│   ├── 05-analytical-dimensions.tex
│   ├── 06-analytical-framework.tex
│   └── 07-conclusion.tex
├── bib/                  # Bibliography
│   └── refs.bib
└── figures/              # Diagrams and images
    ├── hierarchy-diagram.tex
    ├── timeline.tex
    ├── maes-1994-clipping.png
    ├── park-2023-generative-agents.png
    └── xi-2023-agent-society.png
```

## Building

From chapter directory:
```bash
make pdf      # Build standalone chapter PDF
make clean    # Remove auxiliary files
```

From repository root:
```bash
make chapters # Build all chapter PDFs
```
