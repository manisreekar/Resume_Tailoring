# Resume Tailoring Skill

> AI-powered resume tailoring that switches tech stacks, injects missing skills (including AI/LLM), dynamically adjusts years of experience, enforces 2-page limits, and generates professional LaTeX PDFs — with multi-job batch support.

**Mission:** Your ability to get a job should be based on your experiences and capabilities, not on your resume writing skills.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

This skill generates high-quality, tailored resumes optimized for specific job descriptions. It goes beyond simple keyword matching by:

- **Tech Stack Switching:** Automatically switches backend frameworks (Java ↔ Node.js ↔ Python) to match JD requirements
- **Skill Injection:** Adds experience points for missing technologies (Redis, Terraform, GraphQL, AI/LLM, etc.)
- **AI/LLM Enhancement:** Injects AI agent, RAG, LLM, and prompt engineering experience when JDs require it
- **Dynamic Years:** Adjusts years of experience in Career Summary to match JD (minimum 4, scales up)
- **2-Page Enforcement:** Strict 2-page limit — automatically prunes or expands to fit exactly 2 pages
- **LaTeX PDF Output:** Generates professional resumes from LaTeX templates compiled to PDF
- **Multi-Job Batch Processing:** Process 3-5 similar jobs efficiently in batch mode
- **Recruiter Email:** Auto-generates a short, human-sounding outreach email per job
- **Self-Improving:** Library grows with each successful resume

## Installation

### Option 1: Install from GitHub (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/manisreekar/resume-tailoring-skill.git ~/.claude/skills/resume-tailoring
   ```

2. **Verify installation:**
   ```bash
   ls ~/.claude/skills/resume-tailoring/skills/resume-tailoring/
   ```
   You should see: `SKILL.md`, `framework-switching.md`, `latex-generation.md`, `templates/`

3. **Restart Claude Code** (if already running)

### Option 2: Manual Installation

1. **Create the skill directory:**
   ```bash
   mkdir -p ~/.claude/skills/resume-tailoring
   ```

2. **Download the files:**
   - Download all files from this repository
   - Place them in `~/.claude/skills/resume-tailoring/`

3. **Verify installation:**
   - Open Claude Code
   - Type `/skills` to see available skills
   - `resume-tailoring` should appear in the list

## Prerequisites

**Required:**
- Claude Code with skills enabled
- Base LaTeX resume template (included in `skills/resume-tailoring/templates/`)
- `pdflatex` for PDF compilation (or Overleaf as fallback)

**Optional but Recommended:**
- WebSearch capability (for company research)
- Docker with `texlive/texlive` image (alternative LaTeX compilation)
- Multiple existing resumes for richer library

**LaTeX Setup (macOS):**
```bash
# Install TeX Live (for pdflatex)
brew install --cask mactex-no-gui

