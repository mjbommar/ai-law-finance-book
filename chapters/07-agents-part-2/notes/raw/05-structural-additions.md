# Structural Additions for Chapter 07

**Generated**: November 27, 2025
**Purpose**: New subsections and structural changes to add to Part II

---

## Overview

This document specifies new structural elements to add to Chapter 07. These additions address alignment gaps with Part I and incorporate November 2025 developments.

---

## Addition 1: GPA+IAT Mapping Section

**Location**: After `sec:agents2-intro`, before `sec:agents2-architecture`
**New label**: `sec:agents2-hierarchy-mapping`
**Priority**: HIGH

### Rationale

Part II currently lacks explicit connection to Part I's three-level hierarchy. This section bridges the conceptual foundation (Part I) to practical implementation (Part II).

### Proposed Content

```latex
\section{How Part II Implements Part I's Framework}
\label{sec:agents2-hierarchy-mapping}

Part I establishes what makes a system agentic: six properties organized into a three-level hierarchy (\Cref{sec:intro}). Part II shows how to implement these properties in practice.

\subsection{The Six Properties Revisited}

Recall from Part I that agentic systems require:

\begin{itemize}
  \item \textbf{Goal (G)} — Clear objective or performance criterion
  \item \textbf{Perception (P)} — Awareness of environment through sensing
  \item \textbf{Action (A)} — Capability to affect environment
  \item \textbf{Iteration (I)} — Multiple perceive-act cycles with state preservation
  \item \textbf{Adaptation (A)} — Strategy adjustment based on feedback
  \item \textbf{Termination (T)} — Clear stopping conditions
\end{itemize}

Part II's architecture, protocols, and evaluation practices operationalize each property.

\subsection{Architecture Mapping}

\begin{table}[htbp]
\centering
\small
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Architecture Pillar} & \textbf{Properties Implemented} & \textbf{How} \\
\midrule
Tools \& Function Calling & Action (A) & Define what agent can do \\
Memory \& State & Iteration (I), Perception (P) & Preserve state; store observations \\
Planning \& Control & Goal (G), Adaptation (A), Termination (T) & Decompose goals; adjust; stop \\
\bottomrule
\end{tabular}
\caption{Mapping architecture pillars to GPA+IAT properties.}
\label{tab:arch-properties}
\end{table}

\subsection{Level 2 vs. Level 3 Implementation}

Part II's guidance applies to both traditional (Level 2) and AI-powered (Level 3) agentic systems. The properties are implementation-agnostic:

\begin{table}[htbp]
\centering
\small
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Property} & \textbf{Level 2 (Traditional)} & \textbf{Level 3 (AI-Powered)} \\
\midrule
Goal & Config files, hardcoded & Natural language instructions \\
Perception & Structured APIs, SQL & Semantic search, document understanding \\
Action & Function calls, DB writes & LLM tool orchestration \\
Iteration & State machines, queues & Conversation history, memory systems \\
Adaptation & Threshold tuning, rules & Chain-of-thought, in-context learning \\
Termination & Explicit conditionals & LLM-decided + external budgets \\
\bottomrule
\end{tabular}
\caption{Implementation approaches across Levels 2 and 3.}
\label{tab:level-implementations}
\end{table}

As you read Part II, ask: does this guidance apply to Level 2, Level 3, or both? Most guidance applies to both because the properties are implementation-agnostic.
```

---

## Addition 2: Architecture Section Opener

**Location**: Beginning of `sec:agents2-architecture`
**Priority**: HIGH

### Rationale

The architecture section jumps directly into tools without explaining how the three pillars relate to Part I's framework.

### Proposed Content

```latex
\section{Reference Architecture and Core Components}
\label{sec:agents2-architecture}

This section presents a vendor-neutral reference architecture for legal agents. The architecture has three pillars, each implementing specific properties from Part I's GPA+IAT framework (\Cref{sec:intro}):

\begin{enumerate}
  \item \textbf{Tools and Function Calling} — implements the \textbf{Action} property
  \item \textbf{Memory and State Management} — implements \textbf{Iteration} and supports \textbf{Perception}
  \item \textbf{Planning, Reasoning, and Control} — implements \textbf{Goal}, \textbf{Adaptation}, and \textbf{Termination}
\end{enumerate}

The architecture does not prescribe specific technologies. It works equally well for rule-based systems (Level 2) and LLM-powered systems (Level 3). The key is ensuring all six properties are present and properly implemented.

% [Continue with existing subsections...]
```

