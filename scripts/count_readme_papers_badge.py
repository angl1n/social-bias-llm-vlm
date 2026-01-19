#!/usr/bin/env python3
from __future__ import annotations
import json
import re
from pathlib import Path

def count_papers_in_readme(readme_path: str = "README.md") -> int:
    text = Path(readme_path).read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()

    table_row_re = re.compile(r"^\s*\|")
    separator_re = re.compile(r"^\s*\|[\s:\-|\+]+\|\s*$")

    in_table = False
    table_rows = []
    total = 0

    def flush_table():
        nonlocal in_table, table_rows, total
        if not in_table or not table_rows:
            in_table = False
            table_rows = []
            return

        cleaned = [r for r in table_rows if table_row_re.match(r)]
        cleaned = [r for r in cleaned if not separator_re.match(r)]

        # Heuristic: first non-separator row is header; count rest as papers
        if cleaned:
            total += max(0, len(cleaned) - 1)

        in_table = False
        table_rows = []

    for line in lines:
        if table_row_re.match(line):
            in_table = True
            table_rows.append(line)
        else:
            flush_table()

    flush_table()
    return total

def write_badge_json(total: int, out_path: str = "badges/papers.json"):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schemaVersion": 1,
        "label": "papers",
        "message": str(total),
        "color": "blue",
    }
    Path(out_path).write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    total = count_papers_in_readme("README.md")
    write_badge_json(total, "badges/papers.json")
    print(f"TOTAL papers: {total} -> badges/papers.json")