# Or use Docker instead
docker pull texlive/texlive:latest
```

## Quick Start

### Single Job Application
**1. Invoke the skill:**
```
"I want to apply for [Role] at [Company]. Here's the JD: [paste job description]"
```

**2. The skill will automatically:**
1. Analyze JD → detect tech stack, years requirement, missing skills
2. Switch all framework references to match JD (Java → Node.js, etc.)
3. Inject missing skills (Redis, Terraform, AI/LLM, etc.)
4. Adjust years of experience in Career Summary
5. Generate LaTeX → compile to PDF (exactly 2 pages)
6. Generate recruiter outreach email
7. Present output

**3. Review and approve:**
- Checkpoints at key decision points
- Full transparency on all changes made
- Option to revise at each stage

### Multiple Jobs (Batch Mode)
**1. Provide multiple job descriptions:**
```
"I want to apply for these 3 roles:
1. [Company 1] - [Role]: [JD or URL]
2. [Company 2] - [Role]: [JD or URL]
3. [Company 3] - [Role]: [JD or URL]"
```

**2. The skill will:**
1. Detect multi-job intent and offer batch mode
2. Analyze gaps across ALL jobs (deduplicates common requirements)
3. Process each job individually (research + stack switching + skill injection)
4. Generate each resume as LaTeX → PDF (exactly 2 pages each)
5. Generate recruiter email for each job
6. Present all resumes for batch review

**3. Time savings:**
- Shared gap analysis (deduplicate once, not 3-5 times)
- 11-27% faster than processing jobs sequentially
- Same quality as single-job mode

## Files

### Core Implementation
- `skills/resume-tailoring/SKILL.md` — Entry point: overview, constraints, file routing map
- `skills/resume-tailoring/phase-0-analysis.md` — Phase 0: JD parsing, stack detection, tailoring plan
- `skills/resume-tailoring/phase-1-2-tailoring.md` — Phase 1-2: Framework switching + skill injection (incl. AI/LLM)
- `skills/resume-tailoring/phase-3-5-output.md` — Phase 3-6: LaTeX generation, 2-page enforcement, recruiter email
- `skills/resume-tailoring/errors-examples-tests.md` — Error handling, usage examples, test cases
- `skills/resume-tailoring/framework-switching.md` — Switching tables, injection templates, career summary template
- `skills/resume-tailoring/latex-generation.md` — LaTeX structure, compilation commands, error reference
- `skills/resume-tailoring/templates/full_base_resume.tex` — Master base LaTeX resume
- `skills/resume-tailoring/templates/base_resume.tex` — Template with section placeholders

### Supporting Files
- `multi-job-workflow.md` — Complete multi-job batch processing workflow

### Documentation
- `README.md` — This file
- `LICENSE` — MIT License

## Key Features

**🔄 Tech Stack Switching**
- Detects JD's primary tech stack (Node.js, Python, Java, etc.)
- Switches ALL framework references across Career Summary, Skills, and Experience
- Adjusts testing tools (JUnit → Jest), build tools (Maven → npm), ORMs (Hibernate → Prisma)
- Preserves all achievements and metrics — only tool names change

**🤖 AI/LLM/Agentic Injection**
- Detects AI-related requirements (LLM, RAG, AI agents, prompt engineering)
- Injects AI-specific experience bullets based on genuine Assembli AI work
- Expands AI Engineering skills table row
- Adds ML & Data Science row when needed

**📅 Dynamic Years of Experience**
- Detects JD's years requirement (e.g., "5+ years", "6-8 years")
- Adjusts Career Summary accordingly (minimum floor: 4 years, maximum: 7+)
- Defaults to "5 years" when JD doesn't specify

**💉 Skill Injection**
- Identifies missing JD technologies (Redis, Terraform, GraphQL, Elasticsearch, etc.)
- Injects truthful experience bullets based on adjacent experience
- Adds technologies to Technical Skills table
- Auto-prunes lowest-priority bullets if needed to maintain 2 pages

**📄 LaTeX PDF Output**
- Professional LaTeX template matching original resume format
- Compiled via `pdflatex` (with Docker and Overleaf fallbacks)
- **Strict 2-page enforcement** — auto-prunes or expands to exactly 2 pages
- Output organized in `resumes/{Company}_{Frameworks}/` folders
- Each folder contains: `.tex`, `.pdf`, `.log`, and `recruiter_mail.md`

**🚀 Multi-Job Batch Processing**
- Process 3-5 similar jobs efficiently
- Shared experience discovery (ask once, apply to all)
- Aggregate gap analysis with deduplication
- Time savings: 11-27% faster than sequential processing
- Incremental batches (add more jobs later)

**📧 Recruiter Email**
- Auto-generates a short outreach email per job
- Brief company research for one natural, specific line
- Human writing principles: no buzzwords, no filler, varied sentence length
- Anti-AI checked: no "passionate", "leverage", or cover letter tone

**🎯 Smart Content Matching**
- Confidence-scored content selection (Direct/Transferable/Adjacent)
- Transparent gap identification
- Truth-preserving reframing

## Architecture

### Single-Job Workflow
```
Phase 0: JD Analysis (tech stack + years + missing skills — single pass)
   ↓
Phase 1: Framework Switching (career summary + skills + bullets)
   ↓
Phase 2: Skill Injection (missing tech + AI/LLM + skills table)
   ↓  [CHECKPOINT]
Phase 3: LaTeX Generation + 2-Page Enforcement
   ↓  Output → resumes/{Company}_{Frameworks}/
Phase 4: Recruiter Email Generation
   ↓
Phase 5: User Review
   ↓
Phase 6: Iteration (if needed)
```

**Output Structure:**
```
resumes/
├── resume_index.md            ← framework cache (auto-updated)
├── Google_React_NodeJS/
│   ├── resume.tex
│   ├── resume.pdf
│   ├── resume.log
│   └── recruiter_mail.md
├── Stripe_Python_FastAPI/
│   └── (same structure)
└── OpenAI_Python_LLM/
    └── (same structure)
```

### Multi-Job Workflow
```
Phase 0: Intake & Batch Initialization
   ↓
Phase 1: Aggregate Gap Analysis (deduplicates across all jobs)
   ↓
Phase 2: Per-Job Processing (stack switch + injection + LaTeX → PDF + email for each)
   ↓
