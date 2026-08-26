import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(
    page_title="Spotify Popularity Predictor",
    page_icon="🎵",
    layout="wide"
)

# App Title & Description
st.title("🎵 Spotify Track Popularity Predictor")
st.markdown("""
Predict the estimated **Popularity Score (0–100)** of an upcoming track based on its intrinsic audio features and release metadata.
""")

# Load trained pipeline
@st.cache_resource
def load_model():
    return joblib.load('data/spotify_rf_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}. Please ensure 'spotify_rf_model.pkl' exists in the 'data/' directory.")
    st.stop()

# Layout: Sidebar Controls
st.sidebar.header("🎛️ Track Metadata")

genre = st.sidebar.selectbox(
    "Genre",
    ['Pop', 'Rock', 'Hip-Hop', 'EDM', 'R&B', 'Latin', 'Indie', 'Folk', 'Jazz', 'Reggaeton']
)
key_name = st.sidebar.selectbox(
    "Musical Key",
    ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
)
mode_name = st.sidebar.radio("Modality", ['Major', 'Minor'], horizontal=True)
release_day = st.sidebar.selectbox(
    "Release Day of Week",
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)
is_explicit = st.sidebar.checkbox("Explicit Lyrics", value=False)
is_weekend = release_day in ['Saturday', 'Sunday']

# Main Controls
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎼 Acoustic Signatures")
    danceability = st.slider("Danceability", 0.0, 1.0, 0.65, 0.01)
    energy = st.slider("Energy", 0.0, 1.0, 0.70, 0.01)
    loudness = st.slider("Loudness (dB)", -30.0, 0.0, -6.5, 0.5)
    instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.05, 0.01)
    upbeat_score = (danceability + energy) / 2

with col2:
    st.subheader("⏱️ Temporal & Structural Metrics")
    tempo = st.number_input("Tempo (BPM)", min_value=50.0, max_value=220.0, value=120.0, step=1.0)
    duration_min = st.number_input("Duration (Minutes)", min_value=0.5, max_value=15.0, value=3.2, step=0.1)
    release_year = st.slider("Release Year", 2015, 2026, 2026)
    release_month = st.slider("Release Month", 1, 12, 8)
    artist_tracks = st.number_input("Artist Catalog Size (Tracks)", min_value=1, max_value=500, value=10)

# Prediction Section
st.markdown("---")
if st.button("🚀 Predict Track Popularity", type="primary", use_container_width=True):
    input_data = pd.DataFrame([{
        'danceability': danceability,
        'energy': energy,
        'loudness': loudness,
        'instrumentalness': instrumentalness,
        'tempo': tempo,
        'duration_minutes': duration_min,
        'release_year': release_year,
        'release_month': release_month,
        'upbeat_score': upbeat_score,
        'artist_track_count': artist_tracks,
        'genre': genre,
        'key_name': key_name,
        'mode_name': mode_name,
        'release_day_of_week': release_day,
        'is_explicit_bool': int(is_explicit),
        'is_weekend_release': int(is_weekend)
    }])

    prediction = model.predict(input_data)[0]
    prediction = np.clip(prediction, 0, 100)

    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(label="Estimated Popularity Score", value=f"{prediction:.1f} / 100")
    
    with res_col2:
        tier = "🔥 High Potential Hit" if prediction >= 75 else ("📈 Mainstream Contender" if prediction >= 50 else "💿 Catalog / Niche Track")
        st.metric(label="Commercial Tier", value=tier)

    with res_col3:
        st.metric(label="Upbeat Score", value=f"{upbeat_score:.2f}")

    st.info("💡 **Analytical Insight:** Audio characteristics provide the baseline profile, but final streaming velocity relies heavily on marketing spend, algorithmic recommendation engines, and editorial playlist positions.")
