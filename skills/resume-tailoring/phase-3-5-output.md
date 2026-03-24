# Phase 3-6: Output Generation

## Phase 3: LaTeX Generation & 2-Page Enforcement

**Goal:** Produce the final `resume.tex`, enforce 2-page limit, compile to PDF.

**Inputs:** Completed resume content (Phase 1 + 2) + `latex-generation.md` for structure.

### 3.1 Assemble the LaTeX File

Start from `templates/full_base_resume.tex`. Assemble sections in order:
1. **Heading** — unchanged (name, phone, email, LinkedIn, location)
2. **Career Summary** — rewritten in Phase 1.1
3. **Technical Skills** — reordered + AI/LLM skills from Phase 1.2 + 2
4. **Work Experience** — switched + injected from Phase 1.3 + 2
5. **Education** — unchanged
6. **Projects** — adjust technology mentions if relevant

### 3.2 Two-Page Enforcement (AUTO — do not ask user)

```
AFTER assembling the full .tex, CHECK page count:

IF > 2 pages:
  1. Shorten verbose bullets (tighten wording, aim for 1.5-2 lines per bullet)
  2. Consolidate near-duplicate bullets within the same role into one
  3. NEVER remove bullet points — all original bullets must be preserved
  4. Recompile and verify exactly 2 pages

IF < 2 pages:
  1. Expand bullet detail in recent roles (MicroGig, Assembli AI)
  2. Expand Technical Skills with JD-relevant technologies
  3. Add/expand project descriptions
  4. Recompile and verify exactly 2 pages

ALWAYS verify final PDF is exactly 2 pages before presenting to user.
NEVER produce a resume that is not exactly 2 pages.
```

### 3.3 LaTeX Validation (before compiling)

- All `\textbf{}` braces properly closed
- All `\begin{itemize}` have matching `\end{itemize}`
- All `\begin{tabular*}` have matching `\end{tabular*}`
- No unescaped special characters (`&`, `%`, `$`, `#`, `_`)
- `\href{}{}` links have proper URL encoding
- Em-dashes use `--` (not unicode `—`)
- Dollar amounts use `\$`

See `latex-generation.md` for the full checklist and error reference.

### 3.4 Output Folder Structure

```
resumes/{Company}_{Framework1}_{Framework2}/
├── resume.tex        → LaTeX source
├── resume.pdf        → Compiled PDF
├── resume.log        → LaTeX compilation log (keep for debugging)
├── recruiter_mail.md → Recruiter outreach email
└── run_log.md        → Tailoring summary log (changes made, switches applied)
```

**Folder naming rules:**
1. Company: PascalCase, no spaces (`"Goldman Sachs"` → `"GoldmanSachs"`)
2. Top 2-3 key frameworks from JD (`"NodeJS"`, `"SpringBoot"`, `"LLM"`)
3. Separated by underscores, no special characters

**Examples:**
```
resumes/Google_React_NodeJS/
resumes/Stripe_Python_FastAPI/
resumes/OpenAI_Python_LLM/
resumes/GoldmanSachs_Java_SpringBoot/
```

### 3.5 Compile to PDF

The output PDF is always named `Mani_Resume.pdf`.

```bash
mkdir -p ./resumes/{Company}_{Tech1}_{Tech2}

# Compile (run twice for cross-references)
pdflatex -interaction=nonstopmode -jobname=Mani_Resume \
  -output-directory=./resumes/{Company}_{Tech1}_{Tech2} \
  ./resumes/{Company}_{Tech1}_{Tech2}/resume.tex

pdflatex -interaction=nonstopmode -jobname=Mani_Resume \
  -output-directory=./resumes/{Company}_{Tech1}_{Tech2} \
  ./resumes/{Company}_{Tech1}_{Tech2}/resume.tex

# Clean aux files (keep .tex, .pdf, .log)
rm -f ./resumes/{Company}_{Tech1}_{Tech2}/Mani_Resume.aux \
      ./resumes/{Company}_{Tech1}_{Tech2}/Mani_Resume.out
```

**pdflatex is installed locally via BasicTeX (`brew install --cask basictex`).**
Path: `/Library/TeX/texbin/pdflatex` — add to PATH if not found: `export PATH=$PATH:/Library/TeX/texbin`

**Fallback if pdflatex not available:**
1. Provide `.tex` file for Overleaf (free online LaTeX editor)
2. Reinstall: `brew install --cask basictex`

### 3.6 Update Resume Index

After every successful full generation, register the new resume in the cache:

```bash
python3 scripts/cache_check.py --add "{Company}_{Tech1}_{Tech2}" "{Framework1}, {Framework2}, {Framework3}"
```

The script creates `resumes/resume_index.md` if it doesn't exist, and appends the entry.
This enables cache hits on future runs with similar tech stacks (see Phase 0, Step 0).

---

## Phase 4: Generation Report + Run Log

Write `run_log.md` in the output folder AND present the same summary to the user.

### 4.1 run_log.md format

