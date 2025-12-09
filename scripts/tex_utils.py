#!/usr/bin/env python3
"""
tex_utils.py — Shared utilities for LaTeX text analysis tools.

This module provides common functionality for parsing, cleaning, and analyzing
LaTeX documents. It's designed for textbook authoring workflows where you need
to analyze prose quality, repetition, and structure.

Features:
    - LaTeX-aware paragraph extraction (skips figures, tables, boxes)
    - Configurable environment exclusion
    - Clean text extraction preserving semantic content
    - Tokenization (simple and regex-based)
    - N-gram generation

Usage:
    This module is imported by the tex-* CLI tools. You generally don't run it directly.

    >>> from tex_utils import extract_paragraphs_from_tex, clean_latex_text
    >>> paragraphs = extract_paragraphs_from_tex("chapter.tex")
    >>> clean_text = clean_latex_text(raw_latex)

Dependencies:
    None (stdlib only) — this module has no external dependencies.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterator, List, Optional, Tuple


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class Paragraph:
    """
    A paragraph of prose text extracted from a LaTeX file.

    Attributes:
        text: The raw LaTeX text of the paragraph.
        cleaned_text: The text with LaTeX commands stripped (computed lazily).
        source_file: Basename of the source file.
        source_path: Full path to the source file.
        line_start: Starting line number (1-indexed).
        line_end: Ending line number (1-indexed).
        section: Current section heading when this paragraph appears.
        word_count: Approximate word count of cleaned text.
    """
    text: str
    source_file: str
    source_path: str
    line_start: int
    line_end: int
    section: str = ""
    cleaned_text: str = ""
    word_count: int = 0

    def __post_init__(self):
        """Compute derived fields after initialization."""
        if not self.cleaned_text:
            self.cleaned_text = clean_latex_text(self.text)
        if self.word_count == 0:
            self.word_count = len(tokenize_regex(self.cleaned_text))

    @property
    def location(self) -> str:
        """Return file:line format for terminal/editor clickability.

        Uses relative path from current directory when possible for readability.
        """
        try:
            rel_path = os.path.relpath(self.source_path)
            # Use relative path if it's shorter or doesn't go up too many directories
            if not rel_path.startswith("../../../") and len(rel_path) < len(self.source_path):
                return f"{rel_path}:{self.line_start}"
        except ValueError:
            pass  # On Windows, relpath can fail across drives
        return f"{self.source_path}:{self.line_start}"

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        d = asdict(self)
        d["location"] = self.location
        return d


@dataclass
class Chunk:
    """
    A sliding window of consecutive paragraphs for context-aware analysis.

    Attributes:
        paragraphs: List of Paragraph objects in this chunk.
        chunk_id: Sequential identifier for this chunk.
    """
    paragraphs: List[Paragraph]
    chunk_id: int

    @property
    def text(self) -> str:
        """Combined text of all paragraphs."""
        return "\n\n".join(p.cleaned_text for p in self.paragraphs)

    @property
    def source_files(self) -> List[str]:
        """Unique source files represented in this chunk."""
        return list(dict.fromkeys(p.source_file for p in self.paragraphs))

    @property
    def sections(self) -> List[str]:
        """Unique sections represented in this chunk."""
        return list(dict.fromkeys(p.section for p in self.paragraphs if p.section))

    @property
    def total_words(self) -> int:
        """Total word count across all paragraphs."""
        return sum(p.word_count for p in self.paragraphs)

    @property
    def location(self) -> str:
        """Return file:line format for the first paragraph."""
        if self.paragraphs:
            return self.paragraphs[0].location
        return ""

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "chunk_id": self.chunk_id,
            "location": self.location,
            "source_files": self.source_files,
            "sections": self.sections,
            "total_words": self.total_words,
            "text": self.text,
            "paragraphs": [p.to_dict() for p in self.paragraphs],
        }


# =============================================================================
# LaTeX Environments to Exclude
# =============================================================================

# Default environments to skip when extracting prose paragraphs
DEFAULT_EXCLUDED_ENVIRONMENTS = frozenset({
    # Floats
    "figure", "figure*", "table", "table*",
    # Graphics
    "tikzpicture", "pgfpicture",
    # Custom boxes (common in textbooks)
    "definitionbox", "highlightbox", "keybox", "questionbox",
    "theorembox", "cautionbox", "notebox", "practicebox", "examplebox",
    # Tables
    "tabular", "tabularx", "longtable", "tabulary",
    # Lists (often fragment prose analysis)
    "itemize", "enumerate", "description", "evallist",
    # Code
    "lstlisting", "verbatim", "minted",
    # Math (block-level)
    "equation", "equation*", "align", "align*", "gather", "gather*",
    "multline", "multline*", "split",
    # Other
    "abstract", "quote", "quotation",
})


# =============================================================================
# LaTeX Text Cleaning
# =============================================================================

def clean_latex_text(text: str, preserve_structure: bool = False) -> str:
    """
    Remove LaTeX commands from text, preserving readable content.

    This function strips LaTeX markup while keeping the semantic text content.
    It's designed to produce text suitable for word counting, readability
    analysis, and frequency analysis.

    Args:
        text: Raw LaTeX text.
        preserve_structure: If True, keep paragraph breaks as newlines.

    Returns:
        Cleaned text with LaTeX commands removed.

    Example:
        >>> clean_latex_text(r"This is \\textbf{important} text.")
        'This is important text.'
    """
    # Remove comments (but not escaped percent signs)
    text = re.sub(r'(?<!\\)%.*$', '', text, flags=re.MULTILINE)

    # Commands that extract their argument content
    content_commands = [
        r'\\textbf', r'\\textit', r'\\emph', r'\\keyterm',
        r'\\texttt', r'\\textsf', r'\\textsc', r'\\textrm',
        r'\\underline', r'\\uline',
    ]
    for cmd in content_commands:
        text = re.sub(rf'{cmd}\{{([^}}]+)\}}', r'\1', text)

    # Commands that should be removed entirely (citations, refs)
    remove_commands = [
        r'\\parencite(?:\[[^\]]*\])?\{[^}]+\}',
        r'\\textcite(?:\[[^\]]*\])?\{[^}]+\}',
        r'\\cite(?:\[[^\]]*\])?\{[^}]+\}',
        r'\\autocite(?:\[[^\]]*\])?\{[^}]+\}',
        r'\\footcite(?:\[[^\]]*\])?\{[^}]+\}',
        r'\\Cref\{[^}]+\}',
        r'\\cref\{[^}]+\}',
        r'\\ref\{[^}]+\}',
        r'\\eqref\{[^}]+\}',
        r'\\pageref\{[^}]+\}',
        r'\\label\{[^}]+\}',
        r'\\index\{[^}]+\}',
    ]
    for pattern in remove_commands:
        text = re.sub(pattern, '', text)

    # Section-like refs (replace with placeholder to avoid word-joining)
    text = re.sub(r'Section~\\ref\{[^}]+\}', 'Section X', text)
    text = re.sub(r'Figure~\\ref\{[^}]+\}', 'Figure X', text)
    text = re.sub(r'Table~\\ref\{[^}]+\}', 'Table X', text)
    text = re.sub(r'Chapter~\\ref\{[^}]+\}', 'Chapter X', text)

    # Environment delimiters
    text = re.sub(r'\\begin\{[^}]+\}(?:\[[^\]]*\])?(?:\{[^}]*\})?', '', text)
    text = re.sub(r'\\end\{[^}]+\}', '', text)

    # Generic commands with braced arguments (greedy but imperfect)
    text = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?\{[^}]*\}', '', text)

    # Remaining commands without arguments
    text = re.sub(r'\\[a-zA-Z]+\*?', '', text)

    # Special characters and spacing
    text = re.sub(r'~', ' ', text)  # Non-breaking space
    text = re.sub(r'---', ' — ', text)  # Em dash
    text = re.sub(r'--', ' – ', text)  # En dash
    text = re.sub(r'``|\'\'', '"', text)  # Quotes
    text = re.sub(r'\$[^$]+\$', '', text)  # Inline math
    text = re.sub(r'[{}\\]', '', text)  # Remaining braces and backslashes

    # Normalize whitespace
    if preserve_structure:
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
    else:
        text = re.sub(r'\s+', ' ', text)

    return text.strip()


# =============================================================================
# Tokenization
# =============================================================================

def tokenize_simple(text: str) -> List[str]:
    """
    Simple whitespace-based tokenization.

    Args:
        text: Input text.

    Returns:
        List of whitespace-delimited tokens.
    """
    return text.split()


def tokenize_regex(text: str) -> List[str]:
    """
    Regex-based tokenization that handles punctuation properly.

    Extracts word-like tokens, handling contractions and hyphenated words.

    Args:
        text: Input text.

    Returns:
        List of word tokens.

    Example:
        >>> tokenize_regex("It's a well-known fact.")
        ["It's", 'a', 'well-known', 'fact']
    """
    # Match words with optional internal apostrophes/hyphens
    return re.findall(r"\b[a-zA-Z][a-zA-Z'\-]*[a-zA-Z]\b|\b[a-zA-Z]\b", text)


def get_ngrams(tokens: List[str], n: int) -> List[Tuple[str, ...]]:
    """
    Generate n-grams from a token list.

    Args:
        tokens: List of tokens.
        n: Size of n-gram (2 for bigrams, 3 for trigrams, etc.).

    Returns:
        List of n-gram tuples.

    Example:
        >>> get_ngrams(['the', 'quick', 'brown', 'fox'], 2)
        [('the', 'quick'), ('quick', 'brown'), ('brown', 'fox')]
    """
    if len(tokens) < n:
        return []
    return [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]


# =============================================================================
# Paragraph Extraction
# =============================================================================

def extract_paragraphs_from_tex(
    file_path: str | Path,
    excluded_envs: Optional[frozenset[str]] = None,
    min_words: int = 10,
) -> List[Paragraph]:
    """
    Extract prose paragraphs from a LaTeX file.

    This function parses a LaTeX file and extracts contiguous blocks of prose
    text, excluding structural elements like figures, tables, and custom boxes.
    It's designed to isolate the narrative content for quality analysis.

    Args:
        file_path: Path to the LaTeX file.
        excluded_envs: Set of environment names to skip. Defaults to
            DEFAULT_EXCLUDED_ENVIRONMENTS.
        min_words: Minimum word count to include a paragraph.

    Returns:
        List of Paragraph objects, ordered by appearance in the file.

    Example:
        >>> paragraphs = extract_paragraphs_from_tex("chapter.tex")
        >>> print(f"Found {len(paragraphs)} paragraphs")
    """
    file_path = Path(file_path)
    excluded_envs = excluded_envs or DEFAULT_EXCLUDED_ENVIRONMENTS

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    paragraphs: List[Paragraph] = []
    current_para_lines: List[str] = []
    current_start_line = 0
    current_section = ""
    env_depth = 0  # Track nested excluded environments

    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()

        # Track section headings
        section_match = re.match(r'\\(sub)*section\*?\{([^}]+)\}', stripped)
        if section_match:
            current_section = section_match.group(2)

        # Track environment nesting
        begin_match = re.match(r'\\begin\{(\w+\*?)\}', stripped)
        end_match = re.match(r'\\end\{(\w+\*?)\}', stripped)

        if begin_match and begin_match.group(1) in excluded_envs:
            # Save current paragraph before entering excluded environment
            if current_para_lines:
                _save_paragraph(
                    paragraphs, current_para_lines, file_path,
                    current_start_line, line_num - 1, current_section, min_words
                )
                current_para_lines = []
            env_depth += 1
            continue

        if end_match and end_match.group(1) in excluded_envs:
            env_depth = max(0, env_depth - 1)
            continue

        # Skip content inside excluded environments
        if env_depth > 0:
            continue

        # Detect structural/non-prose lines
        is_structural = (
            stripped.startswith('%') or
            stripped.startswith('\\begin{') or
            stripped.startswith('\\end{') or
            stripped.startswith('\\input{') or
            stripped.startswith('\\include{') or
            stripped.startswith('\\label{') or
            stripped.startswith('\\pagebreak') or
            stripped.startswith('\\newpage') or
            stripped.startswith('\\clearpage') or
            stripped.startswith('\\vspace') or
            stripped.startswith('\\hspace') or
            stripped.startswith('\\noindent') or
            stripped.startswith('\\addcontentsline') or
            re.match(r'^\\(sub)*section', stripped) or
            re.match(r'^\\chapter', stripped) or
            re.match(r'^\\part', stripped) or
            stripped.startswith('% ===') or
            stripped.startswith('% ---') or
            stripped == ''
        )

        # \paragraph{} starts a new logical paragraph
        para_match = re.match(r'^\\paragraph\{([^}]+)\}(.*)$', stripped)

        if is_structural or para_match:
            # Save accumulated paragraph
            if current_para_lines:
                _save_paragraph(
                    paragraphs, current_para_lines, file_path,
                    current_start_line, line_num - 1, current_section, min_words
                )
                current_para_lines = []

            # Handle \paragraph{} content on same line
            if para_match:
                remaining = para_match.group(2).strip()
                if remaining:
                    current_start_line = line_num
                    current_para_lines = [remaining]
            continue

        # Accumulate prose lines
        if not current_para_lines:
            current_start_line = line_num
        current_para_lines.append(stripped)

    # Don't forget final paragraph
    if current_para_lines:
        _save_paragraph(
            paragraphs, current_para_lines, file_path,
            current_start_line, len(lines), current_section, min_words
        )

    return paragraphs


def _save_paragraph(
    paragraphs: List[Paragraph],
    lines: List[str],
    file_path: Path,
    start_line: int,
    end_line: int,
    section: str,
    min_words: int,
) -> None:
    """Helper to create and save a Paragraph if it meets criteria."""
    text = " ".join(lines)
    cleaned = clean_latex_text(text)
    word_count = len(tokenize_regex(cleaned))

    if word_count >= min_words:
        paragraphs.append(Paragraph(
            text=text,
            source_file=file_path.name,
            source_path=str(file_path),
            line_start=start_line,
            line_end=end_line,
            section=section,
            cleaned_text=cleaned,
            word_count=word_count,
        ))


# =============================================================================
# Chunk Creation
# =============================================================================

def create_chunks(
    paragraphs: List[Paragraph],
    window_size: int = 3,
    overlap: int = 1,
) -> List[Chunk]:
    """
    Create sliding window chunks from paragraphs.

    Chunks provide context for analysis that benefits from seeing multiple
    consecutive paragraphs together (e.g., detecting repetition across
    adjacent paragraphs, analyzing flow and transitions).

    Args:
        paragraphs: List of Paragraph objects.
        window_size: Number of paragraphs per chunk.
        overlap: Number of paragraphs shared between consecutive chunks.

    Returns:
        List of Chunk objects.

    Example:
        >>> paragraphs = extract_paragraphs_from_tex("chapter.tex")
        >>> chunks = create_chunks(paragraphs, window_size=3, overlap=1)
    """
    if len(paragraphs) < window_size:
        if paragraphs:
            return [Chunk(paragraphs=paragraphs, chunk_id=0)]
        return []

    chunks: List[Chunk] = []
    step = window_size - overlap

    for i in range(0, len(paragraphs) - window_size + 1, step):
        chunk_paras = paragraphs[i:i + window_size]
        chunks.append(Chunk(paragraphs=chunk_paras, chunk_id=len(chunks)))

    # Ensure we capture trailing paragraphs not in last chunk
    last_chunk_end = ((len(paragraphs) - window_size) // step) * step + window_size
    if last_chunk_end < len(paragraphs):
        remaining = paragraphs[-window_size:]
        if not chunks or remaining != chunks[-1].paragraphs:
            chunks.append(Chunk(paragraphs=remaining, chunk_id=len(chunks)))

    return chunks


# =============================================================================
# File Discovery
# =============================================================================

def find_tex_files(
    path: str | Path,
    pattern: str = "*.tex",
    recursive: bool = True,
) -> List[Path]:
    """
    Find LaTeX files in a directory.

    Args:
        path: Directory to search, or a single file.
        pattern: Glob pattern for matching files.
        recursive: Whether to search subdirectories.

    Returns:
        Sorted list of Path objects.
    """
    path = Path(path)

    if path.is_file():
        return [path] if path.suffix == ".tex" else []

    if recursive:
        files = list(path.rglob(pattern))
    else:
        files = list(path.glob(pattern))

    # Sort by path for consistent ordering
    return sorted(files)


def find_section_files(chapter_dir: str | Path) -> List[Path]:
    """
    Find section files in a chapter's sections/ subdirectory.

    This follows the book's convention of chapters having a sections/
    subdirectory with numbered section files.

    Args:
        chapter_dir: Path to chapter directory.

    Returns:
        Sorted list of section file paths.
    """
    chapter_dir = Path(chapter_dir)
    sections_dir = chapter_dir / "sections"

    if sections_dir.is_dir():
        return sorted(sections_dir.glob("*.tex"))

    # Fallback: look for .tex files in chapter dir itself
    return sorted(chapter_dir.glob("*.tex"))


# =============================================================================
# Stopwords
# =============================================================================

STOPWORDS = frozenset({
    # Articles, prepositions, conjunctions
    'a', 'an', 'the', 'and', 'or', 'but', 'if', 'then', 'else', 'when',
    'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
    'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
    'further', 'once', 'of', 'as', 'until', 'while', 'than',
    # Pronouns
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself',
    'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them',
    'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
    'that', 'these', 'those',
    # Common verbs
    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
    'had', 'having', 'do', 'does', 'did', 'doing', 'would', 'should', 'could',
    'ought', 'might', 'must', 'shall', 'will', 'can', 'may',
    # Other common
    'no', 'not', 'only', 'own', 'same', 'so', 'just', 'now', 'here', 'there',
    'where', 'why', 'how', 'all', 'each', 'few', 'more', 'most', 'other',
    'some', 'such', 'any', 'both', 'nor', 'too', 'very',
    # Contractions fragments
    's', 't', 'd', 'm', 'o', 're', 've', 'll', 'don', 'didn', 'doesn',
    'hadn', 'hasn', 'haven', 'isn', 'wasn', 'weren', 'won', 'wouldn',
    # LaTeX artifacts
    'ref', 'sec', 'fig', 'e', 'g', 'etc', 'ie', 'eg', 'vs', 'p',
})


def filter_stopwords(tokens: List[str]) -> List[str]:
    """Remove stopwords from token list."""
    return [t for t in tokens if t.lower() not in STOPWORDS]


def filter_stopword_ngrams(ngrams: List[Tuple[str, ...]], min_content: int = 1) -> List[Tuple[str, ...]]:
    """
    Filter n-grams that are mostly stopwords.

    Args:
        ngrams: List of n-gram tuples.
        min_content: Minimum number of non-stopword tokens required.

    Returns:
        Filtered list of n-grams.
    """
    return [
        ng for ng in ngrams
        if sum(1 for w in ng if w.lower() not in STOPWORDS) >= min_content
    ]
