# Error Handling, Examples & Testing

## Error Handling & Edge Cases

**Edge Case 1: JD Has No Clear Tech Stack**
```
"The JD doesn't specify a tech stack.

OPTIONS:
1. Keep Java/SpringBoot (default)
2. Switch to Node.js (common in web roles)
3. Switch to Python (common in data/AI roles)
4. You tell me what stack to use"
```

**Edge Case 2: JD Requests a Stack the User Has No Experience In**
```
"The JD specifies {Go/Rust/.NET} which isn't in your experience.

APPROACH:
- Keep closest equivalent ({Java/Python})
- Emphasize transferable concepts (distributed systems, API design)
- Note polyglot capability in Career Summary
- Flag gap for cover letter"
```

**Edge Case 3: Too Many Skills to Inject**
```
"The JD mentions {N} technologies not on your resume.

PRIORITIZATION (inject top 3-5 only):
1. {Skill}: Required in JD → HIGH priority
2. {Skill}: Preferred in JD → MEDIUM priority
3. {Skill}: Mentioned once → LOW priority

Inject top {N}? Or you choose?"
```

**Edge Case 4: LaTeX Compilation Fails**
```
1. Check error log for specific issue
2. Fix LaTeX syntax error (unclosed brace, unescaped &, etc.)
3. Retry compilation
4. If persistent: provide .tex file for Overleaf
```

**Edge Case 5: Resume Exceeds 2 Pages After Injections**

Auto-enforce — do NOT ask user. See `phase-3-5-output.md` §3.3 for the full enforcement rules.
Key: shorten verbose bullets, consolidate near-duplicates, NEVER remove original bullets.

**Edge Case 6: JD Asks for More Years Than Realistic**

See `phase-0-analysis.md` Step 3 for the full rules. Key: min 4, max 7+, never claim more.

**Edge Case 7: JD is Heavily AI/LLM Focused**
```
- Expand AI Engineering row in Technical Skills
- Add ML & Data Science row if JD mentions it
- Inject 2-3 AI-specific bullets in Assembli AI and MicroGig roles
- Emphasize RAG, AI agents, LLM integration in Career Summary
- Ensure AI capabilities appear in Career Summary's "proven track record" line
```

---

## Usage Examples

**Example 1: Java → Node.js Switch**
```
USER: "I want to apply for this Node.js backend role. JD: {paste}"

SKILL:
1. JD Analysis: Detects Node.js, Express, MongoDB, Redis, Jest
2. Switches: Java→Node.js, SpringBoot→Express, JUnit→Jest, Maven→npm
3. Injects: Redis caching experience bullet
4. Reorders: JavaScript/TypeScript first in Languages
5. Generates: LaTeX → PDF (exactly 2 pages)

RESULT: Resume reads as a Node.js developer with 5 years experience
OUTPUT: resumes/Company_NodeJS_Redis/resume.pdf
```

**Example 2: DevOps-Heavy Role**
```
USER: "Role requires heavy Terraform, K8s, and monitoring. JD: {paste}"

SKILL:
1. JD Analysis: Detects Terraform (heavy), Kubernetes, Prometheus, Grafana
2. Switches: Minor — emphasizes existing DevOps skills
3. Injects: Terraform module authoring, K8s cluster management, Grafana dashboards
4. Generates: LaTeX → PDF (exactly 2 pages)

RESULT: Resume emphasizes infrastructure and DevOps capabilities
```

**Example 3: Python Data/AI Role**
```
USER: "Applying for a Python/AI engineer role. JD: {paste}"

SKILL:
1. JD Analysis: Detects Python, FastAPI, PyTorch, Redis, Elasticsearch, LLM, RAG
2. Years: JD says 5+ → "5+ years"
3. Switches: Java→Python, SpringBoot→FastAPI, Hibernate→SQLAlchemy
4. Injects: Elasticsearch, AI agents, RAG pipeline, vector embeddings
5. AI Enhancement: Expanded AI Engineering row, ML & Data Science row added
6. 2-Page Check: Pruned 2 bullets from Synchrony Intern to fit
7. Generates: LaTeX → PDF (exactly 2 pages)

RESULT: Resume reads as Python AI engineer with 5+ years
OUTPUT: resumes/OpenAI_Python_LLM/resume.pdf
```

**Example 4: Multi-Job Batch**
```
USER: "Apply for these 3 roles:
      1. Node.js Backend - Stripe
      2. Python AI Engineer - OpenAI
      3. Full-Stack Java - Goldman Sachs"

SKILL:
1. Detects multi-job mode → user confirms batch
2. Aggregate gap analysis across all 3 JDs
3. Per-job processing:
   - Stripe: Node.js switch, Redis/Kafka injection, 5+ years
   - OpenAI: Python switch, AI/LLM heavy, RAG emphasis, 5 years
   - Goldman: Java default, security emphasis, Terraform, 6+ years
4. Each: LaTeX → PDF (exactly 2 pages each)
5. Each folder: resume.tex, resume.pdf, resume.log, recruiter_mail.md

RESULT: 3 tailored resumes, each 2 pages, each with correct stack
OUTPUT FOLDERS:
- resumes/Stripe_NodeJS_Redis/
- resumes/OpenAI_Python_LLM/
- resumes/GoldmanSachs_Java_SpringBoot/
```

---

## Testing Guidelines

**Test 1: Java → Node.js Switch**
- Provide Node.js-heavy JD
- Verify ALL Java/SpringBoot refs switched
- Verify JUnit→Jest, Maven→npm
- Verify Career Summary rewritten, Technical Skills reordered
- Compile PDF successfully, verify exactly 2 pages

PASS: No Java/SpringBoot in prominent positions, PDF is 2 pages

**Test 2: Skill Injection (Redis)**
- Provide JD mentioning Redis
- Verify Redis in Technical Skills, experience bullet added, reasonable metric
- Verify exactly 2 pages

PASS: Redis appears naturally, 2 pages

**Test 3: LaTeX Compilation**
- Generate .tex, run pdflatex
- Verify no errors, PDF renders correctly, formatting matches template
- Verify exactly 2 pages

PASS: Clean PDF output matching template style, 2 pages

**Test 4: Dynamic Years of Experience**
- JD "5+ years" → Career Summary says "5+" or "5 years"
- JD "6+ years" → says "6+ years"
- JD "3 years" (below floor) → says "4+ years"
- JD no years → says "5 years" (default)

PASS: Years within bounds (min 4, max 7+)

**Test 5: AI/LLM Injection**
- JD mentions LLM, RAG, AI agents, prompt engineering
- Verify AI Engineering row expanded, AI bullets injected, Career Summary mentions AI
- Verify exactly 2 pages

PASS: Resume reads as AI-capable engineer, 2 pages

**Test 6: Multi-Skill Injection + 2-Page Limit**
- JD with Redis, Terraform, GraphQL, Grafana, AI agents
- Verify all skills injected, resume EXACTLY 2 pages

PASS: All skills present, exactly 2 pages

**Test 7: Unknown Stack (Go/Rust)**
- JD mentioning Rust/Go → graceful fallback, closest stack kept
- Verify transferable skills emphasized, 2 pages

PASS: Reasonable fallback, 2 pages

**Test 8: Multi-Job Batch (3 JDs)**
- Verify batch mode activated, each resume has correct stack
- Verify each exactly 2 pages, recruiter email per job

PASS: 3 distinct resumes, each 2 pages, correct tech stack, each with recruiter_mail.md
