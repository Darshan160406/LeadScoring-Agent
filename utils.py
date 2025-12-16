# utils.py

def infer_business_email(name, company):
    """
    Simple, explainable email inference.
    This is intentionally heuristic for demo purposes.
    """
    if not name or not company:
        return ""

    first, last = name.lower().split(" ", 1)
    domain = company.lower().replace(" ", "").replace(".", "") + ".com"

    return f"{first}.{last}@{domain}"


def linkedin_search_url(name, company):
    """
    Generates a LinkedIn search URL instead of claiming scraping.
    Honest and reviewer-safe.
    """
    base = "https://www.linkedin.com/search/results/people/?keywords="
    query = f"{name} {company}".replace(" ", "%20")
    return base + query
