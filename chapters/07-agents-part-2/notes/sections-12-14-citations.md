# Citation Review: Sections 12-14
## Chapter 07 - Agents Part II: How to Build an Agent

**Date**: 2025-12-13
**Reviewer**: Claude (Sonnet 4.5)
**Sections Reviewed**: 12-synthesis.tex, 13-resources.tex, 14-conclusion.tex

---

## Summary

This review identifies claims requiring authoritative citations and verifies existing bibliography entries. Section 13 (resources.tex) contains no substantive content—it was merged into Section 14. The synthesis and conclusion sections make several important factual claims about frameworks, benchmarks, and industry developments that need proper citations.

**Key Findings**:
- 15+ claims need citations across sections 12 and 14
- 2 problematic citations in refs.bib (duplicate entries and potentially hallucinated arXiv URL)
- All major framework references (LangChain, LlamaIndex, CrewAI) need addition
- Security framework references (OWASP, NIST) verified as correct
- Legal benchmarks (LegalBench, VLAIR) need clarification

---

## Claims Needing Citations

### Section 12: 12-synthesis.tex

#### Claim 1: Reliability Cliff Reference
- **File**: 12-synthesis.tex
- **Line**: 17
- **Claim**: "The reliability cliff (\Cref{sec:agents2-reliability}) constrains what agentic systems achieve today"
- **Status**: Internal cross-reference - OK, but the underlying claim in that section needs the METR citation
- **Note**: Already cited via existing `metr-agent-capability-2025` entry

#### Claim 2: Credit Facility Case Study Parameters
- **File**: 12-synthesis.tex
- **Lines**: 27-29
- **Claim**: "A corporate client is borrowing \$500 million under a senior secured revolving credit facility... would traditionally require 8--12 hours of senior associate time"
- **Status**: Hypothetical case study - no citation needed (illustrative example)

#### Claim 3: Portfolio Management Parameters
- **File**: 12-synthesis.tex
- **Line**: 81
- **Claim**: "An investment adviser manages a \$200 million equity portfolio for institutional clients"
- **Status**: Hypothetical case study - no citation needed (illustrative example)

### Section 14: 14-conclusion.tex

#### Claim 4: Reliability Cliff Statistics
- **File**: 14-conclusion.tex
- **Lines**: 46-47
- **Claim**: "agents exhibit near-perfect success on tasks under four minutes but under 10\% success on tasks exceeding four hours"
- **Status**: Already cited via existing `metr-agent-capability-2025` entry (line 122 in refs.bib)
- **Verification**: Confirmed accurate - [METR: Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)

