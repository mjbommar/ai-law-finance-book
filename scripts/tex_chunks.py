#!/usr/bin/env python3
"""
tex_chunks.py — Create and analyze sliding-window chunks from LaTeX documents.

This tool extracts prose paragraphs from LaTeX files and creates overlapping
chunks for context-aware analysis. Useful for:

    - Feeding context windows to LLMs for review
    - Detecting repetition patterns across adjacent paragraphs
    - Analyzing narrative flow and transitions
    - Creating training data with proper context

Output Formats:
    - table: Rich formatted table (default, human-readable)
    - json:  Single JSON object with all data
    - jsonl: One JSON object per chunk (streaming-friendly)
    - csv:   Comma-separated values

Usage:
    # Analyze a chapter directory
    uv run --with rich,typer scripts/tex_chunks.py chapters/07-agents-part-2/

    # Output as JSONL for processing
    uv run --with rich,typer scripts/tex_chunks.py chapters/07-agents-part-2/ -f jsonl > chunks.jsonl

    # Custom window size and overlap
    uv run --with rich,typer scripts/tex_chunks.py chapters/07-agents-part-2/ -w 5 -o 2

    # Analyze specific files
    uv run --with rich,typer scripts/tex_chunks.py chapter.tex sections/*.tex

Dependencies:
    pip install rich typer
    — or —
    uv run --with rich,typer scripts/tex_chunks.py ...
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
from pathlib import Path
from typing import List, Optional

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
        Chunk,
        extract_paragraphs_from_tex,
        create_chunks,
        find_tex_files,
        find_section_files,
        clean_latex_text,
        tokenize_regex,
        STOPWORDS,
    )
except ImportError:
    # Handle running from different directories
    script_dir = Path(__file__).parent
    sys.path.insert(0, str(script_dir))
    from tex_utils import (
        Paragraph,
        Chunk,
        extract_paragraphs_from_tex,
        create_chunks,
        find_tex_files,
        find_section_files,
        clean_latex_text,
        tokenize_regex,
        STOPWORDS,
    )


# =============================================================================
# CLI Application
# =============================================================================

app = typer.Typer(
    name="tex-chunks",
    help="Create and analyze sliding-window chunks from LaTeX documents.",
    add_completion=False,
    rich_markup_mode="rich",
)

console = Console()


# =============================================================================
# Output Formatters
# =============================================================================

def output_table(chunks: List[Chunk], paragraphs: List[Paragraph], show_text: bool = False):
    """Output chunks as a rich table."""
    # Summary panel
    total_words = sum(p.word_count for p in paragraphs)
    summary = f"[bold]{len(paragraphs)}[/bold] paragraphs → [bold]{len(chunks)}[/bold] chunks"
    summary += f" | [dim]{total_words:,} total words[/dim]"
    console.print(Panel(summary, title="[bold blue]Chunk Analysis[/bold blue]", expand=False))

    # Chunks table
    table = Table(title="Chunks", show_lines=show_text)
    table.add_column("ID", style="cyan", width=4)
    table.add_column("Location", style="green", no_wrap=True)
    table.add_column("Sections", style="yellow")
    table.add_column("Words", style="magenta", justify="right")
    if show_text:
        table.add_column("Preview", style="white", max_width=60)

    for chunk in chunks:
        # Format as file:line for terminal clickability
        first_para = chunk.paragraphs[0]
        location = f"{first_para.source_path}:{first_para.line_start}"
        sections = ", ".join(chunk.sections) or "—"
        preview = chunk.text[:100].replace("\n", " ") + "..." if show_text else ""

        row = [str(chunk.chunk_id), location, sections, str(chunk.total_words)]
        if show_text:
            row.append(preview)
        table.add_row(*row)

    console.print(table)


def output_json(chunks: List[Chunk], paragraphs: List[Paragraph]):
    """Output as a single JSON object."""
    data = {
        "summary": {
            "total_paragraphs": len(paragraphs),
            "total_chunks": len(chunks),
            "total_words": sum(p.word_count for p in paragraphs),
            "files": list(set(p.source_file for p in paragraphs)),
        },
        "chunks": [c.to_dict() for c in chunks],
    }
    print(json.dumps(data, indent=2))


def output_jsonl(chunks: List[Chunk], paragraphs: List[Paragraph]):
    """Output as JSON Lines (one object per line)."""
    for chunk in chunks:
        print(json.dumps(chunk.to_dict()))


def output_csv(chunks: List[Chunk], paragraphs: List[Paragraph]):
    """Output as CSV."""
    writer = csv.writer(sys.stdout)
    writer.writerow([
        "chunk_id", "location", "sections", "total_words", "text"
    ])
    for chunk in chunks:
        first_para = chunk.paragraphs[0]
        location = f"{first_para.source_path}:{first_para.line_start}"
        writer.writerow([
            chunk.chunk_id,
            location,
            "|".join(chunk.sections),
            chunk.total_words,
            chunk.text.replace("\n", "\\n"),
        ])


# =============================================================================
# Repetition Analysis
# =============================================================================

def analyze_repetition(paragraphs: List[Paragraph], patterns: Optional[dict] = None) -> dict:
    """
    Analyze repetition patterns across paragraphs.

    Args:
        paragraphs: List of paragraphs to analyze.
        patterns: Optional dict of pattern_name -> regex pattern.

    Returns:
        Dict mapping pattern names to lists of occurrences.
    """
    if patterns is None:
        patterns = {
            "framework": r"\bframework\b",
            "three pillars": r"three\s+pillars",
            "tools, memory, planning": r"tools?,?\s*(and\s+)?memory,?\s*(and\s+)?planning",
        }

    results = {name: [] for name in patterns}

    for para in paragraphs:
        for name, pattern in patterns.items():
            if re.search(pattern, para.cleaned_text, re.IGNORECASE):
                results[name].append({
                    "file": para.source_file,
                    "section": para.section,
                    "line": para.line_start,
                    "preview": para.cleaned_text[:80],
                })

    return results


def output_repetition_table(repetition: dict):
    """Output repetition analysis as a rich table."""
    console.print("\n")
    console.print(Panel("[bold]Repetition Analysis[/bold]", expand=False))

    for pattern_name, occurrences in repetition.items():
        if not occurrences:
            continue

        table = Table(title=f'"{pattern_name}" ({len(occurrences)} occurrences)')
        table.add_column("File", style="green")
        table.add_column("Section", style="yellow")
        table.add_column("Line", style="cyan", justify="right")
        table.add_column("Preview", style="dim", max_width=50)

        for occ in occurrences[:10]:  # Limit to first 10
            table.add_row(
                occ["file"],
                occ["section"] or "—",
                str(occ["line"]),
                occ["preview"] + "...",
            )

        if len(occurrences) > 10:
            table.add_row("...", f"+{len(occurrences) - 10} more", "", "")

        console.print(table)


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
    window: int = typer.Option(
        3,
        "--window", "-w",
        help="Number of paragraphs per chunk",
        min=1,
        max=20,
    ),
    overlap: int = typer.Option(
        1,
        "--overlap", "-o",
        help="Number of paragraphs overlapping between chunks",
        min=0,
    ),
    min_words: int = typer.Option(
        10,
        "--min-words", "-m",
        help="Minimum words for a paragraph to be included",
        min=1,
    ),
    show_text: bool = typer.Option(
        False,
        "--show-text", "-t",
        help="Show text preview in table output",
    ),
    analyze_patterns: bool = typer.Option(
        False,
        "--analyze", "-a",
        help="Run repetition pattern analysis",
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
    Create sliding-window chunks from LaTeX documents.

    Extracts prose paragraphs (excluding figures, tables, boxes) and creates
    overlapping chunks for context-aware analysis.

    Examples:

        # Analyze a chapter
        tex-chunks chapters/07-agents-part-2/

        # Output as JSONL for LLM processing
        tex-chunks chapters/07-agents-part-2/ -f jsonl > chunks.jsonl

        # Custom window: 5 paragraphs with 2 overlap
        tex-chunks chapters/07-agents-part-2/ -w 5 -o 2

        # Include repetition analysis
        tex-chunks chapters/07-agents-part-2/ -a
    """
    # Validate overlap
    if overlap >= window:
        console.print("[red]Error:[/red] Overlap must be less than window size", file=sys.stderr)
        raise typer.Exit(1)

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
        # Silent extraction for data formats
        for file_path in all_files:
            paras = extract_paragraphs_from_tex(file_path, min_words=min_words)
            all_paragraphs.extend(paras)

    if not all_paragraphs:
        console.print("[yellow]Warning:[/yellow] No paragraphs extracted", file=sys.stderr)
        raise typer.Exit(0)

    # Create chunks
    chunks = create_chunks(all_paragraphs, window_size=window, overlap=overlap)

    # Output
    if format == "table":
        output_table(chunks, all_paragraphs, show_text=show_text)
        if analyze_patterns:
            repetition = analyze_repetition(all_paragraphs)
            output_repetition_table(repetition)
    elif format == "json":
        output_json(chunks, all_paragraphs)
    elif format == "jsonl":
        output_jsonl(chunks, all_paragraphs)
    elif format == "csv":
        output_csv(chunks, all_paragraphs)
    else:
        console.print(f"[red]Error:[/red] Unknown format: {format}", file=sys.stderr)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
