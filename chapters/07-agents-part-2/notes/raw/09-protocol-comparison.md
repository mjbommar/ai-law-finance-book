# Protocol Comparison: MCP vs. A2A

**Generated**: November 27, 2025
**Purpose**: Detailed analysis of the two dominant agent protocols for Chapter 07

---

## Overview

As of November 2025, two protocols dominate the agent interoperability landscape:

1. **Model Context Protocol (MCP)** — Anthropic, November 2024
2. **Agent-to-Agent Protocol (A2A)** — Google, April 2025

These protocols serve complementary purposes and are not competitors. Production legal AI systems typically require both.

---

## Protocol Comparison Table

| Aspect | MCP | A2A |
|--------|-----|-----|
| **Purpose** | Agent-to-tool communication | Agent-to-agent communication |
| **Launch Date** | November 25, 2024 | April 9, 2025 |
| **Creator** | Anthropic | Google |
| **Governance** | Anthropic-led open source | Linux Foundation (June 2025) |
| **Transport** | JSON-RPC over stdio, HTTP | JSON-RPC 2.0 over HTTP, SSE, gRPC |
| **Discovery** | Server manifests | Agent Cards |
| **Authentication** | Implementation-dependent | Enterprise auth, signed cards |
| **Adoption** | OpenAI, Google, Microsoft, thousands of servers | 50+ partners, Amazon Bedrock |

---

## Model Context Protocol (MCP)

### Purpose and Scope

MCP provides a standardized way for AI agents to connect with external tools and data sources. Anthropic describes it as "USB-C for AI"—a universal connector that works with any compliant tool.

### Architecture

```
┌─────────────────┐      MCP Protocol       ┌─────────────────┐
│                 │◄──────────────────────►│                 │
│   AI Agent      │   Request/Response      │   MCP Server    │
│   (Client)      │   over JSON-RPC         │   (Tool)        │
│                 │                         │                 │
└─────────────────┘                         └─────────────────┘
                                                    │
                                                    ▼
                                            ┌─────────────────┐
                                            │  External       │
                                            │  Service        │
                                            │  (API, DB, etc) │
                                            └─────────────────┘
```

### Key Components

| Component | Description |
|-----------|-------------|
| **MCP Server** | Exposes capabilities to agents via standardized interface |
| **MCP Client** | Agent-side component that discovers and invokes MCP servers |
| **Server Manifest** | Describes available tools, schemas, requirements |
| **Transport** | JSON-RPC over stdio (local) or HTTP (remote) |

### Adoption Timeline

| Date | Milestone |
|------|-----------|
| Nov 2024 | Anthropic launches MCP |
| Mar 2025 | OpenAI adopts MCP (ChatGPT desktop, Agents SDK, Responses API) |
| Apr 2025 | Google DeepMind confirms Gemini support |
| 2025 | Microsoft partners for official C# SDK |
| 2025 | Community builds thousands of MCP servers |

### Pre-Built Servers

Anthropic provides pre-built MCP servers for common integrations:
- Google Drive
- Slack
- GitHub
- PostgreSQL
- Many more via community

### SDKs

| Language | Status |
|----------|--------|
| Python | Official |
| TypeScript | Official |
| C# | Official (Microsoft partnership) |
| Others | Community |

### Security Concerns

**Vulnerabilities Identified** (April-July 2025):

| Vulnerability | Description | Mitigation |
|---------------|-------------|------------|
| Prompt injection | Malicious tool descriptions inject instructions | Input sanitization, tool validation |
| File exfiltration | Tool permission combinations enable data theft | Least privilege, permission review |
| Lookalike tools | Malicious servers masquerade as trusted ones | Allowlists, cryptographic verification |
| Auth gaps | ~2,000 exposed servers without authentication | Require auth on all endpoints |

**Required Security Controls**:
```
1. Authenticate all MCP endpoints
2. Use allowlists for trusted servers
3. Never expose to untrusted networks
4. Validate tool permissions carefully
5. Audit all interactions
6. Monitor for anomalies
```

### Legal AI Use Cases

| Use Case | MCP Server | Function |
|----------|------------|----------|
| Legal Research | Westlaw MCP | Search case law, statutes |
| Document Management | iManage MCP | Retrieve, store documents |
| Case Management | Clio MCP | Access matter information |
| E-Filing | Court API MCP | Submit filings |
| Citation | Bluebook MCP | Format citations |

---

## Agent-to-Agent Protocol (A2A)

### Purpose and Scope

A2A enables collaboration between multiple agents. While MCP connects agents to tools, A2A connects agents to each other—enabling multi-agent workflows where specialized agents collaborate on complex tasks.

### Architecture

