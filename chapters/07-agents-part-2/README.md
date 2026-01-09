# Chapter: Agents - Part II: How to Design an Agent

**Subtitle**: Architectures, Protocols, and Technical Evaluation

## Overview

This chapter is Part II of a three-part series from the textbook *Artificial Intelligence for Law and Finance*. It addresses architectures, protocols, and technical evaluation for designing agentic systems, organizing key architectural decisions into ten questions that guide building, evaluating, deploying, and governing agents.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 1 | `sections/00-how-to-read.tex` | How to Read This Chapter |
| 2 | `sections/01-introduction.tex` | Introduction |
| 3 | `sections/02-triggers.tex` | How Does an Agent Know When It Has Work to Do? |
| 4 | `sections/03-intent.tex` | How Does an Agent Understand What's Being Asked? |
| 5 | `sections/04-perception.tex` | How Does an Agent Find Things Out? |
| 6 | `sections/05-action.tex` | How Does an Agent Make Things Happen? |
| 7 | `sections/06-memory.tex` | How Does an Agent Remember Things? |
| 8 | `sections/07-planning.tex` | How Does an Agent Break a Big Job into Steps? |
| 9 | `sections/08-termination.tex` | How Does an Agent Know When It's Done? |
| 10 | `sections/09-escalation.tex` | How Does an Agent Know When to Ask for Help? |
| 11 | `sections/10-delegation.tex` | How Does an Agent Work with Other Agents? |
| 12 | `sections/11-governance.tex` | How Do We Design Systems That Can Be Governed? |
| 13 | `sections/12-conclusion.tex` | Conclusion |

## Files

```
07-agents-part-2/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
├── sections/             # Section content
│   ├── 00-how-to-read.tex
│   ├── 01-introduction.tex
│   ├── 02-triggers.tex
│   ├── 03-intent.tex
│   ├── 04-perception.tex
│   ├── 05-action.tex
│   ├── 06-memory.tex
│   ├── 07-planning.tex
│   ├── 08-termination.tex
│   ├── 09-escalation.tex
│   ├── 10-delegation.tex
│   ├── 11-governance.tex
│   └── 12-conclusion.tex
├── bib/                  # Bibliography
│   └── refs.bib
└── figures/              # TikZ figure definitions
    ├── agent-loop.tex
    ├── eval-layers.tex
    ├── fig-hierarchical-planning.tex
    ├── fig-orchestration-patterns.tex
    ├── fig-oversight-spectrum.tex
    ├── fig-rag-pipeline.tex
    ├── fig-react-cycle.tex
    ├── fig-reliability-cliff.tex
    ├── fig-reversibility-spectrum.tex
    ├── fig-trigger-channels.tex
    ├── fig-when-to-clarify.tex
    ├── mcp-architecture.tex
    ├── pattern-selection.tex
    └── react-loop.tex
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
