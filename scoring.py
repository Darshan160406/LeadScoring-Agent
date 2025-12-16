def score_all_leads(leads, enrich_fn, weights):
    output = []

    max_score = sum(weights.values()) or 1

    for lead in leads:
        enriched = enrich_fn(lead)

        raw = (
            enriched["role_factor"] * weights["role"] +
            enriched["sci_factor"] * weights["science"] +
            enriched["company_factor"] * weights["company"] +
            enriched["tech_factor"] * weights["tech"] +
            enriched["location_factor"] * weights["location"]
        )

        probability = int((raw / max_score) * 100)

        output.append({
            **lead,
            "Probability": probability,
            "Score_Drivers": ", ".join(enriched["signal_reasons"])
        })

    output.sort(key=lambda x: x["Probability"], reverse=True)

    for i, row in enumerate(output, start=1):
        row["Rank"] = i

    return output
