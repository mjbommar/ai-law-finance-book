#!/usr/bin/env python3
"""Update Amazon KDP cover variables based on interior page count.

Calculates spine width and cover dimensions using Amazon KDP's specifications.

KDP Paperback (White Paper):
- Spine: (pages * 0.002252) + 0.06 inches
- Cover: 2*TrimWidth + Spine + 2*Bleed (width)
         TrimHeight + 2*Bleed (height)

KDP Paperback (Cream Paper):
- Spine: (pages * 0.0025) + 0.06 inches

Reference: https://kdp.amazon.com/cover-calculator
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# KDP specifications
STANDARD_BLEED = 0.125  # inches - trimmed off during manufacturing
WHITE_PAPER_THICKNESS = 0.002252  # inches per page
CREAM_PAPER_THICKNESS = 0.0025  # inches per page
SPINE_BASE = 0.06  # inches


def run_cmd(cmd: list[str]) -> str:
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "command failed")
    return result.stdout


def page_count_from_pdf(pdf_path: Path) -> int:
    if shutil.which("pdfinfo"):
        output = run_cmd(["pdfinfo", str(pdf_path)])
        match = re.search(r"^Pages:\s+(\d+)\s*$", output, re.MULTILINE)
        if match:
            return int(match.group(1))
    if shutil.which("mutool"):
        output = run_cmd(["mutool", "info", "-M", str(pdf_path)])
        match = re.search(r"^Pages:\s+(\d+)\s*$", output, re.MULTILINE)
        if match:
            return int(match.group(1))
    raise RuntimeError("unable to determine page count (need pdfinfo or mutool)")


def spine_width_kdp(pages: int, paper: str = "white") -> float:
    """Calculate KDP spine width."""
    if pages < 24:
        raise ValueError("KDP paperback requires at least 24 interior pages")
    if paper == "cream":
        return (pages * CREAM_PAPER_THICKNESS) + SPINE_BASE
    else:
        return (pages * WHITE_PAPER_THICKNESS) + SPINE_BASE


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update Amazon KDP cover variables",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # From interior PDF (white paper)
  python update_kdp_cover_vars.py --pdf kdp-interior.pdf

  # From page count (cream paper)
  python update_kdp_cover_vars.py --page-count 250 --paper cream

  # Custom output file
  python update_kdp_cover_vars.py --pdf kdp-interior.pdf --output front-matter/cover/kdp-cover-vars.tex
""",
    )
    parser.add_argument("--pdf", type=Path, help="Interior PDF for page count")
    parser.add_argument("--page-count", type=int, help="Interior page count (alternative to --pdf)")
    parser.add_argument(
        "--paper",
        choices=["white", "cream"],
        default="white",
        help="Paper type (default: white)",
    )
    parser.add_argument("--trim-width", type=float, default=6.0, help="Trim width in inches (default: 6.0)")
    parser.add_argument("--trim-height", type=float, default=9.0, help="Trim height in inches (default: 9.0)")
    parser.add_argument("--bleed", type=float, default=STANDARD_BLEED, help=f"Bleed in inches (default: {STANDARD_BLEED})")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("front-matter/cover/kdp-cover-vars.tex"),
        help="Output TeX file",
    )
    args = parser.parse_args()

    # Determine page count
    if args.page_count is None:
        if not args.pdf:
            parser.error("provide --pdf or --page-count")
        if not args.pdf.exists():
            parser.error(f"pdf not found: {args.pdf}")
        pages = page_count_from_pdf(args.pdf)
    else:
        pages = args.page_count

    # Calculate spine width
    spine_in = spine_width_kdp(pages, args.paper)

    # Calculate total cover dimensions
    # KDP: 2*TrimWidth + Spine + 2*Bleed
    cover_width_in = (2 * args.trim_width) + spine_in + (2 * args.bleed)
    cover_height_in = args.trim_height + (2 * args.bleed)

    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Paper thickness info
    if args.paper == "cream":
        thickness = CREAM_PAPER_THICKNESS
    else:
        thickness = WHITE_PAPER_THICKNESS

    spec_comment = (
        f"% KDP Paperback Specifications ({args.paper} paper):\n"
        f"%   - Spine width: {spine_in:.4f}\" (formula: pages*{thickness} + {SPINE_BASE})\n"
        f"%   - Total cover: {cover_width_in:.4f}\" x {cover_height_in:.4f}\"\n"
        f"%   - Interior trim: {args.trim_width}\" x {args.trim_height}\"\n"
        f"%   - Bleed: {args.bleed}\"\n"
    )

    content = (
        "% ============================================================================\n"
        "% COVER VARIABLES - Generated for Amazon KDP wrap cover\n"
        "% ============================================================================\n"
        f"% Generated: {now}\n"
        f"% Paper: {args.paper} | Pages: {pages}\n"
        f"{spec_comment}"
        "% ============================================================================\n\n"
        "\\newlength{\\CoverTrimWidth}\n"
        "\\newlength{\\CoverTrimHeight}\n"
        "\\newlength{\\CoverBleed}\n"
        "\\newlength{\\CoverSpineWidth}\n"
        "\\newlength{\\CoverWrapArea}\n"
        f"\\newcommand{{\\CoverPageCount}}{{{pages}}}\n"
        f"\\newcommand{{\\CoverPaper}}{{{args.paper}}}\n"
        f"\\newcommand{{\\CoverBinding}}{{kdp-paperback}}\n\n"
        f"\\setlength{{\\CoverTrimWidth}}{{{args.trim_width:.3f}in}}\n"
        f"\\setlength{{\\CoverTrimHeight}}{{{args.trim_height:.3f}in}}\n"
        f"\\setlength{{\\CoverBleed}}{{{args.bleed:.3f}in}}\n"
        f"\\setlength{{\\CoverSpineWidth}}{{{spine_in:.6f}in}}\n"
        f"\\setlength{{\\CoverWrapArea}}{{0.000in}}\n\n"
        f"% Derived dimensions (inches):\n"
        f"%   Total cover width:  {cover_width_in:.6f}\n"
        f"%   Total cover height: {cover_height_in:.4f}\n"
    )
    output.write_text(content)

    print(f"Wrote {output}")
    print(f"Paper: {args.paper}")
    print(f"Pages: {pages}")
    print(f"Spine width: {spine_in:.4f}\"")
    print(f"Total cover: {cover_width_in:.4f}\" x {cover_height_in:.4f}\"")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
