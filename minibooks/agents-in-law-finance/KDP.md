# Amazon KDP Publishing Guide

**Book:** Agentic AI in Law and Finance
**Subtitle:** Navigating a New Era of Autonomous Systems
**Authors:** Michael J. Bommarito II, Daniel M. Katz, Jillian Bommarito
**ISBN (Print):** 979-8-9943457-0-2 (paperback)
**ISBN (Ebook):** 979-8-9943457-1-9 (Kindle)
**Formats:** Paperback (print-on-demand), Kindle eBook (Fixed-Layout Print Replica)
**Last reviewed:** 2026-01-16

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

### Author Bios (for Author Central and Editorial Reviews)

**Michael J. Bommarito II:**
```
Michael J. Bommarito II is CEO of 273 Ventures and Adjunct Professor at Michigan State University College of Law. His research on AI and law has been published in Science, Cambridge University Press, and other leading venues, with work cited over 3,000 times. He co-founded legal AI company LexPredict (acquired 2018) and led the research demonstrating GPT-4's ability to pass the Uniform Bar Examination. He holds degrees from the University of Michigan in mathematics, political science, and financial engineering.
```

**Daniel M. Katz:**
```
Daniel M. Katz is Professor of Law at Illinois Tech Chicago-Kent College of Law and co-founder of 273 Ventures. Named by the Financial Times as one of the top 20 legal market shapers of the past two decades, he teaches courses on artificial intelligence, legal analytics, and legal technology. He holds a Ph.D. in political science and public policy from the University of Michigan and a J.D. cum laude from Michigan Law.
```

**Jillian Bommarito:**
```
Jillian Bommarito is Chief Risk Officer of 273 Ventures and one of the first certified AI auditors in the world. A risk and governance specialist, she holds CIPP/US and CIPP/E certifications and brings expertise in compliance, privacy, and AI governance. She co-founded LexPredict and oversaw the training of the world's first openly-licensed large language model.
```

---

### Description (HTML for KDP)

**SEO-optimized for discoverability. Front-loads keywords and author credentials.**

```html
<b>The practical guide to AI agent deployment in regulated industries—from the researchers who proved GPT-4 could pass the bar exam.</b>

<br><br>

If you're evaluating AI agents for legal work, financial services, or compliance, you need more than vendor demos. You need a framework for understanding what these systems can actually do—and what it takes to deploy them responsibly.

<br><br>

<b>AGENTIC AI IN LAW AND FINANCE</b> delivers exactly that. Drawing on seven decades of AI research, the authors—who co-founded LexPredict, demonstrated GPT-4's bar exam capabilities, and were named among the top 20 legal market shapers by the Financial Times—provide a rigorous yet accessible framework for professionals in regulated industries.

<br><br>

<b>What you'll learn:</b>
<ul>
<li>How to evaluate AI agent claims and separate genuine capability from marketing hype</li>
<li>Design patterns for building reliable agents: triggers, perception, action, memory, planning, and termination</li>
<li>Governance frameworks that satisfy non-delegable duties in legal and financial settings</li>
<li>Escalation and oversight controls for autonomous systems in production</li>
<li>Risk assessment criteria for agentic AI procurement decisions</li>
</ul>

<br><br>

<b>Who this book is for:</b> General counsel and legal operations teams evaluating AI tools. Compliance officers developing AI governance policies. Technology leaders making build-vs-buy decisions. Risk managers assessing autonomous systems. Regulators seeking to understand agentic AI.

<br><br>

<em>"A clear, practical framework for the legal and compliance professionals who actually have to make AI deployment decisions."</em>
```

**Character count:** ~1,800 (under 4,000 limit)

### Description (Plain Text for ISBN/Bowker)

**Use for Bowker MyIdentifiers, library cataloging, and metadata services.**

