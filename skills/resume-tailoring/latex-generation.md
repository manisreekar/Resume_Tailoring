# LaTeX Resume Generation Guide

## Overview

All resume output is generated as **LaTeX (.tex)** files and compiled to **PDF** using `pdflatex`. This replaces DOCX/Markdown generation as the primary output format.

## LaTeX Template Structure

The base template is located at: `skills/resume-tailoring/templates/full_base_resume.tex`

This template uses these LaTeX packages:
- `fullpage`, `titlesec` - Layout and section formatting
- `enumitem` - Custom list formatting  
- `hyperref` - Clickable links
- `fontawesome5` - Icons
- `xcolor` - Color support
- `fancyhdr` - Header/footer control

## Custom Commands Reference

### Resume Subheading (Work Experience)
```latex
\resumeSubheading{Title, Company}{Location}{}{Dates}
```
Example:
```latex
\resumeSubheading{Senior Software Engineer, MicroGig}{Dallas, TX}
{}{Sep 2025 -- Present}
```

### Education Heading
```latex
\resumeEduHeading{University}{Location}{Degree; GPA}{Dates}
```

### Bullet Points
Use `\textbulletlight` label with `\textbf{}` for emphasis:
```latex
\item \small Developed \textbf{Node.js/Express backend} and integrated with...
```

## Section Assembly Rules

### Career Summary Section
```latex
\section{Career Summary}
\small{Full-Stack and AI Engineer with \textbf{5 years}...}
```

### Technical Skills Section
```latex
\section{Technical Skills}
\begin{tabular*}{\textwidth}{@{}p{0.27\textwidth}@{\hspace{1pt}}p{0.73\textwidth}@{}}
\textbf{Category Name} & Skill1, Skill2, Skill3 \\
...
\end{tabular*}
```

### Work Experience Section  
Each role follows this pattern:
```latex
\begin{itemize}[leftmargin=0pt, rightmargin=0pt, label={}, itemsep=0pt]
    \resumeSubheading{Title, Company}{Location}
    {}{Dates}
\end{itemize}\vspace{-6pt}
\begin{itemize}[leftmargin=12pt, rightmargin=0pt, label={\textbulletlight}, itemsep=0pt, topsep=2pt]
        \item \small Bullet point text with \textbf{bold keywords}...
        \item Another bullet...
\end{itemize}
```

### Projects Section
```latex
\begin{itemize}[leftmargin=0pt, label={}, itemsep=0pt, parsep=0pt, font=\normalfont]
\item {\small \textbf{Project Title: Technologies}}
\end{itemize}\vspace{-6pt}
\begin{itemize}[leftmargin=12pt, labelsep=1pt, label={\textbulletlight}, itemsep=0pt, topsep=2pt]
        \item \small Description of the project...
\end{itemize}
```

## PDF Compilation

### Output Directory Structure

All output goes into `resumes/{Company}_{Framework1}_{Framework2}/`:

```
resumes/Google_React_NodeJS/
├── resume.tex              → LaTeX source
├── Mani_Resume.pdf         → Compiled PDF (always this name)
├── Mani_Resume.log         → LaTeX compilation log
├── recruiter_mail.md       → Recruiter outreach email
└── run_log.md              → Tailoring summary log
```

**Folder naming rules:**
1. Company name in PascalCase ("Goldman Sachs" → "GoldmanSachs")
2. Top 2-3 key frameworks from JD ("NodeJS", "React", "Python", "LLM")
3. Separated by underscores, no special characters

### Method 1: pdflatex (Preferred — installed locally via BasicTeX)

The output PDF is always named `Mani_Resume.pdf` using `-jobname=Mani_Resume`.

