#!/usr/bin/env python3
"""
JD tech stack detector — lightweight keyword extraction from job descriptions.

Replaces the detection tables in framework-switching.md with deterministic matching.
Claude should still do the REASONING about how to tailor — this script just does
the mechanical keyword scanning.

Usage:
  From text:   python3 scripts/jd_analyzer.py "We need a Node.js engineer with 5+ years..."
  From file:   python3 scripts/jd_analyzer.py --file jd.txt

Output (pipe-delimited, one line per category):
  BACKEND|nodejs|Node.js, Express, NestJS
  FRONTEND|react|React, Next.js
  CLOUD|aws|AWS, EC2, Lambda
  DATABASE|postgresql,redis|PostgreSQL, Redis
  QUEUE|kafka|Kafka
  AI|llm,rag,agents|LLM, RAG, AI Agents
  YEARS|5+
  SWITCH|nodejs  ← recommended primary backend switch
"""

import sys
import os
import re

# Detection patterns: {category: {signal_key: [keywords_to_match]}}
PATTERNS = {
    "BACKEND": {
        "nodejs": ["node.js", "nodejs", "express", "nestjs", "npm", "yarn"],
        "java": ["java", "spring boot", "springboot", "hibernate", "maven", "gradle"],
        "python": ["python", "django", "flask", "fastapi", "pip", "poetry"],
        "go": ["golang", " go ", "gin framework"],
        "dotnet": [".net", "c#", "asp.net"],
        "ruby": ["ruby", "rails", "ruby on rails"],
    },
    "FRONTEND": {
        "react": ["react", "next.js", "nextjs", "redux"],
        "angular": ["angular", "rxjs", "ngrx"],
        "vue": ["vue.js", "vuejs", "nuxt"],
    },
    "CLOUD": {
        "aws": ["aws", " ec2", "lambda", " s3 ", "ecs", "eks", "cloudformation", "sagemaker", "bedrock"],
        "gcp": ["gcp", "google cloud", "cloud run", "bigquery"],
        "azure": ["azure", "azure devops"],
    },
    "DATABASE": {
        "postgresql": ["postgresql", "postgres"],
        "mysql": ["mysql"],
        "mongodb": ["mongodb", "nosql", "mongo"],
        "redis": ["redis", "caching layer", "cache"],
        "dynamodb": ["dynamodb"],
        "elasticsearch": ["elasticsearch", "elastic search", "elk stack", "elk"],
    },
    "QUEUE": {
        "kafka": ["kafka"],
        "rabbitmq": ["rabbitmq"],
        "sqs": ["sqs", "sns", "aws sqs"],
    },
    "INFRA": {
        "kubernetes": ["kubernetes", "k8s", "eks", "gke", "aks"],
        "docker": ["docker", "container"],
        "terraform": ["terraform", "iac", "infrastructure as code"],
        "cicd": ["ci/cd", "cicd", "github actions", "jenkins", "gitlab ci", "circleci"],
    },
    "AI": {
        "llm": ["llm", "large language model", "gpt", "claude", "bedrock", "openai"],
        "rag": ["rag", "retrieval-augmented", "retrieval augmented"],
        "agents": ["ai agent", "agentic", "autonomous agent"],
        "prompt": ["prompt engineering", "prompt design"],
        "vector": ["vector database", "embeddings", "semantic search", "pinecone", "weaviate"],
        "ml": ["machine learning", "deep learning", "pytorch", "tensorflow", "scikit"],
        "nlp": ["nlp", "natural language processing"],
        "cv": ["computer vision"],
    },
    "MONITOR": {
        "datadog": ["datadog"],
        "grafana": ["grafana", "prometheus"],
        "newrelic": ["new relic"],
    },
}

# Years pattern
YEARS_RE = re.compile(r"(\d+)\+?\s*(?:[\-–]\s*\d+\s*)?years?\s*(?:of\s+)?(?:experience|exp)?", re.IGNORECASE)

# Known technical terms (flattened from PATTERNS) — used to identify what we DID match
_ALL_KNOWN_KEYWORDS: set[str] = set()
for _signals in PATTERNS.values():
    for _kws in _signals.values():
        _ALL_KNOWN_KEYWORDS.update(kw.strip().lower() for kw in _kws)

# Common tech terms regex — catches CamelCase tools, acronyms, dotted names
# This helps us find tech words the script doesn't have in its lookup tables
TECH_TERM_RE = re.compile(
    r"\b(?:"
    r"[A-Z][a-z]+(?:[A-Z][a-z]+)+"  # CamelCase: GraphQL, FastAPI, SvelteKit
    r"|[A-Z]{2,}"                    # Acronyms: REST, gRPC, SQL, NATS
    r"|[a-zA-Z]+\.(?:js|io|py|rs)"   # Dotted: Vue.js, Deno.js, Svelte.js
    r"|[a-zA-Z]+-[a-zA-Z]+"          # Hyphenated: server-side, type-safe
    r")\b",
)

