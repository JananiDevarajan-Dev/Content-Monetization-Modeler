import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64
from sklearn.preprocessing import LabelEncoder

# --- Load saved objects ---
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
X_train_columns = joblib.load("X_train_columns.pkl")
#label_encoders = joblib.load("encoder.pkl")  # single pickle containing all LabelEncoders

# Path to your local image (adjust if needed)
image_path = "F:/Python_WC/Content Monetization Modeler/images/youtubeapp.png"
# Read and encode image to base64
with open(image_path, "rb") as f:
    data = f.read()
encoded = base64.b64encode(data).decode()

# ----- PAGE CONFIG -----
st.set_page_config(page_title="YouTube Ad Revenue Dashboard", page_icon="🎬", layout="wide")

# ----- HEADER -----
st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; gap: 10px;">
        <img src="data:image/png;base64,{encoded}" alt="YouTube Logo" width="60">
        <h1 style="margin: 0;">YouTube Ad Revenue Predictor</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<hr>", unsafe_allow_html=True)
# ----- LAYOUT -----
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    views = st.number_input("👁️ Views", min_value=0)
with col2:
    watch_time_minutes = st.number_input("⏱️ Watch Time (minutes)", min_value=0.0)
with col3:
    category = st.selectbox("📊 Category", ["Entertainment", "Gaming", "Lifestyle", "Music", "Tech", "Education"])

with col4:
    likes = st.number_input("❤️ Likes", min_value=0)
with col5:
    video_length_minutes = st.number_input("🎬 Video Length (minutes)", min_value=0.0)
with col6:
    device = st.selectbox("💻 Device", ["Mobile", "TV", "Tablet", "Desktop"])

col7, col8, col9 = st.columns(3)
with col7:
    comments = st.number_input("💬 Comments", min_value=0)
with col8:
    subscribers = st.number_input("👥 Subscribers", min_value=0)
with col9:
    country = st.selectbox("🌍 Country", ["CA", "DE", "IN", "UK", "US","AU"])

st.markdown("<hr>", unsafe_allow_html=True)

# ----- METRICS -----
engagement_rate = (comments / views) if views > 0 else 0
avg_view_duration = (watch_time_minutes / views) if views > 0 else 0
avg_percent_watched = (avg_view_duration / video_length_minutes * 100) if video_length_minutes > 0 else 0
avg_percent_watched = round(avg_percent_watched, 2)
#engagement_rate = (likes + comments) / views if views > 0 else 0
st.write("### 📈 Engagement Metrics")

m1, m2, m3 = st.columns(3)
m1.metric("Engagement Rate", f"{engagement_rate:.4f}")
m2.metric("Views", f"{views:,}")
m3.metric("Subscribers", f"{subscribers:,}")

st.markdown("<hr>", unsafe_allow_html=True)

# --- Encode categorical features ---
# --- Safe Label Encoding ---
category_encoder = LabelEncoder()
device_encoder = LabelEncoder()
country_encoder = LabelEncoder()

# Fit encoders on known classes (same order every time)
category_encoder.fit(["Entertainment", "Gaming", "Lifestyle", "Music", "Tech", "Education"])
device_encoder.fit(["Mobile", "TV", "Tablet", "Desktop"])
country_encoder.fit(["CA", "DE", "IN", "UK", "US", "AU"])

# Encode selected values
category_encoded = category_encoder.transform([category])[0]
device_encoded = device_encoder.transform([device])[0]
country_encoded = country_encoder.transform([country])[0]

# ----- PREDICTION -----
st.markdown("""
<style>
    .stButton>button {
        background-color: #1e40af;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.write("### 🤖 Revenue Prediction")
predict_button = st.button("💡 Predict Ad Revenue")

if predict_button:
    # Build input DataFrame
    input_dict = {
        'views': views,
        'likes': likes,
        'comments': comments,
        'watch_time_minutes': watch_time_minutes,
        'video_length_minutes': video_length_minutes,
        'subscribers': subscribers,
        'category': category_encoded,
        'device': device_encoded,
        'country': country_encoded,
        'engagement_rate': engagement_rate,
        'avg_view_duration': avg_view_duration,
        'avg_percent_watched': avg_percent_watched  
    }

    input_df = pd.DataFrame([input_dict])

    
    # --- Fill missing columns & reorder to match training data ---
    for col in X_train_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[X_train_columns]



    # --- Scale numeric features ---
    num_cols = ['views','likes','comments','watch_time_minutes','video_length_minutes','subscribers', 'category','device', 'country','engagement_rate','avg_view_duration','avg_percent_watched']
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    # --- Predict ---
    predicted_revenue = model.predict(input_df.values)[0]
    
    
    st.success(f"💰 **Predicted Ad Revenue: ${predicted_revenue:,.2f} USD**")