---

## Addition 3: Evaluation Section Opener

**Location**: Beginning of `sec:agents2-eval`
**Priority**: HIGH

### Rationale

The evaluation section defines three layers but doesn't explain how they validate Part I's properties.

### Proposed Content

```latex
\section{Technical Evaluation: Retrieval, Reasoning, and Workflows}
\label{sec:agents2-eval}

This section defines evaluation layers for technical correctness prior to governance gates in Part III. Each layer validates specific properties from Part I's GPA+IAT framework (\Cref{sec:intro}):

\begin{itemize}
  \item \textbf{Layer 1 (Retrieval)} validates the \textbf{Perception property}: Can the agent access and assess its environment? Does it recognize temporal validity and jurisdictional scope?

  \item \textbf{Layer 2 (Reasoning)} validates the \textbf{Adaptation property}: Can the agent adjust its analysis based on evidence? Does it ground claims in sources?

  \item \textbf{Layer 3 (Workflows)} validates \textbf{Iteration} and \textbf{Termination}: Does the agent complete multiple perceive-act cycles? Does it recognize when to stop or escalate?
\end{itemize}

\begin{cautionbox}[title={Evaluation Gates}]
Failures in these technical layers indicate the system lacks foundational agentic properties. A system that cannot perceive its environment (Layer 1), adapt its reasoning (Layer 2), or iterate toward termination (Layer 3) is not an agentic system per Part I's definition---regardless of how sophisticated its underlying model.
\end{cautionbox}

Before advancing to governance evaluation in Part III, all three layers must pass.

% [Continue with existing subsections...]
```

---

## Addition 4: Security Considerations Section

**Location**: New section after `sec:agents2-industry`, before `sec:agents2-eval`
**New label**: `sec:agents2-security`
**Priority**: MEDIUM-HIGH

### Rationale

Security is critical for legal AI agents handling confidential data. Currently absent from Part II.

### Proposed Content

```latex
\section{Security Considerations for Agent Architectures}
\label{sec:agents2-security}

Legal and financial agents handle confidential information: attorney-client privileged communications, work product, material non-public information, and personally identifiable data. Security must be designed into the architecture, not bolted on later.

\subsection{Threat Model for Legal AI Agents}

Legal AI agents face an elevated threat model due to:
\begin{itemize}
  \item \textbf{Data sensitivity}: Privileged communications, trade secrets, MNPI
  \item \textbf{Adversarial inputs}: Opposing parties may attempt prompt injection
  \item \textbf{Extended attack surface}: Each tool, memory store, and integration point is a potential vector
  \item \textbf{Regulatory consequences}: Breach of privilege or confidentiality can result in sanctions, malpractice liability, or regulatory action
\end{itemize}

\subsection{Security Architecture Principles}

\paragraph{Graceful Degradation.} Per the AWS Agentic AI Security Scoping Matrix, agents should automatically reduce autonomy when security events are detected. Detective controls can inject restrictions or disable agents entirely. A legal research agent that detects potential data exfiltration should halt operations and escalate to human review rather than continue operating.

\paragraph{Zero Trust for Agents.} Apply Zero Trust principles to agent systems:
\begin{itemize}
  \item Assume breach: design for containment
  \item Never implicitly trust: verify every request
  \item Explicit verification: authenticate agents, tools, and data sources
  \item Least privilege: limit agent capabilities to minimum required
\end{itemize}

\paragraph{Protocol Security.} MCP and A2A protocols require careful security configuration:
\begin{itemize}
  \item Authenticate all MCP servers; do not expose unauthenticated endpoints
  \item Validate tool permissions to prevent file exfiltration attacks
  \item Guard against lookalike tools that silently replace trusted ones
  \item Use signed Agent Cards in A2A to verify agent identity
\end{itemize}

\subsection{Security Evaluation}

Include security in Layer 3 workflow evaluation:
\begin{evallist}
  \item Does the agent detect and respond to prompt injection attempts?
  \item Are privilege boundaries enforced across tool invocations?
  \item Does the agent gracefully degrade under adversarial conditions?
  \item Are audit logs tamper-resistant and complete?
\end{evallist}

% Cross-reference to Part III governance
Security controls are further developed in Part III's governance framework.
```