```
The practical guide to AI agent deployment in regulated industries—from the researchers who proved GPT-4 could pass the bar exam.

If you're evaluating AI agents for legal work, financial services, or compliance, you need more than vendor demos. You need a framework for understanding what these systems can actually do—and what it takes to deploy them responsibly.

Drawing on seven decades of AI research, the authors—who co-founded LexPredict, demonstrated GPT-4's bar exam capabilities, and were named among the top 20 legal market shapers by the Financial Times—provide a rigorous yet accessible framework for professionals in regulated industries.

The book covers: How to evaluate AI agent claims and separate genuine capability from marketing hype. Design patterns for building reliable agents: triggers, perception, action, memory, planning, and termination. Governance frameworks that satisfy non-delegable duties in legal and financial settings. Escalation and oversight controls for autonomous systems in production. Risk assessment criteria for agentic AI procurement decisions.

Written for general counsel, legal operations teams, compliance officers, technology leaders, risk managers, and regulators who need clarity on AI agent deployment that will remain relevant as technology evolves.
```

### Short Description (~350 characters)

**Use for limited metadata fields, social media, and promotional materials.**

```
The practical guide to AI agent deployment for legal and financial professionals. From the researchers who proved GPT-4 could pass the bar exam—a framework for evaluating, designing, and governing AI agents in regulated industries where precision and compliance matter.
```

### One-Liner (~100 characters)

```
The definitive guide to AI agent governance for law and finance professionals.
```

### Taglines for Marketing

