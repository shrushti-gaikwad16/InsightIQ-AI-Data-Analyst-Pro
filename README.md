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

##  Screenshots
<img width="1913" height="917" alt="Screenshot 2026-08-06 010204" src="https://github.com/user-attachments/assets/7774b845-296f-4335-b758-53f5c8763609" />
<img width="1913" height="906" alt="Screenshot 2026-08-06 010223" src="https://github.com/user-attachments/assets/aa9c90b0-ee1a-47ac-b2ba-8059125dbd96" />
<img width="1912" height="917" alt="Screenshot 2026-08-06 010241" src="https://github.com/user-attachments/assets/4aa82348-bcf1-4e37-8e08-3e3564ea48e8" />
<img width="1907" height="910" alt="Screenshot 2026-08-06 010306" src="https://github.com/user-attachments/assets/860ee22e-3c9f-4a6f-9a62-3458a719c463" />
<img width="1910" height="911" alt="Screenshot 2026-08-06 010326" src="https://github.com/user-attachments/assets/2c0cc693-3d00-47dc-b173-d3f6bc376356" />
<img width="1916" height="921" alt="Screenshot 2026-08-06 010344" src="https://github.com/user-attachments/assets/bcee757f-3ce1-48da-bf1d-dc4e95e3bc98" />
<img width="1912" height="902" alt="Screenshot 2026-08-06 010414" src="https://github.com/user-attachments/assets/844d5027-012d-4c95-a822-5edb90a35c78" />
<img width="1917" height="911" alt="Screenshot 2026-08-06 010427" src="https://github.com/user-attachments/assets/ddd19452-45e5-44ae-ab8f-84f9241141ad" />
<img width="1912" height="912" alt="Screenshot 2026-08-06 010443" src="https://github.com/user-attachments/assets/3c2f38f9-9cce-4dbf-bbc7-76ef9fa9efce" />
<img width="1903" height="907" alt="Screenshot 2026-08-06 010501" src="https://github.com/user-attachments/assets/ff716dc2-465f-419b-87cc-56b9f64ce0ff" />
<img width="1912" height="912" alt="Screenshot 2026-08-06 010526" src="https://github.com/user-attachments/assets/32d67b82-9a19-4de3-a86e-6a17c598c286" />
<img width="1897" height="908" alt="Screenshot 2026-08-06 010512" src="https://github.com/user-attachments/assets/0ba20578-8dd9-4559-8a8e-bb76c3ed4fda" />
<img width="1906" height="902" alt="Screenshot 2026-08-06 010541" src="https://github.com/user-attachments/assets/863cd00f-8818-4791-a97f-e37191c68923" />
<img width="1912" height="912" alt="Screenshot 2026-08-06 010554" src="https://github.com/user-attachments/assets/c0f442dc-eba4-4e40-a35f-66c67a6bef83" />
<img width="1910" height="911" alt="Screenshot 2026-08-06 010608" src="https://github.com/user-attachments/assets/0bd4a548-abab-47fc-9469-dc8060a46cee" />
<img width="1885" height="912" alt="Screenshot 2026-08-06 010620" src="https://github.com/user-attachments/assets/aad1064d-d120-48c4-bff8-0a7debb4bf1e" />
<img width="1907" height="906" alt="Screenshot 2026-08-06 010632" src="https://github.com/user-attachments/assets/422a3c0b-72d7-4d0b-9c19-21c85c9d5d27" />
<img width="1908" height="906" alt="Screenshot 2026-08-06 010648" src="https://github.com/user-attachments/assets/a9a6869c-03f4-4939-862f-f07b76db5133" />
<img width="1903" height="903" alt="Screenshot 2026-08-06 010700" src="https://github.com/user-attachments/assets/c65b7759-bb1b-407e-994e-03bc8a6c5421" />
<img width="1913" height="900" alt="Screenshot 2026-08-06 010719" src="https://github.com/user-attachments/assets/5b286386-7dd4-41f9-8d3e-455f623dbc38" />
<img width="1905" height="911" alt="Screenshot 2026-08-06 010735" src="https://github.com/user-attachments/assets/1c74e801-15a7-45c8-be44-47ad7645cb1f" />







