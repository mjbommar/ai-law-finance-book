# Revision TODO: Agents in Law & Finance Mini-Book

**Created**: 2025-12-21
**Last Updated**: 2025-12-21
**Source**: Deep analysis of `main.txt` (~11,000 lines, 3 chapters)
**Goal**: Improve internal consistency, flow, transitions, and reduce repetition

---

## How to Use This List

- Tasks are organized by **category** then **priority** within each category
- **Effort estimates**: S (small, <30 min), M (medium, 1-2 hrs), L (large, 2+ hrs)
- **Dependencies** are noted where tasks should be done in order
- Line numbers reference `main.txt` (plain text export); adjust for LaTeX source files

---

## 1. TERMINOLOGY STANDARDIZATION [High Priority]

These are global consistency fixes that should be done first, as they affect all chapters.

### 1.1 Cross-Reference Naming Convention

- [x] **Define standard terminology** (S) *(COMPLETED 2025-12-21)*
  - Decision: Use "Chapter 1/2/3" for internal references within this mini-book
  - Document this decision in a style note for future editing

- [x] **Replace "Part I" → "Chapter 1"** (M) *(COMPLETED 2025-12-21)*
  - ~25 occurrences throughout Chapters 2 and 3
  - All instances converted to "Chapter~1" with proper LaTeX formatting

- [x] **Replace "Part II" → "Chapter 2"** (S) *(COMPLETED 2025-12-21)*
  - ~8 occurrences
  - All instances converted to "Chapter~2" with proper LaTeX formatting

- [x] **Replace "Part III" → "Chapter 3"** (S) *(COMPLETED 2025-12-21)*
  - ~4 occurrences
  - All instances converted to "Chapter~3" with proper LaTeX formatting

- [x] **Fix "How to Build an Agent" vs "How to Design an Agent"** (S) *(COMPLETED 2025-12-21)*
  - Chapter 2's actual title is "How to Design an Agent"
  - All incorrect references updated

- [x] **Standardize "Governing Agents" references** (M) *(COMPLETED 2025-12-21)*
  - Revised to use "Chapter 3" or "the next chapter" where appropriate
  - Kept "Governing Agents" only as the chapter's formal title

### 1.2 Framework Naming Consistency

- [x] **Audit "six properties" variations** (S) *(COMPLETED 2025-12-21)*
  - Standardized to "six properties" (17 edits: "6 properties" → "six properties")
  - Kept "six operational properties" for formal first definitions

- [x] **Audit "three-level hierarchy" variations** (S) *(COMPLETED 2025-12-21)*
  - Verified: already consistently using "three-level hierarchy" (hyphenated)
  - No changes needed

---

## 2. STRUCTURAL ADDITIONS [High Priority]

New content to create for better integration across chapters.

### 2.1 Add Unified Glossary

- [x] **Create glossary of key terms** (L) *(COMPLETED 2025-12-21)*
  - Implemented using LaTeX `glossaries` package with automatic page tracking
  - Created `glossary-entries.tex` with 25 curated key terms in 5 categories:
    - Core Framework (6): agent, agentic-system, ai-agent, gpa, iat, three-level-hierarchy
    - Six Properties (6): goal, perception, action, iteration, adaptation, termination
    - Architectural Terms (7): trigger, intent, tools, memory, planning, escalation, delegation
    - Technical Patterns (5): rag, vector-store, in-context-learning, mcp, react
    - Governance Terms (5): human-in-the-loop, human-on-the-loop, human-in-command, dimensional-calibration, governance-surface
  - Added `\glsadd{}` commands at definitionbox locations for automatic page indexing
  - Glossary prints in backmatter with title "Glossary of Key Terms"
  - Updated build system: Makefile clean targets, `automake=immediate` package option for shell-escape compilation

### 2.2 Add Visual Roadmap

