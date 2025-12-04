# Research Notes: Reference Architecture

## Section Overview

This section presents a comprehensive reference architecture for AI agents, organizing the architecture around three pillars: tools, memory, and planning. These pillars implement the GPA+IAT properties (Goal, Perception, Action, Iteration, Adaptation, Termination) established in Part I. The section also addresses deployment patterns for enterprise contexts, framework selection criteria, and security considerations specific to legal AI applications.

The research covers:
- Three architectural pillars (Tools, Memory, Planning)
- Core agent loop patterns (ReAct, Plan-Execute, Tree of Thoughts, Hierarchical, OODA)
- Memory systems (RAG, vector stores, knowledge graphs, episodic/semantic memory)
- Tool design principles and security
- Human-in-the-loop patterns and EU AI Act compliance
- Multi-agent orchestration and deployment topologies
- Framework landscape and selection criteria
- AWS Agentic Security Scoping Matrix

---

## Core Concepts

### The Core Agent Loop

At its simplest, an agent executes a perception-reasoning-action loop until a termination condition is met. This loop embodies the GPA+IAT properties by pursuing a goal, gathering information through perception, effecting change through action, repeating via iteration, updating memory for adaptation, and checking conditions for termination.

**Three Pillars**:
1. **Tools**: Enable perception (reading data) and action (writing data or triggering effects)
2. **Memory**: Enable the agent to retain and retrieve context across interactions (adaptation)
3. **Planning**: Enable goal decomposition, step execution, and termination detection

---

## Pillar 1: Tools

### Tool Design Principles

Recent best practices from production deployments emphasize several key design principles:

**Single Responsibility**: Each tool should do one thing well. This principle mirrors the Unix philosophy and enables more predictable tool selection by the agent. Composability comes from combining simple tools, not building complex ones.

**Clear Contracts**: Tools must have well-defined input schemas and output formats. JSON schema-defined functions with explicit parameter types enable reliable function calling. The Berkeley Function Calling Leaderboard (BFCL) demonstrates that function-calling accuracy improves when tool contracts are explicit and unambiguous.

**Graceful Failure**: Tools should return informative errors rather than crashing. An agent that receives "Error: Case not found for citation 123 F.3d 456" can adapt; an agent that receives a stack trace cannot.

**Least Privilege**: Tools should request only the permissions they need. This principle becomes critical when tools are exposed via MCP servers, where permission combinations can enable unintended data exfiltration.

