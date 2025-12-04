# Canonical Resources for Chapter 07

**Generated**: November 27, 2025
**Purpose**: New citations to add to Part II bibliography with complete BibLaTeX entries

---

## Already Cited in Part I

The following resources are already in the Chapter 06 bibliography and should NOT be duplicated:

- `yao2022react` — ReAct: Synergizing Reasoning and Acting in Language Models
- `shinn2023reflexion` — Reflexion: Language Agents with Verbal Reinforcement Learning
- `schick2024toolformer` — Toolformer: Language Models Can Teach Themselves to Use Tools
- `anthropic-mcp` — Introducing the Model Context Protocol
- `a2a-survey-2025` — A survey of agent interoperability protocols
- `langchain-agents-docs` — LangChain Agents Documentation
- `openai-agents-sdk` — OpenAI Agents SDK
- `legalagentbench` — LegalAgentBench
- `legalbench-github` — LegalBench benchmark suite
- `legalbench-rag` — LegalBench-Retrieve

---

## Priority 1: Must-Cite Resources

### 1. MemGPT (Memory Architecture)

**Relevance**: Canonical reference for hierarchical memory architecture in agents. OS-inspired approach highly relevant to legal/finance systems requiring long-term context.

**Relevant to**: `sec:agents2-memory`

```bibtex
@article{packer2023memgpt,
  author       = {Packer, Charles and Wooders, Sarah and Lin, Kevin and Fang, Vivian and Patil, Shishir G. and Stoica, Ion and Gonzalez, Joseph E.},
  title        = {{MemGPT}: Towards {LLMs} as Operating Systems},
  year         = {2023},
  eprint       = {2310.08560},
  archiveprefix = {arXiv},
  primaryclass = {cs.AI},
  url          = {https://arxiv.org/abs/2310.08560},
  urldate      = {2025-11-27},
  note         = {OS-inspired virtual context management with hierarchical memory (core/archival/recall); features self-editing memory and inner monologue; now productized as Letta platform}
}
```

---

### 2. Tree of Thoughts (Reasoning Patterns)

**Relevance**: Demonstrates advanced reasoning patterns beyond simple chain-of-thought. Relevant for complex legal reasoning tasks requiring exploration of alternatives.

**Relevant to**: `sec:agents2-planning`

```bibtex
@inproceedings{yao2023tot,
  author       = {Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L. and Cao, Yuan and Narasimhan, Karthik},
  title        = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
  booktitle    = {Advances in Neural Information Processing Systems 36 (NeurIPS 2023)},
  year         = {2023},
  eprint       = {2305.10601},
  archiveprefix = {arXiv},
  primaryclass = {cs.AI},
  url          = {https://arxiv.org/abs/2305.10601},
  urldate      = {2025-11-27},
  note         = {Introduces Tree of Thoughts framework enabling deliberate multi-path reasoning with lookahead and backtracking; achieved 74\% success on Game of 24 vs GPT-4's 4\% with chain-of-thought}
}
```

---

### 3. Agent2Agent Protocol (A2A)

**Relevance**: Critical emerging standard for agent-to-agent interoperability. Complements already-cited MCP (agent-to-tool).

**Relevant to**: `sec:agents2-protocols`

```bibtex
@online{google-a2a,
  author       = {{Google Developers}},
  title        = {Announcing the Agent2Agent Protocol ({A2A})},
  year         = {2025},
  url          = {https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/},
  urldate      = {2025-11-27},
  note         = {Open protocol for agent-to-agent communication using JSON-RPC 2.0 over HTTP; donated to Linux Foundation; features Agent Cards for capability discovery}
}

@online{a2a-spec,
  title        = {Agent2Agent Protocol Specification},
  year         = {2025},
  url          = {https://a2a-protocol.org/latest/},
  institution  = {Linux Foundation},
  urldate      = {2025-11-27},
  note         = {Official specification for A2A protocol enabling agent collaboration while preserving opacity}
}
```

---

### 4. AgentBench (Evaluation)

**Relevance**: First systematic multi-environment benchmark for evaluating LLM-as-Agent. Provides credible evaluation methodology.

**Relevant to**: `sec:agents2-eval`

