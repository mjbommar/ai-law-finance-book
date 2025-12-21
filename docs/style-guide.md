# Writing Style Guide
## What Is an Agent? — Chapter Series

**Last Updated**: October 29, 2025
**Status**: Living document — update as we refine the writing

---

## 1. Purpose & Philosophy

This style guide ensures consistency across the "What Is an Agent?" chapter series. These chapters are being published incrementally as working drafts before integration into a single comprehensive work.

**Core Principles:**
- **Accessible yet rigorous**: Professional and educational without being stuffy or unnecessarily dense
- **Readable scholarship**: Academic depth with practitioner accessibility
- **Inviting rather than gatekeeping**: We want readers to understand, not to prove how smart we are

---

## 2. Tone & Voice

### 2.1 General Tone
✅ **DO**: Write with clarity, directness, and warmth
✅ **DO**: Use accessible language and concrete examples
✅ **DO**: Explain jargon when first introduced
✅ **DO**: Acknowledge complexity without apologizing for it

❌ **DON'T**: Use unnecessarily formal or archaic academic language
❌ **DON'T**: Be flip, sarcastic, or dismissive (even of marketing hype)
❌ **DON'T**: Over-apologize for length or complexity
❌ **DON'T**: Use stuffy constructions like "it is to be noted that" or "one might observe"

### 2.2 Person and Voice Patterns

**Use consistent person/voice within each section type:**

| Section Type | Voice | Example | Rationale |
|--------------|-------|---------|-----------|
| **Reader guidance** ("How to Read") | Direct address (you) | "Your time is valuable" | Personal, helpful tone |
| **Definitions & concepts** | Authorial plural (we) or neutral | "We define an agent as..." or "An agent is..." | Collaborative or objective |
| **Historical narrative** | Third person past | "Anscombe established..." | Scholarly distance |
| **Practical guidance** | Direct address (you) | "Use this rubric when..." | Actionable advice |
| **Analysis & synthesis** | Authorial plural (we) | "We now synthesize..." | Collaborative analysis |
| **Examples & applications** | Mix: third person for description, "you" for guidance | "A thermostat perceives... You can verify this by..." | Clear + actionable |

**Key decisions:**
- **Prefer "we"** for analysis and synthesis (inclusive, collaborative)
- **Use "you"** sparingly for direct guidance and reader navigation
- **Avoid "I"** entirely (this is collaborative scholarship, not a personal essay)
- **Avoid "one"** (sounds archaic and stuffy: "one might consider" → "consider" or "we consider")

### 2.3 Tense Consistency

| Context | Tense | Example |
|---------|-------|---------|
| Definitions | Present | "An agent is a system that..." |
| Historical events | Past | "Russell and Norvig defined..." |
| Current state/facts | Present | "The concept appears everywhere..." |
| Analysis of texts | Present | "Bratman argues...", "The paper proposes..." |
| Future directions | Future/conditional | "This will enable...", "Practitioners can leverage..." |
| Examples/scenarios | Present | "A thermostat maintains temperature..." |

---

## 3. Chapter vs. Book Framing

### 3.1 Current Status
This work is being developed as a **chapter series** with incremental publication before final integration into a single book.

**How to reference the work:**
- Within the document: "this chapter" (not "this paper" or "this book")
- In metadata/README: "chapter" or "working draft chapter"
- When referencing the eventual whole: "the book" or "the complete work"

### 3.2 Language for Work-in-Progress

✅ **GOOD examples:**
- "This chapter is being published as a working draft and will be revised"
- "Subsequent chapters will address..."
- "We acknowledge this chapter focuses narrowly on..."
- "The complete work will integrate..."

❌ **AVOID**:
- Apologetic language: "This is just a draft", "We haven't finished yet"
- Over-promises: "Future versions will completely solve..."
- Vague references: "other parts", "somewhere else in the book"

