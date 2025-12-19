# Chapter 7 Rewrite Plan: "How to Build an Agent"

## Executive Summary

This plan reorganizes Chapter 7 around **10 Fundamental Questions** that every agent designer must answer. Each question corresponds to an organizational analogy that makes abstract concepts concrete for legal and financial professionals.

**Key Insight**: The existing content is high-quality but organized around technical components (Tools, Memory, Planning). The rewrite elevates the organizational analogy—already present in the introduction—into the primary organizing principle.

---

## The 10-Question Framework

| # | Simple Question | Section Name | Organizational Analogy | Ch.6 Property |
|---|----------------|--------------|------------------------|---------------|
| 1 | How does an agent know when it has work to do? | **Triggers** | Inbox, phone, calendar | Entry to GPA loop |
| 2 | How does an agent understand what's being asked? | **Intent** | Reading the assignment memo | Goal specification |
| 3 | How does an agent find things out? | **Perception** | Library and database access | Perception |
| 4 | How does an agent make things happen? | **Action** | Filing, sending, executing | Action |
| 5 | How does an agent remember things? | **Memory** | Case file, firm knowledge base | Adaptation |
| 6 | How does an agent break a big job into steps? | **Planning** | Project plan and task list | Goal decomposition |
| 7 | How does an agent know when it's done? | **Termination** | Deliverable acceptance criteria | Termination |
| 8 | How does an agent know when to ask for help? | **Escalation** | Going to the supervisor | Termination (handoff) |
| 9 | How does an agent work with other agents? | **Delegation** | Coordinating with specialists | Multi-agent Iteration |
| 10 | How do we keep the agent safe? | **Governance** | Compliance, audit, oversight | Bridge to Ch.8 |

---

## New Chapter Structure

```
00-how-to-read.tex          [EXPAND]     Quick orientation (~500 words)
01-introduction.tex         [REWRITE]    Framework motivation + GPA+IAT bridge
02-triggers.tex             [ADAPT]      Q1: When does work arrive?
03-intent.tex               [NEW]        Q2: Understanding the ask
04-perception.tex           [ADAPT]      Q3: Finding information
05-action.tex               [ADAPT]      Q4: Making things happen
06-memory.tex               [ADAPT]      Q5: Remembering context
07-planning.tex             [ADAPT]      Q6: Breaking down work
08-termination.tex          [ADAPT]      Q7: Knowing when done
09-escalation.tex           [ADAPT]      Q8: When to ask for help
10-delegation.tex           [ADAPT]      Q9: Working with others
11-governance.tex           [NEW]        Q10: Keeping agents safe
12-synthesis.tex            [ADAPT]      Reference architectures (case studies)
13-resources.tex            [ADAPT]      Further learning
14-conclusion.tex           [REWRITE]    Synthesis + Ch.8 bridge
```

---

## Section-by-Section Instructions

### Section 00: How to Read This Chapter
**Source**: `00-how-to-read.tex` (16 lines → ~60 lines)
**Action**: EXPAND

**Instructions**:
1. Keep three-chapter arc positioning (Ch.6 theory → Ch.7 build → Ch.8 govern)
2. Add explicit enumeration of all 10 questions with one-line organizational analogies
3. Keep "technical but conceptual" framing for non-engineer audience
4. Add paragraph: "Who Should Read This Chapter?" with practitioner value props
5. Update cross-references to use new labels
6. Maintain voice: "you" for guidance throughout
7. Keep as unnumbered section with `\addcontentsline`

**Content to Preserve**:
- "Like understanding how a legal department or asset manager organizes work"
- "Vocabulary to assess vendor claims, participate in procurement decisions"

---

### Section 01: Introduction
**Source**: `01-introduction.tex` (109 lines → ~150 lines)
**Action**: MAJOR REWRITE

**Instructions**:
1. Open with GPA+IAT recap from Ch.6 (keep lines 14-18)
2. NEW subsection 1.1: "Ten Fundamental Questions" - elevate organizational analogy to organizing principle
3. NEW subsection 1.2: "The GPA+IAT Bridge" - explicit mapping table showing how 10 questions implement Ch.6 properties
4. RELOCATE definition boxes (Tool, Memory, Planning) to their respective Q sections
5. RELOCATE event-driven content (lines 46-57) to Section 02 (Triggers)
6. Keep and enhance "Architecture Enables Governance" highlightbox (lines 97-103)
7. Add visual figure: three-chapter progression diagram
8. Add roadmap paragraph previewing all 10 sections