```markdown
# Resume Tailoring Run Log

**Date:** {YYYY-MM-DD}
**Company:** {Company}
**Role:** {Job Title}
**JD URL:** {URL}
**Output Folder:** resumes/{Company}_{Tech1}_{Tech2}/

---

## Files Created

- `resume.tex` — LaTeX source
- `resume.pdf` — Compiled PDF (exactly 2 pages)
- `resume.log` — LaTeX compilation log
- `recruiter_mail.md` — Recruiter outreach email
- `run_log.md` — This file

---

## JD Tech Stack Detected

- **Primary Backend:** {detected}
- **Frontend:** {detected}
- **Cloud:** {detected}
- **Databases:** {detected}
- **AI/ML:** {detected or "None"}
- **Years:** {JD requirement} → {applied value}

---

## Changes Made

### Career Summary
- Years: {value}
- Primary stack: {stack}
- Key framing: {1-line summary}

### Technical Skills
- {row}: {what changed}
- All {N} skill rows preserved

### Experience (ALL bullets preserved — {N} total)

| Role | Switch Applied |
|---|---|
| {Role} | {what switched or "No change"} |
...

### Projects
- {what changed or "No change"}

### No Changes
- Company names, dates, job titles, metrics
- Education section

---

## Cache
- Registered: `{folder}` → {frameworks}
```

### 4.2 Present to user

After writing run_log.md, show the user the same content as a summary.

---

## Phase 5: Recruiter Email Generation

**Goal:** Write `recruiter_mail.md` — a short, human-sounding outreach email.

### 5.0 Candidate Background (use naturally, don't force)

Weave in whichever of these fits the target company/role:
- **0-to-1 startup experience** — built core platform at Assembli AI from the ground up (early-stage, wore many hats, shipped fast)
- **Fintech experience** — worked at Synchrony Financial on production financial systems, compliance-aware, high-stakes data
- **Enterprise-scale systems** — built distributed microservices architecture (150+ services) for a Fortune 500 financial client, real-time transactions, vendor onboarding

Pick the one that resonates most with the target company:
- Startup/growth-stage company → lead with Assembli AI (0-1 startup)
- Fintech/banking/payments → lead with Synchrony (fintech production systems)
- Enterprise/scale → lead with enterprise client work (150+ microservices)

**IMPORTANT:** Never mention "MicroGig" in the email — it's a staffing firm. Refer to the actual work as "a Fortune 500 financial client" or "an enterprise financial services client" instead.

### 5.1 Brief Company Research

Do a quick search for ONE specific thing:
- A recent product launch, funding round, or news item
- A specific team/project mentioned in the JD
- A company mission or product that genuinely resonates

One natural line. Not a marketing paragraph. Takes < 30 seconds.

### 5.2 Writing Rules (Human, Not AI)

```
MANDATORY:
1. SHORT — 5-7 sentences max
2. NO BUZZWORDS — no "passionate", "leverage", "synergy", "thrilled"
3. NO FILLER — no "I hope this finds you well", "I wanted to reach out"
4. VARY SENTENCE LENGTH — short. Then longer ones. Mix it up.
5. BE SPECIFIC — cite one real achievement from the tailored resume
6. ONE COMPANY LINE — show you looked them up, not sycophantically
7. NO COVER LETTER TONE — no "Dear Hiring Manager" or "Sincerely"
8. SIMPLE CLOSING — "Would love to chat" not "I welcome the opportunity"
9. FIRST PERSON IS FINE — don't avoid "I"
10. READ IT ALOUD — if it sounds AI-written, rewrite it
```

**Anti-AI Checklist — verify NONE of these appear:**
```
✘ "I'm excited about" / "I'm passionate about"
✘ "leverage my experience"
✘ "proven track record"
✘ "results-driven" / "detail-oriented"
✘ "I believe I would be a great fit"
✘ "I hope this message finds you well"
✘ "I wanted to reach out regarding"
✘ "unique opportunity" / "exciting role"
✘ Em-dash overuse (—)
✘ Every sentence starting with "I"
✘ Three-part lists (rule of three)
✘ All sentences the same length
✘ "I look forward to hearing from you"
```

### 5.3 Email Template

```markdown
# Recruiter Email

Subject: {Role} — {One-line hook}

---

Hi {Recruiter/Team},

{1-2 sentences: why you're reaching out + one specific company detail}

{2-3 sentences: what you bring that maps to their JD — cite real work/metrics}

{1 sentence: simple ask}

Best,
Mani Sreekar
```

**Example — fintech company (lead with Synchrony):**
```markdown
# Recruiter Email

Subject: Backend Engineer — Built payment systems at Synchrony

---

Hi,

Saw the backend role at Stripe. The bit about building payment
infrastructure that handles millions of transactions caught my eye.

I spent two years at Synchrony Financial building financial data
pipelines and compliance-grade APIs. More recently I've been running
150+ microservices handling real-time transactions for a large
financial services client. Shipped a Redis caching layer that cut
DB load by 40%.

Would love to chat if the team's still hiring.

Best,
Mani Sreekar
```

**Example — startup (lead with Assembli AI 0-1):**
```markdown
# Recruiter Email

Subject: Full-Stack Engineer — Built a product from scratch

---

Hi,

Saw the engineering role at {Startup}. Building {their product area}
from the ground up is basically what I just did.

I joined Assembli AI as one of the first engineers and built the core
platform from zero — RAG pipelines, AI agent workflows, the whole
stack. Before that I was scaling distributed systems for an enterprise
financial client across microservices.

Happy to share more if there's interest.

Best,
Mani Sreekar
```

Save as `recruiter_mail.md` in `resumes/{Company}_{Frameworks}/`.

---

## Phase 6: Iteration (Conditional)

If user requests revisions:

```
"What would you like to adjust?

1. Different framework emphasis
2. Add/remove injected skills
3. Change bullet phrasing
4. Adjust Career Summary focus
5. Change skill ordering"
```

Apply changes → Regenerate LaTeX → Recompile PDF → Verify 2 pages → Present again.