```
"From bar exam breakthrough to deployment blueprint."

"AI agent governance for professionals who can't afford to get it wrong."

"Define. Design. Govern. The framework for AI agents in regulated industries."
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

**Strategy:** Target high-intent search phrases from legal/finance professionals evaluating AI. Avoid terms already in title/categories (agentic, AI, law, finance, autonomous).

**Recommended Keywords:**

1. `GPT agents for lawyers compliance guide` (39 chars)
   - *Leverages bar exam research credibility*

2. `LLM deployment regulated industries book` (40 chars)
   - *Captures enterprise/compliance buyers*

3. `AI governance framework risk management` (38 chars)
   - *Compliance officers, risk managers*

4. `legal technology procurement evaluation` (39 chars)
   - *Decision-makers evaluating vendors*

5. `financial services AI oversight controls` (40 chars)
   - *Finance compliance, FINRA/SEC context*

6. `enterprise AI agent design architecture` (38 chars)
   - *Technical decision-makers*

7. `non-delegable duties AI supervision` (35 chars)
   - *Legal-specific governance concept*

**Alternative Keywords (rotate after 60 days if underperforming):**

- `ChatGPT Claude enterprise deployment guide` (41 chars)
- `responsible AI legal financial services` (39 chars)
- `AI vendor evaluation framework legal` (36 chars)
- `machine learning governance compliance` (38 chars)

---

## BISAC Subject Codes

| Priority | Code | Description |
|----------|------|-------------|
| Primary | COM004000 | COMPUTERS / Artificial Intelligence / General |
| Primary | LAW050000 | LAW / Legal Services |
| Secondary | BUS027000 | BUSINESS & ECONOMICS / Finance / General |
| Secondary | COM051300 | COMPUTERS / Software Development & Engineering / General |

---

## Market Research: Comparable Titles

This book occupies a **specialized niche**: practical AI agent guidance for legal/financial professionals with governance emphasis. Most AI books are either too technical (ML engineers) or too general (pop-science). Few address regulatory context.

### Tier 1: Direct Competitors (AI for Legal/Finance Professionals)

| Title | Author | Positioning | Gap This Book Fills |
|-------|--------|-------------|---------------------|
| The Alignment Problem | Brian Christian | Ethics focus, academic | No practical deployment guidance |
| AI Snake Oil | Narayanan & Kapoor | Skeptical, hype-debunking | No design/governance frameworks |
| The Coming Wave | Suleyman | Policy/existential risk | No professional implementation |
| Legal Informatics | Katz, Bommarito et al. | Academic, Cambridge UP | Broader scope, less agent-focused |

### Tier 2: Adjacent Professional Books

| Category | Price Range | Our Positioning |
|----------|-------------|-----------------|
| Legal tech guides | $35-55 | Professional pricing justified |
| Finance compliance books | $40-70 | Risk/governance audience |
| Enterprise AI guides | $30-50 | Technical decision-makers |

### Author Credentials Advantage

| Competitor Books | Typical Authors | This Book's Authors |
|------------------|-----------------|---------------------|
| Most AI books | Tech-only background | Law + Finance + Tech |
| Most legal tech | Academic-only | Entrepreneur + Academic |
| Most governance guides | Consultant | Built & sold AI company + First AI auditor |

---

## Pricing Recommendations

### Comparable Professional Titles (2026)

| Title | Paperback | Kindle | Positioning |
|-------|-----------|--------|-------------|
| The Alignment Problem | $18 | $14-15 | Mass market |
| AI Snake Oil | — | $18 | Trade non-fiction |
| Enterprise AI guides | $35-45 | $25-35 | Professional |
| Legal tech books | $40-60 | $30-45 | Specialized professional |
| Compliance/risk books | $45-70 | $35-50 | Institutional buyers |

### Recommended Pricing

| Format | Price | Rationale |
|--------|-------|-----------|
| Paperback | **$29.99** | Professional positioning, institutional purchasing |
| Kindle | **$19.99** | Competitive with enterprise guides |
| Hardcover (if offered) | **$44.99** | Library/institutional market |

**Pricing Strategy:**
- Higher than consumer AI books ($15-20) because professional audience
- Lower than specialized legal treatises ($75+) for accessibility
- Sweet spot for individual professional purchase + institutional buyers
- CC BY-SA license: print purchase = "support the authors" value proposition

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

### Immediate (First Week)

1. **Author Central:** Set up author pages for all three authors with bios, photos, and links to ai4lf.com
2. **A+ Content:** Apply for enhanced product page with:
   - Define → Design → Govern framework visual
   - Author credentials comparison table
   - "Who this book is for" grid
3. **Editorial Reviews:** Add endorsement quotes from legal tech/compliance leaders
4. **Verify Links:** Ensure "Look Inside" shows professional formatting

### First 30 Days

5. **Request Additional Categories:** Email KDP Support for:
   - Law / Computers & Internet (if not available at setup)
   - Business & Money / Management & Leadership
6. **Track Rankings:** Monitor category rankings and bestseller badges
7. **Collect Reviews:** Reach out to early readers for verified reviews

### Ongoing (30-90 Days)

8. **Keywords Review:** Analyze search term reports, rotate underperforming keywords
9. **Price Testing:** Consider temporary $14.99 Kindle promotion to boost ranking
10. **Cross-Promotion:** Feature in:
    - Legal technology newsletters (ABA, ILTA)
    - Compliance publications (SCCE, ACAMS)
    - LinkedIn professional groups
    - AI/ML podcasts and blogs

### Professional Channels

**Legal:**
- ABA Legal Technology Resource Center
- ILTACON conference materials
- State bar technology committees
- Law firm innovation partners

**Finance:**
- Financial compliance associations (SCCE, ACAMS)
- Risk management publications
- Fintech industry newsletters
- RegTech vendor partnerships

**Academic:**
- Law school library acquisitions
- Business school AI/ethics courses
- Compliance certification programs
- Continuing legal education (CLE) tie-ins

---

## Quick Reference: Form Values

| Field | Value |
|-------|-------|
| Language | English |
| Title | Agentic AI in Law and Finance |
| Subtitle | Navigating a New Era of Autonomous Systems |
| Series | (blank) |
| Edition | 1 |
| Author 1 | Michael J. Bommarito II |
| Author 2 | Daniel M. Katz |
| Author 3 | Jillian Bommarito |
| ISBN (Print) | 979-8-9943457-0-2 |
| ISBN (Ebook) | 979-8-9943457-1-9 |
| Rights | I own the copyright... |
| Territories | All territories |
| Audience | Standard adult content |
| Explicit | No |
| Marketplace | Amazon.com |
| Trim | 6" × 9" |
| Interior | Black & white on white |
| Bleed | No |
| DRM | Off (CC BY-SA license) |
| KDP Select | No (open license) |
| Paperback Price | $29.99 |
| Kindle Price | $19.99 |

---

## References

- [KDP Cover Calculator](https://kdp.amazon.com/cover-calculator)
- [KDP Print Specifications](https://kdp.amazon.com/en_US/help/topic/G201834180)
- [Kindle Print Replica Guidelines](https://kdp.amazon.com/en_US/help/topic/G202059480)
- [BISAC Subject Codes](https://www.bisg.org/complete-bisac-subject-headings-list)
