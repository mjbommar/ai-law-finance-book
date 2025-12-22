# Glossary Guide

**Last Updated**: 2025-12-21
**Purpose**: Best practices for using the LaTeX `glossaries` package in this project

---

## Overview

This project uses the `glossaries` package to maintain a unified glossary of key terms with automatic page number tracking. Terms are defined once and can be referenced throughout the document, with the glossary automatically listing all pages where each term appears.

---

## Quick Reference

### Referencing Terms

| Command | Output | Use Case |
|---------|--------|----------|
| `\gls{agent}` | agent | Normal inline reference |
| `\Gls{agent}` | Agent | Start of sentence (capitalized) |
| `\glspl{agent}` | agents | Plural form |
| `\Glspl{agent}` | Agents | Plural at start of sentence |
| `\glsadd{agent}` | *(nothing printed)* | Add page reference without printing term |

### Examples

```latex
% Normal usage - prints term and registers page
An \gls{agent} must exhibit goal-directed behavior.

% Start of sentence - auto-capitalizes
\Gls{adaptation} allows systems to learn from experience.

% Plural forms
Multiple \glspl{agent} can coordinate through delegation.

% Silent page registration (use in definition boxes)
\begin{definitionbox}[title={Agent}]
  \glsadd{agent}
  A system exhibiting Goal, Perception, and Action...
\end{definitionbox}
```

---

## When to Use Each Command

### Use `\gls{key}` when:
- You want to print the term in running text
- The term should appear in its defined form
- You want to register this page in the glossary

### Use `\glsadd{key}` when:
- The term is already visible (e.g., in a definition box title)
- You want to register the page without printing anything
- You're in a heading or caption where the term appears naturally

### Use `\Gls{key}` when:
- The term starts a sentence
- You need the capitalized form

---

## Adding New Terms

Terms are defined in `glossary-entries.tex` (for minibooks) or the chapter's glossary file.

### Basic Entry

```latex
\newglossaryentry{key}{
  name={Display Name},
  description={Definition text without trailing period}
}
```

### Entry with Plural Form

```latex
\newglossaryentry{agent}{
  name={Agent},
  plural={Agents},
  description={A system exhibiting Goal, Perception, and Action (GPA)}
}
```

### Entry with Custom First Use

```latex
\newglossaryentry{mcp}{
  name={MCP},
  first={Model Context Protocol (MCP)},
  description={An open protocol for connecting AI models to external tools}
}
```

---

## Project Configuration

### Package Options (in `preamble.tex`)

```latex
\usepackage[
  toc,                    % Add glossary to table of contents
  section=chapter,        % Format glossary as chapter-level heading
  nogroupskip,            % No extra space between letter groups
  nopostdot,              % No period after descriptions
  style=altlist,          % Term on own line, description below
  automake=immediate      % Auto-run makeglossaries via shell escape
]{glossaries}

\makeglossaries
```

### Key Options Explained

| Option | Effect |
|--------|--------|
| `toc` | Glossary appears in table of contents |
| `section=chapter` | Glossary gets chapter-level formatting |
| `nogroupskip` | No extra vertical space between A, B, C groups |
| `nopostdot` | No automatic period after descriptions |
| `style=altlist` | Term on its own line with description below |
| `automake=immediate` | Runs makeglossaries automatically during build |

### Build Process

With `automake=immediate`, the standard `make pdf` handles everything:

```bash
make pdf    # Automatically runs makeglossaries
```

No manual intervention or special build steps required.

---

## File Organization

### Minibook Structure

```
minibooks/agents-in-law-finance/
├── preamble.tex           # Package configuration
├── glossary-entries.tex   # Term definitions
├── main.tex               # Includes glossary-entries, prints glossary
└── chapters/
    └── */sections/*.tex   # Use \gls{} and \glsadd{} here
```

### In `main.tex`

```latex
% After preamble
\input{glossary-entries}

% In backmatter
\printglossary[title={Glossary of Key Terms}]
```

---

## Best Practices

