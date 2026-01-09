# Chapter: Foundations - Conversations and Reasoning

**Subtitle**: Chat Mechanics, Memory, and Reasoning Patterns

## Overview

This chapter covers the transition from single-shot completions to multi-turn conversations, context management strategies, and the reasoning patterns that enable complex problem-solving.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 0 | `sections/00-howtoread.tex` | How to Read This Chapter |
| 1 | `sections/01-intro.tex` | Introduction and Scope |
| 2 | `sections/02-conversational-models.tex` | Conversational Models and State |
| 3 | `sections/03-reasoning-patterns.tex` | Reasoning Patterns and When to Use Them |
| 4 | `sections/04-strategy-selection.tex` | Choosing Strategies Under Constraints |
| 5 | `sections/05-synthesis.tex` | Synthesis: From Stateless Models to Cognitive Systems |
| 6 | `sections/06-furtherlearning.tex` | Further Learning |
| 7 | `sections/07-conclusion.tex` | Conclusion |

## Files

```
02-foundations-conversations-reasoning/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
├── sections/             # Section content
│   ├── 00-howtoread.tex
│   ├── 01-intro.tex
│   ├── 02-conversational-models.tex
│   ├── 03-reasoning-patterns.tex
│   ├── 04-strategy-selection.tex
│   ├── 05-synthesis.tex
│   ├── 06-furtherlearning.tex
│   └── 07-conclusion.tex
├── bib/                  # Bibliography
│   └── refs.bib
└── figures/              # TikZ figure definitions
    ├── fig-context-assembly.tex
    ├── fig-lost-middle.tex
    ├── fig-react-loop.tex
    └── fig-reasoning-patterns.tex
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
