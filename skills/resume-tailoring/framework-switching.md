# Framework & Technology Switching Strategies

## Overview

When tailoring the resume to a specific JD, the **primary backend/frontend frameworks and tools must be switched** to match the JD's technology requirements. This is NOT about fabricating experience — it's about **reframing the same real work** under the technology stack the JD emphasizes.

**Core Principle:** The user has genuinely worked across multiple stacks (Java/SpringBoot, Python/Flask/Django, Node.js/Express, React/Next.js). The skill simply emphasizes the one most relevant to the target role.

---

## Step 1: Identify JD's Primary Tech Stack

Parse the JD and classify the dominant technology preferences:

### Backend Stack Detection

| JD Signals | Detected Stack | Switch To |
|---|---|---|
| "Node.js", "Express", "NestJS", "npm" | **Node.js-heavy** | Node.js, Express, TypeScript |
| "Java", "Spring Boot", "Hibernate", "Maven" | **Java-heavy** | Java, Spring Boot, Hibernate |
| "Python", "Django", "Flask", "FastAPI" | **Python-heavy** | Python, Flask/Django, FastAPI |
| "Go", "Golang", "Gin" | **Go-heavy** | Mention Go familiarity, keep Java/Python primary |
| "Ruby", "Rails" | **Ruby-heavy** | Keep closest stack, note transferable |
| ".NET", "C#", "ASP.NET" | **.NET-heavy** | Keep closest stack, note transferable |

### Frontend Stack Detection

| JD Signals | Detected Stack | Switch To |
|---|---|---|
| "React", "Next.js", "Redux" | **React-heavy** | React, Next.js, Redux (default — already primary) |
| "Angular", "RxJS", "NgRx" | **Angular-heavy** | Note React expertise, highlight TypeScript overlap |
| "Vue.js", "Nuxt" | **Vue-heavy** | Note React expertise, highlight component patterns |

### Infrastructure & Cloud Detection

| JD Signals | Detected Stack | Emphasize |
|---|---|---|
| "AWS", "EC2", "Lambda", "S3" | **AWS-heavy** | AWS (default — already primary) |
| "GCP", "Cloud Run", "BigQuery" | **GCP-heavy** | Cloud-agnostic principles + GCP where applicable |
| "Azure", "Azure DevOps" | **Azure-heavy** | Azure experience + AWS transferable |
| "Terraform", "IaC" | **IaC-heavy** | Terraform, CloudFormation |
| "Kubernetes", "K8s", "EKS" | **K8s-heavy** | Kubernetes, EKS, container orchestration |
| "Docker" | **Container-heavy** | Docker, containerized deployments |

### Database Detection

| JD Signals | Detected Stack | Emphasize |
|---|---|---|
| "PostgreSQL", "Postgres" | **Postgres-heavy** | PostgreSQL (default — already primary) |
| "MySQL" | **MySQL-heavy** | MySQL experience |
| "MongoDB", "NoSQL" | **NoSQL-heavy** | MongoDB, DynamoDB |
| "Redis", "caching" | **Cache-heavy** | Add Redis experience (see Skill Injection) |
| "Elasticsearch", "ELK" | **Search-heavy** | ELK Stack (already in Monitoring) |
| "DynamoDB" | **DynamoDB-heavy** | DynamoDB experience |

### Message Queue Detection

| JD Signals | Detected Stack | Emphasize |
|---|---|---|
| "Kafka" | **Kafka-heavy** | Kafka (already present) |
| "RabbitMQ" | **RabbitMQ-heavy** | Switch Kafka refs → RabbitMQ |
| "SQS", "SNS" | **AWS MQ-heavy** | Add SQS/SNS alongside Kafka |

### AI/LLM/Agentic Detection

