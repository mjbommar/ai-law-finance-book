# Citation Analysis: Sections 09-11 (Escalation, Delegation, Governance)

**Analysis Date:** 2025-12-13
**Sections Analyzed:** 09-escalation.tex, 10-delegation.tex, 11-governance.tex
**Status:** Comprehensive review complete

---

## Summary

This analysis identifies **45+ claims requiring authoritative citations** across three sections covering escalation (human-in-the-loop), multi-agent delegation, and governance. The sections currently have **minimal citations** and need substantial source documentation to meet academic credibility standards for a professional textbook.

### Key Citation Needs by Category:

1. **Legal/Professional Responsibility** (15 claims)
   - ABA Model Rules and Formal Opinion 512
   - Professional ethics and supervision
   - Privilege and conflict requirements

2. **Regulatory Frameworks** (12 claims)
   - SEC/FINRA AI guidance
   - EU AI Act governance requirements
   - Banking regulations (OCC, FDIC, FinCEN)
   - Model risk management (SR 11-7)

3. **Technical Standards/Protocols** (8 claims)
   - Agent-to-Agent Protocol (A2A) from Google
   - Model Context Protocol (MCP) from Anthropic
   - Multi-agent system patterns

4. **Security & Risk Management** (10 claims)
   - Human-in-the-loop patterns
   - Security controls and frameworks
   - Audit logging best practices
   - Prompt injection prevention

---

## Claims Needing Citations

### Section 09: Escalation (09-escalation.tex)

#### Line 117: ABA Model Rule 1.1 on Competence
- **Claim:** "Escalate when matters exceed agent training or supervising attorney capacity (ABA Model Rule 1.1)"
- **Type:** Direct legal citation needing formal reference
- **Recommended Source:** ABA Model Rules of Professional Conduct + Formal Opinion 512
- **URLs:**
  - https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
  - https://www.americanbar.org/news/abanews/aba-news-archives/2024/07/aba-issues-first-ethics-guidance-ai-tools/
- **Proposed Citation Key:** `aba-formal-opinion-512-2024`
- **Notes:** Opinion 512 (July 29, 2024) specifically addresses AI competence requirements under Rule 1.1

#### Lines 86-100: Human-in-the-Loop Patterns
- **Claim:** "Five patterns integrate human oversight into agent workflows" (approval gates, checkpoint reviews, confidence-based escalation, human-as-tool, reversibility classification)
- **Type:** Technical framework requiring research citations
- **Recommended Sources:**
  - Academic research on HITL patterns and approval gates
  - Industry best practices from Permit.io, Parseur, Stanford HAI
- **URLs:**
  - https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo
  - https://parseur.com/blog/future-of-hitl-ai
  - https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems
- **Proposed Citation Keys:** `permit-hitl-2024`, `parseur-hitl-trends-2025`, `stanford-hai-hitl-2024`
- **Notes:** 2024 research shows tradeoffs: HITL increases uptake but may decrease accuracy if humans rubber-stamp

#### Line 129: SEC/FINRA Suitability and Fiduciary Duty
- **Claim:** "Escalate investment recommendations for adviser review before client delivery"
- **Type:** Regulatory requirement
- **Recommended Source:** FINRA Regulatory Notice 24-09 on AI/GenAI obligations
- **URL:** https://www.finra.org/rules-guidance/notices/24-09
- **Proposed Citation Key:** `finra-notice-24-09-2024`
- **Notes:** June 2024 notice specifically addresses AI use and suitability requirements

#### Line 129-130: Regulatory Thresholds
- **Claim:** "Escalate when trades approach reporting thresholds or disclosure requirements"
- **Type:** Regulatory requirement
- **Recommended Sources:**
  - SEC Form 13F requirements
  - Section 13(d)/13(g) beneficial ownership reporting
- **URL:** https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f
- **Proposed Citation Key:** `sec-form-13f-faq-2024`
- **Notes:** July 2024 updates to Form 13F filing requirements

#### Line 53-63: Section 10(b) Securities Fraud Research Example
- **Claim:** "2-year discovery period" and "conflicting circuit authority on when discovery is triggered"
- **Type:** Legal doctrine requiring case law citation
- **Recommended Source:** Merck v. Reynolds and circuit split analysis
- **URL:** https://www.cadwalader.com/resources/clients-friends-memos/securities-litigation-alert-ninth-circuit-clarifies-standards-governing-the-statute-of-limitations-for-private-claims-under-section-10b-of-the-securities-exchange-act-of-1934
- **Proposed Citation Key:** `merck-reynolds-statute-limitations`
- **Notes:** Supreme Court case clarified discovery standard for Section 10(b) claims; circuits split on inquiry notice

#### Line 73: Trade Size Approval Threshold Example
- **Claim:** "Trade size exceeds single-approver threshold (\$500K total)"
- **Type:** Industry practice example
- **Recommended Source:** General financial services governance practices
- **Note:** This is an illustrative example - consider adding footnote that thresholds vary by institution

#### Line 76: Tax Impact Calculation
- **Claim:** "Net tax impact: approximately \$8K additional liability"
- **Type:** Technical calculation example
- **Note:** Example calculation - consider citation to tax treatment of capital gains or add "hypothetical example" qualifier

