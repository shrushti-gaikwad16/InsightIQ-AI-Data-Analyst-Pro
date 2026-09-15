import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Dashboard | InsightIQ",
    page_icon="📊",
    layout="wide"
)

# ---------------- CHECK DATA ---------------- #

if "dataset" not in st.session_state:

    st.warning("⚠ Please upload a dataset first.")

    st.stop()

df = st.session_state["dataset"]

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="page-header">

<h1>
📊 Analytics Dashboard
</h1>

<p>
Get a complete overview of your uploaded dataset with interactive analytics and AI-powered summaries.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- DATA ---------------- #

rows = len(df)

cols = len(df.columns)

missing = int(df.isnull().sum().sum())

quality = round(
    (
        1 - (
            missing /
            (rows * cols)
        )
    ) * 100,
    2
)

numeric_cols = df.select_dtypes(include="number").columns.tolist()

categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

# ---------------- KPI CARDS ---------------- #

c1, c2, c3, c4 = st.columns(4)

cards = [

    ("📄", rows, "Rows"),

    ("📑", cols, "Columns"),

    ("⚠️", missing, "Missing Values"),

    ("✨", f"{quality}%", "Quality Score")

]

for col, card in zip(
    [c1, c2, c3, c4],
    cards
):

    with col:

        st.markdown(
            f"""
            <div class="stat-card">

            <h2>{card[0]}</h2>

            <h1>{card[1]}</h1>

            <p>{card[2]}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- QUICK SUMMARY ---------------- #

left, right = st.columns([2, 1])

with left:

    st.markdown("""
    <div class="upload-card">

    <h2>
    📋 Dataset Summary
    </h2>

    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

with right:

    st.markdown("""
    <div class="upload-card">

    <h2>
    🤖 AI Snapshot
    </h2>

    </div>
    """, unsafe_allow_html=True)

    st.success(f"Dataset contains **{rows:,}** rows.")

    st.info(f"Total columns : **{cols}**")

    if missing == 0:

        st.success("No missing values detected.")

    else:

        st.warning(
            f"{missing} missing values detected."
        )

    st.success(
        f"Overall Quality : {quality}%"
    )

# ---------------- CHARTS ---------------- #

st.markdown(
"""
<h2 class='section-title'>
📈 Data Overview
</h2>
""",
unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    if numeric_cols:

        selected = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        fig = px.histogram(
            df,
            x=selected,
            nbins=30,
            title=f"Distribution of {selected}"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col2:

    if categorical_cols:

        category = st.selectbox(
            "Select Category",
            categorical_cols
        )

        counts = (
            df[category]
            .value_counts()
            .reset_index()
        )

        counts.columns = [category, "Count"]

        fig = px.pie(
            counts,
            names=category,
            values="Count",
            hole=0.5,
            title=f"{category} Distribution"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================================================
# MISSING VALUES ANALYSIS
# ==========================================================

st.markdown(
"""
<h2 class='section-title'>
⚠ Missing Values Analysis
</h2>
""",
unsafe_allow_html=True
)

missing_data = (
    df.isnull()
      .sum()
      .sort_values(ascending=False)
)

missing_data = missing_data[missing_data > 0]

if len(missing_data) > 0:

    fig = px.bar(
        x=missing_data.index,
        y=missing_data.values,
        labels={
            "x": "Columns",
            "y": "Missing Values"
        },
        title="Missing Values by Column"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.success("🎉 Your dataset has no missing values.")

# ==========================================================
# CORRELATION MATRIX
# ==========================================================

if len(numeric_cols) >= 2:

    st.markdown(
    """
    <h2 class='section-title'>
    🔥 Correlation Heatmap
    </h2>
    """,
    unsafe_allow_html=True
    )

    corr = df[numeric_cols].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="Purples",
        aspect="auto"
    )

    fig.update_layout(
        template="plotly_dark",
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# DATASET INFORMATION
# ==========================================================

st.markdown(
"""
<h2 class='section-title'>
📋 Dataset Information
</h2>
""",
unsafe_allow_html=True
)

info_df = pd.DataFrame({

    "Column": df.columns,

    "Data Type": df.dtypes.astype(str),

    "Missing": df.isnull().sum().values,

    "Unique Values": df.nunique().values

})

st.dataframe(
    info_df,
    use_container_width=True
)

# ==========================================================
# AI INSIGHTS
# ==========================================================

st.markdown(
"""
<h2 class='section-title'>
🤖 AI Smart Insights
</h2>
""",
unsafe_allow_html=True
)

insights = []

insights.append(
    f"Dataset contains **{rows:,} rows** and **{cols} columns**."
)

if quality >= 95:
    insights.append(
        "Excellent data quality detected."
    )
elif quality >= 80:
    insights.append(
        "Good data quality with minor cleaning required."
    )
else:
    insights.append(
        "Data cleaning is recommended before analysis."
    )

if missing == 0:
    insights.append(
        "No missing values detected."
    )
else:
    insights.append(
        f"{missing} missing values found."
    )

if numeric_cols:
    insights.append(
        f"{len(numeric_cols)} numeric columns available for analysis."
    )

if categorical_cols:
    insights.append(
        f"{len(categorical_cols)} categorical columns detected."
    )

col1, col2 = st.columns(2)

for i, insight in enumerate(insights):

    if i % 2 == 0:

        with col1:

            st.markdown(
                f"""
                <div class="insight-card">
                💡 {insight}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        with col2:

            st.markdown(
                f"""
                <div class="insight-card">
                🚀 {insight}
                </div>
                """,
                unsafe_allow_html=True
            )

# ==========================================================
# QUICK ACTIONS
# ==========================================================

st.markdown(
"""
<h2 class='section-title'>
⚡ Quick Actions
</h2>
""",
unsafe_allow_html=True
)

a1, a2, a3 = st.columns(3)

with a1:
    st.info("📊 Open **Visualizations** from the sidebar.")

with a2:
    st.info("🤖 Explore **AI Insights** from the sidebar.")

with a3:
    st.info("📄 Generate professional **Reports**.")

# ==========================================================
# DOWNLOAD DATA
# ==========================================================

st.markdown(
"""
<div class="download-card">

<h3>⬇ Download Dataset</h3>

<p>
Download the currently loaded dataset as CSV.
</p>

</div>
""",
unsafe_allow_html=True
)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download CSV",
    csv,
    file_name="InsightIQ_Dataset.csv",
    mime="text/csv"
)
