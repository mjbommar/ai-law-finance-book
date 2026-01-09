# Chapter: Foundations - LLM Primer and Mechanics

**Subtitle**: Conceptual Primer, History, Tokens, and Sampling

## Overview

This chapter introduces modern LLMs for legal and financial practitioners. It covers a conceptual primer and brief history, then explains tokens, tokenizers, context windows, and completion sampling.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 0 | `sections/00-howtoread.tex` | How to Read This Chapter |
| 1 | `sections/01-intro.tex` | Introduction and Scope |
| 2 | `sections/02-history-primer.tex` | Conceptual Primer and Brief History |
| 3 | `sections/03-tokens-sampling.tex` | Tokens, Tokenizers, and Context Windows |
| 4 | `sections/04-sampling.tex` | Sampling and Decoding: Controlling Generation |
| 5 | `sections/05-prompt-fundamentals.tex` | Prompt Fundamentals (First Touch) |
| 6 | `sections/06-representations-embeddings.tex` | Representations and Embeddings |
| 7 | `sections/07-failure-modes.tex` | Common Failure Modes and Why They Happen |
| 8 | `sections/08-synthesis.tex` | Synthesis: From Mechanics to Practice |
| 9 | `sections/09-furtherlearning.tex` | Further Learning |
| 10 | `sections/10-conclusion.tex` | Conclusion |

## Files

```
01-foundations-llm-primer-mechanics/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
├── sections/             # Section content
│   ├── 00-howtoread.tex
│   ├── 01-intro.tex
│   ├── 02-history-primer.tex
│   ├── 03-tokens-sampling.tex
│   ├── 04-sampling.tex
│   ├── 05-prompt-fundamentals.tex
│   ├── 06-representations-embeddings.tex
│   ├── 07-failure-modes.tex
│   ├── 08-synthesis.tex
│   ├── 09-furtherlearning.tex
│   └── 10-conclusion.tex
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
