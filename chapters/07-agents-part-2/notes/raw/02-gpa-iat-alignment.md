# GPA+IAT Framework Alignment

**Generated**: November 27, 2025
**Purpose**: Extract the conceptual framework from Part I and identify alignment gaps in Part II

---

## Part I Framework Summary

### Agent Definition (Level 1: Minimal Agency)

From `chapters/06-agents-part-1/sections/01-introduction.tex`:

> "An **agent** is any entity that pursues goals through perception and action, with at least minimal discretion over which action to take in response to what it perceives."

**Minimal properties (GPA)**:
- **G**oal — Clear objective or performance criterion
- **P**erception — Awareness of environment through sensing
- **A**ction — Capability to affect environment

---

### Agentic System Definition (Level 2: Operational)

From `chapters/06-agents-part-1/sections/01-introduction.tex`:

> "An **agentic system** is a goal-directed agent that repeatedly perceives and acts in its environment, adapting from observations until clear termination conditions are met (explicit or implicit)."

**Additional properties beyond Level 1 (IAT)**:
- **I**teration — Repeat perceive-act cycles, not single-shot
- **A**daptation — Adjust strategy based on feedback/results
- **T**ermination — Clear stopping conditions (explicit or implicit)

**Total: 6 operational properties (GPA + IAT)**

---

### Three-Level Hierarchy

| Level | Name | Properties | Implementation |
|-------|------|------------|----------------|
| 1 | Minimal Agency | G + P + A (3) | Conceptual baseline |
| 2 | Traditional Agentic Software | G + P + A + I + A + T (6) | Rules, algorithms, deterministic logic |
| 3 | AI-Powered Agentic Systems | G + P + A + I + A + T (6) | LLMs, neural networks + traditional components |

**Key insight**: Levels 2 and 3 share identical property requirements; they differ in implementation approach.

---

### Six-Question Evaluation Rubric

From `chapters/06-agents-part-1/sections/02-recognize-agent.tex` (`sec:rubric-6q`):

| Question | Property | Test | Falsification |
|----------|----------|------|---------------|
| Q1. Does it have goals? | G | Look for clear objectives, task specifications | Responds identically regardless of desired outcomes |
| Q2. Does it perceive? | P | Check for environmental awareness (sensors, APIs, databases) | Operates identically regardless of environmental state |
| Q3. Does it act? | A | Verify capability to affect environment with ≥2 possible actions | Cannot modify environment or executes exactly one fixed sequence |
| Q4. Does it iterate? | I | Confirm multiple perceive-act cycles with state preservation | Processes input once without maintaining state |
| Q5. Does it adapt? | A | Check whether strategy modifies based on observations | Applies identical logic regardless of outcomes |
| Q6. Does it stop? | T | Verify clear stopping conditions | No mechanism for recognizing when to stop |

**Interpretation**:
- Q1-Q3 yes = qualifies as an **agent**
- All six yes = qualifies as an **agentic system**

---

### Termination Property (Special Emphasis)

From `chapters/06-agents-part-1/sections/06-analytical-framework.tex`:

**Two modes of termination**:

1. **Explicit Termination**:
   - Resource budgets (computation time, API calls, token limits)
   - Timeout constraints (wall clock time, iteration counts)
   - Escalation triggers (confidence thresholds, error conditions)

2. **Implicit Termination**:
   - Goal satisfaction (target state achieved)
   - Quiescent states (no further actions available)
   - Bounded episodes (fixed-duration tasks)

**Professional deployments combine both modes.**

---

### Autonomy Spectrum

From `chapters/06-agents-part-1/sections/05-analytical-dimensions.tex` (`sec:dimensions`):

| Level | Name | Description |
|-------|------|-------------|
| Low | Delegated proxies | Follow instructions; principal retains liability |
| Low-Moderate | Contract-bound delegates | Choose tactics within contracts |
| Moderate | Self-regulating actors | Set sub-goals, monitor, self-adjust |
| Moderate-High | Perception-action planners | Sense and select actions via performance-driven policies |
| High | Learning loop owners | Experiment with actions, update from rewards |
| Very High | Tool orchestrators | Choose when/how to invoke tools, independent task completion |

**Governance principle**: Oversight rigor must scale with autonomy level.

---

### Key Misconceptions (What Does NOT Count)

From `chapters/06-agents-part-1/sections/02-recognize-agent.tex`:

