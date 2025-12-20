# Prose Editing Checklist for Academic Textbooks

This checklist captures the editing patterns used to transform technical writing into clear, engaging academic prose while maintaining professional rigor.

---

## 1. Sentence-Level Flow

### 1.1 Eliminate Em Dash Overuse

**Problem:** Em dashes (---) used as a crutch every other sentence.

**Before:**
```
Voice interfaces work best for short, urgent requests where typing is impractical---a portfolio manager checking a position while walking between meetings.
```

**After:**
```
Voice interfaces work best for short, urgent requests where typing is impractical. Think of a portfolio manager checking a position while walking between meetings.
```

**Techniques:**
- Split into separate sentences
- Use "Think of" or "Consider" to introduce examples
- Use "such as" or "like" for inline examples
- Use "which" clauses for elaboration

### 1.2 Fix Fragment Sentences

**Problem:** Choppy fragments that read like bullet points.

**Before:**
```
Answer the complaint within 21 days. File motions 30 days before hearings. Respond to discovery within 30 days.
```

**After:**
```
You must answer the complaint within 21 days, file motions 30 days before hearings, and respond to discovery within 30 days.
```

**Techniques:**
- Combine related fragments with commas and "and"
- Add a subject ("You must...") to create a complete sentence
- Use parallel structure within a single sentence

### 1.3 Replace Semicolon Lists with Natural Flow

**Problem:** Semicolons creating choppy, list-like prose.

**Before:**
```
The user types or speaks; the system responds; the user refines.
```

**After:**
```
The user types or speaks, the system responds, and the user refines based on what they see.
```

**Techniques:**
- Replace semicolons with commas and conjunctions
- Add context to the final item ("based on what they see")

### 1.4 Convert Colon-Based Lists to Flowing Paragraphs

**Problem:** Bold term followed by colon, creating choppy reading.

**Before:**
```
**Coverage**: Does the system receive events from all relevant sources?

**Latency**: How quickly do events reach the system?

**Reliability**: What happens when feeds fail?
```

**After:**
```
**Coverage** asks whether the system receives events from all relevant sources. A litigation system that monitors CM/ECF but not state court dockets has incomplete coverage that could miss critical filings. **Latency** measures how quickly events reach the system. Real-time market data requires sub-second delivery, while docket alerts can tolerate delays of several minutes. **Reliability** addresses what happens when feeds fail.
```

**Techniques:**
- Keep the bold term but remove the colon
- Add a verb after the bold term ("asks whether", "measures", "addresses")
- Follow with explanation and concrete example
- Flow multiple items into a single paragraph

### 1.5 Vary Repetitive Sentence Structure

**Problem:** Parallel structure becoming monotonous.

**Before:**
```
Each question maps to a capability. Each capability maps to design decisions. And each design decision shapes what the system can do.
```

**After:**
```
Each question maps to a capability every useful agent needs, each capability involves design choices with real consequences, and those choices determine not just what the system can do but how reliably it performs.
```

**Techniques:**
- Combine into one flowing sentence
- Vary the verb structure
- Add additional context to later items

---

## 2. Natural Conjunctions and Transitions

### 2.1 Preferred Conjunctions (Instead of Em Dashes)

| Instead of | Use |
|------------|-----|
| `---allowing` | ", allowing" or ". This allows" |
| `---which` | ", which" or ". This" |
| `---the` | ". The" or ", where the" |
| `---whether` | ", whether" or "such as whether" |

### 2.2 Transitional Phrases for Examples

- "Think of..." (for vivid examples)
- "Consider..." (for scenarios)
- "such as..." (for inline lists)
- "like..." (for comparisons)
- "Examples include..." (for longer lists)

### 2.3 Transitional Phrases for Contrast

- "In contrast,..." (for opposing ideas)
- "However,..." (for caveats)
- "But..." (for direct contradiction - use sparingly)
- "While X does Y, Z does W." (for parallel contrast)

### 2.4 Transitional Phrases for Causation

- "because..." (direct cause)
- "since..." (assumed cause)
- "allowing..." (enabling cause)
- "which in turn..." (chain causation)
- "This is why..." (explaining significance)

### 2.5 Transitional Phrases for Connection

- "The main challenge here is..." (introducing problems)
- "What makes X powerful is..." (introducing benefits)
- "This matters because..." (explaining significance)

---

## 3. Box and Visual Element Design

### 3.1 When to Use Boxes

**USE boxes for:**
- Key definitions (definitionbox) - one per major concept
- Critical warnings or cautions (cautionbox)
- Actionable decision frameworks (keybox)
- Important takeaways readers should remember

