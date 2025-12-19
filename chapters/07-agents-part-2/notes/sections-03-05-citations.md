# Citation Analysis for Sections 03-05 (Intent, Perception, Action)

## Summary

Reviewed sections 03-intent.tex, 04-perception.tex, and 05-action.tex from Chapter 07 "Agents Part II: How to Build an Agent". These sections contain **extensive factual claims requiring authoritative citations** but currently have **almost no citations at all**.

The sections make specific claims about:
- The Model Context Protocol (MCP) and its adoption by major vendors
- Tool use patterns (ReAct, function calling)
- Legal and financial information systems (Westlaw, PACER, EDGAR, CM/ECF, Bloomberg, etc.)
- Security threats (prompt injection, OWASP Top 10)
- Document processing and RAG (Retrieval-Augmented Generation)
- Financial identifiers and risk metrics
- Legal citation standards and procedural rules

**Critical finding**: The textbook's credibility as an authoritative reference for legal and financial professionals depends on proper citation of these factual claims. Current citation density is extremely low (essentially zero in these sections).

---

## Claims Needing Citations

### Section 03: Intent (03-intent.tex)

#### Line 156: LLM Clarification Behavior
- **File**: 03-intent.tex
- **Line**: 156
- **Claim**: "Research has documented that LLMs sometimes select a default interpretation rather than asking for clarification, even when ambiguity is significant."
- **Recommended source**: This needs a research citation. Search for papers on LLM clarification behavior, uncertainty quantification, or calibration studies.
- **Proposed citation key**: `llm-clarification-2024` (pending source identification)
- **Action needed**: Additional search required for academic papers on LLM clarification behavior

---

### Section 04: Perception (04-perception.tex)

#### Line 38: Legal Research Platforms
- **File**: 04-perception.tex
- **Line**: 38
- **Claim**: "Legal research tools include Westlaw, Lexis, Bloomberg Law, PACER for federal court filings, state court docket systems, and regulatory databases like EDGAR."
- **Recommended sources**:
  - Westlaw/Lexis/Bloomberg: Georgetown Law Library overview
  - PACER official site
  - EDGAR official site
- **Proposed citation keys**: `westlaw-lexis-overview`, `pacer-system`, `sec-edgar`

#### Line 38-39: Financial Research Platforms
- **File**: 04-perception.tex
- **Line**: 38-39
- **Claim**: "Financial research tools include Bloomberg Terminal, Reuters Eikon, FactSet, and proprietary analytics platforms."
- **Recommended source**: Wall Street Prep comparison or Investopedia overview
- **Proposed citation key**: `financial-data-platforms-2024`

#### Line 39: Legal Document Management
- **File**: 04-perception.tex
- **Line**: 39
- **Claim**: "Internal knowledge bases round out the category, including the firm's document management system (iManage, NetDocuments)"
- **Recommended source**: Legal technology comparison resources
- **Proposed citation key**: `legal-dms-comparison`

#### Line 48-77: Model Context Protocol (MCP)
- **File**: 04-perception.tex
- **Lines**: 48-77
- **Claims**:
  - MCP standardizes how agents access tools
  - MCP architecture (Host, Client, Server)
  - Resources as read-only data access endpoints
  - "As of late 2025, over 7,260 MCP servers have been catalogued in community directories"
- **Recommended sources**:
  - Official Anthropic MCP documentation: https://docs.anthropic.com/en/docs/mcp
  - MCP announcement: https://www.anthropic.com/news/model-context-protocol
  - MCP donation to AAIF: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
  - Community directories (note: 7,260 number not verified in search results)
- **Proposed citation keys**: `anthropic-mcp-docs`, `anthropic-mcp-announcement`, `anthropic-mcp-aaif`