1. **Single-shot responses are NOT agentic systems** — lack iteration and adaptation
2. **Automation alone is NOT an agentic system** — lack perception, adaptation, iteration
3. **Tool use alone is NOT agency** — requires iterative tool use with adaptation
4. **Complexity is NOT agency** — sophisticated transformation doesn't equal goal-directedness
5. **AI-powered is NOT agency** — neural networks without iteration/adaptation aren't agentic

---

## Part II Current State

### Section Structure

| Section | File | Current Content |
|---------|------|-----------------|
| Architecture | `architecture.tex` | Three pillars: tools, memory, planning |
| Protocols | `protocols.tex` | Capability discovery, governance metadata, errors |
| Industry | `industry_technical.tex` | Topologies, integrations |
| Evaluation | `evaluation_technical.tex` | Three layers: retrieval, reasoning, workflows |
| Synthesis | `synthesis.tex` | Minimal viable blueprint, governance handoff |

### Current References to Part I

- Introduction mentions Part I provides "definitions and foundations"
- No explicit `\Cref{}` references to Part I labels
- No mapping of architecture to GPA+IAT properties

---

## Alignment Gap Analysis

### Architecture Section (`sec:agents2-architecture`)

**Current state**: Mentions "tools," "memory," "planning" but doesn't reference Part I's conceptual framework.

**Gap**: No explicit mapping to GPA+IAT properties.

**Recommended fix**: Add subsection showing how 3 pillars implement the 6 properties.

```latex
\subsection{Mapping Architecture to GPA+IAT}
\label{sec:agents2-gpaiat-mapping}

Recall from Part I (\Cref{sec:intro}) that agentic systems require six properties:
Goal (G), Perception (P), Action (A), Iteration (I), Adaptation (A), and Termination (T).
Our reference architecture operationalizes these:

\begin{itemize}
  \item \textbf{Tools \& function calling} implement the \textbf{Action property}:
    they define what agents can do in their environment.
  \item \textbf{Memory and state management} implement the \textbf{Iteration and Persistence}
    requirements: they preserve state across perception-action cycles.
  \item \textbf{Planning, reasoning, and control} implement \textbf{Goal, Adaptation, and Termination}:
    they decompose goals into actionable steps, adjust strategy based on tool results,
    and enforce stopping conditions.
\end{itemize}
```

---

### Tools Section (`sec:agents2-tools`)

**Current state**: "Design tools with schemas that capture both functionality and governance metadata."

**Gap**: Doesn't address Part I's "tool use ≠ agency" misconception.

**Recommended fix**: Add clarification box.

```latex
\begin{cautionbox}[title={Tool Use is Not Agency}]
From Part I (\Cref{sec:practical}): calling external tools does not automatically
make an entity agentic. The critical question is whether the entity \emph{iterates on tool
results}, \emph{adapts} its strategy based on what it observes, and has clear \textbf{termination}
conditions.

For tool-use patterns to support agentic behavior, the agent must:
\begin{enumerate}
  \item \textbf{Perceive} the tool's output (not just invoke it)
  \item \textbf{Evaluate} whether results advance toward the goal
  \item \textbf{Decide} which tool to invoke next based on observations
  \item \textbf{Know when to stop} using tools (termination)
\end{enumerate}
\end{cautionbox}
```

---

### Memory Section (`sec:agents2-memory`)

**Current state**: "Combine short-term conversational state with persistent case/project memory."

**Gap**: Doesn't explain how memory enables the Iteration property.

**Recommended fix**: Clarify relationship to Iteration.

```latex
\textbf{The Iteration Property and State Preservation.} From Part I (\Cref{sec:intro}),
the Iteration property requires ``multiple perceive-act cycles with state preservation
across rounds.'' Memory systems are the primary mechanism for state preservation.
An agent without persistent memory cannot remember what it has already perceived or tried,
preventing true iteration.

\textit{Example:} A legal research agent might iterate as follows:
\begin{enumerate}
  \item First cycle: Query case law (perception) $\rightarrow$ receive results $\rightarrow$ record findings in memory
  \item Second cycle: Perceive findings from memory $\rightarrow$ refine search terms based on gaps $\rightarrow$ query again (action)
  \item Third cycle: Compare new results to prior findings $\rightarrow$ escalate to human if contradictions found (adaptation)
\end{enumerate}

Without persistent memory between cycles, the agent cannot distinguish ``I searched for this already''
from ``I have not searched for this.''
```

---

### Planning Section (`sec:agents2-planning`)

**Current state**: "Adopt planning patterns (react, plan-act-observe, graph/workflow) appropriate to task risk."

**Gap**: Not mapped to Part I's autonomy spectrum.

**Recommended fix**: Add autonomy mapping table.

