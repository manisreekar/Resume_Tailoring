# Phase 1 & 2: Framework Switching + Skill Injection

## Phase 1: Framework Switching

**Goal:** Switch all technology references to match the JD's detected stack.

**Inputs:** Approved tailoring plan (Phase 0) + base LaTeX template.

### 1.1 Career Summary Rewrite

Apply the Career Summary template from `framework-switching.md`:

```
Variables to set from Phase 0 detection:
- YEARS_EXPERIENCE  → e.g., "5 years", "6+", minimum 4
- PRIMARY_BACKEND   → e.g., "Node.js and Python"
- PRIMARY_FRONTEND  → usually React (unchanged)
- CONTAINER_TOOLS   → Docker, Kubernetes (usually unchanged)
- IAC_TOOLS         → from JD (Terraform, CloudFormation, etc.)
- CI_CD_TOOLS       → from JD (GitHub Actions, Jenkins, etc.)
- MONITORING_TOOLS  → from JD (CloudWatch, Datadog, Grafana, etc.)
- AUTH_TOOLS        → from JD (OAuth2, JWT, etc.)
- AI_CAPABILITIES   → from JD if AI role (RAG, AI agents, LLM, etc.)

YEARS EXAMPLES:
  JD "5+ years" → \textbf{5+ years}
  JD "6 years"  → \textbf{6 years}
  JD nothing    → \textbf{5 years} (default)
  JD "3 years"  → \textbf{4+ years} (minimum floor)
```

### 1.2 Technical Skills Reordering

For each row in the Technical Skills table:
- Move JD-mentioned technologies to the **FRONT** of each row
- Demote (don't remove) technologies not in JD

```
Example — Node.js JD:
BEFORE: Java, Python, C, SQL, HTML, CSS, JavaScript, TypeScript...
AFTER:  JavaScript, TypeScript, Python, Java, C, SQL, HTML, CSS...

BEFORE: Flask, Django, Node.js, Express, Spring Boot, Hibernate, React...
AFTER:  Node.js, Express, React, Next.js, Redux, Tailwind CSS, Flask, Django, Spring Boot...
```

### 1.3 Experience Bullet Switching

For EVERY experience bullet across ALL roles, apply rules from `framework-switching.md`:

```
1. Identify framework/tool references in the bullet
2. Map to JD-equivalent:
   "Java SpringBoot" → "Node.js/Express"
   "JUnit"           → "Jest"
   "Maven"           → "npm"
   "Hibernate"       → "Prisma/Sequelize"
3. Replace ONLY tool names — preserve achievement, metrics, context
4. Verify the rewritten bullet reads naturally
```

**CRITICAL RULES — never break these:**
- NEVER change company names, dates, or job titles
- NEVER change metrics (30%, $400K, 60%, etc.)
- NEVER change the nature of the achievement
- Keep bullet length approximately the same

**Output:** Resume content with all framework references switched

---

## Phase 2: Skill Injection (Including AI/LLM/Agentic)

**Goal:** Add experience points for important JD skills that are missing.

**Inputs:** Missing skills list (Phase 0) + switched resume (Phase 1).

### 2.1 Injection Decision Tree

For each missing skill:
```
1. Is the skill required/preferred in JD?   → If NO, skip
2. Does user have adjacent experience?       → If NO, skip (never fabricate)
3. Which role is most relevant?             → Add bullet there
4. Will this push resume past 2 pages?      → If YES, remove lowest-priority
                                               bullet from oldest role first
5. Use injection template from framework-switching.md
```

### 2.2 AI/LLM/Agentic Injection Rules

User has GENUINE AI/LLM experience at Assembli AI (RAG pipelines, AI agents, LLM API integration, AWS Bedrock, LangChain). Inject/emphasize when JD signals:

```
AI/LLM SIGNALS:
- "LLM", "Large Language Model", "GPT", "Claude", "Bedrock"
- "AI agents", "agentic workflows", "autonomous agents"
- "RAG", "Retrieval-Augmented Generation"
- "prompt engineering", "prompt design"
- "vector database", "embeddings", "semantic search"
- "ML ops", "model deployment", "model serving"
- "AI/ML", "machine learning", "deep learning"
- "NLP", "natural language processing"
- "computer vision", "CV models"
- "fine-tuning", "model training"
```

**AI/LLM Injection Templates (LaTeX):**

```latex
% LLM/AI Agents:
\item \small Architected \textbf{AI agent workflows} with \textbf{LangChain} and \textbf{AWS Bedrock},
implementing multi-step reasoning pipelines that automated complex document analysis, reducing
manual processing time by 70\%.

% RAG:
\item \small Designed and deployed a production \textbf{Retrieval-Augmented Generation (RAG) pipeline}
integrating \textbf{vector embeddings} with \textbf{LLM APIs (OpenAI, Claude, Bedrock)}, achieving
90\% accuracy in context-aware content generation from large document repositories.

% Prompt Engineering:
\item \small Developed \textbf{prompt engineering frameworks} for production LLM integrations,
optimizing token usage by 40\% while maintaining output quality through systematic prompt
testing and evaluation.

% Vector Databases/Embeddings:
\item \small Implemented \textbf{vector embedding pipelines} using \textbf{OpenAI embeddings}
with \textbf{Pinecone/Weaviate}, enabling semantic search across 100K+ documents with
sub-second retrieval times.

% ML Ops / Model Deployment:
\item \small Built \textbf{ML model serving infrastructure} on \textbf{AWS (SageMaker/ECS)},
implementing A/B testing, model versioning, and automated retraining pipelines.

% Computer Vision:
\item \small Developed a \textbf{computer vision (CV) model} for automated document analysis,
extracting project metadata from blueprints to accelerate proposal generation workflows.

% NLP:
\item \small Built \textbf{NLP pipelines} for automated document classification and entity
extraction, processing 10K+ documents daily with 95\% accuracy using transformer-based models.
```

**AI Skills Table Injection (when JD is AI-heavy):**

```latex
% Expand AI Engineering row:
\textbf{AI Engineering} & LLM Integration, AI Agents, Agentic Workflows, Retrieval-Augmented
Generation (RAG), Prompt Engineering, Vector Embeddings, Fine-Tuning, Model Deployment,
LLM API Integration (OpenAI, Claude, Bedrock), LangChain, Semantic Search \\

% Add ML & Data Science row (if JD mentions ML heavily):
\textbf{ML \& Data Science} & PyTorch, TensorFlow, Scikit-learn, Pandas, NumPy,
Model Training, Feature Engineering, A/B Testing, Statistical Analysis \\
```

### 2.3 Injection Quality Check

For each injected bullet, verify:
- [ ] Truthful — based on adjacent/genuine experience
- [ ] Has a quantifiable metric where possible
- [ ] Uses `\textbf{}` for key terms (consistent with other bullets)
- [ ] Fits naturally in the role where placed
- [ ] Valid LaTeX syntax
- [ ] Resume still fits in 2 pages after injection

### 2.4 Present Injections to User

```
"I've identified {N} skills to inject:

1. REDIS (injected into Assembli AI role):
   '...implemented Redis-based caching layer, reducing database load by 40%...'

2. TERRAFORM (emphasized in MicroGig role):
   '...authored Terraform modules for AWS infrastructure (ECS, RDS, VPCs)...'

3. AI AGENTS (emphasized in Assembli AI role):
   '...architected AI agent workflows with LangChain and AWS Bedrock...'

These are based on your existing experience. Accept all / Review individually?"

Wait for user confirmation.
```

**Output:** Complete resume content with injected skill bullets, ready for LaTeX generation