### Section 10: Delegation (10-delegation.tex)

#### Lines 49-67: Agent-to-Agent Protocol (A2A)
- **Claim:** "The Agent-to-Agent Protocol standardizes how agents collaborate" with detailed description of Agent Cards, Tasks, Artifacts, Communication Channels
- **Type:** Technical standard/protocol requiring authoritative source
- **Recommended Sources:**
  - Google Developers Blog announcement
  - A2A Protocol Specification (official)
  - GitHub repository
- **URLs:**
  - https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
  - https://a2a-protocol.org/latest/specification/
  - https://github.com/a2aproject/A2A
- **Proposed Citation Keys:** `google-a2a-announcement-2025`, `a2a-specification-v1-2025`, `a2a-github-2025`
- **Notes:** Google released A2A in April 2025; now under Linux Foundation with 150+ organizations

#### Lines 52, 86: Model Context Protocol (MCP)
- **Claim:** "If MCP is how agents access resources, A2A is how agents delegate work" and "MCP handles agent-to-tool communication"
- **Type:** Technical protocol requiring authoritative source
- **Recommended Sources:**
  - Anthropic MCP announcement
  - MCP Specification (November 2025)
  - MCP donated to Agentic AI Foundation (December 2025)
- **URLs:**
  - https://www.anthropic.com/news/model-context-protocol
  - https://modelcontextprotocol.io/specification/2025-11-25
  - https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- **Proposed Citation Keys:** `anthropic-mcp-announcement-2024`, `mcp-specification-2025-11`, `anthropic-mcp-aaif-2025`
- **Notes:** MCP launched Nov 2024, donated to Linux Foundation in Dec 2025; 97M+ monthly SDK downloads

#### Line 163: MCP Production Status
- **Claim:** "As of late 2025, MCP is production-ready for tool integration. A2A is maturing with a stable specification and active pilots, but cross-vendor reliability remains uneven."
- **Type:** Technology maturity assessment
- **Recommended Sources:** Industry reports and vendor documentation
- **URLs:**
  - https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/
  - https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade
- **Proposed Citation Keys:** `mcp-one-year-anniversary-2025`, `google-a2a-upgrade-2025`
- **Notes:** MCP has OpenAI, Google, Microsoft adoption; A2A at v0.3 as of 2025

#### Lines 101-104: Bank Secrecy Act and FinCEN
- **Claim:** "FinCEN registration is required along with a KYC/AML program"
- **Type:** Regulatory requirement
- **Recommended Source:** FinCEN BSA requirements
- **URL:** https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act
- **Proposed Citation Key:** `fincen-bsa-requirements`
- **Notes:** Bank Secrecy Act (1970) with amendments; FinCEN administers BSA

#### Line 102: Howey Test
- **Claim:** "Product likely constitutes a security under the Howey test"
- **Type:** Legal test requiring case law citation
- **Recommended Source:** SEC Framework for Investment Contract Analysis of Digital Assets
- **URL:** https://www.sec.gov/files/dlt-framework.pdf
- **Proposed Citation Key:** `sec-digital-asset-framework-2019`
- **Notes:** SEC v. W.J. Howey Co., 328 U.S. 293 (1946); SEC framework applies Howey to digital assets

#### Line 103: CFPB UDAP/UDAAP
- **Claim:** "UDAP exposure and recommending clear disclosures and complaint handling procedures"
- **Type:** Regulatory framework
- **Recommended Source:** CFPB UDAAP examination procedures and OCC handbook
- **URLs:**
  - https://www.consumerfinance.gov/compliance/supervision-examinations/unfair-deceptive-or-abusive-acts-or-practices-udaaps-examination-procedures/
  - https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/unfair-deceptive-act/index-udaap.html
- **Proposed Citation Keys:** `cfpb-udaap-exam-procedures`, `occ-udaap-handbook-2024`
- **Notes:** Dodd-Frank Act section 1031/1036 prohibits UDAAP; updated OCC handbook v1.1 in 2024

#### Line 109: VWAP Execution Strategy
- **Claim:** "VWAP execution over two days given average daily volume of \$200M"
- **Type:** Trading strategy/algorithm
- **Recommended Source:** VWAP trading literature and execution algorithms
- **URL:** https://en.wikipedia.org/wiki/Volume-weighted_average_price
- **Proposed Citation Key:** `vwap-execution-algorithms`
- **Notes:** Industry-standard execution benchmark; used by institutional investors

#### Line 109: Form 13F Amendment Requirement
- **Claim:** "13F amendment will be required at quarter-end"
- **Type:** SEC filing requirement
- **Recommended Source:** SEC Form 13F requirements
- **URL:** https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f
- **Proposed Citation Key:** `sec-form-13f-faq-2024`
- **Notes:** Institutional investment managers with $100M+ must file quarterly

