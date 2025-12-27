#!/usr/bin/env python3
"""Update Lulu cover variables based on interior page count.

Calculates spine width and cover dimensions using Lulu's Book Creation Guide.

Paperback:
- Spine: (pages / 444) + 0.06 inches
- Cover: 2×TrimWidth + Spine + 2×Bleed

Hardcover Case Wrap:
- Spine: discrete table lookup (thicker spines)
- Wrap area: 0.75" on all edges (wraps around hardcover boards)
- Cover: 2×(TrimWidth + WrapArea) + Spine + 2×Bleed (width)
         TrimHeight + 2×WrapArea + 2×Bleed (height)

Reference: https://help.lulu.com/en/support/solutions/articles/64000308572
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Lulu hardcover case wrap specifications
HARDCOVER_WRAP_AREA = 0.75  # inches - wraps around boards
HARDCOVER_OVERHANG = 0.125  # inches - cover extends past pages
STANDARD_BLEED = 0.125  # inches - trimmed off during manufacturing

# Hardcover spine width table (page_min, page_max, spine_inches)
# From Lulu Book Creation Guide
HARDCOVER_TABLE = [
    (24, 84, 0.25),
    (85, 140, 0.5),
    (141, 168, 0.625),
    (169, 194, 0.688),
    (195, 222, 0.75),
    (223, 250, 0.813),
    (251, 278, 0.875),
    (279, 306, 0.938),
    (307, 334, 1.0),
    (335, 360, 1.063),
    (361, 388, 1.125),
    (389, 416, 1.188),
    (417, 444, 1.25),
    (445, 472, 1.313),
    (473, 500, 1.375),
    (501, 528, 1.438),
    (529, 556, 1.5),
    (557, 582, 1.563),
    (583, 610, 1.625),
    (611, 638, 1.688),
    (639, 666, 1.75),
    (667, 694, 1.813),
    (695, 722, 1.875),
    (723, 750, 1.938),
    (751, 778, 2.0),
    (779, 799, 2.063),
]


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


def spine_width_paperback(pages: int) -> float:
    if pages < 32:
        raise ValueError("paperback requires at least 32 interior pages")
    return (pages / 444.0) + 0.06


def spine_width_hardcover(pages: int) -> float:
    if pages < 24:
        raise ValueError("hardcover requires at least 24 interior pages")
    for low, high, width in HARDCOVER_TABLE:
        if low <= pages <= high:
            return width
    raise ValueError("page count out of supported hardcover range")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update Lulu cover variables",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Paperback (default)
  python update_cover_vars.py --pdf lulu-interior.pdf

  # Hardcover case wrap
  python update_cover_vars.py --pdf lulu-interior.pdf --binding hardcover

  # Hardcover with custom output file
  python update_cover_vars.py --pdf lulu-interior.pdf --binding hardcover \\
      --output front-matter/cover/cover-vars-hardcover.tex
""",
    )
    parser.add_argument("--pdf", type=Path, help="Interior PDF for page count")
    parser.add_argument("--page-count", type=int, help="Interior page count (alternative to --pdf)")
    parser.add_argument(
        "--binding",
        choices=["paperback", "hardcover"],
        default="paperback",
        help="Binding type (default: paperback)",
    )
    parser.add_argument("--trim-width", type=float, default=6.0, help="Trim width in inches (default: 6.0)")
    parser.add_argument("--trim-height", type=float, default=9.0, help="Trim height in inches (default: 9.0)")
    parser.add_argument("--bleed", type=float, default=STANDARD_BLEED, help=f"Bleed in inches (default: {STANDARD_BLEED})")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("front-matter/cover/cover-vars.tex"),
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

    # Calculate spine width based on binding type
    if args.binding == "paperback":
        spine_in = spine_width_paperback(pages)
        wrap_in = 0.0  # No wrap area for paperback
    else:
        spine_in = spine_width_hardcover(pages)
        wrap_in = HARDCOVER_WRAP_AREA  # 0.75" wrap for hardcover case wrap

    # Calculate total cover dimensions
    # Paperback: 2×TrimWidth + Spine + 2×Bleed
    # Hardcover: 2×(TrimWidth + WrapArea) + Spine + 2×Bleed
    cover_width_in = (2 * (args.trim_width + wrap_in)) + spine_in + (2 * args.bleed)
    cover_height_in = args.trim_height + (2 * wrap_in) + (2 * args.bleed)

    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build header comment with specifications
    if args.binding == "hardcover":
        spec_comment = (
            f"% Hardcover Case Wrap Specifications:\n"
            f"%   - Wrap area: {wrap_in}\" (wraps around boards)\n"
            f"%   - Spine width: {spine_in:.3f}\" (from table lookup)\n"
            f"%   - Total cover: {cover_width_in:.3f}\" × {cover_height_in:.3f}\"\n"
            f"%   - Interior trim: {args.trim_width}\" × {args.trim_height}\"\n"
        )
    else:
        spec_comment = (
            f"% Paperback Perfect Bound Specifications:\n"
            f"%   - Spine width: {spine_in:.3f}\" (formula: pages/444 + 0.06)\n"
            f"%   - Total cover: {cover_width_in:.3f}\" × {cover_height_in:.3f}\"\n"
            f"%   - Interior trim: {args.trim_width}\" × {args.trim_height}\"\n"
        )

    content = (
        "% ============================================================================\n"
        "% COVER VARIABLES - Generated for Lulu wrap cover\n"
        "% ============================================================================\n"
        f"% Generated: {now}\n"
        f"% Binding: {args.binding} | Pages: {pages}\n"
        f"{spec_comment}"
        "% ============================================================================\n\n"
        "\\newlength{\\CoverTrimWidth}\n"
        "\\newlength{\\CoverTrimHeight}\n"
        "\\newlength{\\CoverBleed}\n"
        "\\newlength{\\CoverSpineWidth}\n"
        "\\newlength{\\CoverWrapArea}\n"
        f"\\newcommand{{\\CoverPageCount}}{{{pages}}}\n"
        f"\\newcommand{{\\CoverBinding}}{{{args.binding}}}\n\n"
        f"\\setlength{{\\CoverTrimWidth}}{{{args.trim_width:.3f}in}}\n"
        f"\\setlength{{\\CoverTrimHeight}}{{{args.trim_height:.3f}in}}\n"
        f"\\setlength{{\\CoverBleed}}{{{args.bleed:.3f}in}}\n"
        f"\\setlength{{\\CoverSpineWidth}}{{{spine_in:.6f}in}}\n"
        f"\\setlength{{\\CoverWrapArea}}{{{wrap_in:.3f}in}}\n\n"
        f"% Derived dimensions (inches):\n"
        f"%   Total cover width:  {cover_width_in:.6f}\n"
        f"%   Total cover height: {cover_height_in:.3f}\n"
    )
    output.write_text(content)

    print(f"Wrote {output}")
    print(f"Binding: {args.binding}")
    print(f"Pages: {pages}")
    print(f"Spine width: {spine_in:.3f}\"")
    if wrap_in > 0:
        print(f"Wrap area: {wrap_in:.3f}\"")
    print(f"Total cover: {cover_width_in:.3f}\" × {cover_height_in:.3f}\"")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
