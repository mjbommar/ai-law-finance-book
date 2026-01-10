# Amazon KDP Publishing Guide

**Book:** Agentic AI in Law and Finance
**Subtitle:** Navigating a New Era of Autonomous Systems
**Authors:** Michael J. Bommarito II, Daniel M. Katz, Jillian Bommarito
**ISBN (Print):** 979-8-9943457-0-2 (paperback)
**ISBN (Ebook):** 979-8-9943457-1-9 (Kindle)
**Formats:** Paperback (print-on-demand), Kindle eBook (Fixed-Layout Print Replica)
**Last reviewed:** 2026-01-09

---

## Build Commands

```bash
# Build KDP Print files (interior + cover)
make kdp

# Build Kindle Print Replica PDF only
make kindle

# Individual targets
make kdp-interior      # Interior PDF (no covers)
make kdp-cover-vars    # Calculate cover dimensions
make kdp-cover         # Build wrap cover
make kdp-cover-check   # Verify dimensions
```

### Output Files

| File | Purpose | Upload To |
|------|---------|-----------|
| `kdp-interior.pdf` | Interior pages | KDP Print + Kindle |
| `kdp-cover.pdf` | Wrap cover | KDP Print only |

---

## Kindle Fixed-Layout (Print Replica)

**This book uses Print Replica format for Kindle.**

Print Replica preserves exact page layout, making it ideal for:
- Technical diagrams and figures
- Complex tables
- Mathematical notation
- Page-specific cross-references

### How to Upload

1. Go to KDP Kindle eBook section
2. Upload `kdp-interior.pdf` as the manuscript
3. When prompted, select "Print Replica" format
4. KDP automatically converts to fixed-layout Kindle

### Reader Experience

- Readers see exact PDF pages
- Zoom and pan on mobile devices
- Page numbers match print edition
- Best on tablets and larger screens

---

## KDP Print (Paperback) Setup

### Print Options

| Setting | Value |
|---------|-------|
| Trim size | 6" × 9" (US Trade) |
| Interior | Black & white |
| Paper | White |
| Bleed | No bleed |
| Cover finish | Matte |

### File Requirements

- **Interior:** `kdp-interior.pdf` (no covers, starts at half-title)
- **Cover:** `kdp-cover.pdf` (full wrap: back + spine + front + bleed)

### Cover Dimensions

Calculated automatically by `make kdp-cover-vars` based on page count.

For ~250 pages (white paper):
- Spine width: ~0.623" (pages × 0.002252 + 0.06)
- Total cover: ~12.87" × 9.25"

---

## Form Field Recommendations

### Language
**English**

### Book Title
- **Title:** Agentic AI in Law and Finance
- **Subtitle:** Navigating a New Era of Autonomous Systems

### Series
**Leave blank** (not part of a series)

### Edition Number
**1** (first edition)

### Authors

**Author 1:**
- First name: Michael J.
- Last name: Bommarito II

**Author 2:**
- First name: Daniel M.
- Last name: Katz

**Author 3:**
- First name: Jillian
- Last name: Bommarito

### Description (HTML for KDP)

```html
<b>What makes something agentic or an "AI agent"? How do you design one that actually works? And what does it take to deploy one safely in legal and financial applications?</b>

<br><br>

The term "agentic AI" means different things to different people, creating confusion in procurement, design, and regulation. This book provides a clear framework for building and governing agents in high-stakes domains where precision matters.

<br><br>

We move systematically from theory to practice:

<br><br>

<b>Define.</b> Before you can build, buy, or evaluate an "agent," you need a definition that holds up. Drawing on seven decades of scholarship, this book provides a framework that separates genuine agency from marketing claims—and gives you tools to test what a system can actually do.

<br><br>

<b>Design.</b> Clear definitions lead to sound architecture. The book translates agency into concrete design choices: how work reaches the system, how it perceives and acts, how it remembers and plans, when it escalates, and how it knows when to stop.

<br><br>

<b>Govern.</b> Good architecture makes oversight possible. In legal and financial settings, duties are non-delegable and supervision is not optional. The book shows how governance must change when systems can act with autonomy, and what controls make agentic systems deployable in regulated environments.

<br><br>

Written for legal practitioners, finance professionals, technology leaders, risk and compliance teams, and regulators who need clarity that will still matter as the technology evolves.
```

### Description (Plain Text for ISBN/Bowker)

