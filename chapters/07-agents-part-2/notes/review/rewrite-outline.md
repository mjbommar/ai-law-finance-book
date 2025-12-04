# Event-Driven Rewrite Outline (Part II)  

## 1. Why This Part (Bridge from Part I, Toward Governance)  
### 1.1 Motivation  
- Move from “what is an agent” (GPA+IAT in 06-agents-part-1) to “how agents actually run in production.”  
- Anchor in current intro (`sections/01-introduction.tex`).  
### 1.2 Why event-driven framing  
- Production work = continuous triggers (filings, prices, deadlines) vs. pure chat.  
- Tie to portfolio monitoring scope/autonomy discussion (`sections/03-architecture.tex`).  
- What we still cover (organized by events): tool types, planning patterns (ReAct / Plan-Execute / hierarchical), memory & RAG design, protocols, and HITL controls.  
### 1.3 Forward look  
- Governance & compliance (Part III) depend on knowing when/where events fire (approvals, audits).  
- Set expectation for next chapter: controls map to triggers/handlers.  

## 2. Triggers & Channels (Entry Points)  
### 2.1 External signals  
- Webhooks/feeds: dockets, market data, calendar deadlines.  
- Use portfolio drift trigger (`sections/06-synthesis.tex`).  
### 2.2 Human prompts (chat/console)  
- Intent clarification flow (ReAct example `sections/03-architecture.tex` §3.3.1).  
- Explicitly: any user-originated message (email, Slack/Teams, ticket, chat box) is an event entering the dispatcher.  
### 2.3 Scheduled jobs  
- EOD reconciliations, periodic validations.  
### 2.4 Approval/exception events  
- Escalation when budgets/confidence trip (“Human-in-the-Loop Integration” `sections/03-architecture.tex`).  

## 3. Dispatch & Planning (Event → Plan)  
### 3.1 Intent/goal classification  
- Patterns from `sections/03-architecture.tex` §3.3.1.  
### 3.2 Planner selection  
- ReAct for exploratory (chat); Plan-Execute for checklists (credit review, `sections/06-synthesis.tex`); hierarchical for multi-agent (portfolio).  
### 3.3 Escalation policies  
- Termination criteria, confidence thresholds, loop limits (“Knowing When to Stop” / “Guardrails” `sections/03-architecture.tex`).  

## 4. Resources Bound to Events (Tools & Memory)  
### 4.1 Tool registry & routing  
- Least privilege, rate limits (“Tool Design Principles/Selection” `sections/03-architecture.tex` §§3.2.2–3.2.5).  
### 4.2 Memory keyed to task/matter/client  
- Working, episodic, RAG, vector (“Memory Layers” `sections/03-architecture.tex` §3.2.6).  
### 4.3 Isolation & validity  
- Matter/MNPI walls, shepardizing/temporal checks (“Domain-Specific Memory Requirements” `sections/03-architecture.tex`).  

## 5. Handler Lifecycle (Execution Loop & Guards)  
### 5.1 Core PERCEIVE–REASON–ACT–UPDATE loop  
- From “Core Agent Loop” `sections/03-architecture.tex` §3.2.1.  
### 5.2 Budgets  
- Tokens/time/tool calls/cost (“Guardrails and Loop Detection” §3.3.3).  
### 5.3 Reversibility classes → approvals  
- “Human Oversight Decision Matrix” §3.3.4.  

## 6. Protocol Plumbing  
### 6.1 MCP inside handlers  
- `sections/04-protocols.tex` §§4.2–4.2.2.  
### 6.2 A2A for delegated tasks  
- `sections/04-protocols.tex` §§4.3–4.3.2.  
### 6.3 Dual-protocol fan-out  
- “Dual Protocol Strategy” §4.4.  

## 7. Surfaces (UX Modes Sharing the Spine)  
### 7.1 Chat surface  
- Minimal clarifications, inline cites (trimmed from intent examples).  
### 7.2 Automation surface  
- Alerts/dashboards/tickets (portfolio monitors, `sections/06-synthesis.tex`).  
### 7.3 Document-first surface  
- Issue lists/memos (credit review artifacts, `sections/06-synthesis.tex`).  

## 8. Evaluation Mapped to Events  
*(Scope note: high-level only—what to evaluate and where; detailed metrics/procedures live in Part III and the Evaluation chapter.)*  
### 8.1 Layer 1 (retrieval) per handler  
- `sections/05-evaluation.tex` §§5.1–5.2.  
### 8.2 Layer 2 (reasoning) per plan  
- Misgrounding vs. hallucination rubric.  
### 8.3 Layer 3 (workflow) per event SLA  
- Termination correctness, approval paths (`sections/05-evaluation.tex` §§5.3–5.4).  
### 8.4 Continuous monitoring  
- Long-running handlers (“Continuous Evaluation” §5.5).  
### 8.5 Security by channel  
- Prompt injection (chat), payload validation (webhooks), isolation (memory) (“Security Evaluation” §5.4).  

## 9. Case Studies Reframed Around Events  
### 9.1 Credit facility review  
- Trigger = new draft uploaded; Plan-Execute checklist; approvals on high-severity flags (`sections/06-synthesis.tex`).  
### 9.2 Portfolio monitoring  
- Trigger = exposure/price drift; chain = Monitoring → Rebalancing → Compliance → PM approval (`sections/06-synthesis.tex`).  
### 9.3 Optional chat micro-flow  
- Trigger = user query; ReAct + retrieval; approval if write action (ReAct exemplar `sections/03-architecture.tex`).  

## 10. Governance On-Ramp (Bridge to Next Chapter)  
### 10.1 Map events to controls  
- Which triggers require approvals, audits, segregation, rate limits.  
### 10.2 Accountability & logging  
- Tie handler traces to compliance evidence (sets up Part III).  
### 10.3 Policy artifacts  
- Runbooks, approval matrices, retention rules keyed to event types.  
