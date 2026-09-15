import streamlit as st
import pandas as pd


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Upload Dataset | InsightIQ",
    page_icon="📂",
    layout="wide"
)



# ---------------- HEADER ----------------


st.markdown(
"""
<div class="page-header">

<h1>
📂 Upload Dataset
</h1>

<p>
Upload your CSV or Excel file and let InsightIQ
automatically analyze your data.
</p>

</div>

""",
unsafe_allow_html=True
)



# ---------------- UPLOAD CARD ----------------


st.markdown(
"""
<div class="upload-card">

<h2>
📁 Dataset Upload
</h2>

<p>
Supported formats:
<b>CSV, XLSX</b>
</p>

</div>

""",
unsafe_allow_html=True
)



uploaded_file = st.file_uploader(
    "",
    type=["csv","xlsx"]
)



if uploaded_file:


    with st.spinner(
        "🔄 Analyzing your dataset..."
    ):


        if uploaded_file.name.endswith(".csv"):

            df=pd.read_csv(uploaded_file)


        else:

            df=pd.read_excel(uploaded_file)



    st.success(
        "Dataset Loaded Successfully 🎉"
    )


    # Save dataframe

    st.session_state["dataset"]=df



    st.markdown(
    """
    <h2 class="section-title">
    Dataset Overview
    </h2>
    """,
    unsafe_allow_html=True
    )



    col1,col2,col3,col4=st.columns(4)


    cards=[
    ("📊","Rows",len(df)),
    ("📑","Columns",len(df.columns)),
    ("⚠️","Missing",df.isnull().sum().sum()),
    ("✨","Quality",
     str(round((1-(df.isnull().sum().sum()/(df.shape[0]*df.shape[1])))*100,2))+"%")
    ]



    for col,item in zip(
        [col1,col2,col3,col4],
        cards
    ):


        with col:

            st.markdown(
            f"""

            <div class="stat-card">

            <h2>
            {item[0]}
            </h2>

            <h1>
            {item[2]}
            </h1>


            <p>
            {item[1]}
            </p>


            </div>

            """,
            unsafe_allow_html=True
            )



    st.markdown(
    """
    <h2 class="section-title">
    Dataset Preview
    </h2>
    """,
    unsafe_allow_html=True
    )


    st.dataframe(
        df.head(10),
        use_container_width=True
    )



    st.info(
        "Next step: Go to Dashboard to explore deeper analytics."
    )