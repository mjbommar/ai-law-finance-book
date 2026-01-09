# Chapter: Knowledge Graphs & Semantic Web - Operations with LLMs

**Subtitle**: Build, Validate, Govern, and Use

## Overview

This chapter covers operational pipelines for building and governing knowledge graphs with LLM assistance, hybrid retrieval (symbolic + vector), and evaluation aligned to the book's governance patterns.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 1 | `sections/pipeline.tex` | Ingestion and Mapping Pipeline |
| 2 | `sections/provenance.tex` | Provenance and Versioning |
| 3 | `sections/llm_assisted.tex` | LLM-Assisted Construction and Curation |
| 4 | `sections/hybrid_retrieval.tex` | Hybrid Retrieval: SPARQL + Text/Vector |
| 5 | `sections/examples.tex` | Domain Examples |
| 6 | `sections/evaluation_ops.tex` | Evaluation and Operations |

## Files

```
10-kg-operations-llm/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
└── sections/             # Section content
    ├── pipeline.tex
    ├── provenance.tex
    ├── llm_assisted.tex
    ├── hybrid_retrieval.tex
    ├── examples.tex
    └── evaluation_ops.tex
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
