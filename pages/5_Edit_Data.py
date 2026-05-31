import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "church.db",
    check_same_thread=False
)

df = pd.read_sql(
    "SELECT * FROM members",
    conn
)

st.subheader("✏ Edit Existing Data")

edited_df = st.data_editor(
    df,
    use_container_width=True,
    num_rows="dynamic"
)

if st.button("💾 Update Database"):

    edited_df.to_sql(
        "members",
        conn,
        if_exists="replace",
        index=False
    )

    st.success("✅ Database Updated")
