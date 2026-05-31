import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("church.db")

df = pd.read_sql(
    "SELECT * FROM members",
    conn
)

# ---------------- DATE FIX ----------------
df["marriage_date"] = pd.to_datetime(
    df["marriage_date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["marriage_date"])

# ---------------- MONTH SELECT ----------------
month = st.selectbox(
    "Select Anniversary Month",
    range(1,13)
)

ann_df = df[
    df["marriage_date"].dt.month == month
]

st.subheader("💍 Wedding Anniversary List")

st.dataframe(
    ann_df,
    use_container_width=True
)

# ---------------- DOWNLOAD ----------------
csv = ann_df.to_csv(index=False)

st.download_button(
    "⬇ Download Anniversary List",
    csv,
    "anniversary_list.csv"
)
