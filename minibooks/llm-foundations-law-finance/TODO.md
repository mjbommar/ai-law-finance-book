# LLM Foundations Minibook — Implementation Plan

**Status**: In Progress (Phases 1-11 Complete, Phase 12 Pending)
**Created**: 2024-12-28
**Target**: Standalone minibook paralleling "Agentic AI in Law and Finance"

---

## Book Identity

**Title**: LLM Essentials for Law and Finance
**Subtitle**: A Practitioner's Guide from Mechanics to Mastery

---

## Chapter Structure — Practitioner Journey

### The Arc

```
Foundation → Communication → Control → Application → Mastery
     ↓              ↓            ↓           ↓            ↓
  "What is      "How do I    "How do I   "How do I    "How do I
   this?"       talk to it?"  control it?" use it?"    get better?"
```

### Chapter Titles

| Ch | Title | Description | Stage |
|----|-------|-------------|-------|
| 1 | **What Am I Working With?** | Tokens, probabilities, and failure modes—understand the technology before you trust it. | Foundation |
| 2 | **How Do I Get It to Reason?** | Conversations, context, and chain-of-thought—patterns that turn chat into analysis. | Communication |
| 3 | **How Do I Get Reliable Output?** | Structured results, tool calls, and audit trails that satisfy compliance. | Control |
| 4 | **How Do I Handle Real Documents?** | Contracts, financials, images, and audio—multimodal workflows for regulated work. | Application |
| 5 | **How Do I Improve Systematically?** | Evaluation, versioning, and optimization—prompt engineering as discipline, not guesswork. | Mastery |

### Content Mapping (No Restructuring Required)

| Chapter | Current Sections (unchanged) | New Framing |
|---------|------------------------------|-------------|
| 1 | Tokens, sampling, embeddings, context windows, failure modes | "Before you can use it well, you need to know what it actually is" |
| 2 | Conversations, context management, reasoning patterns (CoT, ReAct) | "Now that you understand it, learn to communicate effectively" |
| 3 | Structured outputs, validation, function calling, RAG, Evidence Record | "Get outputs you can actually use and defend" |
| 4 | Documents, images, tables, audio, privacy/redaction | "Apply these skills to the materials you work with daily" |
| 5 | Design, evaluation, meta-prompting, threat modeling, versioning | "Move from ad-hoc prompting to systematic improvement" |

### Source Directory Mapping

| Minibook Chapter | Source Directory |
|------------------|------------------|
| `chapters/01-llm-mechanics/` | `chapters/01-foundations-llm-primer-mechanics/` |
| `chapters/02-conversations-reasoning/` | `chapters/02-foundations-conversations-reasoning/` |
| `chapters/03-structured-outputs-tools/` | `chapters/03-foundations-structured-outputs-tools/` |
| `chapters/04-multimodal/` | `chapters/04-foundations-multimodal/` |
| `chapters/05-prompt-engineering/` | `chapters/05-foundations-prompt-design-eval-optimization/` |

### Title Consistency Guidelines

All chapter titles:
- Start with interrogative ("What" or "How")
- Are 5-7 words
- Use practitioner voice ("I")
- Progress logically through the journey
- Match actual chapter content without requiring restructuring

---

## Cover Design

### Style Guidelines

