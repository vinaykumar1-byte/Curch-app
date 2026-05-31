import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(layout="wide")

# ---------------- DATABASE ----------------
conn = sqlite3.connect("church.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    family_code TEXT,
    head_name TEXT,
    address TEXT,
    city TEXT,
    pin_code TEXT,
    tel_res TEXT,
    tel_office TEXT,
    mobile TEXT,
    email1 TEXT,
    prayer_area TEXT,
    member_since TEXT,
    status TEXT,
    dob TEXT,
    marriage_date TEXT,
    relationship TEXT
)
""")

conn.commit()

# ---------------- TITLE ----------------
st.markdown("""
<h2 style='text-align:center;
background-color:#00dede;
padding:10px;'>
DELHI MALAYALAM CONGREGATION (CNI)
</h2>
""", unsafe_allow_html=True)

# ---------------- FORM ----------------
with st.form("member_form"):

    col1, col2 = st.columns(2)

    with col1:

        family_code = st.text_input("Family Code")
        head_name = st.text_input("Head Of Family")

        address = st.text_area("Address Home")

        city = st.text_input("Geo Location")
        pin_code = st.text_input("Pin Code")

        tel_res = st.text_input("Tel Res")
        tel_office = st.text_input("Tel Office")

        mobile = st.text_input("Mobile Phone")

    with col2:

        email1 = st.text_input("Email Address")

        prayer_area = st.selectbox(
            "Prayer Area",
            ["CENTRAL", "NORTH", "SOUTH"]
        )

        member_since = st.date_input("Member Since")

        status = st.selectbox(
            "Status",
            ["ACTIVE", "INACTIVE"]
        )

        dob = st.date_input("Date Of Birth")

        marriage_date = st.date_input(
            "Marriage Anniversary"
        )

        relationship = st.selectbox(
            "Relationship",
            ["Self", "Wife", "Son", "Daughter"]
        )

    photo = st.file_uploader(
        "Upload Family Photo",
        type=["jpg", "png", "jpeg"]
    )

    submit = st.form_submit_button("💾 SAVE DATA")

# ---------------- SAVE ----------------
if submit:

    cursor.execute("""
    INSERT INTO members (
        family_code,
        head_name,
        address,
        city,
        pin_code,
        tel_res,
        tel_office,
        mobile,
        email1,
        prayer_area,
        member_since,
        status,
        dob,
        marriage_date,
        relationship
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        family_code,
        head_name,
        address,
        city,
        pin_code,
        tel_res,
        tel_office,
        mobile,
        email1,
        prayer_area,
        str(member_since),
        status,
        str(dob),
        str(marriage_date),
        relationship
    ))

    conn.commit()

    st.success("✅ Data Saved Successfully")

# ---------------- VIEW DATA ----------------
st.subheader("Saved Members")

df = pd.read_sql(
    "SELECT * FROM members",
    conn
)

st.dataframe(
    df,
    use_container_width=True
)

# ---------------- HISTORICAL DATA UPLOAD ----------------

st.subheader("📂 Upload Historical Data")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file is not None:

    upload_df = pd.read_excel(uploaded_file)

    st.write("Preview Data")

    st.dataframe(upload_df)

    if st.button("UPLOAD DATA TO DATABASE"):

        upload_df.to_sql(
            "members",
            conn,
            if_exists="append",
            index=False
        )

        st.success("✅ Historical Data Uploaded Successfully")
