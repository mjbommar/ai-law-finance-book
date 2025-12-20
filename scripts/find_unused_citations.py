#!/usr/bin/env python3
"""Find unused citations in a LaTeX project.

Compares citation keys defined in .bib files against actual usage in .tex files.

Usage:
    uv run python scripts/find_unused_citations.py chapters/07-agents-part-2/
    uv run python scripts/find_unused_citations.py .  # entire project
"""

import argparse
import re
import sys
from pathlib import Path


def extract_bib_keys(bib_file: Path) -> set[str]:
    """Extract all citation keys from a .bib file."""
    content = bib_file.read_text(encoding="utf-8")
    # Match @type{key, where type is article, book, online, etc.
    pattern = r"@\w+\s*\{\s*([^,\s]+)\s*,"
    keys = set(re.findall(pattern, content, re.IGNORECASE))
    return keys


def extract_tex_citations(tex_file: Path) -> set[str]:
    """Extract all citation keys used in a .tex file."""
    content = tex_file.read_text(encoding="utf-8")

    # BibLaTeX citation commands
    # \cite{key}, \parencite{key}, \textcite{key}, \citeauthor{key}, \citeyear{key}
    # \cite[pre][post]{key}, \parencite[pre][post]{key}, etc.
    # Multiple keys: \cite{key1, key2, key3}

    citation_commands = [
        r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\parencite(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\textcite(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\citeauthor(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\citeyear(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\citetitle(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\fullcite(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\autocite(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\footcite(?:\[[^\]]*\])*\{([^}]+)\}",
        r"\\nocite\{([^}]+)\}",
    ]

    keys = set()
    for pattern in citation_commands:
        matches = re.findall(pattern, content)
        for match in matches:
            # Handle multiple keys like {key1, key2, key3}
            for key in match.split(","):
                key = key.strip()
                if key and key != "*":  # \nocite{*} is special
                    keys.add(key)

    return keys


def find_files(directory: Path, pattern: str) -> list[Path]:
    """Find all files matching pattern in directory."""
    return list(directory.rglob(pattern))


def main():
    parser = argparse.ArgumentParser(
        description="Find unused citations in a LaTeX project"
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="Directory to scan (chapter or project root)",
    )
    parser.add_argument(
        "--bib",
        type=Path,
        help="Specific .bib file to check (default: find all .bib files)",
    )
    parser.add_argument(
        "--show-used",
        action="store_true",
        help="Also show which citations are used",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )

    args = parser.parse_args()

    if not args.directory.exists():
        print(f"Error: Directory {args.directory} does not exist", file=sys.stderr)
        sys.exit(1)

    # Find bib files
    if args.bib:
        bib_files = [args.bib]
    else:
        bib_files = find_files(args.directory, "*.bib")

    if not bib_files:
        print("No .bib files found", file=sys.stderr)
        sys.exit(1)

    # Find tex files
    tex_files = find_files(args.directory, "*.tex")
    if not tex_files:
        print("No .tex files found", file=sys.stderr)
        sys.exit(1)

    # Extract all defined keys
    all_defined = {}
    for bib_file in bib_files:
        keys = extract_bib_keys(bib_file)
        for key in keys:
            all_defined[key] = bib_file

    # Extract all used keys
    all_used = set()
    usage_map = {}  # key -> list of files using it
    for tex_file in tex_files:
        keys = extract_tex_citations(tex_file)
        all_used.update(keys)
        for key in keys:
            if key not in usage_map:
                usage_map[key] = []
            usage_map[key].append(tex_file)

    # Find unused
    unused = set(all_defined.keys()) - all_used

    # Find undefined (cited but not in bib)
    undefined = all_used - set(all_defined.keys())

    if args.format == "json":
        import json
        result = {
            "bib_files": [str(f) for f in bib_files],
            "tex_files": [str(f) for f in tex_files],
            "defined_count": len(all_defined),
            "used_count": len(all_used),
            "unused": sorted(unused),
            "undefined": sorted(undefined),
        }
        if args.show_used:
            result["used"] = sorted(all_used & set(all_defined.keys()))
        print(json.dumps(result, indent=2))
    else:
        print(f"Scanned {len(bib_files)} .bib file(s), {len(tex_files)} .tex file(s)")
        print(f"Defined: {len(all_defined)} citation keys")
        print(f"Used: {len(all_used)} citation keys")
        print()

        if unused:
            print(f"UNUSED CITATIONS ({len(unused)}):")
            print("-" * 40)
            for key in sorted(unused):
                print(f"  {key}")
                print(f"    defined in: {all_defined[key]}")
            print()
        else:
            print("All citations are used.")
            print()

        if undefined:
            print(f"UNDEFINED CITATIONS ({len(undefined)}):")
            print("-" * 40)
            for key in sorted(undefined):
                files = usage_map.get(key, [])
                print(f"  {key}")
                for f in files[:3]:  # Show first 3 files
                    print(f"    used in: {f}")
                if len(files) > 3:
                    print(f"    ... and {len(files) - 3} more files")
            print()

        if args.show_used:
            used_and_defined = sorted(all_used & set(all_defined.keys()))
            print(f"USED CITATIONS ({len(used_and_defined)}):")
            print("-" * 40)
            for key in used_and_defined:
                print(f"  {key}")

    # Exit with error if there are issues
    if unused or undefined:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