**Content to Preserve**:
- "Like an associate locked in a library with no internet" (line 31)
- "Like an associate who keeps running searches without a research strategy" (line 39)
- GPA+IAT component mapping (lines 63-80) - adapt into bridge table

**New Content Required**:
- 10-question enumeration with organizational analogies
- GPA+IAT ↔ 10 Questions mapping table
- Chapter roadmap paragraph

---

### Section 02: Triggers (Q1)
**Source**: `02-triggers-channels.tex` (233 lines → ~200 lines)
**Action**: ADAPT with minor restructure

**Instructions**:
1. Open with Q1 framing: "How does an agent know when it has work to do?"
2. Add organizational analogy: "Just as work reaches professionals through inbox, phone, and calendar..."
3. Keep four-channel taxonomy: External Feeds, Human Prompts, Scheduled Jobs, Escalation Events
4. PRESERVE "Speed vs. Reasoning" highlightbox verbatim (lines 47-59) - critical for financial practitioners
5. Keep Event Routing & Prioritization subsection
6. Keep TikZ diagram (lines 137-184)
7. SPLIT escalation content (lines 108-115) - move to Section 09 (Escalation)
8. Keep Surfaces subsection but make it brief
9. Add "Evaluating Triggers" brief subsection (from 05-evaluation content)
10. Add cross-references: Ch.6 §Iteration, Q8 (Escalation), Ch.8 trigger governance

**Content to Preserve**:
- All four channel types with legal/financial examples
- CM/ECF, PACER, SEC EDGAR, Bloomberg/Reuters examples
- Speed vs. Reasoning highlightbox
- Event routing architecture diagram

---

### Section 03: Intent (Q2)
**Source**: NEW (with fragments from `01-introduction.tex` and `03-architecture.tex`)
**Action**: CREATE NEW

**Instructions**:
1. Open with Q2 framing: "How does an agent understand what's being asked?"
2. Add organizational analogy: "Just as a professional reads the assignment memo, clarifies ambiguous instructions..."
3. Extract planning "intent" content from 03-architecture.tex (lines 249-259)
4. NEW subsection: Goal extraction from natural language
5. NEW subsection: Ambiguity detection and clarification
6. NEW subsection: Constraint identification (deadlines, budgets, restrictions)
7. NEW subsection: Intent validation patterns
8. Add legal example: "Review this credit agreement for risks" → decomposed intent
9. Add financial example: "Rebalance to reduce tech exposure" → decomposed intent
10. Add cross-references: Ch.6 §Goal, Q6 (Planning), Ch.8 intent governance

**Key Points to Cover**:
- Difference between instruction and intent
- When to ask for clarification vs. proceed
- Mapping user language to system capabilities
- Handling contradictory or impossible requests

---

### Section 04: Perception (Q3)
**Source**: `03-architecture.tex` (Tools section) + `04-protocols.tex` (MCP Resources)
**Action**: ADAPT and MERGE

**Instructions**:
1. Open with Q3 framing: "How does an agent find things out?"
2. Add organizational analogy: "Just as a professional has library access, database subscriptions..."
3. RELOCATE Tool definition box from introduction
4. Include tool categories for READ operations: information retrieval, document processing
5. Include MCP Resources capability (from 04-protocols.tex) - standardized read-only data access
6. Include MCP architecture diagram (figure from 04-protocols.tex)
7. PRESERVE "MCP Core Concept" keybox with M×N integration math
8. Include Memory as perception into institutional knowledge (RAG, vector stores)
9. Add Tool Design Principles for perception tools
10. Add "Evaluating Perception" brief subsection
11. Add cross-references: Ch.6 §Perception, Q4 (Action), Q5 (Memory), Ch.8 data governance

**Content to Preserve**:
- Tool categories from 03-architecture.tex (lines 60-93)
- MCP Resources explanation (from 04-protocols.tex)
- "MCP eliminates M×N problem" keybox
- Legal examples (Westlaw, case databases)
- Financial examples (Bloomberg terminal, market data)

---

