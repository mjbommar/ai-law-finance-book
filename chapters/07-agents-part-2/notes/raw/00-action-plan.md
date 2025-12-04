# Chapter 07 Action Plan

**Generated**: November 27, 2025
**Purpose**: Master checklist for Chapter 07 (Agents Part II: How to Build an Agent) improvements

---

## Overview

This notes folder contains detailed research and recommendations for improving Chapter 07. The research was conducted by analyzing:

1. All other chapters in the textbook for boundary/overlap analysis
2. Chapter 06 (Part I) for GPA+IAT framework alignment
3. Canonical academic and industry resources not yet cited
4. November 2025 developments in AI agents

---

## File Index

| File | Purpose |
|------|---------|
| `01-chapter-boundaries.md` | What Part II should DEFINE vs. REFERENCE from other chapters |
| `02-gpa-iat-alignment.md` | Framework extraction from Part I and alignment gap analysis |
| `03-canonical-resources.md` | New citations with complete BibLaTeX entries |
| `04-november-2025-trends.md` | Recent developments to incorporate |
| `05-structural-additions.md` | New subsections and structural changes |
| `06-content-enhancements.md` | Section-by-section content improvements |
| `07-security-considerations.md` | Security patterns and concerns for agents |
| `08-legal-ai-case-studies.md` | Harvey, CoCounsel, and other legal AI examples |
| `09-protocol-comparison.md` | MCP vs A2A protocol analysis |
| `10-eu-ai-act-compliance.md` | Regulatory framework and compliance |

---

## Priority Action Items

### High Priority (Structural)

- [ ] Add new subsection: "How Part II Implements GPA+IAT" (after intro)
- [ ] Add architecture section opener mapping 3 pillars to 6 properties
- [ ] Add evaluation section opener mapping layers to properties
- [ ] Add MCP + A2A protocol comparison to protocols section

### High Priority (Content)

- [ ] Tools section: Add "Tool Use ≠ Agency" clarification box
- [ ] Memory section: Explain state preservation enables Iteration
- [ ] Planning section: Add autonomy spectrum mapping table
- [ ] Protocols section: Frame capability discovery as Perception

### Medium Priority (New Content)

- [ ] Add security considerations subsection
- [ ] Add legal AI case studies (Harvey, CoCounsel)
- [ ] Add EU AI Act four-pillar framework to synthesis
- [ ] Connect industry topologies to autonomy levels

### Medium Priority (Citations)

- [ ] Add MemGPT citation (memory architecture)
- [ ] Add Tree of Thoughts citation (reasoning patterns)
- [ ] Add A2A protocol citation (interoperability)
- [ ] Add AgentBench citation (evaluation)
- [ ] Add GAIA benchmark citation (evaluation)
- [ ] Add remaining ~10-15 canonical resources

### Lower Priority (Polish)

- [ ] Ensure all cross-references use `\Cref{}`
- [ ] Verify consistent terminology with Part I glossary
- [ ] Add November 2025 developments throughout
- [ ] Update Further Learning section with new resources

---

## Cross-Reference Summary

### References Part II Should Add

| Target | Source | Context |
|--------|--------|---------|
| `\Cref{sec:intro}` | Chapter 06 | GPA+IAT definitions |
| `\Cref{sec:rubric-6q}` | Chapter 06 | 6-question evaluation rubric |
| `\Cref{sec:dimensions}` | Chapter 06 | Autonomy spectrum, entity frames |
| `\Cref{sec:synthesis}` | Chapter 06 | Professional deployment requirements |
| `\Cref{sec:llmC-rag}` | Chapter 03 | RAG mechanics (already referenced) |
| `\Cref{sec:llmC-evidence}` | Chapter 03 | Evidence records (already referenced) |
| `\Cref{sec:llmC-tools}` | Chapter 03 | Tool contracts, governance metadata |
| `\Cref{sec:llmE-strategy}` | Chapter 05 | Reasoning pattern catalog |
| `\Cref{sec:llmD-eval}` | Chapter 05 | Evaluation methodology |
| `\Cref{sec:llmD-eval-retrieval-quick}` | Chapter 05 | Retrieval sanity checks (already referenced) |

---

## Validation Checklist

Before finalizing Chapter 07:

- [ ] All sections map to at least one GPA+IAT property
- [ ] No content duplicates what's defined in Chapters 02-06
- [ ] All new citations added to `bib/refs.bib`
- [ ] Cross-references use correct labels
- [ ] `make pdf` compiles without errors
- [ ] `make validate` shows no undefined references
- [ ] Consistent with Part I terminology
- [ ] November 2025 developments accurately dated and sourced

---

## Notes

- Part II is currently v0.1 working draft with sparse content
- Figures directory is empty - consider adding architecture diagrams
- Part III (Chapter 08) handles governance; Part II handles technical build
- Target audience: legal/finance professionals building or evaluating agents
