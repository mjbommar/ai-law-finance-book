#!/usr/bin/env python3
"""Convert a BibTeX file to a markdown checklist for review.

Usage:
    uv run python scripts/bib_to_checklist.py chapters/07-agents-part-2/bib/refs.bib
    uv run python scripts/bib_to_checklist.py chapters/07-agents-part-2/bib/refs.bib -o review.md
"""

import argparse
import re
import sys
from pathlib import Path


def parse_bib_entries(bib_file: Path) -> list[dict]:
    """Parse BibTeX file and extract entry metadata."""
    content = bib_file.read_text(encoding="utf-8")

    entries = []

    # Match each entry: @type{key, ... }
    # We need to handle nested braces properly
    entry_pattern = r'@(\w+)\s*\{\s*([^,]+)\s*,'

    # Find all entry starts
    for match in re.finditer(entry_pattern, content):
        entry_type = match.group(1).lower()
        key = match.group(2).strip()

        # Find the full entry by counting braces
        start = match.start()
        brace_count = 0
        end = start
        in_entry = False

        for i, char in enumerate(content[start:], start):
            if char == '{':
                brace_count += 1
                in_entry = True
            elif char == '}':
                brace_count -= 1
                if in_entry and brace_count == 0:
                    end = i + 1
                    break

        entry_text = content[start:end]

        # Extract fields
        entry = {
            'key': key,
            'type': entry_type,
            'title': extract_field(entry_text, 'title'),
            'author': extract_field(entry_text, 'author'),
            'year': extract_field(entry_text, 'year'),
            'url': extract_field(entry_text, 'url'),
            'note': extract_field(entry_text, 'note'),
        }
        entries.append(entry)

    return entries


def extract_field(entry_text: str, field: str) -> str | None:
    """Extract a field value from a BibTeX entry."""
    # Match field = {value} or field = "value" or field = value
    patterns = [
        rf'{field}\s*=\s*\{{([^}}]*(?:\{{[^}}]*\}}[^}}]*)*)\}}',  # field = {value with {nested}}
        rf'{field}\s*=\s*"([^"]*)"',  # field = "value"
        rf'{field}\s*=\s*(\w+)',  # field = value (for months, etc.)
    ]

    for pattern in patterns:
        match = re.search(pattern, entry_text, re.IGNORECASE | re.DOTALL)
        if match:
            value = match.group(1).strip()
            # Clean up LaTeX commands
            value = re.sub(r'\{([^}]*)\}', r'\1', value)  # Remove braces
            value = re.sub(r'\\[a-zA-Z]+\s*', '', value)  # Remove commands
            value = re.sub(r'\s+', ' ', value)  # Normalize whitespace
            return value.strip()

    return None


def clean_author(author: str | None) -> str:
    """Clean and abbreviate author string."""
    if not author:
        return "Unknown"

    # Handle corporate authors
    if author.startswith('{') or 'Foundation' in author or 'Association' in author:
        return author.replace('{', '').replace('}', '').strip()

    # Split by 'and' and take first author + et al.
    authors = re.split(r'\s+and\s+', author)
    if len(authors) > 2:
        first = authors[0].split(',')[0].strip()  # Last name of first author
        return f"{first} et al."
    elif len(authors) == 2:
        first = authors[0].split(',')[0].strip()
        second = authors[1].split(',')[0].strip()
        return f"{first} & {second}"
    else:
        return authors[0].split(',')[0].strip()


def clean_title(title: str | None, max_len: int = 60) -> str:
    """Clean and truncate title."""
    if not title:
        return "Untitled"

    # Remove LaTeX formatting
    title = re.sub(r'\{|\}', '', title)
    title = re.sub(r'\\textit|\\textbf|\\emph', '', title)

    if len(title) > max_len:
        return title[:max_len-3].rsplit(' ', 1)[0] + "..."
    return title


def generate_checklist(entries: list[dict], checked_keys: set[str] = None) -> str:
    """Generate markdown checklist from entries."""
    if checked_keys is None:
        checked_keys = set()

    lines = [
        "# Citation Review Checklist",
        "",
        f"Total citations: {len(entries)}",
        f"Reviewed: {len(checked_keys)}/{len(entries)}",
        "",
        "---",
        "",
    ]

    # Group by type
    by_type: dict[str, list[dict]] = {}
    for entry in entries:
        t = entry['type']
        if t not in by_type:
            by_type[t] = []
        by_type[t].append(entry)

    # Sort types by count (descending)
    sorted_types = sorted(by_type.keys(), key=lambda t: -len(by_type[t]))

    for entry_type in sorted_types:
        type_entries = by_type[entry_type]
        lines.append(f"## {entry_type.capitalize()} ({len(type_entries)})")
        lines.append("")

        # Sort entries by year (descending), then by key
        type_entries.sort(key=lambda e: (-(int(e['year']) if e['year'] and e['year'].isdigit() else 0), e['key']))

        for entry in type_entries:
            check = "x" if entry['key'] in checked_keys else " "
            author = clean_author(entry['author'])
            year = entry['year'] or "n.d."
            title = clean_title(entry['title'])

            line = f"- [{check}] **{entry['key']}**: {author} ({year}). {title}"

            if entry['url']:
                # Truncate long URLs
                url = entry['url']
                if len(url) > 50:
                    display_url = url[:47] + "..."
                else:
                    display_url = url
                line += f" [link]({url})"

            lines.append(line)

        lines.append("")

    return "\n".join(lines)


def load_existing_checklist(checklist_file: Path) -> set[str]:
    """Load checked items from existing checklist."""
    if not checklist_file.exists():
        return set()

    content = checklist_file.read_text(encoding="utf-8")
    checked = set()

    # Match - [x] **key**: ...
    for match in re.finditer(r'- \[x\] \*\*([^*]+)\*\*:', content):
        checked.add(match.group(1))

    return checked


def main():
    parser = argparse.ArgumentParser(
        description="Convert BibTeX file to markdown review checklist"
    )
    parser.add_argument(
        "bib_file",
        type=Path,
        help="Path to .bib file",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output markdown file (default: stdout)",
    )
    parser.add_argument(
        "--preserve-checks",
        action="store_true",
        help="Preserve [x] marks from existing output file",
    )

    args = parser.parse_args()

    if not args.bib_file.exists():
        print(f"Error: {args.bib_file} not found", file=sys.stderr)
        sys.exit(1)

    entries = parse_bib_entries(args.bib_file)

    if not entries:
        print("No entries found in bib file", file=sys.stderr)
        sys.exit(1)

    # Load existing checks if preserving
    checked_keys = set()
    if args.preserve_checks and args.output and args.output.exists():
        checked_keys = load_existing_checklist(args.output)
        print(f"Preserved {len(checked_keys)} checked items", file=sys.stderr)

    checklist = generate_checklist(entries, checked_keys)

    if args.output:
        args.output.write_text(checklist, encoding="utf-8")
        print(f"Wrote checklist to {args.output}", file=sys.stderr)
    else:
        print(checklist)


if __name__ == "__main__":
    main()
