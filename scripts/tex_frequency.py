#!/usr/bin/env python3
"""
tex_frequency.py — Analyze word and n-gram frequencies in LaTeX documents.

This tool extracts text from LaTeX files and computes word, bigram, and trigram
frequencies to help identify:

    - Overused words and phrases
    - Repetitive language patterns
    - Domain term distribution
    - Writing variety and style consistency

Output Formats:
    - table: Rich formatted tables (default, human-readable)
    - json:  Single JSON object with all frequency data
    - jsonl: One JSON object per entry (streaming-friendly)
    - csv:   Comma-separated values

Usage:
    # Analyze a chapter
    uv run --with rich,typer scripts/tex_frequency.py chapters/07-agents-part-2/

    # Show top 100 results
    uv run --with rich,typer scripts/tex_frequency.py chapters/07-agents-part-2/ -n 100

    # Output as JSON for further processing
    uv run --with rich,typer scripts/tex_frequency.py chapters/07-agents-part-2/ -f json > freq.json

    # Per-file breakdown
    uv run --with rich,typer scripts/tex_frequency.py chapters/07-agents-part-2/ --show-files

Dependencies:
    pip install rich typer
    — or —
    uv run --with rich,typer scripts/tex_frequency.py ...
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# =============================================================================
# Dynamic Import Handling
# =============================================================================

def _import_with_hint(module_name: str, package_name: Optional[str] = None):
    """
    Import a module with a helpful error message if missing.

    Args:
        module_name: The module to import.
        package_name: The pip/uv package name if different from module name.

    Returns:
        The imported module.

    Raises:
        SystemExit: If the module is not found, with helpful install instructions.
    """
    package_name = package_name or module_name
    try:
        return __import__(module_name)
    except ImportError:
        print(f"\n✗ Missing required package: {package_name}", file=sys.stderr)
        print(f"\nInstall with:", file=sys.stderr)
        print(f"    pip install {package_name}", file=sys.stderr)
        print(f"\nOr run directly with uv:", file=sys.stderr)
        print(f"    uv run --with rich,typer {sys.argv[0]} ...", file=sys.stderr)
        sys.exit(1)


# Import required packages with helpful errors
typer_module = _import_with_hint("typer")
typer = typer_module
rich_module = _import_with_hint("rich")

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print as rprint

# Import local utilities
try:
    from tex_utils import (
        extract_paragraphs_from_tex,
        find_tex_files,
        find_section_files,
        clean_latex_text,
        tokenize_regex,
        get_ngrams,
        filter_stopwords,
        filter_stopword_ngrams,
        STOPWORDS,
    )
except ImportError:
    script_dir = Path(__file__).parent
    sys.path.insert(0, str(script_dir))
    from tex_utils import (
        extract_paragraphs_from_tex,
        find_tex_files,
        find_section_files,
        clean_latex_text,
        tokenize_regex,
        get_ngrams,
        filter_stopwords,
        filter_stopword_ngrams,
        STOPWORDS,
    )


# =============================================================================
# CLI Application
# =============================================================================

app = typer.Typer(
    name="tex-frequency",
    help="Analyze word and n-gram frequencies in LaTeX documents.",
    add_completion=False,
    rich_markup_mode="rich",
)

console = Console()


# =============================================================================
# Domain Terms
# =============================================================================

DOMAIN_TERMS = frozenset({
    # AI/ML
    "agent", "agents", "agentic", "model", "models", "llm", "llms",
    "prompt", "prompts", "prompting", "inference", "training",
    "embedding", "embeddings", "retrieval", "rag",
    # Tools & Architecture
    "tool", "tools", "memory", "planning", "plan", "workflow", "workflows",
    "protocol", "protocols", "api", "apis", "mcp", "a2a",
    "architecture", "framework", "frameworks", "system", "systems",
    # Legal
    "legal", "attorney", "attorneys", "lawyer", "lawyers", "law",
    "associate", "associates", "partner", "partners", "paralegal",
    "client", "clients", "contract", "contracts", "litigation",
    "compliance", "regulatory", "regulation", "regulations",
    "court", "courts", "judge", "judges", "statute", "statutes",
    # Finance
    "financial", "finance", "bank", "banks", "banking",
    "investment", "investments", "portfolio", "portfolios",
    "risk", "risks", "trading", "market", "markets",
    "transaction", "transactions", "audit", "auditing",
    # Evaluation
    "evaluation", "evaluate", "benchmark", "benchmarks",
    "accuracy", "precision", "recall", "metric", "metrics",
})


# =============================================================================
# Analysis Functions
# =============================================================================

def analyze_files(files: List[Path], min_words: int = 5) -> Dict:
    """
    Extract and tokenize text from multiple files.

    Returns dict with:
        - all_tokens: Combined token list
        - file_tokens: Per-file token lists
        - total_files: Number of files processed
    """
    all_tokens: List[str] = []
    file_tokens: Dict[str, List[str]] = {}

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        cleaned = clean_latex_text(content)
        tokens = tokenize_regex(cleaned)
        tokens_lower = [t.lower() for t in tokens]

        all_tokens.extend(tokens_lower)
        file_tokens[file_path.name] = tokens_lower

    return {
        "all_tokens": all_tokens,
        "file_tokens": file_tokens,
        "total_files": len(files),
    }


def compute_frequencies(
    tokens: List[str],
    include_stopwords: bool = False,
) -> Dict:
    """
    Compute word, bigram, and trigram frequencies.

    Returns dict with Counter objects for each n-gram type.
    """
    # Filter stopwords for content analysis
    if include_stopwords:
        content_tokens = tokens
    else:
        content_tokens = filter_stopwords(tokens)

    # Word frequencies
    word_counts = Counter(content_tokens)

    # Bigrams
    bigrams = get_ngrams(tokens, 2)
    content_bigrams = filter_stopword_ngrams(bigrams, min_content=1)
    bigram_counts = Counter(content_bigrams)

    # Trigrams
    trigrams = get_ngrams(tokens, 3)
    content_trigrams = filter_stopword_ngrams(trigrams, min_content=2)
    trigram_counts = Counter(content_trigrams)

    return {
        "words": word_counts,
        "bigrams": bigram_counts,
        "trigrams": trigram_counts,
        "total_tokens": len(tokens),
        "total_content_tokens": len(content_tokens),
    }


def get_domain_term_frequencies(
    word_counts: Counter,
    total_tokens: int,
) -> List[Dict]:
    """Get frequencies for domain-specific terms."""
    results = []
    for term in sorted(DOMAIN_TERMS):
        count = word_counts.get(term, 0)
        if count > 0:
            per_1000 = (count / total_tokens) * 1000 if total_tokens > 0 else 0
            results.append({
                "term": term,
                "count": count,
                "per_1000": round(per_1000, 2),
            })

    return sorted(results, key=lambda x: -x["count"])


def find_repetitive_phrases(
    bigram_counts: Counter,
    trigram_counts: Counter,
    bigram_threshold: int = 5,
    trigram_threshold: int = 3,
) -> Dict:
    """Identify potentially repetitive phrases."""
    # Bigrams with no stopwords that appear frequently
    repetitive_bigrams = [
        (" ".join(bg), count)
        for bg, count in bigram_counts.most_common(100)
        if count >= bigram_threshold
        and not any(w in STOPWORDS for w in bg)
    ]

    # Trigrams with at least 2 content words
    repetitive_trigrams = [
        (" ".join(tg), count)
        for tg, count in trigram_counts.most_common(100)
        if count >= trigram_threshold
        and sum(1 for w in tg if w not in STOPWORDS) >= 2
    ]

    return {
        "bigrams": repetitive_bigrams[:30],
        "trigrams": repetitive_trigrams[:30],
    }


# =============================================================================
# Output Formatters
# =============================================================================

def format_ngram(ngram: Tuple[str, ...]) -> str:
    """Format n-gram tuple as readable string."""
    return " ".join(ngram)


def output_table(
    frequencies: Dict,
    domain_terms: List[Dict],
    repetitive: Dict,
    file_tokens: Dict[str, List[str]],
    top_n: int = 50,
    min_count: int = 3,
    show_files: bool = False,
):
    """Output as rich tables."""
    total = frequencies["total_tokens"]
    content = frequencies["total_content_tokens"]

    # Summary panel
    summary = f"[bold]{total:,}[/bold] total tokens"
    summary += f" | [bold]{content:,}[/bold] content words"
    summary += f" | [dim]{len(file_tokens)} files[/dim]"
    console.print(Panel(summary, title="[bold blue]Frequency Analysis[/bold blue]", expand=False))

    # Word frequency table
    _output_word_table(frequencies["words"], top_n, min_count, content)

    # Bigram table
    _output_ngram_table(
        frequencies["bigrams"], "Bigrams", top_n, min_count
    )

    # Trigram table
    _output_ngram_table(
        frequencies["trigrams"], "Trigrams", top_n, min_count
    )

    # Domain terms
    if domain_terms:
        _output_domain_table(domain_terms)

    # Repetitive phrases
    if repetitive["bigrams"] or repetitive["trigrams"]:
        _output_repetitive_table(repetitive)

    # Per-file breakdown
    if show_files:
        _output_file_breakdown(file_tokens)


def _output_word_table(counts: Counter, top_n: int, min_count: int, total: int):
    """Output word frequency table."""
    table = Table(title=f"Top {top_n} Words (excluding stopwords)")
    table.add_column("Rank", style="dim", width=5)
    table.add_column("Word", style="cyan")
    table.add_column("Count", style="magenta", justify="right")
    table.add_column("%", style="yellow", justify="right")
    table.add_column("Bar", style="green")

    max_count = counts.most_common(1)[0][1] if counts else 1

    for i, (word, count) in enumerate(counts.most_common(top_n), 1):
        if count < min_count:
            break
        pct = (count / total) * 100 if total > 0 else 0
        bar_len = int((count / max_count) * 20)
        bar = "█" * bar_len

        table.add_row(str(i), word, str(count), f"{pct:.2f}", bar)

    console.print(table)


def _output_ngram_table(counts: Counter, title: str, top_n: int, min_count: int):
    """Output n-gram frequency table."""
    table = Table(title=f"Top {top_n} {title}")
    table.add_column("Rank", style="dim", width=5)
    table.add_column("Phrase", style="cyan")
    table.add_column("Count", style="magenta", justify="right")
    table.add_column("Bar", style="green")

    max_count = counts.most_common(1)[0][1] if counts else 1

    for i, (ngram, count) in enumerate(counts.most_common(top_n), 1):
        if count < min_count:
            break
        bar_len = int((count / max_count) * 20)
        bar = "█" * bar_len

        table.add_row(str(i), format_ngram(ngram), str(count), bar)

    console.print(table)


def _output_domain_table(domain_terms: List[Dict]):
    """Output domain term frequency table."""
    table = Table(title="Domain Term Frequency")
    table.add_column("Term", style="cyan")
    table.add_column("Count", style="magenta", justify="right")
    table.add_column("Per 1000", style="yellow", justify="right")

    for item in domain_terms[:30]:
        table.add_row(item["term"], str(item["count"]), f"{item['per_1000']:.1f}")

    console.print(table)


def _output_repetitive_table(repetitive: Dict):
    """Output potentially repetitive phrases."""
    console.print(Panel("[bold yellow]Potentially Repetitive Phrases[/bold yellow]", expand=False))

    if repetitive["bigrams"]:
        table = Table(title="Repetitive Bigrams (5+ occurrences, no stopwords)")
        table.add_column("Phrase", style="cyan")
        table.add_column("Count", style="magenta", justify="right")
        table.add_column("Review?", style="red")

        for phrase, count in repetitive["bigrams"]:
            review = "← review" if count >= 8 else ""
            table.add_row(phrase, str(count), review)

        console.print(table)

    if repetitive["trigrams"]:
        table = Table(title="Repetitive Trigrams (3+ occurrences)")
        table.add_column("Phrase", style="cyan")
        table.add_column("Count", style="magenta", justify="right")

        for phrase, count in repetitive["trigrams"]:
            table.add_row(phrase, str(count))

        console.print(table)


def _output_file_breakdown(file_tokens: Dict[str, List[str]]):
    """Output per-file token breakdown."""
    table = Table(title="Per-File Breakdown")
    table.add_column("File", style="green")
    table.add_column("Tokens", style="magenta", justify="right")
    table.add_column("Unique", style="cyan", justify="right")
    table.add_column("Lexical Diversity", style="yellow", justify="right")

    for filename, tokens in sorted(file_tokens.items()):
        unique = len(set(tokens))
        diversity = (unique / len(tokens)) * 100 if tokens else 0
        table.add_row(
            filename,
            str(len(tokens)),
            str(unique),
            f"{diversity:.1f}%",
        )

    console.print(table)


def output_json(
    frequencies: Dict,
    domain_terms: List[Dict],
    repetitive: Dict,
    file_tokens: Dict[str, List[str]],
    top_n: int = 50,
):
    """Output as JSON."""
    data = {
        "summary": {
            "total_tokens": frequencies["total_tokens"],
            "content_tokens": frequencies["total_content_tokens"],
            "files": len(file_tokens),
        },
        "words": [
            {"word": w, "count": c}
            for w, c in frequencies["words"].most_common(top_n)
        ],
        "bigrams": [
            {"phrase": format_ngram(ng), "count": c}
            for ng, c in frequencies["bigrams"].most_common(top_n)
        ],
        "trigrams": [
            {"phrase": format_ngram(ng), "count": c}
            for ng, c in frequencies["trigrams"].most_common(top_n)
        ],
        "domain_terms": domain_terms,
        "repetitive": {
            "bigrams": [{"phrase": p, "count": c} for p, c in repetitive["bigrams"]],
            "trigrams": [{"phrase": p, "count": c} for p, c in repetitive["trigrams"]],
        },
        "files": {
            name: {"tokens": len(toks), "unique": len(set(toks))}
            for name, toks in file_tokens.items()
        },
    }
    print(json.dumps(data, indent=2))


def output_jsonl(
    frequencies: Dict,
    domain_terms: List[Dict],
    repetitive: Dict,
    file_tokens: Dict[str, List[str]],
    top_n: int = 50,
):
    """Output as JSON Lines."""
    # Words
    for word, count in frequencies["words"].most_common(top_n):
        print(json.dumps({"type": "word", "value": word, "count": count}))

    # Bigrams
    for ngram, count in frequencies["bigrams"].most_common(top_n):
        print(json.dumps({"type": "bigram", "value": format_ngram(ngram), "count": count}))

    # Trigrams
    for ngram, count in frequencies["trigrams"].most_common(top_n):
        print(json.dumps({"type": "trigram", "value": format_ngram(ngram), "count": count}))


def output_csv(
    frequencies: Dict,
    domain_terms: List[Dict],
    repetitive: Dict,
    file_tokens: Dict[str, List[str]],
    top_n: int = 50,
):
    """Output as CSV."""
    writer = csv.writer(sys.stdout)
    writer.writerow(["type", "value", "count", "percentage"])

    total = frequencies["total_content_tokens"]

    for word, count in frequencies["words"].most_common(top_n):
        pct = (count / total) * 100 if total > 0 else 0
        writer.writerow(["word", word, count, f"{pct:.4f}"])

    for ngram, count in frequencies["bigrams"].most_common(top_n):
        writer.writerow(["bigram", format_ngram(ngram), count, ""])

    for ngram, count in frequencies["trigrams"].most_common(top_n):
        writer.writerow(["trigram", format_ngram(ngram), count, ""])


# =============================================================================
# Main Command
# =============================================================================

@app.command()
def main(
    paths: List[Path] = typer.Argument(
        ...,
        help="LaTeX files or directories to analyze",
        exists=True,
    ),
    format: str = typer.Option(
        "table",
        "--format", "-f",
        help="Output format: table, json, jsonl, csv",
    ),
    top: int = typer.Option(
        50,
        "--top", "-n",
        help="Number of top results to show",
        min=10,
        max=500,
    ),
    min_count: int = typer.Option(
        3,
        "--min-count", "-m",
        help="Minimum occurrences to display",
        min=1,
    ),
    show_files: bool = typer.Option(
        False,
        "--show-files",
        help="Show per-file breakdown (table format only)",
    ),
    include_stopwords: bool = typer.Option(
        False,
        "--include-stopwords",
        help="Include stopwords in word frequency",
    ),
    bigrams_only: bool = typer.Option(
        False,
        "--bigrams-only",
        help="Only output bigram analysis",
    ),
    trigrams_only: bool = typer.Option(
        False,
        "--trigrams-only",
        help="Only output trigram analysis",
    ),
    recursive: bool = typer.Option(
        True,
        "--recursive/--no-recursive", "-r/-R",
        help="Search directories recursively",
    ),
    sections_only: bool = typer.Option(
        False,
        "--sections-only", "-s",
        help="Only look in sections/ subdirectory",
    ),
):
    """
    Analyze word and n-gram frequencies in LaTeX documents.

    Identifies overused words and phrases, domain term distribution,
    and potential repetitive language patterns.

    Examples:

        # Basic analysis of a chapter
        tex-frequency chapters/07-agents-part-2/

        # Top 100 results
        tex-frequency chapters/07-agents-part-2/ --top 100

        # Output as JSON
        tex-frequency chapters/07-agents-part-2/ -f json > freq.json

        # Per-file breakdown
        tex-frequency chapters/07-agents-part-2/ --show-files
    """
    # Collect files
    all_files: List[Path] = []

    for path in paths:
        if path.is_file():
            all_files.append(path)
        elif path.is_dir():
            if sections_only:
                all_files.extend(find_section_files(path))
            else:
                all_files.extend(find_tex_files(path, recursive=recursive))

    if not all_files:
        console.print("[red]Error:[/red] No .tex files found", file=sys.stderr)
        raise typer.Exit(1)

    # Extract and analyze
    if format == "table":
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Analyzing...", total=1)
            analysis = analyze_files(all_files)
            frequencies = compute_frequencies(
                analysis["all_tokens"],
                include_stopwords=include_stopwords,
            )
            progress.advance(task)
    else:
        analysis = analyze_files(all_files)
        frequencies = compute_frequencies(
            analysis["all_tokens"],
            include_stopwords=include_stopwords,
        )

    # Compute additional metrics
    domain_terms = get_domain_term_frequencies(
        frequencies["words"],
        frequencies["total_tokens"],
    )
    repetitive = find_repetitive_phrases(
        frequencies["bigrams"],
        frequencies["trigrams"],
    )

    # Output
    if format == "table":
        output_table(
            frequencies,
            domain_terms,
            repetitive,
            analysis["file_tokens"],
            top_n=top,
            min_count=min_count,
            show_files=show_files,
        )
    elif format == "json":
        output_json(
            frequencies,
            domain_terms,
            repetitive,
            analysis["file_tokens"],
            top_n=top,
        )
    elif format == "jsonl":
        output_jsonl(
            frequencies,
            domain_terms,
            repetitive,
            analysis["file_tokens"],
            top_n=top,
        )
    elif format == "csv":
        output_csv(
            frequencies,
            domain_terms,
            repetitive,
            analysis["file_tokens"],
            top_n=top,
        )
    else:
        console.print(f"[red]Error:[/red] Unknown format: {format}", file=sys.stderr)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