- **Match agents minibook aesthetic** (professional, clean, modern)
- **No network diagrams** — use abstract geometric elements instead
- **pst-vectorian ornaments** for decorative elements
- **Background**: Gradient or subtle color wash
- **Geometric elements**: Circles, lines, abstract shapes
- **Color palette**: Complement agents book (consider blue/teal tones vs agents' palette)

### Print Specifications

- **Format**: US Trade 6" × 9"
- **Binding options**: Paperback (perfect bound), Hardcover (case laminate)
- **Printer**: Lulu

---

## Implementation Tasks

### Phase 1: Foundation Setup ✅ COMPLETE
- [x] 1.1 Create directory structure
- [x] 1.2 Create this TODO.md
- [x] 1.3 Copy preamble from agents minibook
- [x] 1.4 Adapt preamble metadata (title in headers.tex)
- [x] 1.5 Copy .gitignore from agents minibook
- [x] 1.6 Copy figures/icons/ (CC license icons)

### Phase 2: Copy Chapter Content ✅ COMPLETE
- [x] 2.1 Copy Ch1 sections (11 files)
- [x] 2.2 Copy Ch2 sections (8 files)
- [x] 2.3 Copy Ch2 figures (4 files)
- [x] 2.4 Copy Ch3 sections (10 files)
- [x] 2.5 Copy Ch4 sections (10 files)
- [x] 2.6 Copy Ch5 sections (12 files)

**Note**: Found 7 forward references to Ch 6-8 — to fix in Phase 11.8

### Phase 3: Create Chapter Loaders ✅ COMPLETE
- [x] 3.1 Create `chapters/01-llm-mechanics/chapter.tex` (11 sections)
- [x] 3.2 Create `chapters/02-conversations-reasoning/chapter.tex` (8 sections)
- [x] 3.3 Create `chapters/03-structured-outputs-tools/chapter.tex` (10 sections)
- [x] 3.4 Create `chapters/04-multimodal/chapter.tex` (10 sections)
- [x] 3.5 Create `chapters/05-prompt-engineering/chapter.tex` (12 sections)

### Phase 4: Bibliography ✅ COMPLETE
- [x] 4.1 Extract refs.bib from each source chapter (5 files, 1496 lines)
- [x] 4.2 Merge into single bib/refs.bib
- [x] 4.3 Deduplicate citation keys (removed 8 duplicates)
- [x] 4.4 Verified: 118 unique entries, valid BibTeX format

### Phase 5: Front Matter ✅ COMPLETE
- [x] 5.1 Create front-matter/cover/cover.tex (interior cover page)
- [x] 5.2 Adapt front-matter/title-page.tex from agents minibook
- [x] 5.3 Adapt front-matter/copyright.tex from agents minibook
- [x] 5.4 **WRITE** front-matter/preface.tex (new content)
- [x] 5.5 Create front-matter/how-to-read.tex (synthesize from chapters)
- [x] 5.6 Create front-matter/glossary-entries.tex (compile from chapters)

**Cover color scheme**: Blue/teal palette to differentiate from agents book (slate/copper)

### Phase 6: Back Matter ✅ COMPLETE
- [x] 6.1 **WRITE** back-matter/back-cover.tex (promotional copy with blue/teal theme)

### Phase 7: Main Book File ✅ COMPLETE
- [x] 7.1 Create main.tex based on agents minibook structure
- [x] 7.2 Update chapter includes (5 chapters with practitioner-focused titles)
- [x] 7.3 Update metadata and PDF info
- [x] 7.4 Configure front/back matter includes

### Phase 8: Build System ✅ COMPLETE
- [x] 8.1 Copy and adapt Makefile from agents minibook
- [x] 8.2 Update output filenames (llm-essentials-law-finance)
- [x] 8.3 Lulu cover support (simplified from agents book)

### Phase 9: Print Covers ✅ COMPLETE
- [x] 9.1 Create covers/cover-front.tex (blue/teal theme)
- [x] 9.2 Create covers/cover-back.tex (standalone back cover)
- [x] 9.3 Calculate spine width based on page count (423 pages → 1.013")
- [x] 9.4 Create combined lulu-cover.tex

### Phase 10: Documentation ✅ COMPLETE
- [x] 10.1 Create README.md for minibook
- [ ] 10.2 Update root README.md with new minibook entry

### Phase 11: Quality Assurance ✅ COMPLETE
- [x] 11.1 Build PDF (`make pdf`) — 423 pages, 1.4MB
- [x] 11.2 Fix compilation errors (figure paths, label references)
- [x] 11.3 Verify table of contents
- [x] 11.4 Check all cross-references resolve — `make validate` passes
- [x] 11.5 Verify bibliography renders — 118 entries
- [x] 11.6 Review figure placement
- [x] 11.7 Check for broken internal links
- [x] 11.8 Audit for references to chapters 6-10 — rewrote 14 forward references to point to companion volume

### Phase 12: Print Preparation
- [ ] 12.1 Build lulu interior PDF
- [ ] 12.2 Build lulu cover PDF
- [ ] 12.3 Verify margins and bleed
- [ ] 12.4 Test upload to Lulu

---

## Technical Notes

### Cross-Reference Audit

Before building, check for references to chapters outside 1-5:

```bash
# Check for chapter references
grep -rn "ch:agent\|ch:govern\|ch:design\|ch:kg" chapters/

# Check for section references to later chapters
grep -rn "sec:agent\|sec:govern\|sec:kg" chapters/
```

### Bibliography Merge Process

```bash
# Concatenate all refs.bib
cat ../../chapters/01-*/bib/refs.bib \
    ../../chapters/02-*/bib/refs.bib \
    ../../chapters/03-*/bib/refs.bib \
    ../../chapters/04-*/bib/refs.bib \
    ../../chapters/05-*/bib/refs.bib > bib/refs-merged.bib

# Then manually review for duplicates
```

### Glossary Term Extraction

```bash
# Find all keyterms used
grep -roh "\\\\keyterm{[^}]*}" ../../chapters/0[1-5]-*/sections/ | sort -u

# Find all glossary additions
grep -roh "\\\\glsadd{[^}]*}" ../../chapters/0[1-5]-*/sections/ | sort -u
```

### Section Title Consistency

When creating chapter.tex files, ensure section/subsection titles match the punchy style:
- Remove "Foundations:" prefix from section titles
- Keep titles concise but descriptive
- Maintain parallel structure across chapters

---

## Content to Write

### Preface (~500-800 words)

Key points to cover:
- Why this book exists (bridge AI and legal/financial practice)
- Who it's for (practitioners, not researchers)
- What you'll learn (practical LLM skills)
- How it relates to the agents book (this is foundations; that's applications)
- How to use this book (progressive curriculum)

### Back Cover Copy (~150 words)

- Hook/problem statement
- What the book delivers
- Key topics covered
- Author credentials (brief)
- Call to action

### How to Read This Book

Synthesize the individual chapter "how to read" sections into a cohesive book-level guide:
- Reading paths for different audiences
- Prerequisites
- Suggested order vs. reference use

---

## Open Questions

1. ~~**Title selection**~~ — ✅ DECIDED: "LLM Essentials for Law and Finance"
2. ~~**Subtitle selection**~~ — ✅ DECIDED: "A Practitioner's Guide from Mechanics to Mastery"
3. **Cover color palette** — Same as agents or differentiated?
4. **Glossary scope** — Full glossary or abbreviated?
5. **Cross-references to agents book** — Include "see also" notes or keep fully standalone?

---

## File Inventory (Post-Implementation)

```
minibooks/llm-foundations-law-finance/
├── TODO.md                     ← This file
├── README.md                   ← Documentation
├── main.tex                    ← Book entry point
├── Makefile                    ← Build automation
├── .gitignore
├── lulu-cover.tex              ← Print cover
├── preamble/
│   ├── main.tex
│   ├── commands.tex
│   └── tikz.tex
├── front-matter/
│   ├── cover/
│   │   └── cover.tex
│   ├── title-page.tex
│   ├── copyright.tex
│   ├── preface.tex
│   ├── how-to-read.tex
│   └── glossary-entries.tex
├── chapters/
│   ├── 01-llm-mechanics/
│   │   ├── chapter.tex
│   │   └── sections/
│   │       ├── 00-howtoread.tex
│   │       ├── 01-intro.tex
│   │       └── ...
│   ├── 02-conversations-reasoning/
│   ├── 03-structured-outputs-tools/
│   ├── 04-multimodal/
│   └── 05-prompt-engineering/
├── back-matter/
│   └── back-cover.tex
├── bib/
│   └── refs.bib
├── figures/
│   └── icons/
├── covers/
│   ├── cover-front.tex
│   └── cover-back.tex
├── scripts/
└── notes/
```

---

## Changelog

| Date | Change |
|------|--------|
| 2024-12-28 | Initial plan created |
| 2024-12-28 | Finalized title, subtitle, and chapter titles (practitioner journey framing) |