### Section 05: Action (Q4)
**Source**: `03-architecture.tex` (Tools section) + `04-protocols.tex` (MCP Tools/Prompts)
**Action**: ADAPT and MERGE

**Instructions**:
1. Open with Q4 framing: "How does an agent make things happen?"
2. Add organizational analogy: "Just as a professional files documents, sends communications, executes trades..."
3. Include tool categories for WRITE operations: action tools, state-changing operations
4. EMPHASIZE reversibility framework (lines 88-92 from 03-architecture.tex)
5. Include MCP Tools capability (state-changing) and MCP Prompts (reusable templates)
6. Include Tool Security subsection (lines 115-146 from 03-architecture.tex)
7. Add approval workflows: when human confirmation required
8. Add rollback capabilities: what can be undone
9. Add rate limiting and circuit breakers
10. Add "Evaluating Actions" brief subsection
11. Add cross-references: Q3 (Perception), Q8 (Escalation), Ch.8 action governance

**Content to Preserve**:
- Action tool categories (lines 84-88)
- Reversibility framework
- Security principles: least privilege, audit logging
- Human approval patterns
- Legal example: e-filing, document management
- Financial example: trade execution, order routing

---

### Section 06: Memory (Q5)
**Source**: `03-architecture.tex` (Memory section, lines 174-236)
**Action**: ADAPT (preserve almost entirely)

**Instructions**:
1. Open with Q5 framing: "How does an agent remember things?"
2. Add organizational analogy: "Just as a professional maintains case files, accesses firm knowledge base..."
3. RELOCATE Memory definition box from introduction
4. PRESERVE Memory Layers keybox (lines 200-212) - exceptional summary
5. Keep memory architecture: working memory, episodic, RAG, vector stores
6. Keep domain-specific considerations (lines 224-235)
7. EMPHASIZE matter/client isolation for legal contexts
8. EMPHASIZE information barriers for financial contexts
9. Add temporal validity: when memory becomes stale
10. Add "Evaluating Memory" brief subsection
11. Add cross-references: Ch.6 §Adaptation, Q3 (Perception), Ch.8 memory governance

**Content to Preserve**:
- Memory Layers keybox (VERBATIM)
- Working memory, episodic memory, semantic memory typology
- RAG and vector store patterns
- Professional analogies throughout
- Matter isolation requirements

---

### Section 07: Planning (Q6)
**Source**: `03-architecture.tex` (Planning section, lines 240-361)
**Action**: ADAPT (preserve almost entirely)

**Instructions**:
1. Open with Q6 framing: "How does an agent break a big job into steps?"
2. Add organizational analogy: "Just as a professional creates project plans, work breakdown structures..."
3. RELOCATE Planning definition box from introduction
4. Keep planning patterns: ReAct, Plan-Execute, Hierarchical (lines 260-298)
5. PRESERVE pattern selection table
6. Keep budget architecture (lines 345-361)
7. Include ABA Formal Opinion 512 citation (line 358)
8. Add decision framework: which pattern for which task type
9. Add "Evaluating Planning" brief subsection
10. Add cross-references: Ch.6 §Goal, Q2 (Intent), Q7 (Termination), Ch.8 planning governance

**Content to Preserve**:
- Planning patterns table (ReAct, Plan-Execute, Hierarchical)
- Pattern selection guidance
- Budget architecture
- ABA citation on AI oversight
- Professional analogies (partner assigns → decomposition)

---

### Section 08: Termination (Q7)
**Source**: `03-architecture.tex` (Termination section, lines 302-334) + `05-evaluation.tex` (Layer 3)
**Action**: ADAPT and EXPAND

**Instructions**:
1. Open with Q7 framing: "How does an agent know when it's done?"
2. Add organizational analogy: "Just as a professional knows when deliverables meet acceptance criteria..."
3. Keep termination conditions: success criteria, budgets, confidence thresholds, error conditions
4. Keep guardrails and loop detection (lines 321-335)
5. MERGE Layer 3 evaluation content from 05-evaluation.tex
6. Add explicit success criteria patterns
7. Add failure recognition patterns
8. Add graceful degradation patterns
9. Add METR reliability finding: <10% success on 4+ hour tasks (from 03-architecture lines 503+)
10. Add "Evaluating Termination Decisions" subsection
11. Add cross-references: Ch.6 §Termination, Q8 (Escalation), Ch.8 termination governance