```bibtex
@inproceedings{liu2023agentbench,
  author       = {Liu, Xiao and Yu, Hao and Zhang, Hanchen and Xu, Yifan and Lei, Xuanyu and Lai, Hanyu and Gu, Yu and Ding, Hangliang and Men, Kaiwen and Yang, Kejuan and Zhang, Shudan and Deng, Xiang and Zeng, Aohan and Du, Zhengxiao and Zhang, Chenhui and Shen, Sheng and Zhang, Tianjun and Su, Yu and Sun, Huan and Huang, Minlie and Dong, Yuxiao and Tang, Jie},
  title        = {{AgentBench}: Evaluating {LLMs} as Agents},
  booktitle    = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},
  year         = {2024},
  eprint       = {2308.03688},
  archiveprefix = {arXiv},
  primaryclass = {cs.AI},
  url          = {https://arxiv.org/abs/2308.03688},
  urldate      = {2025-11-27},
  note         = {First systematic benchmark with 8 distinct environments; tested 29 LLMs; identified poor long-term reasoning and instruction-following as main obstacles}
}
```

---

### 5. GAIA Benchmark (Evaluation)

**Relevance**: Tests fundamental agent capabilities with human-like robustness philosophy. Ideal for establishing baseline expectations.

**Relevant to**: `sec:agents2-eval`

```bibtex
@article{mialon2023gaia,
  author       = {Mialon, Gr\'{e}goire and Fourrier, Cl\'{e}mentine and Swift, Craig and Wolf, Thomas and LeCun, Yann and Scialom, Thomas},
  title        = {{GAIA}: A Benchmark for General {AI} Assistants},
  year         = {2023},
  eprint       = {2311.12983},
  archiveprefix = {arXiv},
  primaryclass = {cs.AI},
  url          = {https://arxiv.org/abs/2311.12983},
  urldate      = {2025-11-27},
  note         = {466 questions simple for humans (92\% accuracy) yet challenging for AI (GPT-4: 15\%); tests reasoning, multi-modality, web browsing, tool use; emphasizes ungameability and simplicity}
}
```

---

### 6. RAG (Foundational)

**Relevance**: Foundational technique underlying modern agent knowledge systems. Essential for grounding agent responses in external knowledge.

**Relevant to**: `sec:agents2-memory` (reference from Chapter 03)

```bibtex
@inproceedings{lewis2020rag,
  author       = {Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir and Goyal, Naman and K\"{u}ttler, Heinrich and Lewis, Mike and Yih, Wen-tau and Rockt\"{a}schel, Tim and Riedel, Sebastian and Kiela, Douwe},
  title        = {Retrieval-Augmented Generation for Knowledge-Intensive {NLP} Tasks},
  booktitle    = {Advances in Neural Information Processing Systems 33 (NeurIPS 2020)},
  year         = {2020},
  pages        = {9459--9474},
  eprint       = {2005.11401},
  archiveprefix = {arXiv},
  primaryclass = {cs.CL},
  url          = {https://arxiv.org/abs/2005.11401},
  urldate      = {2025-11-27},
  note         = {Foundational RAG paper combining parametric (seq2seq) and non-parametric (dense Wikipedia index) memory; achieved SOTA on three open-domain QA tasks}
}
```

---

### 7. OpenAI Function Calling

**Relevance**: Most widely adopted tool-use specification. Basis for many production agent systems.

**Relevant to**: `sec:agents2-tools`

```bibtex
@online{openai-function-calling,
  author       = {{OpenAI}},
  title        = {Function calling},
  year         = {2024},
  url          = {https://platform.openai.com/docs/guides/function-calling},
  urldate      = {2025-11-27},
  note         = {Official API documentation for connecting OpenAI models to external tools; supports Structured Outputs with strict JSON Schema compliance}
}
```

---

### 8. Plan-and-Execute Architecture

**Relevance**: Practical production pattern with proven cost/speed benefits. Directly applicable to legal/finance workflows.

**Relevant to**: `sec:agents2-planning`

```bibtex
@online{langchain-plan-execute,
  author       = {{LangChain}},
  title        = {Plan-and-Execute Agents},
  year         = {2024},
  url          = {https://blog.langchain.com/planning-agents/},
  urldate      = {2025-11-27},
  note         = {Decomposition architecture with separate planner and executor components; inspired by BabyAGI and Plan-and-Solve paper}
}
```

