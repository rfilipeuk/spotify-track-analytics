# Spotify Tracks Analytics — End-to-End Data Analytics Pipeline

A multi-stage data analytics portfolio project exploring an 85,000-record Spotify catalogue. Covers exploratory data analysis (EDA), relational schema design (SQLite), and analytical SQL querying.

---

## 📊 Project Workflow
### Stage 1: Exploratory Data Analysis & Business Visualisations
* **Data Integrity & Audit:** Validated completeness across 85,000 records with 0 missing values post-cleaning, standardised descriptive statistics formatting, and inspected memory footprints.
* **Target & Correlation Analysis:** Evaluated track popularity distribution (normally distributed around a mean of ~48.2) and verified near-zero linear collinearity between standalone acoustic attributes and popularity scores.
* **Strategic Business Questions Answered:**
  * **Top Artist Volume & Efficiency:** Evaluated cumulative streams and identified efficiency outliers (streams per released track).
  * **Genre Streaming Demand:** Aggregated total streaming volume by genre to highlight commercial concentration versus niche categories.
  * **Content Impact:** Assessed the statistical distribution of explicit vs non-explicit content across stream tiers and popularity.
  * **Temporal Trends (2015–2025):** Mapped day-of-week release volume alongside multi-year streaming consumption curves.
  * **Hit vs Catalog Signatures:** Compared acoustic profiles between breakout hits ($\text{Popularity} \ge 75$) and catalog inventory.

### Stage 2: Relational Modelling & Advanced SQL Warehouse
* **Star Schema Implementation:** Normalised flat CSV records into an analytical relational schema (`dim_labels`, `dim_genres`, and `fact_tracks`).
* **Integrity & Index Optimisation:** Implemented `PRIMARY KEY`, `FOREIGN KEY` referential constraints, and optimised query execution times with B-tree indexes (`idx_tracks_popularity`, `idx_tracks_genre`).
* **Analytical Queries:**
  * **Window Functions:** Computed top 3 tracks per genre using `ROW_NUMBER() OVER(PARTITION BY genre_id ORDER BY stream_count DESC)`.
  * **Conditional Aggregations:** Evaluated label commercial efficiency and hit conversion ratios ($\text{Popularity} \ge 75$).
  * **Longitudinal Aggregations:** Analyzed acoustic trends and streaming evolutions post-2000 using CTEs and relational joins.
 
### Stage 3: Predictive Modelling & Feature Importance
* **Target Leakage Prevention:** Identified and removed `log_stream_count` from predictors, preventing proxy-variable distortion and isolating intrinsic audio/metadata signals.
* **Pipeline Engineering:** Built Scikit-Learn pipelines integrating `ColumnTransformer`, `StandardScaler` for continuous acoustic metrics, and `OneHotEncoder` for categorical metadata.
* **Comparative Evaluation:** Evaluated a regularised linear baseline (`Ridge Regression`) against non-linear ensemble trees (`Random Forest Regressor`).
* **Feature Importance & Coefficients:** Extracted Gini importance scores and standardised beta coefficients, highlighting duration, tempo, loudness, and genre indicators.

---

## 💡 Key Findings & Strategic Insights

* **Target Leakage Identified:** Including stream counts artificially inflates model accuracy ($R^2 \approx 0.54$) because popularity is derived from streams. Removing it isolates the true impact of audio features.
* **Acoustic Limits vs External Drivers:** Audio traits alone (tempo, energy, loudness) hold very low predictive power, proving track success depends primarily on external factors like playlisting, marketing, and artist reach.
* **Even Feature Distribution:** Without stream leakage, predictive weight distributes evenly across duration (~12.5%), tempo (~12.5%), loudness (~12.2%), and instrumentalness (~11.0%).
* **Streaming Concentration:** While mean popularity remains steady across genres (~48 points), total stream volume is heavily concentrated in leading commercial genres with extreme right-tail outliers (>20M streams).

---

## 🗄️ Database Schema & SQL Highlights
* **Relational Normalisation:** Denormalised flat data split into dimension tables (`dim_labels`, `dim_genres`) and a centralised metrics fact table (`fact_tracks`) with foreign key constraints and query indexes.
* **Intra-Genre Rankings:** Leveraged `ROW_NUMBER() OVER(PARTITION BY genre ORDER BY stream_count DESC)` to isolate top-performing catalog assets.
* **Conditional Metrics:** Calculated label hit density via `SUM(CASE WHEN popularity >= 75 THEN 1.0 ELSE 0.0 END) / COUNT(*)`.

---
## 🏗️ Repository Architecture
```text
spotify-track-analytics/
├── data/
│   ├── raw/
│   │   └── spotify_data.csv
│   ├── spotify_data_processed.csv
│   └── spotify_warehouse.db
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_relational_sql_analysis.ipynb
│   └── 03_predictive_modeling.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Quickstart

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rfilipeuk/spotify-track-analytics.git](https://github.com/rfilipeuk/spotify-track-analytics.git)
   cd spotify-track-analytics
   ```

2. **Set up Python environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run notebooks:**
   ```bash
   jupyter notebook
   ```
   * Open `notebooks/01_exploratory_analysis.ipynb` for EDA and business visual analysis.
   * Open `notebooks/02_relational_sql_analysis.ipynb` for star schema initialization and SQL queries.
   * Open `notebooks/03_predictive_modeling.ipynb` for ML pipelines and feature importance analysis.
