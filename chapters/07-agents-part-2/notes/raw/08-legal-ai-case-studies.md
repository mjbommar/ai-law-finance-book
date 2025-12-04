# Legal AI Case Studies

**Generated**: November 27, 2025
**Purpose**: Real-world examples of legal AI agents for Chapter 07

---

## Overview

This document provides detailed case studies of legal AI agents in production as of November 2025. These examples ground abstract architecture concepts in practice.

---

## Case Study 1: Harvey AI

### Company Overview

| Attribute | Value |
|-----------|-------|
| Founded | 2022 |
| Valuation | $8B (October 2025), up from $5B (June 2025) |
| ARR | $100M+ (August 2025) |
| Clients | 700+ in 63 countries |
| Law Firm Adoption | Majority of top 10 US law firms |

### Timeline

| Date | Milestone |
|------|-----------|
| 2022 | Founded |
| 2023 | Initial product launch |
| Mar 2025 | Agentic workflows announced |
| Apr 2025 | A&O Shearman partnership for agentic deployment |
| Jun 2025 | Series E ($300M at $5B); Deep Research for Legal launched |
| Aug 2025 | Reached $100M ARR |
| Oct 2025 | Valuation reaches $8B |

### Architecture Patterns

#### 1. Agentic Workflows (March 2025)

**Description**: Multi-step agents that plan, adapt, and interact to complete complex legal tasks.

**Key Features**:
- **Planning**: Agent decomposes complex tasks into steps
- **Adaptation**: Agent adjusts approach based on intermediate results
- **Interaction**: Agent engages with tools and users throughout workflow

**GPA+IAT Mapping**:
| Property | Implementation |
|----------|----------------|
| Goal | Task specification from user |
| Perception | Document understanding, research results |
| Action | Tool invocation, document generation |
| Iteration | Multi-step workflow execution |
| Adaptation | Strategy adjustment based on findings |
| Termination | Goal completion or human escalation |

#### 2. Deep Research for Legal (June 2025)

**Description**: Combines OpenAI's Deep Research API with Harvey's legal-specific processing.

**Workflow**:
1. **Planning**: Creates research strategy based on legal question
2. **Execution**: Iteratively searches legal databases, analyzes results
3. **Synthesis**: Produces grounded reports with citations
4. **Verification**: Cross-references findings, flags conflicts

**Key Differentiator**: Legal-specific reasoning layer that understands jurisdiction, authority hierarchy, and citation conventions.

#### 3. Custom Evaluation

**Description**: Harvey evaluates agent outputs by comparison to human lawyer work product.

**Approach**:
- Uses actual legal work as gold standard
- Evaluates not just accuracy but legal reasoning quality
- Domain experts review agent outputs
- Continuous improvement based on evaluation feedback

**Relevance to Chapter 07**: Demonstrates importance of domain-specific evaluation beyond generic benchmarks.

### A&O Shearman Deployment (April 2025)

**Partnership**: Allen & Overy Shearman (major global law firm) deployed Harvey agents for complex legal workflows.

**Use Cases**:

| Use Case | Description | Agent Capabilities |
|----------|-------------|-------------------|
| Antitrust Filing Analysis | Review merger filings for competition issues | Document analysis, regulatory knowledge, issue spotting |
| Cybersecurity Incident Assessment | Evaluate breach scenarios, notification requirements | Multi-jurisdiction knowledge, timeline analysis |
| Fund Formation Review | Analyze fund documents for compliance | Regulatory framework knowledge, term comparison |
| Loan Document Analysis | Review credit agreements, identify risks | Contract analysis, covenant tracking |

**Implementation Characteristics**:
- Multi-step reasoning with transparency at each step
- Human review at critical decision points
- Integration with firm's document management systems
- Audit trails for all agent actions

### Key Takeaways for Chapter 07

1. **Custom evaluation matters**: Generic benchmarks insufficient for legal AI
2. **Multi-step workflows**: Complex legal tasks require iteration and adaptation
3. **Domain expertise**: Legal-specific reasoning layer essential
4. **Human oversight**: Critical decision points require human review
5. **Enterprise integration**: Must work with existing firm systems

---

## Case Study 2: Thomson Reuters CoCounsel

### Company Overview

| Attribute | Value |
|-----------|-------|
| Parent | Thomson Reuters (legal information giant) |
| Product | CoCounsel Legal (August 2025) |
| Prior Product | CoCounsel (2023-2025, evolved into CoCounsel Legal) |
| Adoption | 20,000+ law firms and legal departments |
| Market Position | Am Law 100 majority; 100% Fortune 100; 97% Fortune 1000 |

