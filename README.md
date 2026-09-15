#  AI Data Analyst Pro

### Intelligent Dataset Story Generator & Analytics Platform

AI Data Analyst Pro is an AI-powered data analytics platform designed to transform raw datasets into **interactive visualizations, automated data insights, and business-oriented summaries**.

The application combines **Python-based data processing, interactive visualization, Streamlit, and Generative AI/LLMs** to provide a unified analytics experience for exploring and understanding datasets.

---

##  Features

###  Dataset Analysis

* Upload CSV and Excel datasets
* Automatic dataset inspection and profiling
* Analyze rows, columns, data types, and missing values
* Identify numerical and categorical features
* Generate dataset health information

###  Interactive Analytics

* Automated KPI generation
* Interactive charts and visualizations
* Trend and distribution analysis
* Numerical and categorical data exploration
* Interactive Plotly visualizations

###  AI-Powered Insights

* Natural-language dataset analysis
* Automated business insights
* AI-generated analytical summaries
* LLM-powered interpretation of dataset patterns
* Prompt engineering for structured AI responses

###  Business Intelligence

* Identify important trends and patterns
* Generate business-oriented observations
* Convert analytical results into understandable summaries
* Combine traditional data analysis with Generative AI

###  Interactive Interface

* Modern Streamlit interface
* Interactive dashboard experience
* Organized analytics workflow
* Responsive and user-friendly design

---

##  Generative AI & LLM Integration

The platform integrates **Generative AI and Large Language Models (LLMs)** to enhance traditional data analytics.

The AI workflow can:

```text
Dataset
   ↓
Data Processing
   ↓
Statistical & Exploratory Analysis
   ↓
Visualization
   ↓
Prompt Engineering
   ↓
LLM Analysis
   ↓
Business Insights
```

This allows users to interact with dataset information using natural language and receive AI-generated analytical summaries.

---

##  Tech Stack

### Programming Language

* Python

### Data Analytics

* Pandas
* NumPy
* Scikit-learn

### Data Visualization

* Plotly
* Matplotlib

### Generative AI

* Large Language Models (LLMs)
* Generative AI APIs
* Prompt Engineering

### Application Framework

* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* Git & GitHub

---

##  Application Workflow

```text
                ┌─────────────────────┐
                │    Upload Dataset   │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │   Data Processing   │
                │  Pandas / NumPy     │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Dataset Profiling   │
                │ Health & Statistics │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │   Visualization     │
                │     Plotly          │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │   AI / LLM Analysis │
                │ Prompt Engineering  │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Business Insights   │
                │ & AI Summary        │
                └─────────────────────┘
```

---

##  Project Structure

```text
AI-Data-Analyst-Pro/
│
├── app.py
│
├── pages/
│   ├── Dashboard.py
│   ├── Visualizations.py
│   ├── AI_Insights.py
│   └── Reports.py
│
├── assets/
│   ├── images/
│   ├── css/
│   └── ...
│
├── utils/
│   ├── data_processing.py
│   ├── visualization.py
│   └── ...
│
├── requirements.txt
├── README.md
└── .gitignore
```

> The project structure may vary depending on the current implementation.

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/shrushti-gaikwad16/AI-Data-Analyst-Pro.git
```

### 2. Navigate to the project directory

```bash
cd AI-Data-Analyst-Pro
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  API Configuration

If Generative AI / LLM APIs are enabled, **do not store API keys directly in the source code or GitHub repository**.

For Streamlit applications, use Streamlit secrets:

```text
.streamlit/
└── secrets.toml
```

Example:

```toml
GEMINI_API_KEY = "your-api-key"
```

Keep the actual `secrets.toml` file out of GitHub by adding it to `.gitignore`.

---

##  Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