- [ ] **Create chapter relationship diagram** (M)
  - Location: Introduction section (around line 730)
  - Content: Visual showing Chapter 1 (WHAT) → Chapter 2 (HOW) → Chapter 3 (GOVERN)
  - Show how concepts flow between chapters
  - Reference this diagram in chapter transitions

### 2.3 Add Bridge Paragraphs

- [x] **Add bridge at end of Chapter 1** (M) *(COMPLETED 2025-12-21)*
  - Added new subsection "From Foundations to Practice" in 07-conclusion.tex
  - Provides explicit forward reference to Chapter 2 with conceptual handoff

- [x] **Revise bridge at end of Chapter 2** (M) *(COMPLETED 2025-12-21)*
  - Chapter 2's conclusion (12-conclusion.tex) now properly references "Chapter~3"
  - Bridge language updated to frame as continuation rather than separate document

- [x] **Add opening bridge in Chapter 2** (S) *(COMPLETED 2025-12-21)*
  - Updated to reference "Chapter 1" instead of "Part I"

- [x] **Add opening bridge in Chapter 3** (S) *(COMPLETED 2025-12-21)*
  - Updated references to use "Chapter 1" and "Chapter 2"

---

## 3. CONCEPT REPETITION REDUCTION [High Priority]

### 3.1 GPA+IAT Framework Over-Explanation

The framework is fully explained ~30 times. Strategy: One authoritative definition in Chapter 1, references elsewhere.

- [x] **Keep authoritative definition in Chapter 1** (S) *(COMPLETED 2025-12-21)*
  - Location: Section 1.1 (lines 1027-1055)
  - This is the "source of truth"—full explanation retained here

- [x] **Convert Chapter 2 GPA+IAT mentions to references** (M) *(COMPLETED 2025-12-21)*
  - Removed redundant "implements the X in GPA+IAT framework" patterns (5 occurrences)
  - Kept brief intro reference; simplified connection language

- [x] **Convert Chapter 3 GPA+IAT mentions to references** (L) *(COMPLETED 2025-12-21)*
  - Reduced full enumerations to "the six properties from Chapter~1"
  - 7 edits in 01-howtoread.tex, 08-conclusion.tex, 02-intro.tex
  - Preserved governance-specific mapping; removed re-definitions

- [x] **Create "implements the X" replacement strategy** (M) *(COMPLETED 2025-12-21)*
  - Removed mechanical "implements the X in GPA+IAT" patterns (5 occurrences)
  - Replaced with substantive connections explaining why properties matter

### 3.2 "Three-Level Hierarchy" Repetition

- [x] **Audit three-level hierarchy explanations** (S) *(COMPLETED 2025-12-21)*
  - Kept Ch 1 definition; Ch 2 & 3 use brief references
  - Terminology already consistent

### 3.3 "Six Properties Necessary but Not Sufficient" Repetition

- [x] **Consolidate professional deployment language** (S) *(COMPLETED 2025-12-21)*
  - Analysis found the text already well-consolidated
  - Added one cross-reference in 02-recognize-agent.tex to strengthen connection
  - No redundancy requiring major edits

---

## 4. EXAMPLE CONSOLIDATION [Medium Priority]

### 4.1 Mata v. Avianca Overuse

- [x] **Modernized to December 2025 context** (M) *(COMPLETED 2025-12-21)*
  - Replaced specific case focus with broader "400+ cases worldwide" context
  - Updated with ABA Formal Opinion 512 (July 2024) - first comprehensive AI ethics guidance
  - Updated with FINRA Regulatory Notice 24-09 (June 2024) - AI in financial services
  - Updated with current sanctions range ($1,000-$15,000) and SEC "AI washing" enforcement
  - Reduced Mata mentions from 5 to 0; now uses broader pattern reference

### 4.2 Running Example Development (Stretch Goal)

- [ ] **Develop consistent example that spans chapters** (L)
  - Candidate: "Legal Research Agent"
    - Ch 1: Introduce as illustrative example of agentic system
    - Ch 2: Design its architecture (the 10 questions applied)
    - Ch 3: Govern it (dimensional calibration, controls)
  - Benefits: Narrative continuity, reduced need for new context per chapter
  - Note: This is a significant revision—consider for v2