**Content to Preserve**:
- Termination condition categories
- Guardrails implementation
- Loop detection
- METR finding (critical reality check)

---

### Section 09: Escalation (Q8)
**Source**: Scattered across `02-triggers-channels.tex`, `03-architecture.tex`
**Action**: CONSOLIDATE and EXPAND

**Instructions**:
1. Open with Q8 framing: "How does an agent know when to ask for help?"
2. Add organizational analogy: "Just as a professional knows when to go to the supervisor..."
3. CONSOLIDATE escalation content from 02-triggers (lines 108-115) and 03-architecture (lines 315, 336-344)
4. Include HITL patterns: approval gates, checkpoint reviews, confidence-based, human-as-tool
5. NEW subsection: When to escalate (decision framework)
6. NEW subsection: How to escalate (information handoff)
7. NEW subsection: Escalation protocols for legal/financial contexts
8. Add confidence calibration patterns
9. Add "authority boundary" recognition
10. Add "Evaluating Escalation Decisions" subsection
11. Add cross-references: Q7 (Termination), Q9 (Delegation), Ch.8 oversight

**Content to Preserve**:
- HITL pattern descriptions
- Confidence threshold guidance
- Professional examples (partner review, compliance sign-off)

**New Content Required**:
- Decision framework: when is escalation required vs. optional?
- Information handoff: what context must be provided?
- Escalation latency considerations

---

### Section 10: Delegation (Q9)
**Source**: `04-protocols.tex` (A2A section) + `03-architecture.tex` (multi-agent)
**Action**: ADAPT and EXPAND

**Instructions**:
1. Open with Q9 framing: "How does an agent work with other agents?"
2. Add organizational analogy: "Just as professionals coordinate with specialists, delegate to associates..."
3. Include A2A protocol content entirely from 04-protocols.tex
4. PRESERVE "A2A Task Delegation" keybox with 5-phase lifecycle
5. Include Agent Cards, Tasks, Artifacts, Channels concepts
6. Include multi-agent orchestration (lines 369-376 from 03-architecture.tex)
7. Include Dual Protocol Strategy: M&A due diligence example
8. PRESERVE protocol selection table (expand with decision guidance)
9. Include multi-agent legal workflow (Securities/Banking/Consumer/AML agents)
10. Include multi-agent financial workflow (Market/Compliance/Risk/Execution agents)
11. Add coordination failure patterns
12. Add "Evaluating Delegation" subsection
13. Add cross-references: Q3/Q4 (MCP), Q8 (Escalation), Ch.8 delegation governance

**Content to Preserve**:
- A2A Task Delegation keybox (VERBATIM)
- Five-phase lifecycle with engagement letter analogy
- Multi-agent workflow examples
- Protocol selection table
- Security: cryptographic signatures, information barriers, conflicts screening

---

### Section 11: Governance Preview (Q10)
**Source**: Scattered + NEW + bridge content
**Action**: CREATE NEW (brief, bridges to Ch.8)

**Instructions**:
1. Open with Q10 framing: "How do we keep the agent safe?"
2. Add organizational analogy: "Just as firms have compliance programs, audit functions, oversight..."
3. Brief overview: this question spans all others (governance is pervasive)
4. Include 10-question governance mapping table
5. Include security from 07-further-learning.tex (5 security essentials keybox)
6. Add transparency and explainability overview (from 03-architecture lines 408-490)
7. Add auditability vs. retention tension
8. EMPHASIZE: Ch.8 provides comprehensive treatment
9. Keep this section brief (3-4 pages) - it's a bridge, not the full treatment
10. Add explicit forward references to Ch.8 sections

**Content to Preserve**:
- Security Controls keybox from 07-further-learning.tex
- Transparency levels (0-3) from 03-architecture.tex
- "Architecture Enables Governance" keybox

---

### Section 12: Synthesis - Reference Architectures
**Source**: `06-case-studies.tex` (entire section)
**Action**: ADAPT with framework annotations

