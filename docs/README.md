# Documentation Hub

> **Purpose**: Central navigation for all documentation related to writing, building, and maintaining *Artificial Intelligence for Law and Finance*.

**Last Updated**: December 2025

---

## Quick Navigation

| I want to... | Go to... |
|--------------|----------|
| **Set up a new chapter** | [chapter-setup.md](#chapter-setupmd) |
| **Plan chapter content and page counts** | [content-planning.md](#content-planningmd) |
| **Write consistent prose** | [style-guide.md](#style-guidemd) |
| **Edit and polish text** | [prose-editing-checklist.md](#prose-editing-checklistmd) |
| **Use colors correctly** | [color-guide.md](#color-guidemd) |
| **Build the PDF** | [build-guide.md](#build-guidemd) |
| **Understand the full project** | [../CLAUDE.md](../CLAUDE.md) or [../AGENTS.md](../AGENTS.md) |

---

## Document Overview

### [chapter-setup.md](chapter-setup.md)
**Purpose**: Technical setup for creating and structuring chapters

**Key Contents**:
- Directory structure and file organization
- `main.tex` template (complete ~350-line preamble)
- Section file templates
- TikZ figure patterns and common errors
- Box environment usage
- Cross-chapter reference patterns
- "How to Read This Chapter" template
- "Further Learning" section template
- Naming conventions and label formats

**When to use**: Starting a new chapter, adding figures, troubleshooting LaTeX errors

---

### [content-planning.md](content-planning.md)
**Purpose**: Strategies for planning content, estimating pages, and expanding material

**Key Contents**:
- Page count estimation rules of thumb
- Content types ranked by expansion value
- Chapter structure patterns (comprehensive, focused, applied)
- Case study templates (3 patterns)
- Expansion strategies when under/over target
- Quality vs. quantity balance guidelines
- Planning workflow phases

**When to use**: Planning a new chapter, expanding existing content to meet page targets, deciding what content types to add

---

### [style-guide.md](style-guide.md)
**Purpose**: Writing standards for consistent, professional prose

**Key Contents**:
- Tone and voice guidelines
- Person and tense patterns by section type
- Terminology and key terms
- Cross-referencing standards
- Domain integration requirements (legal + financial examples)
- Section-specific guidelines
- Revision checklist

**When to use**: Writing new content, reviewing prose for consistency, ensuring domain coverage

---

### [prose-editing-checklist.md](prose-editing-checklist.md)
**Purpose**: Concrete patterns for improving sentence-level prose quality

**Key Contents**:
- Eliminating em-dash overuse
- Fixing fragment sentences
- Natural conjunctions and transitions
- Box and visual element design
- Table design patterns
- Voice and tone fixes
- Pre-edit and post-edit checklists

**When to use**: Editing existing drafts, polishing prose before finalization

---

### [color-guide.md](color-guide.md)
**Purpose**: Visual design system and semantic color usage

**Key Contents**:
- 4-layer color architecture
- Semantic color mappings
- Component-specific aliases
- Box color usage
- TikZ figure colors
- Legacy color migration

**When to use**: Creating new visual elements, ensuring color consistency, migrating from legacy colors

---

### [build-guide.md](build-guide.md)
**Purpose**: Build system architecture and compilation instructions

**Key Contents**:
- Dual-compilation system (standalone chapters + full book)
- Subfiles package usage
- Build commands and targets
- Troubleshooting common errors
- Bibliography management

**When to use**: Setting up build environment, debugging compilation errors, understanding how chapters integrate

---

## Master Checklists

### Starting a New Chapter

Use this checklist when creating a new chapter from scratch:

**Phase 1: Setup**
- [ ] Create directory structure: `mkdir -p chapters/XX-name/{sections,figures,bib}`
- [ ] Copy Makefile from existing chapter
- [ ] Create `main.tex` using template from [chapter-setup.md](chapter-setup.md)
- [ ] Create empty `bib/refs.bib`
- [ ] Test build with `make pdf`

**Phase 2: Planning** (see [content-planning.md](content-planning.md))
- [ ] Define 5-7 specific learning objectives
- [ ] Outline 4-6 major sections
- [ ] Calculate page estimates per section
- [ ] Verify total within target range (60-70 for comprehensive)
- [ ] Identify 3-4 case studies needed
- [ ] Identify 3-5 key figures to create
- [ ] Gather 15-25 core bibliography sources
- [ ] Brainstorm legal + financial examples for each section

**Phase 3: Structure Creation**
- [ ] Create `sections/howtoread.tex` using template
- [ ] Create section files with proper labels
- [ ] Create figure stubs in `figures/`
- [ ] Populate `bib/refs.bib` with initial sources

**Phase 4: Writing** (see [style-guide.md](style-guide.md))
- [ ] Write How to Read section
- [ ] Write Introduction with definitions
- [ ] Write core technical sections
- [ ] Include legal AND financial examples in each section
- [ ] Create TikZ figures
- [ ] Write case studies using templates
- [ ] Write Further Learning section
- [ ] Write Conclusion

**Phase 5: Review** (see [prose-editing-checklist.md](prose-editing-checklist.md))
- [ ] Apply prose editing checklist
- [ ] Verify domain balance
- [ ] Check all cross-references
- [ ] Validate bibliography entries
- [ ] Run `make validate`
- [ ] Final compilation and page count check

---

### Expanding an Existing Chapter

Use when a chapter is under the page target:

**Content Audit**
- [ ] Verify How to Read section exists with reading paths
- [ ] Check each major section for legal AND financial examples
- [ ] Count case studies (target: 3-4 for comprehensive chapter)
- [ ] Count figures (target: 3-5 for comprehensive chapter)

**High-Value Additions** (see [content-planning.md](content-planning.md))
- [ ] Add domain-specific implementation patterns
- [ ] Create structured case studies using templates
- [ ] Add Common Misconceptions subsection (4-5 items)
- [ ] Add Practitioner Exercises (4-6 exercises)
- [ ] Add Reading Sequence in Further Learning
- [ ] Expand annotated bibliography entries

**Quality Check**
- [ ] Verify new content passes 3-question test
- [ ] Apply prose editing checklist to new sections
- [ ] Ensure consistent depth across chapter
- [ ] Final compilation and page count verification

---

### Pre-Commit Checklist

Before committing chapter changes:

**Technical**
- [ ] `make pdf` compiles without errors
- [ ] `make validate` shows no undefined references
- [ ] All citations exist in `bib/refs.bib`
- [ ] All figures render correctly

**Content Quality**
- [ ] Voice consistent: "we" for analysis, "you" for guidance, no "I"
- [ ] Key terms use `\keyterm{}` on first use
- [ ] Cross-references use `\Cref{}`
- [ ] Legal and financial examples present

**Style Compliance**
- [ ] No excessive em-dashes
- [ ] No choppy fragment sentences
- [ ] Boxes used appropriately (not every paragraph)
- [ ] Figures illuminate concepts (not decorative)

**Metadata**
- [ ] All `\label{}` tags use correct chapter slug
- [ ] Bibliography entries include `urldate` for web sources
- [ ] Figure captions are descriptive

---

### Cross-Chapter Reference Checklist

When handling references to other chapters:

- [ ] No `\Cref{}` or `\ref{}` to labels outside current chapter
- [ ] All cross-chapter refs use `Chapter~N (Title)` format
- [ ] Signpost paragraphs added where detailed treatment exists elsewhere
- [ ] Part references use `Part~N (Title)` format
- [ ] Forward references within chapter use `\Cref{}`
- [ ] `make validate` shows no undefined reference warnings

---

### Domain Integration Checklist

For each major section, verify:

- [ ] At least one concrete legal application example
- [ ] At least one concrete financial application example
- [ ] Examples are substantive (not name-drops)
- [ ] Domain-specific concerns addressed (privilege, regulation, etc.)
- [ ] Terminology appropriate for each domain
- [ ] Neither domain dominates unfairly
- [ ] Governance implications noted where relevant

---

## Key Concepts Summary

### Chapter Slugs

| Chapter | Slug | Prefix |
|---------|------|--------|
| 01 | `llmA` | `sec:llmA-*` |
| 02 | `llmB` | `sec:llmB-*` |
| 03 | `llmC` | `sec:llmC-*` |
| 04 | `llmD` | `sec:llmD-*` |
| 05 | `llmE` | `sec:llmE-*` |
| 06 | `agents1` | `sec:agents1-*` |
| 07 | `agents2` | `sec:agents2-*` |
| 08 | `agents3` | `sec:agents3-*` |

### Box Types

| Box | Color | Use For |
|-----|-------|---------|
| `definitionbox` | Blue | Formal definitions |
| `keybox` | Amber | Key takeaways |
| `highlightbox` | Neutral | Notes, context |
| `cautionbox` | Red | Warnings |
| `theorembox` | Indigo | Formal statements |
| `listingbox` | Gray | Code examples |

### Voice Patterns

| Context | Voice |
|---------|-------|
| Analysis, synthesis | "we" |
| Direct guidance | "you" |
| Historical narrative | Third person |
| Never use | "I", "one" |

### Cross-Chapter Reference Patterns

| Reference Type | Pattern |
|----------------|---------|
| To other chapter | `Chapter~N (Title)` |
| To other part | `Part~N (Title)` |
| Signpost | `\paragraph{Signpost to Chapter~N.}` |
| Within chapter | `\Cref{sec:slug-topic}` |

### Page Estimation Quick Reference

| Content | Pages |
|---------|-------|
| Definition box | 0.3–0.5 |
| Case study | 1.5–2.5 |
| Major section | 5–10 |
| TikZ figure | 0.5–1 |
| Misconception | 0.3–0.5 |
| Exercise | 0.3–0.5 |

---

## Workflow Quick Reference

### New Chapter Workflow

```
1. Setup (chapter-setup.md)
   └─ Directory, Makefile, main.tex, refs.bib

2. Plan (content-planning.md)
   └─ Objectives, sections, estimates, examples

3. Write (style-guide.md)
   └─ Sections, figures, case studies, bibliography

4. Edit (prose-editing-checklist.md)
   └─ Flow, transitions, boxes, domain balance

5. Validate
   └─ make pdf, make validate, checklists
```

### Expansion Workflow

```
1. Assess current state
   └─ Page count, domain coverage, case studies

2. Identify gaps (content-planning.md)
   └─ Missing patterns, case studies, exercises

3. Expand with high-value content
   └─ Implementation patterns, case studies, misconceptions

4. Edit (prose-editing-checklist.md)
   └─ Integrate new content smoothly

5. Validate
   └─ Page count, quality check
```

### Editing Workflow

```
1. Pre-edit scan (prose-editing-checklist.md)
   └─ Em-dashes, fragments, box density

2. Apply fixes
   └─ Conjunctions, transitions, flowing prose

3. Verify voice (style-guide.md)
   └─ "we"/"you" pattern, domain balance

4. Final polish
   └─ Read aloud, check compilation
```

---

## Document Relationships

```
CLAUDE.md (project entry point)
    │
    ├── AGENTS.md (evidence standards, file conventions)
    │
    └── docs/
        │
        ├── README.md (this file - navigation hub)
        │
        ├── chapter-setup.md
        │   └── Technical setup, templates, TikZ, labels
        │
        ├── content-planning.md
        │   └── Page estimates, expansion, case studies
        │
        ├── style-guide.md
        │   └── Voice, tone, domain integration
        │
        ├── prose-editing-checklist.md
        │   └── Sentence-level improvements
        │
        ├── color-guide.md
        │   └── Visual design system
        │
        └── build-guide.md
            └── Compilation, subfiles, troubleshooting
```

---

## Changelog

| Date | Change | Reason |
|------|--------|--------|
| 2025-12-21 | Initial creation | Consolidate documentation navigation |

---

## Contributing to Documentation

When you discover patterns or encounter issues not covered:

1. **Identify the appropriate document** using the table above
2. **Add the pattern or fix** with examples
3. **Update the changelog** in that document
4. **Update this README** if adding major new content

Documentation should be:
- **Concrete**: Include examples and templates
- **Actionable**: Tell readers what to do, not just what exists
- **Navigable**: Use clear headings and cross-references
- **Current**: Update when patterns change
