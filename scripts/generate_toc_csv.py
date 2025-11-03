#!/usr/bin/env python3
"""
Generate a global table of contents CSV mapping with indices:
  - chapter_index (book order from main.tex)
  - section_index (order within chapter)
  - chapter_folder (dirname under chapters/)
  - chapter_title (combined Huge: Large when available)
  - section_title
  - file (relative path)

Parsing rules:
  - Chapter order comes from root `main.tex` via `\subfile{chapters/.../main}` lines.
  - Chapter title prefers combined `Huge: Large` from the chapter's `\title{...}` block; then Large; then Huge; then folder name.
  - Section order comes from `\input{sections/...}` lines in chapter `main.tex`.
  - Section title is taken from the first `\section{...}` or `\section*{...}` in each section file.

Outputs CSV to `assets/tables/global_toc.csv`.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_MAIN = ROOT / "main.tex"

CHAPTER_SUBFILE_RE = re.compile(r"^\\subfile\{(chapters/[^}]+?/main)\}")
TITLE_BLOCK_START_RE = re.compile(r"^\\title\{")
TITLE_LARGE_LINE_RE = re.compile(r"\{\\LARGE[^}]*\}?(.*?)\\\\")
TITLE_HUGE_LINE_RE = re.compile(r"\{\\Huge[^}]*\}?(.*?)\\\\")
INPUT_SECTION_RE = re.compile(r"^\\input\{sections/([^}]+)\}")
SECTION_TITLE_RE = re.compile(r"^\\section\*?\{([^}]*)\}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def tex_to_plain(s: str) -> str:
    s = re.sub(r"\\\\", " ", s)  # line breaks
    s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", "", s)  # commands
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract_chapter_order(book_main: Path) -> list[Path]:
    order: list[Path] = []
    for line in read_text(book_main).splitlines():
        m = CHAPTER_SUBFILE_RE.match(line.strip())
        if m:
            rel = m.group(1)
            p = ROOT / (rel + ".tex" if not rel.endswith(".tex") else rel)
            order.append(p)
    return order


def extract_chapter_title(chapter_main: Path) -> str:
    lines = read_text(chapter_main).splitlines()
    title_lines: list[str] = []
    in_title = False
    brace_depth = 0
    for raw in lines:
        line = raw.rstrip("\n")
        if not in_title and TITLE_BLOCK_START_RE.match(line.strip()):
            in_title = True
            brace_depth = line.count("{") - line.count("}")
            title_lines.append(line)
            continue
        if in_title:
            title_lines.append(line)
            brace_depth += line.count("{") - line.count("}")
            if brace_depth <= 0:
                break

    title_block = "\n".join(title_lines)
    m_large = TITLE_LARGE_LINE_RE.search(title_block)
    m_huge = TITLE_HUGE_LINE_RE.search(title_block)
    if m_huge and m_large:
        huge = tex_to_plain(m_huge.group(1))
        large = tex_to_plain(m_large.group(1))
        combined = f"{huge}: {large}" if huge and large else (huge or large)
        return combined
    if m_large:
        return tex_to_plain(m_large.group(1))
    if m_huge:
        return tex_to_plain(m_huge.group(1))
    return chapter_main.parent.name.replace("-", " ")


def extract_section_order(chapter_main: Path) -> list[str]:
    order: list[str] = []
    for line in read_text(chapter_main).splitlines():
        m = INPUT_SECTION_RE.match(line.strip())
        if m:
            order.append(m.group(1) + ".tex")
    return order


def extract_section_title(section_path: Path) -> str:
    for line in read_text(section_path).splitlines():
        m = SECTION_TITLE_RE.match(line.strip())
        if m:
            return tex_to_plain(m.group(1))
    return section_path.stem.replace("_", " ")


def generate_csv(rows: list[tuple[int, int, str, str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["chapter_index", "section_index", "chapter_folder", "chapter_title", "section_title", "file"])
        for r in rows:
            w.writerow(r)


def main() -> None:
    chapter_mains = extract_chapter_order(BOOK_MAIN)
    rows: list[tuple[int, int, str, str, str]] = []
    for chap_idx, ch_main in enumerate(chapter_mains, start=1):
        if not ch_main.exists():
            continue
        ch_title = extract_chapter_title(ch_main)
        ch_folder = ch_main.parent.name
        sec_files = extract_section_order(ch_main)
        for sec_idx, sec_rel in enumerate(sec_files, start=1):
            sec_path = ch_main.parent / 'sections' / sec_rel
            if not sec_path.exists():
                continue
            sec_title = extract_section_title(sec_path)
            rows.append((chap_idx, sec_idx, ch_folder, ch_title, sec_title, str(sec_path.relative_to(ROOT))))

    out_csv = ROOT / "assets" / "tables" / "global_toc.csv"
    generate_csv(rows, out_csv)
    print(f"Found {len(chapter_mains)} chapters. Wrote {out_csv} with {len(rows)} rows.")


if __name__ == "__main__":
    main()