### 3.3 Section Referencing
Always provide clear, specific references:
- ✅ "Section~\ref{sec:history} traces..." with proper label
- ✅ "the historical analysis in Section~\ref{sec:history}"
- ❌ "as discussed elsewhere"
- ❌ "in another section"

---

## 4. Cross-Referencing & Hyperlinks

### 4.1 Internal Cross-References

**Use LaTeX's cross-referencing consistently:**

```latex
% Sections
\section{Introduction}
\label{sec:intro}

% Reference with:
Section~\ref{sec:intro}         % "Section 2"
\Cref{sec:intro}                % "Section 2" (auto-capitalized)
Sections~\ref{sec:intro}--\ref{sec:history}  % "Sections 2-3"
```

**Always include the non-breaking space `~` before `\ref{}`** to prevent line breaks between "Section" and the number.

### 4.2 Figures and Tables

```latex
% Define
\begin{figure}
  \label{fig:timeline}
  \caption{Timeline of agent definitions}
\end{figure}

% Reference
Figure~\ref{fig:timeline} illustrates...
\Cref{fig:timeline} shows...     % Preferred - auto-capitalizes
As shown in \cref{fig:timeline}  % lowercase variant for mid-sentence
```

### 4.3 When to Cross-Reference

**DO provide cross-references when:**
- Referring to content elsewhere in the chapter
- Pointing to related analysis or examples
- Guiding readers to prerequisite context
- Showing connections between sections

**Example:**
```latex
% GOOD
The three-level hierarchy (Section~\ref{sec:intro}) provides...
For historical context, see Section~\ref{sec:history}.

% BAD
The three-level hierarchy mentioned earlier...
For historical context, see above.
```

### 4.4 External References (Citations)

Use biblatex citation commands consistently:
- `\parencite{author2020}` → (Author, 2020) — for parenthetical citations
- `\textcite{author2020}` → Author (2020) — for narrative citations
- `\parencite[p.~42]{author2020}` → (Author, 2020, p. 42) — with page numbers

**Use non-breaking space for page numbers**: `p.~42` not `p. 42`

---

## 5. Terminology & Key Terms

### 5.1 Highlighting Key Terms

**First introduction of important terms:**
```latex
\keyterm{agent}              % Bold + colored (defined in main.tex)
\keyterm{agentic software}   % Use on first meaningful use
```

**Subsequent uses**: Regular text (not bold, not italic)

### 5.2 Capitalization
- **agent** (lowercase) — general concept
- **Agent** (capitalized) — when starting a sentence or in title
- **LLM** (all caps) — established acronym
- **AI** (all caps)
- **BDI** (all caps) — Beliefs-Desires-Intentions

### 5.3 Consistent Terminology

**Preferred terms** (use consistently):

| Concept | Preferred | Avoid |
|---------|-----------|-------|
| The three types | agent, agentic software, agentic AI | AI agent (ambiguous) |
| Main quality | goal-directed, goal-directedness | goal-oriented, goal-seeking |
| Iteration | perceive-decide-act loop | sense-think-act, perception-action |
| Evaluation tool | rubric, evaluation rubric | checklist, questionnaire |
| Professional domains | legal, medical, financial | law, medicine, finance (as modifiers) |
| AI capability | reasoning, planning | thinking, cognition (too strong) |

### 5.4 Latin & Foreign Terms
- Use sparingly and only when well-established
- Italicize on first use: \textit{prima facie}
- No italics for fully absorbed terms: etc., via, de facto

---

## 6. Sentence & Paragraph Style

### 6.1 Sentence Length
- **Target**: 15-25 words average
- **Range**: Mix short (5-10) for emphasis, medium (15-20) for flow, occasional long (25-30) for complex ideas
- **Break up**: Sentences over 30 words — usually can split or simplify

### 6.2 Paragraph Length
- **Target**: 3-5 sentences or 50-120 words
- **Single-sentence paragraphs**: Acceptable for emphasis, but use sparingly
- **Long paragraphs**: If over 150 words, consider splitting or adding subheadings