### Timeline

| Date | Milestone |
|------|-----------|
| 2023 | CoCounsel initial launch |
| 2024 | Continued development and adoption |
| Aug 5, 2025 | CoCounsel Legal launch with Deep Research |
| Nov 2025 | Beta features announced for early 2026 |

### Architecture Patterns

#### 1. Deep Research (August 2025)

**Description**: Professional-grade agentic AI research creating research plans, executing iteratively, and delivering reports grounded in authoritative content.

**Workflow**:
```
1. Research Planning
   └─ Analyze question → Identify research strategy → Create plan

2. Iterative Execution
   └─ Search Westlaw → Analyze results → Refine search → Repeat
   └─ Search Practical Law → Cross-reference → Synthesize

3. Report Delivery
   └─ Compile findings → Cite sources → Structure report
   └─ Ground all claims in authoritative content
```

**Key Differentiator**: Integration with Westlaw and Practical Law provides authoritative, curated legal content.

#### 2. Authoritative Content Integration

**Content Sources**:
- **Westlaw**: Primary and secondary legal sources, case law, statutes, regulations
- **Practical Law**: Practice notes, standard documents, how-to guides

**Architecture Implication**: Agent retrieval layer connects to premium legal databases, not just general web content.

**Trust Model**: Content from Westlaw/Practical Law has editorial oversight and authority validation.

#### 3. Guided Workflows

**Description**: Structured processes for high-friction legal work.

**Examples**:
- Contract review workflows with defined stages
- Due diligence checklists with automated document gathering
- Research workflows with jurisdiction-specific paths

**GPA+IAT Mapping**:
| Property | Implementation |
|----------|----------------|
| Goal | Workflow completion (predefined stages) |
| Perception | Document ingestion, database search results |
| Action | Document analysis, summary generation, flagging |
| Iteration | Progress through workflow stages |
| Adaptation | Branch based on document type, issue detection |
| Termination | Workflow completion, human review point, escalation |

### Beta Features (November 2025, Early 2026 Release)

**Announced Features**:

| Feature | Description | Significance |
|---------|-------------|--------------|
| Independent Complex Task Execution | Agents execute complex tasks independently | Higher autonomy level |
| Customizable Workflow Plans | Users create and share workflow templates | Personalization + knowledge sharing |
| Bulk Document Review | Process 10,000+ documents in single workflow | Scale demonstration |

**Bulk Review Architecture**:
- Process thousands of documents in parallel
- Consistent application of review criteria
- Aggregate findings across document set
- Human review of agent-flagged issues

### Market Position Advantages

| Advantage | Implication for Architecture |
|-----------|------------------------------|
| Existing Westlaw infrastructure | Proven retrieval at legal scale |
| Editorial quality assurance | Authoritative content trust |
| Enterprise relationships | Security and compliance maturity |
| Practice Law templates | Structured workflow foundation |

### Key Takeaways for Chapter 07

1. **Content authority matters**: Integration with authoritative sources (Westlaw) differentiates from generic RAG
2. **Scale requirements**: Legal AI must handle thousands of documents
3. **Workflow structure**: Guided workflows reduce risk while enabling agentic capabilities
4. **Enterprise maturity**: Security, compliance, and integration with existing systems essential
5. **Customization**: Users need ability to adapt workflows to their practice

---

## Comparison: Harvey vs. CoCounsel

| Aspect | Harvey | CoCounsel |
|--------|--------|-----------|
| Origin | AI-native startup | Legal information incumbent |
| Content | Uses OpenAI + custom legal layer | Integrates Westlaw, Practical Law |
| Evaluation | Custom vs. human lawyers | Integration with existing quality metrics |
| Autonomy | Higher (agentic workflows) | Moderate (guided workflows evolving to higher) |
| Enterprise Integration | Growing | Established |
| Security Model | Startup security practices | Enterprise security heritage |

---

## Common Patterns Across Legal AI Agents

### 1. Multi-Step Reasoning

Both Harvey and CoCounsel implement multi-step workflows:
- Planning phase before execution
- Iterative execution with intermediate results
- Synthesis and report generation
- Human review integration

### 2. Domain-Specific Knowledge