---

## Addition 5: Legal AI Case Studies Section

**Location**: New subsection within `sec:agents2-industry`
**New label**: `sec:agents2-case-studies`
**Priority**: MEDIUM

### Rationale

Real-world examples ground abstract architecture in practice. Harvey and CoCounsel demonstrate production legal AI agents.

### Proposed Content

```latex
\subsection{Case Studies: Legal AI Agents in Production}
\label{sec:agents2-case-studies}

\paragraph{Harvey AI.} Harvey demonstrates multi-step agentic workflows for complex legal tasks. Launched in 2023 and reaching \$100M ARR by August 2025, Harvey serves majority of the top 10 US law firms across 63 countries.

Key architectural patterns:
\begin{itemize}
  \item \textbf{Deep Research}: Combines OpenAI's reasoning API with Harvey's legal-specific processing to plan research strategies, execute iteratively, and deliver grounded reports
  \item \textbf{Custom evaluation}: Compares agent outputs to human lawyer work product, not generic benchmarks
  \item \textbf{Transparency and oversight}: Multi-step reasoning with human review at critical junctures
\end{itemize}

Use cases deployed with A\&O Shearman (April 2025):
\begin{itemize}
  \item Antitrust filing analysis
  \item Cybersecurity incident assessment
  \item Fund formation review
  \item Loan document analysis
\end{itemize}

\paragraph{Thomson Reuters CoCounsel.} CoCounsel Legal (August 2025) demonstrates integration of agentic AI with authoritative legal content:

Key architectural patterns:
\begin{itemize}
  \item \textbf{Deep Research}: Professional-grade agentic research that creates research plans, executes iteratively, and delivers reports grounded in Westlaw and Practical Law
  \item \textbf{Guided workflows}: Structured processes for high-friction legal work
  \item \textbf{Scale}: Beta features (November 2025) include bulk review of 10,000+ documents
\end{itemize}

Adoption metrics:
\begin{itemize}
  \item 20,000+ law firms and legal departments
  \item Majority of Am Law 100
  \item 100\% of Fortune 100, 97\% of Fortune 1000
\end{itemize}

\paragraph{Patterns for Legal AI Agents.} Common patterns across successful legal AI agents:
\begin{enumerate}
  \item Multi-step reasoning with transparency at each step
  \item Integration with authoritative content sources (Westlaw, EDGAR, official reporters)
  \item Human-in-the-loop approval for high-stakes actions
  \item Domain-specific evaluation against human expert work product
  \item Bulk document processing at scale (thousands of documents)
\end{enumerate}
```

---

## Addition 6: Protocol Comparison Subsection

**Location**: New subsection within `sec:agents2-protocols`
**New label**: `sec:agents2-proto-comparison`
**Priority**: HIGH

### Rationale

MCP and A2A are the two dominant protocols as of November 2025. Part II should compare them.

### Proposed Content

```latex
\subsection{MCP vs. A2A: Complementary Protocols}
\label{sec:agents2-proto-comparison}

Two protocols have emerged as standards for agent interoperability: Anthropic's Model Context Protocol (MCP) and Google's Agent-to-Agent Protocol (A2A). They serve complementary purposes.

\begin{table}[htbp]
\centering
\small
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Aspect} & \textbf{MCP} & \textbf{A2A} \\
\midrule
Purpose & Agent-to-tool communication & Agent-to-agent communication \\
Launch & November 2024 (Anthropic) & April 2025 (Google) \\
Governance & Anthropic-led open source & Linux Foundation (June 2025) \\
Transport & JSON-RPC over stdio/HTTP & JSON-RPC 2.0 over HTTP, SSE, gRPC \\
Discovery & Server manifests & Agent Cards \\
Adoption & OpenAI, Google, Microsoft & 50+ partners, Amazon Bedrock \\
\bottomrule
\end{tabular}
\caption{Comparison of MCP and A2A protocols.}
\label{tab:mcp-a2a}
\end{table}

\paragraph{When to Use Each.}
\begin{itemize}
  \item \textbf{MCP}: Connecting agents to tools, databases, and external services. Use for document management system integration, research platform APIs, and structured data access.
  \item \textbf{A2A}: Enabling collaboration between multiple agents. Use for orchestrated workflows where specialized agents (research, drafting, review) hand off work.
\end{itemize}

\paragraph{Dual Protocol Strategy.} Production legal AI systems typically require both protocols:
\begin{itemize}
  \item MCP for tool integration (Westlaw API, document management, case management)
  \item A2A for multi-agent coordination (research agent → drafting agent → review agent)
\end{itemize}

\begin{cautionbox}[title={Protocol Security}]
MCP security issues were identified in April--July 2025: prompt injection vulnerabilities, file exfiltration risks, and authentication gaps on exposed servers. Legal AI deployments must:
\begin{itemize}
  \item Authenticate all MCP endpoints
  \item Validate tool permissions carefully
  \item Never expose MCP servers to untrusted networks
  \item Use signed Agent Cards in A2A deployments
\end{itemize}
\end{cautionbox}
```

