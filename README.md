# COVID Prediction App

## Project Overview
This project predicts COVID-19 test results using Machine Learning.

## Dataset
- Total Records: 278,848
- Features:
  - Cough Symptoms
  - Fever
  - Sore Throat
  - Shortness of Breath
  - Headache
  - Age 60 Above
  - Sex
  - Known Contact

## Data Preprocessing
- Missing value handling
- Categorical feature encoding using One-Hot Encoding
- Train-Test Split

## Models Tested
1. Logistic Regression
2. Random Forest Classifier

## Final Model
Random Forest Classifier

## Performance
- Accuracy: ~75%
- Positive Recall: ~0.78

## Technologies Used
- Python
- Pandas
- Scikit-Learn
- Streamlit
- Joblib

## How to Run

```bash
pip install -r requirements.txt
python -m streamlit run covid.py
```