### 6.3 Active vs. Passive Voice

**Prefer active voice** when the agent is clear:
- ✅ "Russell and Norvig defined agents as..."
- ❌ "Agents were defined by Russell and Norvig as..."

**Passive voice is acceptable** when:
- Focus is on the action/result, not the actor: "The system was tested..."
- Actor is unknown or unimportant: "This term appears everywhere..."
- Parallel structure requires it: "Goals are specified, actions are selected, and results are observed"

### 6.4 Lists and Enumeration

**Use lists for clarity:**
- Bullet points for unordered items
- Numbered lists for sequences or priorities
- Description lists for term-definition pairs

**In LaTeX:**
```latex
\begin{itemize}
  \item First point
  \item Second point
\end{itemize}

\begin{description}
  \item[Term] Definition here
\end{description}
```

---

## 7. Common Pitfalls & Corrections

### 7.1 Double Negatives
❌ **WRONG**:
```latex
You won't find any of the following:
\begin{itemize}
  \item No marketing claims
  \item No product reviews
\end{itemize}
```

✅ **RIGHT** (Option A — Remove "No"):
```latex
You won't find:
\begin{itemize}
  \item Marketing claims about products
  \item Product reviews or comparisons
\end{itemize}
```

✅ **RIGHT** (Option B — Change intro):
```latex
This chapter includes:
\begin{itemize}
  \item No marketing claims about products
  \item No product reviews or comparisons
\end{itemize}
```

### 7.2 Unclear Referents
❌ "Readers interested in these topics will find more of this elsewhere"
→ What does "this" mean? Marketing? Tutorials? Content?

✅ "Readers interested in implementation guides will find numerous tutorials elsewhere"

### 7.3 Apologetic Framing
❌ "This chapter is not short" → Sounds apologetic
❌ "We haven't covered everything" → Defensive

✅ "This chapter provides comprehensive coverage"
✅ "We focus specifically on..."

### 7.4 Vague Intensifiers
Avoid weak intensifiers that don't add meaning:
- ❌ very important → ✅ critical, essential
- ❌ really useful → ✅ useful (or specify how)
- ❌ quite complex → ✅ complex (or specify the complexity)

### 7.5 Hedging Language
Be direct unless genuine uncertainty exists:
- ❌ "It seems that agents might be..." → ✅ "Agents are..."
- ❌ "One could argue that..." → ✅ "This definition argues..." or "We argue..."
- ⚠️ "arguably", "perhaps", "possibly" → Use only for genuine epistemic caution

---

## 8. Visual Elements & Formatting

### 8.1 Boxes and Callouts

**Three box types** (defined in main.tex):

| Box Type | Purpose | Color Scheme | Example Use |
|----------|---------|--------------|-------------|
| `definitionbox` | Formal definitions | Ice blue + slate border | Core definition of "agent" |
| `highlightbox` | Context, notes, asides | Cream + neutral border | Etymology notes, historical context |
| `keybox` | Critical takeaways | Amber + accent border | Stop-here summaries, essential questions |

**Usage:**
```latex
\begin{definitionbox}[title={\textbf{Definition: Agent}}]
An agent is a system that...
\end{definitionbox}

\begin{highlightbox}
\paragraph{Historical Note.} Context here...
\end{highlightbox}

\begin{keybox}[title={\textbf{Essential Questions}}]
Critical content here...
\end{keybox}
```

**Box content rules:**
- Keep box content focused (one concept or set of related points)
- Don't nest boxes (use sections instead)
- Ensure boxes can break across pages if needed (already configured with `breakable`)

### 8.2 Emphasis
- **Bold** (`\textbf{}`) for strong emphasis, key terms first use
- *Italic* (`\textit{}`) for book titles, foreign terms, light emphasis
- `\keyterm{}` for first introduction of domain-specific terms (bold + color)

