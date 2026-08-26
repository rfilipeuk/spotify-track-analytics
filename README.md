# Spotify Track Analytics & Predictive Modeling Pipeline

An end-to-end data science and data engineering portfolio project analysing ~85,000 Spotify tracks (2015–2025). This repository demonstrates exploratory data analysis (EDA), strategic business visualization, star schema relational database modeling, advanced SQLite warehousing, machine learning with target leakage prevention, and an interactive Streamlit inference web app.

---

## 🏗️ Repository Architecture

```text
spotify-track-analytics/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── raw/
│   │   └── spotify_data.csv
│   ├── spotify_data_processed.csv
│   ├── spotify_warehouse.db
│   └── spotify_rf_model.pkl
└── notebooks/
    ├── 01_exploratory_analysis.ipynb
    ├── 02_relational_sql_analysis.ipynb
    └── 03_predictive_modeling.ipynb
```

---

## 📊 Project Stages & Workflow

### Stage 1: Exploratory Data Analysis & Strategic Business Insights
* **Data Integrity & Audit:** Cleaned and validated ~85,000 records with zero missing values post-processing, standardising acoustic measurements and memory consumption.
* **Target & Correlation Analysis:** Evaluated popularity distributions (normally distributed around a mean of ~48.2) and verified near-zero linear collinearity across standalone acoustic attributes.
* **Core Business Analysis:**
  * **Artist Efficiency:** Mapped cumulative streams against catalogue volume to identify high-efficiency catalogue outliers.
  * **Genre Demand:** Visualised streaming concentration across commercial tiers versus niche categories.
  * **Content Dynamics:** Evaluated the statistical impact of explicit vs non-explicit content on streaming volume and popularity.
  * **Temporal Trends (2015–2025):** Analyzed multi-year consumption velocity and day-of-week release distributions.
  * **Hit vs Catalog Signatures:** Compared acoustic profiles between breakout hits ($\text{Popularity} \ge 75$) and catalog inventory.

### Stage 2: Star Schema Modelling & SQL Data Warehousing
* **Relational Normalization:** Structured flat data into an analytical Star Schema containing `dim_labels`, `dim_genres`, and `fact_tracks`.
* **Integrity & Index Optimisation:** Implemented `PRIMARY KEY` and `FOREIGN KEY` referential constraints alongside B-Tree indexes (`idx_tracks_popularity`, `idx_tracks_genre`) for sub-millisecond query execution.
* **Analytical Warehousing Queries:**
  * **Window Functions:** Ranked top 3 tracks per genre using `ROW_NUMBER() OVER(PARTITION BY genre_id ORDER BY stream_count DESC)`.
  * **Hit Rate Ratios:** Computed label conversion efficiency for tracks achieving $\text{Popularity} \ge 75$.
  * **Longitudinal Trends:** Evaluated decade-over-decade acoustic shifts and streaming volume using CTEs and relational joins.

### Stage 3: Predictive Modelling & Feature Importance
* **Target Leakage Prevention:** Identified and removed `log_stream_count` from predictors, preventing proxy-variable distortion and isolating intrinsic audio/metadata signals.
* **Pipeline Engineering:** Built Scikit-Learn pipelines integrating `ColumnTransformer`, `StandardScaler` for continuous acoustic metrics, and `OneHotEncoder` for categorical metadata.
* **Comparative Evaluation:** Evaluated a regularised linear baseline (`Ridge Regression`) against non-linear ensemble trees (`Random Forest Regressor`).
* **Feature Importance & Coefficients:** Extracted Gini importance scores and standardised beta coefficients, highlighting duration, tempo, loudness, and genre indicators.

### Stage 4: Interactive Dashboard Deployment
* Developed an interactive web application using **Streamlit** to allow real-time track popularity simulations based on customizable acoustic sliders, release timing, and metadata inputs.

---

## 💡 Key Findings & Strategic Insights

* **Target Leakage Identified:** Including stream counts artificially inflates model accuracy ($R^2 \approx 0.54$) because popularity is derived from streams. Removing it isolates the true impact of audio features.
* **Acoustic Limits vs External Drivers:** Audio traits alone (tempo, energy, loudness) hold very low predictive power, proving track success depends primarily on external factors like playlisting, marketing, and artist reach.
* **Even Feature Distribution:** Without stream leakage, predictive weight distributes evenly across duration (~12.5%), tempo (~12.5%), loudness (~12.2%), and instrumentalness (~11.0%).
* **Streaming Concentration:** While mean popularity remains steady across genres (~48 points), total stream volume is heavily concentrated in leading commercial genres with extreme right-tail outliers (>20M streams).

---

## 🚀 Quickstart & Reproduction

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rfilipeuk/spotify-track-analytics.git](https://github.com/rfilipeuk/spotify-track-analytics.git)
   cd spotify-track-analytics
   ```

2. **Set up virtual environment:**
   ```bash
   conda create -n spotify-env python=3.10 -y
   conda activate spotify-env
   pip install -r requirements.txt
   ```

3. **Run analytical notebooks:**
   ```bash
   jupyter notebook
   ```
   * `notebooks/01_exploratory_analysis.ipynb` — EDA & Business Visualizations
   * `notebooks/02_relational_sql_analysis.ipynb` — Star Schema & SQLite Warehousing
   * `notebooks/03_predictive_modeling.ipynb` — Machine Learning & Interpretability

4. **Launch interactive Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   Open `http://localhost:8501` in your browser to simulate track popularity in real time.