```bash
# Create output directory
mkdir -p ./resumes/{Company}_{Tech1}_{Tech2}

# Compile (run twice for cross-references)
pdflatex -interaction=nonstopmode -jobname=Mani_Resume \
  -output-directory=./resumes/{Company}_{Tech1}_{Tech2} \
  ./resumes/{Company}_{Tech1}_{Tech2}/resume.tex

pdflatex -interaction=nonstopmode -jobname=Mani_Resume \
  -output-directory=./resumes/{Company}_{Tech1}_{Tech2} \
  ./resumes/{Company}_{Tech1}_{Tech2}/resume.tex

# Cleanup aux files
rm -f ./resumes/{Company}_{Tech1}_{Tech2}/Mani_Resume.aux \
      ./resumes/{Company}_{Tech1}_{Tech2}/Mani_Resume.out
```

If `pdflatex` is not on PATH, use full path: `/Library/TeX/texbin/pdflatex`
To add permanently: `export PATH=$PATH:/Library/TeX/texbin` in `~/.zshrc`

### Method 2: latexmk (Alternative)
```bash
latexmk -pdf -jobname=Mani_Resume -outdir=./resumes/{Company}_{Tech1}_{Tech2} \
  ./resumes/{Company}_{Tech1}_{Tech2}/resume.tex
```

### Cleanup after compilation
```bash
rm -f ./resumes/{Company}_{Tech1}_{Tech2}/Mani_Resume.aux \
      ./resumes/{Company}_{Tech1}_{Tech2}/Mani_Resume.out
```

> **IMPORTANT:** Keep `Mani_Resume.log` — useful for debugging. Keep `Mani_Resume.pdf` and `resume.tex`.

## LaTeX Special Character Escaping

When inserting dynamic content into LaTeX, these characters MUST be escaped:

| Character | LaTeX Escape |
|---|---|
| `&` | `\&` |
| `%` | `\%` |
| `$` | `\$` |
| `#` | `\#` |
| `_` | `\_` |
| `{` | `\{` |
| `}` | `\}` |
| `~` | `\textasciitilde` |
| `^` | `\textasciicircum` |
| `\` | `\textbackslash` |

**IMPORTANT:** The template already uses `$` for math mode separators (`$|$`). Do not escape those.

## File Naming Convention

All output is organized per-company under the `resumes/` root directory:

```
resumes/{Company}_{Framework1}_{Framework2}/
├── resume.tex              → LaTeX source
├── resume.pdf              → Compiled PDF
├── resume.log              → Compilation log (keep for debugging)
└── recruiter_mail.md       → Recruiter outreach email
```

**Folder naming examples:**
```
resumes/Google_React_NodeJS/
resumes/Stripe_Python_FastAPI/
resumes/OpenAI_Python_LLM/
resumes/GoldmanSachs_Java_SpringBoot/
resumes/Meta_React_NodeJS/
```

**Folder naming rules:**
1. Company: PascalCase, no spaces ("Goldman Sachs" → "GoldmanSachs")
2. Frameworks: top 2-3 from JD, short names ("NodeJS", "SpringBoot", "LLM")
3. Separator: underscore between each part
4. No special characters

## Compilation Checklist

Before compiling, verify:
- [ ] All `\textbf{}` braces are properly closed
- [ ] No unescaped special characters in dynamic content
- [ ] All `\begin{itemize}` have matching `\end{itemize}`
- [ ] All `\begin{tabular*}` have matching `\end{tabular*}`
- [ ] No orphaned `\\` at end of last table row (causes errors)
- [ ] `\href{}{}` links have proper URL encoding
- [ ] Em-dashes use `--` (not unicode `—`)
- [ ] Dollar amounts use `\$` (not bare `$`)

## Error Handling

### Common LaTeX Compilation Errors

1. **Missing `}` or `$`**: Check all braces/math delimiters are paired
2. **Undefined control sequence**: Usually a typo in command name
3. **Package conflict**: `hyperref` should be loaded last
4. **Overfull hbox**: Content too wide — shorten text or adjust margins
5. **Font not found**: Ensure `fontawesome5` package is installed

### Fallback Strategy
If `pdflatex` is not available:
1. Try Docker-based compilation
2. Provide the `.tex` file to the user with instructions to compile on Overleaf (free online LaTeX editor)
3. As last resort, suggest user install TeX Live: `brew install --cask mactex-no-gui`