#### Line 88-91: Retrieval-Augmented Generation (RAG)
- **File**: 04-perception.tex
- **Lines**: 88-91
- **Claim**: "Retrieval-Augmented Generation, or RAG, enables semantic search over document archives... Vector stores power this semantic search by encoding documents as high-dimensional embeddings."
- **Recommended sources**:
  - AWS RAG overview: https://aws.amazon.com/what-is/retrieval-augmented-generation/
  - Google Cloud RAG: https://cloud.google.com/use-cases/retrieval-augmented-generation
  - Original RAG paper (if applicable)
- **Proposed citation key**: `rag-overview-2024`, `rag-lewis-2020` (if citing original paper)

#### Line 105: Authority and Case Law
- **File**: 04-perception.tex
- **Line**: 105
- **Claim**: "Authority weighting ensures that primary authority such as statutes and binding precedent ranks higher than secondary sources."
- **Recommended source**: Legal research methodology texts or law library guides
- **Proposed citation key**: `legal-research-authority`

#### Line 109-110: Financial Identifiers
- **File**: 04-perception.tex
- **Lines**: 109-110
- **Claim**: "Financial identifiers proliferate, including ticker symbols, CUSIP numbers, ISIN codes, and Legal Entity Identifiers."
- **Recommended sources**:
  - CUSIP Global Services: https://www.cusip.com/identifiers.html
  - ISO 6166 for ISIN
  - Wikipedia articles as secondary references
- **Proposed citation key**: `financial-identifiers-cusip`, `isin-iso-6166`

#### Line 142: Deadline Calculations
- **File**: 04-perception.tex
- **Line**: 142
- **Claim**: "Federal Rules require answers within 21 days"
- **Recommended source**: Federal Rules of Civil Procedure Rule 12(a)
- **Proposed citation key**: `frcp-rule-12a`
- **URL**: https://www.law.cornell.edu/rules/frcp/rule_12

#### Line 148: Citation Formatting
- **File**: 04-perception.tex
- **Line**: 148
- **Claim**: "Citation formatters convert case information into proper Bluebook format"
- **Recommended source**: The Bluebook: A Uniform System of Citation
- **Proposed citation key**: `bluebook-21st`
- **URL**: https://www.legalbluebook.com/

---

### Section 05: Action (05-action.tex)

#### Line 37: CM/ECF Court Filing System
- **File**: 05-action.tex
- **Line**: 37
- **Claim**: "Court filings through CM/ECF or state systems become part of the public record once submitted."
- **Recommended sources**:
  - Official CM/ECF documentation: https://www.uscourts.gov/court-records/electronic-filing-cm-ecf
  - PACER CM/ECF guide
- **Proposed citation key**: `cmecf-uscourts`

#### Line 37: Regulatory Submissions
- **File**: 05-action.tex
- **Line**: 37
- **Claim**: "Regulatory submissions through EDGAR, FINRA, and state regulatory systems"
- **Recommended sources**:
  - SEC EDGAR: https://www.sec.gov/submit-filings/about-edgar
  - FINRA overview: https://www.finra.org/about
- **Proposed citation keys**: `sec-edgar-about`, `finra-about`

#### Line 100: Prompt Injection Security
- **File**: 05-action.tex
- **Line**: 100
- **Claim**: "Prompt injection through action parameters occurs when adversaries embed instructions in parameters the agent passes to action tools."
- **Recommended source**:
  - OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - OWASP Prompt Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
- **Proposed citation key**: `owasp-llm01-2025`, `owasp-prompt-injection-cheatsheet`

#### Line 100: Privilege Escalation
- **File**: 05-action.tex
- **Line**: 100
- **Claim**: "Privilege escalation through tool chaining happens when an agent chains multiple tools to achieve capabilities no single tool grants."
- **Recommended source**: LLM security research papers or OWASP materials
- **Proposed citation key**: `llm-tool-chaining-security`
- **Action needed**: Additional search for specific research on tool chaining attacks

---

## Additional Cross-Cutting Citations Needed

### Tool Use and Function Calling
**Sections affected**: All three sections reference tool use concepts

