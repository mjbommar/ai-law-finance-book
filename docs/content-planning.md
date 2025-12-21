# Content Planning Guide

> **Purpose**: Strategies for planning chapter content, estimating page counts, and expanding material to meet targets while maintaining quality.

**Last Updated**: December 2025

---

## Table of Contents

1. [Page Count Estimation](#page-count-estimation)
2. [Content Types That Expand Well](#content-types-that-expand-well)
3. [Chapter Structure Patterns](#chapter-structure-patterns)
4. [Case Study Templates](#case-study-templates)
5. [Expansion Strategies](#expansion-strategies)
6. [Quality vs. Quantity Balance](#quality-vs-quantity-balance)
7. [Planning Workflow](#planning-workflow)
8. [Checklists](#checklists)

---

## Page Count Estimation

Understanding how different content types contribute to page count helps with planning.

### Rules of Thumb

| Content Type | Approximate Pages | Notes |
|--------------|-------------------|-------|
| **Definition box** | 0.3–0.5 pages | Depends on definition length |
| **Key box** | 0.4–0.6 pages | Often includes lists |
| **Highlight box** | 0.2–0.4 pages | Usually shorter |
| **Major section** (with 3-4 subsections) | 5–10 pages | Core content unit |
| **Subsection** (with paragraphs) | 1–3 pages | Varies by depth |
| **Case study** (full structure) | 1.5–2.5 pages | Scenario + analysis + recommendation |
| **TikZ figure** (with caption) | 0.5–1 page | Depends on complexity |
| **Table** (5-10 rows) | 0.3–0.5 pages | Plus caption |
| **Annotated bibliography entry** | 0.15–0.25 pages | ~3-4 sentences each |
| **Exercise** (with steps) | 0.3–0.5 pages | Numbered steps + outcome |

### Section-Level Estimates

| Section Type | Typical Pages | Content Mix |
|--------------|---------------|-------------|
| **How to Read** | 3–4 pages | Boxes, lists, brief prose |
| **Introduction** | 4–6 pages | Prose, 1-2 boxes, definitions |
| **Core Technical Section** | 8–15 pages | Heavy prose, figures, boxes |
| **Strategy/Decision Section** | 6–10 pages | Tables, decision trees, examples |
| **Case Studies Section** | 6–10 pages | 3-4 structured case studies |
| **Synthesis/Bridge** | 3–5 pages | Summary boxes, forward refs |
| **Further Learning** | 5–8 pages | Annotated bibs, exercises |
| **Conclusion** | 1–2 pages | Brief summary |
| **Bibliography** | 2–4 pages | Depends on citation count |

### Target Page Count by Chapter Type

| Chapter Type | Target Pages | Rationale |
|--------------|--------------|-----------|
| **Foundational** (Part I) | 50–70 pages | Comprehensive coverage, many examples |
| **Technical** (Part II) | 40–60 pages | Focused depth, heavy figures |
| **Applied/Governance** (Part III) | 35–50 pages | Framework-focused, case-heavy |
| **Mini-chapter** | 20–30 pages | Single-topic deep dive |

---

## Content Types That Expand Well

When you need to increase page count while maintaining quality, these content types add substantive value:

### Tier 1: High-Value Expansion (Strongly Recommended)

#### Domain-Specific Implementation Patterns

Add sections that show how concepts apply specifically to legal and financial contexts:

```latex
\subsection{Implementation Patterns for Professional Applications}

Before synthesizing the architecture, we examine specific patterns that
arise in legal and financial contexts.

\subsubsection{Legal Conversation Patterns}

\paragraph{Privilege Protection.} Attorney-client privilege considerations
must be embedded in the system architecture...

\paragraph{Jurisdictional Awareness.} Legal analysis varies by jurisdiction...

\subsubsection{Financial Conversation Patterns}

\paragraph{Regulatory Boundaries.} Financial services are heavily regulated...

\paragraph{Numerical Precision.} Financial conversations require precision...
```

**Why it works**: Provides concrete value to target audience; demonstrates practical application.

**Typical expansion**: 3–6 pages per major concept.

#### Structured Case Studies

Full case studies with consistent structure:

```latex
\subsubsection{Case Study 1: Legal Research Assistant}

\textbf{Scenario}: A law firm wants to deploy an AI assistant...

\textbf{Analysis}:
\begin{itemize}
  \item \textbf{Stakes}: High. Incorrect citations could lead to malpractice.
  \item \textbf{Data needs}: Critical. Requires access to current case law.
  \item \textbf{Complexity}: High. Multi-step reasoning required.
  \item \textbf{Constraints}: Moderate latency; cost acceptable.
\end{itemize}

\textbf{Recommended Strategy}:
\begin{itemize}
  \item \textbf{ReAct with retrieval}: Essential for current legal data...
  \item \textbf{Chain-of-thought with IRAC}: Follow legal reasoning format...
\end{itemize}

\textbf{Memory Configuration}: Long conversations tracking matter details...
```

**Why it works**: Bridges theory to practice; demonstrates decision-making.

**Typical expansion**: 1.5–2.5 pages per case study; 4 case studies = 6–10 pages.

### Tier 2: Good Expansion (Recommended When Appropriate)

#### Common Misconceptions Section

Address errors that practitioners commonly make:

```latex
\subsection{Common Misconceptions}

\paragraph{Misconception: More reasoning steps always helps.}
Chain-of-thought improves performance on tasks requiring multi-step logic,
but not all tasks benefit. For simple factual questions, reasoning can
introduce "overthinking" that leads to incorrect conclusions. Always
evaluate whether reasoning helps for your specific task type.

\paragraph{Misconception: Longer context windows solve memory problems.}
While extended context windows enable longer conversations, they do not
solve the "lost in the middle" problem. Information in the middle of very
long contexts remains harder to access...
```

**Why it works**: Prevents errors; shows depth of understanding.

**Typical expansion**: 0.3–0.5 pages per misconception; 5 misconceptions = 1.5–2.5 pages.

#### Practitioner Exercises

Hands-on activities that reinforce learning:

```latex
\subsection{Exercises for Practitioners}

\paragraph{Exercise 1: Compare Reasoning Strategies.}
Select a multi-step problem from your domain. Solve it using:
\begin{enumerate}
  \item Direct prompting (zero-shot)
  \item Chain-of-thought prompting
  \item Self-consistency with 5 samples
\end{enumerate}
Compare quality, cost, and latency. Document which approach works best.

\paragraph{Exercise 2: Build a Few-Shot Library.}
Create a library of 10–20 high-quality examples for a frequent task...
```

**Why it works**: Actionable; reinforces concepts; valued by practitioners.

**Typical expansion**: 0.4–0.6 pages per exercise; 5 exercises = 2–3 pages.

#### Reading Sequences in Further Learning

Guide readers through the literature systematically:

```latex
\subsection{Recommended Reading Sequence}

\paragraph{Foundation Level (Week 1--2).}
Begin with foundational papers:
\begin{enumerate}
  \item \textcite{brown2020gpt3} to understand in-context learning
  \item \textcite{wei2022cot} to grasp step-by-step reasoning
  \item \textcite{liu2024lostmiddle} to understand context limitations
\end{enumerate}
This foundation explains why basic techniques work and where they fail.

\paragraph{Intermediate Level (Week 3--4).}
Progress to reliability and tool integration...
```

**Why it works**: Helps readers continue learning; shows scholarly depth.

**Typical expansion**: 1–2 pages.

### Tier 3: Moderate Expansion (Use Selectively)

#### Additional Figures

TikZ diagrams that visualize key concepts:

- Flowcharts for decision processes
- Architecture diagrams for systems
- Comparison matrices as visual tables
- Timeline diagrams for sequences

**Typical expansion**: 0.5–1 page per figure (including caption and discussion).

#### Extended Examples

Longer worked examples within existing sections:

```latex
\paragraph{Extended Example: Contract Review.}
Consider a vendor contract containing the following clause: [quoted text].
Applying the [technique], we would first [step 1]. This reveals [insight].
Next, [step 2]...
```

**Typical expansion**: 0.5–1 page per extended example.

### Tier 4: Low-Value Expansion (Avoid)

These add pages but reduce quality:

- **Redundant explanations**: Saying the same thing multiple ways
- **Excessive caveats**: Over-hedging every statement
- **Tangential history**: Historical details not relevant to practitioners
- **Verbose box content**: Padding boxes with unnecessary text
- **Gratuitous figures**: Diagrams that don't illuminate concepts

---

## Chapter Structure Patterns

### Pattern A: Comprehensive Technical Chapter (60–70 pages)

```
1. How to Read This Chapter (3-4 pages)
   - Reading paths for 3 audiences
   - Prerequisites
   - Key objectives
   - Visual cues explanation
   - Bridge from previous chapter

2. Introduction (4-6 pages)
   - Hook and motivation
   - Core definitions (1-2 definition boxes)
   - Chapter roadmap
   - Terminology

3. Core Technical Section 1 (10-15 pages)
   - Concept explanation
   - Subsections with depth
   - Figures and boxes
   - Domain applications (legal + financial)

4. Core Technical Section 2 (10-15 pages)
   - [Same structure]

5. Strategy/Decision Section (8-12 pages)
   - Decision framework
   - Trade-off analysis
   - Case studies (3-4)
   - Governance implications

6. Synthesis (4-6 pages)
   - Key takeaways (keybox)
   - What we haven't covered
   - Bridge to next chapters

7. Further Learning (6-8 pages)
   - Annotated bibliography by topic
   - Reading sequence
   - Common misconceptions
   - Exercises (4-6)

8. Conclusion (1-2 pages)

9. Bibliography (3-4 pages)
```

### Pattern B: Focused Technical Chapter (40–50 pages)

```
1. How to Read (2-3 pages)
2. Introduction (3-4 pages)
3. Core Section 1 (8-12 pages)
4. Core Section 2 (8-12 pages)
5. Applications/Case Studies (6-8 pages)
6. Synthesis (3-4 pages)
7. Further Learning (4-5 pages)
8. Conclusion (1 page)
9. Bibliography (2-3 pages)
```

### Pattern C: Applied/Governance Chapter (35–45 pages)

```
1. How to Read (2-3 pages)
2. Introduction (3-4 pages)
3. Framework Section (6-8 pages)
4. Case Studies (10-12 pages) — 4-6 detailed cases
5. Implementation Guidance (6-8 pages)
6. Governance Considerations (4-6 pages)
7. Further Learning (3-4 pages)
8. Conclusion (1 page)
9. Bibliography (2-3 pages)
```

---

## Case Study Templates

### Template 1: Strategy Selection Case Study

```latex
\subsubsection{Case Study: [Descriptive Title]}

\textbf{Scenario}: [1-2 sentences describing the situation]

\textbf{Analysis}:
\begin{itemize}
  \item \textbf{Stakes}: [Low/Moderate/High]. [Explanation of consequences]
  \item \textbf{Data needs}: [Low/Moderate/Critical]. [What external data is needed]
  \item \textbf{Complexity}: [Low/Moderate/High]. [Type of reasoning required]
  \item \textbf{Constraints}: [Latency, cost, volume considerations]
\end{itemize}

\textbf{Recommended Strategy}:
\begin{itemize}
  \item \textbf{[Strategy 1]}: [Why this is needed]
  \item \textbf{[Strategy 2]}: [Why this complements]
  \item \textbf{[Strategy 3]}: [Additional considerations]
\end{itemize}

\textbf{[Configuration Type]}: [Specific settings or parameters]
```

### Template 2: Problem-Solution Case Study

```latex
\subsubsection{Case Study: [Problem Description]}

\paragraph{The Challenge.}
[2-3 sentences describing the problem faced by the organization]

\paragraph{Initial Approach.}
[What they tried first and why it didn't work. 2-3 sentences]

\paragraph{Revised Solution.}
[How they applied the chapter's concepts. 3-4 sentences with specifics]

\paragraph{Results.}
[Outcomes achieved. Quantify if possible. 2-3 sentences]

\paragraph{Lessons Learned.}
\begin{itemize}
  \item [Key insight 1]
  \item [Key insight 2]
  \item [Key insight 3]
\end{itemize}
```

### Template 3: Comparison Case Study

```latex
\subsubsection{Case Study: [Comparison Title]}

\paragraph{Context.}
[Shared context for both approaches. 2-3 sentences]

\paragraph{Approach A: [Name].}
[Description of first approach. 3-4 sentences]

\textbf{Strengths}: [2-3 bullet points]
\textbf{Weaknesses}: [2-3 bullet points]

\paragraph{Approach B: [Name].}
[Description of second approach. 3-4 sentences]

\textbf{Strengths}: [2-3 bullet points]
\textbf{Weaknesses}: [2-3 bullet points]

\paragraph{When to Choose Each.}
[Guidance on selection criteria. 2-3 sentences]
```

---

## Expansion Strategies

### When You're Under Target

If your chapter is significantly under the page target:

1. **Audit domain coverage**: Are legal AND financial examples present in each major section?
2. **Add case studies**: 3-4 structured case studies can add 6-10 pages of high-value content
3. **Expand Further Learning**: Add reading sequences, misconceptions, exercises
4. **Deepen implementation sections**: Add professional domain patterns
5. **Create additional figures**: Visualize key concepts that are currently prose-only

### When You're Over Target

If your chapter exceeds the target significantly:

1. **Check for redundancy**: Are you explaining the same concept multiple ways?
2. **Evaluate tangents**: Is all historical context necessary for practitioners?
3. **Consider splitting**: Could this be two chapters?
4. **Move to appendix**: Technical details that interrupt flow
5. **Tighten prose**: Apply the prose-editing-checklist.md rigorously

### Maintaining Quality During Expansion

**DO:**
- Add content that provides new value (examples, case studies, exercises)
- Ensure new content serves the target audience
- Maintain consistent depth across sections
- Add figures that clarify, not decorate
- Include both legal and financial examples

**DON'T:**
- Pad with verbose restatements
- Add caveats and hedging to increase word count
- Include tangential historical details
- Create figures that don't illuminate concepts
- Repeat information across sections

---

## Quality vs. Quantity Balance

### The Golden Rule

**Every paragraph should teach something new or reinforce learning through example.**

### Quality Indicators

**High-quality expansion** looks like:
- Concrete examples from professional practice
- Structured case studies with clear takeaways
- Exercises that reinforce key skills
- Figures that visualize complex relationships
- Domain-specific implementation guidance

**Low-quality expansion** looks like:
- Verbose introductions that delay substance
- Repetitive explanations of the same concept
- Excessive hedging and caveats
- Decorative figures that don't illuminate
- Tangential historical detail

### The 3-Question Test

Before adding content, ask:

1. **Does this help a practitioner do their job better?**
2. **Would a reader miss this if it were removed?**
3. **Does this provide information not available elsewhere in the chapter?**

If the answer to any question is "no," reconsider adding the content.

---

## Planning Workflow

### Phase 1: Initial Structure (Before Writing)

1. Define chapter scope and objectives
2. Identify major sections (4-6 typically)
3. Estimate pages per section using tables above
4. Verify total estimate meets target range
5. Identify case studies and figures needed
6. Create bibliography skeleton with key sources

### Phase 2: First Draft

1. Write all sections to at least 70% of estimated length
2. Include placeholder case studies if needed
3. Create figure skeletons (basic TikZ structure)
4. Compile to check actual page count
5. Identify sections that need expansion

### Phase 3: Expansion and Refinement

1. Add domain-specific patterns where missing
2. Develop full case studies
3. Complete TikZ figures
4. Write Further Learning section
5. Add exercises and misconceptions
6. Compile and verify page count

### Phase 4: Quality Review

1. Apply prose-editing-checklist.md
2. Verify domain balance (legal + financial)
3. Check cross-references
4. Validate bibliography
5. Review figure clarity
6. Final compilation

---

## Checklists

### Pre-Writing Checklist

- [ ] Chapter objectives defined (5-7 specific outcomes)
- [ ] Major sections outlined (4-6 sections)
- [ ] Page estimates calculated for each section
- [ ] Total estimate within target range
- [ ] Case studies identified (3-4 minimum for comprehensive chapter)
- [ ] Key figures identified (3-5 for comprehensive chapter)
- [ ] Core bibliography identified (15-25 sources)
- [ ] Domain examples brainstormed (legal + financial for each major section)

### Expansion Checklist

When under page target, verify you have:

- [ ] How to Read section with reading paths
- [ ] Domain-specific implementation patterns (legal + financial)
- [ ] At least 3-4 structured case studies
- [ ] Common Misconceptions subsection (4-5 misconceptions)
- [ ] Practitioner Exercises subsection (4-6 exercises)
- [ ] Reading Sequence in Further Learning
- [ ] Annotated bibliography entries (not just citations)
- [ ] Figures for key concepts (3-5 minimum)

### Quality Verification Checklist

Before finalizing:

- [ ] Every major section has legal AND financial examples
- [ ] Case studies use consistent structure
- [ ] Prose flows naturally (no choppy fragments)
- [ ] Boxes used appropriately (not every 2nd paragraph)
- [ ] Figures illuminate rather than decorate
- [ ] Cross-references work (`make validate`)
- [ ] Bibliography entries are complete with urldate
- [ ] Exercises have clear steps and outcomes

---

## Related Documentation

- **[chapter-setup.md](chapter-setup.md)** — Directory structure, templates, build system
- **[style-guide.md](style-guide.md)** — Voice, tone, terminology, domain integration
- **[prose-editing-checklist.md](prose-editing-checklist.md)** — Sentence-level improvements
- **[color-guide.md](color-guide.md)** — Visual design system

---

## Changelog

| Date | Change | Reason |
|------|--------|--------|
| 2025-12-21 | Initial creation | Capture content planning patterns from Chapter 02 work |
