# Research Notes: Further Learning (Section 07)

**Date**: November 27, 2025
**Researcher**: Claude Code
**Section**: 07-further-learning.tex

## Section Overview

This section provides resources for continued learning about agent architectures, protocols, and evaluation. It includes framework selection criteria, protocol specifications (MCP and A2A), academic research, security resources, regulatory guidance across jurisdictions, and community learning resources. The research validates and expands the current content with verified URLs and latest developments through November 2025.

---

## Agent Framework Landscape (2025)

### Current Leading Frameworks

**LangGraph (LangChain)**
- Graph-based state machines for stateful, multi-actor applications
- Cyclical graphs with nodes representing reasoning/tool-use steps
- Best for: Complex, stateful workflows with branching logic
- Official: https://langchain.com/ (part of LangChain ecosystem)
- **Source**: [Turing AI Agent Frameworks Comparison](https://www.turing.com/resources/ai-agent-frameworks)

**LlamaIndex**
- Originally RAG-focused, now broader agent platform
- Strong document ingestion, indexing, and querying capabilities
- Best for: Document-grounded agents, knowledge retrieval
- Official: https://www.llamaindex.ai/
- **Source**: [Langfuse AI Agent Comparison](https://langfuse.com/blog/2025-03-19-ai-agent-comparison)

**CrewAI**
- Role-based multi-agent coordination
- Emphasizes teams, tasks, and collaboration protocols
- Opinionated framework, simpler to start, harder to customize
- Best for: Multi-agent collaboration, enterprise orchestration
- Official: https://www.crewai.com/
- **Source**: [DataCamp CrewAI vs LangGraph vs AutoGen](https://www.datacamp.com/tutorial/crewai-vs-langgraph-vs-autogen)

**Microsoft AutoGen**
- Conversation-based multi-agent framework
- Agents interact via structured natural language messages
- Group chat-style collaboration logic
- Best for: Research, flexible multi-agent dialogues
- Official: https://microsoft.github.io/autogen/
- **Source**: [Codecademy Top AI Agent Frameworks](https://www.codecademy.com/article/top-ai-agent-frameworks-in-2025)

**OpenAI Swarm** (experimental)
- Lightweight multi-agent orchestration
- Part of OpenAI ecosystem
- **Source**: [Nuvi Blog: Framework Comparison](https://www.nuvi.dev/blog/ai-agent-framework-comparison-langgraph-crewai-openai-swarm)

### Framework Selection Strategy

**Hybrid Approaches Recommended**: Teams often combine frameworks (e.g., LangChain for workflows, LlamaIndex for knowledge management, LangGraph for orchestration)

**Key Evaluation Factors**:
1. Core capabilities alignment
2. RAG/data integration requirements
3. Enterprise/production considerations
4. Protocol support (MCP, A2A)
5. Community maturity and documentation
6. Licensing and vendor lock-in risk

**Framework Churn**: The landscape is immature and rapidly evolving. Favor frameworks with strong protocol support (MCP, A2A) to reduce lock-in.

---

## Protocol Specifications

### Model Context Protocol (MCP)

**Official Specification**: https://modelcontextprotocol.io/

**Overview**: Open standard for connecting LLM applications to data sources and tools. Introduced by Anthropic in November 2024.

**November 2025 Specification Update** (First Anniversary):
- **Tasks**: New abstraction for tracking work performed by MCP servers with status queries
- **URL-based Client Registration**: OAuth Client ID Metadata Documents for simpler authorization
- **Security Improvements**: Client security requirements for local server installation, enterprise IdP policy controls, OAuth client credentials for machine-to-machine auth
- **MCP Apps Extension (SEP-1865)**: Standardized support for interactive user interfaces
- **Source**: [MCP One Year Anniversary Blog](http://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/)

**Industry Adoption**:
- OpenAI officially adopted MCP in March 2025 (ChatGPT desktop, Agents SDK, Responses API)
- Google, Microsoft, SAP, Oracle, Docker announced support
- GitHub: https://github.com/modelcontextprotocol
- **Sources**:
  - [Anthropic MCP Announcement](https://www.anthropic.com/news/model-context-protocol)
  - [Techzine MCP First Anniversary](https://www.techzine.eu/news/infrastructure/136758/model-context-protocol-receives-major-update-on-its-first-anniversary/)
  - [Descope MCP Guide](https://www.descope.com/learn/post/mcp)

**Technical Details**:
- Re-uses Language Server Protocol (LSP) message-flow ideas
- Transport: JSON-RPC 2.0 over stdio and HTTP (with optional SSE)
- **Source**: [Wikipedia: Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol)

### Agent-to-Agent Protocol (A2A)

**Official Specification**: https://a2a-protocol.org/latest/

**Overview**: Open protocol for standardized multi-agent communication and orchestration.

**Linux Foundation Governance** (June 23, 2025):
- Originally developed by Google (April 2025)
- Donated to Linux Foundation at Open Source Summit North America (Denver)
- Founding members: AWS, Cisco, Google, Microsoft, Salesforce, SAP, ServiceNow
- 100+ supporting companies
- Vendor-neutral governance under Linux Foundation
- **Sources**:
  - [Linux Foundation Press Release](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)
  - [Google Cloud Blog](https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/)

**Technical Details**:
- Transport: HTTPS with JSON-RPC 2.0
- Authentication: OAuth 2.0, OpenID Connect, mTLS
- Agent Cards: Self-description format for capabilities
- Two agent types: client and remote
- **Sources**:
  - [IBM A2A Overview](https://www.ibm.com/think/topics/agent2agent-protocol)
  - [AWS Open Source Blog: A2A](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/)

**Relationship with MCP**: A2A focuses on agent-to-agent communication; MCP focuses on agent-to-tool connections. Both are complementary and can be used together.

**GitHub**: https://github.com/a2aproject/A2A

---

## Research and Academic Resources

### Foundational Papers

**ReAct: Synergizing Reasoning and Acting in Language Models**
- Authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- Date: October 6, 2022
- arXiv: https://arxiv.org/abs/2210.03629
- Project: https://react-lm.github.io/
- Key contribution: Interleaving reasoning traces with task-specific actions
- Results: Overcomes hallucination on HotPotQA/Fever via Wikipedia API; outperforms baselines on ALFWorld (34% improvement) and WebShop (10% improvement)
- **Source**: [arXiv 2210.03629](https://arxiv.org/abs/2210.03629)

**Toolformer: Language Models Can Teach Themselves to Use Tools**
- Authors: Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- Date: February 9, 2023
- arXiv: https://arxiv.org/abs/2302.04761
- Venue: NeurIPS 2023
- Key contribution: Self-supervised learning to use external APIs (calculator, QA, search, translation, calendar)
- **Source**: [arXiv 2302.04761](https://arxiv.org/abs/2302.04761)

**Tree of Thoughts: Deliberate Problem Solving with Large Language Models**
- Authors: Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
- Date: May 17, 2023 (revised December 3, 2023)
- arXiv: https://arxiv.org/abs/2305.10601
- GitHub: https://github.com/princeton-nlp/tree-of-thought-llm
- Venue: NeurIPS 2023
- Key contribution: Deliberate decision-making via exploration over reasoning paths with lookahead and backtracking
- Results: Game of 24 success rate: 74% (ToT) vs 4% (GPT-4 with CoT)
- **Source**: [arXiv 2305.10601](https://arxiv.org/abs/2305.10601)

**Reflexion: Language Agents with Verbal Reinforcement Learning**
- Authors: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- Date: March 20, 2023
- arXiv: https://arxiv.org/abs/2303.11366
- GitHub: https://github.com/noahshinn/reflexion
- Venue: NeurIPS 2023
- Key contribution: Verbal reinforcement (self-reflection) via episodic memory instead of weight updates
- Results: 91% pass@1 on HumanEval (vs 80% for GPT-4 baseline)
- **Source**: [arXiv 2303.11366](https://arxiv.org/abs/2303.11366)

**The Rise and Potential of Large Language Model Based Agents** (Xi et al., 2023)
- Already cited in chapter: \parencite{xi2023rise}
- Comprehensive survey of LLM-based agents

### Agent Benchmarks

**SWE-bench: Software Engineering Tasks**
- Official: https://www.swebench.com/
- GitHub: https://github.com/SWE-bench/SWE-bench
- Overview: 2,294 real-world GitHub issues from Python repos
- Accepted: ICLR 2024 (oral presentation)
- Variants:
  - SWE-bench Full (2,294 tasks)
  - SWE-bench Lite (300 tasks, subset for cheaper evaluation)
  - SWE-bench Verified (500 human-validated tasks, collaboration with OpenAI)
  - SWE-bench Multimodal (517 tasks with visual elements)
  - SWE-bench-Live (1,319 post-2024 tasks, contamination-free)
- Current SOTA (January 2025): 20% Full, 43% Lite, 45% Verified
- **Sources**:
  - [SWE-bench Leaderboard](https://www.swebench.com/)
  - [OpenAI SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)
  - [GitHub SWE-bench](https://github.com/SWE-bench/SWE-bench)

**WebArena: Web Navigation Tasks**
- Official: https://webarena.dev/
- GitHub: https://github.com/web-arena-x/webarena
- Overview: 812 long-horizon tasks across 4 self-hosted web domains (e-commerce, forums, GitLab, CMS)
- Average 3.3 variations per template (241 templates)
- Human performance: 78.24%; GPT-4-based agent: 14.41%
- Current record: 61.7% (IBM CUGA, single-agent)
- Related: VisualWebArena (multimodal extension)
- **Sources**:
  - [WebArena Project](https://webarena.dev/)
  - [arXiv WebArena](https://arxiv.org/html/2307.13854v4)
  - [Jace AI Blog: WebArena Performance](https://jace.ai/blog/awa-1-5-achieves-breakthrough-performance-on-web-arena-benchmark)

**GAIA: General AI Assistants**
- Hugging Face: https://huggingface.co/gaia-benchmark
- Leaderboard: https://huggingface.co/spaces/gaia-benchmark/leaderboard
- arXiv: https://arxiv.org/abs/2311.12983
- Overview: 466 real-world questions requiring reasoning, multi-modality, web browsing, tool-use
- 3 difficulty levels (Level 1: <5 steps; Level 2: 5-10 steps; Level 3: complex planning)
- Human performance: 92%; GPT-4 with plugins: 15%
- Public test set: 166 questions (300 answers held out for leaderboard)
- **Sources**:
  - [GAIA Benchmark on Hugging Face](https://huggingface.co/gaia-benchmark)
  - [arXiv 2311.12983](https://arxiv.org/abs/2311.12983)
  - [Meta AI Research: GAIA](https://ai.meta.com/research/publications/gaia-a-benchmark-for-general-ai-assistants/)

**AgentBench: Multi-Domain Evaluation**
- GitHub: https://github.com/THUDM/AgentBench
- arXiv: https://arxiv.org/abs/2308.03688
- Venue: ICLR 2024
- Overview: 8 diverse environments (web shopping, academic search, database, OS, etc.)
- 5-50 turns per task, multi-turn interacting challenges
- 29 LLMs evaluated (API-based and open-source)
- Key finding: Top commercial LLMs strong; significant gap to OSS models (≤70B)
- **Sources**:
  - [arXiv 2308.03688](https://arxiv.org/abs/2308.03688)
  - [GitHub THUDM/AgentBench](https://github.com/THUDM/AgentBench)

---

## Security Resources

### OWASP LLM Top 10 (2025)

**Official**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
**Gen AI Security Project**: https://genai.owasp.org/

**The 2025 Top 10 Risks**:
1. **Prompt Injection** (consistently #1 since 2023)
2. **Sensitive Information Disclosure**
3. **Supply Chain Vulnerabilities**
4. **Data and Model Poisoning**
5. **Improper Output Handling**
6. **Excessive Agency** (granting LLMs unchecked autonomy)
7. **System Prompt Leakage**
8. **Vector and Embedding Weaknesses** (53% of companies use RAG/Agentic pipelines)
9. **Misinformation**
10. **Unbounded Consumption** (DoS, financial exploitation)

**Agentic AI Focus**: The project now explicitly covers agentic AI systems and AI-driven applications, recognizing the unique security challenges of autonomous agents.

**Sources**:
- [OWASP Gen AI Security](https://genai.owasp.org/llm-top-10/)
- [Confident AI: OWASP 2025](https://www.confident-ai.com/blog/owasp-top-10-2025-for-llm-applications-risks-and-mitigation-techniques)
- [DeepStrike: OWASP LLM 2025](https://deepstrike.io/blog/owasp-llm-top-10-vulnerabilities-2025)

### MCP Security Vulnerabilities

**CVE-2025-32711 (EchoLeak)**:
- Severity: CVSS 9.3 (critical)
- Affected: Microsoft 365 Copilot
- Type: Zero-click AI vulnerability (indirect prompt injection)
- Discovery: Aim Security
- Mechanism: Attacker sends crafted email; Copilot accesses internal data without user interaction; data exfiltrated via image URL
- Patch: June 2025 (Microsoft backend fix, no customer action required)
- No evidence of in-the-wild exploitation
- **Sources**:
  - [NVD CVE-2025-32711](https://nvd.nist.gov/vuln/detail/cve-2025-32711)
  - [Hack The Box: EchoLeak](https://www.hackthebox.com/blog/cve-2025-32711-echoleak-copilot-vulnerability)
  - [The Hacker News: Zero-Click AI Vulnerability](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html)

**MCP Prompt Injection and Tool Poisoning**:
- CyberArk disclosed Full-Schema Poisoning (FSP) attack
- MCP's "optimistic trust model" equates syntactic correctness to semantic safety
- Cato Networks PoC (June 2025): Data leakage via Atlassian MCP through Jira tickets
- Cursor flaw: RCE risk from prompt injections on MCP server
- **Sources**:
  - [Practical DevSecOps: MCP Security](https://www.practical-devsecops.com/mcp-security-vulnerabilities/)
  - [SC Media: Cursor Flaw](https://www.scworld.com/news/cursor-flaw-risks-rce-from-prompt-injections-on-mcp-server-researchers-say)

### Additional Security Standards

**Zero Trust for AI Agents**: Emerging frameworks applying zero trust architecture (verify every request, least privilege, continuous monitoring)

**Security Scoping Matrices**: Frameworks categorizing agents by connectivity (isolated/internal/internet) and autonomy (human-in-loop/supervised/autonomous) to determine controls

**Industry Research**: Ongoing tracking of AI/agent attack patterns by security research organizations

---

## Regulatory Resources

### EU AI Act

**Official EUR-Lex**: https://eur-lex.europa.eu/eli/reg/2024/1689/oj

**Official Title**: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024

**Digital Strategy Page**: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

**Implementation Timeline Page**: https://artificialintelligenceact.eu/implementation-timeline/

**Timeline**:
- Entered into force: August 1, 2024
- Prohibited AI practices: February 2, 2025
- GPAI model obligations: August 2, 2025
- Full applicability: August 2, 2026
- High-risk AI in regulated products: August 2, 2027

**Governance Bodies** (active from August 2, 2025):
- National competent authorities (enforcement)
- AI Office (European Commission) - coordinates rules, regulates GPAI models
- AI Board (Member States representatives)
- Scientific panel of independent experts
- Advisory forum for stakeholders

**2025 Implementation Documents**:
- Commission Implementing Regulation (EU) 2025/454 (March 7, 2025): Scientific panel rules
- Guidelines on prohibited AI practices (February 4, 2025)
- Guidelines on AI system definition (February 6, 2025)
- Draft GPAI guidelines (July 18, 2025)
- Preliminary GPAI provider obligations (April 22, 2025)

**Sources**:
- [EUR-Lex AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [EUR-Lex Summary](https://eur-lex.europa.eu/EN/legal-content/summary/rules-for-trustworthy-artificial-intelligence-in-the-eu.html)
- [AI Act Hub](https://artificialintelligenceact.eu/the-act/)

### US Regulatory Framework

#### General AI Governance

**NIST AI RMF**: https://www.nist.gov/itl/ai-risk-management-framework
- Framework Version 1.0: Released January 26, 2023
- Generative AI Profile (NIST-AI-600-1): Released July 26, 2024
- Four functions: Govern, Map, Measure, Manage
- Voluntary but increasingly referenced by regulators
- Next review expected by 2028
- **Sources**:
  - [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
  - [NIST AI RMF Publication](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)

**Executive Order 14110**: Safe, Secure, and Trustworthy Development of AI (October 2023)

**State Legislation**:
- Colorado AI Act (SB 24-205)
- California AI bills (evolving)

#### Financial Sector

**SEC**:
- Investment adviser AI guidance
- Form ADV disclosure requirements
- 2025 Examination Priorities: AI policies, procedures, disclosure
- Focus: AI in portfolio management, trading, marketing, compliance
- **Sources**:
  - [SEC Form ADV Data](https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data)
  - [Comply: Form ADV 2025 Guide](https://www.comply.com/resource/form-adv-part-2b-brochure-supplement-2025-compliance-guide-for-ria-firms/)

**FINRA**:
- Regulatory Notice 24-09 (June 27, 2024): AI tools subject to existing rules
- Key rules: FINRA 2210 (Communications), 3110 (Supervision)
- 2024 Annual Regulatory Oversight Report: AI section
- Technology-neutral regulatory approach
- Third-party AI tools covered
- **Sources**:
  - [FINRA Regulatory Notice 24-09](https://www.finra.org/rules-guidance/notices/24-09)
  - [FINRA 2024 Report](https://www.finra.org/rules-guidance/guidance/reports/2024-finra-annual-regulatory-oversight-report)
  - [Stradley: FINRA AI Guidance](https://www.stradley.com/insights/publications/2024/07/broker-dealer-ai-july-16-2024)

**OCC/Federal Reserve**: SR 11-7 model risk management (applies to AI)

**CFTC**: Proposed rules on AI in derivatives trading

#### Legal Profession

**ABA Formal Opinion 512** (July 29, 2024):
- Title: "Generative Artificial Intelligence Tools"
- PDF: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
- Key obligations:
  - Competence (Rule 1.1): Understand AI capacity/limitations
  - Confidentiality: Protect client information in AI tools
  - Fees (Rule 1.5): Cannot charge for general AI learning
  - Independent verification: Address hallucination risks
  - Supervisory responsibilities: Governance programs required
- **Sources**:
  - [ABA News: Ethics Guidance](https://www.americanbar.org/news/abanews/aba-news-archives/2024/07/aba-issues-first-ethics-guidance-ai-tools/)
  - [ABA Formal Opinion 512](https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf)

**State Bar Guidance**: California, New York, Florida have issued guidance

**Court Rules**: Growing number of jurisdictions require AI disclosure in filings

### Other Jurisdictions

#### United Kingdom

**AI Safety Institute** (rebranded AI Security Institute, February 2025):
- Focus: National security, misuse risks, frontier model evaluation
- Standards: ISO/IEC 42001

**FCA (Financial Conduct Authority)**:
- AI Lab: Insights, discussions, case studies
- AI Live Testing initiative (summer 2025): 12-month pilot for customer-facing AI
- Collaboration with Nvidia for Digital Sandbox
- No single AI law; context-specific, risk-based regulation
- Potential AI Bill in 2026
- **Sources**:
  - [FCA AI Update](https://www.fca.org.uk/publication/corporate/ai-update.pdf)
  - [FCA AI Approach](https://www.fca.org.uk/firms/innovation/ai-approach)
  - [Bank of England AI Report 2024](https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024)

**PRA (Prudential Regulation Authority)**: Financial services AI oversight

**Third-Party Designation**: FCA proposed key AI providers as critical third parties for operational resilience

#### Canada

**Artificial Intelligence and Data Act (AIDA)**: Pending as part of Bill C-27

#### Singapore

**MAS AI Risk Management Guidelines** (Consultation: November 13, 2025):
- Consultation closes: January 31, 2026
- Scope: All financial institutions
- Covers: Generative AI, AI agents
- Key areas: Governance, oversight, life cycle controls, capabilities
- Proportionate approach based on FI size and risk profile
- Complements FEAT principles (Fairness, Ethics, Accountability, Transparency)
- **Sources**:
  - [MAS Consultation Paper](https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management)
  - [MAS Media Release](https://www.mas.gov.sg/news/media-releases/2025/mas-guidelines-for-artificial-intelligence-risk-management)

**Model AI Governance Framework**: IMDA national framework

**AI Verify Foundation**: Global AI Assurance Pilot (February 2025)

#### China

**Interim Measures for Generative AI Services** (2023)

**Sector-specific requirements**: Various industry regulations

---

## Community and Learning Resources

### Learning Approaches

**Protocol-First Learning**: Start with MCP and A2A specifications before framework-specific tutorials for transferable knowledge

**Benchmark-Driven Practice**: Implement SWE-bench, WebArena, or GAIA tasks for practical experience with real evaluation criteria

**Open-Source Study**: Review open-source implementations on GitHub; focus on architecture patterns over library calls

**Incremental Complexity**:
1. Single-tool agents
2. Add memory
3. Multi-step reasoning
4. Multi-agent orchestration

### Professional Communities

**Domain-Specific**: Legal AI, FinTech, healthcare AI groups discuss agent applications with domain constraints

**Open-Source Framework Communities**: Discussion forums for LangChain, LlamaIndex, CrewAI, AutoGen, etc.

**Research Communities**: NeurIPS, ACL, ICLR increasingly feature agent tracks

**Protocol Working Groups**: Participate in MCP and A2A specification development

### Evaluation Criteria for Learning Resources

Prioritize resources that:
1. Focus on transferable patterns over framework-specific APIs
2. Address security and evaluation rigorously
3. Include regulatory and compliance considerations
4. Provide hands-on exercises with measurable outcomes
5. Acknowledge limitations and failure modes

---

## References and Sources

### Agent Frameworks
- [Turing: AI Agent Frameworks Comparison 2025](https://www.turing.com/resources/ai-agent-frameworks)
- [Langfuse: Comparing Open-Source AI Agent Frameworks](https://langfuse.com/blog/2025-03-19-ai-agent-comparison)
- [DataCamp: CrewAI vs LangGraph vs AutoGen](https://www.datacamp.com/tutorial/crewai-vs-langgraph-vs-autogen)
- [Codecademy: Top AI Agent Frameworks in 2025](https://www.codecademy.com/article/top-ai-agent-frameworks-in-2025)

### Protocols
- [Anthropic: Model Context Protocol Announcement](https://www.anthropic.com/news/model-context-protocol)
- [MCP Blog: One Year Anniversary](http://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/)
- [Linux Foundation: A2A Launch](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)
- [IBM: Agent2Agent Protocol](https://www.ibm.com/think/topics/agent2agent-protocol)

### Research Papers
- [arXiv: ReAct (2210.03629)](https://arxiv.org/abs/2210.03629)
- [arXiv: Toolformer (2302.04761)](https://arxiv.org/abs/2302.04761)
- [arXiv: Tree of Thoughts (2305.10601)](https://arxiv.org/abs/2305.10601)
- [arXiv: Reflexion (2303.11366)](https://arxiv.org/abs/2303.11366)
- [arXiv: AgentBench (2308.03688)](https://arxiv.org/abs/2308.03688)

### Benchmarks
- [SWE-bench](https://www.swebench.com/)
- [WebArena](https://webarena.dev/)
- [GAIA on Hugging Face](https://huggingface.co/gaia-benchmark)
- [AgentBench GitHub](https://github.com/THUDM/AgentBench)

### Security
- [OWASP Gen AI Security Project](https://genai.owasp.org/)
- [NVD: CVE-2025-32711](https://nvd.nist.gov/vuln/detail/cve-2025-32711)
- [Practical DevSecOps: MCP Security](https://www.practical-devsecops.com/mcp-security-vulnerabilities/)

### Regulation
- [EUR-Lex: EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [ABA Formal Opinion 512](https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf)
- [FINRA Regulatory Notice 24-09](https://www.finra.org/rules-guidance/notices/24-09)
- [FCA AI Update](https://www.fca.org.uk/publication/corporate/ai-update.pdf)
- [MAS AI Guidelines Consultation](https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management)

---

## Notes for Citation Integration

### New Citations to Add to bib/refs.bib

**Framework Comparisons** (if citing):
- Turing.com AI agent frameworks comparison (2025)
- Langfuse AI agent comparison blog post (2025)
- DataCamp multi-agent framework tutorial (2025)

**Foundational Papers** (if not already in bib):
```bibtex
@article{yao2022react,
  author = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  title = {ReAct: Synergizing Reasoning and Acting in Language Models},
  journal = {arXiv preprint arXiv:2210.03629},
  year = {2022},
  url = {https://arxiv.org/abs/2210.03629},
  urldate = {2025-11-27}
}

@inproceedings{schick2023toolformer,
  author = {Schick, Timo and Dwivedi-Yu, Jane and Dessì, Roberto and Raileanu, Roberta and Lomeli, Maria and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
  title = {Toolformer: Language Models Can Teach Themselves to Use Tools},
  booktitle = {Proceedings of the 37th International Conference on Neural Information Processing Systems},
  series = {NeurIPS '23},
  year = {2023},
  url = {https://arxiv.org/abs/2302.04761},
  urldate = {2025-11-27}
}

@inproceedings{yao2023tree,
  author = {Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L. and Cao, Yuan and Narasimhan, Karthik},
  title = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
  booktitle = {Proceedings of the 37th International Conference on Neural Information Processing Systems},
  series = {NeurIPS '23},
  year = {2023},
  url = {https://arxiv.org/abs/2305.10601},
  urldate = {2025-11-27}
}

@inproceedings{shinn2023reflexion,
  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},
  booktitle = {Proceedings of the 37th International Conference on Neural Information Processing Systems},
  series = {NeurIPS '23},
  year = {2023},
  url = {https://arxiv.org/abs/2303.11366},
  urldate = {2025-11-27}
}
```

**Benchmarks**:
```bibtex
@inproceedings{jimenez2024swebench,
  title = {SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},
  author = {Jimenez, Carlos E. and others},
  booktitle = {Proceedings of the International Conference on Learning Representations},
  series = {ICLR '24},
  year = {2024},
  url = {https://www.swebench.com/},
  urldate = {2025-11-27}
}

@article{zhou2023webarena,
  title = {WebArena: A Realistic Web Environment for Building Autonomous Agents},
  author = {Zhou, Shuyan and others},
  journal = {arXiv preprint arXiv:2307.13854},
  year = {2023},
  url = {https://webarena.dev/},
  urldate = {2025-11-27}
}

@article{mialon2023gaia,
  title = {GAIA: a benchmark for General AI Assistants},
  author = {Mialon, Grégoire and others},
  journal = {arXiv preprint arXiv:2311.12983},
  year = {2023},
  url = {https://arxiv.org/abs/2311.12983},
  urldate = {2025-11-27}
}

@inproceedings{liu2023agentbench,
  title = {AgentBench: Evaluating LLMs as Agents},
  author = {Liu, Xiao and others},
  booktitle = {Proceedings of the International Conference on Learning Representations},
  series = {ICLR '24},
  year = {2024},
  url = {https://arxiv.org/abs/2308.03688},
  urldate = {2025-11-27}
}
```

**Regulatory**:
```bibtex
@techreport{aba2024opinion512,
  author = {{American Bar Association Standing Committee on Ethics and Professional Responsibility}},
  title = {Formal Opinion 512: Generative Artificial Intelligence Tools},
  institution = {American Bar Association},
  year = {2024},
  month = {July},
  url = {https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf},
  urldate = {2025-11-27}
}

@techreport{finra2024notice2409,
  author = {{Financial Industry Regulatory Authority}},
  title = {Regulatory Notice 24-09: Artificial Intelligence},
  institution = {FINRA},
  year = {2024},
  month = {June},
  url = {https://www.finra.org/rules-guidance/notices/24-09},
  urldate = {2025-11-27}
}

@misc{euaiact2024,
  author = {{European Parliament and Council}},
  title = {Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence},
  howpublished = {Official Journal of the European Union},
  year = {2024},
  month = {June},
  url = {https://eur-lex.europa.eu/eli/reg/2024/1689/oj},
  urldate = {2025-11-27}
}
```

**Security**:
```bibtex
@misc{owasp2025llmtop10,
  author = {{OWASP Foundation}},
  title = {OWASP Top 10 for Large Language Model Applications 2025},
  year = {2025},
  url = {https://owasp.org/www-project-top-10-for-large-language-model-applications/},
  urldate = {2025-11-27},
  note = {Community-driven taxonomy of LLM application security vulnerabilities}
}

@misc{cve202532711,
  author = {{National Vulnerability Database}},
  title = {CVE-2025-32711: Microsoft 365 Copilot EchoLeak Vulnerability},
  year = {2025},
  url = {https://nvd.nist.gov/vuln/detail/cve-2025-32711},
  urldate = {2025-11-27},
  note = {CVSS 9.3 zero-click AI vulnerability enabling data exfiltration}
}
```

---

## Recommendations for Section Updates

1. **Add specific framework names** (with disclaimer about rapid evolution): LangGraph, LlamaIndex, CrewAI, AutoGen as current examples (November 2025)

2. **Update MCP section** with November 2025 spec release details (Tasks, URL-based registration, security improvements, MCP Apps)

3. **Add A2A Linux Foundation governance** details (June 2025 donation, founding members)

4. **Expand foundational papers** with full citations and key results for ReAct, Toolformer, Tree of Thoughts, Reflexion

5. **Update benchmark details** with current performance numbers and variants (SWE-bench Verified, WebArena SOTA, GAIA metrics)

6. **Add CVE-2025-32711** to security vulnerabilities section as concrete example of agent security risk

7. **Update regulatory sections** with:
   - ABA Formal Opinion 512 details
   - FINRA Regulatory Notice 24-09
   - EU AI Act implementation timeline and 2025 guidance
   - UK FCA AI Live Testing initiative
   - Singapore MAS AI Guidelines consultation

8. **Verify all URLs** are accessible and current (all checked as of November 27, 2025)

---

**End of Research Notes**