---

### 9. Memory Survey (ACM TOIS)

**Relevance**: First comprehensive survey on memory mechanisms for LLM-based agents. Provides theoretical grounding.

**Relevant to**: `sec:agents2-memory`

```bibtex
@article{memory-survey-acm,
  title        = {A Survey on the Memory Mechanism of Large Language Model-based Agents},
  journal      = {ACM Transactions on Information Systems},
  year         = {2024},
  url          = {https://dl.acm.org/doi/10.1145/3748302},
  urldate      = {2025-11-27},
  note         = {First comprehensive survey on memory mechanisms for LLM agents; covers working, semantic, episodic, procedural, spatial, and autobiographical memory}
}
```

---

### 10. Agent Evaluation Survey (2025)

**Relevance**: Comprehensive survey of agent evaluation methodologies. Addresses enterprise concerns.

**Relevant to**: `sec:agents2-eval`

```bibtex
@article{agent-eval-survey-2025,
  title        = {Survey on Evaluation of {LLM}-based Agents},
  year         = {2025},
  eprint       = {2503.16416},
  archiveprefix = {arXiv},
  primaryclass = {cs.AI},
  url          = {https://arxiv.org/abs/2503.16416},
  urldate      = {2025-11-27},
  note         = {First comprehensive survey of agent evaluation methodologies; analyzes benchmarks across fundamental capabilities, application-specific domains, generalist agents, and evaluation frameworks}
}
```

---

## Priority 2: Highly Recommended

### WebArena (Evaluation)

**Relevance**: Realistic environment testing long-horizon workflows. Relevant for legal research agents.

**Relevant to**: `sec:agents2-eval-workflow`

```bibtex
@article{zhou2023webarena,
  author       = {Zhou, Shuyan and Xu, Frank F. and Zhu, Hao and Zhou, Xuhui and Lo, Robert and Sridhar, Abishek and Cheng, Xianyi and Bisk, Yonatan and Fried, Daniel and Alon, Uri and Neubig, Graham},
  title        = {{WebArena}: A Realistic Web Environment for Building Autonomous Agents},
  year         = {2023},
  eprint       = {2307.13854},
  archiveprefix = {arXiv},
  primaryclass = {cs.CL},
  url          = {https://arxiv.org/abs/2307.13854},
  urldate      = {2025-11-27},
  note         = {812 tasks across 4 web apps testing long-horizon workflows; best GPT-4 agent: 14.41\% vs human 78.24\%; recent progress: IBM CUGA 61.7\%}
}
```

---

### SWE-bench (Evaluation)

**Relevance**: Critical benchmark for software engineering agents. Relevant for legal/finance AI involving code generation.

**Relevant to**: `sec:agents2-eval`

```bibtex
@online{swebench,
  author       = {{SWE-bench Team}},
  title        = {{SWE-bench}: Can Language Models Resolve Real-World {GitHub} Issues?},
  year         = {2024},
  url          = {https://www.swebench.com/},
  urldate      = {2025-11-27},
  note         = {2,294 real GitHub issues for evaluating software engineering agents; Docker-based evaluation harness; accepted at ICLR 2024}
}
```

---

### AutoGPT

**Relevance**: Pioneering autonomous agent with explicit memory management. Historical reference.

**Relevant to**: `sec:agents2-architecture`

```bibtex
@online{autogpt-platform,
  author       = {{Significant Gravitas}},
  title        = {{AutoGPT}: An Open-Source Framework for Autonomous {AI} Agents},
  year         = {2024},
  url          = {https://github.com/Significant-Gravitas/AutoGPT},
  urldate      = {2025-11-27},
  note         = {Multiagent framework with self-prompting mechanism, hierarchical memory (short-term FIFO and long-term vector storage), and low-code workflows}
}
```

---

### LlamaIndex Agents

**Relevance**: Production-ready framework with strong RAG integration.

**Relevant to**: `sec:agents2-architecture`

```bibtex
@online{llamaindex-agents,
  author       = {{LlamaIndex Documentation}},
  title        = {Agents},
  year         = {2024},
  url          = {https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/},
  urldate      = {2025-11-27},
  note         = {Production-ready agent framework with FunctionAgent, ReActAgent, CodeActAgent, and llama-agents for multi-agent systems}
}
```

