# Color System Guide

**Version:** 1.0
**Last Updated:** 2025-01-31
**Document Type:** Style Guide & Validation Checklist

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Quick Reference](#quick-reference)
4. [Usage Guidelines](#usage-guidelines)
5. [Validation Checklist](#validation-checklist)
6. [Common Mistakes](#common-mistakes)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)

---

## Overview

This document defines the **Educational Semantic Color System** used throughout the textbook. The system uses a four-layer architecture designed for:

- **Clarity:** Colors named by educational purpose, not visual appearance
- **Consistency:** Every content type follows the same three-variant pattern
- **Maintainability:** Centralized color definitions that can be updated globally
- **Modularity:** Clear separation between primitives, semantics, and components

### Design Philosophy

- Semantic naming for intuitive usage (e.g., `definition`, `example`, `key`, `caution`)
- Three-tier variant system: `-dark` (text/borders), `-base` (accents), `-light` (backgrounds)
- Western cultural conventions: blue=formal, green=practical, amber=important, red=warning
- Professional, muted tones suitable for academic content

---

## Architecture

### Four-Layer System

```
Layer 1: PRIMITIVES    → Raw RGB values (slate-900, green-600, etc.)
         ↓
Layer 2: SEMANTICS     → Educational content types (definition, example, key, etc.)
         ↓
Layer 3: COMPONENTS    → Specific usage (bg-*, border-*, text-*)
         ↓
Layer 4: LEGACY        → Backward compatibility aliases
```

### Layer Descriptions

**Layer 1: Primitives** (`main.tex:82-131`)
- Raw color palette organized by family (slate, green, amber, red, teal, indigo, gray)
- Numeric scale: 900 (darkest) → 100 (lightest)
- **Modify these to rebrand the entire document**

**Layer 2: Semantics** (`main.tex:135-189`)
- Educational content types mapped to primitive colors
- **Use these when creating content boxes and callouts**
- Pattern: `[type]-dark`, `[type]-base`, `[type]-light`

**Layer 3: Components** (`main.tex:193-228`)
- Explicit usage contexts (backgrounds, borders, text)
- Makes code self-documenting
- **Use these in tcolorbox definitions and custom components**

**Layer 4: Legacy** (`main.tex:232-255`)
- Backward compatibility for old color names
- Allows gradual migration without breaking changes

---

## Quick Reference

### Educational Content Types (Layer 2)

| Type | Color Family | Use For | Dark | Base | Light |
|------|-------------|---------|------|------|-------|
| **definition** | Blue | Formal definitions, theoretical concepts | `definition-dark` | `definition-base` | `definition-light` |
| **example** | Green | Concrete examples, demonstrations | `example-dark` | `example-base` | `example-light` |
| **key** | Amber | Important takeaways, essential points | `key-dark` | `key-base` | `key-light` |
| **caution** | Red | Warnings, pitfalls, mistakes to avoid | `caution-dark` | `caution-base` | `caution-light` |
| **note** | Neutral | Supplementary info, asides | `note-dark` | `note-base` | `note-light` |
| **theorem** | Indigo | Formal statements, proofs | `theorem-dark` | `theorem-base` | `theorem-light` |
| **practice** | Teal | Exercises, hands-on activities | `practice-dark` | `practice-base` | `practice-light` |

### Component Colors (Layer 3)

| Component | Purpose | Recommended Colors |
|-----------|---------|-------------------|
| Box backgrounds | `colback=` | `bg-definition`, `bg-example`, `bg-key`, `bg-caution`, `bg-note`, `bg-theorem`, `bg-practice` |
| Box borders | `colframe=` | `border-definition`, `border-example`, `border-key`, `border-caution`, `border-note`, `border-theorem`, `border-practice` |
| Box titles (color) | `coltitle=` | `white` (for dark backgrounds), `[type]-dark` (for light backgrounds) |
| Inline text | `\color{}` or `\textcolor{}` | `primary`, `text-secondary`, `text-muted`, `accent` |
| Section headings | `\color{}` | `primary` |
| Hyperlinks | `linkcolor=`, `urlcolor=` | `primary` |
| Citations | `citecolor=` | `accent` |

### Grayscale (Layer 1)

| Color | RGB | Usage |
|-------|-----|-------|
| `gray-900` | (30,32,34) | Primary body text |
| `gray-700` | (73,80,87) | Secondary text |
| `gray-600` | (95,100,105) | Muted/de-emphasized text |
| `gray-500` | (134,142,150) | Medium gray |
| `gray-300` | (210,215,220) | Light borders |
| `gray-100` | (247,248,250) | Subtle backgrounds |

---

## Usage Guidelines

### When to Use Each Semantic Type

#### `definition-*` (Blue)
**Use for:**
- Formal term definitions
- Theoretical frameworks
- Conceptual explanations
- Foundational knowledge

**Example:**
```latex
\begin{definitionbox}[title={Agent}]
An agent is a computational entity...
\end{definitionbox}
```

#### `example-*` (Green)
**Use for:**
- Concrete code examples
- Real-world case studies
- Demonstrations
- Practical applications

**Example:**
```latex
\begin{tcolorbox}[colback=bg-example, colframe=example-base, title={Example: Simple Agent}]
Here's how you might implement...
\end{tcolorbox}
```

#### `key-*` (Amber/Orange)
**Use for:**
- Important takeaways
- Must-remember concepts
- Essential points
- Chapter summaries

**Example:**
```latex
\begin{keybox}[title={Key Takeaway}]
The most important distinction is...
\end{keybox}
```

#### `caution-*` (Red)
**Use for:**
- Common mistakes
- Pitfalls to avoid
- Deprecated patterns
- Critical warnings

**Example:**
```latex
\begin{tcolorbox}[colback=bg-caution, colframe=caution-base, title={Common Mistake}]
Don't confuse agents with...
\end{tcolorbox}
```

#### `note-*` (Neutral)
**Use for:**
- Sidebar notes
- Historical context
- Tangential information
- Further reading suggestions
- Draft notices

**Example:**
```latex
\begin{highlightbox}[colback=bg-note, colframe=border-note]
For more background on this topic...
\end{highlightbox}
```

#### `theorem-*` (Indigo)
**Use for:**
- Mathematical theorems
- Formal logical statements
- Lemmas and proofs
- Rigorous formal arguments

**Example:**
```latex
\begin{tcolorbox}[colback=bg-theorem, colframe=theorem-base, title={Theorem 1}]
For all agents A, if A exhibits autonomy...
\end{tcolorbox}
```

#### `practice-*` (Teal)
**Use for:**
- Practice exercises
- Coding challenges
- Hands-on activities
- "Try it yourself" sections

**Example:**
```latex
\begin{tcolorbox}[colback=bg-practice, colframe=practice-base, title={Exercise}]
Implement an agent that...
\end{tcolorbox}
```

### Structural Elements

#### Headings and Sections
```latex
% Section headings - use primary
\titleformat{\section}
  {\Large\bfseries\color{primary}}

% Subsections - use primary
\titleformat{\subsection}
  {\large\bfseries\color{primary}}

% Subsubsections - use text-secondary
\titleformat{\subsubsection}
  {\normalsize\bfseries\color{text-secondary}}
```

#### Hyperlinks
```latex
% In hyperref setup
\hypersetup{
  linkcolor=primary,      % Internal links
  citecolor=accent,       % Citations
  urlcolor=primary,       % URLs
}
```

#### Inline Text Emphasis
```latex
% Key terms
\keyterm{important term}  % Uses primary color

% Inline colored text
\textcolor{text-secondary}{secondary information}
\textcolor{text-muted}{de-emphasized text}
\textcolor{accent}{emphasized highlight}
```

---

## Validation Checklist

Use this checklist to ensure color system compliance. Each item includes verification commands.

### ✅ Pre-Check: Files to Audit

- [ ] `main.tex` - Main document and color definitions
- [ ] `sections/*.tex` - All content section files
- [ ] Any new `.tex` files added to the project

---

### Section 1: Color Definitions (main.tex only)

#### ☑ Verify Layer 1 (Primitives) is Complete

```bash
# Check that all primitive color families are defined
grep -E "definecolor\{(slate|green|amber|red|teal|indigo|gray|cream)-" main.tex | wc -l
# Expected: At least 20 primitive colors
```

**Pass criteria:** At least 20 primitive color definitions present

---

#### ☑ Verify Layer 2 (Semantics) is Complete

```bash
# Check that all semantic types have dark/base/light variants
grep -E "definecolor\{(definition|example|key|caution|note|theorem|practice)-(dark|base|light)" main.tex | wc -l
# Expected: 21 (7 types × 3 variants)
```

**Pass criteria:** Exactly 21 semantic color definitions (7 types × 3 variants)

**Required semantic types:**
- [ ] `definition-dark`, `definition-base`, `definition-light`
- [ ] `example-dark`, `example-base`, `example-light`
- [ ] `key-dark`, `key-base`, `key-light`
- [ ] `caution-dark`, `caution-base`, `caution-light`
- [ ] `note-dark`, `note-base`, `note-light`
- [ ] `theorem-dark`, `theorem-base`, `theorem-light`
- [ ] `practice-dark`, `practice-base`, `practice-light`

---

#### ☑ Verify Layer 3 (Components) is Complete

```bash
# Check component aliases
grep -E "definecolor\{(bg|border|text)-" main.tex | wc -l
# Expected: At least 20 component color aliases
```

**Pass criteria:** At least 20 component color aliases present

**Required component types:**
- [ ] Background colors: `bg-definition`, `bg-example`, `bg-key`, `bg-caution`, `bg-note`, `bg-theorem`, `bg-practice`, `bg-neutral`
- [ ] Border colors: `border-definition`, `border-example`, `border-key`, `border-caution`, `border-note`, `border-theorem`, `border-practice`, `border-neutral`
- [ ] Text colors: `text-primary`, `text-secondary`, `text-muted`

---

### Section 2: tcolorbox Definitions (main.tex)

#### ☑ Check Box Definitions Use Semantic Colors

```bash
# Check definitionbox uses semantic colors
grep -A 20 "newtcolorbox{definitionbox}" main.tex | grep -E "colback|colframe|coltitle"
```

**Expected output should include:**
- `colback=bg-definition` (not `bg-ice` or `agentlightblue`)
- `colframe=border-definition` (not `border-slate`)
- Title background should use `definition-dark`

**Verification:**
- [ ] `definitionbox` uses `bg-definition`, `border-definition`, `definition-dark`
- [ ] `highlightbox` uses `bg-note`, `border-note`, `note-dark`
- [ ] `keybox` uses `bg-key`, `key-base` (for frame and title background)

---

### Section 3: Section/Heading Formatting (main.tex)

#### ☑ Verify Headings Use `primary` Color

```bash
# Check section formatting
grep -A 3 "titleformat{\\\\section}" main.tex | grep "color{"
# Should contain: \color{primary}

grep -A 3 "titleformat{\\\\subsection}" main.tex | grep "color{"
# Should contain: \color{primary}

grep -A 3 "titleformat{\\\\subsubsection}" main.tex | grep "color{"
# Should contain: \color{text-secondary}
```

**Pass criteria:**
- [ ] `\section` uses `\color{primary}` (NOT `agentblue` or `primary-slate`)
- [ ] `\subsection` uses `\color{primary}` (NOT `agentblue` or `primary-slate`)
- [ ] `\subsubsection` uses `\color{text-secondary}` (NOT `darkgray`)
- [ ] `\paragraph` uses `\color{primary}`

---

### Section 4: Table of Contents (main.tex)

#### ☑ Verify ToC Uses `primary` Color

```bash
# Check ToC title
grep -A 2 "contentsname" main.tex | grep "color{"
# Should contain: \color{primary}

# Check ToC section entries
grep -A 5 "titlecontents{section}" main.tex | grep "color{"
# Should contain: \color{primary}
```

**Pass criteria:**
- [ ] ToC title uses `\color{primary}` (NOT `primary-slate`)
- [ ] ToC section entries use `\color{primary}` (NOT `primary-slate`)

---

### Section 5: Hyperlinks (main.tex)

#### ☑ Verify Hyperref Uses Semantic Colors

```bash
# Check hyperref setup
grep -A 10 "hypersetup{" main.tex | grep -E "(linkcolor|citecolor|urlcolor)"
```

**Expected:**
```latex
linkcolor=primary,
citecolor=accent,
urlcolor=primary,
```

**Pass criteria:**
- [ ] `linkcolor=primary` (NOT `agentblue`)
- [ ] `citecolor=accent` (NOT `accentorange`)
- [ ] `urlcolor=primary` (NOT `agentblue`)

---

### Section 6: Caption Formatting (main.tex)

#### ☑ Verify Captions Use `primary` Color

```bash
# Check caption package setup
grep -A 6 "usepackage\[" main.tex | grep -A 6 "caption" | grep "color="
```

**Pass criteria:**
- [ ] `labelfont={bf,color=primary}` (NOT `agentblue`)

---

### Section 7: Title Page (main.tex)

#### ☑ Verify Title Page Uses Semantic Colors

```bash
# Check title
grep -A 10 "\\title{" main.tex | grep "color{"

# Check author
grep -A 5 "\\author{" main.tex | grep "color{"

# Check date
grep -A 3 "\\date{" main.tex | grep "color{"
```

**Pass criteria:**
- [ ] Main title uses `\color{primary}` (NOT `primary-slate`)
- [ ] Subtitle uses `\color{primary}` (NOT `primary-slate`)
- [ ] Tagline uses `\color{text-secondary}` (NOT `secondary-sage` or `darkgray`)
- [ ] Author uses `\color{text-muted}`
- [ ] Date uses `\color{text-muted}`

---

### Section 8: Draft Notice Box (main.tex)

#### ☑ Verify Draft Notice Uses Semantic Colors

```bash
# Check draft notice tcolorbox
grep -A 15 "Draft notice" main.tex | grep -E "colback|colframe|borderline|coltitle"
```

**Pass criteria:**
- [ ] `colback=bg-note` (NOT `bg-ice`)
- [ ] `colframe=border-note` (NOT `border-slate`)
- [ ] `coltitle` uses `note-dark` (NOT `primary-slate`)
- [ ] `borderline west` uses `note-dark` (NOT `primary-slate`)
- [ ] Text uses `\color{note-dark}` (NOT `primary-slate`)

---

### Section 9: Content Files (sections/*.tex)

#### ☑ Scan All Section Files for Legacy Color Names

```bash
# Search for legacy color names that should be replaced
grep -rn "agentblue\|agentlightblue\|primary-slate\|secondary-sage\|bg-ice\|border-slate" sections/

# Search for old amber colors
grep -rn "accentorange\|accent-amber\|bg-amber-light" sections/

# Search for old gray colors
grep -rn "\\bdarkgray\\b\|bg-gray-cool\|border-sage" sections/
```

**Pass criteria:**
- [ ] No instances of `agentblue` (should be `primary`)
- [ ] No instances of `agentlightblue` (should be `bg-definition` or appropriate semantic)
- [ ] No instances of `primary-slate` (should be `primary`)
- [ ] No instances of `secondary-sage` (removed from palette - choose appropriate semantic)
- [ ] No instances of `bg-ice` (should be `bg-definition` or `bg-note`)
- [ ] No instances of `border-slate` (should be `border-definition` or semantic equivalent)
- [ ] No instances of `accentorange` or `accent-amber` (should be `accent` or `key-base`)
- [ ] No instances of `darkgray` (should be `text-muted` or `text-secondary`)

---

#### ☑ Verify tcolorbox Usage in Content Files

```bash
# Find all tcolorbox instances
grep -rn "begin{tcolorbox}" sections/

# For each instance, manually verify:
# 1. Uses appropriate bg-* color for content type
# 2. Uses matching border-* color
# 3. Uses matching title color if applicable
```

**Manual verification for each tcolorbox:**
- [ ] Box background (`colback=`) uses semantic bg color (`bg-definition`, `bg-example`, etc.)
- [ ] Box border (`colframe=`) uses matching semantic border (`border-definition`, `border-example`, etc.)
- [ ] Box title color (`coltitle=`) uses appropriate color (white for dark backgrounds, `[type]-dark` for light backgrounds)

---

#### ☑ Check highlightbox Usage

```bash
# Find all highlightbox instances
grep -rn "begin{highlightbox}" sections/

# Verify highlightbox parameters
grep -A 1 "begin{highlightbox}" sections/ | grep "colback\|colframe"
```

**Common patterns to verify:**
- [ ] Reading path boxes use `bg-definition`, `definition-base` (conceptual/structural content)
- [ ] General notes use `bg-note`, `border-note` (supplementary content)
- [ ] No legacy colors like `bg-ice`, `border-slate` used directly

---

### Section 10: Custom Commands (main.tex)

#### ☑ Verify Custom Command Colors

```bash
# Check keyterm command
grep "newcommand{\\\\keyterm}" main.tex
# Should use: \color{primary}
```

**Pass criteria:**
- [ ] `\keyterm` uses `\color{primary}` (NOT `agentblue`)

---

### Section 11: No Hardcoded RGB Values

#### ☑ Ensure No Direct RGB Colors in Content

```bash
# Search for direct RGB/color definitions in content files
grep -rn "definecolor\|RGB{" sections/

# Search for direct color specifications in boxes
grep -rn "colback={.*RGB\|colframe={.*RGB" sections/
```

**Pass criteria:**
- [ ] No `\definecolor` commands in section files (all colors should be in main.tex)
- [ ] No direct `RGB{...}` specifications in content (use named colors only)

---

### Section 12: Consistency Checks

#### ☑ Verify Consistent Pairing

For each content type, verify that when a background is used, the matching border is used:

```bash
# Example: Check definition boxes use consistent colors
grep -rn "colback=bg-definition" . | while read line; do
  file=$(echo "$line" | cut -d: -f1)
  linenum=$(echo "$line" | cut -d: -f2)
  # Check if matching border is used nearby
  sed -n "$((linenum-2)),$((linenum+5))p" "$file" | grep "border-definition"
done
```

**Manual verification:**
- [ ] Every `bg-definition` is paired with `border-definition` or `definition-base`
- [ ] Every `bg-example` is paired with `border-example` or `example-base`
- [ ] Every `bg-key` is paired with `border-key` or `key-base`
- [ ] Every `bg-caution` is paired with `border-caution` or `caution-base`
- [ ] Every `bg-note` is paired with `border-note` or `note-base`
- [ ] Every `bg-theorem` is paired with `border-theorem` or `theorem-base`
- [ ] Every `bg-practice` is paired with `border-practice` or `practice-base`

---

### Section 13: Compilation Test

#### ☑ Document Compiles Successfully

```bash
# Clean build
rm -f main.aux main.bbl main.bcf main.blg main.log main.out main.run.xml main.toc

# Compile
pdflatex -interaction=nonstopmode main.tex
biber main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

# Check for errors
echo $?  # Should be 0
```

**Pass criteria:**
- [ ] Document compiles without errors
- [ ] No color-related warnings in log
- [ ] PDF is generated successfully

---

### Section 14: Visual Inspection

#### ☑ Manual PDF Review

Open the generated PDF and verify visually:

- [ ] Section headings are consistent blue color (primary)
- [ ] Definition boxes have light blue background with darker blue border
- [ ] Example boxes have light green background with green border
- [ ] Key takeaway boxes have light amber background with orange/amber border
- [ ] Warning/caution boxes have light red/pink background with red border
- [ ] Note boxes have neutral cream/gray background with subtle border
- [ ] All boxes have appropriate contrast and readability
- [ ] Hyperlinks are visible and colored (blue for links, amber for citations)
- [ ] Table of contents uses consistent coloring
- [ ] No jarring color mismatches or inconsistencies

---

## Common Mistakes

### ❌ Mistake 1: Using Legacy Color Names

**Wrong:**
```latex
\begin{tcolorbox}[colback=bg-ice, colframe=border-slate]
```

**Right:**
```latex
\begin{tcolorbox}[colback=bg-definition, colframe=border-definition]
```

---

### ❌ Mistake 2: Mismatched Background and Border

**Wrong:**
```latex
\begin{tcolorbox}[colback=bg-example, colframe=border-definition]
```

**Right:**
```latex
\begin{tcolorbox}[colback=bg-example, colframe=example-base]
```

---

### ❌ Mistake 3: Using `agentblue` Instead of `primary`

**Wrong:**
```latex
\titleformat{\section}{\Large\bfseries\color{agentblue}}
```

**Right:**
```latex
\titleformat{\section}{\Large\bfseries\color{primary}}
```

---

### ❌ Mistake 4: Using Wrong Semantic Type

**Wrong:**
```latex
% Using "example" colors for a formal definition
\begin{tcolorbox}[colback=bg-example, title={Definition: Agent}]
```

**Right:**
```latex
% Use "definition" colors for formal definitions
\begin{tcolorbox}[colback=bg-definition, colframe=definition-base, title={Definition: Agent}]
```

---

### ❌ Mistake 5: Hardcoding RGB Values

**Wrong:**
```latex
\begin{tcolorbox}[colback={RGB}{240,246,252}]
```

**Right:**
```latex
\begin{tcolorbox}[colback=bg-definition]
```

---

### ❌ Mistake 6: Forgetting Title Colors

**Wrong:**
```latex
% Title text may be hard to read against light background
\begin{tcolorbox}[
  colback=bg-definition,
  colframe=definition-base,
  title={Important}
]
```

**Right:**
```latex
% Specify title color for readability
\begin{tcolorbox}[
  colback=bg-definition,
  colframe=definition-base,
  coltitle=white,  % or definition-dark depending on title background
  title={Important}
]
```

---

### ❌ Mistake 7: Using `-base` for Backgrounds

**Wrong:**
```latex
% Base colors are too saturated for backgrounds
\begin{tcolorbox}[colback=example-base]
```

**Right:**
```latex
% Light variants are designed for backgrounds
\begin{tcolorbox}[colback=example-light]
% Or use the component alias
\begin{tcolorbox}[colback=bg-example]
```

---

### ❌ Mistake 8: Inconsistent Text Colors

**Wrong:**
```latex
% Mixing old and new text color names
Some \textcolor{darkgray}{muted text} and \textcolor{text-muted}{more muted}.
```

**Right:**
```latex
% Use consistent semantic names
Some \textcolor{text-muted}{muted text} and \textcolor{text-muted}{more muted}.
```

---

## Examples

### Example 1: Creating a Definition Box

```latex
\begin{definitionbox}[title={Autonomy}]
  Autonomy refers to the degree to which an agent operates independently
  without direct human intervention.
\end{definitionbox}
```

**Colors used:**
- Background: `bg-definition` (light blue)
- Border: `border-definition` (medium blue)
- Title background: `definition-dark` (dark blue)
- Title text: `white`

---

### Example 2: Creating an Example Box

```latex
\begin{tcolorbox}[
  enhanced,
  colback=bg-example,
  colframe=example-base,
  title={Example: Autonomous Agent},
  coltitle=white,
  boxrule=1.5pt,
  breakable
]
  A self-driving car demonstrates autonomy by making navigation
  decisions without human input.
\end{tcolorbox}
```

**Colors used:**
- Background: `bg-example` (light green)
- Border: `example-base` (medium green)
- Title text: `white`

---

### Example 3: Creating a Key Takeaway Box

```latex
\begin{keybox}[title={Key Point}]
  The essential distinction is between \textit{goal-directed behavior}
  and \textit{goal-directed autonomy}.
\end{keybox}
```

**Colors used:**
- Background: `bg-key` (light amber)
- Border: `key-base` (medium amber)
- Title background: `key-base` (medium amber)
- Title text: `white`

---

### Example 4: Creating a Caution Box

```latex
\begin{tcolorbox}[
  colback=bg-caution,
  colframe=caution-base,
  title={Common Mistake},
  coltitle=white,
  boxrule=1.5pt
]
  Don't confuse an agent's \textit{goals} with its \textit{capabilities}.
  An agent may have sophisticated capabilities but simple goals.
\end{tcolorbox}
```

**Colors used:**
- Background: `bg-caution` (light red/pink)
- Border: `caution-base` (medium red)
- Title text: `white`

---

### Example 5: Inline Text Coloring

```latex
% Primary emphasis
The \textcolor{primary}{most important concept} is autonomy.

% Secondary information
\textcolor{text-secondary}{This is supplementary information.}

% De-emphasized text
\textcolor{text-muted}{Less important details here.}

% Key term (uses custom command)
An \keyterm{agent} is a computational entity...
```

---

### Example 6: Section with Colored Heading

```latex
\section{Introduction to Agents}
% Section heading automatically uses primary color

\subsection{Historical Context}
% Subsection automatically uses primary color

\subsubsection{Early Definitions}
% Subsubsection automatically uses text-secondary color
```

---

## Troubleshooting

### Issue: Colors Not Appearing

**Symptom:** Box backgrounds or text appear in default black/white

**Diagnosis:**
```bash
# Check if color is defined
grep "definecolor{YOUR_COLOR_NAME}" main.tex
```

**Solution:**
- Verify color is defined in main.tex Layer 1, 2, or 3
- Check for typos in color name
- Ensure xcolor package is loaded

---

### Issue: Color Mismatch

**Symptom:** Box background and border don't match expected content type

**Diagnosis:**
- Review the semantic color table in Quick Reference
- Verify the content type matches the color choice

**Solution:**
- Use the correct semantic type for your content
- Follow the consistency pattern: `bg-[type]` with `border-[type]`

---

### Issue: Compilation Errors

**Symptom:** `! Undefined color 'COLOR_NAME'`

**Diagnosis:**
```bash
# Verify color definition exists
grep "definecolor{COLOR_NAME}" main.tex
```

**Solution:**
- Add missing color definition to appropriate layer in main.tex
- Fix typo in color name
- Ensure color is defined before first use

---

### Issue: Low Contrast / Readability

**Symptom:** Text is hard to read against box background

**Diagnosis:**
- Check if using `-dark` variant for background (wrong - too saturated)
- Check if title color contrasts with title background

**Solution:**
- Use `-light` variants for backgrounds
- Use `white` for title text when title background is dark
- Use `[type]-dark` for title text when title background is light

---

### Issue: Legacy Color Names Still Present

**Symptom:** Document uses old color names like `agentblue`

**Diagnosis:**
```bash
# Find all legacy usage
grep -rn "agentblue\|primary-slate\|secondary-sage" .
```

**Solution:**
- Replace systematically using the mapping:
  - `agentblue` → `primary`
  - `primary-slate` → `primary`
  - `agentlightblue` → `bg-definition`
  - `secondary-sage` → Choose appropriate semantic color
  - `darkgray` → `text-muted` or `text-secondary`

---

## Migration from Legacy Colors

If you encounter legacy color names in old content, use this mapping:

| Legacy Name | New Semantic Name | Context |
|-------------|-------------------|---------|
| `agentblue` | `primary` | Headings, links, key terms |
| `agentlightblue` | `bg-definition` | Definition box backgrounds |
| `primary-slate` | `primary` | All structural elements |
| `secondary-sage` | *REMOVED* | Choose appropriate semantic color based on content |
| `accent-amber` | `accent` or `key-base` | Depends on context |
| `accentorange` | `accent` | Emphasis, citations |
| `bg-ice` | `bg-definition` | Definition box backgrounds |
| `bg-cream` | `bg-note` | Note/highlight box backgrounds |
| `bg-amber-light` | `bg-key` | Key takeaway backgrounds |
| `bg-gray-cool` | `bg-neutral` | Neutral backgrounds |
| `border-slate` | `border-definition` | Definition box borders |
| `border-sage` | *REMOVED* | Choose appropriate semantic border |
| `bordergray` | `border-neutral` | Neutral borders |
| `darkgray` | `text-muted` or `text-secondary` | Depends on emphasis level |
| `highlightgray` | `bg-note` | Highlight backgrounds |

---

## Quick Checklist Summary

**Before committing changes:**

1. ✅ Run all grep commands in validation checklist
2. ✅ Verify no legacy color names remain in sections/*.tex
3. ✅ Check all tcolorbox instances use semantic colors
4. ✅ Compile document successfully (no errors)
5. ✅ Visual PDF inspection for consistency
6. ✅ Verify semantic color choice matches content type
7. ✅ Check background/border color pairing is consistent

**For new content:**

1. ✅ Choose appropriate semantic type (definition/example/key/caution/note/theorem/practice)
2. ✅ Use component colors (bg-*, border-*, text-*)
3. ✅ Verify title color contrasts with background
4. ✅ Test compilation before committing

---

## Document Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-31 | Initial comprehensive guide and checklist |

---

**For questions or clarifications, see STYLE.md**
