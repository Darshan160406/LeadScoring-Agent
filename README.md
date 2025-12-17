# Lead Scoring Agent – Business Development Demo

**Live Demo:** [https://7tc5hgbwv5s999gq5mjtxb.streamlit.app](https://7tc5hgbwv5s999gq5mjtxb.streamlit.app/) [web:1]  
**GitHub Repository:** [https://github.com/Darshan160406/LeadScoring-Agent](https://github.com/Darshan160406/LeadScoring-Agent) [web:1]

---

## Overview

This project is a lead-prioritization demo built for a business development use case in the life sciences / 3D in-vitro research space.  
The goal is to answer a very practical BD question:

> Given a list of researchers and biotech professionals, who should we contact first — and why?

Instead of focusing on live scraping or automation complexity, this demo focuses on decision logic and explainability, which is the core challenge in real BD workflows.

---

## Problem Context

Business development teams typically work with raw lead lists from:

- LinkedIn searches  
- Conference attendee lists  
- Publication databases  
- CRM exports  

These lists are large, flat, and noisy.  
Not every “Director” is equally relevant, and not every researcher is ready to engage.

In practice, BD prioritization depends on signals such as:

- Role seniority and influence  
- Relevance of current research  
- Company maturity and readiness  
- Geographic ecosystem  
- Exposure to adjacent technologies  

This project converts those signals into a structured and explainable scoring system.

---

## High-Level Approach

The system follows a simple three-stage flow:

> Identify → Enrich → Rank

### 1. Identify

Leads are provided through a CSV file.  
This mirrors real workflows where data is exported from LinkedIn, conferences, or internal tools.

Each lead includes:

- Name  
- Title  
- Company  
- Person location  
- Company HQ  
- Research keywords  

### 2. Enrich

Each lead is enriched using rule-based, transparent signals:

- **Role fit**  
  - Senior roles (Director, Head, VP) score higher than individual contributors.  
- **Scientific intent**  
  - Keywords related to toxicology, DILI, preclinical safety, and 3D in-vitro models.  
- **Company intent**  
  - Company maturity inferred from size or known funding stage.  
- **Technographic fit**  
  - Exposure to in-vitro, organ-on-chip, or preclinical platforms.  
- **Location signal**  
  - Presence in major biotech hubs.  

Each signal contributes:

- A numeric score component  
- A human-readable explanation  

### 3. Rank

All enrichment signals are combined into a 0–100 probability score.  
Weights are adjustable through the UI.  
Leads are ranked by score.  

Each lead includes score drivers explaining why it ranked where it did.  
The emphasis is on transparency and trust, not black-box scoring.

---

## Dashboard

The Streamlit dashboard allows users to:

- Adjust scoring weights in real time  
- See leads re-rank instantly  
- Understand why a lead scored high or low  
- Export the ranked results as CSV  

The output is designed to be directly usable by a BD team.

---

## Input and Output

### Input

- **File:** `data/input_leads.csv`  
- Curated, realistic sample data representing leads from LinkedIn or conferences.

### Output

- **Generated file:** `ranked_leads.csv`  

Includes:

- Rank  
- Probability score (0–100)  
- Name, title, company  
- Person location and company HQ  
- Email (heuristically inferred)  
- LinkedIn search link  
- Suggested action  
- Score drivers  

---

## About Email and LinkedIn Fields

- Email addresses are inferred using a simple pattern (`first.last@company.com`) for demo purposes.  
- LinkedIn links are generated as search URLs, not scraped profiles.  

This avoids false claims while still reflecting real BD workflows.

---

## Demo vs Real-World Usage

This repository runs in **demo mode**.

### Demo mode

- Curated input data  
- Simulated enrichment  
- No API keys required  
- Fully reproducible  
- Focus on ranking logic  

### Real-world usage (conceptual)

In a production setting, the same architecture could integrate with:

- LinkedIn (via Proxycurl or Apify)  
- PubMed (E-utilities)  
- Crunchbase (funding intelligence)  
- Conference attendee data  

These integrations are documented separately but intentionally disabled here to keep evaluation simple.

---

## Why Not Machine Learning?

Early-stage BD problems usually lack:

- Clean labeled outcomes  
- Stable definitions of “success”  
- Sufficient historical data  

In such cases, transparent heuristics are more effective because teams need to:

- Trust the ranking  
- Explain it internally  
- Adjust priorities quickly  

Machine learning can be added later once outcome data exists.

---

## Tech Stack

- Python  
- Pandas  
- Streamlit  

Chosen for simplicity, clarity, and ease of evaluation.

---

## Running the Project Locally

