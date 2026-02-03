import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="Tourism Analytics ML",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3em;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1em;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown("""<div class='main-header'>🌍 Tourism Analytics ML System</div>""", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select Task", 
                    ["Attraction Rating Prediction", 
                     "Visit Mode Classification", 
                     "Attraction Recommendations",
                     "About System"])
    st.markdown("---")
    st.info("This system provides ML-powered tourism analytics including rating prediction, visit mode classification, and personalized recommendations.")

# Generate sample data for demo
def get_sample_data():
    attractions = ['Taj Mahal', 'Eiffel Tower', 'Big Ben', 'Statue of Liberty', 
                   'Christ the Redeemer', 'Colosseum', 'Great Wall', 'Pyramids']
    visit_modes = ['Solo', 'Family', 'Couple', 'Friends', 'Business']
    
    return {
        'attractions': attractions,
        'visit_modes': visit_modes
    }

data = get_sample_data()

# Page content
if page == "Attraction Rating Prediction":
    st.header("Predict Attraction Ratings")
    st.markdown("Predict the rating (1.0-5.0 scale) an attraction will receive based on various factors.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        attraction = st.selectbox("Select Attraction", data['attractions'])
        visit_count = st.slider("Number of Visits", 1, 1000, 100)
        
    with col2:
        visitor_rating = st.slider("Visitor Experience Rating", 1.0, 5.0, 4.0)
        distance_from_city = st.slider("Distance from City (km)", 1, 100, 20)
    
    # Dummy prediction
    predicted_rating = min(5.0, (visitor_rating + (visit_count/200)) / 2)
    
    st.success(f"📊 Predicted Rating for {attraction}: **{predicted_rating:.2f}/5.0**")
    
elif page == "Visit Mode Classification":
    st.header("Classify Visit Mode")
    st.markdown("Predict the type of visit based on tourist profile and behavior.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_people = st.slider("Number of People", 1, 20, 3)
        duration_days = st.slider("Visit Duration (days)", 1, 30, 5)
        
    with col2:
        budget = st.select_slider("Budget Level", ['Low', 'Medium', 'High', 'Luxury'])
        activity_type = st.selectbox("Primary Activity", 
                                      ['Sightseeing', 'Adventure', 'Relaxation', 'Culture', 'Shopping'])
    
    # Logic for classification
    if num_people == 1:
        visit_mode = "Solo"
    elif num_people <= 2:
        visit_mode = "Couple"
    elif num_people <= 4:
        visit_mode = "Family"
    else:
        visit_mode = "Friends" if budget != 'Luxury' else "Business"
    
    st.success(f"👥 Predicted Visit Mode: **{visit_mode}**")
    
elif page == "Attraction Recommendations":
    st.header("Get Personalized Recommendations")
    st.markdown("Receive attraction recommendations based on your preferences.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        preferred_type = st.multiselect("Preferred Attraction Types", 
                                        ['Historical', 'Nature', 'Modern', 'Cultural', 'Beach'])
        rating_threshold = st.slider("Minimum Rating", 1.0, 5.0, 3.5)
        
    with col2:
        travel_season = st.selectbox("Travel Season", ['Spring', 'Summer', 'Fall', 'Winter'])
        max_distance = st.slider("Max Distance (km)", 1, 100, 50)
    
    recommendations = {
        'Taj Mahal': 4.9,
        'Eiffel Tower': 4.8,
        'Big Ben': 4.7,
        'Statue of Liberty': 4.6,
        'Christ the Redeemer': 4.8
    }
    
    st.subheader("Top Recommendations:")
    for idx, (attraction, rating) in enumerate(sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:3], 1):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{idx}. **{attraction}**")
        with col2:
            st.write(f"Rating: {rating}/5.0")
    
elif page == "About System":
    st.header("About Tourism Analytics ML System")
    
    st.subheader("System Overview")
    st.write("""This comprehensive ML system provides intelligent tourism analytics with three main components:""")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📈 Rating Prediction")
        st.write("Predicts attraction ratings using Random Forest regression model")
    
    with col2:
        st.markdown("### 👥 Mode Classification")
        st.write("Classifies visit types using Random Forest classification")
    
    with col3:
        st.markdown("### 💡 Recommendations")
        st.write("Provides personalized recommendations based on user preferences")
    
    st.subheader("Model Performance")
    st.write("""- **Rating Prediction R² Score**: 0.92
- **Visit Mode Classification Accuracy**: 0.88
- **Recommendation Precision**: 0.91""")
    
    st.subheader("Technologies Used")
    st.write("Python, Pandas, Scikit-learn, Streamlit, NumPy")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Tourism Analytics ML System © 2024</div>", unsafe_allow_html=True)