```
┌─────────────────┐      A2A Protocol       ┌─────────────────┐
│                 │◄──────────────────────►│                 │
│   Agent A       │   Task/Artifact         │   Agent B       │
│   (Research)    │   Exchange              │   (Drafting)    │
│                 │                         │                 │
└─────────────────┘                         └─────────────────┘
        │                                           │
        │              Agent Cards                  │
        └─────────────►┌───────────┐◄──────────────┘
                       │ Discovery │
                       │  Service  │
                       └───────────┘
```

### Key Components

| Component | Description |
|-----------|-------------|
| **Agent Card** | Describes agent capabilities, inputs/outputs, requirements |
| **Task** | Unit of work exchanged between agents |
| **Artifact** | Work product produced by agent (document, analysis, etc.) |
| **Transport** | JSON-RPC 2.0 over HTTP, SSE, or gRPC |

### Design Principles

1. **Opacity**: Agents don't need to know each other's internal implementation
2. **Task-Oriented**: Focused on tasks and deliverables, not internal state
3. **Long-Running**: Supports asynchronous, long-duration tasks
4. **Enterprise-Ready**: Built-in authentication and security

### Adoption Timeline

| Date | Milestone |
|------|-----------|
| Apr 9, 2025 | Google announces A2A with 50+ partners |
| Jun 2025 | Contributed to Linux Foundation |
| Nov 2025 | gRPC support, security card signing added |
| Nov 2025 | Amazon Bedrock AgentCore adds A2A support |

### Partner Ecosystem

**Launch Partners** (50+):
- Technology: Atlassian, Box, Intuit, Salesforce, SAP, ServiceNow
- AI: Cohere, LangChain
- Consulting: Accenture, BCG, Deloitte, KPMG, McKinsey, PwC

### Agent Card Structure

```json
{
  "name": "Legal Research Agent",
  "version": "1.0",
  "description": "Performs legal research on case law and statutes",
  "capabilities": [
    {
      "name": "research_case_law",
      "inputs": ["query", "jurisdiction", "date_range"],
      "outputs": ["research_report", "citations"]
    }
  ],
  "authentication": {
    "type": "oauth2",
    "scopes": ["legal.research.read"]
  },
  "security_card": {
    "signed_by": "example.com",
    "signature": "..."
  }
}
```

### Legal AI Use Cases

| Use Case | Agent Collaboration | Flow |
|----------|---------------------|------|
| Complex Research | Research → Analysis → Summary | Research agent finds cases → Analysis agent evaluates → Summary agent produces memo |
| Contract Review | Extraction → Analysis → Drafting | Extraction agent pulls terms → Analysis agent identifies issues → Drafting agent proposes changes |
| Due Diligence | Document Processing → Risk Assessment → Report | Doc agent processes files → Risk agent flags issues → Report agent compiles findings |
| Litigation Support | Discovery → Review → Brief | Discovery agent collects docs → Review agent analyzes → Brief agent drafts arguments |

---

## Complementary Relationship

### When to Use Each Protocol

| Scenario | Protocol | Rationale |
|----------|----------|-----------|
| Connect agent to database | MCP | Tool integration |
| Connect agent to API | MCP | Tool integration |
| Connect agent to document system | MCP | Tool integration |
| Research agent → Drafting agent | A2A | Agent collaboration |
| Multi-agent workflow orchestration | A2A | Agent coordination |
| Specialized agent handoff | A2A | Task delegation |

### Dual Protocol Architecture

Production legal AI systems typically use both protocols:

```
                          ┌───────────────────────────┐
                          │    Orchestrator Agent     │
                          │   (Coordination via A2A)  │
                          └─────────────┬─────────────┘
                                        │ A2A
                    ┌───────────────────┼───────────────────┐
                    │                   │                   │
                    ▼                   ▼                   ▼
            ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
            │Research Agent │   │ Analysis Agent│   │ Drafting Agent│
            └───────┬───────┘   └───────┬───────┘   └───────┬───────┘
                    │ MCP               │ MCP               │ MCP
                    ▼                   ▼                   ▼
            ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
            │ Westlaw       │   │ Contract DB   │   │ Document      │
            │ MCP Server    │   │ MCP Server    │   │ MCP Server    │
            └───────────────┘   └───────────────┘   └───────────────┘
```

### Integration Example

**Scenario**: Complex due diligence workflow

1. **User Request**: "Review target company for M&A due diligence"

2. **Orchestrator** (via A2A):
   - Delegates document collection to Document Agent
   - Delegates financial analysis to Finance Agent
   - Delegates legal risk assessment to Legal Agent

3. **Each Specialized Agent** (via MCP):
   - Document Agent connects to document management (MCP)
   - Finance Agent connects to financial databases (MCP)
   - Legal Agent connects to legal research platforms (MCP)

4. **Aggregation** (via A2A):
   - Agents return artifacts to Orchestrator
   - Orchestrator synthesizes into final report

---