#### Lines 124-134: Multi-Agent Coordination Failures
- **Claim:** Descriptions of deadlock, divergent conclusions, cascading errors, coordination overhead, accountability gaps
- **Type:** Technical failure modes requiring research citations
- **Recommended Sources:** Multi-agent systems research on coordination failures
- **URLs:**
  - https://arxiv.org/html/2503.13657v1 (Why Do Multi-Agent LLM Systems Fail?)
  - https://arxiv.org/html/2506.01438v1 (Distinguishing Autonomous AI Agents)
  - https://galileo.ai/blog/challenges-monitoring-multi-agent-systems
- **Proposed Citation Keys:** `arxiv-multi-agent-failures-2025`, `arxiv-agent-frameworks-2025`, `galileo-mas-monitoring-2024`
- **Notes:** 2025 research shows MAS correctness can be as low as 25%; cascading failures major concern

#### Lines 130-134: Multi-Agent Security Controls
- **Claim:** Agent identity, authorization controls, information barriers, audit trails, task validation
- **Type:** Security framework requiring authoritative sources
- **Recommended Sources:**
  - OWASP GenAI Security Project
  - Multi-agent security research
- **URLs:**
  - https://genai.owasp.org/
  - https://arxiv.org/html/2505.02077 (Open Challenges in Multi-Agent Security)
- **Proposed Citation Keys:** `owasp-genai-security-2025`, `arxiv-multi-agent-security-2025`
- **Notes:** 2025 research identifies impersonation, cascading privacy leaks, coordinated attacks

### Section 11: Governance (11-governance.tex)

#### Line 22: Professional Duties Non-Delegable
- **Claim:** "Professional duties are non-delegable: attorneys remain liable for AI-assisted work product, and fiduciaries remain accountable for AI-informed recommendations"
- **Type:** Legal principle requiring authoritative citation
- **Recommended Sources:**
  - ABA Formal Opinion 512
  - ABA Model Rules 5.1 and 5.3 on supervision
- **URLs:**
  - https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
  - https://library.law.unc.edu/2025/02/aba-formal-opinion-512-the-paradigm-for-generative-ai-in-legal-practice/
- **Proposed Citation Keys:** `aba-formal-opinion-512-2024`, `aba-model-rule-5-1`, `aba-model-rule-5-3`
- **Notes:** Formal Opinion 512 emphasizes supervision requirements under Rules 5.1 and 5.3

#### Lines 79-91: Five Security Controls
- **Claim:** Input separation, output validation, least privilege, audit logging, matter/client isolation
- **Type:** Security best practices framework
- **Recommended Sources:**
  - OWASP Top 10 for LLM Applications
  - NIST cybersecurity frameworks
  - Cloud provider security guidance (AWS, Azure)
- **URLs:**
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/ (Input separation for prompt injection)
  - https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-92.pdf (NIST SP 800-92 audit logging)
  - https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/platform/security (Azure AI security)
- **Proposed Citation Keys:** `owasp-llm01-prompt-injection-2025`, `nist-sp-800-92-audit-logging`, `microsoft-azure-ai-security-2025`
- **Notes:** Input separation critical for prompt injection prevention; NIST SP 800-92 for audit logging

#### Lines 81-82: Input Separation (Prompt Injection Prevention)
- **Claim:** "Isolate user inputs from system prompts to prevent prompt injection attacks"
- **Type:** Security control requiring technical citations
- **Recommended Sources:**
  - OWASP LLM01 Prompt Injection guidance
  - Academic research on prompt injection prevention
- **URLs:**
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - https://arxiv.org/html/2507.13169v1 (Prompt Injection 2.0)
  - https://www.lakera.ai/blog/guide-to-prompt-injection
- **Proposed Citation Keys:** `owasp-llm01-prompt-injection-2025`, `arxiv-prompt-injection-2024`, `lakera-prompt-injection-guide`
- **Notes:** 2024-2025 research shows parameterization difficult in LLMs; architectural separation recommended

#### Line 83: Output Validation
- **Claim:** "Verify agent outputs before execution to detect hallucinations and constraint violations"
- **Type:** Security control requiring best practices citation
- **Recommended Source:** AI safety and reliability research
- **Note:** General best practice - consider citation to AI reliability frameworks or hallucination detection research

#### Line 85: Least Privilege
- **Claim:** "Grant minimum necessary tool access to limit the scope and impact of failures"
- **Type:** Security principle
- **Recommended Source:** NIST principles of least privilege
- **URL:** https://csrc.nist.gov/glossary/term/least_privilege
- **Proposed Citation Key:** `nist-least-privilege-principle`
- **Notes:** Foundational security principle; NIST RBAC standards

#### Line 87: Audit Logging
- **Claim:** "Maintain comprehensive action logs for accountability and investigation"
- **Type:** Security/compliance requirement
- **Recommended Source:** NIST SP 800-92 Guide to Computer Security Log Management
- **URL:** https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-92.pdf
- **Proposed Citation Key:** `nist-sp-800-92-audit-logging`
- **Notes:** NIST SP 800-92 Rev 1 draft released 2024; playbook for log management planning

#### Line 89: Matter/Client Isolation
- **Claim:** "Enforce confidentiality boundaries to protect privileged and confidential information"
- **Type:** Legal/ethical requirement and technical control
- **Recommended Sources:**
  - ABA Model Rule 1.6 on confidentiality
  - ABA Formal Opinion 512 on AI and confidentiality