**Instructions**:
1. Keep as synthesis section showing complete deployments
2. Add explicit Q1-Q10 annotations throughout both case studies
3. PRESERVE failure mode analysis (pedagogically crucial)
4. Add organizational analogy mappings for each case study
5. Add "What This Teaches" boxes after failure modes
6. Keep Credit Facility Review case study
7. Keep Equity Portfolio Management case study
8. Keep synthesis principles (six cross-domain principles)
9. Add framework completion matrix table
10. Add forward references from Q1-Q10 sections

**Content to Preserve**:
- Both case studies in full
- ALL failure mode analysis
- Honest framing about "reference architectures not turnkey solutions"
- <10% success acknowledgment
- Synthesis principles and deployment checklist

---

### Section 13: Essential Resources
**Source**: `07-further-learning.tex`
**Action**: ADAPT with reordering

**Instructions**:
1. REORDER subsections: Security → Protocols → Research → Learning Paths → Staying Current
2. EXPAND Security Essentials with 10-question mapping
3. Add timestamps to protocol assessments ("as of November 2025")
4. EXPAND benchmark descriptions (one-line each for LegalBench, FinQA, VLAIR)
5. STRENGTHEN learning paths with progression and timeframes
6. Add specific cross-references to Q4 (MCP), Q9 (A2A), Q10 (Governance)
7. Keep audience-specific recommendations (legal, financial, technical, everyone)
8. Keep "Staying Current" disclaimer

**Content to Preserve**:
- Security Controls keybox
- Audience-specific learning paths with validation questions
- Protocol guidance (MCP production-ready, A2A maturing)
- Research citations (Xi et al., Yao et al., Park et al.)
- Benchmarks (LegalBench, FinQA, VLAIR)

---

### Section 14: Conclusion
**Source**: `08-conclusion.tex`
**Action**: MAJOR REWRITE around 10 questions

**Instructions**:
1. Rewrite opening to reference all 10 questions explicitly
2. RESTRUCTURE "What You Now Understand" around 10 questions (not 5 components)
3. Use pattern: "You understand that agents need X. Without X, agents cannot Y."
4. ENHANCE "What This Lets You Do" with question-specific vendor evaluation
5. KEEP honest limitations section (current capabilities reality check)
6. EXPAND governance bridge with explicit 10-question → governance mapping
7. PRESERVE and enhance "You cannot govern what you do not understand" keybox
8. Add explicit forward references to Ch.8 sections
9. Keep practitioner-friendly tone throughout

**Content to Preserve**:
- "AI agents are organized like professional teams" opening
- "What This Lets You Do" practical outcomes
- Governance bridge structure
- Honest limitations acknowledgment
- Keybox on architecture enabling governance

**Structure**:
```
14.1 Opening: Agents as Professional Teams (revised for 10 questions)
14.2 What You Now Understand (10 questions, not 5 components)
14.3 What This Lets You Do (with question-specific guidance)
14.4 Current Limitations (unchanged)
14.5 From Architecture to Governance (expanded 10-question mapping)
```

---

## Content Migration Summary

### PRESERVE VERBATIM (High-Value Keyboxes)
1. "Speed vs. Reasoning" highlightbox (02-triggers)
2. Memory Layers keybox (03-architecture)
3. Planning Patterns table (03-architecture)
4. "MCP Core Concept" M×N keybox (04-protocols)
5. "Protocols as Exemplars, Not Permanence" box (04-protocols)
6. "A2A Task Delegation" 5-phase keybox (04-protocols)
7. Security Controls keybox (07-further-learning)
8. "Architecture Enables Governance" keybox (08-conclusion)
9. All failure mode analysis (06-case-studies)

### RELOCATE
- Definition boxes (Tool, Memory, Planning) → respective Q sections
- Event-driven content → Q1 (Triggers)
- MCP Resources → Q3 (Perception)
- MCP Tools/Prompts → Q4 (Action)
- A2A content → Q9 (Delegation)
- Escalation fragments → Q8 (Escalation)
- HITL patterns → Q8 (Escalation)

### CREATE NEW
- Q2 (Intent) section - largely new content
- Q10 (Governance) section - synthesis of scattered content
- 10-question framework table and mapping
- Organizational analogy mappings throughout
- "What This Teaches" boxes in case studies
- Explicit cross-references throughout

### REMOVE OR REDUCE
- Redundant protocol architecture descriptions (explain once, reference thereafter)
- Adoption statistics that will age poorly
- Defensive vendor commentary
- Detailed reference architecture recaps in conclusion (covered earlier)

