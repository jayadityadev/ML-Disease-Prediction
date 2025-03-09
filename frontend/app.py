# frontend/app.py
# Streamlit web app for disease prediction

import streamlit as st
import pickle
import numpy as np
import sys
import os

# Add parent directory to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(BASE_DIR, "..")))  # Ensures it’s first in path

from utils.predict import predict_disease

# Set app title and icon
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")
st.title("⚕️ Disease Prediction System")
st.markdown("---")  # Optional: Adds a horizontal line for better UI


# Hide Streamlit default UI elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Construct the absolute path for models
MODEL_PATHS = {
    "diabetes": os.path.abspath("models/diabetes_model.sav"),
    "heart_disease": os.path.abspath("models/heart_disease_model.sav"),
    "lung_cancer": os.path.abspath("models/lungs_disease_model.sav"),
    "parkinsons": os.path.abspath("models/parkinsons_model.sav"),
    "thyroid": os.path.abspath("models/thyroid_model.sav"),
}

# Load models dynamically
models = {}
for disease, path in MODEL_PATHS.items():
    try:
        with open(path, "rb") as file:
            models[disease] = pickle.load(file)
    except FileNotFoundError:
        print(f"Warning: Model file not found for {disease} at {path}")


# Create a dropdown menu for disease selection
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes', 'Heart Disease', 'Parkinson\'s', 'Lung Cancer', 'Thyroid']
)

def display_input(label, key, type="number"):
    return st.number_input(label, key=key, step=1) if type == "number" else st.text_input(label, key=key)

# Input sections for each disease
if selected == 'Diabetes':
    st.title('Diabetes Prediction')
    Pregnancies = int(display_input('Number of Pregnancies', 'Pregnancies'))
    Glucose = display_input('Glucose Level', 'Glucose')
    BloodPressure = display_input('Blood Pressure', 'BloodPressure')
    SkinThickness = display_input('Skin Thickness', 'SkinThickness')
    Insulin = display_input('Insulin Level', 'Insulin')
    BMI = display_input('BMI Value', 'BMI')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function', 'DiabetesPedigreeFunction')
    Age = int(display_input('Age', 'Age'))

    if st.button('Predict Diabetes Risk'):
        probability, risk_level = predict_disease(models['diabetes'], [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        st.success(f'Risk Level: {risk_level} ({probability * 100:.2f}% probability)')

elif selected == 'Heart Disease':
    st.title('Heart Disease Prediction')
    Age = int(display_input('Age', 'Age'))
    Sex = int(display_input('Sex (1=Male, 0=Female)', 'Sex'))
    Cp = display_input('Chest Pain Type', 'Cp')
    Trestbps = display_input('Resting Blood Pressure', 'Trestbps')
    Chol = display_input('Serum Cholesterol', 'Chol')
    Fbs = display_input('Fasting Blood Sugar', 'Fbs')
    Restecg = display_input('Resting Electrocardiographic Results', 'Restecg')
    Thalach = display_input('Maximum Heart Rate Achieved', 'Thalach')
    Exang = display_input('Exercise Induced Angina', 'Exang')
    Oldpeak = display_input('ST Depression', 'Oldpeak')
    Slope = display_input('Slope of the Peak Exercise', 'Slope')
    Ca = display_input('Number of Major Vessels', 'Ca')
    Thal = display_input('Thalassemia Type', 'Thal')

    if st.button('Predict Heart Disease Risk'):
        probability, risk_level = predict_disease(models['heart_disease'], [Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal])
        st.success(f'Risk Level: {risk_level} ({probability * 100:.2f}% probability)')

elif selected == "Parkinson's":
    st.title("Parkinson's Disease Prediction")

    # Parkinson's dataset feature names (excluding 'name' and 'status')
    parkinsons_features = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
        "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
        "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
    ]

    # Collect user inputs for all 22 features
    features = [float(display_input(feature, feature)) or 0 for feature in parkinsons_features]

    if st.button("Predict Parkinson's Risk"):
        probability, risk_level = predict_disease(models['parkinsons'], features)
        st.success(f'Risk Level: {risk_level} ({probability * 100:.2f}% probability)')

elif selected == 'Lung Cancer':
    st.title('Lung Cancer Prediction')
    Gender = int(display_input('Gender (1=Male, 0=Female)', 'Gender'))
    Age = int(display_input('Age', 'Age'))
    Smoking = int(display_input('Smoking (1=Yes, 0=No)', 'Smoking'))
    Yellow_Fingers = int(display_input('Yellow Fingers (1=Yes, 0=No)', 'Yellow_Fingers'))
    Anxiety = int(display_input('Anxiety (1=Yes, 0=No)', 'Anxiety'))
    Peer_Pressure = int(display_input('Peer Pressure (1=Yes, 0=No)', 'Peer_Pressure'))
    Chronic_Disease = int(display_input('Chronic Disease (1=Yes, 0=No)', 'Chronic_Disease'))
    Fatigue = int(display_input('Fatigue (1=Yes, 0=No)', 'Fatigue'))
    Allergy = int(display_input('Allergy (1=Yes, 0=No)', 'Allergy'))
    Wheezing = int(display_input('Wheezing (1=Yes, 0=No)', 'Wheezing'))
    Alcohol_Consuming = int(display_input('Alcohol Consumption (1=Yes, 0=No)', 'Alcohol_Consuming'))
    Coughing = int(display_input('Coughing (1=Yes, 0=No)', 'Coughing'))
    Shortness_of_Breath = int(display_input('Shortness of Breath (1=Yes, 0=No)', 'Shortness_of_Breath'))
    Swallowing_Difficulty = int(display_input('Swallowing Difficulty (1=Yes, 0=No)', 'Swallowing_Difficulty'))
    Chest_Pain = int(display_input('Chest Pain (1=Yes, 0=No)', 'Chest_Pain'))

    if st.button('Predict Lung Cancer Risk'):
        probability, risk_level = predict_disease(models['lung_cancer'], [Gender, Age, Smoking, Yellow_Fingers, Anxiety, Peer_Pressure, Chronic_Disease, Fatigue, Allergy, Wheezing, Alcohol_Consuming, Coughing, Shortness_of_Breath, Swallowing_Difficulty, Chest_Pain])
        st.success(f'Risk Level: {risk_level} ({probability * 100:.2f}% probability)')

elif selected == 'Thyroid':
    st.title('Thyroid Disease Prediction')
    Age = int(display_input('Age', 'Age'))
    Sex = int(display_input('Sex (1=Male, 0=Female)', 'Sex'))
    On_Thyroxine = int(display_input('On Thyroxine (1=Yes, 0=No)', 'On_Thyroxine'))
    TSH = display_input('TSH Level', 'TSH')
    T3_Measured = display_input('T3 Measured (1=Yes, 0=No)', 'T3_Measured')
    T3 = display_input('T3 Level', 'T3')
    TT4 = display_input('TT4 Level', 'TT4')

    if st.button('Predict Thyroid Risk'):
        probability, risk_level = predict_disease(models['thyroid'], [Age, Sex, On_Thyroxine, TSH, T3_Measured, T3, TT4])
        st.success(f'Risk Level: {risk_level} ({probability * 100:.2f}% probability)')