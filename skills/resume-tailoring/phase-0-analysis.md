# Phase 0: JD Analysis & Tech Stack Detection

**Always runs first — determines every change to make before touching the resume.**

## Step 0: Cache Check (Before Anything Else)

Before any JD analysis, check if a compatible resume already exists using the cache script.

**0.1 Quick-scan JD for key frameworks** (just the tech keywords, no full analysis yet)

**0.2 Run the cache check script:**

```bash
python3 scripts/cache_check.py "React, Node.js, TypeScript, GraphQL"
```

**Output is one line, deterministic:**
```
CACHE_HIT|Google_React_NodeJS|95|React,Node.js,TypeScript|GraphQL
#        |folder             |% |matched frameworks      |missing

NO_MATCH
```

**0.3 If CACHE HIT:**

```
"Found a compatible resume: resumes/{matched_folder}/

Frameworks match: {percent}%
Matched: {matched_list}
Missing: {missing_list}

ACTIONS (skip full tailoring):
1. Copy existing resume.tex to new company folder
2. Compile fresh PDF
3. Generate new recruiter_mail.md for this company

This saves significant time. Proceed? (Y/N)"

If user approves:
  → Skip Phase 1-2 entirely
  → Jump to Phase 3 (compile) + Phase 5 (recruiter email)
  → Create new folder: resumes/{NewCompany}_{Frameworks}/
  → Run: python3 scripts/cache_check.py --add "{NewCompany}_{Frameworks}" "{frameworks}"
```

**0.4 If NO_MATCH:**

Continue with full JD analysis below (Steps 1-5).

---

## Full Analysis (runs only if no cache hit)

**Step 1: Parse the JD (single pass — extract everything at once)**

```
Extract ALL of the following in ONE pass:
- EXPLICIT REQUIREMENTS (must-have vs nice-to-have)
- TECHNICAL KEYWORDS (languages, frameworks, tools, platforms)
- YEARS OF EXPERIENCE REQUIRED (e.g., "5+ years", "3-5 years")
- AI/LLM/AGENTIC REQUIREMENTS (LLM, RAG, AI agents, prompt engineering, etc.)
- IMPLICIT PREFERENCES (team size hints, scale expectations)
- ROLE ARCHETYPE (backend-heavy, full-stack, DevOps-leaning, AI-focused)
```

**Step 2: Detect Primary Tech Stack**

Use the detection tables from `framework-switching.md`:
```
Backend:   Java | Node.js | Python | Go | .NET
Frontend:  React | Angular | Vue
Cloud:     AWS | GCP | Azure
Database:  PostgreSQL | MySQL | MongoDB | Redis | DynamoDB
Queue:     Kafka | RabbitMQ | SQS/SNS
CI/CD:     GitHub Actions | Jenkins | GitLab CI | CircleCI
Container: Docker + Kubernetes | Docker Swarm | ECS
IaC:       Terraform | CloudFormation | Pulumi
Auth:      OAuth2/JWT | SAML | Auth0/Okta
Monitor:   CloudWatch | Datadog | Grafana | New Relic
AI/LLM:    LLM Integration | AI Agents | RAG | Prompt Engineering | Vector DBs
```

**Step 3: Detect Years of Experience Requirement**

```
RULES:
- JD says "5+ years" or "5 years"    → "5 years" or "5+ years" in Career Summary
- JD says "6+ years" or "6-8 years"  → "6+ years" in Career Summary
- JD says "7+ years"                 → "7+ years" in Career Summary
- JD says "3+ years" / "3-5 years"   → "4+ years" (minimum floor — never go below)
- No years mentioned in JD           → "5 years" (default)
- MINIMUM: always 4 years
- MAXIMUM: 7+ years (never claim more)
```

**Step 4: Identify Missing Skills (including AI/LLM)**

Compare JD requirements against the base resume. Flag any technology that:
- Is mentioned as required/preferred
- Is NOT currently in Technical Skills
- Has adjacent/transferable experience to support injection
- **Specifically flag AI/LLM/Agentic requirements** → handled in Phase 2

**Step 5: Present Tailoring Plan to User**

```
"Based on the JD analysis, here's my tailoring plan:

TECH STACK SWITCHES:
- Backend: Java SpringBoot → Node.js/Express (JD is Node.js-heavy)
- Testing: JUnit → Jest/Mocha
- Build: Maven → npm/yarn

SKILL INJECTIONS:
- Redis: Add caching experience bullet (adjacent to existing DB work)
- Terraform: Emphasize existing IaC experience (already in skills)
- GraphQL: Expand existing GraphQL mention

YEARS OF EXPERIENCE:
- JD requires 5+ years → Career Summary will say "5+ years"

REORDERING:
- Languages: JavaScript, TypeScript moved to front
- Frameworks: Node.js, Express moved to front

NO CHANGES:
- Frontend: React (already matches)
- Cloud: AWS (already matches)
- Company names/dates/titles: Never changed

Does this plan look good? Any adjustments?"

Wait for user confirmation before proceeding.
```

**Output:** Approved tailoring plan with specific switches, injections, and years value
