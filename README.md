# BOTB
# AI Product Visibility & Trust Monitoring Platform

## Overview
As customers increasingly use AI assistants to discover products, companies risk losing visibility or being misrepresented if their products are not included in AI-generated recommendations.

Our platform monitors how brands and products appear in AI-assisted shopping environments. It automatically tests AI assistants with realistic shopping queries, analyzes responses, detects misinformation or hallucinated product data, and provides insights to help companies improve visibility and accuracy.

---

## Problem
Customers now ask AI tools questions like:

- “Best laptops under $1000”
- “Best CRM software for small businesses”
- “Best noise cancelling headphones”

AI assistants often provide short recommendation lists. If a company’s product is not included, it may lose potential customers.

Additionally, AI systems may generate incorrect information such as:
- wrong pricing
- incorrect features
- outdated availability
- misleading comparisons

---

## Solution
Our system monitors AI assistants and evaluates how products appear in their recommendations.

The platform:

1. Sends standardized shopping prompts to AI assistants
2. Captures AI responses
3. Detects whether the brand appears
4. Extracts product information
5. Verifies product data using official sources

This allows companies to monitor visibility and detect misinformation.

---

## Ethics Monitoring
The system detects hallucinated or incorrect product information related to:

- pricing
- product features
- availability
- company policies

When misinformation is detected, the system flags the issue and logs it so companies can correct the source data and improve accuracy.

---

## Key Metrics
The platform tracks:

- Brand appearance rate in AI answers
- Ranking position in recommendations
- Frequency of misinformation
- Accuracy of product descriptions

These metrics help companies improve visibility and customer trust.

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
Monitoring Dashboard

---

## Technologies
Example technologies used in this prototype:

- Python
- OpenAI / LLM APIs
- REST APIs
- PostgreSQL
- React dashboard

---

## Running the Project
Run the prototype using:

```bash
./run.sh
