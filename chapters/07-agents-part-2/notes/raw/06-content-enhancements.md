# Content Enhancements for Chapter 07

**Generated**: November 27, 2025
**Purpose**: Section-by-section content improvements for Part II

---

## Overview

This document specifies content enhancements for existing sections in Chapter 07. These are additions to existing content, not structural reorganizations (see `05-structural-additions.md` for new sections).

---

## Tools Section (`sec:agents2-tools`)

### Current Content

> "Design tools with schemas that capture both functionality and governance metadata (data class, audit flags, jurisdictional constraints). Expose deterministic JSON-compatible interfaces and log every invocation."

### Enhancement 1: Tool Use ≠ Agency Clarification

**Add after current paragraph:**

```latex
\begin{cautionbox}[title={Tool Use is Not Agency}]
From Part I (\Cref{sec:practical}): calling external tools does not automatically make an entity agentic. The critical question is whether the entity \emph{iterates on tool results}, \emph{adapts} its strategy based on what it observes, and has clear \textbf{termination} conditions.

A script that queries an API once is not an agent---it lacks iteration and adaptation. A research system that queries the API, evaluates relevance, and decides what to search next based on results \emph{may} qualify as agentic, depending on whether it completes the perception-action-adaptation cycle and enforces termination.

For tool-use patterns to support agentic behavior, the agent must:
\begin{enumerate}
  \item \textbf{Perceive} the tool's output (not just invoke it)
  \item \textbf{Evaluate} whether results advance toward the goal
  \item \textbf{Decide} which tool to invoke next based on observations
  \item \textbf{Know when to stop} using tools (termination via goal satisfaction, confidence thresholds, or resource limits)
\end{enumerate}
\end{cautionbox}
```

### Enhancement 2: Reference to Chapter 03

**Add cross-reference:**

```latex
Design tools following the contract and governance metadata patterns established in \Cref{sec:llmC-tools}. Each tool schema should capture:
\begin{itemize}
  \item Functionality: name, description, input/output schemas
  \item Data classification: confidential, privileged, jurisdiction-specific
  \item Governance metadata: purpose, legal basis, audit requirements
  \item Idempotency: whether repeated calls are safe
\end{itemize}
```

---

## Memory Section (`sec:agents2-memory`)

### Current Content

> "Combine short-term conversational state with persistent case/project memory. Enforce privilege boundaries and retention policies; prefer content-addressed storage for provenance. Treat the retrieval layer as governed memory: index content with dates and jurisdictions, filter by authorization at query time, and attach evidence records per \Cref{sec:llmC-evidence}. Keep mechanics lightweight here and defer retrieval basics to \Cref{sec:llmC-rag}."

### Enhancement: Iteration Property Explanation

**Replace first sentence with expanded explanation:**

```latex
\textbf{The Iteration Property and State Preservation.} From Part I (\Cref{sec:intro}), the Iteration property requires ``multiple perceive-act cycles with state preservation across rounds.'' Memory systems are the primary mechanism for state preservation. An agent without persistent memory cannot remember what it has already perceived or tried, preventing true iteration---it would merely repeat the same action indefinitely or process input once without learning.

\textit{Example:} A legal research agent might iterate as follows:
\begin{enumerate}
  \item \textbf{Cycle 1}: Query case law (perception) $\rightarrow$ receive results $\rightarrow$ record findings in memory
  \item \textbf{Cycle 2}: Perceive findings from memory $\rightarrow$ refine search terms based on gaps $\rightarrow$ query again (action)
  \item \textbf{Cycle 3}: Compare new results to prior findings $\rightarrow$ escalate to human if contradictions found (adaptation)
  \item \textbf{Cycle 4}: Synthesize accumulated findings $\rightarrow$ determine research is complete (termination)
\end{enumerate}

Without persistent memory between cycles, the agent cannot distinguish ``I searched for this already'' from ``I have not searched for this.'' The cycles collapse into either infinite repetition or single-shot processing---neither of which qualifies as agentic per Part I.

\paragraph{Memory Architecture Layers.} Combine multiple memory types to support the full perception-action-adaptation cycle:
\begin{itemize}
  \item \textbf{Conversational state} (short-term): Current session context, in-flight decisions, working memory
  \item \textbf{Case/project memory} (long-term): Durable findings, prior searches, accumulated evidence
  \item \textbf{Evidence records} (auditable): Traceable provenance per \Cref{sec:llmC-evidence}
  \item \textbf{Privilege boundaries} (legal/ethical): Enforce attorney-client privilege and work product doctrine
\end{itemize}

Treat the retrieval layer as governed memory...
```

