# Chapter: Foundations - Structured Outputs and Tool Use

**Subtitle**: Schemas, Validation, and Function Calling

## Overview

Turn chats into systems: reliable JSON and function calls with governance metadata. Multimodal inputs are covered in a dedicated chapter.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 0 | `sections/00-howtoread.tex` | How to Read This Chapter |
| 1 | `sections/01-intro.tex` | Introduction and Scope |
| 2 | `sections/02-grounding-retrieval.tex` | Grounding and Retrieval Basics (RAG 101) |
| 3 | `sections/03-evidence-record.tex` | Canonical Evidence Record |
| 4 | `sections/04-structured-outputs.tex` | Structured Outputs with Validation |
| 5 | `sections/05-tool-use.tex` | Tool Use and Function Calling |
| 6 | `sections/06-pitfalls-practices.tex` | Pitfalls and Best Practices |
| 7 | `sections/07-synthesis.tex` | Synthesis |
| 8 | `sections/08-furtherlearning.tex` | Further Learning |
| 9 | `sections/09-conclusion.tex` | Conclusion |

## Files

```
03-foundations-structured-outputs-tools/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
├── sections/             # Section content
│   ├── 00-howtoread.tex
│   ├── 01-intro.tex
│   ├── 02-grounding-retrieval.tex
│   ├── 03-evidence-record.tex
│   ├── 04-structured-outputs.tex
│   ├── 05-tool-use.tex
│   ├── 06-pitfalls-practices.tex
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