- **URLs:**
  - https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf
- **Proposed Citation Keys:** `aba-model-rule-1-6`, `aba-formal-opinion-512-2024`
- **Notes:** Opinion 512 addresses confidentiality risks with GenAI tools

#### Lines 110-120: Four Levels of Transparency
- **Claim:** Level 0 (output only), Level 1 (summary with sources), Level 2 (reasoning outline), Level 3 (full execution trace)
- **Type:** Framework requiring citation
- **Recommended Source:** Explainability and transparency research in AI
- **Note:** This appears to be original framework - consider positioning as authors' synthesis or citing XAI literature

#### Lines 129-134: Auditability vs. Retention Framework
- **Claim:** Structured logging, tiered retention, redaction at capture, legal hold integration
- **Type:** Data governance framework
- **Recommended Sources:**
  - NIST SP 800-92 on log retention
  - Legal hold and e-discovery standards
  - Privacy regulations (GDPR, CCPA)
- **URL:** https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-92.pdf
- **Proposed Citation Keys:** `nist-sp-800-92-audit-logging`, `nist-800-171-retention-2024`
- **Notes:** NIST 800-171 requires 90-day retention for DoD contractors; 1 year common for FISMA, HIPAA, SOX

---

## Proposed BibTeX Entries

```bibtex
% ============================================================================
% ABA Ethics and Professional Responsibility
% ============================================================================

@misc{aba-formal-opinion-512-2024,
  author = {{American Bar Association Standing Committee on Ethics and Professional Responsibility}},
  title = {Formal Opinion 512: Generative Artificial Intelligence Tools},
  year = {2024},
  month = {July},
  day = {29},
  url = {https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf},
  urldate = {2025-12-13},
  note = {First formal ABA ethics opinion addressing generative AI use in legal practice. Addresses competence (Rule 1.1), confidentiality (Rule 1.6), supervision (Rules 5.1, 5.3), and fees (Rule 1.5)}
}

@misc{aba-model-rule-1-1,
  author = {{American Bar Association}},
  title = {Model Rules of Professional Conduct: Rule 1.1 - Competence},
  year = {2024},
  url = {https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_1_competence/},
  urldate = {2025-12-13},
  note = {Comment 8 requires lawyers to keep abreast of benefits and risks of relevant technology}
}

@misc{aba-model-rule-1-6,
  author = {{American Bar Association}},
  title = {Model Rules of Professional Conduct: Rule 1.6 - Confidentiality of Information},
  year = {2024},
  url = {https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_6_confidentiality_of_information/},
  urldate = {2025-12-13},
  note = {Establishes duty of confidentiality for client information}
}

@misc{aba-model-rule-5-1,
  author = {{American Bar Association}},
  title = {Model Rules of Professional Conduct: Rule 5.1 - Responsibilities of Partners, Managers, and Supervisory Lawyers},
  year = {2024},
  url = {https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_5_1_responsibilities_of_partners_managers_supervisory_lawyers/},
  urldate = {2025-12-13},
  note = {Requires establishing policies and supervising lawyers to ensure ethical compliance}
}

@misc{aba-model-rule-5-3,
  author = {{American Bar Association}},
  title = {Model Rules of Professional Conduct: Rule 5.3 - Responsibilities Regarding Nonlawyer Assistance},
  year = {2024},
  url = {https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_5_3_responsibilities_regarding_nonlawyer_assistants/},
  urldate = {2025-12-13},
  note = {Requires supervision of nonlawyers including technology providers and contractors}
}

% ============================================================================
% SEC and FINRA Regulation
% ============================================================================

@misc{finra-notice-24-09-2024,
  author = {{Financial Industry Regulatory Authority}},
  title = {Regulatory Notice 24-09: Artificial Intelligence in Member Firms' Securities Businesses},
  year = {2024},
  month = {June},
  day = {27},
  url = {https://www.finra.org/rules-guidance/notices/24-09},
  urldate = {2025-12-13},
  note = {FINRA guidance on AI and GenAI use by broker-dealers. Emphasizes technology governance under Rule 3110, recordkeeping, customer information protection, and Reg BI compliance}
}

@misc{sec-form-13f-faq-2024,
  author = {{U.S. Securities and Exchange Commission}},
  title = {Frequently Asked Questions About Form 13F},
  year = {2024},
  url = {https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f},
  urldate = {2025-12-13},
  note = {Form 13F requires institutional investment managers with \$100M+ in Section 13(f) securities to file quarterly reports. July 2024 updates include Form N-PX proxy voting disclosures}
}

@misc{sec-digital-asset-framework-2019,
  author = {{U.S. Securities and Exchange Commission}},
  title = {Framework for "Investment Contract" Analysis of Digital Assets},
  year = {2019},
  month = {April},
  url = {https://www.sec.gov/files/dlt-framework.pdf},
  urldate = {2025-12-13},
  note = {SEC framework applying Howey test to digital assets and cryptocurrencies}
}

@article{merck-reynolds-statute-limitations,
  author = {Merck \& Co. v. Reynolds},
  title = {559 U.S. 633},
  journal = {Supreme Court Reporter},
  year = {2010},
  note = {Supreme Court held that Section 10(b) two-year statute of limitations begins when plaintiff discovers or should have discovered facts constituting violation, including scienter. Resolved circuit split on inquiry notice vs. discovery}
}

% ============================================================================
% Banking and Financial Regulation
% ============================================================================

@misc{fincen-bsa-requirements,
  author = {{Financial Crimes Enforcement Network}},
  title = {The Bank Secrecy Act},
  year = {2025},
  url = {https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act},
  urldate = {2025-12-13},
  note = {FinCEN administers BSA (Currency and Foreign Transactions Reporting Act of 1970). Requires financial institutions to maintain records, file reports, and implement AML/KYC programs}
}

@misc{cfpb-udaap-exam-procedures,
  author = {{Consumer Financial Protection Bureau}},
  title = {Unfair, Deceptive, or Abusive Acts or Practices (UDAAPs) Examination Procedures},
  year = {2024},
  url = {https://www.consumerfinance.gov/compliance/supervision-examinations/unfair-deceptive-or-abusive-acts-or-practices-udaaps-examination-procedures/},
  urldate = {2025-12-13},
  note = {CFPB examination procedures for UDAAP violations under Dodd-Frank Act sections 1031 and 1036}
}

@misc{occ-udaap-handbook-2024,
  author = {{Office of the Comptroller of the Currency}},
  title = {Comptroller's Handbook: Unfair or Deceptive Acts or Practices and Unfair, Deceptive, or Abusive Acts or Practices},
  year = {2024},
  version = {1.1},
  url = {https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/unfair-deceptive-act/index-udaap.html},
  urldate = {2025-12-13},
  note = {Updated OCC examination handbook for UDAP and UDAAP compliance}
}

@misc{fed-sr-11-7-model-risk-2011,
  author = {{Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency}},
  title = {Supervisory Guidance on Model Risk Management},
  year = {2011},
  month = {April},
  day = {4},
  number = {SR 11-7},
  url = {https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm},
  urldate = {2025-12-13},
  note = {Foundational guidance on model risk management for banking organizations. Emphasizes effective challenge, robust development, validation, and governance. FDIC adopted as FIL-22-2017}
}

% ============================================================================
% Technical Protocols: A2A and MCP
% ============================================================================

@misc{google-a2a-announcement-2025,
  author = {{Google Developers}},
  title = {Announcing the Agent2Agent Protocol (A2A): A New Era of Agent Interoperability},
  year = {2025},
  month = {April},
  url = {https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/},
  urldate = {2025-12-13},
  note = {Google's announcement of A2A protocol for multi-agent collaboration. Uses JSON-RPC 2.0 over HTTP(S), supports Agent Cards, Tasks, Artifacts, and Communication Channels}
}

@misc{a2a-specification-v1-2025,
  author = {{A2A Project}},
  title = {Agent2Agent (A2A) Protocol Specification (DRAFT v1.0)},
  year = {2025},
  url = {https://a2a-protocol.org/latest/specification/},
  urldate = {2025-12-13},
  note = {Official A2A protocol specification. Open source project under Linux Foundation with support from Google, Salesforce, Atlassian, LangChain, and 150+ organizations}
}

@misc{a2a-github-2025,
  author = {{A2A Project}},
  title = {A2A: An Open Protocol Enabling Communication and Interoperability Between Opaque Agentic Applications},
  year = {2025},
  url = {https://github.com/a2aproject/A2A},
  urldate = {2025-12-13},
  note = {Official A2A GitHub repository with reference implementations}
}

@misc{google-a2a-upgrade-2025,
  author = {{Google Cloud}},
  title = {Agent2Agent Protocol (A2A) Is Getting an Upgrade},
  year = {2025},
  url = {https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade},
  urldate = {2025-12-13},
  note = {Announcement of A2A v0.3 with gRPC support, security card signing, and extended client-side support}
}

@misc{anthropic-mcp-announcement-2024,
  author = {{Anthropic}},
  title = {Introducing the Model Context Protocol},
  year = {2024},
  month = {November},
  url = {https://www.anthropic.com/news/model-context-protocol},
  urldate = {2025-12-13},
  note = {Anthropic's announcement of MCP for standardizing LLM integration with external data sources and tools. Uses JSON-RPC 2.0 over stdio and HTTP/SSE}
}

@misc{mcp-specification-2025-11,
  author = {{Model Context Protocol}},
  title = {Model Context Protocol Specification (2025-11-25)},
  year = {2025},
  month = {November},
  day = {25},
  url = {https://modelcontextprotocol.io/specification/2025-11-25},
  urldate = {2025-12-13},
  note = {Official MCP specification v2025-11-25 with asynchronous operations, statelessness, server identity, and task abstractions}
}

@misc{anthropic-mcp-aaif-2025,
  author = {{Anthropic}},
  title = {Donating the Model Context Protocol and Establishing the Agentic AI Foundation},
  year = {2025},
  month = {December},
  url = {https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation},
  urldate = {2025-12-13},
  note = {Anthropic donated MCP to Agentic AI Foundation (Linux Foundation) co-founded with Block and OpenAI. Supported by Google, Microsoft, AWS, Cloudflare, Bloomberg}
}

@misc{mcp-one-year-anniversary-2025,
  author = {{Model Context Protocol}},
  title = {One Year of MCP: November 2025 Spec Release},
  year = {2025},
  month = {November},
  day = {25},
  url = {http://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/},
  urldate = {2025-12-13},
  note = {MCP one-year anniversary report. 97M+ monthly SDK downloads across Python and TypeScript. Adopted by OpenAI, Google, Microsoft}
}

% ============================================================================
% EU AI Act
% ============================================================================

@misc{eu-ai-act-2024,
  author = {{European Commission}},
  title = {Regulation (EU) 2024/1689 of the European Parliament and of the Council on Artificial Intelligence (AI Act)},
  year = {2024},
  month = {July},
  day = {12},
  url = {https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai},
  urldate = {2025-12-13},
  note = {First comprehensive legal framework on AI worldwide. Risk-based approach with four tiers. Entered into force August 1, 2024; fully applicable August 2, 2026. Penalties up to 7\% of global annual turnover}
}

@misc{eu-ai-act-summary-2024,
  author = {{EU Artificial Intelligence Act}},
  title = {High-Level Summary of the AI Act},
  year = {2024},
  url = {https://artificialintelligenceact.eu/high-level-summary/},
  urldate = {2025-12-13},
  note = {Comprehensive summary of EU AI Act requirements including governance structure, risk categorization, and compliance obligations}
}

% ============================================================================
% Human-in-the-Loop Research
% ============================================================================

@misc{permit-hitl-2024,
  author = {Permit.io},
  title = {Human-in-the-Loop for AI Agents: Best Practices, Frameworks, Use Cases, and Demo},
  year = {2024},
  url = {https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo},
  urldate = {2025-12-13},
  note = {Comprehensive guide to HITL patterns including approval gates, checkpoint reviews, and deferred tool execution}
}

@misc{parseur-hitl-trends-2025,
  author = {Parseur},
  title = {Future of Human-in-the-Loop AI (2025): Emerging Trends \& Hybrid Automation Insights},
  year = {2025},
  url = {https://parseur.com/blog/future-of-hitl-ai},
  urldate = {2025-12-13},
  note = {2025 trends in HITL AI systems including governance market analysis (70\% enterprise adoption, 66\% oversight solutions)}
}

@misc{stanford-hai-hitl-2024,
  author = {{Stanford Human-Centered AI Institute}},
  title = {Humans in the Loop: The Design of Interactive AI Systems},
  year = {2024},
  url = {https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems},
  urldate = {2025-12-13},
  note = {Stanford HAI research on designing effective human-AI interaction patterns}
}

@article{hitl-uptake-accuracy-tradeoff-2024,
  author = {Multiple Authors},
  title = {Putting a Human in the Loop: Increasing Uptake, but Decreasing Accuracy of Automated Decision-Making},
  journal = {PLoS One},
  year = {2024},
  url = {https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10857587/},
  urldate = {2025-12-13},
  note = {Study (N=292) found HITL increases algorithmic uptake but may decrease accuracy if humans rubber-stamp recommendations}
}

% ============================================================================
% Multi-Agent Systems and Coordination
% ============================================================================

@misc{arxiv-multi-agent-failures-2025,
  author = {Multiple Authors},
  title = {Why Do Multi-Agent LLM Systems Fail?},
  year = {2025},
  url = {https://arxiv.org/html/2503.13657v1},
  urldate = {2025-12-13},
  note = {Analysis showing multi-agent system correctness can be as low as 25\%. Identifies cascading hallucinations, timing dependencies, and coordination overhead as key failure modes}
}

@misc{arxiv-agent-frameworks-2025,
  author = {Multiple Authors},
  title = {Distinguishing Autonomous AI Agents from Collaborative Agentic Systems: A Comprehensive Framework for Understanding Modern Intelligent Architectures},
  year = {2025},
  url = {https://arxiv.org/html/2506.01438v1},
  urldate = {2025-12-13},
  note = {Framework for understanding autonomous agents vs. collaborative multi-agent systems}
}

@misc{galileo-mas-monitoring-2024,
  author = {Galileo AI},
  title = {9 Key Challenges in Monitoring Multi-Agent Systems at Scale},
  year = {2024},
  url = {https://galileo.ai/blog/challenges-monitoring-multi-agent-systems},
  urldate = {2025-12-13},
  note = {Industry analysis of MAS monitoring challenges including cascading failures and accountability gaps}
}

@misc{arxiv-multi-agent-security-2025,
  author = {Multiple Authors},
  title = {Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents},
  year = {2025},
  url = {https://arxiv.org/html/2505.02077},
  urldate = {2025-12-13},
  note = {Security challenges in multi-agent systems including secret collusion, coordinated attacks, cascading privacy leaks, and decentralized adversarial coordination}
}

@misc{arxiv-multi-agent-coordination-2025,
  author = {Multiple Authors},
  title = {Multi-Agent Coordination across Diverse Applications: A Survey},
  year = {2025},
  url = {https://arxiv.org/html/2502.14743v2},
  urldate = {2025-12-13},
  note = {Survey of multi-agent coordination mechanisms addressing fundamental questions: what is coordination, why coordinate, who to coordinate with, how to coordinate}
}

% ============================================================================
% Security: NIST, OWASP, Cloud Providers
% ============================================================================

@misc{nist-sp-800-92-audit-logging,
  author = {{National Institute of Standards and Technology}},
  title = {Special Publication 800-92 Revision 1: Cybersecurity Log Management Planning Guide (Draft)},
  year = {2024},
  url = {https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-92.pdf},
  urldate = {2025-12-13},
  note = {NIST guidance on log management for cybersecurity. Playbook for improving log management to support best practices and regulatory requirements}
}

@misc{nist-800-171-retention-2024,
  author = {{National Institute of Standards and Technology}},
  title = {NIST SP 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations},
  year = {2024},
  url = {https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final},
  urldate = {2025-12-13},
  note = {Requirement 3.3 on audit and accountability. DoD contractors must retain logs for at least 90 days per DFARS 252.204-7012}
}

@misc{nist-least-privilege-principle,
  author = {{National Institute of Standards and Technology}},
  title = {Glossary: Least Privilege},
  year = {2024},
  url = {https://csrc.nist.gov/glossary/term/least_privilege},
  urldate = {2025-12-13},
  note = {Foundational security principle requiring minimum necessary access rights}
}

@misc{owasp-llm01-prompt-injection-2025,
  author = {{OWASP Gen AI Security Project}},
  title = {LLM01:2025 Prompt Injection},
  year = {2025},
  url = {https://genai.owasp.org/llmrisk/llm01-prompt-injection/},
  urldate = {2025-12-13},
  note = {OWASP guidance on prompt injection vulnerabilities. Exploits lack of separation between system instructions and user input. Recommends delimiters, datamarking, and architectural separation}
}

@misc{owasp-genai-security-2025,
  author = {{OWASP Gen AI Security Project}},
  title = {OWASP Generative AI Security Project},
  year = {2025},
  url = {https://genai.owasp.org/},
  urldate = {2025-12-13},
  note = {Comprehensive security framework for generative AI applications including LLM-specific vulnerabilities}
}

@misc{arxiv-prompt-injection-2024,
  author = {Multiple Authors},
  title = {Prompt Injection 2.0: Hybrid AI Threats},
  year = {2024},
  url = {https://arxiv.org/html/2507.13169v1},
  urldate = {2025-12-13},
  note = {Research on evolving prompt injection attacks and hybrid threat models}
}

@misc{lakera-prompt-injection-guide,
  author = {Lakera},
  title = {Prompt Injection \& the Rise of Prompt Attacks: All You Need to Know},
  year = {2024},
  url = {https://www.lakera.ai/blog/guide-to-prompt-injection},
  urldate = {2025-12-13},
  note = {Comprehensive guide to prompt injection attacks and prevention techniques}
}

@misc{microsoft-azure-ai-security-2025,
  author = {{Microsoft}},
  title = {Secure Azure Platform Services (PaaS) for AI - Cloud Adoption Framework},
  year = {2025},
  url = {https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/platform/security},
  urldate = {2025-12-13},
  note = {Microsoft Azure security framework for AI agents. Includes Microsoft Purview for data governance, MITRE ATLAS and OWASP GenAI risk frameworks, AI security posture management in Defender for Cloud}
}

% ============================================================================
% Trading and Financial Operations
% ============================================================================

@misc{vwap-execution-algorithms,
  author = {{Wikipedia}},
  title = {Volume-Weighted Average Price},
  year = {2024},
  url = {https://en.wikipedia.org/wiki/Volume-weighted_average_price},
  urldate = {2025-12-13},
  note = {VWAP is a trading benchmark calculated as ratio of value traded to total volume. Used by institutional investors to evaluate execution quality and as basis for execution algorithms}
}
```