### Enhancement: MemGPT Reference

**Add reference to hierarchical memory:**

```latex
For agents requiring extended context, consider hierarchical memory architectures such as MemGPT \parencite{packer2023memgpt}, which treats the context window as a constrained memory resource and implements paging between core memory (immediately accessible) and archival memory (retrieved on demand).
```

---

## Planning Section (`sec:agents2-planning`)

### Current Content

> "Adopt planning patterns (react, plan-act-observe, graph/workflow) appropriate to task risk. Separate deliberation traces from user-facing output; instrument escalation triggers for low confidence."

### Enhancement 1: Autonomy Spectrum Mapping

**Add table and explanation:**

```latex
\paragraph{Planning Patterns and Autonomy.} Planning patterns should be chosen based on both \textbf{task risk} and \textbf{agent autonomy level} from Part I's analytical dimensions (\Cref{sec:dimensions}). Part I identifies an autonomy spectrum ranging from delegated proxies (low autonomy, tight control) to tool orchestrators (very high autonomy, minimal intervention). Each planning pattern supports different points on this spectrum:

\begin{table}[htbp]
\centering
\small
\begin{tabular}{@{}p{3cm}p{3.5cm}p{6cm}@{}}
\toprule
\textbf{Pattern} & \textbf{Autonomy Level} & \textbf{When to Use} \\
\midrule
Reactive (if-then rules) & Delegated proxy & Rule-based compliance; tight control required; deterministic outcomes expected \\
Plan-act-observe & Contract-bound delegate & Predefined workflows with tactical discretion; human reviews plan before execution \\
ReAct (reasoning loops) & Perception-action planner & Tool-based research; agent interprets goals and selects tools within scope \\
Tree/Graph-of-Thought & Self-regulating actor & Complex reasoning requiring exploration of alternatives; legal analysis with multiple viable interpretations \\
Multi-agent orchestration & Tool orchestrator & Complex task decomposition across specialized agents; minimal human intervention \\
\bottomrule
\end{tabular}
\caption{Planning patterns mapped to autonomy levels from Part I (\Cref{sec:dimensions}).}
\label{tab:patterns-autonomy}
\end{table}

\textbf{Governance Implication} (from Part I): Oversight rigor must scale with autonomy. High-autonomy planning (tool orchestrators, multi-agent systems) requires:
\begin{itemize}
  \item Explicit termination mechanisms (resource budgets, iteration limits)
  \item Human-in-the-loop checkpoints at critical decision points
  \item Robust audit trails capturing deliberation traces
  \item Clear escalation triggers for low confidence or unexpected situations
\end{itemize}

Low-autonomy planning (delegated proxies) operates under tight principal control with lighter oversight but less flexibility.
```

### Enhancement 2: Reference to Chapter 05

**Add cross-reference:**

```latex
Select reasoning patterns from the strategy catalog in \Cref{sec:llmE-strategy}. Chapter 05 provides detailed guidance on when to use chain-of-thought, self-consistency, ReAct, and tree-of-thought patterns based on task characteristics. Part II adds the autonomy dimension: match pattern complexity to the agent's position on the autonomy spectrum.
```

### Enhancement 3: Tree of Thoughts Reference

**Add citation:**

```latex
For complex legal reasoning requiring exploration of alternatives, consider Tree of Thoughts \parencite{yao2023tot}, which enables deliberate problem solving with lookahead and backtracking. This pattern is appropriate for legal analysis tasks where multiple interpretations must be considered before reaching a conclusion.
```

---

## Protocols Section (`sec:agents2-proto-discovery`)

### Current Content

> "Advertise actions with names, schemas, pre/postconditions, data classifications, and audit requirements. Prefer machine-readable descriptors over prose documentation."

### Enhancement: Capability Discovery as Perception

**Replace with expanded explanation:**

