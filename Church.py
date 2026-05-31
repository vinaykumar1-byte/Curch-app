# Church.py

import streamlit as st

st.set_page_config(
    page_title="Delhi Malayalam Congregation",
    layout="wide"
)

# ---------------- HIDE STREAMLIT ----------------
hide_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

st.markdown(hide_style, unsafe_allow_html=True)

# ---------------- HEADER WITH IMAGE ----------------
col1, col2 = st.columns([1,5])

with col1:
    st.image("church.jpg", width=120)

with col2:
    st.markdown("""
    <h1 style='
    color:red;
    margin-top:20px;
    '>
    DELHI MALAYALAM CONGREGATION
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h4 style='
    color:green;
    margin-top:-15px;
    '>
    DIOCESE OF DELHI
    </h4>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- MENU ----------------
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("📝 DATA ENTRY "):
        st.page_link("pages/1_Data_Entry.py", label="📝 DATA ENTRY")

with col2:
    if st.button("🎂  BIRTHDAY  "):
        st.switch_page("pages/2_Birthday.py")

with col3:
    if st.button("💍 ANNIVERSARY"):
        st.switch_page("pages/3_Anniversary.py")

with col4:
    if st.button("👴 SR CITIZENS"):
        st.switch_page("pages/4_Senior_Citizens.py")

with col5:
    if st.button("✏ EDIT  DATA "):
        st.switch_page("pages/5_Edit_Data.py")
with col6:
    if st.button("📮 MAILING LABELS"):
        st.switch_page("pages/6_Mailing_Labels.py")


st.write("")
