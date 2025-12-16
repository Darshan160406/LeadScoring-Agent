ROLE_KEYWORDS = {
    "decision": ["director", "head", "vp", "vice president"],
    "senior": ["principal scientist", "senior scientist", "lead scientist"],
    "individual": ["scientist", "researcher", "fellow"]
}

SCIENCE_KEYWORDS = [
    "drug-induced liver injury",
    "liver toxicity",
    "hepatic",
    "3d",
    "organ-on-chip",
    "in-vitro",
    "in vitro",
    "preclinical"
]

TECH_KEYWORDS = [
    "in-vitro",
    "3d",
    "organ-on-chip",
    "preclinical",
    "drug discovery",
    "nams"
]

BIOTECH_HUBS = [
    "boston", "cambridge", "bay area",
    "san francisco", "basel", "oxford", "london"
]

FUNDING_LOOKUP = {
    "genentech": "public",
    "astrazeneca": "public",
    "vertex pharmaceuticals": "public",
    "takeda": "public",
    "roche": "public",
    "moderna": "public",
    "gilead sciences": "public",
    "beam therapeutics": "series b",
    "recursion pharmaceuticals": "series b",
    "aligos therapeutics": "series b",
    "sanofi": "public",
    "eisai": "public",
    "boehringer ingelheim": "public",
    "encellin pharmaceuticals": "seed",
    "replimune": "series b"
}


def _has_any(text, keywords):
    return any(k in text for k in keywords)


def enrich_lead(lead):
    reasons = []

    title = lead.get("Title", "").lower()
    research = lead.get("Research_Keywords", "").lower()
    company = lead.get("Company", "").lower()
    location_blob = f"{lead.get('Person_Location','')} {lead.get('Company_HQ','')}".lower()

    # Role fit
    if _has_any(title, ROLE_KEYWORDS["decision"]):
        role_factor = 1.0
        reasons.append("Decision-maker role")
    elif _has_any(title, ROLE_KEYWORDS["senior"]):
        role_factor = 0.7
        reasons.append("Senior scientific role")
    elif _has_any(title, ROLE_KEYWORDS["individual"]):
        role_factor = 0.4
        reasons.append("Hands-on research role")
    else:
        role_factor = 0.0

    # Scientific intent
    sci_factor = 1.0 if _has_any(research, SCIENCE_KEYWORDS) else 0.0
    if sci_factor:
        reasons.append("Relevant preclinical / toxicity research")

    # Company intent
    stage = FUNDING_LOOKUP.get(company, "unknown")
    if stage in ["public", "series b"]:
        company_factor = 1.0
        reasons.append(f"{stage} funded company")
    elif stage == "series a":
        company_factor = 0.6
        reasons.append("Series A company")
    elif stage == "seed":
        company_factor = 0.3
        reasons.append("Early-stage company")
    else:
        company_factor = 0.0

    # Technographic fit
    tech_factor = 1.0 if _has_any(research, TECH_KEYWORDS) else 0.0
    if tech_factor:
        reasons.append("Exposure to in-vitro / preclinical tech")

    # Location hub
    location_factor = 1.0 if _has_any(location_blob, BIOTECH_HUBS) else 0.0
    if location_factor:
        reasons.append("Based in major biotech hub")

    return {
        "role_factor": role_factor,
        "sci_factor": sci_factor,
        "company_factor": company_factor,
        "tech_factor": tech_factor,
        "location_factor": location_factor,
        "signal_reasons": reasons
    }