```latex
\subsection{Capability Discovery and Contracts}
\label{sec:agents2-proto-discovery}

\textbf{Capability Discovery as Agent Perception.} From Part I (\Cref{sec:intro}), the Perception property requires ``awareness of environment through sensing capabilities---sensors, APIs, database access, document reading.'' In a software agent context, the environment includes not just data (case law, regulatory filings) but also the set of available actions (tools, APIs, services). Capability discovery is the mechanism by which agents \emph{perceive} what actions are available.

An agent that does not know what tools exist or what they can do is perceptually blind to part of its environment. This blindness prevents adaptive behavior: the agent cannot select the best tool for the current goal if it cannot perceive what tools are available.

\paragraph{Requirements for Capability Discovery.} For adaptive behavior, the agent must:
\begin{itemize}
  \item \textbf{Discover} available tools and their capabilities (capability discovery via MCP manifests or A2A Agent Cards)
  \item \textbf{Understand} pre/postconditions and data requirements (constraints on when actions are valid)
  \item \textbf{Select} which tool is appropriate for the current goal (reasoning about capabilities)
  \item \textbf{Observe} results and adapt next steps accordingly (perception-action coupling)
\end{itemize}

\paragraph{Machine-Readable Descriptors.} Advertise actions with machine-readable descriptors including:
\begin{itemize}
  \item Names and functional descriptions (what the tool does)
  \item Input/output schemas and data types (JSON Schema, OpenAPI)
  \item Pre/postconditions and invariants (when the tool can be called, what it guarantees)
  \item Data classifications (confidential, privileged, jurisdiction-specific)
  \item Audit requirements and logging expectations (what gets logged, retention policies)
  \item Rate limits and cost information (operational constraints)
\end{itemize}

Prefer machine-readable formats (JSON Schema, OpenAPI specifications) over prose documentation to enable agents to parse, reason about, and adapt to available capabilities programmatically.
```

---

## Industry Section (`sec:agents2-topologies`)

### Current Content

> "Single-agent with tools; orchestrated multi-agent with shared memory; hub-and-spoke integrations with standardized capability gateways."

### Enhancement: Connection to Autonomy Spectrum

**Expand with Part I mapping:**

```latex
\subsection{Common Topologies}
\label{sec:agents2-topologies}

Deployment topologies should align with Part I's autonomy spectrum (\Cref{sec:dimensions}) and entity frames:

\paragraph{Single-Agent with Tools.} Appropriate for perception-action planners operating within defined scope. The agent has a clear mandate, accesses tools to fulfill it, and maintains single point of accountability.
\begin{itemize}
  \item \textbf{Autonomy level}: Moderate (perception-action planner)
  \item \textbf{Entity frame}: Machine-centered or human extension
  \item \textbf{Use case}: Legal research assistant, contract analyzer, regulatory monitor
\end{itemize}

\paragraph{Orchestrated Multi-Agent with Shared Memory.} Enables tool orchestrator-level autonomy. Multiple specialized agents collaborate on complex tasks, sharing state through common memory.
\begin{itemize}
  \item \textbf{Autonomy level}: High (tool orchestrators coordinating)
  \item \textbf{Entity frame}: Institutional/hybrid (agents as team members)
  \item \textbf{Use case}: Complex due diligence, multi-jurisdiction analysis, M\&A workflows
  \item \textbf{Governance}: Requires clear delegation contracts and escalation paths between agents
\end{itemize}

\paragraph{Hub-and-Spoke Integrations.} Centralizes control in an orchestrator (lower autonomy) while delegating specific tasks to specialized agents at the spokes.
\begin{itemize}
  \item \textbf{Autonomy level}: Moderate (orchestrator) to Low (spokes)
  \item \textbf{Entity frame}: Institutional hierarchy
  \item \textbf{Use case}: Enterprise legal operations, centralized intake and triage
  \item \textbf{Governance}: Orchestrator maintains audit trail and approval authority
\end{itemize}

From Part I's entity frames (\Cref{sec:dimensions}), consider how agents should be framed in your organization:
\begin{itemize}
  \item \textbf{Machine-centered}: Agents as autonomous computational entities with defined capabilities
  \item \textbf{Human-centered}: Agents as extensions of human professionals who retain oversight
  \item \textbf{Institutional/Hybrid}: Agents embedded in organizational authority structures with role-based permissions
\end{itemize}

The choice of topology and entity frame affects governance requirements (Part III) and liability allocation.
```