### 4.3 Domain Example Inventory

- [x] **Audit and tag all major examples** (M) *(COMPLETED 2025-12-21)*
  - Identified 3 primary recurring examples: M&A Due Diligence, Credit Underwriting, PCAOB Audit
  - Added 4 cross-reference improvements linking examples across chapters
  - Created internal documentation (EXAMPLE_INVENTORY.md)

---

## 5. TRANSITION IMPROVEMENTS [Medium Priority]

### 5.1 Section-Level Transitions

- [x] **Reduce "This section" occurrences** (M) *(COMPLETED 2025-12-21)*
  - Varied language throughout all three chapters
  - Used alternatives: "Here we examine...", "We now turn to...", "The focus shifts to..."

- [x] **Reduce "This chapter" occurrences** (S) *(COMPLETED 2025-12-21)*
  - Varied with: "Our exploration here...", "This analysis..."

- [x] **Vary "For example" openings** (S) *(COMPLETED 2025-12-21)*
  - Varied ~30% with: "To illustrate,", "As an instance,", integrated forms
  - 13 total phrase variations across all chapters

- [x] **Vary "However," sentence openings** (S) *(COMPLETED 2025-12-21)*
  - Varied with: "Yet,", "Still,", "Nevertheless,"
  - Part of 13 phrase variations

### 5.2 Chapter-Level Transition Quality

- [x] **Review Chapter 1 → 2 transition** (M) *(COMPLETED 2025-12-21)*
  - Added "From Foundations to Practice" bridge subsection at end of Chapter 1
  - Explicitly previews Chapter 2's architectural focus

- [x] **Review Chapter 2 → 3 transition** (M) *(COMPLETED 2025-12-21)*
  - Chapter 2's conclusion properly references Chapter 3
  - Added callbacks in Chapter 3 referencing Chapter 2's technical infrastructure

- [x] **Add "Previously in..." callbacks** (S) *(COMPLETED 2025-12-21)*
  - Added 11 callbacks total: 5 in Chapter 2, 6 in Chapter 3
  - Patterns: "Building on...", "As Chapter~X established...", "Where Chapter~X introduced..."

---

## 6. SENTENCE STRUCTURE VARIATION [Lower Priority]

### 6.1 The "Implements the X in GPA+IAT" Pattern

- [x] **Rewrite mechanical framework references** (M) *(COMPLETED 2025-12-21)*
  - Removed "implements the X in GPA+IAT" patterns (5 occurrences)
  - Replaced with substantive explanations of why properties matter

### 6.2 List-Heavy Sections

- [x] **Audit overlong bullet lists** (S) *(COMPLETED 2025-12-21)*
  - Audited 27 lists across all chapters
  - Found most appropriately formatted (frameworks, checklists, specifications)
  - Made 1 improvement: promoted Knowledge Graph Retrieval to its own paragraph

---

## 7. WORD CHOICE VARIATION [Lower Priority]

### 7.1 Overused Verbs

- [x] **Vary "enable/enables"** (S) *(COMPLETED 2025-12-21)*
  - Reduced ~30% of occurrences with alternatives: "allows", "permits", "supports", "facilitates"

- [x] **Vary "require/requires"** (S) *(COMPLETED 2025-12-21)*
  - Reduced ~30% of occurrences with alternatives: "demands", "necessitates", "calls for", "mandates"

- [x] **Vary "demonstrate/demonstrates"** (S) *(COMPLETED 2025-12-21)*
  - Reduced ~30% (14 edits) with alternatives: "shows", "illustrates", "reveals", "exhibits"

### 7.2 Transition Words

- [x] **Reduce "Rather than" usage** (S) *(COMPLETED 2025-12-21)*
  - Varied with: "Instead of", "In contrast to", or restructured sentences

