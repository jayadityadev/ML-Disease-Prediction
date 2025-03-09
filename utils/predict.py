# utils/predict.py
# This module loads trained models and predicts disease probabilities with risk levels.

import pickle
import numpy as np
from utils.risk_assessment import get_risk_level

# Load trained models
models = {
    'diabetes': pickle.load(open('models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('models/thyroid_model.sav', 'rb'))
}

def predict_disease(model, input_data):
    """
    Predicts disease risk level using a trained model.

    Args:
    - model: The trained machine learning model.
    - input_data: A list or tuple of user inputs.

    Returns:
    - probability: Probability of having the disease.
    - risk_level: Low, Moderate, or High Risk classification.
    """
    # Convert input data to numpy array and reshape for prediction
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64).reshape(1, -1)

    # Predict probability
    probabilities = model.predict_proba(input_data_as_numpy_array)
    probability = probabilities[0][1]  # Probability of having the disease
    
    # Get risk level
    risk_level = get_risk_level(probability)

    return probability, risk_level
