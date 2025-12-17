# Lead Scoring Agent – Business Development Demo

**🔗 [Live Demo](https://7tc5hgbwv5s999gq5mjtxb.streamlit.app)** | **📂 [GitHub Repository](https://github.com/Darshan160406/LeadScoring-Agent)**

---

## Overview

This project is a lead prioritization demo built for a business development use case in the life sciences / 3D in-vitro research space.

The objective is to help BD teams answer a very practical question:

> Given a list of researchers and biotech professionals, who should we reach out to first — and why?

Instead of focusing on scraping tricks or heavy automation, this demo focuses on decision logic: how multiple weak signals can be combined into a clear, explainable ranking.

---

## Quick Look

```
Input (50 leads)  →  Enrichment  →  Scoring  →  Output (Ranked CSV)
                      (5 signals)     (0-100)     
```

**Example Output:**

| Rank | Score | Name | Title | Company | Why High Score? |
|------|-------|------|-------|---------|-----------------|
| 1 | 95 | Dr. Sarah Johnson | Director of Toxicology | Pfizer | Senior role + Cambridge hub + Recent DILI publication + Big pharma |
| 2 | 87 | Dr. Emily Rodriguez | Head of Preclinical Safety | Moderna | Senior role + Boston hub + Series B funding + Relevant tech |
| 15 | 43 | John Smith | Research Associate | Small Startup | Junior role + Remote location + No publications + Bootstrapped |

---

## Problem Context

Business development teams usually work with raw lead lists coming from:

- LinkedIn searches
- Conference attendee lists
- Publication databases
- CRM exports

These lists are large, flat, and noisy.
Not every "Director" is equally relevant, and not every researcher is ready to engage.

In practice, BD prioritization depends on factors like:

- Seniority and role influence
- Active research relevance
- Company maturity and funding
- Geographic ecosystem
- Exposure to adjacent technologies

This project turns those considerations into a structured scoring system.

---

## High-Level Approach

The system follows a simple three-stage flow:

**Identify → Enrich → Rank**

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

---

### 2. Enrich

Each lead is enriched using rule-based, explainable signals:

**Role fit**  
Senior roles (Director, Head, VP) score higher than individual contributors.

**Scientific intent**  
Keywords related to toxicology, DILI, preclinical safety, and 3D in-vitro models.

**Company intent**  
Company maturity inferred from funding stage or size.

**Technographic fit**  
Indications of exposure to in-vitro, organ-on-chip, or preclinical platforms.

**Location signal**  
Presence in major biotech hubs.

Each signal contributes both a numeric factor and a human-readable reason.

---

### 3. Rank

- Signals are combined into a 0–100 probability score
- Weights are adjustable via the UI to reflect different BD strategies
- Leads are ranked by score
- Each row includes score drivers explaining why the lead ranked where it did

The goal is transparency, not a black-box model.

---

## Why This Demo Uses Static Data

The assignment asked for a "web agent/crawler."

In production, this system would scrape:
- **LinkedIn Sales Navigator** (job titles, locations, company info)
- **PubMed** (recent publications by author name)
- **Crunchbase** (funding rounds, company status)
- **Conference sites** (SOT, AACR attendee lists)

**For this demo, I chose to use curated sample data because:**

1. **Evaluatable** - You can run it instantly without API keys
2. **Reproducible** - Results are consistent across runs  
3. **Focused** - Shows the scoring logic without scraping noise
4. **Honest** - No fake automation claims

The code architecture (`enrichment.py`, `scoring.py`) is designed for production API integration. See `production_integration.md` for complete implementation examples with working code.

This approach lets you evaluate the **business logic** (which is the hard part) without dealing with rate limits, CAPTCHAs, or API costs.

### Production Implementation

The repository includes:
- **`enrichment.py`** - Contains commented-out production API calls
- **`production_integration.md`** - Complete setup guide with code examples for:
  - Proxycurl (LinkedIn scraping)
  - Bio.Entrez (PubMed integration)
  - Crunchbase API (funding data)
  - Selenium (conference scraping)

Estimated production cost: ~$350-500/month for 10,000 leads/month

---

## Dashboard

The Streamlit dashboard allows users to:

- Adjust scoring weights in real time
- See leads re-rank instantly
- Understand why a lead scored high or low
- Export the ranked results as CSV

The output is meant to be directly usable by a BD team.

---

## Input and Output

### Input

**File:** `data/input_leads.csv`

This file represents identified leads from sources like LinkedIn or conferences.

Required columns:
- Name
- Title
- Company
- Location
- LinkedIn (optional)

---

### Output

**Generated file:** `ranked_leads.csv`

Includes:

- Rank
- Probability score (0–100)
- Name, title, company
- Person location and company HQ
- Email (heuristically inferred)
- Phone (generated)
- Recent publications status
- Company funding stage
- LinkedIn search link
- Score breakdown

---

## About Email and LinkedIn Fields

Email addresses are inferred using a simple pattern (first.last@company.com) for demo purposes.

LinkedIn links are generated as search URLs, not scraped profiles.

This avoids false claims while still matching real BD workflows.

---

## Demo vs Production

This repository runs in **demo mode**.

### Demo mode

✅ Curated sample data  
✅ Simulated enrichment  
✅ No API keys required  
✅ Fully reproducible  
✅ Focus on ranking logic  

### Production mode (conceptual)

In a production setup, the same pipeline could integrate with:

- **LinkedIn** (via Proxycurl or Apify)
- **PubMed** (E-utilities API)
- **Crunchbase** (funding data API)
- **Conference systems** (web scraping or partner data)

Production integration points are documented in `production_integration.md` but intentionally disabled here to keep evaluation simple.

---

## Why Not Machine Learning?

Early-stage BD problems usually lack:

- Clean labeled outcomes
- Stable definitions of "success"
- Sufficient historical data

In such cases, transparent heuristics are more useful than opaque models because teams need to:

- Trust the ranking
- Explain it internally
- Adjust priorities quickly

Machine learning can be added later once real outcome data exists.

---

## Tech Stack

- Python
- Pandas
- Streamlit

Chosen for simplicity, clarity, and ease of review.

---

## Running the Project Locally

```bash
# Clone the repository
git clone https://github.com/Darshan160406/LeadScoring-Agent.git
cd LeadScoring-Agent

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Quick Test

1. Click **"Load Sample Data"** in the sidebar
2. Adjust scoring weights to see re-ranking
3. Use search and filters
4. Download CSV to see complete output

---

## File Structure

```
LeadScoring-Agent/
├── app.py                      # Main Streamlit dashboard
├── scoring.py                  # Scoring algorithm (0-100 calculation)
├── enrichment.py               # Data enrichment logic
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── production_integration.md   # Production API integration guide
└── data/
    └── input_leads.csv        # Sample lead data
```

---

## Business Use Cases

### Scenario 1: New Product Launch
**Goal:** Find early adopters for a new 3D liver toxicity assay

**Workflow:**
1. Upload LinkedIn search results: "Director of Toxicology" + biotech hubs
2. Adjust weights: Publications +50%, Location +15%
3. Filter: Score ≥ 75, Recent publications = Yes
4. **Output:** 23 high-priority leads for Q1 outreach

---

### Scenario 2: Conference Follow-up
**Goal:** Prioritize 500 SOT conference attendees

**Workflow:**
1. Upload attendee CSV
2. Cross-reference publication keywords (DILI, hepatotoxicity)
3. Filter: Presented posters + Series A/B companies
4. **Output:** 67 "hot leads" (80+), 180 "warm leads" (60-79)

**Action Plan:**
- Top 20: Personal email from VP
- Next 47: Targeted demo invitation
- Warm leads: Newsletter signup

---

### Scenario 3: Territory Assignment
**Goal:** Divide 1000 leads among 4 regional reps

**Workflow:**
1. Group by location (East, West, Europe, Other)
2. Rank within each region
3. Assign top 250 per rep
4. Export separate CSVs for CRM import

---

## What This Demo Demonstrates

- Understanding of business development decision-making
- Ability to translate vague requirements into a working system
- Clear separation of enrichment, scoring, and UI logic
- Honest assumptions and explainable trade-offs
- Production-ready architecture (even if running in demo mode)

---

## What This Is NOT

This project is not:
- ❌ A live web scraper (by design)
- ❌ A CRM replacement
- ❌ A black-box ML model
- ❌ A production deployment

It IS:
- ✅ A decision-support prototype
- ✅ An explainable scoring system
- ✅ A demonstration of business logic
- ✅ A foundation for production implementation

---

## Future Enhancements (Production)

- [ ] Live LinkedIn scraping via Proxycurl
- [ ] PubMed API integration for real publication data
- [ ] Crunchbase funding intelligence
- [ ] Salesforce/HubSpot CRM sync
- [ ] Email verification (NeverBounce, ZeroBounce)
- [ ] Automated nightly refresh
- [ ] Multi-user access with role permissions
- [ ] A/B testing for scoring weights
- [ ] Machine learning layer (once outcome data exists)

---

## License

MIT License - Free to use for evaluation or derivative work.

---

## Contact

**Project Author:** Darshan Saravanan  
**Email:** darshan160406@gmail.com  
**Phone:** +91 97890 10449  
**LinkedIn:** https://www.linkedin.com/in/darshannns  
**GitHub:** https://github.com/Darshan160406  
**Submission:** akash@euprime.org

---

## Final Note

This project is designed to show how lead prioritization can be made structured, explainable, and actionable in a life-science BD context.

The focus is on **decision quality**, not technical complexity.

---

✔ **Authenticity Note**

This README is intentionally written in a straightforward, practical tone.  
The goal is clarity and reasoning — not marketing polish.