**Claims**:
- Discussion of tools, perception tools, action tools throughout
- ReAct pattern (not explicitly cited but implied in the architecture)
- Function calling mechanisms

**Recommended sources**:
- ReAct paper: Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", ICLR 2023
  - arXiv: https://arxiv.org/abs/2210.03629
  - Project page: https://react-lm.github.io/
- OpenAI function calling documentation: https://platform.openai.com/docs/guides/function-calling
- Anthropic tool use documentation

**Proposed citation keys**: `yao-react-2023`, `openai-function-calling`, `anthropic-tool-use`

### Language Server Protocol (Referenced in MCP discussion)
**Section**: 04-perception.tex, Line 69-71

**Claim**: "MCP deliberately re-uses the message-flow ideas of the Language Server Protocol (LSP) and is transported over JSON-RPC 2.0"

**Recommended source**:
- Official LSP specification: https://microsoft.github.io/language-server-protocol/
- LSP overview documentation

**Proposed citation key**: `lsp-specification-microsoft`

---

## Proposed BibTeX Entries

```bibtex
% ============================================================================
% Model Context Protocol (MCP)
% ============================================================================

@online{anthropic-mcp-docs,
  author = {{Anthropic}},
  title = {What is the Model Context Protocol (MCP)?},
  year = {2024},
  url = {https://docs.anthropic.com/en/docs/mcp},
  urldate = {2025-12-13},
  note = {Official documentation for the Model Context Protocol, standardizing how AI agents access external tools and data sources}
}

@online{anthropic-mcp-announcement,
  author = {{Anthropic}},
  title = {Introducing the Model Context Protocol},
  year = {2024},
  month = nov,
  url = {https://www.anthropic.com/news/model-context-protocol},
  urldate = {2025-12-13},
  note = {Official announcement of MCP as an open-source standard for connecting AI applications to external systems}
}

@online{anthropic-mcp-aaif,
  author = {{Anthropic}},
  title = {Donating the Model Context Protocol and Establishing the Agentic AI Foundation},
  year = {2025},
  month = dec,
  url = {https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation},
  urldate = {2025-12-13},
  note = {Announcement of MCP donation to the Agentic AI Foundation under the Linux Foundation, with support from major technology companies}
}

% ============================================================================
% ReAct and Tool Use
% ============================================================================

@inproceedings{yao-react-2023,
  author = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  title = {ReAct: Synergizing Reasoning and Acting in Language Models},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2023},
  url = {https://arxiv.org/abs/2210.03629},
  urldate = {2025-12-13},
  note = {Foundational paper introducing ReAct pattern for interleaving reasoning traces with actions in language model agents}
}

@online{openai-function-calling,
  author = {{OpenAI}},
  title = {Function Calling},
  year = {2024},
  url = {https://platform.openai.com/docs/guides/function-calling},
  urldate = {2025-12-13},
  note = {Official documentation for function calling in OpenAI API, allowing models to call external functions with structured outputs}
}

% ============================================================================
% Retrieval-Augmented Generation (RAG)
% ============================================================================

@online{aws-rag-overview,
  author = {{Amazon Web Services}},
  title = {What is RAG? - Retrieval-Augmented Generation AI Explained},
  year = {2024},
  url = {https://aws.amazon.com/what-is/retrieval-augmented-generation/},
  urldate = {2025-12-13},
  note = {Overview of RAG architecture for enhancing LLM responses with external knowledge retrieval}
}

@online{google-rag-overview,
  author = {{Google Cloud}},
  title = {What is Retrieval-Augmented Generation (RAG)?},
  year = {2024},
  url = {https://cloud.google.com/use-cases/retrieval-augmented-generation},
  urldate = {2025-12-13},
  note = {Technical overview of RAG implementation patterns and use cases in enterprise AI systems}
}

% ============================================================================
% Legal Systems and Databases
% ============================================================================

@online{pacer-system,
  author = {{Administrative Office of the U.S. Courts}},
  title = {Public Access to Court Electronic Records (PACER)},
  year = {2024},
  url = {https://pacer.uscourts.gov/},
  urldate = {2025-12-13},
  note = {Official PACER system providing electronic public access to federal court records}
}

@online{cmecf-uscourts,
  author = {{Administrative Office of the U.S. Courts}},
  title = {Electronic Filing (CM/ECF)},
  year = {2024},
  url = {https://www.uscourts.gov/court-records/electronic-filing-cm-ecf},
  urldate = {2025-12-13},
  note = {Case Management/Electronic Case Files system for filing federal court documents online}
}

@online{sec-edgar-about,
  author = {{U.S. Securities and Exchange Commission}},
  title = {About EDGAR},
  year = {2024},
  url = {https://www.sec.gov/submit-filings/about-edgar},
  urldate = {2025-12-13},
  note = {Electronic Data Gathering, Analysis, and Retrieval system for SEC filings}
}

@online{westlaw-lexis-overview,
  author = {{Georgetown Law Library}},
  title = {Lexis, Westlaw, \& Bloomberg Law},
  year = {2024},
  url = {https://www.law.georgetown.edu/library/databases/lexis-westlaw-bloomberg/},
  urldate = {2025-12-13},
  note = {Overview of major legal research databases and their capabilities}
}

@online{legal-dms-comparison,
  author = {{Legaltech Hub}},
  title = {Document Management Systems},
  year = {2024},
  url = {https://www.legaltechnologyhub.com/topics/documents/document-management/},
  urldate = {2025-12-13},
  note = {Comparison of legal document management systems including iManage and NetDocuments}
}

@book{bluebook-21st,
  title = {The Bluebook: A Uniform System of Citation},
  edition = {21st},
  year = {2020},
  publisher = {Harvard Law Review Association},
  note = {Standard citation manual for legal documents in the United States}
}

@online{frcp-rule-12a,
  author = {{Legal Information Institute}},
  title = {Rule 12. Defenses and Objections: When and How Presented},
  booktitle = {Federal Rules of Civil Procedure},
  year = {2024},
  url = {https://www.law.cornell.edu/rules/frcp/rule_12},
  urldate = {2025-12-13},
  note = {Federal rule establishing 21-day deadline for answers and other pleading requirements}
}

% ============================================================================
% Financial Systems and Identifiers
% ============================================================================

@online{financial-data-platforms-2024,
  author = {{Wall Street Prep}},
  title = {Bloomberg vs. Capital IQ (CapIQ) vs. Factset vs. Refinitiv},
  year = {2024},
  url = {https://www.wallstreetprep.com/knowledge/bloomberg-vs-capital-iq-vs-factset-vs-thomson-reuters-eikon/},
  urldate = {2025-12-13},
  note = {Comparison of major financial data platforms and their market positions}
}

@online{cusip-identifiers,
  author = {{CUSIP Global Services}},
  title = {About CGS Identifiers},
  year = {2024},
  url = {https://www.cusip.com/identifiers.html},
  urldate = {2025-12-13},
  note = {Overview of CUSIP, CINS, and other financial security identification systems}
}

@online{isin-iso-6166,
  author = {{International Organization for Standardization}},
  title = {ISO 6166:2021 - Securities and related financial instruments - International securities identification numbering system (ISIN)},
  year = {2021},
  url = {https://www.iso.org/standard/78502.html},
  urldate = {2025-12-13},
  note = {International standard for ISIN codes used globally for securities identification}
}

@online{finra-about,
  author = {{Financial Industry Regulatory Authority}},
  title = {About FINRA},
  year = {2024},
  url = {https://www.finra.org/about},
  urldate = {2025-12-13},
  note = {Overview of FINRA's role as self-regulatory organization for U.S. securities firms}
}

@online{var-overview,
  author = {{Corporate Finance Institute}},
  title = {Value at Risk - Learn About Assessing and Calculating VaR},
  year = {2024},
  url = {https://corporatefinanceinstitute.com/resources/career-map/sell-side/risk-management/value-at-risk-var/},
  urldate = {2025-12-13},
  note = {Overview of Value at Risk as a financial risk metric}
}

% ============================================================================
% Security and Safety
% ============================================================================

@online{owasp-llm01-2025,
  author = {{OWASP Foundation}},
  title = {LLM01:2025 Prompt Injection},
  booktitle = {OWASP Gen AI Security Project},
  year = {2025},
  url = {https://genai.owasp.org/llmrisk/llm01-prompt-injection/},
  urldate = {2025-12-13},
  note = {OWASP Top 10 for LLM Applications 2025: Prompt injection vulnerabilities and mitigations}
}

@online{owasp-prompt-injection-cheatsheet,
  author = {{OWASP Foundation}},
  title = {LLM Prompt Injection Prevention Cheat Sheet},
  booktitle = {OWASP Cheat Sheet Series},
  year = {2025},
  url = {https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html},
  urldate = {2025-12-13},
  note = {Practical guidance for preventing prompt injection attacks in LLM applications}
}

% ============================================================================
% Technical Standards and Protocols
% ============================================================================

@online{lsp-specification-microsoft,
  author = {{Microsoft}},
  title = {Language Server Protocol Specification},
  year = {2024},
  url = {https://microsoft.github.io/language-server-protocol/},
  urldate = {2025-12-13},
  note = {Official specification for the Language Server Protocol, which influenced MCP design}
}
```

