#!/usr/bin/env python3
"""
PDF Margin Content Detector

Analyzes PDF documents to find content bleeding into margins (overfull boxes,
oversized images, etc.). Uses pypdfium2 for rendering and numpy for pixel analysis.

Usage:
    uv run --with pypdfium2,pillow,numpy,rich,typer python scripts/check_margins.py main.pdf

Author: AI Assistant
License: MIT
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

import numpy as np
import pypdfium2 as pdfium
from PIL import Image
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.table import Table
from rich import box
import typer

app = typer.Typer(
    name="check_margins",
    help="Detect content bleeding into PDF margins",
    add_completion=False,
)

console = Console()


class MarginType(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    BOTTOM = "bottom"
    TOP = "top"


@dataclass
class MarginViolation:
    """Represents a margin violation found on a page."""
    page_num: int  # 1-indexed
    margin_type: MarginType
    pixel_count: int  # Number of non-white pixels
    percentage: float  # Percentage of margin area with content
    bbox: tuple[int, int, int, int]  # (x1, y1, x2, y2) of violation area
    severity: str  # "low", "medium", "high"


@dataclass
class PageAnalysis:
    """Results of analyzing a single page."""
    page_num: int
    width_px: int
    height_px: int
    violations: list[MarginViolation] = field(default_factory=list)
    whitespace_gaps: list["WhitespaceGap"] = field(default_factory=list)

    @property
    def has_violations(self) -> bool:
        return len(self.violations) > 0

    @property
    def has_whitespace_gaps(self) -> bool:
        return len(self.whitespace_gaps) > 0

    @property
    def has_any_issues(self) -> bool:
        return self.has_violations or self.has_whitespace_gaps


@dataclass
class MarginConfig:
    """Configuration for margin detection.

    Default values are for US Trade (6x9in) book format with typical LaTeX book class margins:
    - Paper: 6in x 9in
    - Inner (gutter): 0.75in = 12.5% of width
    - Outer: 0.625in = 10.4% of width
    - Top: 0.7in = 7.8% of height
    - Bottom: 0.8in = 8.9% of height
    """
    # Page dimensions (inches) - US Trade default
    page_width_in: float = 6.0
    page_height_in: float = 9.0

    # Margin sizes in inches (matching geometry package defaults)
    inner_margin_in: float = 0.75   # Gutter (binding side)
    outer_margin_in: float = 0.625  # Outside edge
    top_margin_in: float = 0.7
    bottom_margin_in: float = 0.8

    # Twoside document (margins swap on odd/even pages)
    twoside: bool = True

    # Areas to skip (headers, footers) - as percentage of margin
    top_skip_pct: float = 0.0  # Skip top X% of top margin for running headers
    bottom_skip_pct: float = 0.0  # Skip bottom X% of bottom margin for footers

    # Page number exclusion zone (horizontal center of bottom margin)
    page_num_center_start_pct: float = 40.0  # Start of center skip
    page_num_center_end_pct: float = 60.0  # End of center skip

    # Detection parameters
    threshold: int = 250  # Pixels below this are "content" (0=black, 255=white)
    min_violation_pixels: int = 50  # Minimum pixels to report as violation
    dpi: int = 150  # Render resolution

    # Page skipping
    skip_first: int = 0
    skip_last: int = 0

    # Margin enable/disable
    check_top: bool = True
    check_bottom: bool = True
    check_left: bool = True
    check_right: bool = True

    # Whitespace gap detection
    check_whitespace: bool = False
    gap_min_height_in: float = 1.0  # Minimum gap height in inches
    gap_include_margins: bool = False  # If True, scan full page height
    gap_skip_page_white_pct: float = 95.0  # Skip gap scan if page is >= this % white

    def get_margins_for_page(self, page_num: int) -> tuple[float, float, float, float]:
        """Get (left, right, top, bottom) margins in inches for a given page number.

        For twoside documents:
        - Odd pages (recto): left=inner, right=outer
        - Even pages (verso): left=outer, right=inner
        """
        if self.twoside:
            if page_num % 2 == 1:  # Odd page (recto)
                left = self.inner_margin_in
                right = self.outer_margin_in
            else:  # Even page (verso)
                left = self.outer_margin_in
                right = self.inner_margin_in
        else:
            left = self.inner_margin_in
            right = self.outer_margin_in

        return (left, right, self.top_margin_in, self.bottom_margin_in)

    def margins_to_pixels(self, page_num: int, width_px: int, height_px: int) -> tuple[int, int, int, int]:
        """Convert margins to pixel coordinates for a rendered page.

        Returns (left_px, right_start_px, top_px, bottom_start_px).
        """
        left_in, right_in, top_in, bottom_in = self.get_margins_for_page(page_num)

        # Calculate pixels per inch from rendered dimensions
        ppi_x = width_px / self.page_width_in
        ppi_y = height_px / self.page_height_in

        left_px = int(left_in * ppi_x)
        right_start_px = width_px - int(right_in * ppi_x)
        top_px = int(top_in * ppi_y)
        bottom_start_px = height_px - int(bottom_in * ppi_y)

        return (left_px, right_start_px, top_px, bottom_start_px)


def render_page_to_array(page: pdfium.PdfPage, dpi: int) -> np.ndarray:
    """Render a PDF page to a numpy array."""
    # Calculate scale factor
    scale = dpi / 72.0  # PDF uses 72 DPI internally

    # Render to bitmap
    bitmap = page.render(scale=scale)
    pil_image = bitmap.to_pil()

    # Convert to grayscale for simpler analysis
    gray = pil_image.convert("L")

    return np.array(gray)


def find_content_bbox(region: np.ndarray, threshold: int) -> Optional[tuple[int, int, int, int]]:
    """Find bounding box of content in a region. Returns (x1, y1, x2, y2) or None."""
    # Find pixels below threshold (content)
    content_mask = region < threshold

    if not np.any(content_mask):
        return None

    # Find bounding box
    rows = np.any(content_mask, axis=1)
    cols = np.any(content_mask, axis=0)

    y_indices = np.where(rows)[0]
    x_indices = np.where(cols)[0]

    if len(y_indices) == 0 or len(x_indices) == 0:
        return None

    return (
        int(x_indices[0]),
        int(y_indices[0]),
        int(x_indices[-1]),
        int(y_indices[-1])
    )


def classify_severity(pixel_count: int, percentage: float) -> str:
    """Classify violation severity based on pixel count and percentage."""
    if percentage > 5.0 or pixel_count > 5000:
        return "high"
    elif percentage > 1.0 or pixel_count > 1000:
        return "medium"
    else:
        return "low"


def classify_gap_severity(height_in: float, min_height_in: float) -> str:
    """Classify whitespace gap severity based on height in inches."""
    if height_in >= min_height_in * 2.0:
        return "high"
    if height_in >= min_height_in * 1.5:
        return "medium"
    return "low"


@dataclass
class WhitespaceGap:
    """Represents a full-width whitespace gap on a page."""
    page_num: int  # 1-indexed
    height_px: int
    height_in: float
    bbox: tuple[int, int, int, int]  # (x1, y1, x2, y2)
    severity: str  # "low", "medium", "high"


def analyze_margin_region(
    page_array: np.ndarray,
    region_coords: tuple[int, int, int, int],  # x1, y1, x2, y2
    margin_type: MarginType,
    page_num: int,
    config: MarginConfig,
) -> Optional[MarginViolation]:
    """Analyze a margin region for content violations."""
    x1, y1, x2, y2 = region_coords

    # Extract region
    region = page_array[y1:y2, x1:x2]

    if region.size == 0:
        return None

    # Count non-white pixels
    content_mask = region < config.threshold
    pixel_count = int(np.sum(content_mask))

    if pixel_count < config.min_violation_pixels:
        return None

    # Calculate percentage
    total_pixels = region.size
    percentage = (pixel_count / total_pixels) * 100

    # Find bounding box of content within region
    local_bbox = find_content_bbox(region, config.threshold)
    if local_bbox is None:
        return None

    # Convert to page coordinates
    lx1, ly1, lx2, ly2 = local_bbox
    bbox = (x1 + lx1, y1 + ly1, x1 + lx2, y1 + ly2)

    severity = classify_severity(pixel_count, percentage)

    return MarginViolation(
        page_num=page_num,
        margin_type=margin_type,
        pixel_count=pixel_count,
        percentage=percentage,
        bbox=bbox,
        severity=severity,
    )


def analyze_page(
    page: pdfium.PdfPage,
    page_num: int,
    config: MarginConfig,
) -> PageAnalysis:
    """Analyze a single page for margin violations."""
    # Render page
    page_array = render_page_to_array(page, config.dpi)
    height_px, width_px = page_array.shape

    analysis = PageAnalysis(
        page_num=page_num,
        width_px=width_px,
        height_px=height_px,
    )

    # Get margin boundaries in pixels for this specific page (handles twoside)
    left_margin_px, right_margin_start_px, top_margin_px, bottom_margin_start_px = \
        config.margins_to_pixels(page_num, width_px, height_px)

    # Calculate skip zones (as percentage of the margin area, not page)
    # For top: skip from page edge inward by skip percentage of top margin
    top_skip_px = int(top_margin_px * config.top_skip_pct / 100)
    # For bottom: skip from bottom edge upward by skip percentage of bottom margin
    bottom_margin_height = height_px - bottom_margin_start_px
    bottom_skip_start_px = height_px - int(bottom_margin_height * config.bottom_skip_pct / 100)

    # Page number exclusion zone (for bottom margin)
    page_num_start_px = int(width_px * config.page_num_center_start_pct / 100)
    page_num_end_px = int(width_px * config.page_num_center_end_pct / 100)

    # Analyze LEFT margin (skip header/footer zones)
    if config.check_left:
        left_region = (
            0,  # x1
            top_skip_px,  # y1 (skip header)
            left_margin_px,  # x2
            bottom_skip_start_px,  # y2 (skip footer)
        )
        violation = analyze_margin_region(
            page_array, left_region, MarginType.LEFT, page_num, config
        )
        if violation:
            analysis.violations.append(violation)

    # Analyze RIGHT margin (skip header/footer zones)
    if config.check_right:
        right_region = (
            right_margin_start_px,  # x1
            top_skip_px,  # y1
            width_px,  # x2
            bottom_skip_start_px,  # y2
        )
        violation = analyze_margin_region(
            page_array, right_region, MarginType.RIGHT, page_num, config
        )
        if violation:
            analysis.violations.append(violation)

    # Analyze BOTTOM margin (split into left and right parts, excluding page number zone)
    if config.check_bottom:
        # Left part of bottom margin
        bottom_left_region = (
            0,  # x1
            bottom_margin_start_px,  # y1
            page_num_start_px,  # x2 (stop before page number zone)
            height_px,  # y2
        )
        violation = analyze_margin_region(
            page_array, bottom_left_region, MarginType.BOTTOM, page_num, config
        )
        if violation:
            analysis.violations.append(violation)

        # Right part of bottom margin
        bottom_right_region = (
            page_num_end_px,  # x1 (start after page number zone)
            bottom_margin_start_px,  # y1
            width_px,  # x2
            height_px,  # y2
        )
        violation = analyze_margin_region(
            page_array, bottom_right_region, MarginType.BOTTOM, page_num, config
        )
        if violation:
            analysis.violations.append(violation)

    # Analyze TOP margin (full width, for completeness)
    # Skip the very top edge (possible PDF artifacts)
    if config.check_top:
        top_region = (
            left_margin_px,  # x1 (exclude corners which may have page numbers)
            0,  # y1
            right_margin_start_px,  # x2
            top_margin_px,  # y2
        )
        violation = analyze_margin_region(
            page_array, top_region, MarginType.TOP, page_num, config
        )
        if violation:
            analysis.violations.append(violation)

    # Analyze full-width whitespace gaps
    if config.check_whitespace:
        analysis.whitespace_gaps.extend(
            find_whitespace_gaps(
                page_array,
                page_num,
                config,
                top_margin_px,
                bottom_margin_start_px,
            )
        )

    return analysis


def find_whitespace_gaps(
    page_array: np.ndarray,
    page_num: int,
    config: MarginConfig,
    top_margin_px: int,
    bottom_margin_start_px: int,
) -> list[WhitespaceGap]:
    """Find full-width whitespace gaps exceeding the minimum height."""
    height_px, width_px = page_array.shape

    # Determine vertical scan region
    if config.gap_include_margins:
        y_start, y_end = 0, height_px
    else:
        y_start, y_end = top_margin_px, bottom_margin_start_px

    if y_start >= y_end:
        return []

    # Skip near-blank pages to avoid flagging whole-page gaps
    scan_region = page_array[y_start:y_end, :]
    content_pixels = int(np.sum(scan_region < config.threshold))
    total_pixels = scan_region.size
    if total_pixels == 0:
        return []
    white_pct = 100.0 * (1.0 - (content_pixels / total_pixels))
    if white_pct >= config.gap_skip_page_white_pct:
        return []

    # Compute pixels per inch vertically
    ppi_y = height_px / config.page_height_in
    min_gap_px = max(1, int(round(config.gap_min_height_in * ppi_y)))

    # Identify rows that are entirely white across the page width
    content_rows = np.any(scan_region < config.threshold, axis=1)
    white_rows = ~content_rows

    gaps: list[WhitespaceGap] = []
    run_start: Optional[int] = None

    for idx, is_white in enumerate(white_rows):
        if is_white and run_start is None:
            run_start = idx
        elif not is_white and run_start is not None:
            run_end = idx
            run_len = run_end - run_start
            if run_len >= min_gap_px:
                y1 = y_start + run_start
                y2 = y_start + run_end
                height_in = run_len / ppi_y
                severity = classify_gap_severity(height_in, config.gap_min_height_in)
                gaps.append(WhitespaceGap(
                    page_num=page_num,
                    height_px=run_len,
                    height_in=height_in,
                    bbox=(0, y1, width_px, y2),
                    severity=severity,
                ))
            run_start = None

    if run_start is not None:
        run_end = len(white_rows)
        run_len = run_end - run_start
        if run_len >= min_gap_px:
            y1 = y_start + run_start
            y2 = y_start + run_end
            height_in = run_len / ppi_y
            severity = classify_gap_severity(height_in, config.gap_min_height_in)
            gaps.append(WhitespaceGap(
                page_num=page_num,
                height_px=run_len,
                height_in=height_in,
                bbox=(0, y1, width_px, y2),
                severity=severity,
            ))

    return gaps


def format_severity(severity: str) -> str:
    """Format severity with color."""
    colors = {
        "low": "[yellow]LOW[/yellow]",
        "medium": "[orange1]MEDIUM[/orange1]",
        "high": "[red bold]HIGH[/red bold]",
    }
    return colors.get(severity, severity)


def print_summary(analyses: list[PageAnalysis], pdf_path: Path, config: MarginConfig) -> int:
    """Print summary of all analyses. Returns exit code."""
    total_margin_violations = sum(len(a.violations) for a in analyses)
    total_gap_violations = sum(len(a.whitespace_gaps) for a in analyses)
    total_issues = total_margin_violations + total_gap_violations
    pages_with_issues = sum(1 for a in analyses if a.has_any_issues)

    # Summary panel
    summary_lines = [
        f"[bold]File:[/bold] {pdf_path.name}",
        f"[bold]Pages analyzed:[/bold] {len(analyses)}",
        f"[bold]Pages with issues:[/bold] {pages_with_issues}",
        f"[bold]Margin violations:[/bold] {total_margin_violations}",
        f"[bold]Whitespace gaps:[/bold] {total_gap_violations}",
    ]

    if total_issues == 0:
        console.print(Panel(
            "\n".join(summary_lines) + "\n\n[green bold]No margin or whitespace issues found![/green bold]",
            title="Margin Analysis Complete",
            border_style="green",
        ))
        return 0

    console.print(Panel(
        "\n".join(summary_lines),
        title="Margin Analysis Summary",
        border_style="yellow" if total_issues < 10 else "red",
    ))

    # Detailed violations table
    if total_margin_violations > 0:
        table = Table(
            title="Margin Violations",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold cyan",
        )

        table.add_column("Page", justify="right", style="bold")
        table.add_column("Margin", justify="center")
        table.add_column("Severity", justify="center")
        table.add_column("Pixels", justify="right")
        table.add_column("Coverage", justify="right")
        table.add_column("Location (x1,y1)-(x2,y2)", justify="left")

        # Sort violations by severity then page
        all_violations: list[MarginViolation] = []
        for analysis in analyses:
            all_violations.extend(analysis.violations)

        severity_order = {"high": 0, "medium": 1, "low": 2}
        all_violations.sort(key=lambda v: (severity_order[v.severity], v.page_num))

        for v in all_violations:
            table.add_row(
                str(v.page_num),
                v.margin_type.value.upper(),
                format_severity(v.severity),
                f"{v.pixel_count:,}",
                f"{v.percentage:.2f}%",
                f"({v.bbox[0]},{v.bbox[1]})-({v.bbox[2]},{v.bbox[3]})",
            )

        console.print(table)

    if total_gap_violations > 0:
        gap_table = Table(
            title="Whitespace Gaps",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta",
        )

        gap_table.add_column("Page", justify="right", style="bold")
        gap_table.add_column("Severity", justify="center")
        gap_table.add_column("Height (in)", justify="right")
        gap_table.add_column("Height (px)", justify="right")
        gap_table.add_column("Location (x1,y1)-(x2,y2)", justify="left")

        all_gaps: list[WhitespaceGap] = []
        for analysis in analyses:
            all_gaps.extend(analysis.whitespace_gaps)

        severity_order = {"high": 0, "medium": 1, "low": 2}
        all_gaps.sort(key=lambda g: (severity_order[g.severity], g.page_num))

        for g in all_gaps:
            gap_table.add_row(
                str(g.page_num),
                format_severity(g.severity),
                f"{g.height_in:.2f}",
                f"{g.height_px:,}",
                f"({g.bbox[0]},{g.bbox[1]})-({g.bbox[2]},{g.bbox[3]})",
            )

        console.print(gap_table)

    # Group by page for easier fixing
    console.print("\n[bold]Pages requiring attention:[/bold]")
    for analysis in analyses:
        if analysis.has_any_issues:
            margins = ", ".join(sorted(set(v.margin_type.value for v in analysis.violations)))
            gaps = len(analysis.whitespace_gaps)
            severities = [v.severity for v in analysis.violations] + [g.severity for g in analysis.whitespace_gaps]
            worst = "high" if "high" in severities else ("medium" if "medium" in severities else "low")
            margin_str = f"{margins} margin(s)" if margins else "no margin issues"
            gap_str = f"{gaps} gap(s)" if gaps > 0 else "no gaps"
            console.print(f"  Page {analysis.page_num}: {margin_str}, {gap_str} - {format_severity(worst)}")

    any_high = any(v.severity == "high" for analysis in analyses for v in analysis.violations)
    any_high_gap = any(g.severity == "high" for analysis in analyses for g in analysis.whitespace_gaps)
    return 1 if (any_high or any_high_gap) else 0


def save_debug_images(
    pdf: pdfium.PdfDocument,
    analyses: list[PageAnalysis],
    output_dir: Path,
    config: MarginConfig,
) -> None:
    """Save debug images showing detected violations."""
    output_dir.mkdir(parents=True, exist_ok=True)

    pages_to_save = [a for a in analyses if a.has_any_issues]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Saving debug images...", total=len(pages_to_save))

        for analysis in pages_to_save:
            page_idx = analysis.page_num - 1  # 0-indexed
            page = pdf[page_idx]

            # Render at higher DPI for debug
            scale = config.dpi / 72.0
            bitmap = page.render(scale=scale)
            pil_image = bitmap.to_pil().convert("RGB")

            # Draw margin regions and violations
            from PIL import ImageDraw
            draw = ImageDraw.Draw(pil_image)

            width_px, height_px = pil_image.size

            # Get margin boundaries for this page (handles twoside)
            left_margin_px, right_margin_start_px, top_margin_px, bottom_margin_start_px = \
                config.margins_to_pixels(analysis.page_num, width_px, height_px)

            margin_color = (100, 100, 255)  # Light blue
            draw.line([(left_margin_px, 0), (left_margin_px, height_px)], fill=margin_color, width=2)
            draw.line([(right_margin_start_px, 0), (right_margin_start_px, height_px)], fill=margin_color, width=2)
            draw.line([(0, top_margin_px), (width_px, top_margin_px)], fill=margin_color, width=2)
            draw.line([(0, bottom_margin_start_px), (width_px, bottom_margin_start_px)], fill=margin_color, width=2)

            # Draw violations (red boxes)
            for violation in analysis.violations:
                x1, y1, x2, y2 = violation.bbox
                color = {"high": (255, 0, 0), "medium": (255, 165, 0), "low": (255, 255, 0)}[violation.severity]
                draw.rectangle([x1, y1, x2, y2], outline=color, width=3)

            # Draw whitespace gaps (purple boxes)
            for gap in analysis.whitespace_gaps:
                x1, y1, x2, y2 = gap.bbox
                color = {"high": (180, 0, 255), "medium": (210, 120, 255), "low": (235, 200, 255)}[gap.severity]
                draw.rectangle([x1, y1, x2, y2], outline=color, width=3)

            # Save
            output_path = output_dir / f"page_{analysis.page_num:04d}_violations.png"
            pil_image.save(output_path)

            progress.update(task, advance=1)

    console.print(f"[green]Debug images saved to:[/green] {output_dir}")


@app.command()
def check(
    pdf_path: Path = typer.Argument(..., help="Path to PDF file to analyze"),
    # Page dimensions (US Trade 6x9 default)
    page_width: float = typer.Option(6.0, "--page-width", help="Page width in inches"),
    page_height: float = typer.Option(9.0, "--page-height", help="Page height in inches"),
    # Margin sizes in inches (LaTeX geometry defaults for US Trade)
    inner_margin: float = typer.Option(0.75, "--inner", "-i", help="Inner (gutter) margin in inches"),
    outer_margin: float = typer.Option(0.625, "--outer", "-o", help="Outer margin in inches"),
    top_margin: float = typer.Option(0.7, "--top", "-t", help="Top margin in inches"),
    bottom_margin: float = typer.Option(0.8, "--bottom", "-b", help="Bottom margin in inches"),
    # Twoside document
    oneside: bool = typer.Option(False, "--oneside", help="Oneside document (don't swap margins on even pages)"),
    # Skip zones (percentage of margin to skip for headers/footers)
    top_skip: float = typer.Option(0.0, "--top-skip", help="Skip % of top margin for running headers"),
    bottom_skip: float = typer.Option(0.0, "--bottom-skip", help="Skip % of bottom margin for footers"),
    page_num_start: float = typer.Option(40.0, "--page-num-start", help="Start of page number zone (% from left)"),
    page_num_end: float = typer.Option(60.0, "--page-num-end", help="End of page number zone (% from left)"),
    # Detection params
    threshold: int = typer.Option(250, "--threshold", help="Pixel threshold (0-255, below=content)"),
    min_pixels: int = typer.Option(50, "--min-pixels", help="Minimum pixels to report as violation"),
    dpi: int = typer.Option(150, "--dpi", help="Render resolution"),
    # Page skipping
    skip_first: int = typer.Option(0, "--skip-first", help="Skip first N pages (covers)"),
    skip_last: int = typer.Option(0, "--skip-last", help="Skip last N pages (covers)"),
    # Margin enable/disable
    no_top: bool = typer.Option(False, "--no-top", help="Don't check top margin"),
    no_bottom: bool = typer.Option(False, "--no-bottom", help="Don't check bottom margin"),
    no_left: bool = typer.Option(False, "--no-left", help="Don't check left margin"),
    no_right: bool = typer.Option(False, "--no-right", help="Don't check right margin"),
    # Whitespace gap detection
    check_whitespace: bool = typer.Option(False, "--check-whitespace", help="Detect full-width whitespace gaps"),
    gap_min_height: float = typer.Option(1.0, "--gap-min-height", help="Minimum gap height in inches"),
    gap_include_margins: bool = typer.Option(False, "--gap-include-margins", help="Include margins when scanning for gaps"),
    gap_skip_page_white_pct: float = typer.Option(95.0, "--gap-skip-page-white-pct", help="Skip gap scan if page is >= this % white"),
    # Output options
    debug_dir: Optional[Path] = typer.Option(None, "--debug-dir", "-d", help="Save debug images to directory"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Only output violations"),
) -> None:
    """
    Analyze PDF margins for content violations.

    Detects overfull boxes, oversized images, and other content bleeding
    into margins. Useful for quality-checking LaTeX documents before printing.

    Examples:

        # Basic check with defaults
        check_margins.py document.pdf

        # Stricter margins (12% on each side)
        check_margins.py document.pdf -l 12 -r 12 -t 12 -b 12

        # Skip cover pages
        check_margins.py document.pdf --skip-first 1 --skip-last 1

        # Save debug images showing violations
        check_margins.py document.pdf --debug-dir ./margin-debug

        # Detect full-width whitespace gaps of at least 1 inch, skipping near-blank pages
        check_margins.py document.pdf --check-whitespace --gap-min-height 1.0 --gap-skip-page-white-pct 95
    """
    if not pdf_path.exists():
        console.print(f"[red]Error:[/red] File not found: {pdf_path}")
        raise typer.Exit(1)

    config = MarginConfig(
        page_width_in=page_width,
        page_height_in=page_height,
        inner_margin_in=inner_margin,
        outer_margin_in=outer_margin,
        top_margin_in=top_margin,
        bottom_margin_in=bottom_margin,
        twoside=not oneside,
        top_skip_pct=top_skip,
        bottom_skip_pct=bottom_skip,
        page_num_center_start_pct=page_num_start,
        page_num_center_end_pct=page_num_end,
        threshold=threshold,
        min_violation_pixels=min_pixels,
        dpi=dpi,
        skip_first=skip_first,
        skip_last=skip_last,
        check_top=not no_top,
        check_bottom=not no_bottom,
        check_left=not no_left,
        check_right=not no_right,
        check_whitespace=check_whitespace,
        gap_min_height_in=gap_min_height,
        gap_include_margins=gap_include_margins,
        gap_skip_page_white_pct=gap_skip_page_white_pct,
    )

    # Build margin check list for display
    checking = []
    if config.check_left:
        checking.append("L")
    if config.check_right:
        checking.append("R")
    if config.check_top:
        checking.append("T")
    if config.check_bottom:
        checking.append("B")
    margins_str = ", ".join(checking) if checking else "[dim]none[/dim]"
    twoside_str = "twoside" if config.twoside else "oneside"

    if not quiet:
        console.print(Panel(
            f"[bold]Analyzing:[/bold] {pdf_path}\n"
            f"[bold]Page size:[/bold] {page_width}\" x {page_height}\" ({twoside_str})\n"
            f"[bold]Margins:[/bold] inner={inner_margin}\" outer={outer_margin}\" top={top_margin}\" bottom={bottom_margin}\"\n"
            f"[bold]Checking:[/bold] {margins_str}\n"
            f"[bold]Detection:[/bold] threshold={threshold} min_pixels={min_pixels} dpi={dpi}\n"
            f"[bold]Whitespace gaps:[/bold] {('on' if check_whitespace else 'off')} "
            f"(min={gap_min_height}\" include_margins={gap_include_margins} "
            f"skip_page_white>={gap_skip_page_white_pct}%)",
            title="Margin Analysis Configuration",
            border_style="blue",
        ))

    # Open PDF
    try:
        pdf = pdfium.PdfDocument(str(pdf_path))
    except Exception as e:
        console.print(f"[red]Error opening PDF:[/red] {e}")
        raise typer.Exit(1)

    total_pages = len(pdf)

    # Calculate page range
    start_page = config.skip_first
    end_page = total_pages - config.skip_last

    if start_page >= end_page:
        console.print("[yellow]Warning:[/yellow] No pages to analyze after skipping.")
        raise typer.Exit(0)

    if not quiet:
        console.print(f"[dim]Analyzing pages {start_page + 1} to {end_page} of {total_pages}[/dim]\n")

    # Analyze pages
    analyses: list[PageAnalysis] = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
        disable=quiet,
    ) as progress:
        task = progress.add_task("Analyzing pages...", total=end_page - start_page)

        for page_idx in range(start_page, end_page):
            page = pdf[page_idx]
            analysis = analyze_page(page, page_idx + 1, config)  # 1-indexed page numbers
            analyses.append(analysis)
            progress.update(task, advance=1)

    # Print results
    exit_code = print_summary(analyses, pdf_path, config)

    # Save debug images if requested
    if debug_dir and any(a.has_violations for a in analyses):
        save_debug_images(pdf, analyses, debug_dir, config)

    pdf.close()
    raise typer.Exit(exit_code)


@app.command()
def show_config() -> None:
    """Show default configuration values (US Trade 6x9 format)."""
    config = MarginConfig()

    table = Table(title="Default Configuration (US Trade 6\"x9\")", box=box.ROUNDED)
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="green")
    table.add_column("Description")

    table.add_row("page_width_in", f'{config.page_width_in}"', "Page width")
    table.add_row("page_height_in", f'{config.page_height_in}"', "Page height")
    table.add_row("inner_margin_in", f'{config.inner_margin_in}"', "Inner (gutter) margin")
    table.add_row("outer_margin_in", f'{config.outer_margin_in}"', "Outer margin")
    table.add_row("top_margin_in", f'{config.top_margin_in}"', "Top margin")
    table.add_row("bottom_margin_in", f'{config.bottom_margin_in}"', "Bottom margin")
    table.add_row("twoside", str(config.twoside), "Twoside document (swap margins)")
    table.add_row("top_skip_pct", f"{config.top_skip_pct}%", "Skip % of top margin")
    table.add_row("bottom_skip_pct", f"{config.bottom_skip_pct}%", "Skip % of bottom margin")
    table.add_row("page_num_center_start_pct", f"{config.page_num_center_start_pct}%", "Page number zone start")
    table.add_row("page_num_center_end_pct", f"{config.page_num_center_end_pct}%", "Page number zone end")
    table.add_row("threshold", str(config.threshold), "Pixel brightness threshold")
    table.add_row("min_violation_pixels", str(config.min_violation_pixels), "Min pixels for violation")
    table.add_row("dpi", str(config.dpi), "Render resolution")
    table.add_row("check_whitespace", str(config.check_whitespace), "Detect full-width whitespace gaps")
    table.add_row("gap_min_height_in", f'{config.gap_min_height_in}"', "Minimum gap height")
    table.add_row("gap_include_margins", str(config.gap_include_margins), "Scan full page height for gaps")
    table.add_row("gap_skip_page_white_pct", f"{config.gap_skip_page_white_pct}%", "Skip gap scan if page mostly white")

    console.print(table)


if __name__ == "__main__":
    app()
