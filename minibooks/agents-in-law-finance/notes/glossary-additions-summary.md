# Glossary Reference Additions Summary

## Task Overview
Add `\glsadd{}` references for SIX PROPERTIES glossary terms in the minibook:
- goal
- perception
- action
- iteration
- adaptation
- termination

## Existing References Found

Already present in the codebase:
- `\glsadd{goal}` in chapters/01-what-is-agent/sections/01-introduction.tex (line 59)
- `\glsadd{goal}` in chapters/02-how-to-design/sections/03-intent.tex (line 45)
- `\glsadd{perception}` in chapters/01-what-is-agent/sections/01-introduction.tex (line 63)
- `\glsadd{perception}` in chapters/02-how-to-design/sections/04-perception.tex (line 22)
- `\glsadd{action}` in chapters/01-what-is-agent/sections/01-introduction.tex (line 67)
- `\glsadd{action}` in chapters/02-how-to-design/sections/05-action.tex (line 19)
- `\glsadd{iteration}` in chapters/01-what-is-agent/sections/01-introduction.tex (line 106)
- `\glsadd{adaptation}` in chapters/01-what-is-agent/sections/01-introduction.tex (line 110)
- `\glsadd{adaptation}` in chapters/02-how-to-design/sections/06-memory.tex (line 162)
- `\glsadd{termination}` in chapters/01-what-is-agent/sections/01-introduction.tex (line 114)
- `\glsadd{termination}` in chapters/02-how-to-design/sections/08-termination.tex (line 19)

## Strategic Locations for New References

### Chapter 01: What Is an Agent

**File: chapters/01-what-is-agent/sections/06-analytical-framework.tex**

1. **Pattern 1 keybox (line 12)** - Add `\glsadd{goal}` after opening brace
   - Context: "Pattern 1: Goal-Directedness" - key discussion of goal property

2. **Pattern 2 keybox (line 16)** - Add `\glsadd{perception}`, `\glsadd{action}`, `\glsadd{iteration}`
   - Context: "Pattern 2: Perception–Action Coupling" - discusses all three properties together

3. **Pattern 4 keybox (line 24)** - Add `\glsadd{termination}` before existing `\glsadd{escalation}`
   - Context: "Pattern 4: Termination" - key discussion of termination property

4. **Thermostats paragraph (line 150)** - Add `\glsadd{adaptation}` at start
   - Context: Explains why thermostats lack adaptation property

### Chapter 02: How to Design

**File: chapters/02-how-to-design/sections/07-planning.tex**
- Line 16: Planning paragraph discussing goal decomposition

**File: chapters/02-how-to-design/sections/08-termination.tex**
- Already has `\glsadd{termination}` at line 19

### Chapter 03: How to Govern

**File: chapters/03-how-to-govern/sections/03-dimensional_calibration.tex**
- Line 26: Goal Dynamics dimension definition
- Line 170-197: Goal Dynamics Calibration subsection

## Principles Applied

1. **Not every mention** - Only substantive discussions where the property is explained or defined
2. **Avoid common usage** - "goal" as regular English word vs. "goal" as agent property
3. **Definition boxes preferred** - Add at start of key/definition boxes
4. **Section-level coverage** - One reference per major section discussing the property
5. **No duplication** - Check for existing nearby references within 5-10 lines

## Files to Edit

Priority order based on importance and clarity of context:

1. ✅ chapters/01-what-is-agent/sections/06-analytical-framework.tex (4 additions)
2. chapters/02-how-to-design/sections/07-planning.tex (1-2 additions)
3. chapters/03-how-to-govern/sections/03-dimensional_calibration.tex (1-2 additions)

## Status

- [IN PROGRESS] Chapter 01 analytical framework edits
- [PENDING] Chapter 02 planning section
- [PENDING] Chapter 03 governance calibration