---

## Existing Citations to Fix/Remove

### Section 09
- **Line 117:** "ABA Model Rule 1.1" - currently cited parenthetically without formal bibliography entry
  - **Action:** Add formal citation to `aba-model-rule-1-1` and `aba-formal-opinion-512-2024`

### Section 10
- **No existing citations found** in this section
  - **Action:** Add all recommended citations throughout

### Section 11
- **No existing citations found** in this section
  - **Action:** Add all recommended citations throughout

---

## Implementation Priority

### High Priority (Essential for Credibility)
1. **ABA Formal Opinion 512** and Model Rules (professional responsibility foundation)
2. **A2A and MCP specifications** (core technical protocols discussed extensively)
3. **FINRA Notice 24-09** and **SEC guidance** (regulatory requirements for financial services)
4. **NIST SP 800-92** (audit logging best practices)
5. **OWASP LLM01** (prompt injection prevention)
6. **EU AI Act** (governance framework)
7. **Fed SR 11-7** (model risk management)

### Medium Priority (Supports Specific Claims)
1. **FinCEN BSA requirements** (Bank Secrecy Act/AML)
2. **SEC Form 13F** and **Howey test** (specific regulatory examples)
3. **CFPB UDAAP** (consumer protection)
4. **Multi-agent systems research** (coordination failures, security)
5. **HITL research** (human-in-the-loop patterns)
6. **Cloud security frameworks** (AWS, Azure)

