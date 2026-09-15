import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Insights | InsightIQ",
    page_icon="🤖",
    layout="wide"
)

# ---------------- DATA CHECK ---------------- #

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

numeric = df.select_dtypes(include=np.number)

categorical = df.select_dtypes(exclude=np.number)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="page-header">

<h1>🤖 AI Insights</h1>

<p>
InsightIQ automatically analyzes your dataset and highlights important findings.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- HEALTH SCORE ---------------- #

st.markdown(
"""
<h2 class="section-title">
Dataset Health
</h2>
""",
unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(f"""
<div class="stat-card">

<h2>✨</h2>

<h1>{quality}%</h1>

<p>Health Score</p>

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown(f"""
<div class="stat-card">

<h2>📄</h2>

<h1>{rows}</h1>

<p>Total Rows</p>

</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown(f"""
<div class="stat-card">

<h2>📑</h2>

<h1>{cols}</h1>

<p>Total Columns</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- EXECUTIVE SUMMARY ---------------- #

st.markdown("""
<h2 class="section-title">
Executive Summary
</h2>
""", unsafe_allow_html=True)

summary = []

summary.append(
    f"The dataset contains **{rows:,} rows** and **{cols} columns**."
)

summary.append(
    f"The overall quality score is **{quality}%**."
)

if missing == 0:
    summary.append(
        "No missing values were detected."
    )
else:
    summary.append(
        f"There are **{missing}** missing values."
    )

summary.append(
    f"Numeric Columns: **{len(numeric.columns)}**"
)

summary.append(
    f"Categorical Columns: **{len(categorical.columns)}**"
)

for item in summary:

    st.markdown(f"""
<div class="insight-card">
💡 {item}
</div>
""",
unsafe_allow_html=True)

# ---------------- STATISTICS ---------------- #

st.markdown("""
<h2 class="section-title">
Statistical Summary
</h2>
""",
unsafe_allow_html=True)

if not numeric.empty:

    st.dataframe(
        numeric.describe().T,
        use_container_width=True
    )

    # ---------------- STRONG CORRELATIONS ---------------- #

st.markdown("""
<h2 class="section-title">
Strong Correlations
</h2>
""",
unsafe_allow_html=True)

if len(numeric.columns) >= 2:

    corr = numeric.corr()

    pairs = []

    for i in corr.columns:
        for j in corr.columns:

            if i != j:

                value = corr.loc[i, j]

                if abs(value) >= 0.7:

                    pairs.append(
                        (i, j, round(value, 2))
                    )

    if pairs:

        shown = set()

        for a, b, value in pairs:

            if (b, a) not in shown:

                shown.add((a, b))

                st.markdown(f"""
<div class="insight-card">

📈 <b>{a}</b> and <b>{b}</b>

<br>

Correlation : <b>{value}</b>

</div>
""",
unsafe_allow_html=True)

    else:

        st.info(
            "No strong correlations detected."
        )

# ---------------- RECOMMENDATIONS ---------------- #

st.markdown("""
<h2 class="section-title">
AI Recommendations
</h2>
""",
unsafe_allow_html=True)

recommendations = []

if missing > 0:

    recommendations.append(
        "Clean missing values before building ML models."
    )

if quality >= 95:

    recommendations.append(
        "Dataset is clean enough for visualization and predictive analytics."
    )

if len(numeric.columns) >= 2:

    recommendations.append(
        "Correlation analysis indicates suitable features for predictive modeling."
    )

if len(categorical.columns):

    recommendations.append(
        "Categorical columns can be encoded for machine learning."
    )

recommendations.append(
    "Generate a professional report from the Reports page."
)

for rec in recommendations:

    st.markdown(f"""
<div class="insight-card">
✅ {rec}
</div>
""",
unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #

st.success(
    "Analysis completed successfully."
)