---

## Evaluation Section (`sec:agents2-eval-retrieval`)

### Current Content

> "Assess precision/recall, MRR, and nDCG on legal corpora; include jurisdictional coverage and temporal validity checks. For quick gates before system trials, use the retrieval sanity checks in \Cref{sec:llmD-eval-retrieval-quick} and require evidence records per \Cref{sec:llmC-evidence}."

### Enhancement: Expand Metrics and Benchmarks

```latex
\subsection{Layer 1: Retrieval}
\label{sec:agents2-eval-retrieval}

Layer 1 validates the \textbf{Perception property}: can the agent accurately access and assess its environment?

\paragraph{Core Metrics.}
\begin{itemize}
  \item \textbf{Precision/Recall}: What fraction of retrieved documents are relevant? What fraction of relevant documents are retrieved?
  \item \textbf{Mean Reciprocal Rank (MRR)}: How highly is the first relevant document ranked?
  \item \textbf{Normalized Discounted Cumulative Gain (nDCG)}: How well does ranking reflect graded relevance?
\end{itemize}

\paragraph{Legal-Specific Requirements.}
\begin{itemize}
  \item \textbf{Jurisdictional coverage}: Does retrieval correctly scope to relevant jurisdictions? A Delaware corporate law question should not retrieve California precedents.
  \item \textbf{Temporal validity}: Does retrieval respect effective dates? Superseded statutes and overruled cases must be flagged.
  \item \textbf{Source authority}: Does retrieval distinguish binding authority from persuasive authority?
\end{itemize}

\paragraph{Quick Gates.} For rapid validation before full system trials, use the retrieval sanity checks in \Cref{sec:llmD-eval-retrieval-quick}:
\begin{evallist}
  \item Confirm recall@k on known question-answer pairs
  \item Verify returned passages carry dates and jurisdictions
  \item Verify quotes and locators match sources
  \item Require evidence records per \Cref{sec:llmC-evidence}
\end{evallist}

\paragraph{Benchmark References.} For systematic retrieval evaluation:
\begin{itemize}
  \item LegalBench-Retrieve \parencite{legalbench-rag} for legal retrieval
  \item GAIA \parencite{mialon2023gaia} for general retrieval with tool use
\end{itemize}
```

---

## Evaluation Section (`sec:agents2-eval-workflow`)

### Current Content

> "Measure end-to-end task completion, robustness to tool errors, and escalation triggers under uncertainty."

### Enhancement: Expand with Property Mapping

```latex
\subsection{Layer 3: Agentic Workflows}
\label{sec:agents2-eval-workflow}

Layer 3 validates \textbf{Iteration} and \textbf{Termination}: does the agent complete multiple perceive-act cycles and recognize when to stop?

\paragraph{Iteration Validation.}
\begin{evallist}
  \item Does the agent execute multiple perceive-act cycles for complex tasks?
  \item Does state persist correctly across cycles (memory evaluation)?
  \item Does the agent build on prior observations rather than repeating searches?
\end{evallist}

\paragraph{Termination Validation.}
\begin{evallist}
  \item Does the agent terminate when the goal is achieved?
  \item Does the agent respect resource budgets (iteration limits, token limits, time limits)?
  \item Does the agent escalate appropriately when confidence is low or when it encounters unexpected situations?
\end{evallist}

\paragraph{Robustness Testing.}
\begin{evallist}
  \item \textbf{Tool failures}: Does the agent recover gracefully from tool errors, timeouts, and rate limits?
  \item \textbf{Adversarial inputs}: Does the agent detect and handle prompt injection attempts?
  \item \textbf{Edge cases}: Does the agent handle missing data, ambiguous queries, and conflicting information?
\end{evallist}

\paragraph{End-to-End Metrics.}
\begin{itemize}
  \item \textbf{Task completion rate}: What fraction of tasks reach successful termination?
  \item \textbf{Cycles to completion}: How many perceive-act cycles does the agent require?
  \item \textbf{Escalation accuracy}: When the agent escalates, is escalation appropriate?
  \item \textbf{Cost efficiency}: What is the total cost (tokens, API calls, time) per completed task?
\end{itemize}

\paragraph{Benchmark References.}
\begin{itemize}
  \item AgentBench \parencite{liu2023agentbench} for multi-environment workflow evaluation
  \item WebArena \parencite{zhou2023webarena} for realistic web-based workflows
  \item LegalAgentBench \parencite{legalagentbench} for legal-specific workflow evaluation
\end{itemize}
```