---

## Addition 7: Further Learning Updates

**Location**: `sec:agents2-further`
**Priority**: LOW

### Rationale

Current Further Learning section is sparse. Should point to key resources.

### Proposed Content

```latex
\section{Further Learning}
\label{sec:agents2-further}

\subsection{Protocol Specifications}

\begin{itemize}
  \item \textbf{Model Context Protocol}: \url{https://modelcontextprotocol.io/} --- Anthropic's agent-to-tool standard; SDKs for Python, TypeScript, C\#
  \item \textbf{Agent-to-Agent Protocol}: \url{https://a2a-protocol.org/} --- Linux Foundation specification for agent collaboration
  \item \textbf{OpenAI Function Calling}: \url{https://platform.openai.com/docs/guides/function-calling} --- De facto tool-use specification
\end{itemize}

\subsection{Evaluation Benchmarks}

\begin{itemize}
  \item \textbf{AgentBench}: 8-environment benchmark for LLM-as-Agent evaluation \parencite{liu2023agentbench}
  \item \textbf{GAIA}: General AI Assistant benchmark testing reasoning and tool use \parencite{mialon2023gaia}
  \item \textbf{LegalAgentBench}: Legal-specific agent evaluation \parencite{legalagentbench}
  \item \textbf{WebArena}: Realistic web environment for agent testing \parencite{zhou2023webarena}
\end{itemize}

\subsection{Frameworks and Platforms}

\begin{itemize}
  \item \textbf{LangChain/LangGraph}: \url{https://langchain.com/} --- Production agent framework (1.0 released October 2025)
  \item \textbf{Amazon Bedrock AgentCore}: \url{https://aws.amazon.com/bedrock/agents/} --- Enterprise agent infrastructure
  \item \textbf{LlamaIndex Agents}: \url{https://docs.llamaindex.ai/} --- RAG-focused agent framework
\end{itemize}

\subsection{Research Surveys}

\begin{itemize}
  \item Memory mechanisms for LLM agents \parencite{memory-survey-acm}
  \item Agent evaluation methodologies \parencite{agent-eval-survey-2025}
  \item AI agents under the EU AI Act \parencite{eu-ai-act-agents}
\end{itemize}

Part III introduces primary regulatory sources and governance frameworks.
```

---

## Summary: Structural Changes

| Addition | Location | Label | Priority |
|----------|----------|-------|----------|
| GPA+IAT Mapping Section | After intro | `sec:agents2-hierarchy-mapping` | HIGH |
| Architecture Section Opener | Start of architecture | — | HIGH |
| Evaluation Section Opener | Start of evaluation | — | HIGH |
| Security Section | After industry, before eval | `sec:agents2-security` | MEDIUM-HIGH |
| Case Studies Subsection | Within industry | `sec:agents2-case-studies` | MEDIUM |
| Protocol Comparison | Within protocols | `sec:agents2-proto-comparison` | HIGH |
| Further Learning Updates | Further learning | — | LOW |

### Updated Section Order

```
\input{sections/howtoread}
\input{sections/intro}
% NEW: \input{sections/hierarchy-mapping}  % Addition 1
\input{sections/architecture}              % With Addition 2 opener
\input{sections/protocols}                 % With Addition 6 comparison
\input{sections/industry_technical}        % With Addition 5 case studies
% NEW: \input{sections/security}           % Addition 4
\input{sections/evaluation_technical}      % With Addition 3 opener
\input{sections/synthesis}
\input{sections/furtherlearning}           % With Addition 7 updates
\input{sections/conclusion}
```
