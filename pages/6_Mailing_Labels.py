import streamlit as st
import pandas as pd
import sqlite3

from docx import Document
from docx.shared import Inches

st.set_page_config(layout="wide")

# ---------------- DATABASE ----------------
conn = sqlite3.connect("church.db")

df = pd.read_sql(
    "SELECT * FROM members",
    conn
)

st.title("📮 Mailing Labels")

# ---------------- SEARCH ----------------
search = st.text_input("Search Member")

if search:

    df = df[
        df["head_name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

st.dataframe(df)

# ---------------- GENERATE WORD FILE ----------------
if st.button("GENERATE MAILING LABEL DOC"):

    doc = Document()

    # ---------------- A4 PAGE ----------------
    section = doc.sections[0]

    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)

    # ---------------- 3 COLUMN TABLE ----------------
    table = doc.add_table(
        rows=0,
        cols=3
    )

    table.autofit = True

    row_cells = None

    for i, row in df.iterrows():

        if i % 3 == 0:

            row_cells = table.add_row().cells

        col_index = i % 3

        text = f"""Mr./Mrs. {row['head_name']}
{row['address']}
{row['city']} - {row['pin_code']}
{row['mobile']}"""

        row_cells[col_index].text = text

    # ---------------- SAVE ----------------
    file_path = "mailing_labels.docx"

    doc.save(file_path)

    # ---------------- DOWNLOAD ----------------
    with open(file_path, "rb") as file:

        st.download_button(
            label="⬇ Download Mailing Labels Word File",
            data=file,
            file_name="mailing_labels.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