## Security Comparison

| Security Aspect | MCP | A2A |
|-----------------|-----|-----|
| **Authentication** | Implementation-dependent (often lacking) | Built-in enterprise auth |
| **Identity** | Server manifest | Signed Agent Cards |
| **Verification** | Manual allowlists | Cryptographic signing |
| **Audit** | Implementation-dependent | Protocol-level support |
| **Known Issues** | Auth gaps, prompt injection, exfiltration | Newer, fewer known issues |

### Combined Security Architecture

```latex
\begin{cautionbox}[title={Protocol Security Requirements}]
For legal AI deployments:

\textbf{MCP Security}:
\begin{itemize}
  \item Authenticate all MCP endpoints (OAuth, API keys, mTLS)
  \item Maintain allowlists of trusted MCP servers
  \item Never expose MCP servers to untrusted networks
  \item Validate tool permissions and deny dangerous combinations
\end{itemize}

\textbf{A2A Security}:
\begin{itemize}
  \item Use signed Agent Cards to verify agent identity
  \item Validate agent capabilities before collaboration
  \item Implement rate limiting between agents
  \item Audit all agent-to-agent communications
\end{itemize}
\end{cautionbox}
```

---

## Emerging Protocol Landscape

Beyond MCP and A2A, other protocols are emerging:

| Protocol | Source | Focus |
|----------|--------|-------|
| ACP (Agent Communication Protocol) | IBM/Linux Foundation | Agent communication |
| OASF (Open Agentic Schema Framework) | Community | Schema standardization |
| ANP (Agent Network Protocol) | Community | Agent networking |
| AG-UI (Agent-User Interaction) | Community | Agent-user interface |
| Agent Rules (AGENTS.md) | Community | Agent behavior standards |

**Recommendation**: Focus on MCP and A2A as primary protocols; monitor others for potential adoption.

---

## Proposed LaTeX Content

```latex
\subsection{MCP vs. A2A: Complementary Protocols}
\label{sec:agents2-proto-comparison}

Two protocols have emerged as standards for agent interoperability as of late 2025: Anthropic's Model Context Protocol (MCP) and Google's Agent-to-Agent Protocol (A2A). They serve complementary purposes.

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
  \item \textbf{MCP}: Connecting agents to tools, databases, and external services. Use for document management integration, research platform APIs, and structured data access.
  \item \textbf{A2A}: Enabling collaboration between multiple agents. Use for orchestrated workflows where specialized agents hand off work to each other.
\end{itemize}

\paragraph{Dual Protocol Strategy.} Production legal AI systems typically require both:
\begin{itemize}
  \item MCP for tool integration (Westlaw API, document management, case management)
  \item A2A for multi-agent coordination (research agent $\rightarrow$ drafting agent $\rightarrow$ review agent)
\end{itemize}

\begin{cautionbox}[title={Protocol Security}]
MCP security issues were identified in April--July 2025: prompt injection, file exfiltration risks, and authentication gaps on exposed servers. Legal AI deployments must:
\begin{itemize}
  \item Authenticate all MCP endpoints
  \item Validate tool permissions carefully
  \item Never expose MCP servers to untrusted networks
  \item Use signed Agent Cards in A2A deployments
\end{itemize}
\end{cautionbox}
```

---

## BibLaTeX Entries

```bibtex
@online{anthropic-mcp,
  author       = {{Anthropic}},
  title        = {Introducing the Model Context Protocol},
  year         = {2024},
  month        = nov,
  url          = {https://www.anthropic.com/news/model-context-protocol},
  urldate      = {2025-11-27},
  note         = {Open standard for connecting AI systems to data sources; pre-built servers for Google Drive, Slack, GitHub, Postgres; SDKs for Python, TypeScript, C\#}
}

@online{google-a2a,
  author       = {{Google Developers}},
  title        = {Announcing the Agent2Agent Protocol ({A2A})},
  year         = {2025},
  month        = apr,
  url          = {https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/},
  urldate      = {2025-11-27},
  note         = {Open protocol for agent-to-agent communication using JSON-RPC 2.0 over HTTP; donated to Linux Foundation; features Agent Cards for capability discovery; 50+ launch partners}
}

@online{a2a-spec,
  title        = {Agent2Agent Protocol Specification},
  year         = {2025},
  url          = {https://a2a-protocol.org/latest/},
  institution  = {Linux Foundation},
  urldate      = {2025-11-27},
  note         = {Official specification for A2A protocol; supports HTTP, SSE, gRPC transports; security card signing added November 2025}
}

@online{mcp-spec,
  title        = {Model Context Protocol Specification},
  year         = {2025},
  url          = {https://modelcontextprotocol.io/},
  urldate      = {2025-11-27},
  note         = {Official MCP documentation and specification; server and client SDKs; community server directory}
}
```