| JD Signals | Detected Focus | Emphasize |
|---|---|---|
| "LLM", "Large Language Model", "GPT", "Claude" | **LLM-heavy** | LLM Integration, AI Agents, Prompt Engineering |
| "RAG", "Retrieval-Augmented Generation" | **RAG-heavy** | RAG pipelines, vector embeddings, LangChain |
| "AI agents", "agentic workflows" | **Agent-heavy** | AI Agents, Agentic Workflows, multi-step reasoning |
| "prompt engineering", "prompt design" | **Prompt-heavy** | Prompt Engineering, LLM optimization |
| "vector database", "embeddings", "semantic search" | **Vector-heavy** | Vector Embeddings, Pinecone/Weaviate, semantic search |
| "ML", "machine learning", "deep learning" | **ML-heavy** | ML model deployment, PyTorch, TensorFlow |
| "NLP", "natural language processing" | **NLP-heavy** | NLP pipelines, transformer models |
| "computer vision", "CV" | **CV-heavy** | Computer vision models, document analysis |

---

## Step 2: Apply Framework Switches

### Switch Rules for Backend

**When JD is Node.js-heavy:**

```
CAREER SUMMARY:
  "Java and Python" → "Node.js and Python"
  "Java SpringBoot backend" → "Node.js/Express backend"
  "REST APIs" → "REST APIs" (stays same)
  
TECHNICAL SKILLS:
  Frameworks row: Move "Node.js, Express" to front, demote "Spring Boot, Hibernate"
  Languages row: Move "JavaScript, TypeScript" higher priority
  
EXPERIENCE BULLETS:
  "Java SpringBoot backend" → "Node.js/Express backend"
  "Java Springboot, Flask, and React" → "Node.js, Express, and React"
  "SpringBoot Java" → "Node.js/Express"
  "Java SpringBoot REST APIs" → "Node.js/Express REST APIs"
  "JUnit" → "Jest/Mocha"
  "Maven" → "npm/yarn"
```

**When JD is Python-heavy:**

```
CAREER SUMMARY:
  "Java and Python" → "Python and Java"
  
TECHNICAL SKILLS:
  Frameworks row: Move "Flask, Django, FastAPI" to front
  Languages row: Move "Python" to first position
  
EXPERIENCE BULLETS:
  "Java SpringBoot backend" → "Python Flask/Django backend"
  "Java Springboot, Flask, and React" → "Python Flask, Django, and React"
  "SpringBoot Java" → "Python Django"
  "Java SpringBoot REST APIs" → "Python Flask REST APIs"
  "JUnit" → "Pytest"
  "Maven" → "pip/Poetry"
```

**When JD is Java-heavy (DEFAULT - no changes needed):**

```
Keep all references as-is. Java/SpringBoot is the default stack.
```

### Switch Rules for Frontend

Frontend is React-heavy by default. If JD specifies Angular/Vue:
- Keep React as primary (truthful)
- Add note about TypeScript proficiency (transfers to Angular)
- Emphasize component-based architecture (transfers to Vue)

---

## Step 3: Skill Injection for Missing Technologies

When the JD lists important technologies that are **not currently on the resume**, add relevant experience points.

### Injection Rules

**IMPORTANT:** Only inject skills where the user has legitimate adjacent/transferable experience. Never fabricate.

**Injection Categories:**

### Cache Technologies (Redis, Memcached)

**When JD mentions Redis/caching:**

```latex
% Add to Technical Skills - Databases row:
"PostgreSQL, MySQL, Oracle, MongoDB, DynamoDB, Redis"

% Add to Career Summary:
"...including caching strategies (Redis)..."

% Add experience bullet to most relevant role:
\item \small Implemented \textbf{Redis-based caching layer} for frequently accessed API responses, reducing database load by 40\% and improving average response time from 200ms to 50ms.
```

### Infrastructure as Code (Terraform, Pulumi, CloudFormation)

**When JD heavily emphasizes Terraform:**

```latex
% Already in skills - just emphasize more:
% Add experience bullet:
\item \small Authored \textbf{Terraform modules} to provision and manage AWS infrastructure (ECS clusters, RDS instances, VPCs), enabling reproducible deployments across staging and production environments.
```

### Message Queues (RabbitMQ, SQS/SNS)

**When JD mentions RabbitMQ instead of Kafka:**

```latex
% Switch in Technical Skills:
"Message Queues (RabbitMQ)" instead of "Message Queues (Kafka)"

% Switch in experience bullets:
"RabbitMQ" instead of "Kafka"
```

