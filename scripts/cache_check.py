#!/usr/bin/env python3
"""
Resume cache checker — deterministic framework matching against resume_index.md.

Usage:
  Check cache:   python scripts/cache_check.py "React, Node.js, TypeScript"
  Add entry:     python scripts/cache_check.py --add "Google_React_NodeJS" "React, Node.js, GraphQL, TypeScript"
  List all:      python scripts/cache_check.py --list

Output (check):
  CACHE_HIT|FolderName|MatchPercent|MatchedFrameworks|MissingFrameworks
  NO_MATCH

Output (add):
  ADDED|FolderName
  EXISTS|FolderName  (if folder already in index)
"""

import sys
import os
import re

INDEX_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resumes", "resume_index.md")
MATCH_THRESHOLD = 90  # percent


def normalize(framework: str) -> str:
    """Normalize framework name for comparison."""
    return framework.strip().lower().replace(".", "").replace("-", "").replace(" ", "")


def parse_index() -> dict[str, set[str]]:
    """Read resume_index.md and return {folder: set(normalized_frameworks)}."""
    entries = {}
    if not os.path.exists(INDEX_PATH):
        return entries

    with open(INDEX_PATH, "r") as f:
        for line in f:
            line = line.strip()
            # Match table rows: | FolderName | Framework1, Framework2, ... |
            match = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", line)
            if match:
                folder = match.group(1).strip()
                frameworks_raw = match.group(2).strip()
                # Skip header rows
                if folder.startswith("-") or folder == "Folder":
                    continue
                frameworks = {normalize(f) for f in frameworks_raw.split(",")}
                entries[folder] = frameworks
    return entries


def check_cache(jd_frameworks_raw: str) -> None:
    """Check if any existing resume matches ≥90% of the given frameworks."""
    jd_frameworks = {normalize(f) for f in jd_frameworks_raw.split(",")}
    if not jd_frameworks:
        print("NO_MATCH")
        return

    entries = parse_index()
    if not entries:
        print("NO_MATCH")
        return

    best_folder = None
    best_pct = 0
    best_matched = set()
    best_missing = set()

    for folder, cached_frameworks in entries.items():
        matched = jd_frameworks & cached_frameworks
        pct = int((len(matched) / len(jd_frameworks)) * 100) if jd_frameworks else 0

        if pct > best_pct:
            best_pct = pct
            best_folder = folder
            best_matched = matched
            best_missing = jd_frameworks - cached_frameworks

    if best_pct >= MATCH_THRESHOLD and best_folder:
        # Reverse-normalize for display: find original names from raw input
        raw_list = [f.strip() for f in jd_frameworks_raw.split(",")]
        matched_display = [f for f in raw_list if normalize(f) in best_matched]
        missing_display = [f for f in raw_list if normalize(f) in best_missing]

        print(f"CACHE_HIT|{best_folder}|{best_pct}|{','.join(matched_display)}|{','.join(missing_display)}")
    else:
        print("NO_MATCH")


def add_entry(folder_name: str, frameworks_raw: str) -> None:
    """Add a new entry to resume_index.md."""
    entries = parse_index()

    if folder_name in entries:
        print(f"EXISTS|{folder_name}")
        return

    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)

    # Create file with header if it doesn't exist
    if not os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, "w") as f:
            f.write("# Resume Index\n\n")
            f.write("| Folder | Frameworks |\n")
            f.write("|--------|------------|\n")

    # Append new row
    with open(INDEX_PATH, "a") as f:
        f.write(f"| {folder_name} | {frameworks_raw.strip()} |\n")

    print(f"ADDED|{folder_name}")


def list_entries() -> None:
    """List all entries in the index."""
    entries = parse_index()
    if not entries:
        print("EMPTY")
        return
    for folder, frameworks in entries.items():
        print(f"{folder}|{','.join(sorted(frameworks))}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print('  Check:  python scripts/cache_check.py "React, Node.js, TypeScript"')
        print('  Add:    python scripts/cache_check.py --add "FolderName" "React, Node.js"')
        print("  List:   python scripts/cache_check.py --list")
        sys.exit(1)

    if sys.argv[1] == "--add":
        if len(sys.argv) < 4:
            print("Error: --add requires folder_name and frameworks")
            sys.exit(1)
        add_entry(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "--list":
        list_entries()
    else:
        check_cache(sys.argv[1])


if __name__ == "__main__":
    main()
