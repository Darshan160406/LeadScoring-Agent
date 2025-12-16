import streamlit as st
import pandas as pd

from enrichment import enrich_lead
from scoring import score_all_leads
from utils import infer_business_email, linkedin_search_url

st.set_page_config(layout="wide", page_title="Lead Scoring Agent")

st.title("Lead Scoring Agent – 3D In-Vitro Therapy Research")

st.markdown(
    "Prioritizes researchers and industry professionals based on their "
    "**propensity to engage with 3D in-vitro models**. "
    "Scoring is heuristic and adjustable for BD decision-making."
)

# Load data
data = pd.read_csv("data/input_leads.csv")

# Sidebar controls
with st.sidebar:
    st.header("Scoring Weights")
    weights = {
        "role": st.slider("Role Fit", 0, 40, 30),
        "science": st.slider("Scientific Intent", 0, 50, 40),
        "company": st.slider("Company Intent", 0, 30, 20),
        "tech": st.slider("Technographic Fit", 0, 25, 15),
        "location": st.slider("Location Hub", 0, 20, 10),
    }

records = data.to_dict(orient="records")
ranked = score_all_leads(records, enrich_lead, weights)
df = pd.DataFrame(ranked)

# Add missing required fields
df["Email"] = df.apply(
    lambda r: infer_business_email(r["Name"], r["Company"]), axis=1
)
df["LinkedIn"] = df.apply(
    lambda r: linkedin_search_url(r["Name"], r["Company"]), axis=1
)
df["Action"] = "Review / Reach Out"

display_cols = [
    "Rank",
    "Probability",
    "Name",
    "Title",
    "Company",
    "Person_Location",
    "Company_HQ",
    "Email",
    "LinkedIn",
    "Action",
    "Score_Drivers"
]

st.subheader("Ranked Leads")
st.dataframe(df[display_cols], use_container_width=True)

st.download_button(
    "Download as CSV",
    df.to_csv(index=False).encode("utf-8"),
    file_name="ranked_leads.csv",
    mime="text/csv"
)