---

### AI Agent Protocols Overview

**Relevance**: Comprehensive landscape of emerging protocols.

**Relevant to**: `sec:agents2-protocols`

```bibtex
@online{ai-agent-protocols,
  author       = {{IBM}},
  title        = {What Are {AI} Agent Protocols?},
  year         = {2024},
  url          = {https://www.ibm.com/think/topics/ai-agent-protocols},
  urldate      = {2025-11-27},
  note         = {Overview of emerging agent protocol landscape including MCP, A2A, ACP, OASF, ANP, AG-UI, and Agent Rules}
}
```

---

## Priority 3: Supporting Resources

### ACM KDD Agent Evaluation Survey

```bibtex
@inproceedings{agent-eval-kdd-2025,
  title        = {Evaluation and Benchmarking of {LLM} Agents: A Survey},
  booktitle    = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2},
  year         = {2025},
  url          = {https://dl.acm.org/doi/10.1145/3711896.3736570},
  urldate      = {2025-11-27},
  note         = {Two-dimensional taxonomy: evaluation objectives (behavior, capabilities, reliability, safety) and process (interaction modes, datasets, metrics, tooling); highlights enterprise challenges including compliance}
}
```

---

### LangChain/LangGraph 1.0

```bibtex
@online{langchain-1-0,
  author       = {{LangChain}},
  title        = {{LangChain} and {LangGraph} 1.0},
  year         = {2025},
  month        = oct,
  url          = {https://blog.langchain.com/langchain-langgraph-1dot0/},
  urldate      = {2025-11-27},
  note         = {First stable major releases; LangChain 1.0 introduces create\_agent abstraction, middleware system, standard content blocks; LangGraph 1.0 adds durable state persistence and human-in-loop patterns}
}
```

---

### Amazon Bedrock AgentCore

```bibtex
@online{bedrock-agentcore,
  author       = {{Amazon Web Services}},
  title        = {Amazon {Bedrock} {AgentCore} is now generally available},
  year         = {2025},
  month        = oct,
  url          = {https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-is-now-generally-available/},
  urldate      = {2025-11-27},
  note         = {Seven core services: Runtime (8-hour sessions), Gateway (MCP integration), Browser Tool, Code Interpreter, Observability, Identity (OAuth), Knowledge Base; framework-agnostic}
}
```

---

### EU AI Act Agents Report

```bibtex
@techreport{eu-ai-act-agents,
  author       = {{The Future Society}},
  title        = {{AI} Agents in the {EU}: A Focused Discussion on {AI} Agents Under the {AI} Act},
  year         = {2025},
  url          = {https://thefuturesociety.org/aiagentsintheeu/},
  urldate      = {2025-11-27},
  note         = {Identifies 10 measures for GPAI providers and agent deployers; addresses risk assessment, transparency tools, technical deployment controls, human oversight}
}
```

---

### AWS Agentic Security Matrix

```bibtex
@online{aws-agentic-security,
  author       = {{Amazon Web Services}},
  title        = {The Agentic {AI} Security Scoping Matrix: A Framework for Securing Autonomous {AI} Systems},
  year         = {2025},
  url          = {https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/},
  urldate      = {2025-11-27},
  note         = {Framework categorizing four agentic architectures based on connectivity and autonomy levels; key principle: graceful degradation when security events detected}
}
```

---

## Summary: Top 10 Priority Citations

| Rank | Resource | Section | Why Essential |
|------|----------|---------|---------------|
| 1 | MemGPT | Memory | Canonical hierarchical memory architecture |
| 2 | RAG (Lewis 2020) | Memory | Foundational retrieval technique |
| 3 | Tree of Thoughts | Planning | Advanced reasoning beyond CoT |
| 4 | A2A Protocol | Protocols | Agent-to-agent standard alongside MCP |
| 5 | AgentBench | Evaluation | Multi-environment systematic benchmark |
| 6 | GAIA | Evaluation | Tests fundamental capabilities |
| 7 | OpenAI Function Calling | Tools | De facto tool-use specification |
| 8 | Plan-and-Execute | Planning | Production decomposition pattern |
| 9 | Memory Survey (ACM) | Memory | Theoretical grounding |
| 10 | Agent Eval Survey | Evaluation | Comprehensive methodology survey |
