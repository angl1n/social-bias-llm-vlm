#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sort Markdown tables by a 'Date' column (descending by default).
- Works well for GitHub-flavored Markdown tables.
- Assumes no unescaped '|' inside a cell. (Common in README tables.)
"""

from __future__ import annotations
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple


DATE_COL_CANDIDATES = {"date", "time", "published", "pub date", "release", "year"}


def _split_md_row(line: str) -> List[str]:
    """
    Split a Markdown table row into cells.
    Removes leading/trailing pipe and strips spaces.
    """
    s = line.strip()
    if not s.startswith("|"):
        return []
    # remove leading/trailing pipes for clean split
    s = s.strip().strip("|")
    return [c.strip() for c in s.split("|")]


def _is_separator_row(line: str) -> bool:
    """
    Check if line is like: | :--- | :---: | ---: |
    """
    s = line.strip()
    if not s.startswith("|"):
        return False
    # allow colons, dashes, spaces, pipes
    return bool(re.fullmatch(r"\|\s*[:\-|\s]+\s*\|", s))


def _parse_date(s: str) -> Tuple[int, int, int]:
    """
    Parse date strings like YYYY, YYYY-MM, YYYY-MM-DD.
    Returns (year, month, day). Missing month/day default to 1.
    Unparseable dates return (0,0,0) so they sink to bottom.
    """
    t = s.strip()
    # pick the first YYYY(-MM(-DD)) pattern inside the cell
    m = re.search(r"\b(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?\b", t)
    if not m:
        return (0, 0, 0)
    y = int(m.group(1))
    mo = int(m.group(2)) if m.group(2) else 1
    d = int(m.group(3)) if m.group(3) else 1
    # basic sanity
    if not (1 <= mo <= 12 and 1 <= d <= 31):
        return (0, 0, 0)
    return (y, mo, d)


@dataclass
class TableBlock:
    start: int
    end: int  # inclusive
    lines: List[str]


def _find_tables(lines: List[str]) -> List[TableBlock]:
    """
    Identify Markdown tables:
    header row + separator row + data rows (>=0), contiguous.
    """
    tables: List[TableBlock] = []
    i = 0
    n = len(lines)

    while i < n - 1:
        if lines[i].lstrip().startswith("|") and _is_separator_row(lines[i + 1]):
            # capture contiguous table rows starting at i
            start = i
            j = i + 2
            while j < n and lines[j].lstrip().startswith("|") and lines[j].strip() != "|":
                j += 1
            end = j - 1
            tables.append(TableBlock(start=start, end=end, lines=lines[start : end + 1]))
            i = j
        else:
            i += 1
    return tables


def _sort_table_block(tb: TableBlock, descending: bool = True) -> List[str]:
    """
    Sort a table block by 'Date' column if present.
    Keep header + separator intact.
    """
    if len(tb.lines) < 2:
        return tb.lines

    header = tb.lines[0]
    sep = tb.lines[1]
    rows = tb.lines[2:]

    headers = [h.lower() for h in _split_md_row(header)]
    if not headers:
        return tb.lines

    # find date column index
    date_idx: Optional[int] = None
    for k, name in enumerate(headers):
        if name in DATE_COL_CANDIDATES or "date" == name:
            date_idx = k
            break
    if date_idx is None:
        # also allow "Date" exact match (already covered), or headers containing "date"
        for k, name in enumerate(headers):
            if "date" in name:
                date_idx = k
                break

    if date_idx is None or not rows:
        return tb.lines

    parsed_rows = []
    for r in rows:
        cells = _split_md_row(r)
        date_cell = cells[date_idx] if date_idx < len(cells) else ""
        key = _parse_date(date_cell)
        parsed_rows.append((key, r))

    parsed_rows.sort(key=lambda x: x[0], reverse=descending)
    return [header, sep] + [r for _, r in parsed_rows]


def sort_markdown_tables(text: str, descending: bool = True) -> str:
    lines = text.splitlines(keepends=False)
    tables = _find_tables(lines)
    if not tables:
        return text

    # apply edits from bottom to top to keep indices valid
    for tb in reversed(tables):
        new_block = _sort_table_block(tb, descending=descending)
        lines[tb.start : tb.end + 1] = new_block

    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=str, help="Markdown file (e.g., README.md)")
    ap.add_argument("--asc", action="store_true", help="Sort ascending (default: descending/newest first)")
    ap.add_argument("--check", action="store_true", help="Exit non-zero if file would change")
    args = ap.parse_args()

    p = Path(args.path)
    original = p.read_text(encoding="utf-8")
    sorted_text = sort_markdown_tables(original, descending=not args.asc)

    if args.check:
        if sorted_text != original:
            print(f"[FAIL] {p} is not sorted by Date.")
            sys.exit(1)
        print(f"[OK] {p} already sorted.")
        return

    if sorted_text != original:
        p.write_text(sorted_text, encoding="utf-8")
        print(f"[UPDATED] Sorted tables in {p}")
    else:
        print(f"[NOOP] No changes for {p}")


if __name__ == "__main__":
    main()