### 8.3 Tables
- Use `booktabs` style: `\toprule`, `\midrule`, `\bottomrule`
- Add `\addlinespace` between logical groups of rows
- Keep tables readable — if over 10 columns, reconsider layout
- Always include `\caption{}` and `\label{}`

### 8.4 Quotations
- Inline quotes: Use LaTeX-friendly double backticks and apostrophes: `` ``quoted text'' ``
- Block quotes: Use `quote` or `quotation` environment for 3+ lines
- Always cite source after quotation

---

## 9. Grammar & Mechanics

### 9.1 Punctuation
- **Serial comma**: YES — "A, B, and C" (not "A, B and C")
- **Em-dash**: Use `---` (no spaces) for parenthetical breaks
- **En-dash**: Use `--` for ranges: "1957--2025", "pages 10--15"
- **Hyphenation**:
  - goal-directed (hyphenated adjective)
  - decision tree (no hyphen)
  - agent-oriented programming (hyphenated)
  - multi-agent system (hyphenated)

### 9.2 Numbers
- **Spell out**: Numbers under 10 when not technical: "three levels", "six questions"
- **Use numerals**: 10 and above, all technical contexts: "45 pages", "10-question rubric"
- **Consistency in lists**: If one item needs numerals, use numerals for all

### 9.3 Abbreviations
- **First use**: Spell out with abbreviation in parentheses: "large language models (LLMs)"
- **Subsequent**: Use abbreviation only: "LLMs enable..."
- **Well-known**: No need to spell out: AI, PDF, API (reader context dependent)

---

## 10. Section-Specific Guidelines