---

## Cross-Chapter Alignment

### Backward References to Chapter 6
Each Q section should include:
- Explicit mapping to GPA+IAT property
- "In Chapter 6, we defined X. Here we show how to implement it."

### Forward References to Chapter 8
Each Q section should include:
- Brief governance implications
- "Chapter 8 provides comprehensive X governance controls."

### Alignment Table for Reference
| Ch.7 Section | Ch.6 Property | Ch.8 Control Domain |
|--------------|---------------|---------------------|
| Q1 Triggers | Entry to GPA loop | Event authorization, audit |
| Q2 Intent | Goal | Purpose limitation, alignment |
| Q3 Perception | Perception | Data governance, access control |
| Q4 Action | Action | Actuation controls, approval |
| Q5 Memory | Adaptation | State integrity, retention |
| Q6 Planning | Goal + Iteration | Bounded operation, budgets |
| Q7 Termination | Termination | Exit protocols, criteria |
| Q8 Escalation | Termination | Human oversight, triggers |
| Q9 Delegation | Multi-agent | Agent identity, contracts |
| Q10 Governance | All | Five-layer stack |

---

## Quality Checklist

### Before Each Section
- [ ] Opens with fundamental question
- [ ] Includes organizational analogy
- [ ] Maps to Ch.6 GPA+IAT property
- [ ] Previews Ch.8 governance implications

### After Each Section
- [ ] Contains legal AND financial examples
- [ ] Includes practical evaluation guidance
- [ ] Cross-references related Q sections
- [ ] Voice consistent ("we" for analysis, "you" for guidance)

### Chapter-Wide
- [ ] All labels migrated from `sec:agents2-*` to new scheme
- [ ] All figures referenced correctly
- [ ] All citations preserved (especially METR, ABA, VLAIR)
- [ ] No content duplication between sections
- [ ] Keyboxes preserved in appropriate locations
- [ ] 10-question framework consistent throughout

---

## Estimated Effort

| Section | Action | Effort | Priority |
|---------|--------|--------|----------|
| 00-how-to-read | EXPAND | 1 hour | HIGH |
| 01-introduction | REWRITE | 3 hours | HIGH |
| 02-triggers | ADAPT | 2 hours | HIGH |
| 03-intent | CREATE | 4 hours | HIGH |
| 04-perception | MERGE | 3 hours | HIGH |
| 05-action | MERGE | 3 hours | HIGH |
| 06-memory | ADAPT | 2 hours | MEDIUM |
| 07-planning | ADAPT | 2 hours | MEDIUM |
| 08-termination | EXPAND | 3 hours | MEDIUM |
| 09-escalation | CREATE | 4 hours | MEDIUM |
| 10-delegation | ADAPT | 3 hours | MEDIUM |
| 11-governance | CREATE | 2 hours | HIGH |
| 12-synthesis | ADAPT | 3 hours | MEDIUM |
| 13-resources | ADAPT | 1 hour | LOW |
| 14-conclusion | REWRITE | 3 hours | HIGH |

**Total Estimated Effort**: 39 hours

---

## Success Criteria

The rewrite succeeds if:

1. **Framework Clarity**: Reader understands 10 questions as organizing principle within first 5 pages
2. **Continuity**: Clear bridge from Ch.6 (theory) through Ch.7 (build) to Ch.8 (govern)
3. **Practical Value**: Legal/financial professionals can evaluate vendors using 10-question checklist
4. **Honest**: Current limitations and failure modes prominently acknowledged
5. **Complete**: All high-value content from original preserved or improved
6. **Navigable**: Cross-references enable both sequential and random-access reading

---

## Open Questions for Author

1. **Intent Section (Q2)**: How much detail on NLP/prompt parsing vs. keeping it conceptual?
2. **Governance Preview (Q10)**: How much to include vs. deferring entirely to Ch.8?
3. **Case Studies**: Keep both, or condense to one with the other as appendix?
4. **Evaluation Content**: Hybrid approach (per-section + comprehensive) or just comprehensive?
5. **Length Target**: Current chapter is ~60 pages; target for rewrite?

---

*Last Updated: December 2024*
*Status: Ready for Author Review*
