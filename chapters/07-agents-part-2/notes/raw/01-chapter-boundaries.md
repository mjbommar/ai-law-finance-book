# Chapter Boundaries: What to Define vs. Reference

**Generated**: November 27, 2025
**Purpose**: Clarify what Chapter 07 (Part II) should define itself vs. reference from other chapters

---

## Chapter Inventory

### Chapter 01: Foundations - LLM Primer and Mechanics
**Directory**: `chapters/01-foundations-llm-primer-mechanics/`
**Scope**: Conceptual primer covering tokens, tokenizers, context windows, embedding representations, and completion sampling. Provides foundational knowledge on how modern LLMs work mechanically.

**Relevance to Part II**: Context window budgeting affects agent memory design. Token limits constrain agent planning horizons.

---

### Chapter 02: Foundations - Conversations and Reasoning
**Directory**: `chapters/02-foundations-conversations-reasoning/`
**Scope**: Multi-turn chat mechanics and reasoning patterns. Covers conversational roles (system/user/assistant), memory/state management strategies, context budgeting, and reasoning patterns (chain-of-thought, self-consistency).

**Relevance to Part II**: Foundation for agent conversational state layer. Part II extends this with agent-specific memory patterns.

---

### Chapter 03: Foundations - Structured Outputs and Tool Use
**Directory**: `chapters/03-foundations-structured-tools-multimodal/`
**Scope**: Reliable structured outputs, function calling, and governance metadata. Key sections:
- `sec:llmC-rag` — RAG 101 (chunking, embeddings, indexing, freshness)
- `sec:llmC-evidence` — Evidence record schema (claim/source binding)
- `sec:llmC-tools` — Tool use with invocation contracts, governance metadata

**Relevance to Part II**: Critical foundation. Part II builds on these but does NOT redefine them.

---

### Chapter 04: Foundations - Multimodal Fundamentals
**Directory**: `chapters/04-foundations-multimodal/`
**Scope**: Practical multimodal workflows for legal and finance including document structure preservation, table/chart extraction, audio transcription, and privacy/redaction patterns.

**Relevance to Part II**: Reference when agents ingest documents (contracts, filings, etc.).

---

### Chapter 05: Foundations - Prompt Design, Evaluation, and Optimization
**Directory**: `chapters/05-foundations-prompt-design-eval-optimization/`
**Scope**: Specifications, tests, meta-prompting, and change management. Key sections:
- `sec:llmE-strategy` — Strategy catalog (CoT, ReAct, Tree-of-Thought)
- `sec:llmD-eval` — Evaluation frameworks with test sets
- `sec:llmD-eval-retrieval-quick` — Retrieval sanity checks

**Relevance to Part II**: Part II extends evaluation for multi-turn agent workflows.

---

### Chapter 06: Agents - Part I: What is an Agent?
**Directory**: `chapters/06-agents-part-1/`
**Scope**: Conceptual primer and operational definitions:
- Level 1: Minimal agency (GPA—goals, perception, action)
- Level 2: Agentic systems (GPA+IAT—iteration, adaptation, termination)
- Level 3: AI-powered vs. traditional implementations
- 6-question evaluation rubric
- Analytical dimensions (autonomy, entity frames, goal dynamics, persistence)

**Relevance to Part II**: THE conceptual foundation. Part II implements what Part I defines.

---

### Chapter 08: Agents - Part III: How to Govern an Agent
**Directory**: `chapters/08-agents-part-3/`
**Scope**: Regulation, controls, conformance, and deployment. Covers governance imperative, five-layer governance stack, implementation patterns, accountability structures.

**Relevance to Part II**: Part II validates "does it work?"; Part III validates "is it safe to deploy?"

---

### Chapters 09-10: Knowledge Graphs
**Directories**: `chapters/09-kg-foundations/`, `chapters/10-kg-operations-llm/`
**Scope**: Semantic Web foundations (RDF, OWL, SPARQL) and operational pipelines with LLM assistance.

**Relevance to Part II**: Applicable to agent memory and retrieval systems using structured knowledge.

---

## What Part II Should DEFINE

These are novel contributions that Part II should establish:

### 1. Agent Reference Architecture