### 10.1 "How to Read This Chapter"
**Purpose**: Help readers navigate efficiently
**Voice**: Direct address (you)
**Structure**:
- Lead with the core question/value
- Provide clear reading paths with specific section references
- Scope clearly (what IS included) before disclaimers (what's NOT)
- End with a natural transition to Section 1

**Avoid**:
- Over-apologizing for length
- Excessive disclaimers
- Dismissive tone toward related work

### 10.2 Introduction
**Purpose**: Establish definitions, motivation, structure
**Voice**: Authorial plural (we) for analysis, neutral for definitions
**Structure**:
- Hook with the core question
- Provide accessible entry point ("doer with a to-do")
- Build to formal definition
- Explain stakes (why definitions matter)
- Preview structure

### 10.3 Historical Sections
**Purpose**: Trace chronological evolution
**Voice**: Third person past tense
**Structure**:
- Organize by decade/era with clear transitions
- Use `\paragraph{Year: Title}` for individual milestones
- Connect to contemporary relevance where appropriate

### 10.4 Practical/Applied Sections
**Purpose**: Provide actionable guidance
**Voice**: Direct address (you) and imperative
**Structure**:
- Lead with clear use case
- Provide decision tools (rubrics, trees, tables)
- Include concrete examples
- End with guidance on when/how to apply

---

## 11. Citation & Attribution

### 11.1 When to Cite
**Always cite** when:
- Quoting directly
- Paraphrasing specific claims
- Referencing empirical findings
- Using discipline-specific definitions
- Claiming historical facts about scholarship

**No citation needed** for:
- General knowledge in the field
- Your own analysis/synthesis
- Widely-known facts (LLMs use transformers)

### 11.2 Citation Style
Using biblatex with authoryear style:
- In-text: `\parencite{russell2020}` or `\textcite{russell2020}`
- Multiple: `\parencite{author2020, other2021}`
- Page numbers: `\parencite[p.~42]{author2020}`

---

## 12. Revision Checklist

Before considering a section complete, verify:

**Consistency**:
- [ ] Person/voice matches section type (see Section 2.2)
- [ ] Tense is appropriate for content type (see Section 2.3)
- [ ] Key terms are introduced with `\keyterm{}` on first use
- [ ] Cross-references use `\ref{}` with proper labels

**Clarity**:
- [ ] No sentences over 35 words without good reason
- [ ] No paragraphs over 150 words without subheadings
- [ ] Technical terms defined on first use
- [ ] Examples illustrate abstract concepts

**Correctness**:
- [ ] All citations in `bib/refs.bib`
- [ ] All `\label{}` references exist and are correct
- [ ] No double negatives (see Section 7.1)
- [ ] No unclear referents ("this", "that", "it" without clear antecedent)

**Accessibility**:
- [ ] Tone is professional but approachable
- [ ] Jargon is explained or avoided
- [ ] Structure guides readers (headings, lists, boxes)
- [ ] Cross-references help readers navigate

**Polish**:
- [ ] No apologetic framing
- [ ] No dismissive tone
- [ ] Active voice where appropriate
- [ ] Parallel structure in lists

---

## 13. Tools & Resources

### 13.1 LaTeX Commands Reference
See `main.tex` lines 269-278 for custom commands:
- `\keyterm{term}` — Bold + colored for first use
- `\Cref{label}` — Auto-capitalized cross-reference
- `\parencite{key}` — Parenthetical citation

### 13.2 Build & Validation
```bash
# Full build
make pdf

# Quick single-pass (for testing)
make quick

# Validate references
make validate

# Word count
make wordcount
```

### 13.3 This Style Guide
- **Location**: `paper/versions/v3/STYLE.md`
- **Status**: Living document — update as patterns emerge
- **Referenced from**: README.md (see Section 14 below)

---

## 14. Domain Integration: Legal and Financial Examples

This textbook targets legal and financial professionals. Every major concept should be grounded in domain-specific examples that resonate with this audience.

### 14.1 The Domain Integration Requirement

**Rule:** Each major section should include examples from BOTH legal and financial contexts.

**Why this matters:**
- Readers from legal backgrounds may not immediately see financial applications (and vice versa)
- Domain-specific examples validate that concepts work in real professional contexts
- Examples from both domains demonstrate the generalizability of techniques
- Practitioners prefer examples from their own field

### 14.2 Legal Domain Examples

When illustrating concepts, draw from these legal practice areas:

| Practice Area | Example Topics |
|---------------|----------------|
| **Litigation** | Case law research, document review, deadline management, motion drafting |
| **Contracts** | Clause extraction, risk identification, playbook comparison, negotiation |
| **Compliance** | Regulatory monitoring, policy updates, audit preparation, disclosure |
| **Research** | Statutory analysis, precedent search, jurisdiction comparison |
| **Due Diligence** | Document analysis, red flag identification, closing checklists |

**Legal-specific considerations to address:**
- Attorney-client privilege protection
- Jurisdictional variation
- Temporal sensitivity (law changes over time)
- Citation verification (cases, statutes, regulations)
- Ethical obligations (competence, confidentiality, candor)

**Example structure for legal illustrations:**
```latex
\paragraph{Legal Application.} In litigation support, [concept] manifests as
[specific application]. A legal research assistant using [technique] must
[specific requirement] because [legal rationale]. For instance, when
researching [topic], the system should [concrete behavior].
```

### 14.3 Financial Domain Examples

When illustrating concepts, draw from these financial practice areas:

| Practice Area | Example Topics |
|---------------|----------------|
| **Portfolio Management** | Position analysis, risk assessment, rebalancing, reporting |
| **Trading** | Order execution, market data analysis, compliance checks |
| **Risk Management** | Scenario analysis, stress testing, limit monitoring |
| **Compliance** | Regulatory reporting, surveillance, disclosure review |
| **Research** | Fundamental analysis, earnings reviews, sector analysis |
| **Client Service** | Suitability assessment, recommendations, portfolio reviews |

**Financial-specific considerations to address:**
- Regulatory boundaries (advice vs. information)
- Numerical precision (calculations, currency, percentages)
- Real-time data requirements
- Audit trail requirements
- Client risk profiles and suitability

**Example structure for financial illustrations:**
```latex
\paragraph{Financial Application.} In portfolio management, [concept] appears
when [specific scenario]. An analyst using [technique] must consider
[specific requirement] because [regulatory/practical rationale]. For example,
when analyzing [topic], the system should [concrete behavior] to ensure
[outcome].
```

### 14.4 Balancing Domain Examples

**Pattern A: Parallel treatment**
Discuss concept generally, then provide equal-weight examples from both domains:
```latex
[General explanation of concept]

\paragraph{Legal Application.} [Legal example with 3-4 sentences]

\paragraph{Financial Application.} [Financial example with 3-4 sentences]
```

**Pattern B: Integrated discussion**
Weave examples throughout the explanation:
```latex
[Concept introduction] For instance, a litigation support system might
[legal example], while a portfolio analyzer would [financial example].
The key difference lies in [distinguishing factor].
```

**Pattern C: Case study pairs**
For major concepts, provide detailed case studies from both domains:
```latex
\subsubsection{Case Study: Legal Document Review}
[Detailed scenario, analysis, and recommendations]

\subsubsection{Case Study: Financial Report Analysis}
[Parallel structure with financial context]
```

### 14.5 Domain-Specific Terminology

Maintain consistency in domain terminology:

| Legal Term | Financial Term | Neutral Alternative |
|------------|----------------|---------------------|
| case, matter | trade, position | task, item |
| counsel, attorney | analyst, advisor | professional, user |
| filing, pleading | report, disclosure | document |
| court, tribunal | exchange, regulator | authority |
| privilege | confidentiality | access control |
| jurisdiction | market, sector | scope, domain |

### 14.6 Domain Integration Checklist

Before finalizing any section, verify:

- [ ] **Legal example present**: At least one concrete legal application
- [ ] **Financial example present**: At least one concrete financial application
- [ ] **Examples are substantive**: Not just name-drops but actual illustrations
- [ ] **Domain-specific concerns addressed**: Privilege, regulation, precision, etc.
- [ ] **Terminology appropriate**: Uses domain terms correctly
- [ ] **Balance achieved**: Neither domain dominates unfairly
- [ ] **Governance implications noted**: Compliance, audit, risk considerations

### 14.7 When Examples Aren't Parallel

Sometimes a concept applies more naturally to one domain. In these cases:

1. **Acknowledge the asymmetry** explicitly
2. **Provide the stronger example** in full detail
3. **Offer a lighter touch** for the other domain
4. **Explain why** the difference exists

```latex
\paragraph{Legal Application.} Contract review provides a natural application
of [concept] because [detailed reason]. [Full example]

\paragraph{Financial Parallel.} While less central to financial workflows,
[concept] appears in [lighter example], particularly when [specific context].
```

---

## 15. Integration with Project Documentation

This style guide should be referenced in:
1. **README.md** — Add link in "How to Contribute" or "Writing Guidelines" section
2. **CLAUDE.md** or **AGENTS.md** (if created) — Reference for AI-assisted writing
3. **Git commit messages** when making style-related changes

**Suggested README.md addition:**
```markdown
## Writing & Style

This chapter follows the guidelines in [STYLE.md](STYLE.md), which covers:
- Tone and voice (accessible but rigorous)
- Person and tense consistency
- Cross-referencing and hyperlinks
- Terminology and formatting
- Section-specific guidance

Please review the style guide before making substantial edits.
```

---

## Changelog

| Date | Change | Reason |
|------|--------|--------|
| 2025-10-29 | Initial creation | Establish consistency across chapter series |
| 2025-12-21 | Added Section 14: Domain Integration | Ensure legal/financial examples throughout |

---

**Questions or suggestions?** Update this guide as patterns emerge and edge cases arise. This is a living document.
