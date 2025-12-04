# Diagram Specifications for Chapter 07

This document specifies the TikZ diagrams needed for Part II. Reference Chapter 06's figures/ for style consistency.

## Priority 1: Reference Architecture Diagram

**Location**: Section 03 (Architecture), after line 33
**Purpose**: Show Three Pillars surrounding LLM core
**Style**: Concentric or hub-spoke layout (see `06-agents-part-1/figures/hierarchy-diagram.tex`)

**Elements**:
- Center: LLM Core (reasoning engine)
- Pillar 1: Tools (left) - labeled with "Perception" and "Action"
- Pillar 2: Memory (right) - labeled with "Adaptation"
- Pillar 3: Planning (top) - labeled with "Goal", "Iteration", "Termination"
- External: Environment/World boundary

**Colors**: Use semantic palette (definition-dark for LLM, example-base for Tools, key-base for Memory, practice-base for Planning)

---

## Priority 2: MCP Architecture Diagram

**Location**: Section 04 (Protocols), after line 76
**Purpose**: Show MCP client-host-server relationships

**Elements**:
- Host (IDE, Claude Desktop, etc.)
- Client (LLM/Agent within host)
- Server (MCP Server with tools/resources)
- Arrows: JSON-RPC messages, two transport paths (stdio, HTTP)

**Layout**: Horizontal flow, left-to-right

---

## Priority 3: Three-Layer Evaluation Framework

**Location**: Section 05 (Evaluation), after line 41
**Purpose**: Show layers mapped to GPA+IAT properties

**Elements**:
- Layer 1: Retrieval/Perception (bottom) - maps to P
- Layer 2: Reasoning/Adaptation (middle) - maps to A
- Layer 3: Workflows/Termination (top) - maps to G, I, T
- Vertical progression with labels

**Style**: Stacked rectangles with arrows upward (increasing complexity)

---

## Priority 4: Dual-Protocol Architecture Diagram

**Location**: Section 04 (Protocols), after line 395
**Purpose**: Show orchestrator using A2A with specialists using MCP

**Elements**:
- Center: Orchestrator Agent
- Surrounding: Specialist Agents (Research, Document, Finance)
- Below each specialist: MCP servers (Westlaw, iManage, Bloomberg)
- A2A connections between orchestrator and specialists
- MCP connections between specialists and servers

**Layout**: Hub-spoke with two layers

---

## Priority 5: Matter-Isolated Memory Architecture

**Location**: Section 03 (Architecture), after line 267
**Purpose**: Show privilege boundaries in legal AI memory

**Elements**:
- Multiple matter containers (Client A Matter 1, Client A Matter 2, Client B)
- Vector store namespaces within each
- Access control layer
- Ethical wall indicators between conflicted matters

**Style**: Partitioned boxes with clear boundaries

---

## Priority 6: Human-in-the-Loop Decision Flowchart

**Location**: Section 03 (Architecture), after line 416
**Purpose**: Show when to route to human approval

**Elements**:
- Diamond: Is action reversible?
- Diamond: Confidence threshold met?
- Diamond: High-risk domain?
- Boxes: Execute autonomously, Request approval, Escalate to human
- Arrows showing flow

**Style**: Standard flowchart with decision diamonds

---

## Implementation Notes

1. All diagrams should use the chapter's semantic color palette (see `main.tex` lines 45-120)
2. Follow Chapter 06 TikZ style for consistency
3. Use `\small` or `\footnotesize` for labels
4. Include `blur shadow` for depth (see hierarchy-diagram.tex)
5. Export standalone if needed using `standalone` document class

## Reference Files

- `/chapters/06-agents-part-1/figures/timeline.tex` - horizontal timeline style
- `/chapters/06-agents-part-1/figures/hierarchy-diagram.tex` - concentric circles style
