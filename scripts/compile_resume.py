#!/usr/bin/env python3
"""
LaTeX resume compiler — handles pdflatex invocation, cleanup, and page count verification.

Usage:
  Compile:     python3 scripts/compile_resume.py resumes/Google_React_NodeJS/resume.tex
  Check pages: python3 scripts/compile_resume.py --pages resumes/Google_React_NodeJS/Mani_Resume.pdf

Output (compile):
  COMPILED|/path/to/Mani_Resume.pdf|2 pages
  ERROR|{error description}

Output (pages):
  PAGES|2
  PAGES|3  ← means 2-page enforcement needed
"""

import sys
import os
import subprocess
import shutil
import re


def find_pdflatex() -> str | None:
    """Find pdflatex binary — check PATH first, then common macOS locations."""
    result = shutil.which("pdflatex")
    if result:
        return result

    common_paths = [
        "/Library/TeX/texbin/pdflatex",
        "/usr/local/texlive/2024/bin/universal-darwin/pdflatex",
        "/usr/local/texlive/2023/bin/universal-darwin/pdflatex",
    ]
    for p in common_paths:
        if os.path.isfile(p):
            return p

    return None


def count_pages(pdf_path: str) -> int:
    """Count pages in a PDF by scanning for /Type /Page entries."""
    try:
        with open(pdf_path, "rb") as f:
            content = f.read()
        # Count page objects (not PageS which is the pages tree)
        count = len(re.findall(rb"/Type\s*/Page(?!s)", content))
        return count if count > 0 else -1
    except Exception:
        return -1


def compile_resume(tex_path: str) -> None:
    """Compile .tex to PDF via pdflatex (2 passes), cleanup aux files, verify pages."""
    tex_path = os.path.abspath(tex_path)

    if not os.path.isfile(tex_path):
        print(f"ERROR|File not found: {tex_path}")
        sys.exit(1)

    if not tex_path.endswith(".tex"):
        print(f"ERROR|Not a .tex file: {tex_path}")
        sys.exit(1)

    pdflatex = find_pdflatex()
    if not pdflatex:
        print("ERROR|pdflatex not found. Install: brew install --cask basictex")
        print("HINT|Add to PATH: export PATH=$PATH:/Library/TeX/texbin")
        print("HINT|Or use Overleaf (free online LaTeX editor) with the .tex file")
        sys.exit(1)

    output_dir = os.path.dirname(tex_path)
    jobname = "Mani_Resume"

    cmd = [
        pdflatex,
        "-interaction=nonstopmode",
        f"-jobname={jobname}",
        f"-output-directory={output_dir}",
        tex_path,
    ]

    # Run twice for cross-references
    for pass_num in (1, 2):
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            # Extract first meaningful error from log
            error_lines = []
            for line in result.stdout.split("\n"):
                if line.startswith("!") or "Error" in line:
                    error_lines.append(line.strip())
                    if len(error_lines) >= 3:
                        break

            error_msg = "; ".join(error_lines) if error_lines else "Unknown compilation error"
            log_path = os.path.join(output_dir, f"{jobname}.log")
            print(f"ERROR|Pass {pass_num} failed: {error_msg}")
            print(f"LOG|{log_path}")
            sys.exit(1)

    # Cleanup aux files (keep .pdf, .log, .tex)
    for ext in (".aux", ".out"):
        aux_file = os.path.join(output_dir, f"{jobname}{ext}")
        if os.path.exists(aux_file):
            os.remove(aux_file)

    # Verify output PDF exists and count pages
    pdf_path = os.path.join(output_dir, f"{jobname}.pdf")
    if not os.path.isfile(pdf_path):
        print("ERROR|PDF not generated despite successful compilation")
        sys.exit(1)

    pages = count_pages(pdf_path)
    print(f"COMPILED|{pdf_path}|{pages} pages")

    if pages != 2:
        print(f"WARNING|Resume is {pages} pages — must be exactly 2. Adjust content and recompile.")


def check_pages(pdf_path: str) -> None:
    """Just count pages in an existing PDF."""
    pdf_path = os.path.abspath(pdf_path)
    if not os.path.isfile(pdf_path):
        print(f"ERROR|File not found: {pdf_path}")
        sys.exit(1)
    pages = count_pages(pdf_path)
    print(f"PAGES|{pages}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Compile:  python3 scripts/compile_resume.py path/to/resume.tex")
        print("  Pages:    python3 scripts/compile_resume.py --pages path/to/resume.pdf")
        sys.exit(1)

    if sys.argv[1] == "--pages":
        if len(sys.argv) < 3:
            print("ERROR|Provide PDF path")
            sys.exit(1)
        check_pages(sys.argv[2])
    else:
        compile_resume(sys.argv[1])


if __name__ == "__main__":
    main()