Phase 3: Batch Finalization (review all resumes, update library)
```

**Time Savings:**
- 3 jobs: ~40 min vs ~45 min sequential (11% savings)
- 5 jobs: ~55 min vs ~75 min sequential (27% savings)

See `multi-job-workflow.md` for complete details.

## Design Philosophy

**Truth-Preserving Optimization:**
- NEVER fabricate experience
- Intelligently reframe and emphasize existing work
- Transparent about gaps

**Strict 2-Page Format:**
- Every resume is exactly 2 pages
- Auto-prunes or expands as needed
- Verified after PDF compilation

**Performance First:**
- Single-pass JD analysis (extract everything at once)
- Single-pass framework switching (all bullets in one go)
- LaTeX validation before compilation (avoid recompilation)
- Concise user interactions (don't overwhelm)

## Usage Examples

### Example 1: Java → Node.js Switch
```
USER: "I want to apply for this Node.js backend role. JD: {paste}"

RESULT:
- Backend switched: Java SpringBoot → Node.js/Express
- Testing: JUnit → Jest, Build: Maven → npm
- Redis caching experience injected
- Career Summary: "5+ years" (matched JD requirement)
- Technical Skills reordered: JavaScript/TypeScript first
- Output: resumes/Google_React_NodeJS/ (exactly 2 pages)
```

### Example 2: Python AI Engineer Role
```
USER: "Applying for a Python/AI engineer role at OpenAI. JD: {paste}"

RESULT:
- Backend switched: Java → Python/FastAPI
- AI Enhancement: RAG pipeline emphasis, AI agents, vector embeddings
- AI Engineering row expanded, ML & Data Science row added
- Career Summary: "5 years" with AI capabilities highlighted
- Elasticsearch injected for search requirements
- Output: resumes/OpenAI_Python_LLM/ (exactly 2 pages)
```

### Example 3: DevOps-Heavy Role
```
USER: "Role at HashiCorp requires heavy Terraform, K8s, and monitoring. JD: {paste}"

RESULT:
- Terraform module authoring bullet injected
- Kubernetes cluster management emphasized
- Grafana dashboards bullet added
- DevOps & CI/CD section expanded
- Years: "6+ years" (matched JD)
- Output: resumes/HashiCorp_Terraform_Kubernetes/ (exactly 2 pages)
```

### Example 4: Multi-Job Batch
```
USER: "Apply for these 3 roles:
      1. Node.js Backend - Stripe
      2. Python AI Engineer - OpenAI
      3. Full-Stack Java - Goldman Sachs"

RESULT:
- Batch mode activated, 3 resumes generated
- Each with correct tech stack switch + recruiter email
- Output folders:
  - resumes/Stripe_NodeJS_Redis/
  - resumes/OpenAI_Python_LLM/
  - resumes/GoldmanSachs_Java_SpringBoot/
- Each folder: .tex + .pdf + .log + recruiter_mail.md
- All exactly 2 pages
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Make your changes:**
   - Update `SKILL.md` for implementation changes
   - Add tests if applicable
   - Update README if architecture changes
4. **Commit with descriptive messages:** `git commit -m "feat: add amazing feature"`
5. **Push to your fork:** `git push origin feature/amazing-feature`
6. **Open a Pull Request**

**Before submitting:**
- Run regression tests (see Testing section in SKILL.md)
- Ensure all phases work end-to-end
- Update documentation

## Troubleshooting

**Skill not appearing:**
- Verify files are in the correct skill directory
- Restart Claude Code
- Check SKILL.md has valid YAML frontmatter

**LaTeX compilation failing:**
- Ensure `pdflatex` is installed (`brew install --cask mactex-no-gui`)
- Or use Docker: `docker run --rm -v $(pwd):/workspace texlive/texlive pdflatex ...`
- Or use Overleaf (free online LaTeX editor) with the generated .tex file

**Resume not exactly 2 pages:**
- The skill should auto-enforce this
- If manually editing .tex, adjust bullet count or spacing
- Check `latex-generation.md` for margin and spacing settings

**Low match confidence:**
- Consider adding more context about your experience
- Review gap handling recommendations

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for Claude Code skills framework
- Designed with truth-preserving optimization principles
- Inspired by the belief that job opportunities should be based on capabilities, not resume writing skills

## Support

- **Issues:** [GitHub Issues](https://github.com/manisreekar/resume-tailoring-skill/issues)
- **Discussions:** [GitHub Discussions](https://github.com/manisreekar/resume-tailoring-skill/discussions)

## Roadmap

- [ ] Cover letter generation integration
- [ ] LinkedIn profile optimization
- [ ] Interview preparation Q&A generation
- [ ] Multi-language resume support
- [ ] Custom industry templates
- [ ] ATS compatibility scoring
