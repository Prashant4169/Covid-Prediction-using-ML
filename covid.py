import streamlit as st
import joblib
import pandas as pd

model_rf = joblib.load("covid_prediction_random_forest.pkl")

st.title("COVID Prediction App")

Cough_symptoms = st.selectbox("Cough Symptoms", ["True", "False"])
Fever = st.selectbox("Fever", ["True", "False"])
Sore_throat = st.selectbox("Sore Throat", ["True", "False"])
Shortness_of_breath = st.selectbox("Shortness of Breath", ["True", "False"])
Headache = st.selectbox("Headache", ["True", "False"])
Age_60_above = st.selectbox("Age 60 Above", ["Yes", "No", "Unknown"])
Sex = st.selectbox("Sex", ["male", "female", "Unknown"])
Known_contact = st.selectbox("Known Contact", ["Other", "Abroad" , "Contact with confirmed"])

if st.button("Predict"):
    data = pd.DataFrame({
        "Cough_symptoms": [Cough_symptoms],
        "Fever": [Fever],
        "Sore_throat": [Sore_throat],
        "Shortness_of_breath": [Shortness_of_breath],
        "Headache": [Headache],
        "Age_60_above": [Age_60_above],
        "Sex": [Sex],
        "Known_contact": [Known_contact]
    })

    prediction = model_rf.predict(data)

    if prediction[0] == "positive":
        st.error("COVID Prediction: Positive")

    elif prediction[0] == "negative":
        st.success("COVID Prediction: Negative")

    else:
        st.warning("COVID Prediction: Other")