Legal AI agents require:
- Understanding of legal authority hierarchy
- Jurisdiction-specific reasoning
- Citation format and conventions
- Temporal validity (superseded law, overruled cases)

### 3. Authoritative Content Integration

Successful legal AI agents integrate with:
- Primary legal sources (statutes, cases, regulations)
- Secondary sources (treatises, practice guides)
- Curated, editorially reviewed content
- Current and historical versions

### 4. Human-in-the-Loop

Both implement human oversight:
- Critical decision points require human approval
- Escalation paths for uncertain situations
- Audit trails for all agent actions
- Ability to override agent recommendations

### 5. Custom Evaluation

Generic benchmarks insufficient:
- Evaluate against human lawyer work product
- Domain experts review quality
- Legal-specific metrics (citation accuracy, authority hierarchy)
- Continuous improvement loops

---

## Proposed LaTeX Content

```latex
\subsection{Case Studies: Legal AI Agents in Production}
\label{sec:agents2-case-studies}

Two leading legal AI platforms demonstrate how the architectural patterns in this chapter manifest in production systems.

\paragraph{Harvey AI.} Harvey demonstrates multi-step agentic workflows for complex legal tasks. Reaching \$100M ARR by August 2025 and serving the majority of top 10 US law firms, Harvey exemplifies AI-native legal agent architecture.

Key patterns:
\begin{itemize}
  \item \textbf{Deep Research}: Combines LLM reasoning with legal-specific processing to plan research strategies, execute iteratively, and deliver grounded reports
  \item \textbf{Custom evaluation}: Compares agent outputs to human lawyer work product, not generic benchmarks
  \item \textbf{Multi-step transparency}: Each step in agentic workflows is visible and subject to human review
\end{itemize}

Harvey's April 2025 deployment with A\&O Shearman covered antitrust filing analysis, cybersecurity incident assessment, fund formation review, and loan document analysis---demonstrating breadth of legal agent applications.

\paragraph{Thomson Reuters CoCounsel.} CoCounsel Legal (August 2025) demonstrates integration of agentic AI with authoritative legal content infrastructure:

Key patterns:
\begin{itemize}
  \item \textbf{Authoritative retrieval}: Agent retrieval layer connects to Westlaw and Practical Law, providing curated, editorially reviewed content
  \item \textbf{Guided workflows}: Structured processes reduce risk while enabling agentic capabilities
  \item \textbf{Scale}: Beta features (November 2025) include bulk review of 10,000+ documents
\end{itemize}

Adoption metrics---majority of Am Law 100, 100\% of Fortune 100---demonstrate enterprise-scale deployment.

\paragraph{Common Patterns.} Across successful legal AI agents:
\begin{enumerate}
  \item Multi-step reasoning with transparency at each step
  \item Integration with authoritative content sources (not just web search)
  \item Human-in-the-loop approval for high-stakes decisions
  \item Domain-specific evaluation against human expert work product
  \item Enterprise-scale document processing capabilities
\end{enumerate}

These patterns inform the architectural and evaluation guidance throughout this chapter.
```

---

## Additional Examples (Brief)

### Ironclad (Contract Lifecycle Management)

- AI agents for contract drafting, review, and negotiation
- Integration with contract repository
- Workflow automation for approval processes

### Luminance (Document Review)

- AI-powered document analysis for due diligence
- Multi-language support
- M&A and litigation support

### Kira Systems (Contract Analysis)

- Machine learning for contract review
- Training on firm-specific precedents
- Integration with document management

### Relativity (e-Discovery)

- AI-assisted document review for litigation
- Predictive coding and TAR
- Large-scale document processing

---

## References

- Harvey AI Agentic Workflows: https://www.artificiallawyer.com/2025/03/17/harvey-to-roll-out-agentic-workflows/
- A&O Shearman Partnership: https://www.aoshearman.com/en/news/ao-shearman-and-harvey-to-roll-out-agentic-ai-agents-targeting-complex-legal-workflows
- Harvey Series E: https://fortune.com/2025/06/23/harvey-raises-300-million-at-5-billion-valuation-to-be-legal-ai-for-lawyers-worldwide/
- CoCounsel Legal Launch: https://legaltechnology.com/2025/08/05/thomson-reuters-launches-cocounsel-legal-with-agentic-ai-and-deep-research-capabilities/
- CoCounsel Beta Features: https://www.law.com/legaltechnews/2025/11/05/thomson-reuters-announces-upcoming-agentic-ai-features-for-cocounsel-legal/
