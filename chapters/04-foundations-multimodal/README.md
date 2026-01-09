# Chapter: Foundations - Multimodal Fundamentals

**Subtitle**: PDFs, Layout, Tables/Charts, Images, and Audio

## Overview

Practical multimodal workflows for legal and finance: preserve structure, extract tables, summarize audio, and protect privacy.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 0 | `sections/00-howtoread.tex` | How to Read This Chapter |
| 1 | `sections/01-intro.tex` | Introduction and Scope |
| 2 | `sections/02-images-visual.tex` | Images and Visual Content |
| 3 | `sections/03-document-structure.tex` | Document Structure and Layout |
| 4 | `sections/04-tables-charts.tex` | Tables and Charts |
| 5 | `sections/05-audio-transcripts.tex` | Audio and Transcripts |
| 6 | `sections/06-privacy-redaction.tex` | Privacy and Redaction |
| 7 | `sections/07-synthesis.tex` | Synthesis |
| 8 | `sections/08-furtherlearning.tex` | Further Learning |
| 9 | `sections/09-conclusion.tex` | Conclusion |

## Files

```
04-foundations-multimodal/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
├── sections/             # Section content
│   ├── 00-howtoread.tex
│   ├── 01-intro.tex
│   ├── 02-images-visual.tex
│   ├── 03-document-structure.tex
│   ├── 04-tables-charts.tex
│   ├── 05-audio-transcripts.tex
│   ├── 06-privacy-redaction.tex
│   ├── 07-synthesis.tex
│   ├── 08-furtherlearning.tex
│   └── 09-conclusion.tex
└── bib/                  # Bibliography
    └── refs.bib
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
