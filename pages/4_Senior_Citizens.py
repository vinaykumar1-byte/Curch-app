import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

conn = sqlite3.connect("church.db")

df = pd.read_sql(
    "SELECT * FROM members",
    conn
)

# ---------------- DATE FIX ----------------
df["dob"] = pd.to_datetime(
    df["dob"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["dob"])

# ---------------- AGE CALCULATION ----------------
today = datetime.today()

df["age"] = (
    today.year - df["dob"].dt.year
)

# ---------------- FILTER ----------------
senior_df = df[
    df["age"] >= 60
]

st.subheader("👴 Senior Citizens")

st.dataframe(
    senior_df,
    use_container_width=True
)

# ---------------- DOWNLOAD ----------------
csv = senior_df.to_csv(index=False)

st.download_button(
    "⬇ Download Senior Citizen List",
    csv,
    "senior_citizens.csv"
)
