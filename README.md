# TNS AI (Truth and Service)

### AI Product Visibility & Trust Monitoring Platform

## Overview

As customers increasingly use AI assistants to discover products, companies risk losing visibility or being misrepresented if their products are not included in AI-generated recommendations.

**TNS AI** monitors how brands and products appear in AI-assisted shopping environments. The system automatically tests AI assistants with realistic shopping queries, analyzes responses, detects misinformation or hallucinated product data, and provides insights that help companies improve product visibility and accuracy.

---

## Problem

Customers now ask AI tools questions such as:

* “Best laptops under $1000”
* “Best CRM software for small businesses”
* “Best noise cancelling headphones”

AI assistants often return only a few recommendations. If a company’s product is missing or misrepresented, it can lose potential customers.

Additionally, AI systems may generate incorrect product information such as:

* wrong pricing
* incorrect features
* outdated availability
* misleading comparisons

Companies currently have **no clear way to monitor how their products appear inside AI answers.**

---

## Solution

TNS AI provides an automated monitoring platform that evaluates how products appear across AI assistants.

The system:

1. Sends standardized shopping prompts to AI assistants
2. Captures AI responses
3. Detects whether the brand appears in recommendations
4. Extracts product information from responses
5. Verifies product data against official sources
6. Detects hallucinated or incorrect product claims

This allows companies to monitor visibility, detect misinformation, and improve how their products are represented in AI-generated shopping results.

---

## Ethics Monitoring

AI-generated responses may contain incorrect or misleading product information.

TNS AI detects hallucinated claims related to:

* pricing
* product features
* availability
* company policies

When misinformation is detected, the system flags the issue and logs it so companies can correct the source data and improve AI accuracy.

---

## Key Metrics

The platform tracks:

* **Brand Appearance Rate** – how often the product appears in AI answers
* **Recommendation Ranking** – position within AI recommendation lists
* **Hallucination Frequency** – rate of incorrect AI product information
* **Accuracy Score** – percentage of verified product facts in responses

These metrics help companies improve visibility and customer trust in AI-driven product discovery.

---

## System Workflow

Prompt Library
↓
Prompt Engine
↓
AI Connectors (ChatGPT, Gemini, Claude)
↓
Response Parser
↓
Fact Checker (API Verification)
↓
Monitoring Metrics
↓
Monitoring Dashboard

---

## Technologies

Example technologies used in this prototype:

* Python
* REST APIs
* LLM APIs (OpenAI, Anthropic, Gemini)
* JSON data pipelines
* React-based dashboard prototype

---

## API Integration Notes

The current prototype uses **simulated AI responses** and **simulated product data** to ensure the project runs reliably without requiring external API credentials.

To demonstrate real-world feasibility, the repository includes example API integration files:

* `api/ai_api_examples.py`
* `api/product_api_examples.py`

These examples show how the system could connect to:

* AI model APIs (OpenAI, Anthropic, Gemini)
* company product APIs
* retailer product APIs
* structured product data feeds

This architecture allows the prototype to run consistently while still demonstrating production-ready integration design.

---

## Running the Project

Run the monitoring prototype:

```bash
./run.sh
```

Example output:

```
Monitoring Dell Inspiron 15
AI Model: ChatGPT
Brand Mentioned: True
Rank: 2
Accuracy Score: 80%
Hallucination Detected: RAM specification incorrect
```

Monitoring results are saved to:

```
logs/monitoring_results.json
```

---

## Repository Structure

```
BOTB/
│
├── api/                 # API integration examples
├── config/              # company profiles
├── monitor/             # monitoring engine modules
├── logs/                # monitoring results
├── architecture/        # system architecture documentation
├── dashboard/           # UI prototype documentation
├── tests/               # standardized monitoring prompts
│
├── main.py              # monitoring pipeline
├── run.sh               # run script
└── README.md
```

---

## Future Improvements

Future production versions of the platform could include:

* live AI API monitoring
* real product data integrations
* automated monitoring dashboards
* visibility optimization recommendations
* demographic fairness monitoring

---

## Competition Context

This prototype was developed to demonstrate a technical solution for monitoring product visibility and trust in **AI-assisted shopping environments**.
