import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Visualizations | InsightIQ",
    page_icon="📊",
    layout="wide"
)

# ---------------- DATA CHECK ---------------- #

if "dataset" not in st.session_state:
    st.warning("⚠ Please upload a dataset first.")
    st.stop()

df = st.session_state["dataset"]

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="page-header">
<h1>📊 Visual Analytics</h1>
<p>
Explore your dataset through interactive charts and uncover meaningful insights.
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- KPI CARDS ---------------- #

rows = len(df)
cols = len(df.columns)
missing = int(df.isnull().sum().sum())

quality = round(
    (1 - missing / (rows * cols)) * 100,
    2
)

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("📄", "Rows", rows),
    ("📑", "Columns", cols),
    ("⚠", "Missing", missing),
    ("✨", "Quality", f"{quality}%")
]

for col, card in zip([c1, c2, c3, c4], cards):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <h2>{card[0]}</h2>
            <h1>{card[2]}</h1>
            <p>{card[1]}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

numeric_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

tabs = st.tabs([
    "📈 Distribution",
    "📊 Comparison",
    "🎯 Relationship",
    "🔥 Correlation"
])

# ===================================================
# TAB 1
# ===================================================

with tabs[0]:

    st.markdown("## Histogram")

    if numeric_cols:

        column = st.selectbox(
            "Choose Numeric Column",
            numeric_cols
        )

        bins = st.slider(
            "Number of Bins",
            5,
            100,
            30
        )

        fig = px.histogram(
            df,
            x=column,
            nbins=bins,
            title=f"Distribution of {column}"
        )

        fig.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.info(f"""
Minimum : {df[column].min()}

Maximum : {df[column].max()}

Mean : {round(df[column].mean(),2)}

Median : {round(df[column].median(),2)}
""")

    else:
        st.warning("No numeric columns available.")

# ===================================================
# TAB 2
# ===================================================

with tabs[1]:

    left, right = st.columns(2)

    with left:

        st.subheader("Bar Chart")

        if categorical_cols and numeric_cols:

            x = st.selectbox(
                "Category",
                categorical_cols,
                key="barx"
            )

            y = st.selectbox(
                "Numeric Value",
                numeric_cols,
                key="bary"
            )

            agg = (
                df.groupby(x)[y]
                .mean()
                .reset_index()
            )

            fig = px.bar(
                agg,
                x=x,
                y=y,
                color=y,
                title=f"{y} by {x}"
            )

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with right:

        st.subheader("Pie Chart")

        if categorical_cols:

            pie_col = st.selectbox(
                "Select Category",
                categorical_cols,
                key="pie"
            )

            pie = (
                df[pie_col]
                .value_counts()
                .reset_index()
            )

            pie.columns = [pie_col, "Count"]

            fig = px.pie(
                pie,
                names=pie_col,
                values="Count",
                hole=0.45,
                title=f"{pie_col} Distribution"
            )

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # ===================================================
# TAB 3 - RELATIONSHIP
# ===================================================

with tabs[2]:

    left, right = st.columns(2)

    with left:

        st.subheader("Scatter Plot")

        if len(numeric_cols) >= 2:

            scatter_x = st.selectbox(
                "X Axis",
                numeric_cols,
                key="scatter_x"
            )

            scatter_y = st.selectbox(
                "Y Axis",
                numeric_cols,
                index=1 if len(numeric_cols) > 1 else 0,
                key="scatter_y"
            )

            color_col = None

            if categorical_cols:
                color_col = st.selectbox(
                    "Color By (Optional)",
                    ["None"] + categorical_cols,
                    key="scatter_color"
                )

                if color_col == "None":
                    color_col = None

            fig = px.scatter(
                df,
                x=scatter_x,
                y=scatter_y,
                color=color_col,
                title=f"{scatter_x} vs {scatter_y}"
            )

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with right:

        st.subheader("Box Plot")

        if numeric_cols:

            box_col = st.selectbox(
                "Numeric Column",
                numeric_cols,
                key="box"
            )

            fig = px.box(
                df,
                y=box_col,
                points="outliers",
                title=f"Box Plot of {box_col}"
            )

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# ===================================================
# TAB 4 - CORRELATION
# ===================================================

with tabs[3]:

    st.subheader("Correlation Heatmap")

    if len(numeric_cols) >= 2:

        corr = df[numeric_cols].corr()

        heatmap = go.Figure(
            data=go.Heatmap(
                z=corr.values,
                x=corr.columns,
                y=corr.columns,
                text=corr.round(2).values,
                texttemplate="%{text}"
            )
        )

        heatmap.update_layout(
            template="plotly_dark",
            height=650,
            title="Correlation Matrix"
        )

        st.plotly_chart(
            heatmap,
            use_container_width=True
        )

    else:

        st.info("Need at least two numeric columns.")

# ===================================================
# MISSING VALUES
# ===================================================

st.markdown("---")

st.markdown("## ⚠ Missing Values Analysis")

missing_data = df.isnull().sum()

missing_data = missing_data[missing_data > 0]

if len(missing_data):

    fig = px.bar(
        x=missing_data.index,
        y=missing_data.values,
        labels={
            "x": "Columns",
            "y": "Missing Values"
        },
        title="Missing Values per Column"
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

    st.success("🎉 No missing values found.")

# ===================================================
# DATASET SUMMARY
# ===================================================

st.markdown("---")

st.markdown("## 📋 Dataset Summary")

summary = pd.DataFrame({
    "Data Type": df.dtypes,
    "Missing": df.isnull().sum(),
    "Unique Values": df.nunique()
})

st.dataframe(
    summary,
    use_container_width=True
)

# ===================================================
# QUICK INSIGHTS
# ===================================================

st.markdown("---")

st.markdown("## 🤖 Quick Insights")

insights = []

insights.append(f"📄 Dataset contains **{rows:,} rows** and **{cols} columns**.")

insights.append(f"✨ Data quality score: **{quality}%**.")

if missing == 0:
    insights.append("✅ No missing values detected.")
else:
    insights.append(f"⚠ Dataset contains **{missing}** missing values.")

if numeric_cols:
    insights.append(
        f"📊 Numeric columns available: **{len(numeric_cols)}**"
    )

if categorical_cols:
    insights.append(
        f"🏷 Categorical columns available: **{len(categorical_cols)}**"
    )

for item in insights:
    st.markdown(f"- {item}")

# ===================================================
# DOWNLOAD DATASET
# ===================================================

st.markdown("---")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Current Dataset",
    csv,
    file_name="InsightIQ_Dataset.csv",
    mime="text/csv"
)