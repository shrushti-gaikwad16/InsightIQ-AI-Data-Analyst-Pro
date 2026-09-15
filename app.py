import streamlit as st

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="InsightIQ - AI Data Analytics Platform",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------- LOAD CSS --------------------

def load_css():
    with open("css/style.css", "r") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">
            💜 InsightIQ
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <div class="sidebar-card">

        🚀 AI Data Analytics Platform

        <br><br>

        <b>Features</b>

        <br><br>

        📂 Upload Dataset

        <br>
        📊 Dashboard

        <br>
        📈 Visual Analytics

        <br>
        🤖 AI Insights

        <br>
        📄 Reports

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown("---")


    st.markdown(
        """
        <div class="sidebar-footer">

        Built With ❤️

        <br><br>

        Python  
        Streamlit  
        Plotly  
        Machine Learning  

        </div>
        """,
        unsafe_allow_html=True
    )



# -------------------- HERO SECTION --------------------


st.markdown(
"""
<div class="hero">


<div class="hero-content">


<h1>
InsightIQ
</h1>


<h2>
AI-Powered Data Analytics Platform
</h2>


<p>
Transform raw datasets into meaningful business intelligence.
Analyze, visualize and generate AI-powered insights instantly.
</p>


<div class="hero-buttons">

<div class="primary-btn">
🚀 Upload Dataset
</div>


<div class="secondary-btn">
Explore Features
</div>

</div>


</div>



<div class="dashboard-preview">


<div class="preview-title">
Dataset Intelligence
</div>


<div class="score">
92%
</div>


<p>
Data Quality Score
</p>



<div class="progress">
<div></div>
</div>



<div class="mini-card">

📊

<b>
20+ Visualizations
</b>

</div>


<div class="mini-card">

🤖

<b>
AI Insights Generated
</b>

</div>


<div class="mini-card">

📄

<b>
Professional Reports
</b>

</div>



</div>



</div>

""",
unsafe_allow_html=True
)



# -------------------- FEATURES --------------------


st.markdown(
"""
<h2 class="section-title">
Everything you need for Data Intelligence
</h2>
""",
unsafe_allow_html=True
)



col1,col2,col3 = st.columns(3)



features=[

("📂","Smart Dataset Upload",
"Upload CSV and Excel files with automatic analysis."),

("📊","Advanced Analytics",
"Generate interactive charts and statistics."),

("🤖","AI Insights",
"Understand your data with automated recommendations.")

]



for col,data in zip(
    [col1,col2,col3],
    features
):

    with col:

        st.markdown(
        f"""

        <div class="feature-card">

        <div class="icon">
        {data[0]}
        </div>


        <h3>
        {data[1]}
        </h3>


        <p>
        {data[2]}
        </p>


        </div>

        """,
        unsafe_allow_html=True
        )



# -------------------- STATS --------------------


st.markdown("<br>",unsafe_allow_html=True)


st.markdown(
"""
<h2 class="section-title">
Powerful Analytics Engine
</h2>
""",
unsafe_allow_html=True
)



a,b,c,d = st.columns(4)


stats=[

("📁","Unlimited","Datasets"),

("📈","20+","Charts"),

("🤖","AI","Insights"),

("📄","PDF","Reports")

]


for col,item in zip(
    [a,b,c,d],
    stats
):

    with col:

        st.markdown(
        f"""

        <div class="stat-card">

        <h2>
        {item[0]}
        </h2>

        <h1>
        {item[1]}
        </h1>

        <p>
        {item[2]}
        </p>


        </div>

        """,
        unsafe_allow_html=True
        )




# -------------------- HOW IT WORKS --------------------


st.markdown(
"""
<h2 class="section-title">
How InsightIQ Works
</h2>


<div class="workflow">


<div>
1️⃣ Upload Dataset
</div>


<div>
2️⃣ AI Analysis
</div>


<div>
3️⃣ Generate Insights
</div>


<div>
4️⃣ Export Reports
</div>


</div>


""",
unsafe_allow_html=True
)



# -------------------- FOOTER --------------------


st.markdown(
"""
<div class="footer">

💜 InsightIQ

<br>

Turning Data Into Decisions

<br><br>

Developed by Shrushti Gaikwad

</div>

""",
unsafe_allow_html=True
)