**Content**: Three-pillar structure mapping to GPA+IAT
- **Tools pillar** → implements Action property
- **Memory pillar** → implements Iteration and Persistence
- **Planning pillar** → implements Goal, Adaptation, Termination

**Rationale**: No other chapter provides this integrated view.

### 2. Agent-Level Tool Orchestration

**Content**:
- Multi-tool sequencing and parallel execution patterns
- Tool discovery and capability registration (beyond single tool contracts)
- Agent-to-agent tool invocation

**Rationale**: Chapter 03 covers individual tool design; Part II covers orchestration.

### 3. Agent Memory Architecture

**Content**:
- How to layer conversational state (Ch. 02) + retrieval-backed memory (Ch. 03 RAG) + case/project memory
- Privilege boundaries and authorization filters at memory query time
- Provenance and content-addressed storage

**Rationale**: Chapter 02 covers conversation state; Part II covers agent-scale memory.

### 4. Planning and Reasoning at Agent Scale

**Content**:
- Agent-specific reasoning patterns (ReAct for tool workflows, planning-then-acting, graph exploration)
- How to instrument deliberation traces separately from user output
- Escalation triggers for low confidence

**Rationale**: Chapter 05 covers single-turn patterns; Part II covers multi-turn agent loops.

### 5. Agent Protocols

**Content**:
- Capability discovery and contracts (extends Chapter 03 to agent-to-agent)
- Invocation semantics with governance metadata
- Error handling and escalation policies
- MCP and A2A protocol analysis

**Rationale**: Protocol-level interoperability is novel to Part II.

### 6. Agent-Level Evaluation

**Content**:
- 3-layer evaluation: retrieval (quick gates), reasoning (legal analysis), workflows (end-to-end)
- End-to-end task completion metrics
- Robustness to tool failures and rate limits
- Escalation trigger validation

**Rationale**: Chapter 05 covers single-turn evaluation; Part II covers workflow evaluation.

### 7. Industry Deployment Patterns

**Content**:
- Common topologies (single-agent, orchestrated multi-agent, hub-and-spoke)
- Integration touchpoints: DMS, research platforms, practice management, workflow orchestration
- Trade-offs and anti-patterns

**Rationale**: No other chapter covers deployment architectures.

---

## What Part II Should REFERENCE

These topics are owned by other chapters. Part II should reference, not redefine:

### From Chapter 02 (Conversations)

| Topic | Label | How Part II Uses It |
|-------|-------|---------------------|
| Conversational roles | — | Foundation for agent conversational state |
| Context budgeting | — | Constraints on agent memory design |
| Memory strategies | — | Building block for agent memory layer |

### From Chapter 03 (Structured Outputs & Tools)

| Topic | Label | How Part II Uses It |
|-------|-------|---------------------|
| RAG mechanics | `sec:llmC-rag` | Agent retrieval layer uses RAG |
| Evidence records | `sec:llmC-evidence` | Agents must produce evidence records |
| Tool contracts | `sec:llmC-tools` | Agent tools follow these contracts |
| Governance metadata | `sec:llmC-tools` | Agents attach metadata per this spec |

**Existing references in Part II**:
- `sec:agents2-memory` references `sec:llmC-rag` and `sec:llmC-evidence`
- `sec:agents2-eval-retrieval` references `sec:llmC-evidence`

**Needed references**:
- `sec:agents2-tools` should reference `sec:llmC-tools`
- `sec:agents2-proto-governance` should reference `sec:llmC-tools`

### From Chapter 05 (Prompt Design & Evaluation)

| Topic | Label | How Part II Uses It |
|-------|-------|---------------------|
| Reasoning patterns | `sec:llmE-strategy` | Agent planning uses these patterns |
| Evaluation methodology | `sec:llmD-eval` | Agent evaluation extends this |
| Retrieval sanity checks | `sec:llmD-eval-retrieval-quick` | Layer 1 evaluation uses these |

**Existing references in Part II**:
- `sec:agents2-eval-retrieval` references `sec:llmD-eval-retrieval-quick`

**Needed references**:
- `sec:agents2-planning` should reference `sec:llmE-strategy`
- `sec:agents2-eval-reasoning` should reference `sec:llmD-eval`