```
What makes something agentic or an "AI agent"? How do you design one that actually works? And what does it take to deploy one safely in legal and financial applications?

The term "agentic AI" means different things to different people, creating confusion in procurement, design, and regulation. This book provides a clear framework for building and governing agents in high-stakes domains where precision matters.

We move systematically from theory to practice—defining what makes systems truly agentic, designing architectures that work reliably, and governing their deployment in regulated environments.

Define: Before you can build, buy, or evaluate an "agent," you need a definition that holds up. Drawing on seven decades of scholarship, this book provides a framework that separates genuine agency from marketing claims.

Design: Clear definitions lead to sound architecture. The book translates agency into concrete design choices: how work reaches the system, how it perceives and acts, how it remembers and plans, when it escalates, and how it knows when to stop.

Govern: Good architecture makes oversight possible. In legal and financial settings, duties are non-delegable and supervision is not optional. The book shows how governance must change when systems can act with autonomy.

Written for legal practitioners, finance professionals, technology leaders, risk and compliance teams, and regulators who need clarity that will still matter as the technology evolves.
```

### Publishing Rights
**Select:** "I own the copyright and I hold the necessary publishing rights."

### Primary Audience
**Select:** Standard adult content

### Sexually Explicit Content
**No**

### Primary Marketplace
**Amazon.com**

---

## Categories

Amazon allows up to 3 categories.

### Recommended Categories

1. **Computers & Technology > Computer Science > AI & Machine Learning > General**
   - Primary category, most directly relevant

2. **Law > Legal Services**
   - Captures legal practitioner audience

3. **Business & Money > Finance > Financial Risk Management**
   - Captures finance/compliance audience

### Alternative Categories

- Law > Ethics & Professional Responsibility
- Computers & Technology > Computer Science > AI & Machine Learning > Neural Networks
- Business & Money > Industries > Financial Services

---

## Keywords (7 slots, max 50 chars each)

1. `agentic AI legal compliance governance` (40 chars)
2. `AI agents financial services regulation` (40 chars)
3. `autonomous systems risk management` (35 chars)
4. `LLM agent architecture design patterns` (38 chars)
5. `AI governance framework enterprise` (35 chars)
6. `legal tech artificial intelligence` (35 chars)
7. `fintech AI regulatory compliance` (33 chars)

---

## BISAC Subject Codes

| Priority | Code | Description |
|----------|------|-------------|
| Primary | COM004000 | COMPUTERS / Artificial Intelligence / General |
| Primary | LAW050000 | LAW / Legal Services |
| Secondary | BUS027000 | BUSINESS & ECONOMICS / Finance / General |
| Secondary | COM051300 | COMPUTERS / Software Development & Engineering / General |

---

## Pricing Recommendations

### Comparable Titles

| Title | Paperback | Kindle |
|-------|-----------|--------|
| The Alignment Problem | $18 | $14-15 |
| AI Snake Oil | — | $18 |
| The Coming Wave | — | $14 |

### Recommended Pricing

| Format | Price | Notes |
|--------|-------|-------|
| Paperback | $24.99 | Professional/technical positioning |
| Kindle | $14.99 | Competitive with similar titles |

---

## Kindle Print Replica Notes

### Advantages
- Exact page fidelity
- All diagrams, tables, and figures preserved
- Page numbers match print
- No reflowing issues with technical content

### Limitations
- Less comfortable on phones (designed for tablets)
- No adjustable font size
- Larger file size than reflowable

### When to Use Print Replica
- Technical/academic content
- Complex diagrams or tables
- Mathematical notation
- Books with specific page layouts

This book is an ideal candidate for Print Replica due to its technical diagrams, tables, and precise formatting.

---

## Pre-Publication Checklist

- [ ] Build `kdp-interior.pdf` with `make kdp-interior`
- [ ] Build `kdp-cover.pdf` with `make kdp-cover`
- [ ] Verify cover dimensions with `make kdp-cover-check`
- [ ] Review interior for orphans/widows
- [ ] Check all cross-references resolve
- [ ] Verify ISBN barcode on back cover
- [ ] Test upload to KDP (draft mode)

---

## Post-Publication

1. **Author Central:** Set up author pages for all three authors
2. **A+ Content:** Apply for enhanced product page
3. **Categories:** Request additional categories via KDP Support if needed
4. **Keywords:** Review performance after 30-60 days

---

## References

- [KDP Cover Calculator](https://kdp.amazon.com/cover-calculator)
- [KDP Print Specifications](https://kdp.amazon.com/en_US/help/topic/G201834180)
- [Kindle Print Replica Guidelines](https://kdp.amazon.com/en_US/help/topic/G202059480)
- [BISAC Subject Codes](https://www.bisg.org/complete-bisac-subject-headings-list)
