# Tourism Analytics ML System

🎯 **Complete machine learning pipeline for tourism analytics with rating prediction, visit mode classification, and attraction recommendations**

## Overview

This project implements a production-ready ML system that analyzes tourism data to:
- **Predict attraction ratings** (1.0-5.0 scale) using regression
- **Classify visit modes** (Solo, Family, Couple, Friends, Business) using classification
- **Recommend attractions** based on popularity and ratings
- **Provide interactive web app** using Streamlit

## Features

✅ **3 Trained ML Models**
- RandomForest Regression for rating prediction
- RandomForest Classification for visit mode prediction  
- Recommendation system with collaborative filtering

✅ **Complete Data Pipeline**
- 5,000 tourism transactions
- 1,000 users across 6 continents
- 150 attractions with detailed metadata
- Exploratory Data Analysis with visualizations

✅ **Interactive Web Application**
- Streamlit-based UI with sidebar inputs
- Real-time predictions and recommendations
- Professional metrics display
- EDA visualizations

✅ **Production Ready**
- All models saved and serialized
- Label encoders included
- Complete dataset for reference
- Comprehensive documentation

## Files Included

### Models (Trained & Ready to Use)
- `model_regression.joblib` - Rating prediction model
- `model_classification.joblib` - Visit mode classifier
- `le_dict_reg.joblib` - Regression label encoders
- `le_dict_clf.joblib` - Classification label encoders

### Data
- `item_stats.csv` - Attraction statistics (150 items)
- `tourism_data_full.csv` - Complete dataset (5,000 transactions)

### Application
- `streamlit_app.py` - Interactive web application
- `tourism_eda.png` - EDA visualizations
- `README.md` - This documentation

## Installation & Setup

### Requirements
- Python 3.7+
- pip or conda

### Step 1: Install Dependencies

```bash
pip install streamlit scikit-learn pandas numpy joblib
```

### Step 2: Download Files

Clone or download this repository:

```bash
git clone https://github.com/alwinappu/Tourism-Analytics-ML.git
cd Tourism-Analytics-ML
```

### Step 3: Run the Application

```bash
streamlit run streamlit_app.py
```

The web app will open automatically at `http://localhost:8501`

## Usage

### Using the Streamlit App

1. **Input Parameters** (in sidebar):
   - Visit Month (1-12)
   - Visit Year (2022-2025)
   - Your Continent
   - Attraction Continent
   - Attraction Type
   - Expected Rating (1.0-5.0)

2. **Click "Run Prediction"** button

3. **View Results**:
   - Predicted rating (1-5 scale)
   - Predicted visit mode
   - Top-5 recommended attractions
   - Location details

### Using Models Programmatically

```python
import joblib
import pandas as pd

# Load models
model_reg = joblib.load('model_regression.joblib')
model_clf = joblib.load('model_classification.joblib')
le_dict_reg = joblib.load('le_dict_reg.joblib')

# Prepare input
X = pd.DataFrame([{
    'VisitMonth': 6,
    'VisitYear': 2024,
    'Continent': 'Asia',
    'Region': 'Asia_Region_1',
    'AttractionType': 'Beach',
    'AttractionContinent': 'Asia'
}])

# Encode
for col in le_dict_reg.keys():
    X[col] = le_dict_reg[col].transform(X[col].astype(str))

# Predict
rating = model_reg.predict(X[le_dict_reg.keys()])[0]
print(f"Predicted Rating: {rating:.2f}")
```

## Model Performance

### Rating Regression
- **Algorithm**: RandomForestRegressor (100 trees)
- **Features**: 6 input features
- **Training Samples**: 4,000
- **Test Samples**: 1,000
- **Metrics**: R² Score, RMSE

### Visit Mode Classification
- **Algorithm**: RandomForestClassifier (100 trees, balanced class weights)
- **Classes**: 5 (Solo, Family, Couple, Friends, Business)
- **Features**: 6 input features
- **Training Samples**: 4,000
- **Test Samples**: 1,000
- **Metrics**: Accuracy, F1-Score (weighted)

### Recommendation System
- **Approach**: Popularity-based + Collaborative Filtering
- **Items**: 150 attractions
- **Output**: Top-N ranked attractions by mean rating

## Dataset