**Sources**:
- [Writing effective tools for AI agents—using AI agents - Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [12-Factor Agents — Principles for Building Reliable LLM Applications - Medium](https://medium.com/@agentics/12-factor-agents-principles-for-building-reliable-llm-applications-7bdbfad6ce84)
- [Function calling in LLM agents - Symflower](https://symflower.com/en/company/blog/2025/function-calling-llm-agents/)
- [Best Practices for Function Calling in LLMs in 2025 - Scalifiai](https://www.scalifiai.com/blog/function-calling-tool-call-best%20practices)

### Berkeley Function Calling Leaderboard (BFCL)

The Berkeley Function Calling Leaderboard (BFCL) V4 evaluates LLM's ability to call functions (tools) accurately. BFCL consists of 2k question-function-answer pairs with multiple languages (Python, Java, JavaScript, REST API), diverse application domains, and complex use cases including multiple function calls and parallel function calls.

Key findings:
- State-of-the-art LLMs excel at single-turn calls
- Memory, dynamic decision-making, and long-horizon reasoning remain open challenges
- Irrelevance Detection (875 examples) tests scenarios where no function should be invoked
- Models struggle more with multi-turn, multi-step function calling evaluation

BFCL has become the de facto standard for evaluating function-calls since its preview.

**Sources**:
- [Berkeley Function Calling Leaderboard (BFCL) V4](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)
- [The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic - OpenReview](https://openreview.net/pdf?id=2GmDdhBdDk)

### Tool Security and MCP Vulnerabilities

The Model Context Protocol (MCP), introduced by Anthropic in November 2024, has become an emerging standard for connecting AI models to external tools and data. However, MCP introduces several security vulnerabilities:

**1. Prompt Injection Attacks**: Attackers insert hidden or malicious instructions within input prompts or data fields, tricking AI models into executing unintended commands. LLMs will trust anything that can send them convincing sounding tokens, making them extremely vulnerable to confused deputy attacks.

**2. Tool Poisoning**: Attackers embed malicious instructions within the descriptions of MCP tools. LLMs use tool metadata (name and description) to determine which tools to invoke. Compromised descriptions can manipulate the model into executing unintended tool calls. This is particularly dangerous in hosted MCP server scenarios where tool definitions can be dynamically amended ("rug pull").

**3. Indirect Injection via Context**: Attackers inject malicious payloads through external data or context sources like cached data, ticket histories, and third-party websites scraped by tools. When AI agents ingest these unscrubbed contexts, they unwittingly execute harmful instructions.

**4. Malicious Code Execution (MCE)**: Attackers induce the agent to run harmful code on the host system through prompt injection methods or by exploiting overly permissive tool use.

**5. Credential Exposure**: MCP servers often request broad permission scopes for flexible functionality. Centralized storage of multiple sensitive credentials can lead to exposure.

**Security Mitigations**:
- Input/output validation: Treat all tool descriptions as untrusted input
- Human-in-the-loop: MCP specification states there SHOULD always be a human with ability to deny tool invocations
- Sandboxing and privilege restriction: Execute MCP server commands in sandboxed environment with minimal privileges
- Version control: Pin tool versions and calculate cryptographic hash to prevent "rug pulls"
- Comprehensive logging: Audit all interactions to detect potential prompt injection attempts

**Sources**:
- [Model Context Protocol (MCP): A Security Overview - Palo Alto Networks](https://www.paloaltonetworks.com/blog/cloud-security/model-context-protocol-mcp-a-security-overview/)
- [Model Context Protocol has prompt injection security problems - Simon Willison](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [MCP Security Vulnerabilities - Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-vulnerabilities/)
- [Security Best Practices - Model Context Protocol](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [How to secure model-agent interactions against MCP vulnerabilities - Stytch](https://stytch.com/blog/mcp-vulnerabilities/)

---

## Pillar 2: Memory

### Memory Types

Agent memory systems typically include multiple types:

**Short-Term Memory**: The current conversation or session context, implemented as the LLM's context window. Limited by token capacity.

**Long-Term Memory**: Persistent storage of information across sessions. Implemented via vector databases, knowledge graphs, or structured stores.

**Episodic Memory**: Records of past interactions and their outcomes. Enables learning from experience ("Last time I tried this approach, it failed"). Episodic memory stores specific past events and experiences, like a personal diary of the AI's interactions.

**Semantic Memory**: General knowledge and facts relevant to the agent's domain. Often implemented as RAG over curated corpora. Semantic memory contains generalized information such as facts, definitions and rules.

**Sources**:
- [Build smarter AI agents: Manage short-term and long-term memory with Redis](https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/)
- [What Is AI Agent Memory? - IBM](https://www.ibm.com/think/topics/ai-agent-memory)
- [AI Agent Memory: Short/Long Term, RAG, Agentic RAG - Decoding AI](https://www.decodingai.com/p/memory-the-secret-sauce-of-ai-agents)

### RAG (Retrieval-Augmented Generation)

Lewis et al. (2020) coined the term "Retrieval-Augmented Generation (RAG)" and proposed a general framework that leverages the strength of pre-trained parametric memory (the LLM) with non-parametric memory (a separate database) as a new way to improve performance for knowledge-intensive tasks.

**Recent RAG Advances**:

**Self-Reflective RAG (Self-RAG)**: Dynamically decides when and how to retrieve information, evaluating relevance and critiquing outputs before presenting them. Introduces "reflection tokens" as explicit signals indicating that the model requires external knowledge. This strategy outperforms static RAG, especially on tasks that require precise factual grounding.

**GraphRAG**: Microsoft's approach constructs entity-centric graphs from retrieved passages using community summarization, improving multi-hop question-answering recall by over 6 points compared to baseline retrieval. GraphRAG detects "communities" of densely connected nodes in a hierarchical fashion, partitioning the graph at multiple levels from high-level themes to low-level topics. Results show ~70-80% win rate on comprehensiveness and diversity compared to naive RAG.

**Hybrid Retrieval**: Combines dense embeddings (semantic meaning) with sparse methods like BM25 (exact matches), achieving up to 13% improvement in retrieval correctness.

**RAFT (Retrieval-Augmented Fine-Tuning)**: Combines RAG and fine-tuning advantages, creating synthetic datasets for domain-specific improvement—particularly effective in medicine and law. Given a question and a set of retrieved documents, the model is trained to ignore "distractor documents" that don't help answer the question. RAFT particularly excels in domain-specific sectors such as biomedicine, law, and APIs.

**Sources**:
- [Retrieval-Augmented Generation (RAG) in 2025: Innovations - Caiyman AI](https://www.caiyman.ai/blog/retrieval-augmented-generation-rag-2025-innovations-architecture-adoption-frameworks)
- [What Is Retrieval-Augmented Generation aka RAG - NVIDIA](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
- [Agentic Retrieval-Augmented Generation: A Survey - arXiv](https://arxiv.org/abs/2501.09136)
- [From Local to Global: A Graph RAG Approach - arXiv](https://arxiv.org/html/2404.16130v1)
- [GraphRAG: New tool for complex data discovery - Microsoft Research](https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery-now-on-github/)
- [RAFT: Adapting Language Model to Domain Specific RAG - arXiv](https://arxiv.org/abs/2403.10131)

### Dynamic Retrieval Triggering

A growing class of systems dynamically controls when and how to retrieve, conditioned on generation uncertainty, task complexity, or intermediate outputs.

**DRAGIN (Dynamic Retrieval Augmented Generation based on Information Needs)**: Published at ACL 2024, DRAGIN improves upon FLARE by proposing a lightweight RAG framework that dynamically determines when and what to retrieve. It consists of two components: Real-time Information Needs Detection (RIND) and Query Formulation based on Self-attention (QFS). DRAGIN determines when to retrieve based on token generation probabilities and performs query reformulation using attention weights.

**FLARE (Forward-Looking Active REtrieval)**: Introduces an uncertainty-aware retrieval mechanism that monitors token-level generation probabilities during decoding. When low-confidence tokens are detected, the system automatically formulates retrieval queries. FLARE triggers retrieval when encountering an uncertain token—specifically, if any token has a probability lower than a certain threshold.

Performance: DRAGIN frameworks achieve moderate improvements, typically 22-44% over raw LLMs and 14-34% over retrieval baselines. FLAREdirect achieves 62% improvement on 2Wiki, suggesting that model-guided active retrieval significantly strengthens multi-hop evidence gathering.

**Sources**:
- [DRAGIN: Dynamic Retrieval Augmented Generation - ACL Anthology](https://aclanthology.org/2024.acl-long.702/)
- [DRAGIN: Dynamic Retrieval Augmented Generation - arXiv](https://arxiv.org/html/2403.10081v1)
- [Dynamic and Parametric Retrieval-Augmented Generation - arXiv](https://arxiv.org/html/2506.06704v1)
- [Retrieval-Augmented Generation: Comprehensive Survey - arXiv](https://arxiv.org/html/2506.00054v1)

### Vector Databases and Knowledge Graphs

**Vector Stores**: Embeddings of documents, conversations, or facts stored in vector databases enable efficient similarity search across large collections. Several architectural approaches exist:
- Managed cloud services: Fully managed, serverless architectures
- Open-source standalone systems: Self-hosted solutions with hybrid search
- Embedded databases: Lightweight architectures for prototyping
- Relational database extensions: Vector search capabilities added to existing SQL infrastructure

**Knowledge Graphs**: Structured representations of entities and relationships. Better for traversing connections than similarity-based retrieval. For legal AI, knowledge graphs enable:
- Combining multidimensional heterogeneous knowledge (legal provisions, judicial interpretations, cases, defenses) into structured triples
- Similar case recommendation based on constructed relationships
- Legislative systems support, compensating for LLM limitations with up-to-date external knowledge
- RAG enhancement through vector stores combined with hierarchical legal ontologies

Recent studies demonstrate effectiveness of knowledge graphs in recommending similar legal cases, linking case law with statutes for improved retrieval, and enhancing legal case law search. Ontologies serve as essential frameworks in AI, acting as blueprints for legal knowledge, defining terms, relationships, and rules.

**Hybrid Approaches**: Vector databases (sufficient for conversational memory - Q&A pairs) are insufficient for agentic tasks given their need to manage additional memory types: semantic memory, episodic memory, procedural memory, and emotional memory. This highlights need for alternative formalisms (e.g., knowledge graphs, finite state machines).

**MemoriesDB**: Functions as a coherence engine implementing a temporal-semantic-relational database for long-term agent memory. By embedding semantic relationships directly into temporal order, it prevents context fragmentation that typically accompanies long-horizon reasoning.

**Sources**:
- [Comparing Memory Systems for LLM Agents - MarkTechPost](https://www.marktechpost.com/2025/11/10/comparing-memory-systems-for-llm-agents-vector-graph-and-event-logs/)
- [MemoriesDB: A Temporal-Semantic-Relational Database - arXiv](https://arxiv.org/html/2511.06179v1)
- [How VectorDBs Power Intelligent AI Agents - Zilliz](https://zilliz.com/blog/critical-role-of-vectordbs-in-building-intelligent-ai-agents)
- [Bridging Legal Knowledge and AI - arXiv](https://arxiv.org/html/2502.20364v1)
- [Similar Cases Recommendation using Legal Knowledge Graphs - arXiv](https://arxiv.org/html/2107.04771v2)

### Agentic RAG

Agentic Retrieval-Augmented Generation (Agentic RAG) transcends limitations of traditional RAG by embedding autonomous AI agents into the RAG pipeline. These agents leverage agentic design patterns—reflection, planning, tool use, and multiagent collaboration—to dynamically manage retrieval strategies, iteratively refine contextual understanding, and adapt.

Agentic RAG combines RAG with autonomous agents that can plan and execute tasks using retrieved knowledge. It allows for complex, multi-turn, tool-augmented tasks, blends query processing, action-taking, and reasoning, enables integration with APIs, workflows, and databases, and merges structured and unstructured data sources.

**Internal Memory**: Captures the agent's own experiences, such as successful planning examples, execution traces, dialogues, and inferred knowledge. Dynamic, incremental knowledge updates are essential—agentic systems demand a memory architecture capable of evolving alongside newly acquired data.

**Sources**:
- [Agentic Retrieval-Augmented Generation: A Survey - arXiv](https://arxiv.org/abs/2501.09136)
- [Towards the Next Generation of Agent Systems: From RAG to Agentic AI - VLDB](https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/LLM+Graph/LLMGraph-8.pdf)

### Legal Memory Requirements (ABA Formal Opinion 512)

The ABA issued Formal Opinion 512 (July 2024) addressing AI use in legal practice, raising particular concerns about memory systems.

**Key Requirements**:

**Matter Isolation**: Memory from one client matter must never leak to another. Cross-matter contamination could waive attorney-client privilege. Multi-client memory systems must implement ethical walls (also called "Chinese walls") to prevent information flow between matters with conflicts of interest.

**Privilege Preservation**: Privileged communications must be protected even within memory systems. Self-learning AI raises the possibility that client information may be stored and revealed in response to future inquiries by third parties. Attorney-client privilege can be waived if information is disclosed to an outside party. AI-processed communications might not be protected from discovery if the memory system stores or transmits data to third-party vendors.

**Temporal Validity**: Legal rules change; memory must track when information was valid. A case cited as good law in 2020 may be overruled by 2025.

**Authority Hierarchy**: Some sources (statutes, regulations) should be weighted over others (secondary sources). Standard RAG achieves high textual similarity but lacks doctrinal authority.

**Jurisdiction Awareness**: Memory retrieval should respect jurisdictional boundaries. A California precedent may be irrelevant—or worse, misleading—for a Texas matter.

**Technical Controls for Ethical Walls**:
- Separate vector store namespaces or collections per client/matter
- Access control lists verified before any retrieval operation
- Audit trails for all memory access with tamper-resistant logging
- Secure deletion capabilities when matters close or conflicts arise

**Sources**:
- [ABA issues first ethics guidance on AI tools](https://www.americanbar.org/news/abanews/aba-news-archives/2024/07/aba-issues-first-ethics-guidance-ai-tools/)
- [ABA Formal Opinion 512 - Full PDF](https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf)
- [AI and Attorney-Client Privilege: A Brave New World - ABA](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-september/ai-attorney-client-privilege/)

---

## Pillar 3: Planning

### Planning Patterns

Several planning patterns have emerged in agentic systems:

#### ReAct (Reasoning + Acting)

Introduced by Yao et al., 2022, ReAct synergizes reasoning and acting in language models by generating both reasoning traces and task-specific actions in an interleaved manner. Each cycle produces a thought, an action, and an observation from the environment.

**How it works**: In this approach, LLMs generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two. Reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources to gather additional information.

**Key advantage**: While actions lead to observation feedback from an external environment, reasoning traces affect the internal state of the model by reasoning over the context and updating it with useful information to support future reasoning and acting. The reasoning traces make the agent's decision process transparent and auditable—critical for legal applications where explainability matters.

**Benchmark results**: On question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation by interacting with a simple Wikipedia API. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples.

**Limitation**: Single-step reasoning can be inefficient for complex, multi-step tasks where upfront planning would be more efficient.

**Sources**:
- [ReAct: Synergizing Reasoning and Acting in Language Models - arXiv](https://arxiv.org/abs/2210.03629)
- [ReAct: Synergizing Reasoning and Acting - Official Website](https://react-lm.github.io/)
- [ReAct: Synergizing Reasoning and Acting - Google Research](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/)
- [ReAct Prompting - Prompt Engineering Guide](https://www.promptingguide.ai/techniques/react)

#### MRKL (Modular Reasoning, Knowledge and Language)

MRKL Systems (pronounced "miracle") are a neuro-symbolic architecture that combines Large Language Models (neural computation) with external tools like calculators (symbolic computation) to solve complex problems. Introduced in May 2022 by Ehud Karpas et al.

**Architecture Components**:
- **Router**: Routes every user query to a module that can best respond to user's question
- **Expert Modules**: An extendable set of expert modules, along with a large language model (LLM), that are specialized for specific tasks
- **Module Types**: Can be neural (including general-purpose huge language model and specialized smaller LMs) or symbolic

**Key Benefits**:
- Easy extensibility by adding modules without retraining the whole system
- Explainability, since it's clear which module produced an answer
- Up-to-date real-time data from external APIs and databases
- Secure access to proprietary data sources
- By composing modules in multi-input/output chains, the model can correctly respond to complex questions

AI21 Labs implemented a MRKL system called Jurassic-X, which was trained to handle basic arithmetic reliably.

**Sources**:
- [MRKL Systems - IBM](https://www.ibm.com/architectures/hybrid/genai-mrkl)
- [MRKL Systems - arXiv](https://arxiv.org/abs/2205.00445)
- [MRKL Systems - AI21](https://www.ai21.com/research/mrkl-systems-a-modular-neuro-symbolic-architecture-that-combines-large-language-models-external-knowledge-sources-and-discrete-reasoning/)

#### Reflexion: Language Agents with Verbal Reinforcement Learning

Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Published in March 2023 by Noah Shinn et al.

**Key Framework Components**:
1. **Actor**: Generates text and actions based on state observations
2. **Evaluator**: Scores outputs produced by the Actor, taking a generated trajectory as input and outputting a reward score
3. **Self-Reflection**: An LLM that generates verbal reinforcement cues to assist the Actor in self-improvement

**How it Works**: Self-reflective feedback acts as a 'semantic gradient signal' by providing the agent with a concrete direction to improve upon, helping it learn from prior mistakes. Self-reflection is created by showing two-shot examples to LLM and each example is a pair of (failed trajectory, ideal reflection for guiding future changes in the plan). Reflections are added into the agent's working memory, up to three, to be used as context for querying LLM.

**Performance Results**:
- Achieves 91% pass@1 accuracy on HumanEval coding benchmark, surpassing GPT-4 (80%)
- Evaluated on sequential decision-making (AlfWorld), reasoning (HotPotQA), and programming (HumanEval and MBPP)

**Advantages**: Reflexion offers a lightweight alternative to traditional RL that doesn't require fine-tuning the underlying language model, making it more efficient in terms of data and compute resources.

**Sources**:
- [Reflexion: Language Agents with Verbal Reinforcement Learning - arXiv](https://arxiv.org/abs/2303.11366)
- [Reflexion - Prompt Engineering Guide](https://www.promptingguide.ai/techniques/reflexion)
- [LLM Powered Autonomous Agents - Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [Self-Reflection in LLM Agents - arXiv](https://arxiv.org/pdf/2405.06682)

#### Tree of Thoughts (ToT)

Introduced by Yao et al., 2023 (Princeton), Tree of Thoughts generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving.

**Key Features**: ToT maintains a tree of thoughts, where thoughts represent coherent language sequences that serve as intermediate steps toward solving a problem. This approach enables an LM to self-evaluate the progress through intermediate thoughts made towards solving a problem through a deliberate reasoning process. The LM's ability to generate and evaluate thoughts is combined with search algorithms (e.g., breadth-first search and depth-first search) to enable systematic exploration of thoughts with lookahead and backtracking.

**Experimental Results**: For Game of 24, while GPT-4 with chain-of-thought prompting only solved 4% of tasks, ToT achieved a success rate of 74%. ToT significantly enhances language models' problem-solving abilities on three novel tasks requiring non-trivial planning or search: Game of 24, Creative Writing, and Mini Crosswords.

**Tradeoffs**: ToT increases resource consumption and can lead to redundant exploration of low-value paths, making it less efficient for simpler tasks.

**Publication**: Published as part of Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track.

**Sources**:
- [Tree of Thoughts: Deliberate Problem Solving - arXiv](https://arxiv.org/abs/2305.10601)
- [Tree of Thoughts - GitHub](https://github.com/princeton-nlp/tree-of-thought-llm)
- [Tree of Thoughts - Prompt Engineering Guide](https://www.promptingguide.ai/techniques/tot)
- [Tree of Thoughts - NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf)

#### Plan-and-Execute

The agent creates a complete plan before execution, then follows it step by step. Inspired by the Plan-and-Solve paper and early autonomous agent research, this pattern separates an LLM-powered "planner" from the tool execution runtime.

**Key Advantages**:
- Explicit long-term planning (which even strong LLMs struggle with in ReAct mode)
- Ability to use smaller/weaker models for execution, reserving larger models for planning
- Plan revision capability after accomplishing intermediate tasks

**Task Decomposition Strategies**: Popular techniques include Chain of Thought (CoT) and Tree of Thoughts, which can be categorized as single-path reasoning and multi-path reasoning, respectively.

**Hierarchical Planning**: LLM planning frameworks are often built on hierarchical architectures that split planning into high-level and low-level stages. High-level planners use LLMs to parse task instructions and generate sequences of subgoals or abstract actions, while low-level controllers map these subgoals to primitive actions executable by an agent.

**ADaPT (As-needed Decomposition and Planning)**: Uses recursive decomposition to decompose tasks when the executor fails. Determines the decomposition strategy based on the execution capabilities of the LLM, allowing recursive adjustment of subtasks if difficulties arise during execution.

**Sources**:
- [LLM Powered Autonomous Agents - Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [LLM Agents - Prompt Engineering Guide](https://www.promptingguide.ai/research/llm-agents)
- [A Roadmap to Guide the Integration of LLMs in Hierarchical Planning - arXiv](https://arxiv.org/html/2501.08068)
- [Understanding the planning of LLM agents - arXiv](https://arxiv.org/pdf/2402.02716)

#### LLMCompiler and ReWOO

**LLMCompiler**: Introduced to execute functions in parallel to efficiently orchestrate multiple function calls. Drawing inspiration from principles of classical compilers, LLMCompiler enables parallel function calling with three components: (i) Function Calling Planner, (ii) Task Fetching Unit, and (iii) Executor.

**Architecture**:
- **Planner**: Streams a DAG of tasks, where each task contains a tool, arguments, and list of dependencies
- **Task Fetching Unit**: Schedules and executes tasks, accepting a stream of tasks and scheduling them once dependencies are met
- **Joiner**: Dynamically replans or finishes based on entire graph history

**Performance**: Demonstrates consistent latency speedup of up to 3.7x, cost savings of up to 6.7x, and accuracy improvement of up to ~9% compared to ReAct. Published at ICML 2024.

**ReWOO (Reasoning WithOut Observation)**: A modular paradigm that detaches the reasoning process from external observations, significantly reducing token consumption and demonstrating robustness under tool-failure scenarios. ReWOO permits variable assignment in the planner's output, removing the need to always use an LLM for each task while still allowing tasks to depend on previous task results.

**Sources**:
- [LLMCompiler: An LLM Compiler for Parallel Function Calling - arXiv](https://arxiv.org/abs/2312.04511)
- [LLMCompiler - GitHub](https://github.com/SqueezeAILab/LLMCompiler)
- [Plan-and-Execute Agents - LangChain Blog](https://blog.langchain.com/planning-agents/)

#### OODA Loop (Observe-Orient-Decide-Act)

The Observe-Orient-Decide-Act framework, developed by military strategist John Boyd in the 1970s, provides a classical model for iterative decision-making under uncertainty. While predating LLM agents, OODA maps cleanly to agentic systems:

- **Observe**: Gather information from the environment (Perception via tools)
- **Orient**: Analyze observations in context (Memory retrieval and reasoning). Boyd believed that Orientation was central to the information-processing system.
- **Decide**: Select a course of action (Planning and action selection)
- **Act**: Execute the decision (Action via tools)

**Key Insight**: Faster iteration through this loop—enabled by better perception and streamlined decision-making—provides competitive advantage. For legal AI agents, OODA emphasizes the importance of continuous observation (monitoring case developments, regulatory changes) and rapid re-orientation when circumstances shift.

**Differences from ReAct**: Unlike ReAct's explicit thought traces, OODA treats orientation as an implicit synthesis step, making it useful for high-tempo environments where explicit reasoning may slow response. Boyd didn't imagine that people transition through each stage consecutively—rather, he described an iterative process with multiple feedback loops where information might travel through various paths.

**Applications**: Originally designed for combat operations, OODA's utility extends to business management, sports, and emergency response. An entity that can process this cycle quickly, observing and reacting to unfolding events more rapidly than an opponent, can gain advantage.

**Sources**:
- [OODA loop - Wikipedia](https://en.wikipedia.org/wiki/OODA_loop)
- [What is the OODA loop? - TechTarget](https://www.techtarget.com/searchcio/definition/OODA-loop)
- [The OODA Loop Explained - OODAloop](https://oodaloop.com/the-ooda-loop-explained-the-real-story-about-the-ultimate-model-for-decision-making-in-competitive-environments/)
- [OODA Loop by John Boyd - Toolshero](https://www.toolshero.com/decision-making/ooda-loop/)

### Termination Mechanisms and Guardrails

Proper termination is critical for agent safety. Agents must know when to stop:

**Termination Conditions**:
- Success Conditions: Goal achieved, task completed, answer found
- Resource Budgets: Token limits, time limits, iteration limits, cost limits
- Confidence Thresholds: Uncertainty too high, conflicting information, requires human judgment
- Error Conditions: Tool failures, unexpected states, constraint violations
- Escalation Triggers: High-stakes decisions, novel situations, explicit user request

**Loop Detection Strategies**:

**Step Limits**: Define maximum iterations (e.g., 50 tool calls per task). Increment a counter each time the agent calls a tool or the LLM. If the counter exceeds threshold, terminate or escalate.

**Token Thresholds**: Track total tokens consumed and stop if it exceeds preset limit. Common example uses token budget of 10,000 tokens and terminates execution when exceeded.

**Reflection Steps**: Periodic self-evaluation ("Am I making progress?")

**External Watchdogs**: Independent monitoring processes that can terminate runaway agents

**Meta-policies**: Rules to cut off obvious loops (e.g., same tool called 5+ times with identical parameters)

**Budget-Based Guardrails**: Pattern of per-agent budget + thresholds at 75%/90% is effective operationally and minimizes surprise bills. In one real example, a misbehaving automated test once spiked LLM spend in a pilot; budget guardrails capped the loss to $30 by denying calls after budget exhaustion and alerting FinOps.

**Frameworks Implementing Guardrails**: Modern agent frameworks implement guardrails as middleware to intercept execution at strategic points. Many modern frameworks provide built-in guardrail primitives for loop detection, token limiting, and step counting.

**Tools**:
- **AgentGuard**: Real-time guardrail that shows token spend and kills runaway LLM/agent loops
- **OpenAI Agents SDK**: Offers blocking execution where guardrail runs before agent starts
- **LangChain Guardrails**: Validate and filter content at key points in agent's execution

**Sources**:
- [Execution Guardrails for AI Agentic Implementation - Itzikr's Blog](https://itzikr.wordpress.com/2025/01/08/execution-guardrails-for-ai-agentic-implementation/)
- [AgentGuard - GitHub](https://github.com/dipampaul17/AgentGuard)
- [Guardrails - OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/)
- [Adding Guardrails for AI Agents - Reco.ai](https://www.reco.ai/hub/guardrails-for-ai-agents)
- [Aegis: Agent Rate Limits & Budget Guardrails](https://www.cloudmatos.ai/blog/aegis-agent-rate-limits-budget-guardrails/)

---

## Human-in-the-Loop Patterns

### EU AI Act Article 14 Requirements

Under Article 14(1) of the EU AI Act, systems must be designed and developed so they can be "effectively overseen by natural persons during the period in which the AI system is in use." Article 14 requires that high-risk AI systems be designed to allow effective human oversight, with the goal of preventing or minimizing risks to health, safety, or fundamental rights.

**Types of Human Oversight Models**:

**Human-in-Command (HIC)**: Ultimate authority where humans maintain absolute control and veto power over AI operations, essential for critical infrastructure and national security applications.

**Human-in-the-Loop (HITL)**: Direct operational involvement where humans are actively engaged in AI decision-making processes, with real-time intervention capabilities and pre-decision approval requirements.

**Human-on-the-Loop (HOTL)**: Supervisory oversight where humans monitor AI systems and intervene when necessary, focusing on exception-based intervention and system-level performance monitoring.

**Article 14(4) Requirements**: Can be grouped into three categories:
- **Authority**: Ability to override, stop, or reject outputs
- **Comprehension**: Understanding system limits, interpreting output
- **Environment**: Awareness of automation bias and ensuring the overseer has time, training, and support

**Compliance**: Full compliance with the EU AI Act is required by August 2026. Non-compliance can incur fines up to €35 million or 7% of global revenue.

**Challenges**: Research shows that human oversight often falls short. Humans can easily become rubber stampers, unable—or unwilling—to critically evaluate automated decision-making. Cognitive limits, automation bias, and time pressure mean humans often don't catch mistakes—and may even make good outputs worse.

**Sources**:
- [Key Issue 4: Human Oversight - EU AI Act](https://www.euaiact.com/key-issue/4)
- [EU AI Act Human Oversight Requirements - eyreACT](https://www.eyreact.com/eu-ai-act-human-oversight-requirements-comprehensive-implementation-guide/)
- [Human Oversight under Article 14 - SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5147196)
- [Article 14: Human Oversight - EU Artificial Intelligence Act](https://artificialintelligenceact.eu/article/14/)

### Human-in-the-Loop Implementation Patterns

**Approval Gates**: Certain actions require explicit human approval before execution. The agent pauses, presents its proposed action, and waits for confirmation. Essential for irreversible actions in legal contexts.

**Checkpoint Reviews**: At defined points in workflow, the agent presents its progress for human review. Human can approve, modify, or redirect, enabling course correction before significant work is wasted.

**Confidence-Based Escalation**: When agent's confidence falls below threshold, it escalates to human rather than proceeding with uncertainty. Organizations report 37-point higher trust scores for agent outputs when humans verify critical decisions.

**Reversibility Classification**: Actions classified as reversible or irreversible. Irreversible actions (filing, sending, publishing) require human approval; reversible actions (drafting, searching, analyzing) may proceed autonomously.

**Interrupt/Pause Pattern**: Agent is paused mid-execution for human input, then resumes based on response. Modern graph-based frameworks support this through persistent state that survives interruption.

**Human-as-Tool Pattern**: Agent treats "human" as a callable tool, routing uncertain questions to human reviewer and using the response in subsequent context. Enables selective human involvement without blocking entire workflows.

**Role-Based Approval**: Only specific human roles can approve certain actions. Agents initiate requests but require approval from authorized personnel—mapping to legal practice where partners approve work product that associates draft.

**Sources**:
- [What is HITL (Human-in-the-Loop) for an AI Assistant? - Aire](https://aireapps.com/articles/what-is-hitl-human-in-the-loop-for-an-ai-assistant/)
- Framework-specific documentation on HITL patterns

---

## Deployment Patterns

### Single-Agent vs Multi-Agent Patterns

**Market Growth**: The AI agents market is growing from $5.25 billion in 2024 to $52.62 billion by 2030—a 46.3% CAGR, with multi-agent systems representing the fastest-growing segment. Organizations should start with single agents when building proof-of-concepts, then move to multi-agent when tasks require concurrency, isolation, or regulation.

**Single-Agent Deployment**:
- **Advantages**: Simpler security model, easier to audit and monitor, lower coordination overhead
- **Disadvantages**: Limited scalability, single point of failure, may require broad permissions
- **Best For**: Well-defined tasks with clear boundaries, initial deployments, high-security environments

**Multi-Agent Orchestration**:
- **Pattern**: Orchestrator receives tasks, delegates to specialists, aggregates results. Specialists are domain-focused agents (research, drafting, review, filing). Uses protocols like A2A for agent-to-agent communication.
- **Advantages**: Specialized agents can be optimized for their domain, narrower permission sets per agent, better scalability
- **Disadvantages**: Coordination complexity, multiple attack surfaces, harder to debug
- **Best For**: Complex workflows, high-volume processing, mature deployments

**Performance Benefits**: Organizations using multi-agent architectures achieve 45% faster problem resolution and 60% more accurate outcomes compared to single-agent systems.

**Architecture Patterns**: Current architecture patterns have consolidated around five dominant approaches:
- Centralized orchestration for strict governance requirements
- Decentralized multi-agent for autonomous coordination
- Hierarchical agent architecture for complex workflows
- Event-driven orchestration for real-time responses
- Hybrid human-AI orchestration

**Hub-and-Spoke**: A "command center approach" where central orchestrator manages all agent interactions, creating predictable workflows with strong consistency. For compliance-heavy workflows in finance or healthcare, this trade-off often makes sense.

**Mesh Architectures**: Let agents communicate directly, creating resilient systems that can handle failure gracefully. When one agent goes down, others route around it. Patterns vary—full mesh where every agent connects to every other agent, partial mesh with selective connectivity, or swarming patterns that enable emergent coordination.

**Sources**:
- [Building Secure Multi-Agent AI Architectures for Enterprise SecOps - AppSecEngineer](https://www.appsecengineer.com/blog/building-secure-multi-agent-ai-architectures-for-enterprise-secops)
- [AI Agent Architecture Patterns in 2025 - NexAI Tech](https://nexaitech.com/multi-ai-agent-architecutre-patterns-for-scale/)
- [Multi-Agent AI Orchestration: Enterprise Strategy for 2025-2026 - OnAbout.ai](https://www.onabout.ai/p/mastering-multi-agent-orchestration-architectures-patterns-roi-benchmarks-for-2025-2026)
- [Everything you need to know about multi AI agents in 2025 - Springs](https://springsapps.com/knowledge/everything-you-need-to-know-about-multi-ai-agents-in-2024-explanation-examples-and-challenges)

### Agent-to-Agent (A2A) Protocol

The Agent2Agent (A2A) protocol is a communication protocol for AI agents, initially introduced by Google in April 2025. This open protocol is designed for multi-agent systems, allowing interoperability between AI agents from varied providers or those built using different AI agent frameworks.

**Key Features**:
- Uses lightweight JSON-based RPC schema on top of standard web protocols like HTTP
- Agents provide HTTP(S) endpoint based on A2A specification for message exchange
- Relies on JSON-RPC 2.0 for request/response and Server Sent Events (SSE) for streaming updates
- Agents advertise capabilities using structured metadata format called "agent cards"
- Includes provisions for trust, routing, and structured memory exchange

**Core Components**:
- **A2A client (client agent)**: Agent/service/application that initiates tasks by reaching out to other agents. Acts as orchestrator or project manager in multi-agent workflow
- **A2A server (remote agent)**: AI agent that provides HTTP endpoint compliant with A2A protocol. Accepts incoming requests, processes assigned tasks, sends back results

**Industry Support**: A2A was introduced by Google with support from over 50 technology partners. Now housed by the Linux Foundation as open-source Agent2Agent (A2A) project.

**Complementary Protocols**: The current phase (2024-2025) emphasizes lightweight, standardized protocols such as MCP, ACP, ANP, and A2A. These protocols address previous limitations by enabling dynamic discovery, secure communication, and decentralized collaboration. MCP addresses immediate need to contextualize LLMs; ACP looks at semantic richness and intent modeling; A2A targets broad interoperability.

**Sources**:
- [Announcing the Agent2Agent Protocol (A2A) - Google Developers Blog](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- [Empowering multi-agent apps with A2A protocol - Microsoft Cloud Blog](https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/05/07/empowering-multi-agent-apps-with-the-open-agent2agent-a2a-protocol/)
- [What Is Agent2Agent (A2A) Protocol? - IBM](https://www.ibm.com/think/topics/agent2agent-protocol)
- [Survey of Agent Interoperability Protocols - arXiv](https://arxiv.org/html/2505.02279v1)
- [MCP, ACP, and A2A - Camunda Blog](https://camunda.com/blog/2025/05/mcp-acp-a2a-growing-world-inter-agent-communication/)

---

## AWS Agentic AI Security Scoping Matrix

Published approximately November 21, 2025, AWS developed the Agentic AI Security Scoping Matrix, a mental model and framework that categorizes four distinct agentic architectures based on connectivity and autonomy levels, mapping critical security controls across each.

### Background and Rationale

Unlike traditional FMs that operate in stateless request-response patterns, agentic AI systems introduce autonomous capabilities, persistent memory, tool orchestration, identity and agency challenges, and external system integration, expanding the risks that organizations must address. Traditional AI security frameworks don't always extend into the agentic space. The autonomous nature of agentic systems requires fundamentally different security approaches.

### Key Concepts

**Agency**: Fundamentally about capabilities and permissions—what the system is allowed to do within its operational environment.

**Autonomy**: Refers to the degree of independent decision-making and action the system can take without human intervention. This includes when it operates, how it chooses between available actions, and whether it requires human approval for execution. Autonomy is about independence in decision-making and execution—how freely the system can act within its granted agency.

### The Four Scopes

The matrix helps organizations classify their agentic AI implementations across four architectural scopes—from workflow systems to fully autonomous agents—and implement appropriate security controls across six critical dimensions including identity management, memory protection, and behavioral monitoring.

**Scope 1 (Interactive)**: Low autonomy, limited connectivity. Human-initiated systems with no autonomous change capabilities, where agents follow predefined execution paths and operate in read-only mode. These systems provide information and recommendations but cannot make changes to external systems or data without explicit human action. Security focus: identity context, workflow integrity, input validation.

**Scope 2 (Distributed)**: Low autonomy, extended connectivity. Human-initiated systems that can recommend actions, including ability to make changes to environment, but require mandatory human approval before execution through "Human in the Loop" (HITL) workflows. Agents can analyze situations, propose solutions, and prepare actions, but all changes must be explicitly approved by authorized personnel. Security focus: robust approval workflows, secure communication channels.

**Scope 3 (Isolated)**: High autonomy, limited connectivity. Human-initiated systems with autonomous execution capabilities that can make contextual decisions and take actions that can modify the environment without requiring further HITL approvals once activated. Agents operate within predefined, bounded parameters and can complete complex, multi-step tasks independently while maintaining alignment with original human objectives. Security focus: continuous monitoring, behavioral validation, kill switches. Post-activation oversight required.

**Scope 4 (Networked)**: High autonomy, extended connectivity. Highest risk. Full autonomy with self-adjusting boundaries. May implement self-adjusting boundaries and intelligent constraint enforcement to give desired flexibility to act in safe but creative ways to solve contextual problems; however, Scope 4 agents should never be allowed to operate outside bounds of designed purpose. Requires dynamic context-aware limitations and comprehensive security controls.

### Security Considerations

**Memory Persistence**: Introduces data protection requirements and memory poisoning attack vectors. At higher scopes, security boundaries shift from static constraints to dynamic, context-aware limitations.

**Key Concerns**: Privilege escalation prevention, identity context enforcement, human-provided context validation.

**Graceful Degradation**: A key principle—agents should reduce autonomy or halt operation when security events are detected. A Scope 4 agent that detects anomalous behavior should degrade to Scope 2 (requiring human approval) rather than continuing autonomous operation.

### Legal AI Agent Positioning

Legal AI agents typically start in Scope 1 (Interactive) and may progress to Scope 2 (Distributed) as trust is established. Scope 4 (Networked) deployments require mature security controls, comprehensive audit capabilities, and organizational readiness for autonomous legal decision-making—a threshold most organizations have not yet reached.

**Progressive Autonomy Deployment**: Start with Scope 1 or 2 implementations and gradually advance through scopes as organizational confidence and security capabilities mature. This approach minimizes risk while building operational experience.

**Sources**:
- [The Agentic AI Security Scoping Matrix - AWS Security Blog](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/)
- [Securing Agentic AI: The Agentic AI Security Scoping Matrix - AWS](https://aws.amazon.com/ai/security/agentic-ai-scoping-matrix/)
- [The Agentic AI Security Scoping Matrix - AWS News](https://aws-news.com/article/2025-11-21-the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems)

---

## Framework Landscape

### Framework Categories

Agent frameworks generally fall into several categories:
- **Graph-based orchestration**: Stateful workflows with nodes/edges, persistence, streaming, human-in-the-loop patterns
- **Document-centric**: RAG-focused, knowledge management, document processing pipelines
- **Managed cloud services**: Vendor-hosted infrastructure, enterprise security, integrated identity management
- **Model-specific SDKs**: Tight integration with particular foundation models, native tool use
- **Enterprise integration**: .NET/Python ecosystems, cloud service integration, corporate IT alignment
- **Multi-agent conversation**: Agent-to-agent communication, collaborative problem solving, role-based architectures
- **Lightweight/composable**: Minimal dependencies, provider-agnostic, integration with workflow engines

### Major Frameworks

**LangChain/LangGraph**: Arguably the most recognized and widely adopted agent framework in the LLM ecosystem. Originally launched to simplify prompt chaining, it has evolved into full-fledged orchestration layer. LangChain is a Swiss army knife of AI agent frameworks, giving developers core components to wire up tools, prompts, memory, and reasoning. LangGraph handles single-agent, multi-agent, hierarchical, and sequential workflows.

**LangGraph Specifics**:
- Launched in early 2024 as new take on agentic framework
- Very low level, controllable agentic framework incorporating lessons learned from LangChain
- Graph architecture provides explicit state management where shared context persists across nodes
- Conditional transitions allow branching and routing to adapt dynamically at runtime
- Models agent workflows as graphs with State (shared data structure), Nodes (Python functions encoding logic), and Edges (Python functions determining next Node based on state)
- Supports human-in-the-loop through interruption mechanism with checkpoints
- Implements central persistence layer enabling memory that persists arbitrary aspects of application's state
- Breakpoints halt graph execution at critical points for human-in-the-loop dynamics
- State is checkpointed, so execution can be interrupted and resumed

**CrewAI**: Shines for role-based crews. Open-source framework for multi-agent systems, enabling AI agents to collaborate on tasks through defined roles and shared goals. Easy to get started—define crew, assign each agent a role, give shared objective. Most suited for demos and prototypes.

**AutoGPT**: Autonomous agent framework that turns GPT-chatbots into self-planning, goal-driven assistant. You hand it a goal, like "compile a market analysis," and it breaks job into subtasks, fetches data, writes files, or calls APIs on its own. Automates tasks using goal-driven agents that can plan and execute steps autonomously. Community-driven and easy to deploy, popular for experimentation, prototyping, and learning.

**Market Share**: Top 3 frameworks in terms of adoption rate are LangChain (30%), AutoGPT (25%), and CrewAI (20%).

### Framework Selection Criteria

Framework selection depends on multiple factors evaluated together:
- **Model alignment**: Some frameworks optimized for specific foundation models; consider whether model portability is required
- **Enterprise requirements**: Security controls, compliance features, support SLAs, vendor relationship
- **Existing infrastructure**: Cloud provider alignment, programming language ecosystem, development tooling
- **Use case fit**: Document-heavy (RAG-focused) vs. tool-heavy (orchestration-focused) vs. multi-agent (collaborative) workflows
- **Deployment model**: Managed cloud services vs. self-hosted infrastructure
- **Team expertise**: Development team familiarity with framework's paradigm and programming model
- **Observability**: Debugging, tracing, and monitoring capabilities for production deployments

**For Legal AI Applications**:
- Matter isolation: Framework support for strict data separation between client matters
- Audit logging: Comprehensive logging of all agent actions and decisions
- Legal platform integration: Ease of integrating with legal research platforms and document management systems
- Privilege preservation: Framework capabilities for maintaining attorney-client privilege in memory and tool systems

**Recommendations**: Start with single-agent frameworks like LangChain or Semantic Kernel for MVPs. Scale to multi-agent frameworks like CrewAI or AutoGen once workflows mature. For complex or enterprise use, LangChain, LangGraph, or AutoGen work well. For quick prototypes, AgentGPT or AutoGPT are more accessible.

**Sources**:
- [The Complete Guide to Choosing an AI Agent Framework in 2025 - Langflow](https://www.langflow.org/blog/the-complete-guide-to-choosing-an-ai-agent-framework-in-2025)
- [Top AI Agent Frameworks in 2025: LangChain, AutoGen, CrewAI - Medium](https://medium.com/@iamanraghuvanshi/agentic-ai-3-top-ai-agent-frameworks-in-2025-langchain-autogen-crewai-beyond-2fc3388e7dec)
- [A Detailed Comparison of Top 6 AI Agent Frameworks - Turing](https://www.turing.com/resources/ai-agent-frameworks)
- [Autogen vs LangChain vs CrewAI - Instinctools](https://www.instinctools.com/blog/autogen-vs-langchain-vs-crewai/)
- [Top 10 Open-Source AI Agent Frameworks for 2025 - SuperAGI](https://superagi.com/top-10-open-source-ai-agent-frameworks-for-2025-a-comparison-of-features-and-use-cases/)
- [LangGraph](https://www.langchain.com/langgraph)
- [LangGraph: Building Intelligent Multi-Agent Workflows - Medium](https://medium.com/@saimoguloju2/langgraph-building-intelligent-multi-agent-workflows-with-state-management-0427264b6318)
- [LangGraph 201: Adding Human Oversight - Towards Data Science](https://towardsdatascience.com/langgraph-201-adding-human-oversight-to-your-deep-research-agent/)

---

## Legal/Financial AI Applications

### Matter Isolation and Ethical Walls

Multi-client memory systems must implement ethical walls (also called "Chinese walls") to prevent information flow between matters with conflicts of interest. These walls must be enforced at memory layer, not just application layer.

Technical controls:
- Separate vector store namespaces or collections per client/matter
- Access control lists verified before any retrieval operation
- Audit trails for all memory access with tamper-resistant logging
- Secure deletion capabilities when matters close or conflicts arise

### Attorney-Client Privilege

ABA Formal Opinion 512 states: "Because the large language models used in generative AI continue to develop, some without safeguards similar to those already in use in law offices, such as ethical walls, they may run afoul of Rules 1.7 and 1.9 by using the information developed from one representation to inform another."

Privilege waiver risk: Attorney-client privilege can be waived if information is disclosed to outside party. AI-processed communications might not be protected from discovery if memory system stores or transmits data to third-party vendors. Some practitioners recommend using technology where information is not stored in AI memory.

### Legal Knowledge Graphs

Knowledge graph technology uses triples as basic unit, efficiently transforming multisource heterogeneous information into knowledge representation form close to human cognition. For legal AI:
- Combining multidimensional heterogeneous knowledge (legal provisions, judicial interpretations, cases, defenses) into structured triples
- Similar case recommendation based on constructed relationships
- Legislative systems support, compensating for LLM limitations with up-to-date external knowledge
- RAG enhancement through vector stores combined with hierarchical legal ontologies

Convergence of ontologies and Legal Knowledge Graphs highlights potential for facilitating 'explainable AI' in legal system, ensuring fairness and transparency in AI adoption.

### Legal Tool Composition Example

Rather than building monolithic "legal research" tool, compose specialized tools:
1. `search_cases(query, jurisdiction, date_range)`: Returns case citations
2. `retrieve_case(citation)`: Fetches full case text
3. `extract_holding(case_text)`: Identifies legal holding
4. `shepardize(citation)`: Returns case history and treatment
5. `format_citation(case_data, style)`: Formats citation in specified style

Agent orchestrates these tools to complete complex research tasks. Composition enables reuse and easier testing.

---

## Security Considerations

### Layered Security Architecture

A layered security architecture should implement defense-in-depth with security controls at multiple levels—network, application, agent, and data layers—to safeguard against complete system failure from a single compromise.

### Progressive Autonomy

Successful agentic deployments share common pattern: progressive autonomy deployment. Start with Scope 1 or 2 implementations and gradually advance through scopes as organizational confidence and security capabilities mature. This approach minimizes risk while building operational experience.

### Security Controls by Scope

Different deployment scopes require different security controls:
- **Scope 1**: Focus on identity context, workflow integrity, input validation
- **Scope 2**: Robust approval workflows, secure communication channels
- **Scope 3**: Continuous monitoring, behavioral validation, kill switches
- **Scope 4**: Dynamic context-aware limitations, comprehensive security controls

### Tool Permission Combinations

When tools are exposed via MCP servers, permission combinations can enable unintended data exfiltration. This becomes critical security concern requiring careful architectural consideration.

---

## References

### Agent Loop Patterns
- [ReAct: Synergizing Reasoning and Acting in Language Models - arXiv](https://arxiv.org/abs/2210.03629)
- [MRKL Systems - IBM](https://www.ibm.com/architectures/hybrid/genai-mrkl)
- [Reflexion: Language Agents with Verbal Reinforcement Learning - arXiv](https://arxiv.org/abs/2303.11366)
- [Tree of Thoughts: Deliberate Problem Solving - arXiv](https://arxiv.org/abs/2305.10601)
- [LLMCompiler: Parallel Function Calling - arXiv](https://arxiv.org/abs/2312.04511)
- [OODA loop - Wikipedia](https://en.wikipedia.org/wiki/OODA_loop)

### Tool Design & Function Calling
- [Writing effective tools for AI agents - Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [Best Practices for Function Calling in LLMs - Scalifiai](https://www.scalifiai.com/blog/function-calling-tool-call-best%20practices)
- [12-Factor Agents - Medium](https://medium.com/@agentics/12-factor-agents-principles-for-building-reliable-llm-applications-7bdbfad6ce84)

### Memory Systems & RAG
- [What Is AI Agent Memory? - IBM](https://www.ibm.com/think/topics/ai-agent-memory)
- [GraphRAG: From Local to Global - arXiv](https://arxiv.org/html/2404.16130v1)
- [RAFT: Adapting Language Model to Domain Specific RAG - arXiv](https://arxiv.org/abs/2403.10131)
- [DRAGIN: Dynamic Retrieval Augmented Generation - ACL Anthology](https://aclanthology.org/2024.acl-long.702/)
- [Agentic RAG Survey - arXiv](https://arxiv.org/abs/2501.09136)
- [Bridging Legal Knowledge and AI - arXiv](https://arxiv.org/html/2502.20364v1)
- [MemoriesDB: Temporal-Semantic-Relational Database - arXiv](https://arxiv.org/html/2511.06179v1)

### Security
- [Model Context Protocol: Security Overview - Palo Alto Networks](https://www.paloaltonetworks.com/blog/cloud-security/model-context-protocol-mcp-a-security-overview/)
- [MCP Security Vulnerabilities - Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-vulnerabilities/)
- [AWS Agentic AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/)
- [Execution Guardrails for AI Agentic Implementation](https://itzikr.wordpress.com/2025/01/08/execution-guardrails-for-ai-agentic-implementation/)

### Human-in-the-Loop
- [Key Issue 4: Human Oversight - EU AI Act](https://www.euaiact.com/key-issue/4)
- [EU AI Act Human Oversight Requirements - eyreACT](https://www.eyreact.com/eu-ai-act-human-oversight-requirements-comprehensive-implementation-guide/)
- [Article 14: Human Oversight - EU AI Act](https://artificialintelligenceact.eu/article/14/)

### Legal Ethics
- [ABA Formal Opinion 512](https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf)
- [ABA issues first ethics guidance on AI tools](https://www.americanbar.org/news/abanews/aba-news-archives/2024/07/aba-issues-first-ethics-guidance-ai-tools/)
- [AI and Attorney-Client Privilege - ABA](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-september/ai-attorney-client-privilege/)

### Multi-Agent Systems & Protocols
- [Announcing the Agent2Agent Protocol (A2A) - Google](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- [What Is Agent2Agent (A2A) Protocol? - IBM](https://www.ibm.com/think/topics/agent2agent-protocol)
- [Survey of Agent Interoperability Protocols - arXiv](https://arxiv.org/html/2505.02279v1)
- [Building Secure Multi-Agent AI Architectures - AppSecEngineer](https://www.appsecengineer.com/blog/building-secure-multi-agent-ai-architectures-for-enterprise-secops)

### Frameworks
- [LangGraph](https://www.langchain.com/langgraph)
- [Complete Guide to Choosing AI Agent Framework - Langflow](https://www.langflow.org/blog/the-complete-guide-to-choosing-an-ai-agent-framework-in-2025)
- [Top AI Agent Frameworks Comparison - Turing](https://www.turing.com/resources/ai-agent-frameworks)
- [Autogen vs LangChain vs CrewAI - Instinctools](https://www.instinctools.com/blog/autogen-vs-langchain-vs-crewai/)
