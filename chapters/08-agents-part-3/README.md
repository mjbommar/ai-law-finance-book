# Chapter: Agents - Part III: Governing AI Agents

**Subtitle**: Risk, Compliance, and Accountability in Law and Finance

## Overview

This chapter is Part III of a three-part series from the textbook *Artificial Intelligence for Law and Finance*. It translates the conceptual foundations from Part I and the tactical information from Part II into governance practice, addressing how to govern agentic systems responsibly for chief risk officers, compliance officers, general counsel, and senior leadership in regulated domains.

## Chapter Structure

| # | Section File | Section Title |
|---|--------------|---------------|
| 1 | `sections/01-howtoread.tex` | How to Read This Chapter |
| 2 | `sections/02-intro.tex` | Introduction: The Governance Imperative |
| 3 | `sections/03-dimensional_calibration.tex` | Design Principles: Dimensional Calibration |
| 4 | `sections/04-governance_stack.tex` | The Governance Stack: Overlapping Obligations |
| 5 | `sections/05-implementation.tex` | Implementation: Building Governance Systems |
| 6 | `sections/06-accountability.tex` | Accountability and Organizational Structure |
| 7 | `sections/07-examples.tex` | Examples in Context |
| 8 | `sections/08-conclusion.tex` | Conclusion: Synthesis and Path Forward |

## Files

```
08-agents-part-3/
├── main.tex              # Chapter entry point
├── Makefile              # Build configuration
├── sections/             # Section content
│   ├── 01-howtoread.tex
│   ├── 02-intro.tex
│   ├── 03-dimensional_calibration.tex
│   ├── 04-governance_stack.tex
│   ├── 05-implementation.tex
│   ├── 06-accountability.tex
│   ├── 07-examples.tex
│   └── 08-conclusion.tex
├── bib/                  # Bibliography
│   └── refs.bib
└── figures/              # TikZ figure definitions
    ├── fig-ai-acceptable-use-policy.tex
    ├── fig-autonomy-hic.tex
    ├── fig-autonomy-hitl.tex
    ├── fig-autonomy-hotl.tex
    ├── fig-escalation-example.tex
    ├── fig-escalation-tiers.tex
    ├── fig-five-layer-framework.tex
    ├── fig-governance-investment.tex
    ├── fig-hotl-dashboard.tex
    ├── fig-incident-email-closure.tex
    ├── fig-incident-email-discovery.tex
    ├── fig-incident-report-legal.tex
    ├── fig-incident-response-cycle.tex
    ├── fig-iterative-investigation.tex
    └── fig-vendor-diligence.tex
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