# Noise words to exclude from unmatched (common non-tech terms that match patterns)
NOISE = {
    "REST", "API", "APIs", "SaaS", "PaaS", "IaaS", "HTML", "CSS", "JSON", "XML",
    "HTTP", "HTTPS", "URL", "SQL", "NoSQL", "ORM", "MVC", "IDE", "UI", "UX",
    "ETL", "CTO", "CEO", "VP", "PM", "TPM", "SWE", "SRE", "US", "TX", "AZ",
    "AM", "PM", "EST", "PST", "CST", "PDT", "GMT", "UTC", "PhD", "BS", "MS",
    "BA", "MA", "GPA", "OK", "NA", "TBD", "FAQ", "FYI", "ASAP", "EOD", "WFH",
    "AND", "OR", "NOT", "THE", "FOR", "WITH", "FROM", "INTO", "HAVE", "HAS",
    "WE", "YOU", "OUR", "ARE", "CAN", "WILL", "MAY", "THIS", "THAT", "MUST",
    "SHOULD", "WOULD", "COULD", "TEAM", "ROLE", "WORK", "JOIN", "LEAD", "BUILD",
    "ABOUT", "HELP", "MAKE", "IF", "IT", "IN", "ON", "AT", "TO", "OF", "AS",
    "IS", "BE", "DO", "BY", "AN", "SO", "UP", "NO", "ALL", "NEW", "PLUS",
}


def analyze_jd(text: str) -> None:
    """Scan JD text for tech stack signals and output structured results."""
    text_lower = text.lower()

    # Track all keywords we successfully matched
    matched_all_keywords: set[str] = set()

    # Detect backend priority (which one is mentioned most/first)
    backend_scores: dict[str, int] = {}

    for category, signals in PATTERNS.items():
        matched_keys = []
        matched_display = []

        for key, keywords in signals.items():
            hits = sum(1 for kw in keywords if kw.lower() in text_lower)
            if hits > 0:
                matched_keys.append(key)
                matched_all_keywords.update(kw.lower() for kw in keywords if kw.lower() in text_lower)
                display_map = {
                    "nodejs": "Node.js", "postgresql": "PostgreSQL", "mongodb": "MongoDB",
                    "dynamodb": "DynamoDB", "elasticsearch": "Elasticsearch",
                    "rabbitmq": "RabbitMQ", "cicd": "CI/CD", "dotnet": ".NET",
                    "sqs": "SQS/SNS", "nlp": "NLP", "cv": "Computer Vision",
                    "aws": "AWS", "gcp": "GCP", "llm": "LLM", "rag": "RAG",
                    "ml": "ML", "kubernetes": "Kubernetes", "docker": "Docker",
                    "terraform": "Terraform", "datadog": "Datadog", "grafana": "Grafana",
                    "newrelic": "New Relic", "agents": "AI Agents", "prompt": "Prompt Engineering",
                    "vector": "Vector DBs", "redis": "Redis", "kafka": "Kafka",
                    "java": "Java", "python": "Python", "go": "Go", "ruby": "Ruby",
                    "react": "React", "angular": "Angular", "vue": "Vue.js",
                    "mysql": "MySQL", "azure": "Azure",
                }
                matched_display.append(display_map.get(key, key.replace("_", " ").title()))

                if category == "BACKEND":
                    backend_scores[key] = hits

        if matched_keys:
            print(f"{category}|{','.join(matched_keys)}|{', '.join(matched_display)}")

    # Years detection
    years_match = YEARS_RE.search(text)
    if years_match:
        raw_years = int(years_match.group(1))
        # Apply floor/ceiling: min 4, max 7+
        if raw_years < 4:
            print(f"YEARS|4+|floor applied (JD said {raw_years})")
        elif raw_years > 7:
            print(f"YEARS|7+|ceiling applied (JD said {raw_years})")
        else:
            plus = "+" if "+" in years_match.group(0) else ""
            print(f"YEARS|{raw_years}{plus}")
    else:
        print("YEARS|5|default (not specified in JD)")

    # Recommended switch
    if backend_scores:
        primary = max(backend_scores, key=backend_scores.get)
        if primary != "java":  # java is default, no switch needed
            print(f"SWITCH|{primary}")
        else:
            print("SWITCH|none|Java is default, no switch needed")
    else:
        print("SWITCH|none|No clear backend detected")

    # --- Unmatched tech term detection ---
    # Find technical-looking terms in the JD that we didn't match
    potential_tech = set(TECH_TERM_RE.findall(text))
    unmatched = []
    for term in sorted(potential_tech):
        term_lower = term.lower()
        if term.upper() in NOISE:
            continue
        if term_lower in matched_all_keywords:
            continue
        if any(term_lower in kw or kw in term_lower for kw in matched_all_keywords):
            continue
        unmatched.append(term)

    if unmatched:
        print(f"UNMATCHED|{','.join(unmatched)}|LLM should evaluate these manually")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print('  python3 scripts/jd_analyzer.py "JD text here..."')
        print('  python3 scripts/jd_analyzer.py --file jd.txt')
        sys.exit(1)

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("ERROR|Provide file path")
            sys.exit(1)
        with open(sys.argv[2]) as f:
            text = f.read()
    else:
        text = " ".join(sys.argv[1:])

    analyze_jd(text)


if __name__ == "__main__":
    main()