```latex
Planning patterns should be chosen based on both \textbf{task risk} and \textbf{agent autonomy level}
from Part I's analytical dimensions (\Cref{sec:dimensions}):

\begin{table}[h]
\centering
\small
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Pattern} & \textbf{Autonomy Level} & \textbf{When to Use} \\
\midrule
Reactive (if-then rules) & Delegated proxy & Rule-based compliance; tight control required \\
Plan-act-observe & Contract-bound delegate & Predefined workflows with tactical discretion \\
ReAct (reasoning loops) & Perception-action planner & Tool-based research; interpret goals within scope \\
Goal negotiation & Tool orchestrator & Multi-agent scenarios; complex task decomposition \\
\bottomrule
\end{tabular}
\caption{Planning patterns mapped to autonomy levels from Part I.}
\label{tab:patterns-autonomy}
\end{table}

\textbf{Governance Implication} (from Part I): Oversight rigor must scale with autonomy.
High-autonomy planning (tool orchestrators) requires explicit termination mechanisms,
human-in-the-loop checkpoints, and robust audit trails.
```

---

### Protocols Section (`sec:agents2-protocols`)

**Current state**: "Advertise actions with names, schemas, pre/postconditions, data classifications, and audit requirements."

**Gap**: Capability discovery not framed as agent Perception.

**Recommended fix**: Reframe discovery as perceiving available actions.

```latex
\textbf{Capability Discovery as Agent Perception.} From Part I (\Cref{sec:intro}),
the Perception property requires ``awareness of environment through sensing capabilities.''
In a software agent context, the environment includes not just data (case law, regulatory filings)
but also the set of available actions (tools, APIs, services).
Capability discovery is the mechanism by which agents \emph{perceive} what actions are available.

An agent that does not know what tools exist or what they can do is perceptually blind to part
of its environment. For adaptive behavior, the agent must:
\begin{itemize}
  \item Discover available tools and their capabilities (capability discovery)
  \item Understand pre/postconditions and data requirements (constraints on action)
  \item Recognize which tool is appropriate for the current goal (tool selection)
  \item Observe the results and adapt next steps accordingly (perception-action coupling)
\end{itemize}
```

---

### Evaluation Section (`sec:agents2-eval`)

**Current state**: Three layers (retrieval, reasoning, workflow) without explicit connection to Part I's framework.

**Gap**: Layers not explicitly tied to GPA+IAT properties.

**Recommended fix**: Add opening mapping layers to properties.

```latex
\section{Technical Evaluation: Retrieval, Reasoning, and Workflows}
\label{sec:agents2-eval}

This section defines evaluation layers for technical correctness prior to governance gates in Part III.
Each layer validates one or more of Part I's six essential properties (\Cref{sec:intro}):

\begin{itemize}
  \item \textbf{Layer 1 (Retrieval)} validates the \textbf{Perception property}: Can the agent
    access and assess its environment (legal corpora, regulatory databases)?
  \item \textbf{Layer 2 (Reasoning)} validates the \textbf{Adaptation property}: Can the agent
    adjust its analysis based on evidence and context?
  \item \textbf{Layer 3 (Workflows)} validates \textbf{Iteration and Termination}: Does the agent
    complete multiple perceive-act cycles? Does it recognize when to stop or escalate?
\end{itemize}

Failures in these technical layers indicate the system lacks foundational agentic properties
and should not advance to governance evaluation in Part III.
```

---

### Industry Section (`sec:agents2-industry`)

**Current state**: "Single-agent with tools; orchestrated multi-agent with shared memory; hub-and-spoke integrations."

**Gap**: Topologies not mapped to autonomy spectrum or entity frames.

**Recommended fix**: Connect patterns to Part I analytical dimensions.

```latex
\textbf{Topologies and Autonomy.} Deployment topologies from Part I's autonomy spectrum
(\Cref{sec:dimensions}) inform architecture choices:

\begin{itemize}
  \item \textbf{Single-agent with tools}: Appropriate for perception-action planners
    operating within defined scope. Single point of accountability.
  \item \textbf{Orchestrated multi-agent}: Enables tool orchestrator level autonomy.
    Requires clear delegation contracts and escalation paths between agents.
  \item \textbf{Hub-and-spoke}: Centralizes control in orchestrator (lower autonomy)
    while delegating specific tasks to specialized agents.
\end{itemize}

From Part I's entity frames, consider whether agents should be framed as:
\begin{itemize}
  \item \textbf{Machine-centered}: Agents as autonomous computational entities
  \item \textbf{Human-centered}: Agents as extensions of human professionals
  \item \textbf{Institutional/Hybrid}: Agents embedded in organizational authority structures
\end{itemize}
```

