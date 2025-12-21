# Artificial Intelligence for Law and Finance

**A Modern Textbook at the Intersection of AI, Law, and Finance**

🚧 **Status: Working Draft** (Last Updated: December 2025)

Welcome! This repository contains the evolving draft of *Artificial Intelligence for Law and Finance*, an open-source textbook designed to bridge the gap between AI and its practical applications in legal and financial domains.

⭐ **Stay Updated**: [Star this repository](https://github.com/mjbommar/ai-law-finance-book) or click "Watch" to get notified of new chapters and updates!

---

## 🧭 Chapter Roadmap (ToC + TODO)

Legend:
- `[x]` Finished chapter (current working draft ready for readers)
- `[~]` In progress (substantial draft exists, still being developed)
- `[ ]` Planned (outline or resources only)

### Part I — Foundations: LLMs and Prompting

- [~] **01 — Foundations: LLM Primer and Mechanics**  
  [source](chapters/01-foundations-llm-primer-mechanics)

- [~] **02 — Foundations: Conversations and Reasoning**  
  [source](chapters/02-foundations-conversations-reasoning)

- [~] **03 — Foundations: Structured Outputs and Tool Use**  
  [source](chapters/03-foundations-structured-tools-multimodal)

- [~] **04 — Foundations: Multimodal Fundamentals**  
  [source](chapters/04-foundations-multimodal)

- [~] **05 — Foundations: Prompt Design, Evaluation, and Optimization**  
  [source](chapters/05-foundations-prompt-design-eval-optimization)

### Part II — Agents and Agentic Systems

- [x] **06 — Agents Part I: What Is an Agent?**  
  [PDF](chapters/06-agents-part-1/main.pdf) · [source](chapters/06-agents-part-1)

- [x] **07 — Agents Part II: How to Build an Agent**  
  [PDF](chapters/07-agents-part-2/main.pdf) · [source](chapters/07-agents-part-2)

- [x] **08 — Agents Part III: How to Govern an Agent**  
  [PDF](chapters/08-agents-part-3/main.pdf) · [source](chapters/08-agents-part-3)

### Part III — Knowledge Graphs & Semantic Web

- [~] **09 — Knowledge Graphs & Semantic Web: Foundations for Law and Finance**  
  [source](chapters/09-kg-foundations)

- [~] **10 — Knowledge Graphs & Semantic Web: Operations with LLMs**  
  [source](chapters/10-kg-operations-llm)

## 📚 About This Book

We're creating a comprehensive, vendor-neutral resource that combines academic rigor with real-world practicality. Whether you're a legal professional exploring AI's impact on your field, a financial analyst considering machine learning applications, or a researcher studying this interdisciplinary space, this book is for you.

### Who This Book Is For

- **Practitioners**: Lawyers, compliance officers, risk managers, and financial professionals seeking to understand and apply AI
- **Regulators & Policymakers**: Those shaping the future of AI governance in law and finance
- **Graduate Students & Researchers**: Academics exploring the intersection of AI, law, economics, and information systems
- **Industry Builders**: Technologists and entrepreneurs developing AI solutions for legal and financial sectors

## 🌐 Coming Soon: ai4lf.com

We're building a dedicated website at **[ai4lf.com](https://ai4lf.com)** where you'll be able to:
- Read the book online with enhanced navigation
- Access interactive examples and visualizations
- Download the latest versions in multiple formats
- Join the community discussion

Stay tuned for the launch!

## 📖 Read the Latest Drafts

Want to dive right in? Here's where to find the current PDF drafts:

### 📚 Complete Book
- **main.pdf** — The full book with all current chapters integrated (working draft). Generate locally via `make pdf`.

### 📑 Individual Chapters
Current standalone chapter PDFs (all working drafts unless marked finished in the roadmap):

- **01 — Foundations: LLM Primer and Mechanics** — [chapters/01-foundations-llm-primer-mechanics/main.pdf](chapters/01-foundations-llm-primer-mechanics/main.pdf)
- **02 — Foundations: Conversations and Reasoning** — [chapters/02-foundations-conversations-reasoning/main.pdf](chapters/02-foundations-conversations-reasoning/main.pdf)
- **03 — Foundations: Structured Outputs and Tool Use** — [chapters/03-foundations-structured-tools-multimodal/main.pdf](chapters/03-foundations-structured-tools-multimodal/main.pdf)
- **04 — Foundations: Multimodal Fundamentals** — [chapters/04-foundations-multimodal/main.pdf](chapters/04-foundations-multimodal/main.pdf)
- **05 — Foundations: Prompt Design, Evaluation, and Optimization** — [chapters/05-foundations-prompt-design-eval-optimization/main.pdf](chapters/05-foundations-prompt-design-eval-optimization/main.pdf)
- **06 — Agents Part I: What Is an Agent?** — [chapters/06-agents-part-1/main.pdf](chapters/06-agents-part-1/main.pdf)
- **07 — Agents Part II: How to Build an Agent** — [chapters/07-agents-part-2/main.pdf](chapters/07-agents-part-2/main.pdf)
- **08 — Agents Part III: How to Govern an Agent** — [chapters/08-agents-part-3/main.pdf](chapters/08-agents-part-3/main.pdf)
- **09 — Knowledge Graphs & Semantic Web: Foundations for Law and Finance** — [chapters/09-kg-foundations/main.pdf](chapters/09-kg-foundations/main.pdf)
- **10 — Knowledge Graphs & Semantic Web: Operations with LLMs** — [chapters/10-kg-operations-llm/main.pdf](chapters/10-kg-operations-llm/main.pdf)

More chapters coming soon! This is a living document—we're actively writing and revising.

⭐ **Star this repository** to get notified when new chapters are published!

## 📘 Mini Books

- **Agents in Law & Finance** — [minibooks/agents-in-law-finance](minibooks/agents-in-law-finance) (standalone mini book with its own build files)

## 🚀 Getting Started

### For Readers
Simply download the PDFs above and start reading! We welcome feedback through [GitHub issues](https://github.com/mjbommar/ai-law-finance-book/issues).

### For Contributors
We'd love your help making this book better! Whether you're fixing a typo, improving an explanation, or adding new content, your contributions are welcome.

#### Quick Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/mjbommar/ai-law-finance-book.git
   cd ai-law-finance-book
   ```

2. **Build the book** (requires LaTeX):
   ```bash
   make pdf  # Build the complete book
   ```

3. **Work on a specific chapter**:
   ```bash
   cd chapters/06-agents-part-1
   make pdf  # Build just this chapter
   ```

## 📂 Repository Structure

We've organized everything to be intuitive and maintainable:

```
📁 ai-law-finance-book/
├── 📄 main.tex           # Complete book document
├── 📄 main.pdf           # 👈 Full book PDF (generated; not tracked)
├── 📄 Makefile           # Build automation
├── 📄 preamble.tex       # Shared LaTeX configuration
├── 📁 chapters/          # Individual chapter workspaces
│   ├── 📁 01-foundations-llm-primer-mechanics/
│   ├── 📁 02-foundations-conversations-reasoning/
│   ├── 📁 03-foundations-structured-tools-multimodal/
│   ├── 📁 04-foundations-multimodal/
│   ├── 📁 05-foundations-prompt-design-eval-optimization/
│   ├── 📁 06-agents-part-1/
│   │   ├── main.tex
│   │   ├── main.pdf      # 👈 Chapter PDF (current working draft)
│   │   └── sections/
│   ├── 📁 07-agents-part-2/
│   ├── 📁 08-agents-part-3/
│   ├── 📁 09-kg-foundations/
│   └── 📁 10-kg-operations-llm/
├── 📁 minibooks/         # Standalone mini books
│   └── 📁 agents-in-law-finance/
├── 📁 docs/              # Style and contribution guides
│   ├── build-guide.md    # Build system documentation
│   ├── style-guide.md    # Writing standards
│   └── color-guide.md    # Visual design system
├── 📁 scripts/           # Quality check tools
├── 📄 AGENTS.md          # Contributor workflows
├── 📄 CLAUDE.md          # AI assistant guide
└── 📄 README.md          # You are here!
```

## 🔨 Building from Source

### Prerequisites
You'll need a LaTeX distribution installed:
- **macOS**: MacTeX or BasicTeX
- **Linux**: TeX Live (`sudo apt install texlive-full` or equivalent)
- **Windows**: MiKTeX or TeX Live
- **Docker Alternative**: No local install needed! Just use `make docker`

### Build Commands

#### Build Everything
```bash
make pdf          # Build the complete book
make all-pdfs     # Build book + all individual chapters
```

#### Build Individual Chapters
```bash
cd chapters/06-agents-part-1
make pdf          # Full build with bibliography
make quick        # Quick preview (single pass)
make validate     # Check references and citations
```

#### Other Useful Commands
```bash
make clean        # Remove temporary files
make cleanall     # Remove everything including PDFs
make wordcount    # Get word counts for tracking progress
```

## ✍️ Writing Guidelines

### Our Approach
We aim for clarity and accessibility while maintaining academic rigor. Think of your favorite textbook—the one that made complex topics click. That's what we're building here.

### Key Principles
- **Tone**: Professional yet approachable, like a knowledgeable colleague explaining concepts
- **Citations**: Every claim needs backing. We use BibLaTeX with full metadata
- **Examples**: Real-world scenarios from law firms, banks, and regulatory bodies
- **Visuals**: Diagrams and figures to illuminate complex concepts

For detailed guidelines, see our [Style Guide](docs/style-guide.md).

## 🤝 Contributing

We welcome contributions from practitioners, academics, and anyone passionate about AI's intersection with law and finance!

### How to Contribute

1. **Small improvements**: Typo fixes, clarifications, or citation updates—just submit a PR!
2. **New content**: Open an issue first to discuss your ideas
3. **Feedback**: Use [GitHub issues](https://github.com/mjbommar/ai-law-finance-book/issues) to suggest improvements

### Contribution Guidelines
- Write for your audience: legal and financial professionals who may be new to AI
- Back up claims with citations from primary sources
- Test your LaTeX thoroughly before submitting
- Keep commits focused and descriptive

See [AGENTS.md](AGENTS.md) for detailed contribution workflows.

## 🛠️ Development Tools

### Quality Checks
Run these scripts to validate your contributions:

```bash
# Run all checks on the repository
./scripts/run_all.sh .

# Test a specific chapter
./scripts/test_chapter.sh chapters/06-agents-part-1
```

Our validation suite includes:
- **Markdown**: Linting and style checks
- **Spelling**: Multiple spell checkers
- **LaTeX**: Syntax and reference validation
- **Bibliography**: Citation format verification
- **Links**: URL validation

## 📜 Legal Disclaimer

This textbook is for **educational purposes only**. Nothing in this book constitutes:
- Legal advice or attorney-client relationship
- Financial, investment, or trading advice
- Professional consulting or recommendations

Always consult qualified professionals for specific legal or financial matters. Examples are illustrative—verify current laws and regulations in your jurisdiction.

## 🗺️ Roadmap

### Coming Soon (Q4 2025 - Q1 2026)
- Launch website at [ai4lf.com](https://ai4lf.com)
- Complete planned Prompting & Meta-Prompting chapter
- Add interactive Jupyter notebooks for examples
- Implement continuous integration for PDF builds

### Future Plans (2026)
- Complete 10 core chapters covering AI fundamentals for law and finance
- Add case studies from major financial institutions and law firms
- Create companion course materials for universities
- Develop practitioner resources and workshops

## 📬 Contact & Community

- **Issues & Feedback**: [GitHub Issues](https://github.com/mjbommar/ai-law-finance-book/issues)
- **Website**: [ai4lf.com](https://ai4lf.com) (coming soon)
- **Updates**: Star this repository for notifications

## 📄 License

This work is licensed under Creative Commons Attribution 4.0 International License (CC BY 4.0).

You are free to:
- **Share**: Copy and redistribute the material
- **Adapt**: Remix, transform, and build upon the material

As long as you provide appropriate credit and indicate changes.

---

*Building bridges between artificial intelligence and professional practice in law and finance.*