### Lower Priority (Examples and Illustrations)
1. **VWAP execution** (trading example)
2. **Section 10(b) statute of limitations** (legal research example)
3. **Money transmitter licensing** (fintech example)

---

## Integration Notes

### Where to Add Citations in LaTeX

1. **Inline citations for specific claims:**
   ```latex
   \parencite{aba-formal-opinion-512-2024}
   ```

2. **Narrative citations for author-focused references:**
   ```latex
   As \textcite{google-a2a-announcement-2025} explains...
   ```

3. **Multiple sources for comprehensive support:**
   ```latex
   \parencite{finra-notice-24-09-2024, sec-form-13f-faq-2024}
   ```

4. **Page-specific citations when referencing specific passages:**
   ```latex
   \parencite[p.~5]{aba-formal-opinion-512-2024}
   ```

### Bibliography File Location
- Add all BibTeX entries to: `/home/mjbommar/projects/personal/ai-law-finance-book/chapters/07-agents-part-2/bib/refs.bib`

### Validation After Implementation
Run these checks:
```bash
cd /home/mjbommar/projects/personal/ai-law-finance-book/chapters/07-agents-part-2
make pdf      # Verify compilation with new citations
make validate # Check for undefined references
```

---

## Additional Research Needs

### Topics Requiring Further Investigation
1. **Specific AWS/Azure agent security frameworks** - needs more detailed technical documentation
2. **Transparency levels framework** - appears to be original; consider positioning as authors' synthesis or finding XAI research to cite
3. **Auditability vs. retention framework** - needs legal/compliance citations on retention schedules by industry
4. **Reversibility classification pattern** - needs research citation or position as authors' framework