---

### Synthesis Section (`sec:agents2-synthesis`)

**Current state**: "Instrument audit and provenance at design time; do not bolt on later."

**Gap**: Doesn't explicitly connect to Part I's professional deployment safeguards.

**Recommended fix**: Reference Part I's six safeguards.

```latex
The synthesis is grounded in Part I's professional deployment framework (\Cref{sec:synthesis}),
which identifies six essential safeguards:

\begin{enumerate}
  \item \textbf{Attribution and Provenance} — Every factual claim traceable to its source
  \item \textbf{Auditable Reasoning} — Log reasoning steps, tool invocations, decision points
  \item \textbf{Bounded Operation} — Explicit computational budgets and time constraints
  \item \textbf{Escalation Pathways} — Clear triggers for human review and override
  \item \textbf{Confidentiality Controls} — Enforce privilege, role-based access, redaction
  \item \textbf{Accountability Mapping} — Clear lines of responsibility when failures occur
\end{enumerate}

Part II's architecture, protocols, and evaluation practices enable each safeguard:

\begin{keybox}[title={From Build to Govern}]
\begin{itemize}
  \item \textbf{Attribution}: Retrieval evaluation ensures evidence records (\Cref{sec:llmC-evidence})
  \item \textbf{Auditable Reasoning}: Planning patterns produce decision traces
  \item \textbf{Bounded Operation}: Termination mechanisms enforce resource budgets
  \item \textbf{Escalation}: Protocol-level governance metadata and error handlers
  \item \textbf{Confidentiality}: Memory design incorporates privilege boundaries
  \item \textbf{Accountability}: Deployment gates ensure role clarity
\end{itemize}
\end{keybox}
```

---

## New Subsection: Three-Level Hierarchy Mapping

**Recommended new section** (after intro, before architecture):

```latex
\section{How Part II Implements Part I's Three-Level Hierarchy}
\label{sec:agents2-hierarchy-mapping}

Part I establishes three levels of agentic sophistication (\Cref{sec:intro}):

\begin{itemize}
  \item \textbf{Level 1: Minimal Agency} (3 properties: Goal, Perception, Action)
  \item \textbf{Level 2: Traditional Agentic Software} (6 properties via rules/algorithms)
  \item \textbf{Level 3: AI-Powered Agentic Systems} (6 properties via LLMs/neural networks)
\end{itemize}

Part II's architecture, protocols, and evaluation methods \textbf{support all three levels}.
The reference architecture does not mandate LLMs; it works equally well for traditional
rule-based systems (Level 2) and AI-powered systems (Level 3):

\begin{table}[h]
\centering
\small
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Component} & \textbf{Level 2 (Traditional)} & \textbf{Level 3 (AI-Powered)} \\
\midrule
Goal specification & Config files, hardcoded objectives & Natural language instructions \\
Perception & Structured APIs, SQL queries & LLM document understanding, semantic search \\
Action (tools) & Function calls, database writes & LLM tool orchestration, code generation \\
Planning/reasoning & Decision trees, rule engines & LLM chains, ReAct loops \\
Adaptation & Threshold tuning, A/B test results & Chain-of-thought, in-context learning \\
Termination & Explicit conditionals & LLM-decided task completion + external budgets \\
\bottomrule
\end{tabular}
\caption{Implementation approaches for the same six properties across Level 2 and Level 3.}
\label{tab:arch-levels}
\end{table}

As you read Part II, ask: which architectural choices apply to Level 2, which to Level 3,
and which to both? The answer is: \textbf{most apply to both}, because the properties
are implementation-agnostic.
```

---

## Summary: Alignment Status

| Section | Current Alignment | Priority Fix |
|---------|-------------------|--------------|
| Architecture | WEAK | Add GPA+IAT mapping subsection |
| Tools | WEAK | Add "Tool Use ≠ Agency" box |
| Memory | MODERATE | Clarify Iteration property relationship |
| Planning | MODERATE | Add autonomy spectrum table |
| Protocols | WEAK | Reframe discovery as Perception |
| Evaluation | MODERATE | Add property-to-layer mapping |
| Industry | WEAK | Connect topologies to autonomy/entity frames |
| Synthesis | MODERATE | Reference Part I's six safeguards |

**Strong alignments to maintain**:
- Protocols section on governance metadata (already aligned with Part I)
- Evaluation Layer 1 retrieval (appropriately validates Perception)
- Synthesis emphasis on audit/provenance