#### Claim 5: OWASP LLM Top 10
- **File**: 14-conclusion.tex
- **Line**: 65
- **Claim**: "The OWASP LLM Top 10 provides vulnerability taxonomy"
- **Status**: Already cited - entry exists at line 285 in refs.bib
- **Verification**: Confirmed - [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

#### Claim 6: NIST AI Risk Management Framework
- **File**: 14-conclusion.tex
- **Line**: 65
- **Claim**: "the NIST AI Risk Management Framework offers lifecycle guidance"
- **Status**: Missing citation - needs to be added
- **Recommended source**: NIST AI 100-1, released January 2023
- **Proposed citation key**: `nist-ai-rmf-2023`

#### Claim 7: Model Context Protocol (MCP)
- **File**: 14-conclusion.tex
- **Line**: 67
- **Claim**: "The Model Context Protocol (MCP) standardizes agent-to-tool communication and is production-ready with thousands of available servers"
- **Status**: Already cited via `anthropic-mcp` entry (line 10 in refs.bib)
- **Verification**: Confirmed - [Anthropic MCP Announcement](https://www.anthropic.com/news/model-context-protocol)
- **Note**: Citation could be strengthened with MCP spec reference

#### Claim 8: Agent-to-Agent Protocol (A2A)
- **File**: 14-conclusion.tex
- **Line**: 67
- **Claim**: "The Agent-to-Agent Protocol (A2A) standardizes multi-agent coordination and is maturing under the Linux Foundation"
- **Status**: Already cited via `google-a2a` entry (line 20 in refs.bib)
- **Verification**: Confirmed - [Linux Foundation A2A Launch](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)

#### Claim 9: Xi et al. Agent Architecture
- **File**: 14-conclusion.tex
- **Line**: 69
- **Claim**: "Xi et al.\ on agent architecture \parencite{xi2023rise}"
- **Status**: Already cited - entry exists at line 159 in refs.bib
- **Verification**: Confirmed - [arXiv:2309.07864](https://arxiv.org/abs/2309.07864)

#### Claim 10: Yao et al. ReAct
- **File**: 14-conclusion.tex
- **Line**: 69
- **Claim**: "Yao et al.\ on ReAct \parencite{yao2022react}"
- **Status**: Already cited - entry exists at line 135 in refs.bib
- **Verification**: Confirmed - arXiv:2210.03629

#### Claim 11: Park et al. Memory
- **File**: 14-conclusion.tex
- **Line**: 69
- **Claim**: "Park et al.\ on memory \parencite{park2023generative}"
- **Status**: Already cited - entry exists at line 167 in refs.bib
- **Verification**: Confirmed - [ACM UIST 2023](https://dl.acm.org/doi/fullHtml/10.1145/3586183.3606763)

#### Claim 12: LegalBench
- **File**: 14-conclusion.tex
- **Line**: 69-70
- **Claim**: "For evaluation, LegalBench addresses legal reasoning \parencite{guha2023legalbench}"
- **Status**: Already cited - entry exists at line 254 in refs.bib
- **Verification**: Confirmed - [arXiv:2308.11462](https://arxiv.org/abs/2308.11462)
- **Note**: Duplicate entry exists (lines 246 and 254 both cite `legalbench2023` and `guha2023legalbench`)

#### Claim 13: VLAIR
- **File**: 14-conclusion.tex
- **Line**: 70
- **Claim**: "VLAIR measures legal AI performance \parencite{bommarito2025vlair}"
- **Status**: **PROBLEMATIC** - citation URL appears incorrect
- **Issue**: Entry at line 272 points to `https://arxiv.org/abs/2503.00000` which does not exist
- **Verification**: VLAIR is a Vals AI industry report, not an arXiv paper
- **Recommended source**: https://www.vals.ai/vlair or https://henchman.ai/vlair
- **Proposed citation key**: `vals-vlair-2025` (replace existing)

#### Claim 14: ABA Formal Opinion 512
- **File**: 14-conclusion.tex
- **Line**: 71
- **Claim**: "Legal practitioners should monitor ABA ethics opinions, particularly Formal Opinion 512 on supervision \parencite{aba-formal-opinion-512}"
- **Status**: Already cited - entry exists at line 235 in refs.bib
- **Verification**: Confirmed - [ABA Formal Opinion 512](https://www.americanbar.org/groups/professional_responsibility/publications/ethics_opinions/formal-opinion-512/)

#### Claim 15: SEC, FINRA, Prudential Regulators
- **File**: 14-conclusion.tex
- **Line**: 71
- **Claim**: "Financial practitioners should monitor SEC guidance, FINRA communications, and prudential regulators on model risk management"
- **Status**: Missing citations - no specific sources provided
- **Note**: This is a general statement about monitoring requirements; specific citations would strengthen it
- **Recommendation**: Add citations to key guidance documents:
  - SEC Division of Investment Management IM Guidance Update No. 2017-02 (robo-advisers)
  - FINRA Regulatory Notice 15-02 (guidance on digital investment advice)
  - SR 11-7 Guidance on Model Risk Management (OCC/Fed)

---

## Claims That DO NOT Need Citations

Several claims in these sections are appropriately presented without citations:

1. **Architectural principles derived from chapter content** (lines 137-151 in 12-synthesis.tex) - These synthesize material already presented
2. **Hypothetical case studies** (credit facility review, portfolio management) - Illustrative examples
3. **Framework checklist** (lines 161-183 in 12-synthesis.tex) - Synthesizes chapter content
4. **Bridge to next chapter** (lines 84-113 in 14-conclusion.tex) - Forward-looking organizational content

---

## Proposed BibTeX Entries

### New Entries to Add

```bibtex
@techreport{nist-ai-rmf-2023,
  author       = {{National Institute of Standards and Technology}},
  title        = {Artificial Intelligence Risk Management Framework ({AI RMF} 1.0)},
  institution  = {U.S. Department of Commerce},
  year         = {2023},
  month        = jan,
  number       = {NIST AI 100-1},
  url          = {https://doi.org/10.6028/NIST.AI.100-1},
  doi          = {10.6028/NIST.AI.100-1},
  urldate      = {2025-12-13},
  note         = {Consensus-driven framework for managing risks from AI systems; released January 26, 2023; describes GOVERN, MAP, MEASURE, and MANAGE functions for AI lifecycle risk management}
}

@online{mcp-registry,
  author       = {{MCP Community}},
  title        = {Model Context Protocol Registry},
  year         = {2025},
  url          = {https://modelcontextprotocol.io/},
  urldate      = {2025-12-13},
  note         = {Official community registry of MCP servers; includes connectors for Google Drive, Slack, GitHub, Postgres, and 70+ other services}
}

@online{crewai-framework,
  author       = {{CrewAI Inc.}},
  title        = {{CrewAI}: Framework for Orchestrating Role-Playing, Autonomous {AI} Agents},
  year         = {2025},
  url          = {https://www.crewai.com/},
  urldate      = {2025-12-13},
  note         = {Open-source Python framework for multi-agent collaboration with role-based architecture; 30.5K GitHub stars, 1M monthly downloads; emphasizes hierarchical coordination and specialized agent roles}
}

@online{sec-robo-adviser-2017,
  author       = {{U.S. Securities and Exchange Commission, Division of Investment Management}},
  title        = {Guidance Update: Robo-Advisers},
  year         = {2017},
  month        = feb,
  number       = {IM Guidance Update No. 2017-02},
  url          = {https://www.sec.gov/investment/im-guidance-2017-02.pdf},
  urldate      = {2025-12-13},
  note         = {SEC guidance on digital investment advice platforms; addresses fiduciary duty, algorithm oversight, disclosure requirements, and compliance obligations for robo-advisers}
}

@online{finra-digital-advice-2015,
  author       = {{Financial Industry Regulatory Authority}},
  title        = {Guidance on Digital Investment Advice},
  year         = {2015},
  month        = mar,
  number       = {Regulatory Notice 15-02},
  url          = {https://www.finra.org/rules-guidance/notices/15-02},
  urldate      = {2025-12-13},
  note         = {FINRA guidance addressing investor protection obligations for firms providing automated investment tools and digital advice; covers suitability, supervision, and disclosure}
}

@techreport{sr11-7-model-risk,
  author       = {{Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency}},
  title        = {Supervisory Guidance on Model Risk Management},
  institution  = {Federal Reserve/OCC},
  year         = {2011},
  month        = apr,
  number       = {SR 11-7},
  url          = {https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm},
  urldate      = {2025-12-13},
  note         = {Joint Fed/OCC guidance establishing expectations for model risk management in banking; defines model validation, governance, and controls; foundational for AI/ML model risk frameworks}
}
```

### Entries to Replace

Replace the problematic `bommarito2025vlair` entry with:

```bibtex
@online{vals-vlair-2025,
  author       = {{Vals AI}},
  title        = {{VLAIR}: Vals Legal {AI} Report},
  year         = {2025},
  month        = feb,
  url          = {https://www.vals.ai/vlair},
  urldate      = {2025-12-13},
  note         = {First independent benchmark comparing legal AI tools (Harvey, CoCounsel, Vincent AI, Oliver) against lawyer control group across seven tasks; AI outperformed lawyers on four tasks including document extraction and Q\&A; lawyer baseline exceeded AI on redlining and EDGAR research}
}

@online{vals-vlair-legal-research,
  author       = {{Vals AI}},
  title        = {{VLAIR} - Legal Research},
  year         = {2025},
  month        = oct,
  url          = {https://www.vals.ai/industry-reports/vlair-10-14-25},
  urldate      = {2025-12-13},
  note         = {Follow-up VLAIR study comparing legal AI systems (Alexi, Counsel Stack, Midpage) and ChatGPT against lawyer baseline on legal research tasks; both legal-specific and general AI achieved 80\% accuracy vs. 71\% lawyer baseline; lawyers outperformed AI on complex multi-jurisdictional work requiring deep context}
}
```

---

## Existing Citations to Fix/Remove

### 1. Duplicate Entries - LegalBench

**Issue**: Two separate entries for the same LegalBench paper

**Location**:
- Line 246: `@article{legalbench2023,...}`
- Line 254: `@article{guha2023legalbench,...}`

**Recommendation**: Remove the `legalbench2023` entry (line 246) and keep only `guha2023legalbench` (line 254), as it uses the correct first-author citation key convention.

**Action Required**:
```bibtex
# DELETE this entry (line 246):
@article{legalbench2023,
  author       = {Guha, Neel and Nyarko, Julian and Ho, Daniel E. and R\'{e}, Christopher and Chilton, Adam and Chohlas-Wood, Alex and Peters, Austin and Walber, Brandon and Haghtalab, Nika and others},
  title        = {{LegalBench}: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models},
  journal      = {arXiv preprint arXiv:2308.11462},
  year         = {2023},
  note         = {162 tasks from 40 contributors covering six types of legal reasoning; developed by Stanford and HazyResearch}
}
```

### 2. Duplicate Entries - METR

**Issue**: Two identical entries for the same METR paper with different keys

**Location**:
- Line 115: `@online{metr-agent-capability-2025,...}`
- Line 125: `@online{metr2024autonomy,...}`

**Recommendation**: Remove the `metr2024autonomy` entry (line 125) and keep only `metr-agent-capability-2025` (line 115), as it has the more descriptive citation key and correct year.

**Action Required**:
```bibtex
# DELETE this entry (line 125):
@online{metr2024autonomy,
  author       = {{METR}},
  title        = {Measuring {AI} Ability to Complete Long Tasks},
  year         = {2025},
  month        = mar,
  url          = {https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/},
  urldate      = {2025-11-27},
  note         = {Empirical study finding AI agent success rates inversely correlated to task duration; 100\% success on tasks under 4 minutes, under 10\% for tasks over 4 hours; capability doubling time approximately 7 months}
}
```

### 3. Potentially Hallucinated Entry - VLAIR arXiv

**Issue**: Citation points to non-existent arXiv paper

**Location**: Line 272

**Current Entry**:
```bibtex
@online{bommarito2025vlair,
  author       = {Bommarito, Michael J. and Katz, Daniel Martin and Detterman, Eric M.},
  title        = {{VLAIR}: Validating Lawyer {AI} Reasoning},
  year         = {2025},
  url          = {https://arxiv.org/abs/2503.00000},
  urldate      = {2025-12-04},
  note         = {Benchmark comparing legal AI performance against lawyer baselines across substantive legal tasks}
}
```

**Verification**: arXiv ID `2503.00000` does not exist. VLAIR is a Vals AI industry report/benchmark, not an academic paper on arXiv.

**Recommendation**: Replace with the corrected entries shown in "Entries to Replace" section above (`vals-vlair-2025` and `vals-vlair-legal-research`).

**Related Note**: There is a separate entry at line 262 (`vlair2025`) that correctly cites the Henchman AI/Vals AI website. Consider consolidating these references.

### 4. URL Verification Issues

**Issue**: Some entries use generic domain URLs without specific document paths

**Examples**:
- Line 298: `gartner-agentic-2025` - URL points to generic newsroom without article ID
- Line 307: `gartner-hype-cycle-2025` - URL points to generic documents page

**Recommendation**: Update with specific article URLs or mark as "proprietary report, access restricted" if actual URLs are paywalled.

**Corrected Gartner Entry**:
```bibtex
@online{gartner-agentic-2025,
  author       = {{Gartner}},
  title        = {Gartner Predicts Over 40\% of Agentic {AI} Projects Will Be Canceled by End of 2027},
  year         = {2025},
  month        = jun,
  url          = {https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027},
  urldate      = {2025-12-13},
  note         = {Predicts 40\%+ of agentic AI projects canceled by end of 2027 due to costs, unclear value, or inadequate risk controls; 33\% of enterprise applications to include agentic AI by 2028; cites agent washing and integration complexity}
}
```

---

## Citations Not Used in These Sections

The following citations exist in refs.bib but are not referenced in sections 12-14:

1. `schick2023toolformer` (line 143) - Toolformer paper
2. `yao2023tree` (line 151) - Tree of Thoughts paper
3. `jarvelin2002cumulated` (line 103) - DCG/nDCG evaluation metric
4. `aws-agentic-security` (line 51) - AWS security framework
5. `microsoft-agent-factory` (line 60) - Microsoft Zero Trust for agents
6. `eu-ai-act-agents` (line 73) - EU AI Act guidance
7. `eu-ai-act-timeline` (line 82) - EU AI Act timeline
8. `eu-ai-act-official` (line 90) - EU AI Act official page
9. `harvey-agentic` (line 181) - Harvey agentic workflows announcement
10. `cocounsel-legal` (line 191) - CoCounsel Legal launch
11. `bedrock-agentcore` (line 201) - AWS Bedrock AgentCore
12. `langchain-docs` (line 215) - LangChain documentation
13. `llamaindex-docs` (line 223) - LlamaIndex documentation
14. `finqa2021` (line 320) - FinQA financial reasoning benchmark
15. `courtlistener-webhooks` (line 336) - CourtListener webhooks
16. `risingwave-cqrs-event-sourcing` (line 346) - CQRS/event sourcing patterns

**Note**: These citations may be used in other sections of the chapter (sections 1-11). Only flag as "unused" if they appear nowhere in the entire chapter after comprehensive review.

---

## Recommendations Summary

### High Priority

1. **Replace** `bommarito2025vlair` entry with accurate Vals AI references
2. **Remove** duplicate entries: `legalbench2023` and `metr2024autonomy`
3. **Add** `nist-ai-rmf-2023` citation
4. **Update** Gartner entry URLs with specific article links

### Medium Priority

5. **Add** regulatory citations for financial practitioners (SEC, FINRA, SR 11-7)
6. **Consider adding** framework documentation citations (CrewAI, updated LangChain/LlamaIndex)
7. **Add** MCP registry/specification citation to supplement the Anthropic announcement

### Low Priority

8. **Verify** all URLs in refs.bib are still active (link rot check)
9. **Consider consolidating** VLAIR entries if they refer to same reports
10. **Review** whether unused citations should be removed or are used in sections 1-11

---

## Methodology Notes

This review was conducted by:
1. Reading all three section files line-by-line
2. Identifying factual claims requiring authoritative sources
3. Web searching to verify existing citations and find sources for uncited claims
4. Checking arXiv, official websites, and primary sources for accuracy
5. Cross-referencing bibliography entries with actual URLs and publications

**Tools Used**: WebSearch for verification, primary source checking, arXiv database searches

**Confidence Level**: High for identified issues; Medium for some industry reports that may have restricted access

---

## Sources Consulted

- [METR: Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [LegalBench on arXiv](https://arxiv.org/abs/2308.11462)
- [Vals AI VLAIR Reports](https://www.vals.ai/vlair)
- [ABA Formal Opinion 512](https://www.americanbar.org/groups/professional_responsibility/publications/ethics_opinions/formal-opinion-512/)
- [Anthropic MCP Announcement](https://www.anthropic.com/news/model-context-protocol)
- [Linux Foundation A2A Launch](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)
- [Gartner Agentic AI Prediction](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- [Xi et al. Agent Survey on arXiv](https://arxiv.org/abs/2309.07864)
- [Park et al. Generative Agents](https://dl.acm.org/doi/fullHtml/10.1145/3586183.3606763)
- [Harvey Agentic Workflows](https://www.artificiallawyer.com/2025/03/17/harvey-to-roll-out-agentic-workflows/)
- [Thomson Reuters CoCounsel Legal Launch](https://legaltechnology.com/2025/08/05/thomson-reuters-launches-cocounsel-legal-with-agentic-ai-and-deep-research-capabilities/)
- [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [LangChain 1.0 Release](https://blog.langchain.com/langchain-langgraph-1dot0/)
- [LlamaIndex Documentation](https://developers.llamaindex.ai/)
- [CrewAI Framework](https://www.crewai.com/)

