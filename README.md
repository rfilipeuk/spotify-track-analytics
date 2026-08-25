# Spotify Tracks Analytics — Exploratory Data Analysis (EDA)

Exploratory data analysis and statistical evaluation of an 85,000-record Spotify dataset across 33 acoustic, categorical, and streaming features.

---

## 📌 Project Overview
* **Objective:** Audit data integrity, analyse acoustic distributions, evaluate correlation structures, and identify streaming trends across genres and release dates.
* **Tech Stack:** Python 3.10+, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook.
* **Architecture:** 
  * Data Pipeline: Cleaned schema with 0 nulls and 0 duplicates across 85,000 rows.
  * Analytical Framework: Univariate distributions, bivariate correlations, and multi-variable segmentations.

---

## 📊 Key Findings & Business Insights
* **Target Distribution:** Popularity scores follow a near-normal distribution with a central tendency around ~48 points, showing that breakout viral tracks (>80 popularity) represent a tiny fraction of the catalogue.
* **Linear Feature Independence:** Standalone acoustic features (`danceability`, `energy`, `tempo`, `loudness`) show near-zero linear correlation with popularity scores, proving that popularity cannot be modeled using simple linear relationships.
* **Streaming Relationship:** Moderate positive correlation (0.36) between stream volume and popularity scores.
* **Metadata Uniformity:** Distribution across record labels, release days, and explicit flags is highly balanced, requiring non-linear models (e.g., Random Forest / XGBoost) for predictive modeling.

---

## 📁 Repository Structure
```text
spotify-track-analytics/
├── data/                      # Processed dataset
├── notebooks/                 # Executable Jupyter notebooks (EDA)
├── .gitignore                 # Exclusion rules (venv, checkpoints, system files)
├── README.md                  # Project documentation
└── requirements.txt           # Environment dependencies
```

##🚀 How to Run Locally
Follow these steps to reproduce this analysis in your local environment:

# 1. Clone the repository
git clone [https://github.com/rfilipeuk/spotify-track-analytics.git]
cd spotify-track-analytics

# 2. Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Open Jupyter Notebook
jupyter notebook notebooks/01_exploratory_analysis.ipynb