**DON'T use boxes for:**
- Every sub-concept or dimension of a topic
- Lists that could be paragraphs
- Content that flows naturally as prose
- Anything that would create 3+ boxes in sequence

### 3.2 Box Type Selection

| Box Type | Use For | Visual Style |
|----------|---------|--------------|
| `definitionbox` | Formal definitions, key terms | Blue, scholarly |
| `keybox` | Actionable guidance, decision frameworks | Amber, prominent |
| `highlightbox` | Supplementary context, notes | Neutral, subtle |
| `cautionbox` | Warnings, pitfalls, mistakes | Red, attention-grabbing |

### 3.3 Box Internal Structure

**Add vertical spacing:**
```latex
\vspace{0.5em}  % After intro text, before first item
\vspace{0.3em}  % Between items
\vspace{0.5em}  % Before closing statement
```

**Use descriptive sentences, not questions:**

**Before:**
```
**Synchronicity**: Does the user wait for results (synchronous) or receive them later (asynchronous)?
```

**After:**
```
**Synchronicity** describes whether the user waits for results in real time or receives them later through notifications or reports.
```

### 3.4 Preventing Box Page Breaks

```latex
\begin{keybox}[breakable=false, title={Title}]
```

### 3.5 Converting Boxes to Paragraphs

When you have multiple related boxes, convert to:

1. One definition box introducing the concept
2. Multiple paragraphs, each starting with **Bold term**
3. Each paragraph flows naturally with examples

---

## 4. Table Design

### 4.1 Hyperlinked Section References

```latex
\Cref{sec:section-label}  % Creates clickable "Section X"
```

### 4.2 Column Width Adjustment

Start with proportions that match content length:
```latex
\begin{tabular}{p{0.15\textwidth}p{0.24\textwidth}p{0.49\textwidth}}
```

Adjust iteratively based on how content wraps.

### 4.3 Table Placement

```latex
\begin{table}[H]  % Force exact placement (requires float package)
\begin{table}[!ht]  % Try hard to place here or top
```

---

## 5. Section Structure

### 5.1 Add Narrative Between Definitions

After a definition box, add a paragraph that:
- Explains why the distinction matters
- Connects to practical concerns (governance, audit, design)
- Previews what comes next

### 5.2 Add Forward References

Connect current content to later sections:
```latex
This is why intent understanding (\Cref{sec:intent}) matters even more for asynchronous workflows.
```

### 5.3 Add Contrast Paragraphs

After discussing one approach, add:
```
In contrast, [alternative approach] does not require [X], but introduces [Y] challenges...
```

---

## 6. Voice and Tone

### 6.1 Pronoun Usage

- **"you"** for direct guidance and reader navigation
- **"we"** for analysis and collaborative synthesis
- **Never "I"** (this is collaborative scholarship)
- **Avoid "one"** (archaic and stuffy)

### 6.2 Conversational but Professional

**Before (stiff):**
```
Properties do not deploy. To evaluate a vendor's claims, one needs to understand...
```

**After (conversational):**
```
But recognizing a system is not the same as deploying it, governing it, or knowing when a vendor is overselling it. For that, you need to understand...
```

### 6.3 Concrete Examples

Always include domain-specific examples from:
- Legal practice (litigation, compliance, contracts)
- Financial services (portfolio management, trading, risk)

---

## 7. Pre-Edit Checklist

Before editing a section, check for:

- [ ] Em dashes used more than once per paragraph
- [ ] Fragment sentences (periods where commas would work)
- [ ] Semicolon chains (;...;...;)
- [ ] Bold-colon format (**Term**: description)
- [ ] Repetitive sentence structure (Each X. Each Y. Each Z.)
- [ ] Multiple boxes in sequence (3+)
- [ ] Boxes with question-format content
- [ ] Missing transitions between concepts
- [ ] Missing forward/backward references
- [ ] Missing concrete examples
- [ ] Tables without hyperlinks
- [ ] Tables floating away from discussing text

---

## 8. Post-Edit Checklist

After editing a section, verify:

- [ ] Paragraphs flow naturally when read aloud
- [ ] Bold terms appear at paragraph starts (not mid-sentence with colons)
- [ ] Examples are woven into prose (not separate fragments)
- [ ] Boxes are used sparingly (1-2 per subsection max)
- [ ] Transitions connect ideas ("In contrast", "This is why", "Think of")
- [ ] Forward references link to later sections where relevant
- [ ] No em dash appears more than once per paragraph
- [ ] PDF compiles without errors
- [ ] Tables appear near their discussing text