### Data Composition
- **Users**: 1,000 from 6 continents
- **Attractions**: 150 with type and location metadata
- **Transactions**: 5,000 with ratings (1.0-5.0) and visit modes
- **Features**: Visit month/year, geographic location, attraction type

### Data Statistics
- Average Rating: 3.86/5.0
- Date Range: 2022-2024
- Visit Modes: 5 categories (balanced distribution)
- Regions: 18 (3 per continent)

## EDA Visualizations

The project includes 4 professional visualizations:
1. **Visit Mode Distribution** - Bar chart of visit mode frequencies
2. **Rating Distribution** - Histogram of attraction ratings
3. **Top Attraction Types** - Horizontal bar chart of most popular types
4. **Average Rating by Continent** - Regional rating comparison

All visualizations saved in `tourism_eda.png`

## Deployment Options

### Option 1: Local Machine (Recommended for Testing)
```bash
streamlit run streamlit_app.py
```

### Option 2: Streamlit Cloud (Free Hosting)
1. Push repository to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Select this repository
4. Deploy automatically
5. Share public URL

### Option 3: Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app.py"]
```

## Technology Stack

- **ML Frameworks**: scikit-learn, pandas, numpy
- **Models**: RandomForest (regression & classification)
- **Web Framework**: Streamlit
- **Data Processing**: pandas, numpy
- **Serialization**: joblib
- **Visualization**: matplotlib, seaborn

## Project Structure

```
Tourism-Analytics-ML/
├── streamlit_app.py          # Main web application
├── model_regression.joblib   # Trained regression model
├── model_classification.joblib # Trained classification model
├── le_dict_reg.joblib        # Regression encoders
├── le_dict_clf.joblib        # Classification encoders
├── item_stats.csv            # Attraction recommendations data
├── tourism_data_full.csv     # Complete dataset
├── tourism_eda.png           # EDA visualizations
└── README.md                 # This file
```

## How Models Were Built

### Data Preparation
1. Generated realistic tourism dataset (1,000 users, 150 attractions, 5,000 transactions)
2. Feature engineering with geographic and temporal features
3. Label encoding for categorical variables
4. Train-test split (80-20)

### Model Training
1. **Regression Model**:
   - RandomForestRegressor with 100 trees
   - Trained on rating prediction task
   - Cross-validated and evaluated on test set

2. **Classification Model**:
   - RandomForestClassifier with 100 trees and balanced class weights
   - Trained on visit mode prediction task
   - Stratified split to maintain class distribution

3. **Recommendation System**:
   - Computed item statistics (mean rating, count)
   - Implemented collaborative filtering approach
   - Ranked attractions by popularity and ratings

## Model Inputs & Outputs

### Input Features (All Models)
1. `VisitMonth` (1-12)
2. `VisitYear` (2022-2025)
3. `Continent` (6 continents)
4. `Region` (18 regions)
5. `AttractionType` (8 types)
6. `AttractionContinent` (6 continents)

### Outputs
- **Regression**: Continuous rating (1.0-5.0)
- **Classification**: Visit mode category
- **Recommendation**: Top-5 attractions with ratings

## Performance Metrics

- **Regression R² Score**: Calculated on test set
- **Classification Accuracy**: Calculated on stratified test set
- **F1-Score (Weighted)**: For imbalanced class handling
- **Recommendation Quality**: Based on popularity and ratings

## Future Improvements

- [ ] Add LightGBM model for comparison
- [ ] Implement deep learning models (Neural Networks)
- [ ] Add user-based collaborative filtering
- [ ] Integrate with real tourism APIs
- [ ] Add temporal trend analysis
- [ ] Implement model versioning and MLOps
- [ ] Add A/B testing framework
- [ ] Create production monitoring dashboard

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - feel free to use this project for your own purposes.

## Author

**Created**: February 2026  
**Location**: Karavaloor, Kerala, India  
**Contact**: [GitHub: alwinappu](https://github.com/alwinappu)

## Acknowledgments

- scikit-learn for excellent ML tools
- Streamlit for beautiful web app framework
- The open-source community

## Support & Questions

If you have questions or issues:
1. Check the troubleshooting section
2. Review the code comments
3. Open an issue on GitHub
4. Create a discussion in the repository

---

**Made with ❤️ for tourism analytics enthusiasts**