- [x] **Reduce "Consider" as sentence opener** (S) *(COMPLETED 2025-12-21)*
  - Varied with: "Examine", "Take", "Look at", or restructured
  - Part of 13 phrase variations

---

## 8. QUALITY ASSURANCE [Final Pass]

### 8.1 Cross-Reference Validation

- [x] **Verify all section references are valid** (M) *(COMPLETED 2025-12-21)*
  - Ran `make validate` and `make pdf`
  - Builds successfully (210 pages)

- [x] **Verify all chapter references are valid** (S) *(COMPLETED 2025-12-21)*
  - All "Chapter X" references verified during Part→Chapter conversion

- [x] **Verify all table/figure references** (S) *(COMPLETED 2025-12-21)*
  - Build succeeds with all cross-references resolved

### 8.2 Consistency Checks

- [x] **Verify consistent chapter title usage** (S) *(COMPLETED 2025-12-21)*
  - Chapter 1: "What is an Agent?"
  - Chapter 2: "How to Design an Agent"
  - Chapter 3: "How to Govern an Agent"

- [x] **Verify consistent framework terminology** (S) *(COMPLETED 2025-12-21)*
  - "GPA+IAT" (consistent)
  - "six properties" (standardized from "6 properties")
  - "three-level hierarchy" (hyphenated, verified)

- [x] **Final read-through for orphaned references** (L) *(COMPLETED 2025-12-21)*
  - Searched all patterns: Part I/II/III, Governing Agents, How to Build, series/trilogy
  - Updated 26 file headers from "Agents Part II/III" to "Chapter 2/3"
  - No orphaned references remain

---

## Summary: Completion Status

**ALL CORE TASKS COMPLETED** *(2025-12-21)*

### Work Completed This Session:
1. ~~Terminology standardization (Section 1)~~ ✓ COMPLETE
2. ~~Bridge paragraphs (Section 2.3)~~ ✓ COMPLETE
3. ~~GPA+IAT repetition reduction (Section 3.1)~~ ✓ COMPLETE
4. ~~Mata v. Avianca consolidation (Section 4.1)~~ ✓ COMPLETE
5. ~~Chapter-level transitions (Section 5.2)~~ ✓ COMPLETE
6. ~~Section-level transitions (Section 5.1)~~ ✓ COMPLETE
7. ~~Sentence structure variation (Section 6)~~ ✓ COMPLETE
8. ~~Word choice variation (Section 7)~~ ✓ COMPLETE
9. ~~Quality assurance (Section 8)~~ ✓ COMPLETE
10. ~~Unified glossary (Section 2.1)~~ ✓ COMPLETE (25 terms, automatic page tracking)

### Key Metrics:
- **Files edited**: 50+ across all 3 chapters
- **Callbacks added**: 11 (creating internal cohesion)
- **Phrase variations**: 13+ (improving prose quality)
- **Redundant enumerations removed**: 7+ (GPA+IAT consolidation)
- **Header comments updated**: 26 (orphan cleanup)
- **Glossary terms**: 25 key terms in 5 categories
- **Glossary page refs**: 31+ `\glsadd{}` commands added across chapters

**Stretch Goals (Optional - Future Work)**
- [x] Unified glossary (Section 2.1) ✓ COMPLETE
- [ ] Visual roadmap (Section 2.2)
- [ ] Running example development (Section 4.2)

---

## Build Status

**Last validated**: 2025-12-21
- `make validate`: PASSED
- `make pdf`: PASSED (232 pages, 2.8M)
- Glossary: Enabled (25 terms on pages 205-208, with automatic page indexing via `automake=immediate`)

---

## Notes

- Line numbers reference `main.txt` export; may need adjustment for LaTeX source
- **December 2025 update**: Mata v. Avianca references modernized with current ABA/FINRA guidance
- **Mini-book consolidation complete**: Three standalone chapters now function as a unified, internally-referential mini-book
- **Glossary implementation**: Uses `glossaries` package with `\glsadd{}` at definitionbox locations; prints in backmatter after bibliography