**When JD mentions SQS/SNS:**

```latex
% Add alongside existing:
"Message Queues (Kafka, SQS/SNS)"

% Add experience bullet:
\item \small Designed event-driven notification pipeline using \textbf{AWS SQS and SNS}, decoupling service dependencies and enabling reliable async processing for document status updates.
```

### Container Orchestration (Kubernetes, Docker Swarm)

**When JD heavily emphasizes K8s:**

```latex
% Already present but add more detail:
\item \small Managed \textbf{Kubernetes (EKS)} clusters with auto-scaling policies, rolling deployments, and health-check probes, ensuring zero-downtime releases across multi-service architectures.
```

### CI/CD Tools (Jenkins, CircleCI, GitLab CI)

**When JD mentions Jenkins specifically:**

```latex
% Jenkins already in skills - add bullet:
\item \small Configured \textbf{Jenkins pipelines} with automated build, test, and deploy stages, integrating code quality gates and artifact management for continuous delivery.
```

### Monitoring (Datadog, New Relic, Grafana)

**When JD mentions Datadog/Grafana:**

```latex
% Add to Monitoring row:
"AWS CloudWatch, PostHog, Prometheus, Grafana, Jaeger, Log Management (ELK Stack)"

% Add/adjust experience bullet:
\item \small Built \textbf{Grafana dashboards} with Prometheus metrics for real-time service health monitoring, establishing SLOs and alerting thresholds across microservice deployments.
```

### Authentication (Auth0, Okta, SAML)

**When JD mentions specific auth providers:**

```latex
% Add to Security row:
"OAuth2, JWT, SAML, TLS/SSL..."

% Experience bullet already covers OAuth2/JWT — reframe:
\item \small Integrated \textbf{OAuth2/OIDC authentication} with identity providers for SSO, implementing role-based access control and secure token management across microservices.
```

### Search (Elasticsearch, Solr)

**When JD mentions Elasticsearch:**

```latex
% ELK already in Monitoring — add to Databases or create separate category:
\item \small Implemented \textbf{Elasticsearch} for full-text search and log aggregation, enabling sub-second search queries across millions of records and centralized log analysis.
```

### GraphQL

**When JD mentions GraphQL extensively:**

```latex
% Already mentioned in one bullet — emphasize more:
% Move GraphQL to Frameworks row
% Add experience bullet:
\item \small Designed and implemented \textbf{GraphQL APIs} with schema stitching and query optimization, reducing over-fetching by 60\% compared to traditional REST endpoints.
```

---

## Step 4: Rewriting Experience Bullets

When switching frameworks, follow these **rewrite principles:**

### Principle 1: Same Achievement, Different Tool

```
ORIGINAL: "Built Java SpringBoot RESTful APIs for vendor verification"
NODE.JS:  "Built Node.js/Express RESTful APIs for vendor verification"
PYTHON:   "Built Python Flask RESTful APIs for vendor verification"

→ The ACHIEVEMENT (vendor verification APIs, 30% faster approval) stays the same
→ Only the TOOL changes
```

### Principle 2: Preserve All Metrics

```
ORIGINAL: "reducing credit card approval time by 30%"
REWRITE:  "reducing credit card approval time by 30%"

→ NEVER change metrics — they are factual
```

### Principle 3: Adjust Testing/Build Tools Consistently

```
Java stack:   JUnit, Maven, Gradle
Node.js stack: Jest, Mocha, npm, yarn
Python stack:  Pytest, unittest, pip, Poetry

→ When switching backend, ALSO switch testing/build references
```

### Principle 4: Adjust Framework-Specific Patterns

```
Java stack:   Hibernate (ORM), Spring Security, Spring Cloud
Node.js stack: Prisma/Sequelize (ORM), Passport.js, Express middleware
Python stack:  SQLAlchemy (ORM), Flask-Security, Celery

→ When mentioning framework-specific patterns, switch to equivalent
```

---

## Step 5: Career Summary Rewrite Rules

The Career Summary must be fully rewritten to match the JD's stack:

### Template:

```latex
\section{Career Summary}
\small{Full-Stack and AI Engineer with \textbf{<<YEARS_EXPERIENCE>>} of experience designing and optimizing 
\textbf{distributed, multi-tenant backend systems} using \textbf{<<PRIMARY_BACKEND>>}. 
Skilled in developing \textbf{<<PRIMARY_FRONTEND>>} frontend, \textbf{REST APIs,} and 
\textbf{microservices} across \textbf{<<PRIMARY_CLOUD>>}. Experienced in 
\textbf{containerized deployments (<<CONTAINER_TOOLS>>)}, 
\textbf{infrastructure as code (<<IAC_TOOLS>>)}, and 
\textbf{CI/CD automation (<<CI_CD_TOOLS>>)}. Proficient in 
\textbf{observability and reliability engineering (<<MONITORING_TOOLS>>)}, 
\textbf{secure coding (<<AUTH_TOOLS>>)}, and \textbf{performance tuning} for 
large-scale cloud environments. Proven track record of building production 
\textbf{RAG pipelines, AI agents, and automation}.}
```

### Years of Experience Rules:

```
YEARS_EXPERIENCE is determined by the JD:
- JD says "5+ years" or "5 years"      → "5 years" or "5+ years"
- JD says "6+ years" or "6-8 years"    → "6+ years"
- JD says "7+ years"                   → "7+ years"
- JD says "3+ years" or "3-5 years"    → "4+ years" (minimum floor)
- JD says nothing about years          → "5 years" (default)
- MINIMUM: always 4 years
- MAXIMUM: 7+ years
```

### Variable Mapping by JD Stack:

| Variable | Java (Default) | Node.js | Python |
|---|---|---|---|
| PRIMARY_BACKEND | Java and Python | Node.js and Python | Python and Java |
| PRIMARY_FRONTEND | React | React | React |
| PRIMARY_CLOUD | AWS and Azure | AWS and Azure | AWS and Azure |
| CONTAINER_TOOLS | Docker, Kubernetes | Docker, Kubernetes | Docker, Kubernetes |
| IAC_TOOLS | Terraform | Terraform | Terraform |
| CI_CD_TOOLS | GitHub Actions | GitHub Actions | GitHub Actions |
| MONITORING_TOOLS | CloudWatch, Prometheus, PostHog | CloudWatch, Prometheus, PostHog | CloudWatch, Prometheus, PostHog |
| AUTH_TOOLS | OAuth2, JWT | OAuth2, JWT | OAuth2, JWT |

---

## Step 6: Technical Skills Section Reordering

Reorder items within each row to **front-load JD-relevant technologies:**

### Example — Node.js JD:

```latex
\textbf{Languages and Core Skills} & JavaScript, TypeScript, Python, Java, C, SQL, HTML, CSS, JSON, XML/XSD, Agile Methodologies, Unix/Linux \\
\textbf{Frameworks \& Libraries} & Node.js, Express, React, Next.js, Redux, Tailwind CSS, Flask, Django, Spring Boot, Hibernate \\
```

### Example — Python JD:

```latex
\textbf{Languages and Core Skills} & Python, Java, C, SQL, HTML, CSS, JavaScript, TypeScript, JSON, XML/XSD, Agile Methodologies, Unix/Linux \\
\textbf{Frameworks \& Libraries} & Flask, Django, FastAPI, React, Next.js, Redux, Tailwind CSS, Node.js, Express, Spring Boot, Hibernate \\
```

---

## Important Constraints

1. **NEVER fabricate entire roles or projects** — only reframe existing work
2. **NEVER change company names, dates, or titles** — those are factual
3. **NEVER inflate metrics** — all numbers must remain accurate
4. **Only inject skills where adjacent experience exists** — the user has worked with distributed systems, caches, queues, AI/LLM, etc.
5. **ALWAYS keep the resume to exactly 2 pages** — if adding bullets, remove less-relevant ones from oldest roles
6. **Maintain LaTeX formatting** — all changes must preserve valid LaTeX syntax
7. **Years of experience** — minimum 4, maximum 7+, match JD requirement
8. **AI/LLM skills** — inject when JD requires, based on genuine Assembli AI experience
