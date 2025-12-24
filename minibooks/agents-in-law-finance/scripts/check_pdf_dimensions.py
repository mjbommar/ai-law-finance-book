#!/usr/bin/env python3
"""Triple-check PDF dimensions using pdfinfo, mutool, and ghostscript."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd: list[str]) -> str:
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "command failed")
    return result.stdout


def parse_length_in(value: str) -> float:
    value = value.strip()
    match = re.match(r"^([0-9.]+)\s*(in|mm)?$", value)
    if not match:
        raise ValueError(f"unsupported length: {value}")
    number = float(match.group(1))
    unit = match.group(2) or "in"
    if unit == "in":
        return number
    if unit == "mm":
        return number / 25.4
    raise ValueError(f"unsupported unit: {unit}")


def sizes_from_cover_vars(vars_path: Path) -> tuple[float, float]:
    text = vars_path.read_text()

    def find_length(name: str) -> float:
        match = re.search(rf"\\setlength{{\\{name}}}{{([^}}]+)}}", text)
        if not match:
            raise ValueError(f"missing {name} in {vars_path}")
        return parse_length_in(match.group(1))

    trim_w = find_length("CoverTrimWidth")
    trim_h = find_length("CoverTrimHeight")
    bleed = find_length("CoverBleed")
    spine = find_length("CoverSpineWidth")

    width_in = (2 * trim_w) + spine + (2 * bleed)
    height_in = trim_h + (2 * bleed)
    return width_in, height_in


def size_from_pdfinfo(pdf_path: Path) -> tuple[float, float, int | None]:
    if not shutil.which("pdfinfo"):
        raise RuntimeError("pdfinfo not found")
    output = run_cmd(["pdfinfo", str(pdf_path)])
    match = re.search(r"Page size:\s+([0-9.]+)\s+x\s+([0-9.]+)\s+pts", output)
    if not match:
        raise RuntimeError("pdfinfo: page size not found")
    width_pt = float(match.group(1))
    height_pt = float(match.group(2))
    pages = None
    pages_match = re.search(r"^Pages:\s+(\d+)\s*$", output, re.MULTILINE)
    if pages_match:
        pages = int(pages_match.group(1))
    return width_pt, height_pt, pages


def size_from_mutool(pdf_path: Path) -> tuple[float, float, int | None]:
    if not shutil.which("mutool"):
        raise RuntimeError("mutool not found")
    output = run_cmd(["mutool", "info", "-M", str(pdf_path)])
    match = re.search(r"\[\s*([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s*\]", output)
    pages = None
    pages_match = re.search(r"^Pages:\s+(\d+)\s*$", output, re.MULTILINE)
    if pages_match:
        pages = int(pages_match.group(1))
    if match:
        llx, lly, urx, ury = (float(match.group(i)) for i in range(1, 5))
        width_pt = urx - llx
        height_pt = ury - lly
        return width_pt, height_pt, pages

    # Fallback: extract MediaBox from pages tree.
    catalog = run_cmd(["mutool", "show", str(pdf_path), "1"])
    pages_ref = re.search(r"/Pages\s+(\d+)\s+0\s+R", catalog)
    if not pages_ref:
        raise RuntimeError("mutool: pages reference not found")
    pages_obj = pages_ref.group(1)
    pages_obj_data = run_cmd(["mutool", "show", str(pdf_path), pages_obj])
    mediabox = re.search(
        r"/MediaBox\s*\[\s*([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s*\]",
        pages_obj_data,
    )
    if not mediabox:
        raise RuntimeError("mutool: mediabox not found")
    llx, lly, urx, ury = (float(mediabox.group(i)) for i in range(1, 5))
    width_pt = urx - llx
    height_pt = ury - lly
    if pages is None:
        count_match = re.search(r"/Count\s+(\d+)", pages_obj_data)
        if count_match:
            pages = int(count_match.group(1))
    return width_pt, height_pt, pages


def size_from_gs(pdf_path: Path) -> tuple[float, float, None]:
    if not shutil.which("gs"):
        raise RuntimeError("gs not found")
    cmd = [
        "gs",
        "-q",
        "-dNOSAFER",
        "-dNODISPLAY",
        "-c",
        (
            f"({pdf_path}) (r) file runpdfbegin "
            "1 1 pdfgetpage /MediaBox get "
            "dup 0 get =only ( ) print "
            "dup 1 get =only ( ) print "
            "dup 2 get =only ( ) print "
            "3 get =only quit"
        ),
    ]
    output = run_cmd(cmd)
    numbers = [float(x) for x in output.strip().split()]
    if len(numbers) != 4:
        raise RuntimeError(f"gs: unexpected output: {output.strip()}")
    llx, lly, urx, ury = numbers
    width_pt = urx - llx
    height_pt = ury - lly
    return width_pt, height_pt, None


def close_enough(value: float, expected: float, tol: float) -> bool:
    return abs(value - expected) <= tol


def main() -> int:
    parser = argparse.ArgumentParser(description="Triple-check PDF dimensions")
    parser.add_argument("pdf", type=Path, help="PDF to check")
    parser.add_argument("--vars", type=Path, help="TeX vars file with trim/bleed/spine")
    parser.add_argument("--width-in", type=float, help="Expected width in inches")
    parser.add_argument("--height-in", type=float, help="Expected height in inches")
    parser.add_argument("--pages", type=int, help="Expected page count")
    parser.add_argument("--tolerance-pt", type=float, default=0.5, help="Tolerance in points")
    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"PDF not found: {args.pdf}", file=sys.stderr)
        return 2

    if args.vars:
        expected_width_in, expected_height_in = sizes_from_cover_vars(args.vars)
    else:
        if args.width_in is None or args.height_in is None:
            print("Provide --vars or both --width-in and --height-in", file=sys.stderr)
            return 2
        expected_width_in = args.width_in
        expected_height_in = args.height_in

    expected_width_pt = expected_width_in * 72.0
    expected_height_pt = expected_height_in * 72.0

    methods = []
    errors = []

    try:
        w, h, pages = size_from_pdfinfo(args.pdf)
        methods.append(("pdfinfo", w, h, pages))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"pdfinfo: {exc}")

    try:
        w, h, pages = size_from_mutool(args.pdf)
        methods.append(("mutool", w, h, pages))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"mutool: {exc}")

    try:
        w, h, pages = size_from_gs(args.pdf)
        methods.append(("ghostscript", w, h, pages))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"ghostscript: {exc}")

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    print(f"Expected: {expected_width_pt:.2f} x {expected_height_pt:.2f} pts")

    ok = True
    for label, w, h, pages in methods:
        status = "ok"
        if not close_enough(w, expected_width_pt, args.tolerance_pt):
            status = "mismatch"
            ok = False
        if not close_enough(h, expected_height_pt, args.tolerance_pt):
            status = "mismatch"
            ok = False
        print(f"{label}: {w:.2f} x {h:.2f} pts ({status})")
        if args.pages is not None and pages is not None and pages != args.pages:
            print(f"{label}: pages {pages} != expected {args.pages}")
            ok = False

    # Cross-check agreement between methods
    base_label, base_w, base_h, _ = methods[0]
    for label, w, h, _ in methods[1:]:
        if not close_enough(w, base_w, args.tolerance_pt) or not close_enough(h, base_h, args.tolerance_pt):
            print(f"{label} differs from {base_label} beyond tolerance")
            ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
