---
name: resume-tailoring
description: Use when creating tailored resumes for job applications - analyzes JD tech stack, switches frameworks (Java↔Node.js↔Python), injects missing skills (Redis, Terraform, AI/LLM, etc.), dynamically adjusts years of experience, enforces 2-page limit, supports multi-job batch processing, and generates LaTeX PDF + recruiter email output
---

# Resume Tailoring Skill

## Overview

Generates JD-tailored resumes by **switching the technology stack**, **injecting missing skills** (including AI/LLM/Agentic), and **dynamically adjusting years of experience**. Output is a **LaTeX-compiled PDF** saved in `resumes/{Company}_{Frameworks}/`. **The final resume MUST always be exactly 2 pages.**

**Core Principle:** Truth-preserving — the user has genuine experience across multiple stacks. Emphasize the stack most relevant to the JD while preserving all factual achievements and metrics. Never fabricate.

## Hard Constraints

> ⚠️ **The final resume MUST be exactly 2 pages. Never 1, never 3+.**
> If over 2 pages: shorten verbose bullets, tighten spacing — do NOT remove bullets.
> Verify page count after every compilation.

> ⚠️ **Never remove existing bullet points. All original bullets must be preserved.**
> The primary change is framework switching within bullets. Do not prune bullets for space.

> ⚠️ **Never change company names, dates, job titles, or metrics.**

> ⚠️ **Years of experience: minimum 4, maximum 7+. Match JD requirement.**

## When to Use

- User provides a JD and wants a tailored resume
- User provides multiple JDs for batch processing
- User wants resume reframed for a different stack (e.g., Node.js vs Java)
- User needs missing skills added based on JD (Redis, Terraform, AI/LLM, etc.)

**Do NOT use for:** cover letters, LinkedIn optimization, resumes from scratch.

## File Map — READ IN ORDER

The workflow is split across focused files. Read only what you need for the current phase:

| File | When to Read | Content |
|---|---|---|
| **SKILL.md** (this file) | Always first | Overview, constraints, quick start |
| `phase-0-analysis.md` | Start of every run | Cache check + JD parsing, stack detection, tailoring plan |
| `phase-1-2-tailoring.md` | After Phase 0 approval | Framework switching + skill injection (incl. AI/LLM) |
| `framework-switching.md` | During Phase 1-2 | Switching tables, injection templates, career summary template |
| `phase-3-5-output.md` | After Phase 2 | LaTeX generation, structure, 2-page enforcement, recruiter email |
| `errors-examples-tests.md` | On errors or edge cases | Error handling, usage examples, test cases |
| `multi-job-workflow.md` | When batch mode detected | Multi-job batch workflow (uses batch_manager.py) |
| **Scripts — execute, never read:** | | |
| `scripts/cache_check.py` | Phase 0 cache check | Resume cache checker |
| `scripts/jd_analyzer.py` | Phase 0 JD analysis | Tech stack detection from JD text |
| `scripts/compile_resume.py` | Phase 3 compilation | LaTeX → PDF + page count verification |
| `scripts/batch_manager.py` | Multi-job batches | Batch state CRUD (init, add-job, status, complete) |

## Performance Optimization

1. **Read base LaTeX template ONCE** at start — keep in working memory
2. **Single-pass JD analysis** — extract stack + years + missing skills simultaneously
3. **Single-pass bullet switching** — don't loop over bullets multiple times
4. **Validate LaTeX syntax BEFORE compile** — catch errors early
5. **Compile PDF once** (twice max for cross-refs)
6. **Present tailoring plan concisely** — bullet points only, let user ask for detail

## Quick Start

**Required from user:** Job description (text or URL)

**Execution order:**
```
0. Read phase-0-analysis.md → Step 0: check resume_index.md for cache hit
   → If ≥90% framework match: skip to step 3 (reuse .tex, just compile + email)
1. Read phase-0-analysis.md → full JD analysis, detect stack, present plan, get approval
2. Read phase-1-2-tailoring.md + framework-switching.md → switch + inject
3. Read phase-3-5-output.md → generate LaTeX, compile PDF, write email
4. Update resumes/resume_index.md → append new entry for future cache hits
5. Present output to user
```

**If multiple JDs detected:** Read `multi-job-workflow.md` instead of running single-job flow.

**If errors occur:** Read `errors-examples-tests.md` for edge case handling.

## Output Structure

```
resumes/
├── resume_index.md   ← framework cache (lookup before every run)
└── {Company}_{Framework1}_{Framework2}/
    ├── resume.tex        ← LaTeX source
    ├── Mani_Resume.pdf   ← Compiled PDF (always this name, exactly 2 pages)
    ├── Mani_Resume.log   ← LaTeX compilation log
    ├── recruiter_mail.md ← Human-written outreach email
    └── run_log.md        ← Tailoring summary (what changed, switches applied)
```

Folder naming: `PascalCaseCompany_TopFramework_SecondFramework`
Examples: `Google_React_NodeJS/`, `OpenAI_Python_LLM/`, `GoldmanSachs_Java_SpringBoot/`