---

## Synthesis Section (`sec:agents2-synthesis`)

### Current Content

> "We synthesize architectural and protocol guidance into a minimal viable agent blueprint and identify the governance controls that Part III will require (transparency, audit, privilege, jurisdictional policy, and deployment gates)."

### Enhancement: Connect to Part I Safeguards

**Expand with specific safeguard mapping:**

```latex
\section{Synthesis and Handoff to Governance}
\label{sec:agents2-synthesis}

We synthesize architectural and protocol guidance into a minimal viable agent blueprint and identify the governance controls that Part III will require.

\paragraph{Part I's Professional Deployment Safeguards.} The synthesis is grounded in Part I's professional deployment framework (\Cref{sec:synthesis}), which identifies six essential safeguards for legal and financial AI agents:

\begin{enumerate}
  \item \textbf{Attribution and Provenance} --- Every factual claim must be traceable to its source
  \item \textbf{Auditable Reasoning} --- Reasoning steps, tool invocations, and decision points must be logged
  \item \textbf{Bounded Operation} --- Explicit computational budgets, time constraints, and iteration limits
  \item \textbf{Escalation Pathways} --- Clear triggers for human review and override
  \item \textbf{Confidentiality Controls} --- Enforce privilege, role-based access, and redaction
  \item \textbf{Accountability Mapping} --- Clear lines of responsibility when failures occur
\end{enumerate}

\paragraph{How Part II Enables Each Safeguard.}

\begin{keybox}[title={From Build to Govern}]
\begin{itemize}
  \item \textbf{Attribution}: Retrieval-layer evaluation (Layer 1) ensures evidence records (\Cref{sec:llmC-evidence}) are captured and attached to claims
  \item \textbf{Auditable Reasoning}: Planning and reasoning patterns (architecture section) are instrumented to produce decision traces separate from user output
  \item \textbf{Bounded Operation}: Termination mechanisms (GPA+IAT property T) enforce resource budgets, iteration limits, and time constraints
  \item \textbf{Escalation}: Protocol-level governance metadata and error handlers (protocols section) define escalation triggers and pathways
  \item \textbf{Confidentiality}: Memory architecture (architecture section) incorporates privilege boundaries and authorization filters
  \item \textbf{Accountability}: Industry patterns and deployment gates (industry section) ensure role clarity and approval workflows
\end{itemize}
\end{keybox}

\paragraph{Design-Time, Not Bolt-On.} These safeguards must be \textbf{designed in from the start}, not bolted on after development:
\begin{itemize}
  \item Instrument audit and provenance at design time
  \item Treat protocols as control planes: they carry governance metadata alongside functional data
  \item Validate Layers 1--3 before advancing to governance evaluation in Part III
\end{itemize}

Part III builds on this foundation by implementing the governance controls themselves and defining deployment gates for production use.
```

---

## Summary: Content Enhancements

| Section | Enhancement | Priority |
|---------|-------------|----------|
| `sec:agents2-tools` | Tool Use ≠ Agency box + Chapter 03 reference | HIGH |
| `sec:agents2-memory` | Iteration property explanation + MemGPT reference | HIGH |
| `sec:agents2-planning` | Autonomy spectrum table + Chapter 05 reference + ToT reference | HIGH |
| `sec:agents2-proto-discovery` | Capability discovery as Perception reframing | HIGH |
| `sec:agents2-topologies` | Connection to autonomy spectrum and entity frames | MEDIUM |
| `sec:agents2-eval-retrieval` | Expanded metrics and legal-specific requirements | MEDIUM |
| `sec:agents2-eval-workflow` | Property mapping and robustness testing | MEDIUM |
| `sec:agents2-synthesis` | Part I safeguard mapping | HIGH |
