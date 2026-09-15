import streamlit as st
import pandas as pd
from io import BytesIO

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Reports | InsightIQ",
    page_icon="📄",
    layout="wide"
)

# ---------------- CHECK DATA ---------------- #

if "dataset" not in st.session_state:
    st.warning("⚠ Please upload a dataset first.")
    st.stop()

df = st.session_state["dataset"]

rows = len(df)
cols = len(df.columns)
missing = int(df.isnull().sum().sum())

quality = round(
    (1 - missing / (rows * cols)) * 100,
    2
)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="page-header">

<h1>📄 Reports Center</h1>

<p>
Generate professional reports and export your analysis in multiple formats.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- REPORT OVERVIEW ---------------- #

st.markdown("""
<h2 class="section-title">
Report Summary
</h2>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("📄", rows, "Rows"),
    ("📑", cols, "Columns"),
    ("⚠️", missing, "Missing"),
    ("✨", f"{quality}%", "Quality")
]

for col, card in zip([c1, c2, c3, c4], cards):

    with col:

        st.markdown(f"""
        <div class="stat-card">

        <h2>{card[0]}</h2>

        <h1>{card[1]}</h1>

        <p>{card[2]}</p>

        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- DATA PREVIEW ---------------- #

st.markdown("""
<h2 class="section-title">
Dataset Preview
</h2>
""", unsafe_allow_html=True)

st.dataframe(
    df.head(20),
    use_container_width=True
)

# ---------------- SUMMARY ---------------- #

st.markdown("""
<h2 class="section-title">
Statistical Summary
</h2>
""", unsafe_allow_html=True)

st.dataframe(
    df.describe(include="all").fillna(""),
    use_container_width=True
)

# ---------------- REPORT NOTES ---------------- #

st.markdown("""
<h2 class="section-title">
Executive Summary
</h2>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="insight-card">

✅ Dataset contains <b>{rows:,}</b> records.

<br><br>

✅ {cols} columns detected.

<br><br>

✅ Overall quality score is <b>{quality}%</b>.

<br><br>

✅ Missing values: <b>{missing}</b>

</div>
""", unsafe_allow_html=True)

# ---------------- CSV DOWNLOAD ---------------- #

st.markdown("""
<h2 class="section-title">
Download Dataset
</h2>
""", unsafe_allow_html=True)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download CSV",
    csv,
    file_name="InsightIQ_Report.csv",
    mime="text/csv"
)

# ---------------- EXCEL DOWNLOAD ---------------- #

buffer = BytesIO()

with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Dataset")

st.download_button(
    "📊 Download Excel",
    buffer.getvalue(),
    file_name="InsightIQ_Report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ---------------- REPORT STATUS ---------------- #

st.markdown("---")

st.success("✅ Report generated successfully.")

st.info(
    "You can now download the dataset in CSV or Excel format."
)
