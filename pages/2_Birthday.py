import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("church.db")

df = pd.read_sql(
    "SELECT * FROM members",
    conn
)

df["dob"] = pd.to_datetime(
    df["dob"],
    errors="coerce"
)

month = st.selectbox(
    "Select Birthday Month",
    range(1,13)
)

birthday_df = df[
    df["dob"].dt.month == month
]

st.dataframe(
    birthday_df,
    use_container_width=True
)

csv = birthday_df.to_csv(index=False)

st.download_button(
    "⬇ Download Birthday List",
    csv,
    "birthday_list.csv"
)
