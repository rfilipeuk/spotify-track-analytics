# Spotify Tracks Analytics — Exploratory Data Analysis (EDA)

# Spotify Tracks Analytics — End-to-End Data Analytics Pipeline

A multi-stage data analytics portfolio project exploring an 85,000-record Spotify catalogue. Covers exploratory data analysis (EDA), relational schema design (SQLite), and analytical SQL querying.

---

## 📌 Project Stages & Architecture
* **Stage 1: Exploratory Data Analysis (EDA)** — Cleaned and validated schema (0 nulls, 0 duplicates), analysed acoustic distributions, and evaluated correlation structures.
* **Stage 2: Relational Data Modelling & Advanced SQL** — Structured normalised 3NF star-schema tables (`dim_labels`, `dim_genres`, `fact_tracks`) and executed business queries using CTEs and Window Functions.

---

## 📊 Key Findings & Analytics Insights
* **Target Distribution:** Popularity scores follow a near-normal distribution centred around ~48 points, showing that breakout viral tracks (>80 popularity) represent a tiny fraction of the catalogue.
* **Linear Feature Independence:** Standalone acoustic features (`danceability`, `energy`, `tempo`, `loudness`) show near-zero linear correlation with popularity scores, proving that popularity cannot be modelled using simple linear relationships.
* **Streaming Relationship:** Moderate positive correlation (0.36) between stream volume and popularity scores.
* ** Catalogue Efficiency (SQL):** Aggregated hit-to-catalogue ratios reveal that major labels maintain consistent average popularity, while specific niche labels achieve higher density of high-popularity tracks ($\ge 75$).

---

## 🗄️ Database Schema & SQL Highlights
* **Relational Normalisation:** Denormalised flat data split into dimension tables (`dim_labels`, `dim_genres`) and a centralised metrics fact table (`fact_tracks`) with foreign key constraints and query indexes.
* **Intra-Genre Rankings:** Leveraged `ROW_NUMBER() OVER(PARTITION BY genre ORDER BY stream_count DESC)` to isolate top-performing catalog assets.
* **Conditional Metrics:** Calculated label hit density via `SUM(CASE WHEN popularity >= 75 THEN 1.0 ELSE 0.0 END) / COUNT(*)`.

---
## 📁 Repository Structure
```text
spotify-track-analytics/
├── data/                      # Processed dataset & SQLite warehouse
├── notebooks/                 # Executable Jupyter Notebooks
│   ├── 01_exploratory_analysis.ipynb
│   └── 02_relational_sql_analysis.ipynb
├── .gitignore                 # Exclusion rules (venv, .db, checkpoints)
├── README.md                  # Project documentation
└── requirements.txt           # Environment dependencies
```

## 🚀 How to Run Locally

Follow these steps to reproduce this analysis in your local environment:

```bash
# 1. Clone the repository
git clone [https://github.com/rfilipeuk/spotify-track-analytics.git](https://github.com/rfilipeuk/spotify-track-analytics.git)
cd spotify-track-analytics

# 2. Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Open Jupyter Notebook
jupyter notebook