---

## Existing Citations to Fix/Remove

### Current Status
**Sections 03-05 contain ZERO citations.** This is a critical gap for a textbook targeting legal and financial professionals who expect authoritative sourcing.

### Citations Missing from Cross-References
The sections reference several concepts from other chapters that should have citations:
- GPA framework (referenced but not cited to where it's defined)
- Memory systems (forward reference to sec:agents2-memory)
- Planning (forward reference to sec:agents2-planning)
- Termination (forward reference to sec:agents2-termination)
- Escalation (forward reference to sec:agents2-escalation)

These are internal cross-references (using `\Cref`) which are appropriate, but the original introduction of concepts like GPA should cite authoritative sources.

---

## Additional Research Required

### High Priority - Needs Specific Sources

1. **LLM Clarification Behavior** (Line 156, 03-intent.tex)
   - Need academic papers on when LLMs ask for clarification vs. making assumptions
   - Search terms: "LLM uncertainty quantification", "LLM calibration", "clarification questions dialogue systems"
   - Consider: Anthropic's research on AI assistance, OpenAI's research papers

2. **Tool Chaining Security** (Line 100, 05-action.tex)
   - Need specific research on privilege escalation through tool composition
   - Search terms: "LLM tool chaining attacks", "agent security composition", "multi-tool privilege escalation"

3. **MCP Server Count** (Line 76, 04-perception.tex)
   - Claim: "over 7,260 MCP servers"
   - Could not verify this specific number in search results
   - Found references to "6880+ servers" in PulseMCP directory
   - Action: Either verify the 7,260 number or update to verifiable count with citation to specific directory

### Medium Priority - General Knowledge Areas

4. **Legal Research Methodology**
   - Standard texts on legal research for authority hierarchy discussion
   - Consider: "Legal Research in a Nutshell" or similar standard references

5. **Financial Risk Management Standards**
   - Authoritative sources on VaR, duration, and other risk metrics beyond basic definitions
   - Consider: BIS publications, GARP references, CFA Institute materials

---

## Citation Density Recommendations

### Current State
- **Section 03 (Intent)**: 0 citations across 259 lines
- **Section 04 (Perception)**: 0 citations across 215 lines
- **Section 05 (Action)**: 0 citations across 172 lines
- **Total**: 0 citations across 646 lines of substantive content

### Target State
For a professional textbook in law and finance:
- **Minimum acceptable**: 15-20 citations across these three sections
- **Good practice**: 25-35 citations
- **Excellent**: 40+ citations with mix of primary sources, standards, and research

### Recommended Citation Points (Minimum Set)
1. MCP official documentation (3 citations: docs, announcement, AAIF donation)
2. ReAct paper (1 citation)
3. Function calling documentation (1 citation)
4. RAG overview (1-2 citations)
5. PACER/CM/ECF systems (2 citations)
6. EDGAR system (1 citation)
7. Legal research databases (1 citation)
8. Financial data platforms (1 citation)
9. Financial identifiers (2 citations: CUSIP, ISIN)
10. FRCP Rule 12(a) (1 citation)
11. Bluebook (1 citation)
12. OWASP LLM security (2 citations)
13. LSP specification (1 citation)
14. FINRA (1 citation)

**Minimum total: 19 citations** to establish basic credibility

---

## Implementation Notes

### Priority Order for Adding Citations

**Phase 1 - Critical Infrastructure** (Do immediately):
1. MCP citations (foundational to the architecture discussion)
2. Legal systems (PACER, EDGAR, CM/ECF) - these are factual claims about government systems
3. OWASP security citations - security claims need authoritative backing

**Phase 2 - Technical Foundations** (Next):
4. ReAct and function calling
5. RAG and semantic search
6. LSP specification

**Phase 3 - Domain References** (Final):
7. Legal research platforms and citation standards
8. Financial platforms and identifiers
9. Risk metrics and standards

### Citation Style Notes
- Use `\parencite{}` for parenthetical citations
- Use `\textcite{}` for narrative citations
- Include specific page numbers or section references where applicable
- For online sources, always include `urldate` field
- Add brief `note` field explaining relevance to help readers evaluate source quality

### Cross-Reference with CLAUDE.md Guidance
Per the project's CLAUDE.md guidelines:
- Use authoryear citation style (BibLaTeX)
- Always include urldate for web sources
- Prefer primary, dated, link-stable sources
- For government systems (PACER, EDGAR, FINRA), use official .gov/.org sources
- For standards (OWASP, ISO), use official specification sources
- For research, prefer peer-reviewed venues

---

## Sources

The following sources were consulted in preparing this citation analysis:

- [Model Context Protocol - Anthropic Documentation](https://docs.anthropic.com/en/docs/mcp)
- [Introducing the Model Context Protocol - Anthropic](https://www.anthropic.com/news/model-context-protocol)
- [Donating MCP to AAIF - Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [ReAct: Synergizing Reasoning and Acting in Language Models - arXiv](https://arxiv.org/abs/2210.03629)
- [Function Calling - OpenAI API](https://platform.openai.com/docs/guides/function-calling)
- [What is RAG? - AWS](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [Retrieval-Augmented Generation - Google Cloud](https://cloud.google.com/use-cases/retrieval-augmented-generation)
- [LLM01:2025 Prompt Injection - OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [LLM Prompt Injection Prevention Cheat Sheet - OWASP](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
- [PACER - Federal Court Records](https://pacer.uscourts.gov/)
- [CM/ECF - U.S. Courts](https://www.uscourts.gov/court-records/electronic-filing-cm-ecf)
- [About EDGAR - SEC](https://www.sec.gov/submit-filings/about-edgar)
- [Lexis, Westlaw, & Bloomberg Law - Georgetown Law Library](https://www.law.georgetown.edu/library/databases/lexis-westlaw-bloomberg/)
- [Federal Rules of Civil Procedure Rule 12 - Cornell LII](https://www.law.cornell.edu/rules/frcp/rule_12)
- [About CGS Identifiers - CUSIP](https://www.cusip.com/identifiers.html)
- [Language Server Protocol Specification - Microsoft](https://microsoft.github.io/language-server-protocol/)
- [About FINRA](https://www.finra.org/about)
- [Bloomberg vs. Other Financial Data Platforms - Wall Street Prep](https://www.wallstreetprep.com/knowledge/bloomberg-vs-capital-iq-vs-factset-vs-thomson-reuters-eikon/)
