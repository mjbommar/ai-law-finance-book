#!/usr/bin/env python3
"""
tex_paragraphs.py — Analyze paragraph structure in LaTeX documents.

This tool extracts prose paragraphs from LaTeX files and analyzes their
structure to help identify:

    - Short paragraphs that may indicate choppy writing
    - Long paragraphs that may need breaking up
    - Paragraph length distribution
    - Potential merge or split candidates

Output Formats:
    - table: Rich formatted tables (default, human-readable)
    - json:  Single JSON object with all paragraph data
    - jsonl: One JSON object per paragraph (streaming-friendly)
    - csv:   Comma-separated values

Usage:
    # Find short paragraphs (< 30 words)
    uv run --with rich,typer scripts/tex_paragraphs.py chapters/07-agents-part-2/

    # Custom threshold
    uv run --with rich,typer scripts/tex_paragraphs.py chapters/07-agents-part-2/ --max-words 50

    # Find long paragraphs instead
    uv run --with rich,typer scripts/tex_paragraphs.py chapters/07-agents-part-2/ --long

    # Output as JSON for processing
    uv run --with rich,typer scripts/tex_paragraphs.py chapters/07-agents-part-2/ -f json > paragraphs.json

Dependencies:
    pip install rich typer
    — or —
    uv run --with rich,typer scripts/tex_paragraphs.py ...
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from dataclasses import dataclass
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
        Paragraph,
        extract_paragraphs_from_tex,
        find_tex_files,
        find_section_files,
        tokenize_regex,
    )
except ImportError:
    script_dir = Path(__file__).parent
    sys.path.insert(0, str(script_dir))
    from tex_utils import (
        Paragraph,
        extract_paragraphs_from_tex,
        find_tex_files,
        find_section_files,
        tokenize_regex,
    )


# =============================================================================
# CLI Application
# =============================================================================

app = typer.Typer(
    name="tex-paragraphs",
    help="Analyze paragraph structure in LaTeX documents.",
    add_completion=False,
    rich_markup_mode="rich",
)

console = Console()


# =============================================================================
# Analysis Data Classes
# =============================================================================

@dataclass
class ParagraphAnalysis:
    """Extended paragraph analysis with context."""
    paragraph: Paragraph
    context_before: Optional[str] = None
    context_after: Optional[str] = None
    issue: str = ""  # "short", "long", or ""


# =============================================================================
# Analysis Functions
# =============================================================================

def analyze_paragraphs(
    paragraphs: List[Paragraph],
    short_threshold: int = 30,
    long_threshold: int = 150,
    min_words: int = 5,
) -> Dict:
    """
    Analyze paragraph lengths and identify potential issues.

    Returns:
        Dict with analysis results:
            - short: Paragraphs below short_threshold
            - long: Paragraphs above long_threshold
            - stats: Distribution statistics
            - by_file: Counts per file
    """
    short_paragraphs: List[ParagraphAnalysis] = []
    long_paragraphs: List[ParagraphAnalysis] = []

    for i, para in enumerate(paragraphs):
        # Get context
        context_before = None
        context_after = None

        if i > 0:
            prev = paragraphs[i - 1]
            words = tokenize_regex(prev.cleaned_text)[:15]
            context_before = " ".join(words) + ("..." if len(words) == 15 else "")

        if i < len(paragraphs) - 1:
            next_p = paragraphs[i + 1]
            words = tokenize_regex(next_p.cleaned_text)[:15]
            context_after = " ".join(words) + ("..." if len(words) == 15 else "")

        if para.word_count < short_threshold and para.word_count >= min_words:
            short_paragraphs.append(ParagraphAnalysis(
                paragraph=para,
                context_before=context_before,
                context_after=context_after,
                issue="short",
            ))

        if para.word_count > long_threshold:
            long_paragraphs.append(ParagraphAnalysis(
                paragraph=para,
                context_before=context_before,
                context_after=context_after,
                issue="long",
            ))

    # Compute statistics
    word_counts = [p.word_count for p in paragraphs]
    stats = compute_distribution_stats(word_counts)

    # Per-file breakdown
    by_file: Dict[str, Dict] = {}
    for para in paragraphs:
        if para.source_file not in by_file:
            by_file[para.source_file] = {
                "total": 0, "short": 0, "long": 0, "words": []
            }
        by_file[para.source_file]["total"] += 1
        by_file[para.source_file]["words"].append(para.word_count)

    for analysis in short_paragraphs:
        by_file[analysis.paragraph.source_file]["short"] += 1

    for analysis in long_paragraphs:
        by_file[analysis.paragraph.source_file]["long"] += 1

    return {
        "short": short_paragraphs,
        "long": long_paragraphs,
        "all_paragraphs": paragraphs,
        "stats": stats,
        "by_file": by_file,
    }


def compute_distribution_stats(word_counts: List[int]) -> Dict:
    """Compute distribution statistics for word counts."""
    if not word_counts:
        return {"min": 0, "max": 0, "mean": 0, "median": 0, "total": 0}

    sorted_counts = sorted(word_counts)
    n = len(sorted_counts)

    return {
        "min": sorted_counts[0],
        "max": sorted_counts[-1],
        "mean": sum(sorted_counts) / n,
        "median": sorted_counts[n // 2] if n % 2 else (sorted_counts[n // 2 - 1] + sorted_counts[n // 2]) / 2,
        "total": n,
        "p10": sorted_counts[int(n * 0.1)] if n > 10 else sorted_counts[0],
        "p25": sorted_counts[int(n * 0.25)] if n > 4 else sorted_counts[0],
        "p75": sorted_counts[int(n * 0.75)] if n > 4 else sorted_counts[-1],
        "p90": sorted_counts[int(n * 0.9)] if n > 10 else sorted_counts[-1],
    }


def compute_histogram(word_counts: List[int], bin_size: int = 10) -> Dict[int, int]:
    """Compute histogram of word counts."""
    bins: Dict[int, int] = {}
    for count in word_counts:
        bucket = (count // bin_size) * bin_size
        bins[bucket] = bins.get(bucket, 0) + 1
    return bins


# =============================================================================
# Output Formatters
# =============================================================================

def output_table(
    analysis: Dict,
    mode: str,  # "short", "long", or "all"
    show_context: bool = False,
    show_histogram: bool = True,
):
    """Output analysis as rich tables."""
    stats = analysis["stats"]
    by_file = analysis["by_file"]

    # Summary panel
    total = stats["total"]
    short_count = len(analysis["short"])
    long_count = len(analysis["long"])

    summary = f"[bold]{total}[/bold] paragraphs"
    summary += f" | [yellow]{short_count}[/yellow] short"
    summary += f" | [red]{long_count}[/red] long"
    summary += f" | mean: [cyan]{stats['mean']:.0f}[/cyan] words"
    console.print(Panel(summary, title="[bold blue]Paragraph Analysis[/bold blue]", expand=False))

    # Distribution stats
    stats_table = Table(title="Word Count Distribution", show_header=False)
    stats_table.add_column("Metric", style="cyan")
    stats_table.add_column("Value", style="magenta", justify="right")

    stats_table.add_row("Minimum", str(stats["min"]))
    stats_table.add_row("10th percentile", str(stats.get("p10", "—")))
    stats_table.add_row("25th percentile", str(stats.get("p25", "—")))
    stats_table.add_row("Median", f"{stats['median']:.0f}")
    stats_table.add_row("Mean", f"{stats['mean']:.1f}")
    stats_table.add_row("75th percentile", str(stats.get("p75", "—")))
    stats_table.add_row("90th percentile", str(stats.get("p90", "—")))
    stats_table.add_row("Maximum", str(stats["max"]))

    console.print(stats_table)

    # Histogram
    if show_histogram:
        _output_histogram([p.word_count for p in analysis["all_paragraphs"]])

    # Short paragraphs
    if mode in ("short", "all") and analysis["short"]:
        _output_issue_table(analysis["short"], "Short Paragraphs", show_context)

    # Long paragraphs
    if mode in ("long", "all") and analysis["long"]:
        _output_issue_table(analysis["long"], "Long Paragraphs", show_context)

    # Per-file summary
    _output_file_summary(by_file)


def _output_histogram(word_counts: List[int], bin_size: int = 20):
    """Output histogram of word counts."""
    console.print("\n[bold]Word Count Distribution[/bold]")

    bins = compute_histogram(word_counts, bin_size)
    max_count = max(bins.values()) if bins else 1

    for bucket in sorted(bins.keys()):
        count = bins[bucket]
        bar_len = int((count / max_count) * 30)
        bar = "█" * bar_len

        label = f"{bucket:3d}–{bucket + bin_size - 1:3d}"
        console.print(f"  {label} │ {bar} ({count})")


def _output_issue_table(
    analyses: List[ParagraphAnalysis],
    title: str,
    show_context: bool,
):
    """Output table of problematic paragraphs."""
    table = Table(title=title, show_lines=show_context)
    table.add_column("Location", style="cyan", no_wrap=True)
    table.add_column("Section", style="yellow", max_width=25)
    table.add_column("Words", style="magenta", justify="right")
    table.add_column("Preview", style="dim", max_width=50)

    if show_context:
        table.add_column("Context", style="dim", max_width=40)

    for analysis in analyses[:50]:  # Limit output
        para = analysis.paragraph
        preview = para.cleaned_text[:80] + ("..." if len(para.cleaned_text) > 80 else "")

        # Format as file:line for terminal clickability
        location = f"{para.source_path}:{para.line_start}"

        row = [
            location,
            para.section or "—",
            str(para.word_count),
            preview,
        ]

        if show_context:
            ctx = ""
            if analysis.context_before:
                ctx += f"↑ {analysis.context_before}\n"
            if analysis.context_after:
                ctx += f"↓ {analysis.context_after}"
            row.append(ctx or "—")

        table.add_row(*row)

    if len(analyses) > 50:
        table.add_row("...", f"+{len(analyses) - 50} more", "", "")

    console.print(table)


def _output_file_summary(by_file: Dict[str, Dict]):
    """Output per-file summary."""
    table = Table(title="Per-File Summary")
    table.add_column("File", style="green")
    table.add_column("Total", style="cyan", justify="right")
    table.add_column("Short", style="yellow", justify="right")
    table.add_column("Long", style="red", justify="right")
    table.add_column("Avg Words", style="magenta", justify="right")
    table.add_column("Issue %", style="dim", justify="right")

    for filename in sorted(by_file.keys()):
        data = by_file[filename]
        total = data["total"]
        avg_words = sum(data["words"]) / total if total else 0
        issue_pct = ((data["short"] + data["long"]) / total * 100) if total else 0

        table.add_row(
            filename,
            str(total),
            str(data["short"]) if data["short"] else "—",
            str(data["long"]) if data["long"] else "—",
            f"{avg_words:.0f}",
            f"{issue_pct:.1f}%" if issue_pct > 0 else "—",
        )

    console.print(table)


def output_json(analysis: Dict, mode: str):
    """Output as JSON."""
    paragraphs_to_include = []

    if mode == "short":
        paragraphs_to_include = [
            {
                **a.paragraph.to_dict(),
                "issue": a.issue,
                "context_before": a.context_before,
                "context_after": a.context_after,
            }
            for a in analysis["short"]
        ]
    elif mode == "long":
        paragraphs_to_include = [
            {
                **a.paragraph.to_dict(),
                "issue": a.issue,
                "context_before": a.context_before,
                "context_after": a.context_after,
            }
            for a in analysis["long"]
        ]
    else:  # all
        paragraphs_to_include = [p.to_dict() for p in analysis["all_paragraphs"]]

    data = {
        "summary": {
            "total_paragraphs": analysis["stats"]["total"],
            "short_paragraphs": len(analysis["short"]),
            "long_paragraphs": len(analysis["long"]),
        },
        "stats": analysis["stats"],
        "paragraphs": paragraphs_to_include,
        "by_file": {
            k: {
                "total": v["total"],
                "short": v["short"],
                "long": v["long"],
                "avg_words": sum(v["words"]) / v["total"] if v["total"] else 0,
            }
            for k, v in analysis["by_file"].items()
        },
    }
    print(json.dumps(data, indent=2))


def output_jsonl(analysis: Dict, mode: str):
    """Output as JSON Lines."""
    if mode == "short":
        for a in analysis["short"]:
            data = a.paragraph.to_dict()
            data["issue"] = a.issue
            data["location"] = f"{a.paragraph.source_path}:{a.paragraph.line_start}"
            print(json.dumps(data))
    elif mode == "long":
        for a in analysis["long"]:
            data = a.paragraph.to_dict()
            data["issue"] = a.issue
            data["location"] = f"{a.paragraph.source_path}:{a.paragraph.line_start}"
            print(json.dumps(data))
    else:
        for p in analysis["all_paragraphs"]:
            data = p.to_dict()
            data["location"] = f"{p.source_path}:{p.line_start}"
            print(json.dumps(data))


def output_csv(analysis: Dict, mode: str):
    """Output as CSV."""
    writer = csv.writer(sys.stdout)
    writer.writerow([
        "location", "section", "word_count", "issue", "preview"
    ])

    if mode == "short":
        items = [(a.paragraph, a.issue) for a in analysis["short"]]
    elif mode == "long":
        items = [(a.paragraph, a.issue) for a in analysis["long"]]
    else:
        items = [(p, "") for p in analysis["all_paragraphs"]]

    for para, issue in items:
        location = f"{para.source_path}:{para.line_start}"
        writer.writerow([
            location,
            para.section,
            para.word_count,
            issue,
            para.cleaned_text[:100].replace("\n", " "),
        ])


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
    max_words: int = typer.Option(
        30,
        "--max-words",
        help="Maximum words for 'short' classification",
        min=10,
    ),
    min_words: int = typer.Option(
        5,
        "--min-words",
        help="Minimum words to include (filter noise)",
        min=1,
    ),
    long_threshold: int = typer.Option(
        150,
        "--long-threshold",
        help="Minimum words for 'long' classification",
        min=50,
    ),
    short: bool = typer.Option(
        True,
        "--short/--no-short",
        help="Show short paragraphs",
    ),
    long: bool = typer.Option(
        False,
        "--long",
        help="Show long paragraphs",
    ),
    show_context: bool = typer.Option(
        False,
        "--context", "-c",
        help="Show surrounding paragraph context",
    ),
    no_histogram: bool = typer.Option(
        False,
        "--no-histogram",
        help="Hide histogram (table format only)",
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
    Analyze paragraph structure in LaTeX documents.

    By default, finds short paragraphs (under 30 words) that may indicate
    choppy writing or incomplete thoughts.

    Examples:

        # Find short paragraphs
        tex-paragraphs chapters/07-agents-part-2/

        # Custom short threshold (50 words)
        tex-paragraphs chapters/07-agents-part-2/ --max-words 50

        # Find long paragraphs (over 150 words)
        tex-paragraphs chapters/07-agents-part-2/ --long

        # Show surrounding context
        tex-paragraphs chapters/07-agents-part-2/ --context

        # Output all paragraphs as JSON
        tex-paragraphs chapters/07-agents-part-2/ --no-short -f json > paras.json
    """
    # Determine mode
    if long and not short:
        mode = "long"
    elif short and not long:
        mode = "short"
    else:
        mode = "all"

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

    # Extract paragraphs
    all_paragraphs: List[Paragraph] = []

    if format == "table":
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Extracting paragraphs...", total=len(all_files))

            for file_path in all_files:
                paras = extract_paragraphs_from_tex(file_path, min_words=min_words)
                all_paragraphs.extend(paras)
                progress.advance(task)
    else:
        for file_path in all_files:
            paras = extract_paragraphs_from_tex(file_path, min_words=min_words)
            all_paragraphs.extend(paras)

    if not all_paragraphs:
        console.print("[yellow]Warning:[/yellow] No paragraphs extracted", file=sys.stderr)
        raise typer.Exit(0)

    # Analyze
    analysis = analyze_paragraphs(
        all_paragraphs,
        short_threshold=max_words,
        long_threshold=long_threshold,
        min_words=min_words,
    )

    # Output
    if format == "table":
        output_table(
            analysis,
            mode=mode,
            show_context=show_context,
            show_histogram=not no_histogram,
        )
    elif format == "json":
        output_json(analysis, mode=mode)
    elif format == "jsonl":
        output_jsonl(analysis, mode=mode)
    elif format == "csv":
        output_csv(analysis, mode=mode)
    else:
        console.print(f"[red]Error:[/red] Unknown format: {format}", file=sys.stderr)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
