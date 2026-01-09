# Chapter: Foundations - Prompt Design, Evaluation, and Optimization

**Subtitle**: Specifications, Tests, Meta-Prompting, and Change Management

## Overview

Treat prompts as specifications, measure results, and optimize safely with rubrics, self-critique, and versioning. This chapter turns prompting into an engineering discipline: specify, measure, and improve.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 0 | `sections/00-howtoread.tex` | How to Read This Chapter |
| 1 | `sections/01-intro.tex` | Introduction and Scope |
| 2 | `sections/02-prompt-design.tex` | Prompt Design as Specification |
| 3 | `sections/03-strategy-catalog.tex` | Strategy Catalog: Architectural Patterns |
| 4 | `sections/04-evaluation.tex` | Prompt Evaluation and Test Sets |
| 5 | `sections/05-telemetry-monitoring.tex` | Telemetry, Monitoring, and Evidence Pipelines |
| 6 | `sections/06-meta-prompting.tex` | Meta-Prompting and Self-Critique |
| 7 | `sections/07-threat-model-redteam.tex` | Threat Modeling and Red-Teaming |
| 8 | `sections/08-optimization-versioning.tex` | Optimization, Versioning, and Change Management |
| 9 | `sections/09-synthesis.tex` | Synthesis |
| 10 | `sections/10-furtherlearning.tex` | Further Learning |
| 11 | `sections/11-conclusion.tex` | Conclusion |

## Files

```
05-foundations-prompt-design-eval-optimization/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
├── sections/             # Section content
│   ├── 00-howtoread.tex
│   ├── 01-intro.tex
│   ├── 02-prompt-design.tex
│   ├── 03-strategy-catalog.tex
│   ├── 04-evaluation.tex
│   ├── 05-telemetry-monitoring.tex
│   ├── 06-meta-prompting.tex
│   ├── 07-threat-model-redteam.tex
│   ├── 08-optimization-versioning.tex
│   ├── 09-synthesis.tex
│   ├── 10-furtherlearning.tex
│   └── 11-conclusion.tex
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