### 1. Define Terms Centrally

Keep all term definitions in one file (`glossary-entries.tex`) for consistency. Group related terms with comments:

```latex
% ----------------------------------------------------------------------------
% CORE FRAMEWORK TERMS
% ----------------------------------------------------------------------------

\newglossaryentry{agent}{...}
\newglossaryentry{agentic-system}{...}

% ----------------------------------------------------------------------------
% GOVERNANCE TERMS
% ----------------------------------------------------------------------------

\newglossaryentry{human-in-the-loop}{...}
```

### 2. Use `\glsadd{}` in Definition Boxes

When a term appears in a definition box title, use `\glsadd{}` to register the page without duplicating the term:

```latex
\begin{definitionbox}[title={Human-in-the-Loop (HITL)}]
  \glsadd{human-in-the-loop}
  A governance model where humans approve each significant agent action...
\end{definitionbox}
```

### 3. Be Consistent with Keys

Use lowercase, hyphenated keys that match the concept:

```latex
% Good
\newglossaryentry{human-in-the-loop}{...}
\newglossaryentry{three-level-hierarchy}{...}

% Avoid
\newglossaryentry{HITL}{...}           % All caps
\newglossaryentry{threeLevelHierarchy}{...}  % camelCase
```

### 4. Write Descriptions Without Trailing Periods

The `nopostdot` option means descriptions should not end with periods:

```latex
% Good
description={A system exhibiting Goal, Perception, and Action}

% Avoid
description={A system exhibiting Goal, Perception, and Action.}
```

### 5. Don't Overuse `\gls{}`

Not every mention needs glossary markup. Use `\gls{}` for:
- First significant use in a section
- Key definitional contexts
- Places where readers might want to look up the term

Avoid using it for every single mention, which clutters the page number list.

### 6. Rebuild After Adding Terms

After adding new glossary entries, you may need two builds for page numbers to stabilize:

```bash
make clean
make pdf
make pdf   # Second pass ensures cross-references resolve
```

---

## Troubleshooting

### Glossary Not Appearing

1. Check that `\makeglossaries` is in the preamble
2. Check that `\printglossary` is in the document
3. Ensure at least one term is referenced via `\gls{}` or `\glsadd{}`
4. Try `make clean && make pdf`

### Page Numbers Missing

- Ensure `automake=immediate` is set (runs makeglossaries automatically)
- May need two compilation passes for page numbers to resolve

### Term Not Found Error

```
Package glossaries Warning: No glossary entry for 'unknown-key'
```

- Check spelling of the key in `\gls{key}`
- Ensure the term is defined in `glossary-entries.tex`
- Verify `\input{glossary-entries}` appears before first use

### Shell Escape Required

The `automake=immediate` option requires shell escape. If you see errors about restricted shell escape:

```bash
# latexmk should handle this automatically
# If not, ensure your editor/build system allows shell escape
pdflatex -shell-escape main.tex
```

---

## Current Glossary Terms

The minibook defines 25 terms in 5 categories:

| Category | Terms |
|----------|-------|
| **Core Framework** | agent, agentic-system, ai-agent, gpa, iat, three-level-hierarchy |
| **Six Properties** | goal, perception, action, iteration, adaptation, termination |
| **Architectural** | trigger, intent, tools, memory, planning, escalation, delegation |
| **Technical Patterns** | rag, vector-store, in-context-learning, mcp, react |
| **Governance** | human-in-the-loop, human-on-the-loop, human-in-command, dimensional-calibration, governance-surface |

---

## References

- [glossaries package documentation (CTAN)](https://ctan.org/pkg/glossaries)
- [Beginner's Guide to glossaries](https://tug.ctan.org/macros/latex/contrib/glossaries/glossariesbegin.pdf)
- [User Manual for glossaries.sty](https://mirror.math.princeton.edu/pub/CTAN/macros/latex/contrib/glossaries/glossaries-user.pdf)
- [Incorporating makeglossaries into builds](https://www.dickimaw-books.com/latex/buildglossaries/)