### From Chapter 06 (Part I: What is an Agent?)

| Topic | Label | How Part II Uses It |
|-------|-------|---------------------|
| GPA definition | `sec:intro` | Part II implements these properties |
| GPA+IAT definition | `sec:intro` | Part II implements these properties |
| 6-question rubric | `sec:rubric-6q` | Validates agent implementations |
| Autonomy spectrum | `sec:dimensions` | Maps to planning pattern selection |
| Entity frames | `sec:dimensions` | Informs deployment topology |
| Professional deployment | `sec:synthesis` | Governance handoff |
| Misconceptions | `sec:practical` | Tool use ≠ agency clarification |

**Existing references in Part II**:
- Introduction mentions Part I generally

**Needed references**:
- Explicit `\Cref{sec:intro}` for GPA+IAT definitions
- `\Cref{sec:rubric-6q}` in evaluation section
- `\Cref{sec:dimensions}` in planning and industry sections
- `\Cref{sec:synthesis}` in synthesis section

---

## Overlap Analysis by Topic

### Topic: Memory and State Management

**Chapter 02 responsibility**: Conversational mechanics, roles, state budgeting
**Chapter 03 responsibility**: RAG, retrieval, evidence records
**Part II responsibility**: Agent-level memory architecture combining all layers

**Boundary**: Part II does NOT redefine RAG or conversation state. It shows how to combine them into an agent memory system.

### Topic: Tool Use and Function Calling

**Chapter 03 responsibility**: Individual tool design, contracts, governance metadata
**Part II responsibility**: Multi-tool orchestration, discovery, agent-to-agent invocation

**Boundary**: Part II does NOT redefine tool contracts. It shows how agents orchestrate multiple tools.

### Topic: Reasoning Patterns

**Chapter 05 responsibility**: Pattern catalog (CoT, ReAct, ToT), single-turn selection
**Part II responsibility**: Agent-scale reasoning loops, planning pattern selection based on autonomy

**Boundary**: Part II references Chapter 05's catalog; adds agent-specific guidance on when to use each.

### Topic: Evaluation

**Chapter 05 responsibility**: Test suite methodology, metrics, citation fidelity
**Part II responsibility**: Multi-turn workflow evaluation, tool failure robustness

**Boundary**: Part II extends Chapter 05 to agent workflows; does NOT redefine evaluation basics.

### Topic: Agent Definitions

**Chapter 06 responsibility**: What is an agent? GPA, IAT, levels, taxonomy
**Part II responsibility**: How to build agents that satisfy these definitions

**Boundary**: Part II NEVER redefines agents. It implements what Part I defines.

---

## Recommended Cross-Reference Additions

### In `sec:agents2-intro` (Introduction)

```latex
% Add after "Relationship to Other Parts" paragraph
Recall from Part I (\Cref{sec:intro}) that agentic systems require six properties:
Goal (G), Perception (P), Action (A), Iteration (I), Adaptation (A), and Termination (T).
Part II shows how to implement these properties in practice.
```

### In `sec:agents2-tools` (Tools Section)

```latex
% Add reference to Chapter 03
Design tools following the contract and governance metadata patterns established in
\Cref{sec:llmC-tools}. Each tool schema should capture functionality, data classification,
and audit requirements.
```

### In `sec:agents2-planning` (Planning Section)

```latex
% Add reference to Chapter 05
Select reasoning patterns from the strategy catalog in \Cref{sec:llmE-strategy} based on
task risk and agent autonomy level (see \Cref{sec:dimensions}).
```

### In `sec:agents2-eval` (Evaluation Section)

```latex
% Add reference to Chapter 05
This section extends the evaluation methodology from \Cref{sec:llmD-eval} to multi-turn
agent workflows. Before Layer 1 evaluation, ensure retrieval sanity checks from
\Cref{sec:llmD-eval-retrieval-quick} pass.
```

### In `sec:agents2-synthesis` (Synthesis Section)

```latex
% Add reference to Chapter 06
The synthesis is grounded in Part I's professional deployment framework (\Cref{sec:synthesis}),
which identifies attribution, auditable reasoning, bounded operation, escalation pathways,
confidentiality controls, and accountability mapping as essential safeguards.
```