### Regulatory Updates to Monitor
- **SEC 2025 Examination Priorities** - AI and emerging technologies focus
- **FINRA 2025 Annual Regulatory Report** - published January 2025
- **ABA state adoption** of technological competence requirements
- **EU AI Act implementation timeline** - phased enforcement through 2027

---

## Sources Referenced in This Analysis

### Legal and Ethics
- [ABA issues first ethics guidance on AI tools](https://www.americanbar.org/news/abanews/aba-news-archives/2024/07/aba-issues-first-ethics-guidance-ai-tools/)
- [ABA Formal Opinion 512: The Paradigm for Generative AI](https://library.law.unc.edu/2025/02/aba-formal-opinion-512-the-paradigm-for-generative-ai-in-legal-practice/)
- [ABA Model Rule 1.1: Competence in Modern Law](https://www.numberanalytics.com/blog/aba-model-rule-1.1-in-modern-law)

### Financial Regulation
- [FINRA Regulatory Notice 24-09](https://www.finra.org/rules-guidance/notices/24-09)
- [SEC Division of Examinations 2025 Exam Priorities](https://www.mofo.com/resources/insights/241101-sec-division-of-examinations-2025-exam-priorities)
- [New SEC Requirements for Form 13F Filers](https://www.cooley.com/news/insight/2024/2024-04-26-new-sec-requirements-for-form-13f-filers-effective-july-1-2024)
- [The Bank Secrecy Act | FinCEN](https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act)
- [SR 11-7 Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)

### Technical Protocols
- [Announcing the Agent2Agent Protocol (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/)
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [MCP Specification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- [Donating MCP to Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)

### EU Regulation
- [AI Act | Shaping Europe's digital future](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [High-level summary of the AI Act](https://artificialintelligenceact.eu/high-level-summary/)

### Human-in-the-Loop Research
- [Human-in-the-Loop for AI Agents: Best Practices](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo)
- [Future of Human-in-the-Loop AI (2025)](https://parseur.com/blog/future-of-hitl-ai)
- [Humans in the Loop: The Design of Interactive AI Systems](https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems)
- [Putting a human in the loop: Increasing uptake, but decreasing accuracy](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10857587/)

### Multi-Agent Systems
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/html/2503.13657v1)
- [Distinguishing Autonomous AI Agents from Collaborative Agentic Systems](https://arxiv.org/html/2506.01438v1)
- [9 Key Challenges in Monitoring Multi-Agent Systems](https://galileo.ai/blog/challenges-monitoring-multi-agent-systems)
- [Open Challenges in Multi-Agent Security](https://arxiv.org/html/2505.02077)

### Security Frameworks
- [NIST SP 800-92 Guide to Computer Security Log Management](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-92.pdf)
- [NIST SP 800-171 Audit & Accountability](https://neqterlabs.com/nist-sp-800-171-requirement-3-3-audit-accountability/)
- [LLM01:2025 Prompt Injection - OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [Prompt Injection 2.0: Hybrid AI Threats](https://arxiv.org/html/2507.13169v1)
- [Secure Azure Platform Services for AI](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/platform/security)

---

**End of Citation Analysis**
